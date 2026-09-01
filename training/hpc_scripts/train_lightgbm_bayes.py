import anndata as ad
import scanpy as sc
import lightgbm as lgbm
from skopt import BayesSearchCV
from skopt.space import Integer, Real, Categorical
from custom_stopper import CustomStopper
# For saving results on HPC Cluster
import joblib
import pandas as pd
import os
from sklearn.metrics import classification_report, accuracy_score, f1_score
from test_robustness_higher_dropout import test_robustness
from preprocess_data import prepare_adata
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
X_train = adata_train.X#to_df()
gene_names_train = adata_train.var_names
#y_train = adata_train.obs['scumi-annotation']
#y_train = adata_train.obs['scumi_clean']
y_train = adata_train.obs['cell_type_final']

X_test = adata_test.to_df()
gene_names_test = adata_test.var_names
#y_test = adata_test.obs['scumi-annotation']
#y_test = adata_test.obs['scumi_clean']
y_test = adata_test.obs['cell_type_final']


# Model training

model = lgbm.LGBMClassifier(objective='multiclass', n_jobs=1)

search_space = {
    'num_leaves': Integer(20, 150),
    'learning_rate': Real(0.01, 0.2, prior='log-uniform'),
    'n_estimators': Integer(50, 150),
    'feature_fraction': Real(0.5, 1.0, prior='uniform'),
}

my_stopper = CustomStopper(patience=5, min_delta=0.002, min_iter=15) 

opt = BayesSearchCV(
    estimator=model,
    search_spaces=search_space,
    n_iter=30,
    cv=5,
    scoring='accuracy',
    n_jobs=-1, #5 # Initially 5, changed it for fairness
    verbose=10
)

print("Start BayesSearch with Early Stopping...")
opt.fit(X_train, y_train, callback=my_stopper)

print(f"\nSearch terminated after {len(opt.cv_results_['mean_test_score'])} Iterations.")
print(f"Best hyperparameters: {opt.best_params_}")
print(f"Test-Split Accuracy:  {opt.score(X_test, y_test):.4f}")


# Save results on HPC Cluster
#output_dir = './results'
#os.makedirs(output_dir, exist_ok=True)

# 1. Save model
#joblib.dump(opt.best_estimator_, f'{output_dir}/best_lightgbm_model.pkl')

# 2. Save hyperparameter results as CSV (DataFrame)
#results_df = pd.DataFrame(opt.cv_results_)
#results_df.to_csv(f'{output_dir}/bayes_search_lightgbm_results.csv', index=False)

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
    #"scumi-annotation",
    "scumi_clean",
    '/home/woody/iwbn/iwbn133h/data/human_immune_health_atlas/human_immune_health_atlas_full_annotated_fine_grained_cleaned.h5ad',
    feature_importance,
    log_to_console=True,
    log_to_file=False,
)

