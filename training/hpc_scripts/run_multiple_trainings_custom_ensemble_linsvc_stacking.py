import importlib
import sys
import pandas as pd
import resource
import time
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import StackingClassifier
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


# Load training data
#adata = ad.read_h5ad('/home/woody/iwbn/iwbn133h/data/CellTypist_HumanCellAtlas_Merged_cleaned.h5ad')
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


hyperparameters = {
        0: {'C': 0.033645854251403165, 'dual': False, 'penalty': 'l1', 'tol': 0.01},
        1: {'C': 0.033030662821415015, 'dual': False, 'penalty': 'l1', 'tol': 0.01},
        2: {'C': 0.03429948310767735, 'dual': False, 'penalty': 'l1', 'tol': 0.0001},
        3: {'C': 0.03229953973971724, 'dual': False, 'penalty': 'l1', 'tol': 0.0001},
        4: {'C': 0.03353399534711077, 'dual': False, 'penalty': 'l1', 'tol': 0.0001},
        5: {'C': 0.029918305898337064, 'dual': False, 'penalty': 'l1', 'tol': 0.01},
        6: {'C': 0.03937640873013549, 'dual': False, 'penalty': 'l1', 'tol': 0.009468662828490342},
        7: {'C': 0.03786441645406222, 'dual': False, 'penalty': 'l1', 'tol': 0.005523576086634508},
        8: {'C': 0.029642629364570676, 'dual': False, 'penalty': 'l1', 'tol': 0.01},
        9: {'C': 0.03174924998189852, 'dual': False, 'penalty': 'l1', 'tol': 0.0011375557337571533},
}

all_runs_data = []
num_runs = 10
start_run = 0
end_run = 9

for i in range(start_run, end_run + 1):
    print(f"=== Start Run {i+1}/{num_runs} ===")
    script_start = time.time()

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

    model_params = hyperparameters[i]
    model = CalibratedClassifierCV(LinearSVC(**model_params))
    pipe_all = make_pipeline(features_model_all, 'linsvc_all', model)
    pipe_minus_075 = make_pipeline(features_model_minus_075, 'linsvc_075', model)
    pipe_minus_15 = make_pipeline(features_model_minus_15, 'linsvc_15', model)
    pipe_minus_25 = make_pipeline(features_model_minus_25, 'linsvc_25', model)

    ensemble = StackingClassifier(
        estimators=[
            ('all_features', pipe_all),
            ('minus_075_pct', pipe_minus_075),
            ('minus_15_pct', pipe_minus_15),
            ('minus_25_pct', pipe_minus_25)
        ],
        final_estimator=LogisticRegression(max_iter=1000),
        cv=5,
        n_jobs=-1,
        passthrough=False
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
        '/home/woody/iwbn/iwbn133h/data/human_immune_health_atlas/human_immune_health_atlas_full_annotated_fine_grained_cleaned.h5ad',
        feature_importance,
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

    df_run.to_csv(f'results/custom_ensemble_linsvc_higher_dropout_stacking/result_{i}.csv', index=True)
    all_runs_data.append(df_run)

current_count = len(all_runs_data)

# If there aren'T all Dataframes in the array, load them
if current_count < num_runs:
    loaded_samples = []
    needed_samples = num_runs - current_count
    print(
        f"There are {needed_samples} DataFrames missing. Load them from save directory..."
    )

    for i in range(needed_samples):
        file_path = f"results/custom_ensemble_linsvc_higher_dropout_stacking/result_{i}.csv"

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

final_df.to_csv('results/custom_ensemble_linsvc_higher_dropout_stacking/combined_result.csv', index=True)
