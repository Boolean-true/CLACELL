import anndata as ad
import scanpy as sc
import numpy as np
import pandas as pd
import os
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from sklearn.svm import LinearSVC
from sklearn.ensemble import VotingClassifier
from sklearn.calibration import CalibratedClassifierCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import accuracy_score, f1_score
from sklearn.base import BaseEstimator, ClassifierMixin
from skopt import BayesSearchCV
from skopt.space import Real, Categorical
import pickle
import joblib
import scipy.stats as stats

from custom_stopper import CustomStopper
from test_robustness_higher_dropout import test_robustness



# 1. Load training data
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

# 2. Create train test split

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
y_train = adata_train.obs['scumi-annotation']

X_test = adata_test.to_df()
y_test = adata_test.obs['scumi-annotation']

# Donor Encoding for the training
donor_train = adata_train.obs['Donor']
oh_encoder = OneHotEncoder(sparse_output=False)
donor_train_oh = oh_encoder.fit_transform(donor_train.to_numpy().reshape(-1, 1))

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 3. Architecture and Custom Wrapper
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

class SubsetCAELinearSVC(ClassifierMixin, BaseEstimator):
    """
    A class that encapsulates the entire pipeline of gene filtering, scaling, 
    training a Conditional Autoencoder (with Early Stopping), and performing 
    BayesSearchCV for LinearSVC on the latent space, all within a single 
    Scikit-Learn estimator.
    """
    _estimator_type = "classifier"

    def __init__(self, features_to_keep=None, donor_train_oh=None, device="cpu", latent_dim=128, num_epochs=150, name="Model"):
        self.features_to_keep = features_to_keep
        self.donor_train_oh = donor_train_oh
        self.device = device
        self.latent_dim = latent_dim
        self.num_epochs = num_epochs
        self.name = name
        
    def fit(self, X, y):
        print(f"\n--- Start training for Pipeline: {self.name} ---")
        # 1. Feature Subset
        X_subset = X.reindex(columns=self.features_to_keep, fill_value=0.0)
        X_vals = X_subset.values
        
        # 2. Scaling
        self.scaler = StandardScaler()
        X_scaled = self.scaler.fit_transform(X_vals)
        
        input_dim = X_scaled.shape[1]
        num_donors = self.donor_train_oh.shape[1]
        
        # 3. Autoencoder Setup & Training
        self.cdae = ConditionalDAE(input_dim, num_donors, self.latent_dim).to(self.device)
        optimizer = optim.AdamW(self.cdae.parameters(), lr=1e-3, weight_decay=1e-4)
        criterion = nn.MSELoss()
        
        train_dataset = TensorDataset(
            torch.tensor(X_scaled, dtype=torch.float32),
            torch.tensor(self.donor_train_oh, dtype=torch.float32)
        )
        train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True)
        
        self.cdae.train()
        best_loss = float('inf')
        patience_counter = 0
        patience = 5
        delta_loss = 0.0002
        
        print(f"[{self.name}] Train Conditional Autoencoder (Dim: {input_dim})...")
        for epoch in range(self.num_epochs):
            epoch_loss = 0.0
            for x_batch, cond_batch in train_loader:
                x_batch, cond_batch = x_batch.to(self.device), cond_batch.to(self.device)
                
                optimizer.zero_grad()
                reconstructed, latent = self.cdae(x_batch, cond_batch)
                loss = criterion(reconstructed, x_batch)
                loss.backward()
                optimizer.step()
                epoch_loss += loss.item() * x_batch.size(0)
                
            total_epoch_loss = epoch_loss / len(train_loader.dataset)
            
            if total_epoch_loss < best_loss - delta_loss:
                best_loss = total_epoch_loss
                patience_counter = 0
            else:
                patience_counter += 1
                
            if patience_counter >= patience:
                print(f"[{self.name}] CAE Early Stopping after Epoch {epoch+1}/{self.num_epochs}.")
                break
                
        # 4. Extract Latent Representations for the entire training set
        self.cdae.eval()
        with torch.no_grad():
            X_tensor = torch.tensor(X_scaled, dtype=torch.float32).to(self.device)
            cond_tensor = torch.tensor(self.donor_train_oh, dtype=torch.float32).to(self.device)
            _, X_latent_tensor = self.cdae(X_tensor, cond_tensor)
            X_latent = X_latent_tensor.cpu().numpy()

        # 5. Hyperparameter-Tuning of the LinearSVC on the latenten representations
        print(f"[{self.name}] Start BayesSearchCV for LinearSVC...")
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
            }
        ]
        
        my_stopper = CustomStopper(patience=5, min_delta=0.002, min_iter=15)
        opt = BayesSearchCV(
            estimator=LinearSVC(random_state=42),
            search_spaces=param_distributions,
            n_iter=30,
            cv=5,
            scoring='accuracy',
            n_jobs=-1,
            verbose=10
        )
        opt.fit(X_latent, y, callback=my_stopper)
        print(f"[{self.name}] Best LinearSVC Parameters: {opt.best_params_}")
        
        # 6. Train final model with best parameters and calibrate
        best_svc = LinearSVC(**opt.best_params_, random_state=42)
        self.classifier = CalibratedClassifierCV(best_svc)
        self.classifier.fit(X_latent, y)
        self.classes_ = self.classifier.classes_
        
        return self

    def _transform_to_latent(self, X):
        X_subset = X.reindex(columns=self.features_to_keep, fill_value=0.0)
        X_scaled = self.scaler.transform(X_subset.values)
        
        X_tensor = torch.tensor(X_scaled, dtype=torch.float32).to(self.device)
        cond_dummy = torch.zeros((X_tensor.shape[0], self.donor_train_oh.shape[1]), dtype=torch.float32).to(self.device)
        
        self.cdae.eval()
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


