import anndata as ad
import scanpy as sc
from sklearn.svm import LinearSVC
from skopt import BayesSearchCV
from skopt.space import Integer, Real, Categorical
from custom_stopper import CustomStopper
# For saving results on HPC Cluster
import joblib
import pandas as pd
import os
from sklearn.metrics import classification_report, accuracy_score, f1_score
from test_robustness import test_robustness
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
X_train = adata_train.X#to_df()
gene_names_train = adata_train.var_names
y_train = adata_train.obs['scumi-annotation']

X_test = adata_test.to_df()
gene_names_test = adata_test.var_names
y_test = adata_test.obs['scumi-annotation']


# Model training

model = LinearSVC()

search_space = [
        {
    'C': Real(1e-3, 2.0, prior='log-uniform'),
    'penalty': Categorical(['l2']),
    'dual': Categorical([True, False]),
    #'class_weight': Categorical(['balanced', None]),
    'tol': Real(1e-4, 1e-2, prior='log-uniform')
        },
        {
    'C': Real(1e-3, 2.0, prior='log-uniform'),
    'penalty': Categorical(['l1']),
    'dual': Categorical([False]),
    #'class_weight': Categorical(['balanced', None]),
    'tol': Real(1e-4, 1e-2, prior='log-uniform')
        },
]


my_stopper = CustomStopper(patience=5, min_delta=0.002, min_iter=15) 

opt = BayesSearchCV(
    estimator=model,
    search_spaces=search_space,
    n_iter=30,
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
#joblib.dump(opt.best_estimator_, f'{output_dir}/best_linearsvc_model.pkl')

# 2. Save hyperparameter results as CSV (DataFrame)
#results_df = pd.DataFrame(opt.cv_results_)
#results_df.to_csv(f'{output_dir}/bayes_search_linearsvc_results.csv', index=False)

#print(f"Results successfully saved in '{output_dir}'!")


best_model = opt.best_estimator_
y_pred = best_model.predict(X_test)

# Finale Evaluation
print("\n--- EVALUATION AUF DEN TESTDATEN ---")
print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.4f}\n")
print(f"Macro F1: {f1_score(y_test, y_pred, average='macro')}")
#print(classification_report(y_test, y_pred))


# Compute model score and robustness
with open("master_feature_importance_interleaved_marker_genes.pkl", "rb") as f:
    feature_importance = pickle.load(f)

#feature_importance = feature_importance.sort_values('Importance', ascending=False)
robustness_results = test_robustness(
    best_model,
    X_test,
    y_test,
    "scumi-annotation",
    'data/humancellatlas/5f29c29a-51c6-435c-8ff0-2b2a9d05ebee/BL_standard_design_annotated.h5ad',
    feature_importance,
    log_to_console=True,
    log_to_file=False,
)

