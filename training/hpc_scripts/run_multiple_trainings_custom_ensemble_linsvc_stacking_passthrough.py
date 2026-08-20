import importlib
import sys
import pandas as pd
import resource
import time
import numpy as np
import pickle
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
X_train = adata_train.to_df()
gene_names_train = adata_train.var_names
y_train = adata_train.obs['scumi-annotation']

X_test = adata_test.to_df()
gene_names_test = adata_test.var_names
y_test = adata_test.obs['scumi-annotation']

hyperparameters = {
        0: {'C': 0.001341474641715613, 'dual': True, 'penalty': 'l2', 'tol': 0.006115627608133035},
        1: {'C': 0.002384995325367488, 'dual': False, 'penalty': 'l2', 'tol': 0.0003111420912036033},
        2: {'C': 0.005752060651221708, 'dual': False, 'penalty': 'l2', 'tol': 0.0003809200477331375},
        3: {'C': 2.0, 'dual': False, 'penalty': 'l1', 'tol': 0.01},
        4: {'C': 0.01902599435448397, 'dual': False, 'penalty': 'l2', 'tol': 0.0001741347482663171},
        5: {'C': 0.0016521511727358553, 'dual': False, 'penalty': 'l2', 'tol': 0.0002792445399570486},
        6: {'C': 0.0020918741886567825, 'dual': True, 'penalty': 'l2', 'tol': 0.004480185617776286},
        7: {'C': 0.0017371295780133772, 'dual': True, 'penalty': 'l2', 'tol': 0.00023839386782510512},
        8: {'C': 0.0013840503361534661, 'dual': True, 'penalty': 'l2', 'tol': 0.0011295470870723676},
        9: {'C': 0.0011596846285095244, 'dual': False, 'penalty': 'l2', 'tol': 0.00011474581565452661},
}

all_runs_data = []
num_runs = 10
start_run = 0
end_run = 9

for i in range(start_run, end_run + 1):
    print(f"=== Start Run {i+1}/{num_runs} ===")
    script_start = time.time()

    with open("feature_importance_randomforest_10_000_genes_scumi_annotated.pkl", "rb") as f:
        feature_importance = pickle.load(f)

    feature_importance = feature_importance.sort_values('Importance', ascending=False)
    sorted_top_genes = feature_importance['Feature'].tolist()


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
        passthrough=True
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
        "scumi-annotation",
        'data/humancellatlas/5f29c29a-51c6-435c-8ff0-2b2a9d05ebee/BL_standard_design_annotated.h5ad',
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

    df_run.to_csv(f'results/custom_ensemble_linsvc_higher_dropout_stacking_passthrough/result_{i}.csv', index=True)
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
        file_path = f"results/custom_ensemble_linsvc_higher_dropout_stacking_passthrough/result_{i}.csv"

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

final_df.to_csv('results/custom_ensemble_linsvc_higher_dropout_stacking_passthrough/combined_result.csv', index=True)
