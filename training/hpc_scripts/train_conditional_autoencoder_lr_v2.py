import anndata as ad
import scanpy as sc
from sklearn.linear_model import LogisticRegression
from skopt import BayesSearchCV
from skopt.space import Real, Categorical
from custom_stopper import CustomStopper
from test_robustness_higher_dropout import test_robustness
from preprocess_data import prepare_adata
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
from sklearn.preprocessing import OneHotEncoder
import scipy.stats as stats
import pickle


# Load training data
adata = ad.read_h5ad('/home/woody/iwbn/iwbn133h/data/CellTypist_HumanCellAtlas_Merged_cleaned_refined_cell_types.h5ad')

# Preprocessing
adata = prepare_adata(adata, batch_key="Donor")

# Create train test split

# All Donors: ['621B', '637C', 'A35', 'A36', 'D496', 'D503']
donor_train = ['637C', 'A35', 'A36', 'D503', '2', '3', '4', '6']
donor_test = ['621B', 'D496', '7', '8']

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
#y_train = adata_train.obs['scumi-annotation']
#y_train = adata_train.obs['scumi_clean']
y_train = adata_train.obs['cell_type_final']

X_test = adata_test.to_df()
gene_names_test = adata_test.var_names
#y_test = adata_test.obs['scumi-annotation']
#y_test = adata_test.obs['scumi_clean']
y_test = adata_test.obs['cell_type_final']


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


class ScRNACVAEClassifier:
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



# Train DAE
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

# --- 4. FEATURE EXTRAKTION (LATENT SPACE) ---
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



# --- 5. AUTOMATISCHES HYPERPARAMETER-TUNING DER LOGISTIC REGRESSION ---
print("Starte automatische Hyperparametersuche auf dem Latent Space...")

# Basis-Modell definieren (feste Parameter, die du beibehalten willst)
base_logreg = LogisticRegression(
    solver='saga',
    max_iter=1000,
    class_weight='balanced',
)

# Suchraum (Distributionen) definieren, zentriert um deine bisherigen Favoriten
# stats.loguniform sucht effizient über mehrere Größenordnungen hinweg
param_distributions = {
    'C': stats.loguniform(1e-3, 2.0),          # Sucht z.B. zwischen 0.1 und 2.0 (dein Wert war ~0.35)
    'l1_ratio': [0.0, 0.5, 1.0],
    #'class_weight': ['balanced', None],
    'tol': stats.loguniform(1e-3, 1e-1)       # Sucht z.B. zwischen 0.001 und 0.1 (dein Wert war ~0.008)
}

# RandomizedSearch aufsetzen
# cv=3 bedeutet 3-fache Kreuzvalidierung auf den Trainings-Embeddings
tuned_classifier = RandomizedSearchCV(
    estimator=base_logreg,
    param_distributions=param_distributions,
    n_iter=50,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=10
)

# Die Suche wird auf den vom DAE extrahierten Features ausgeführt
tuned_classifier.fit(X_train_latent, y_train)

# Die besten gefundenen Hyperparameter ausgeben
print("\n--- TUNING FINISHED ---")
print(f"Beste Parameter: {tuned_classifier.best_params_}")
print(f"Bester CV-Score: {tuned_classifier.best_score_:.4f}")

# Das beste Modell automatisch für die Testdaten verwenden
best_model = tuned_classifier.best_estimator_
#best_model = LogisticRegression(C=0.2770278253617821, class_weight=None, l1_ratio=0.0, tol=0.0019489213147753446, solver='saga', max_iter=1000)
#best_model.fit(X_train_latent, y_train)
y_pred = best_model.predict(X_test_latent)

# Finale Evaluation
print("\n--- EVALUATION AUF DEN TESTDATEN ---")
print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.4f}\n")
print(f"Macro F1: {f1_score(y_test, y_pred, average='macro')}")
#print(classification_report(y_test, y_pred))


print("\n--- Robustness Evaluation ---")
robust_model = ScRNACVAEClassifier(
    cdae=cdae,
    classifier=best_model,
    scaler=scaler,
    num_donors=num_donors
)
# Compute model score and robustness
with open("master_feature_importance_interleaved_marker_genes.pkl", "rb") as f:
    feature_importance = pickle.load(f)

#feature_importance = feature_importance.sort_values('Importance', ascending=False)
robustness_results = test_robustness(
    robust_model,
    X_test,
    y_test,
    #"scumi-annotation",
    "scumi_clean",
    '/home/woody/iwbn/iwbn133h/data/human_immune_health_atlas/human_immune_health_atlas_full_annotated_fine_grained_cleaned.h5ad',
    feature_importance,
    log_to_console=True,
    log_to_file=False,
)