# 4. Feature Selection & Ensemble
print("\nLade Feature Importances...")
with open("feature_importance_randomforest_10_000_genes_scumi_annotated.pkl", "rb") as f:
    feature_importance = pickle.load(f)

feature_importance = feature_importance.sort_values('Importance', ascending=False)
sorted_top_genes = feature_importance['Feature'].tolist()

# Define feature subsets
total_genes = len(sorted_top_genes)
drop_075_pct = int(total_genes * 0.0075)
drop_15_pct = int(total_genes * 0.015)
drop_25_pct = int(total_genes * 0.025)

features_model_all = sorted_top_genes
features_model_minus_075 = sorted_top_genes[drop_075_pct:]
features_model_minus_15 = sorted_top_genes[drop_15_pct:]
features_model_minus_25 = sorted_top_genes[drop_25_pct:]

# Initialize pipelines for each feature subset
pipe_all = SubsetCAELinearSVC(features_model_all, donor_train_oh, device, name="All_Features")
pipe_075 = SubsetCAELinearSVC(features_model_minus_075, donor_train_oh, device, name="Drop_0.75%")
pipe_15 = SubsetCAELinearSVC(features_model_minus_15, donor_train_oh, device, name="Drop_1.5%")
pipe_25 = SubsetCAELinearSVC(features_model_minus_25, donor_train_oh, device, name="Drop_2.5%")

ensemble = VotingClassifier(
    estimators=[
        ('model_all', pipe_all),
        ('model_075', pipe_075),
        ('model_15', pipe_15),
        ('model_25', pipe_25)
    ],
    voting='soft',
    n_jobs=1  # BayesSearchCV in each pipeline already uses n_jobs=-1
)


# 5. Training & Evaluation
print("\nStart training of the ensemble (this could take a while)...")
ensemble.fit(X_train, y_train)

print("\n--- EVALUATION ON THE TESTDATA ---")
y_pred = ensemble.predict(X_test)
print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Macro F1:      {f1_score(y_test, y_pred, average='macro'):.4f}")

print("\n--- ROBUSTNESS EVALUATION ---")
with open("master_feature_importance_interleaved_marker_genes.pkl", "rb") as f:
    feature_importance = pickle.load(f)


robustness_results = test_robustness(
    ensemble,
    X_test,
    y_test,
    "scumi-annotation",
    '/home/hpc/iwbn/iwbn133h/data/humancellatlas/5f29c29a-51c6-435c-8ff0-2b2a9d05ebee/BL_standard_design_annotated.h5ad',
    feature_importance,
    log_to_console=True,
    log_to_file=False,
)
