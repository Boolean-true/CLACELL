import anndata as ad
import scanpy as sc
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from xgboost import XGBClassifier
from skopt import BayesSearchCV
from skopt.space import Real, Categorical, Integer
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
gene_names_train = adata_train.var_names
y_test = adata_test.obs['Manually_curated_celltype']


# Model training

## Filter classes
y_train_series = pd.Series(y_train)

# Only keep classes with at least 5 samples
min_samples = 5
class_counts = y_train_series.value_counts()
valid_classes = class_counts[class_counts >= min_samples].index

# Filter train data
train_mask = y_train_series.isin(valid_classes).values
X_train = X_train[train_mask]
y_train = y_train_series[train_mask]

## Encode Labels
le_train = LabelEncoder()
y_train_enc = le_train.fit_transform(y_train.to_numpy() if hasattr(y_train, 'to_numpy') else y_train)

classes_in_train = set(y_train)
mask = y_test.isin(classes_in_train).values

X_test_filtered = X_test[mask]
y_test_filtered = y_test[mask]

y_test_enc = le_train.transform(y_test_filtered.to_numpy() if hasattr(y_test_filtered, 'to_numpy') else y_test_filtered)


# Modell
model = XGBClassifier()

search_space = {
    #'booster': Categorical(['gbtree', 'gblinear', 'dart']),
    'learning_rate': Real(0.01, 0.3, prior='log-uniform'),
    'max_depth': Integer(3, 10),
    'colsample_bytree': Real(0.1, 0.5, prior='uniform')
}

my_stopper = CustomStopper(patience=5, min_delta=0.002, min_iter=15) 

cv_strat = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

opt = BayesSearchCV(
    estimator=model,
    search_spaces=search_space,
    n_iter=10,
    cv=cv_strat,
    #cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=10
)

print("Start BayesSearch with Early Stopping...")
opt.fit(X_train, y_train_enc, callback=my_stopper)

print(f"\nSearch terminated after {len(opt.cv_results_['mean_test_score'])} Iterations.")
print(f"Best hyperparameters: {opt.best_params_}")
print(f"Test-Split Accuracy:  {opt.score(X_test_filtered, y_test_enc):.4f}")


# Save results on HPC Cluster
output_dir = './results'
os.makedirs(output_dir, exist_ok=True)

# 1. Save model
joblib.dump(opt.best_estimator_, f'{output_dir}/best_xgboost_model.pkl')

# 2. Save hyperparameter results as CSV (DataFrame)
results_df = pd.DataFrame(opt.cv_results_)
results_df.to_csv(f'{output_dir}/bayes_search_xgboost_results.csv', index=False)

print(f"Results successfully saved in '{output_dir}'!")
