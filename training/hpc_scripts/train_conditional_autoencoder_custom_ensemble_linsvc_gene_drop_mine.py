import anndata as ad
import scanpy as sc
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.calibration import CalibratedClassifierCV
from skopt import BayesSearchCV
from skopt.space import Real, Categorical
from custom_stopper import CustomStopper
from test_robustness_higher_dropout import test_robustness
import pickle
# For saving results on HPC Cluster
import joblib
import pandas as pd
import os
# Autoencoder
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.metrics import classification_report, accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import RandomizedSearchCV
from sklearn.preprocessing import OneHotEncoder
import scipy.stats as stats
import pickle


# Load training data
adata = ad.read_h5ad('/home/hpc/iwbn/iwbn133h/data/CellTypistDataset/CountAdded_PIP_global_object_for_cellxgene_annotated.h5ad')

# Filter blood data
adata = adata[adata.obs['Organ'] == 'BLD'].copy()
print(adata)

# Use raw data instead of already preprocessed data
adata.X = adata.layers['counts'].copy()


# Preprocessing

# mitochondrial genes, "MT-" for human, "Mt-" for mouse
adata.var["mt"] = adata.var_names.str.startswith("MT-")
# ribosomal genes
adata.var["ribo"] = adata.var_names.str.startswith(("RPS", "RPL"))
# hemoglobin genes
adata.var["hb"] = adata.var_names.str.contains("^HB[^(P)]")

sc.pp.calculate_qc_metrics(adata, qc_vars=["mt", "ribo", "hb"], inplace=True, log1p=True)

# Remove mitochondrial, ribosomal and hemoglobin
adata = adata[:, ~adata.var["mt"]].copy()
adata = adata[:, ~adata.var["ribo"]].copy()
adata = adata[:, ~adata.var["hb"]].copy()

# Doublet Detection
sc.pp.scrublet(adata, batch_key="Donor")
adata = adata[adata.obs['predicted_doublet'] == False].copy()


# Normalization

# Saving count data
adata.layers["counts"] = adata.X.copy()

# Normalizing to median total counts
sc.pp.normalize_total(adata, target_sum=1e4)
# Logarithmize the data
sc.pp.log1p(adata)

# Filtering Highly variable genes
print('Before filtering highly variable genes ---')
print(adata)

sc.pp.highly_variable_genes(adata, n_top_genes=10000)

# Apply filter
adata = adata[:, adata.var['highly_variable']].copy()

print('After filtering highly variable genes ---')
print(adata)

# Create train test split

# All Donors: ['621B', '637C', 'A35', 'A36', 'D496', 'D503']
donor_train = ['637C', 'A35', 'A36', 'D503']
donor_test = ['621B', 'D496']

adata_train = adata[
    adata.obs["Donor"].isin(donor_train)
].copy()

adata_test = adata[
    adata.obs["Donor"].isin(donor_test)
].copy()

# Check split
print(adata_train.obs['Donor'].unique())
print(adata_test.obs['Donor'].unique())

# Prepare Data for training
X_train = adata_train.to_df()
gene_names_train = adata_train.var_names
y_train = adata_train.obs['scumi-annotation']

X_test = adata_test.to_df()
gene_names_test = adata_test.var_names
y_test = adata_test.obs['scumi-annotation']


# Autoencoder Training

# Setup
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

if hasattr(X_train, "toarray"):
    X_train = X_train.toarray()
if hasattr(X_test, "toarray"):
    X_test = X_test.toarray()

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


donor_train = adata_train.obs['Donor']
donor_test = adata_test.obs['Donor']

oh_encoder = OneHotEncoder(sparse_output=False)
donor_train_oh = oh_encoder.fit_transform(donor_train.to_numpy().reshape(-1, 1))

num_donors = donor_train_oh.shape[1]
input_dim = X_train_scaled.shape[1]
latent_dim = 128


