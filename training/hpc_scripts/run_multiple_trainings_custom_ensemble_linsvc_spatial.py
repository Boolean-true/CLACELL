import importlib
import sys
import pandas as pd
import resource
import time
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.ensemble import VotingClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.calibration import CalibratedClassifierCV
import anndata as ad
import scanpy as sc
# For saving results on HPC Cluster
import joblib
import pandas as pd
import os
from sklearn.metrics import classification_report, accuracy_score, f1_score
#from test_robustness import test_robustness
from test_robustness_higher_dropout import test_robustness
from preprocess_data_spatial import prepare_adata
from skopt import BayesSearchCV
from skopt.space import Integer, Real, Categorical
from custom_stopper import CustomStopper
from scipy.sparse import csr_matrix
import time
from scipy.optimize import root_scalar
from scipy.sparse import issparse
from scipy.stats import nbinom, poisson


# Load training data
#adata = ad.read_h5ad('/home/woody/iwbn/iwbn133h/data/10x-gex/ovarian/f8f7f2b0-b8a5-4087-8048-8d3f5b6a49dd.h5ad')
adata = ad.read_h5ad('/home/woody/iwbn/iwbn133h/data/10x-gex/ovarian/f8f7f2b0-b8a5-4087-8048-8d3f5b6a49dd_spatial.h5ad')

# Use raw counts
#adata = adata.raw.to_adata()
# Check if counts are raw data
#if hasattr(adata.X, "sum"):
#    per_cell_totals = np.asarray(adata.X.sum(axis=1)).ravel()
#else:
#    per_cell_totals = np.sum(adata.X, axis=1)

#print("min:", np.min(per_cell_totals))
#print("median:", np.median(per_cell_totals))
#print("mean:", np.mean(per_cell_totals))
#print("max:", np.max(per_cell_totals))

# Zellen filtern, deren Zelltyp NICHT "Other" ist
adata = adata[adata.obs["author_cell_type"] != "Other"].copy()

# Preprocessing
adata = prepare_adata(adata, batch_key="donor_id")


# Create train test split
donor_train = [
    'SPECTRUM-OV-009', 'SPECTRUM-OV-082', 'SPECTRUM-OV-115', 'SPECTRUM-OV-014',
    'SPECTRUM-OV-116', 'SPECTRUM-OV-022', 'SPECTRUM-OV-045', 'SPECTRUM-OV-053',
    'SPECTRUM-OV-118', 'SPECTRUM-OV-083', 'SPECTRUM-OV-003', 'SPECTRUM-OV-077',
    'SPECTRUM-OV-042', 'SPECTRUM-OV-071', 'SPECTRUM-OV-036', 'SPECTRUM-OV-037',
    'SPECTRUM-OV-041', 'SPECTRUM-OV-105', 'SPECTRUM-OV-008', 'SPECTRUM-OV-107',
    'SPECTRUM-OV-080', 'SPECTRUM-OV-081', 'SPECTRUM-OV-052', 'SPECTRUM-OV-049',
    'SPECTRUM-OV-068', 'SPECTRUM-OV-051', 'SPECTRUM-OV-054', 'SPECTRUM-OV-031'
]
donor_test = [
    'SPECTRUM-OV-026', 'SPECTRUM-OV-007', 'SPECTRUM-OV-110', 'SPECTRUM-OV-065',
    'SPECTRUM-OV-070', 'SPECTRUM-OV-075', 'SPECTRUM-OV-024', 'SPECTRUM-OV-050',
    'SPECTRUM-OV-112', 'SPECTRUM-OV-090', 'SPECTRUM-OV-025', 'SPECTRUM-OV-002',
    'SPECTRUM-OV-067'
]

adata_train = adata[
    adata.obs["donor_id"].isin(donor_train)
].copy()

adata_test = adata[
    adata.obs["donor_id"].isin(donor_test)
].copy()

# Check split
print(adata_train.obs['donor_id'].unique())
print(adata_test.obs['donor_id'].unique())

# Prepare Data for training
X_train = adata_train.to_df()
gene_names_train = adata_train.var_names
y_train = adata_train.obs['author_cell_type']

X_test = adata_test.to_df()
gene_names_test = adata_test.var_names
y_test = adata_test.obs['author_cell_type']


all_runs_data = []
num_runs = 10
start_run = 0
end_run = 9

