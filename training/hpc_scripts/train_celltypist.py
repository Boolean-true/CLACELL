import anndata as ad
import scanpy as sc
import celltypist
from sklearn.metrics import accuracy_score
from skopt import BayesSearchCV
from skopt.space import Real, Categorical
from custom_stopper import CustomStopper
# For saving results on HPC Cluster
import joblib
import pandas as pd
import os
from test_robustness import compute_model_score_and_robustness

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



model = celltypist.train(
    X=adata_train,
    labels='Manually_curated_celltype',
    genes=None,
    check_expression=False,
)

model.write('celltypist_model.pkl')

print("Finished Training. Starting Prediction on Test Data...")

predictions = celltypist.annotate(
    X=adata_test, 
    model=model,
    majority_voting=False
)

y_pred = predictions.predicted_labels['predicted_labels']
y_true = adata_test.obs['Manually_curated_celltype']

accuracy = accuracy_score(y_true, y_pred)
print(f"CellTypist Test Accuracy: {accuracy:.4f}")


# Compute model score and robustness
with open("feature_importance_logisticregression.pkl", "rb") as f:
    feature_importance = pickle.load(f)

feature_importance = feature_importance.sort_values('Importance', ascending=False)

compute_model_score_and_robustness(model, X_test, y_test, None, feature_importance)
