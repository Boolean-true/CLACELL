import importlib
import sys
import pandas as pd
import resource
import time
import numpy as np
import pickle
from clacell import ConditionalCellClassifier
import anndata as ad
import scanpy as sc
# For saving results on HPC Cluster
import joblib
import pandas as pd
import os
from sklearn.metrics import classification_report, accuracy_score, f1_score
from test_robustness_higher_dropout import test_robustness
from preprocess_data import prepare_adata
import scipy.sparse as sp
import logging
from pathlib import Path
from datetime import datetime


# Load training data
#adata = ad.read_h5ad('/home/woody/iwbn/iwbn133h/data/CellTypist_HumanCellAtlas_Merged_cleaned_refined_cell_types.h5ad')
adata = ad.read_h5ad('/home/woody/iwbn/iwbn133h/data/CellTypist_HumanCellAtlas_Merged_cleaned_refined_cell_types_fine_and_coarse.h5ad')

# Use raw data instead of already preprocessed data
adata.X = adata.layers['counts'].copy()

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
#y_train = adata_train.obs['cell_type_final']
y_train = adata_train.obs['scumi_clean_fine_grained']

X_test = adata_test.to_df()
gene_names_test = adata_test.var_names
#y_test = adata_test.obs['cell_type_final']
y_test = adata_test.obs['scumi_clean_fine_grained']

train_donor = adata_train.obs['Donor']
test_donor = adata_test.obs['Donor']

# Model Training

classifier = ConditionalCellClassifier()
classifier.bayes_search(X_train, y_train, train_donor, n_jobs=-1)

best_model = classifier
y_pred = best_model.predict(X_test)

# Finale Evaluation
print("\n--- EVALUATION AUF DEN TESTDATEN ---")
print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.4f}\n")
print(f"Macro F1: {f1_score(y_test, y_pred, average='macro')}")
#print(classification_report(y_test, y_pred))


# Compute model score and robustness
with open("pegasus_feature_importance_interleaved_marker_genes.pkl", "rb") as f:
    feature_importance = pickle.load(f)

#feature_importance = feature_importance.sort_values('Importance', ascending=False)
ood_datasets = {
    'HIHA_Pediatric': '/home/woody/iwbn/iwbn133h/data/human_immune_health_atlas/human_immune_health_atlas_sampled_Children_10k.h5ad',
    'HIHA_Young_Adult': '/home/woody/iwbn/iwbn133h/data/human_immune_health_atlas/human_immune_health_atlas_sampled_Young_Adult_10k.h5ad',
    'HIHA_Older_Adult': '/home/woody/iwbn/iwbn133h/data/human_immune_health_atlas/human_immune_health_atlas_sampled_Older_Adult_10k.h5ad',
    'AIDA': '/home/woody/iwbn/iwbn133h/data/AIDA/aida_sampled_10k.h5ad',
}
robustness_results = test_robustness(
    best_model,
    X_test,
    y_test,
    adata_test.obs['Donor'],
    #"scumi_clean",
    'scumi_clean_fine_grained',
    ood_datasets,
    feature_importance,
    log_to_console=True,
    log_to_file=False,
)

