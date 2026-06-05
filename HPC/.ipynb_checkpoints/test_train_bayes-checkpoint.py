import anndata as ad
import scanpy as sc
from sklearn.linear_model import LogisticRegression
from skopt import BayesSearchCV
from skopt.space import Real, Categorical
from custom_stopper import CustomStopper
# For saving results on HPC Cluster
import joblib
import pandas as pd
import os

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


# Normalization

# Saving count data
adata.layers["counts"] = adata.X.copy()

# Normalizing to median total counts
sc.pp.normalize_total(adata)
# Logarithmize the data
sc.pp.log1p(adata)

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
y_train = adata_train.obs['Manually_curated_celltype']

X_test = adata_test.to_df()
gene_names_train = adata_train.var_names
y_test = adata_test.obs['Manually_curated_celltype']


# Model training

model = LogisticRegression(max_iter=100)

search_space = {
    'C': Real(1e-4, 1e-2, prior='log-uniform'),
    #'penalty': Categorical(['l1', 'l2'])
}

my_stopper = CustomStopper(patience=2, min_delta=0.002, min_iter=4)

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


# Save results on HPC Cluster
output_dir = './results'
os.makedirs(output_dir, exist_ok=True)

# 1. Save model
joblib.dump(opt.best_estimator_, f'{output_dir}/best_logistic_regression_model.pkl')

# 2. Save hyperparameter results as CSV (DataFrame)
results_df = pd.DataFrame(opt.cv_results_)
results_df.to_csv(f'{output_dir}/bayes_search_results.csv', index=False)

print(f"Results successfully saved in '{output_dir}'!")
