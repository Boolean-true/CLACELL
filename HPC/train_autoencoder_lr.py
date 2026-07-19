import anndata as ad
import scanpy as sc
from sklearn.linear_model import LogisticRegression
from skopt import BayesSearchCV
from skopt.space import Real, Categorical
from custom_stopper import CustomStopper
from test_robustness import compute_model_score_and_robustness
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
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import RandomizedSearchCV
import scipy.stats as stats


# Load training data
adata = ad.read_h5ad('/home/hpc/iwbn/iwbn133h/data/CellTypistDataset/global.h5ad')

# Filter blood data
adata = adata[adata.obs['Organ'] == 'BLD'].copy()
print(adata)


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

# Filter only highly variable genes
sc.pp.highly_variable_genes(adata)


# Normalization

# Saving count data
adata.layers["counts"] = adata.X.copy()

# Normalizing to median total counts
sc.pp.normalize_total(adata)
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

# Filtering classes with >=150 samples
y = adata.obs['Manually_curated_celltype']

min_samples = 150
class_counts = y.value_counts()
keep_classes = class_counts[class_counts >= min_samples].index

adata = adata[adata.obs["Manually_curated_celltype"].isin(keep_classes)].copy()


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
X_train = adata_train.X#.to_df()
gene_names_train = adata_train.var_names
y_train = adata_train.obs['Manually_curated_celltype']

X_test = adata_test.X#to_df()
gene_names_test = adata_test.var_names
y_test = adata_test.obs['Manually_curated_celltype']


# Autoencoder Training

# Setup
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

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

# Train DAE
input_dim = X_train_scaled.shape[1]
dae = DenoisingAutoencoder(input_dim=input_dim, latent_dim=50, noise_factor=0.3).to(device)

criterion = nn.MSELoss()
optimizer = optim.AdamW(dae.parameters(), lr=1e-3, weight_decay=1e-4)

num_epochs = 40
dae.train()

print("Start DAE Training...")
for epoch in range(num_epochs):
    epoch_loss = 0.0
    for batch in train_loader:
        inputs = batch[0].to(device)
        
        optimizer.zero_grad()
        # Vorwärtspass (gibt Rekonstruktion und Latent Space zurück)
        reconstructed, _ = dae(inputs)
        
        # Loss berechnet sich aus der Rekonstruktion vs. den ORGINALEN (unverrauschten) Daten
        loss = criterion(reconstructed, inputs)
        
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item() * inputs.size(0)
        
    total_epoch_loss = epoch_loss / len(train_loader.dataset)
    if (epoch + 1) % 10 == 0 or epoch == 0:
        print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {total_epoch_loss:.4f}")

# --- 4. FEATURE EXTRAKTION (LATENT SPACE) ---
dae.eval()
print("\Extract robust features...")
with torch.no_grad():
    # Trainingsdaten encodieren
    _, X_train_latent_torch = dae(train_tensor.to(device))
    X_train_latent = X_train_latent_torch.cpu().numpy()
    
    # Testdaten encodieren
    _, X_test_latent_torch = dae(test_tensor.to(device))
    X_test_latent = X_test_latent_torch.cpu().numpy()



# --- 5. AUTOMATISCHES HYPERPARAMETER-TUNING DER LOGISTIC REGRESSION ---
print("Starte automatische Hyperparametersuche auf dem Latent Space...")

model = LogisticRegression(max_iter=1000, solver='saga')

search_space = {
    'C': Real(1e-3, 2.0, prior='log-uniform'),
    'penalty': Categorical(['l1', 'l2']),
    'class_weight': Categorical(['balanced', None]),
    'tol': Real(1e-4, 1e-2, prior='log-uniform')
}

my_stopper = CustomStopper(patience=5, min_delta=0.002, min_iter=15) 

opt = BayesSearchCV(
    estimator=model,
    search_spaces=search_space,
    n_iter=10,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=10
)

print("Start BayesSearch with Early Stopping...")
opt.fit(X_train, y_train, callback=my_stopper)

print(f"\nSearch terminated after {len(opt.cv_results_['mean_test_score'])} Iterations.")
print(f"Best hyperparameters: {opt.best_params_}")
print(f"Test-Split Accuracy:  {opt.score(X_test, y_test):.4f}")

best_model =opt.best_estimator_
y_pred = best_model.predict(X_test_latent)

# Finale Evaluation
print("\n--- EVALUATION AUF DEN TESTDATEN ---")
print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.4f}\n")
print(classification_report(y_test, y_pred))

print("\n--- Robustness Evaluation ---")
# Compute model score and robustness
with open("feature_importance_logisticregression.pkl", "rb") as f:
    feature_importance = pickle.load(f)

feature_importance = feature_importance.sort_values('Importance', ascending=False)
compute_model_score_and_robustness(model, X_test, y_test, None, feature_importance)