# Define Conditional Denoising Autoencoder (DAE)
class ConditionalDAE(nn.Module):
    def __init__(self, input_dim, num_donors, latent_dim=128, noise_factor=0.3):
        super(ConditionalDAE, self).__init__()

        self.noise_factor = noise_factor

        self.encoder = nn.Sequential(
            nn.Linear(input_dim + num_donors, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(256, latent_dim)
        )

        self.decoder = nn.Sequential(
            nn.Linear(latent_dim + num_donors, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(256, input_dim)
        )

    def forward(self, x, cond):
        if self.training:
            noise = torch.randn_like(x) * self.noise_factor
            x_noisy = x + noise
        else:
            x_noisy = x

        # Combine Gene data and Donor ID for the Encoder
        x_cond = torch.cat([x_noisy, cond], dim=1)
        latent = self.encoder(x_cond)

        # Combine Latent space and Donor ID for the Decoder
        latent_cond = torch.cat([latent, cond], dim=1)
        reconstructed = self.decoder(latent_cond)

        return reconstructed, latent


class ScRNACAEClassifier:
    def __init__(self, cdae, classifier, scaler, num_donors):
        self.cdae = cdae
        self.classifier = classifier
        self.scaler = scaler
        self.num_donors = num_donors
        self.cdae.eval()
        self.device = next(cdae.parameters()).device

    def _transform_to_latent(self, X):
        if hasattr(X, "toarray"):
            X = X.toarray()
        if self.scaler is not None:
            X = self.scaler.transform(X)
            
        X_tensor = torch.tensor(X, dtype=torch.float32).to(self.device)
        
        # DER TRICK: Da das Robustheitsskript keine Spender-IDs liefert, übergeben wir
        # einfach eine Matrix aus Nullen als "neutralen" Spender. Da der CVAE gelernt hat,
        # biologische Signale von Spendereffekten zu trennen, filtert er den Spund-Effekt raus.
        cond_dummy = torch.zeros((X_tensor.shape[0], self.num_donors), dtype=torch.float32).to(self.device)
        
        with torch.no_grad():
            _, latent_tensor = self.cdae(X_tensor, cond_dummy)
            X_latent = latent_tensor.cpu().numpy()
            
        return X_latent

    def predict(self, X):
        X_latent = self._transform_to_latent(X)
        return self.classifier.predict(X_latent)

    def predict_proba(self, X):
        X_latent = self._transform_to_latent(X)
        return self.classifier.predict_proba(X_latent)



# --- Training of the Conditional Autoencoder ---
input_dim = X_train_scaled.shape[1]
cdae = ConditionalDAE(input_dim, num_donors, latent_dim).to(device)

criterion = nn.MSELoss()
optimizer = optim.AdamW(cdae.parameters(), lr=1e-3, weight_decay=1e-4)

# Dataset & Loader (übergibt jetzt immer X UND den Spender-Vektor)
train_dataset = TensorDataset(
    torch.tensor(X_train_scaled, dtype=torch.float32),
    torch.tensor(donor_train_oh, dtype=torch.float32)
)
train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True)


num_epochs = 150
best_loss = float('inf')
patience_counter = 0
patience = 5
delta_loss = 0.0002
cdae.train()

print("Start Conditional DAE Training...")
for epoch in range(num_epochs):
    epoch_loss = 0.0
    for x_batch, cond_batch in train_loader:
        x_batch = x_batch.to(device)
        cond_batch = cond_batch.to(device)

        optimizer.zero_grad()
        reconstructed, latent = cdae(x_batch, cond_batch)

        # Verlust berechnen (Soll das Original ohne Rauschen rekonstruieren)
        loss = criterion(reconstructed, x_batch)
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item() * x_batch.size(0)
        
    total_epoch_loss = epoch_loss / len(train_loader.dataset)
    if (epoch + 1) % 10 == 0 or epoch == 0:
        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {total_epoch_loss:.4f}")
    
    # Early Stopping
    if total_epoch_loss < best_loss - delta_loss:
        best_loss = total_epoch_loss
        patience_counter = 0
    else:
        patience_counter += 1

    if patience_counter >= patience:
        print(f"Early Stopping after [{epoch+1}/{num_epochs}] Epochs!")
        break


# --- FEATURE EXTRAKTION (LATENT SPACE) ---
cdae.eval()
print("\nExtract robust features...")
with torch.no_grad():
    # Wir extrahieren die echten Trainings-Features mit den echten Spender-IDs
    X_train_tensor = torch.tensor(X_train_scaled, dtype=torch.float32).to(device)
    cond_train_tensor = torch.tensor(donor_train_oh, dtype=torch.float32).to(device)
    _, X_train_latent_tensor = cdae(X_train_tensor, cond_train_tensor)
    X_train_latent = X_train_latent_tensor.cpu().numpy()

    # Testdaten
    # Wir extrahieren die echten Trainings-Features mit den echten Spender-IDs
    X_test_tensor = torch.tensor(X_test_scaled, dtype=torch.float32).to(device)
    cond_test_tensor = torch.zeros((X_test_tensor.shape[0], num_donors), dtype=torch.float32).to(device)
    _, X_test_latent_tensor = cdae(X_test_tensor, cond_test_tensor)
    X_test_latent = X_test_latent_tensor.cpu().numpy()


# --- Hyperparametertuning of the LinearSVC on the latent space ---
print("Starte automatische Hyperparametersuche auf dem Latent Space...")

# Basis-Modell definieren (feste Parameter, die du beibehalten willst)
base_model = LinearSVC()

param_distributions = [
        {
    'C': Real(1e-3, 2.0, prior='log-uniform'),
    'penalty': Categorical(['l2']),
    'dual': Categorical([True, False]),
    'class_weight': Categorical(['balanced', None]),
    'tol': Real(1e-4, 1e-2, prior='log-uniform')
        },
        {
    'C': Real(1e-3, 2.0, prior='log-uniform'),
    'penalty': Categorical(['l1']),
    'dual': Categorical([False]),
    'class_weight': Categorical(['balanced', None]),
    'tol': Real(1e-4, 1e-2, prior='log-uniform')
        },
]
my_stopper = CustomStopper(patience=5, min_delta=0.002, min_iter=15)
opt = BayesSearchCV(
            estimator=base_model,
            search_spaces=param_distributions,
            n_iter=30,
            cv=5,
            scoring='accuracy',
            n_jobs=-1,
            verbose=10
        )

print("Start BayesSearch with Early Stopping...")
opt.fit(X_train_latent, y_train, callback=my_stopper)

print(f"\nSearch terminated after {len(opt.cv_results_['mean_test_score'])} Iterations.")
print(f"Best hyperparameters: {opt.best_params_}")
print(f"Test-Split Accuracy:  {opt.score(X_test_latent, y_test):.4f}")


# --- Start training the custom ensemble ---
with open("feature_importance_randomforest_10_000_genes_scumi_annotated.pkl", "rb") as f:
    feature_importance = pickle.load(f)

feature_importance = feature_importance.sort_values('Importance', ascending=False)
sorted_top_genes = feature_importance['Feature'].tolist()


total_genes = len(sorted_top_genes)

# Define subsets
drop_075_pct = int(total_genes * 0.0075)
drop_15_pct = int(total_genes * 0.015)
drop_25_pct = int(total_genes * 0.025)

# Compute Features for each subset
features_model_all = sorted_top_genes
features_model_minus_075 = sorted_top_genes[drop_075_pct:]
features_model_minus_15 = sorted_top_genes[drop_15_pct:]
features_model_minus_25 = sorted_top_genes[drop_25_pct:]


# Build Pipelines with ColumnTransformer
def make_pipeline(features_to_keep, model_name, model):
    preprocessor = ColumnTransformer(
        transformers=[('keep', 'passthrough', features_to_keep)],
        remainder='drop'
    )
    return Pipeline([
        ('select', preprocessor),
        (model_name, model)
    ])

model_params = opt.best_params_
model = CalibratedClassifierCV(LinearSVC(**model_params))
robust_model = ScRNACAEClassifier(
    cdae=cdae,
    classifier=model,
    scaler=scaler,
    num_donors=num_donors
)
pipe_all = make_pipeline(features_model_all, 'linsvc_all', robust_model)
pipe_minus_075 = make_pipeline(features_model_minus_075, 'linsvc_075', robust_model)
pipe_minus_15 = make_pipeline(features_model_minus_15, 'linsvc_15', robust_model)
pipe_minus_25 = make_pipeline(features_model_minus_25, 'linsvc_25', robust_model)

ensemble = VotingClassifier(
    estimators=[
        ('all_features', pipe_all),
        ('minus_075_pct', pipe_minus_075),
        ('minus_15_pct', pipe_minus_15),
        ('minus_25_pct', pipe_minus_25)
    ],
    voting='soft'
)
print("Train custom ensemble...")
ensemble.fit(X_train_latent, y_train)
#print(ensemble.score(X_test, y_test))


# Predict test data
y_pred = ensemble.predict(X_test_latent)

# Final Evaluation
print("\n--- EVALUATION AUF DEN TESTDATEN ---")
print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.4f}\n")
print(f"Macro F1: {f1_score(y_test, y_pred, average='macro')}")
#print(classification_report(y_test, y_pred))


print("\n--- Robustness Evaluation ---")
# Compute model score and robustness
with open("master_feature_importance_interleaved_marker_genes.pkl", "rb") as f:
    feature_importance = pickle.load(f)

#feature_importance = feature_importance.sort_values('Importance', ascending=False)
robustness_results = test_robustness(
    robust_model,
    X_test,
    y_test,
    "scumi-annotation",
    '/home/hpc/iwbn/iwbn133h/data/humancellatlas/5f29c29a-51c6-435c-8ff0-2b2a9d05ebee/BL_standard_design_annotated.h5ad',
    feature_importance,
    log_to_console=True,
    log_to_file=False,
)