for i in range(start_run, end_run + 1):
    print(f"=== Start Run {i+1}/{num_runs} ===")
    script_start = time.time()

    # LinearSVC Hyperparametertuning
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
    opt.fit(X_train, y_train, callback=my_stopper)

    bayes = time.time()
    print(f'=== Bayes Elapsed: {bayes - script_start:.2f} seconds')

    print(f"\nSearch terminated after {len(opt.cv_results_['mean_test_score'])} Iterations.")
    print(f"Best hyperparameters: {opt.best_params_}")
    print(f"Test-Split Accuracy:  {opt.score(X_test, y_test):.4f}")

    hyperparameters = opt.best_params_

    # Compute Feature Importance from basic Random Forest
    rf = RandomForestClassifier()
    rf.fit(X_train, y_train)
    feature_importance = rf.feature_importances_
    feature_importance = np.argsort(feature_importance)[::-1]
    sorted_top_genes = X_train.columns[feature_importance].tolist()

    total_genes = len(sorted_top_genes)

    # Define subsets
    drop_075_pct = int(total_genes * 0.0075)
    drop_15_pct = int(total_genes * 0.015)
    drop_25_pct = int(total_genes * 0.025)

    # Compute Features for each subset
    features_model_all = sorted_top_genes
    features_model_minus_075 = sorted_top_genes[drop_075_pct:]
    features_model_minus_15 = sorted_top_genes[drop_15_pct:]
    features_model_minus_25 = sorted_top_genes[drop_25_pct:]


    # Build Pipelines with ColumnTransformer
    def make_pipeline(features_to_keep, model_name, model):
        preprocessor = ColumnTransformer(
            transformers=[('keep', 'passthrough', features_to_keep)],
            remainder='drop'
        )
        return Pipeline([
            ('select', preprocessor),
            (model_name, model)
        ])

    model_params = hyperparameters
    model = CalibratedClassifierCV(LinearSVC(class_weight='balanced', **model_params))
    pipe_all = make_pipeline(features_model_all, 'linsvc_all', model)
    pipe_minus_075 = make_pipeline(features_model_minus_075, 'linsvc_075', model)
    pipe_minus_15 = make_pipeline(features_model_minus_15, 'linsvc_15', model)
    pipe_minus_25 = make_pipeline(features_model_minus_25, 'linsvc_25', model)

    ensemble = VotingClassifier(
        estimators=[
            ('all_features', pipe_all),
            ('minus_075_pct', pipe_minus_075),
            ('minus_15_pct', pipe_minus_15),
            ('minus_25_pct', pipe_minus_25)
        ],
        voting='soft'
    )
    print("Train custom ensemble...")
    ensemble.fit(X_train, y_train)
    print(ensemble.score(X_test, y_test))
    
    best_model = ensemble
    y_pred = best_model.predict(X_test)
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
        #'/home/woody/iwbn/iwbn133h/data/human_immune_health_atlas/human_immune_health_atlas_full_annotated_fine_grained_cleaned.h5ad',
        feature_importances=feature_importance,
        log_to_console=True,
        log_to_file=False,
    )

    total_script_time_min = (time.time() - script_start) / 60

    # Access the global variable of the training script
    df_run = robustness_results.copy()
    
    # Add Technical Metrics
    ## Runtime
    df_run[("All", "Technical_Metrics", "Resource_Usage", "Total_Pipeline_Time_Min")] = round(total_script_time_min, 2)

    ## RAM Peak
    usage = resource.getrusage(resource.RUSAGE_SELF)
    peak_ram_gb = usage.ru_maxrss / (1024 * 1024)
    dist = "All"
    cat = "Technical_Metrics"
    sub_cat = "Resource_Usage"
    metric = "Peak_RAM_GB"
    df_run[(dist, cat, sub_cat, metric)] = peak_ram_gb

    #break
    df_run.to_csv(f'results/custom_ensemble_linsvc_spatial/result_{i}.csv', index=True)
    all_runs_data.append(df_run)

# End the test execution
#quit()

current_count = len(all_runs_data)

# If there aren'T all Dataframes in the array, load them
if current_count < num_runs:
    loaded_samples = []
    needed_samples = num_runs - current_count
    print(
        f"There are {needed_samples} DataFrames missing. Load them from save directory..."
    )

    for i in range(needed_samples):
        file_path = f"results/custom_ensemble_linsvc_spatial/result_{i}.csv"

        if os.path.exists(file_path):
            old_df = pd.read_csv(file_path, header=[0, 1, 2, 3], index_col=0)
            loaded_samples.append(old_df)
        else:
            print(
                f"Warning: File {file_path} not found! Skip it..."
            )
    all_runs_data = pd.concat([loaded_samples, all_runs_data], axis=0)


# Average over runs
combined_df = pd.concat(all_runs_data, axis=0)

# Compute Statistics for Robustness Test results
means = combined_df.mean()
stds = combined_df.std()

combined = means.round(4).astype(str) + " +- " + stds.round(4).astype(str)

# Create Dataframe with Statistics
stats_df = pd.DataFrame(
    [means, stds, combined], 
    index=["mean", "std", "mean +- std"], 
    columns=combined_df.columns
)

# Combine original Dataframe with Statistic Dataframe
final_df = pd.concat([combined_df, stats_df], axis=0)

print("=== Final result ===")
print(final_df.head())

final_df.to_csv('results/custom_ensemble_linsvc_spatial/combined_result.csv', index=True)
