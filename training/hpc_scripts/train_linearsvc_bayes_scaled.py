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
from sklearn.preprocessing import StandardScaler
from test_robustness_higher_dropout import test_robustness
from preprocess_data import prepare_adata
import pickle
from scipy.sparse import csr_matrix
import time


start = time.time()
print(f'=== Start time: {start}')

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

scaler = StandardScaler(with_mean=False).set_output(transform="pandas")
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Convert train data in sparse matrix for faster computation
X_train_scaled = csr_matrix(X_train_scaled.values)

preprocessing = time.time()
print(f'=== Preprocessing Elapsed: {preprocessing - start:.2f} seconds')

# Model training

model = LinearSVC(class_weight="balanced")

search_space = [
        {
    'C': Real(1e-3, 2.0, prior='log-uniform'),
    'penalty': Categorical(['l1']),
    'dual': Categorical([False]),
    #'class_weight': Categorical(['balanced', None]),
    'tol': Real(1e-4, 1e-2, prior='log-uniform')
        },
        {
    'C': Real(1e-3, 2.0, prior='log-uniform'),
    'penalty': Categorical(['l2']),
    'dual': Categorical([True, False]),
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
#X_sparse = csr_matrix(X_train.values)
#opt.fit(X_sparse, y_train, callback=my_stopper)
opt.fit(X_train_scaled, y_train, callback=my_stopper)

bayes = time.time()
print(f'=== Bayes Elapsed: {bayes - start:.2f} seconds')

print(f"\nSearch terminated after {len(opt.cv_results_['mean_test_score'])} Iterations.")
print(f"Best hyperparameters: {opt.best_params_}")
print(f"Test-Split Accuracy:  {opt.score(X_test, y_test):.4f}")


# Save results on HPC Cluster
#output_dir = './results'
#os.makedirs(output_dir, exist_ok=True)
# 1. Save model
#joblib.dump(opt.best_estimator_, f'{output_dir}/best_linearsvc_model.pkl')


best_model = opt.best_estimator_
y_pred = best_model.predict(X_test_scaled)

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
    #"scumi-annotation",
    "scumi_clean",
    '/home/woody/iwbn/iwbn133h/data/human_immune_health_atlas/human_immune_health_atlas_full_annotated_fine_grained_cleaned.h5ad',
    feature_importance,
    scaler=scaler,
    log_to_console=True,
    log_to_file=False,
)

robustness = time.time()
print(f'=== Robustness Elapsed: {robustness - bayes:.2f} seconds')
print(f'=== Total Elapsed: {robustness - start:.2f} seconds')
