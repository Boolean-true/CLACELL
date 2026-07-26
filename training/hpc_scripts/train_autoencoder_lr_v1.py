import anndata as ad
import scanpy as sc
from sklearn.linear_model import LogisticRegression
from skopt import BayesSearchCV
from skopt.space import Real, Categorical
from custom_stopper import CustomStopper
from test_robustness import test_robustness
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
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import RandomizedSearchCV
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

train_tensor = torch.tensor(X_train_scaled, dtype=torch.float32)
test_tensor = torch.tensor(X_test_scaled, dtype=torch.float32)

train_loader = DataLoader(TensorDataset(train_tensor), batch_size=128, shuffle=True)

# Define Denoising Autoencoder (DAE)
class DenoisingAutoencoder(nn.Module):
    def __init__(self, input_dim, latent_dim=50, noise_factor=0.2):
        super(DenoisingAutoencoder, self).__init__()
        self.noise_factor = noise_factor
        
        # Encoder
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(256, latent_dim),
            nn.BatchNorm1d(latent_dim),
            nn.ReLU()
        )
        
        # Decoder
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Linear(256, input_dim)
        )

    def forward(self, x):
        if self.training:
            noise = torch.randn_like(x) * self.noise_factor
            x_noisy = x + noise
        else:
            x_noisy = x
            
        latent = self.encoder(x_noisy)
        reconstructed = self.decoder(latent)
        return reconstructed, latent


class ScRNADAEClassifier:
    def __init__(self, dae, classifier, scaler=None):
        self.dae = dae
        self.classifier = classifier
        self.scaler = scaler

        # DAE permanent in den Evaluationsmodus versetzen (schaltet Rauschen ab)
        self.dae.eval()
        # Erkennen, ob das Modell auf CPU oder GPU liegt
        self.device = next(dae.parameters()).device

    def _transform_to_latent(self, X):
        # 1. Falls das Test-Skript eine Sparse-Matrix übergibt, in dichtes Array wandeln
        if hasattr(X, "toarray"):
            X = X.toarray()

        # 2. Gen-weise Skalierung anwenden (falls vorhanden)
        if self.scaler is not None:
            X = self.scaler.transform(X)

        # 3. In PyTorch Tensor konvertieren und auf das richtige Device schieben
        X_tensor = torch.tensor(X, dtype=torch.float32).to(self.device)

        # 4. Features durch den Encoder jagen
        with torch.no_grad():
            # Unser DAE-forward gibt (reconstructed, latent) zurück
            _, latent_tensor = self.dae(X_tensor)
            X_latent = latent_tensor.cpu().numpy()

        return X_latent

    def predict(self, X):
        # Daten transformieren (Skalierung + DAE-Encoder)
        X_latent = self._transform_to_latent(X)
        # Vorhersage über die optimierte Logistische Regression
        return self.classifier.predict(X_latent)

    def predict_proba(self, X):
        X_latent = self._transform_to_latent(X)
        return self.classifier.predict_proba(X_latent)


# Train DAE
input_dim = X_train_scaled.shape[1]
dae = DenoisingAutoencoder(input_dim=input_dim, latent_dim=128, noise_factor=0.3).to(device)

criterion = nn.MSELoss()
optimizer = optim.AdamW(dae.parameters(), lr=1e-3, weight_decay=1e-4)

num_epochs = 150
best_loss = float('inf')
patience_counter = 0
patience = 5
delta_loss = 0.0002
dae.train()

print("Start DAE Training...")
for epoch in range(num_epochs):
    epoch_loss = 0.0
    for batch in train_loader:
        inputs = batch[0].to(device)
        
        optimizer.zero_grad()
        # Forwardpass
        reconstructed, _ = dae(inputs)
        
        # Compute loss on reconstructed output and original input
        loss = criterion(reconstructed, inputs)
        
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item() * inputs.size(0)
        
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

# Feature Extraction using the trained DAE
dae.eval()
print("\nExtract robust features...")
with torch.no_grad():
    # Encode training data
    _, X_train_latent_torch = dae(train_tensor.to(device))
    X_train_latent = X_train_latent_torch.cpu().numpy()
    
    # Encode test data
    _, X_test_latent_torch = dae(test_tensor.to(device))
    X_test_latent = X_test_latent_torch.cpu().numpy()



# Hyperparametertuning
print("Starte automatische Hyperparametersuche auf dem Latent Space...")

base_logreg = LogisticRegression(
    solver='saga',
    max_iter=1000,
)

param_distributions = {
    'C': stats.loguniform(1e-3, 2.0),
    'l1_ratio': [0.0, 0.25, 0.5, 0.75, 1.0],
    'class_weight': ['balanced', None],
    'tol': stats.loguniform(1e-3, 1e-1)
}

# RandomizedSearch
tuned_classifier = RandomizedSearchCV(
    estimator=base_logreg,
    param_distributions=param_distributions,
    n_iter=50,
    cv=3,
    scoring='accuracy',
    n_jobs=-1,
    verbose=10
)

tuned_classifier.fit(X_train_latent, y_train)

print("\n--- TUNING FINISHED ---")
print(f"Beste Parameter: {tuned_classifier.best_params_}")
print(f"Bester CV-Score: {tuned_classifier.best_score_:.4f}")

# Das beste Modell automatisch für die Testdaten verwenden
best_model = tuned_classifier.best_estimator_
#best_model = LogisticRegression(C=0.3665682409386545, class_weight=None, l1_ratio=0.5, tol=0.09013945007365622, solver='saga', max_iter=1000)
#best_model.fit(X_train_latent, y_train)
y_pred = best_model.predict(X_test_latent)

# Finale Evaluation
print("\n--- EVALUATION AUF DEN TESTDATEN ---")
print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.4f}\n")
print(f"Macro F1: {f1_score(y_test, y_pred, average='macro')}")
#print(classification_report(y_test, y_pred))


print("\n--- Robustness Evaluation ---")
robust_model = ScRNADAEClassifier(
    dae=dae,
    classifier=best_model,
    scaler=scaler
)
# Compute model score and robustness
with open("master_feature_importance_interleaved_marker_genes.pkl", "rb") as f:
    feature_importance = pickle.load(f)

#feature_importance = feature_importance.sort_values('Importance', ascending=False)
test_robustness(robust_model, X_test, y_test, 'data/humancellatlas/5f29c29a-51c6-435c-8ff0-2b2a9d05ebee/BL_standard_design_annotated.h5ad', feature_importance)
