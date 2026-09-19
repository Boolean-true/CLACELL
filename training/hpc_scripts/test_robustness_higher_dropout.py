import anndata as ad
import numpy as np
import pandas as pd
import scipy.sparse as sp
from scipy.sparse import csr_matrix
import scanpy as sc
import celltypist
import logging
from pathlib import Path
from datetime import datetime
import sys
from preprocess_data import prepare_adata

import json
from scipy.stats import entropy
from sklearn.metrics import classification_report, accuracy_score, f1_score


class StdoutFilter(logging.Filter):
    def filter(self, record):
        return record.levelno < logging.WARNING


def _setup_logger(log_to_console=True, log_to_file=True):
    # Create results directory if it doesn't exist
    Path("results").mkdir(exist_ok=True)

    # Define the log file name with a timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    logfile = f"results/clacell_result_{timestamp}.log"

    handlers = []
    if log_to_console:
        # Handler for stdout (INFO and below)
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(logging.INFO)
        stdout_handler.addFilter(StdoutFilter())
        handlers.append(stdout_handler)

        # Handler for stderr (WARNING and above)
        stderr_handler = logging.StreamHandler(sys.stderr)
        stderr_handler.setLevel(logging.WARNING)
        handlers.append(stderr_handler)
    if log_to_file:
        handlers.append(logging.FileHandler(logfile, mode="w"))

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=handlers,
        force=True,
    )


def _predict_labels(model, X):
    if hasattr(model, "predict"):
        return model.predict(X)

    # Not a scikit-learn style model, try CellTypist-style annotation
    try:
        predictions = celltypist.annotate(filename=ad.anndata(X), model=model)

        return predictions.predicted_labels["predicted_labels"]

    except TypeError:
        raise AttributeError(
            "Model does not have a predict method and cannot be annotated with celltypist.annotate()"
        )


def _prepare_sparse_input(X, gene_names=None):
    if not sp.issparse(X):
        return X

    if gene_names is None:
        logging.error(
            "Error: sparse input requires gene_names. Skipping robustness test."
        )
        return None

    gene_names = list(gene_names)
    if len(gene_names) != X.shape[1]:
        logging.error(
            f"Error: gene_names length ({len(gene_names)}) does not match the number of features in X ({X.shape[1]}). Skipping robustness test."
        )
        return None

    return pd.DataFrame(X.toarray(), columns=gene_names)


def _drop_features(X, pct: float, rng: np.random.Generator):
    if pct <= 0:
        return X

    # Only consider genes that are not 0 for all cells
    X_vals = X.values if hasattr(X, "values") else X
    active_mask = (X_vals != 0).any(axis=0)
    active_indices = np.where(active_mask)[0]

    if len(active_indices) == 0:
        return X

    # Compute number of genes to drop on active genes
    n_drop = max(1, int(len(active_indices) * pct))
    drop_idx = rng.choice(active_indices, size=n_drop, replace=False)

    X_copy = X.copy()
    X_copy.iloc[:, drop_idx] = 0
    return X_copy


def _print_text_confusion_matrix(y_true, y_pred):
    y_true = np.asarray(y_true).ravel()
    y_pred = np.asarray(y_pred).ravel()

    # Terminal-Ausgabe-Optionen setzen, um Abschneiden zu verhindern
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 1000)

    logging.info("\n" + "="*80)
    logging.info("1. ABSOLUTE CONFUSION MATRIX (rows = ground truth, columns = prediction)")
    logging.info("="*80)
    cm_abs = pd.crosstab(
        pd.Series(y_true, name='True_Label'),
        pd.Series(y_pred, name='Pred_Model')
    )
    logging.info("\n" + cm_abs.to_string())

    logging.info("\n" + "="*80)
    logging.info("2. PERCENTAGE SHIFT MATRIX (% per real cell type)")
    logging.info("="*80)
    cm_perc = pd.crosstab(
        pd.Series(y_true, name='True_Label'),
        pd.Series(y_pred, name='Pred_Model'),
        normalize='index'
    ) * 100
    logging.info("\n" + cm_perc.round(1).to_string())


def compute_baseline_score(model, X, y, batch_obs=None):
    y_pred = _predict_labels(model, X)
    accuracy = accuracy_score(y, y_pred)
    macro_f1 = f1_score(y, y_pred, average='macro', zero_division=0)

    logging.info(f"Baseline accuracy score {accuracy:.4f} | Macro F1 {macro_f1:.4f}")
    logging.info(
        f"Classification Report:\n{classification_report(y, y_pred, zero_division=0)}"
    )

    _print_text_confusion_matrix(y, y_pred)

    batch_metrics = {"batch_f1_mean": None, "batch_f1_std": None}

    if batch_obs is not None:
        # Convert batch_ops in a numpy array for clean masking
        batch_obs_array = np.asarray(batch_obs)
        y_array = np.asarray(y)
        y_pred_array = np.asarray(y_pred)

        unique_batches = np.unique(batch_obs_array)
        batch_f1_scores = []

        for b in unique_batches:
            idx = (batch_obs_array == b)
            # Compute the F1-Score only for batches that contain cells
            if np.sum(idx) > 0:
                score = f1_score(y_array[idx], y_pred_array[idx], average='macro', zero_division=0)
                batch_f1_scores.append(score)

        if batch_f1_scores:
            batch_metrics["batch_f1_mean"] = np.mean(batch_f1_scores)
            batch_metrics["batch_f1_std"] = np.std(batch_f1_scores)
            logging.info(f"Batch Stability (N={len(unique_batches)}): Mean F1 {batch_metrics['batch_f1_mean']:.4f} | Std F1 {batch_metrics['batch_f1_std']:.4f}")

    return accuracy, classification_report(y, y_pred, zero_division=0, output_dict=True), batch_metrics


# Computes the robustness of the model by randomly dropping 10% of the features and evaluating the score again.
# This is done 10 times and the average score is reported.
def compute_robustness_random_dropout(model, X, y, drop_pct=0.10):
    acc_scores = []
    f1_scores = []
    for _ in range(10):
        rng = np.random.default_rng()
        dropped = _drop_features(X, drop_pct, rng)
        y_pred = _predict_labels(model, dropped)
        acc_scores.append(accuracy_score(y, y_pred))
        f1_scores.append(f1_score(y, y_pred, average='macro', zero_division=0))
    
    mean_acc = np.mean(acc_scores)
    mean_f1 = np.mean(f1_scores)
    logging.info(f"Random dropout ({drop_pct*100:.1f}%) -> Accuracy: {mean_acc:.4f}, Macro F1: {mean_f1:.4f}")

    return mean_acc, mean_f1


# Computes the robustness of the model by executing it multiple times and check if the predictions are consistent across executions.
# The average score is reported.
def compute_robustness_multiple_executions(model, X, y, n_executions=5):
    results = []
    for _ in range(n_executions):
        y_pred = _predict_labels(model, X)
        results.append(y_pred)

    # Check if the predictions are consistent across executions
    num_samples = len(y)
    num_different_predictions = 0
    for i in range(num_samples):
        # Prüfen, ob für Zelle i unterschiedliche Label vorhergesagt wurden
        unique_preds = {results[exec_idx][i] for exec_idx in range(n_executions)}
        if len(unique_preds) > 1:
            num_different_predictions += 1

    logging.info(f"Total samples: {num_samples}")
    logging.info(f"Number of inconsistent predictions: {num_different_predictions}")

    return num_samples, num_different_predictions


# Computes the robustness of the model by dropping the features with the highest importance scores and evaluating the score again.
# This is done for different percentages of dropped features and the scores are reported.
# feature_importances should be a pandas dataframe with columns "feature" and "importance" sorted by importance in descending order. The "feature" column can contain feature names that are not present in the dataset.
def compute_robustness_feature_importance_dropout(model, X, y, feature_importances):
    # 1. Compute feature column in feature_importances
    feature_col = None
    for column in feature_importances.columns:
        if str(column).lower() == "feature":
            feature_col = column
            break

    if feature_col is None:
        if len(feature_importances.columns) >= 1:
            feature_col = feature_importances.columns[0]
            logging.warning(
                f"Warning: Could not find a column named 'feature'; using '{feature_col}' as feature column."
            )
        else:
            logging.error("feature_importances dataframe has no columns; skipping dropout test.")
            return [], []

    # 2. Compute active genes (not 0 for every gene)
    if hasattr(X, "columns"):
        active_cols = X.columns[(X != 0).any(axis=0)]
    else:
        logging.error("X does not have columns attribute. DataFrame input required.")
        return [], []

    # 3. Filter feature_importances on the active genes
    fi_filtered = feature_importances[feature_importances[feature_col].isin(active_cols)].copy()

    if len(fi_filtered) == 0:
        logging.warning("No matching active features found between X and feature_importances; skipping test.")
        return [], []

    # 4. Number of available genes after filtering
    n_available_features = len(fi_filtered)

    acc_scores = []
    f1_scores = []
    for pct in [0.001, 0.005, 0.01, 0.02]:
        # Compute n_drop according to active genes
        n_drop = max(1, int(n_available_features * pct))
        top_features = fi_filtered[feature_col].iloc[:n_drop].tolist()

        # Prepare a copy of X with selected features zeroed
        X_dropped = X.copy()
        drop_idx = [X_dropped.columns.get_loc(feat) for feat in top_features if feat in X_dropped.columns]

        if drop_idx:
            X_dropped.iloc[:, drop_idx] = 0

        y_pred = _predict_labels(model, X_dropped)
        acc = accuracy_score(y, y_pred)
        f1 = f1_score(y, y_pred, average='macro', zero_division=0)
        
        acc_scores.append(acc)
        f1_scores.append(f1)
        logging.info(
            f"Feature importance dropout ({pct*100:.1f}% features dropped) -> Accuracy: {acc:.4f}, Macro F1: {f1:.4f}"
        )

    return acc_scores, f1_scores


# Computes the score and robustness of the given model on the given dataset (X, y) and feature importance
def compute_model_score_and_robustness(model, X, y, feature_importances=None, dist_name="In-Distribution", batch_obs=None):
    # Baseline
    baseline_accuracy, baseline_report, batch_metrics = compute_baseline_score(model, X, y, batch_obs=batch_obs)

    # Random Robustness Dropouts
    rd_10_acc, rd_10_f1 = compute_robustness_random_dropout(model, X, y, drop_pct=0.10)
    #rd_50_acc, rd_50_f1 = compute_robustness_random_dropout(model, X, y, drop_pct=0.50)
    #rd_90_acc, rd_90_f1 = compute_robustness_random_dropout(model, X, y, drop_pct=0.90)
    #rd_925_acc, rd_925_f1 = compute_robustness_random_dropout(model, X, y, drop_pct=0.925)
    #rd_95_acc, rd_95_f1 = compute_robustness_random_dropout(model, X, y, drop_pct=0.95)
    
    num_samples, num_different_predictions = compute_robustness_multiple_executions(model, X, y, 5)

    # Feature Importance Dropouts
    if feature_importances is not None:
        fi_acc_scores, fi_f1_scores = compute_robustness_feature_importance_dropout(model, X, y, feature_importances)

    # Combine results into a single DataFrame for easier comparison
    results = {}
    results[(dist_name, "Baseline", "Overall", "Accuracy")] = baseline_accuracy
    # Add Batch Metrics
    results[(dist_name, "Baseline", "Batch Effect", "Macro_F1_Mean")] = (
        batch_metrics["batch_f1_mean"]
    )
    results[(dist_name, "Baseline", "Batch Effect", "Macro_F1_Std")] = (
        batch_metrics["batch_f1_std"]
    )
    # Classification Report
    for class_name, metrics in baseline_report.items():
        if isinstance(metrics, dict):
            for metric_name, val in metrics.items():
                results[(dist_name, "Classification Report", class_name, metric_name)] = val
        else:
            # For the row "accuracy" in the report (it is a float not a dict)
            results[(dist_name, "Classification Report", "Total_Accuracy", class_name)] = metrics

    # Map Random Dropout scores
    random_dropouts = [
        ("Random", rd_10_acc, rd_10_f1),
        #("Random_10", rd_10_acc, rd_10_f1),
        #("Random_50", rd_50_acc, rd_50_f1),
        #("Random_90", rd_90_acc, rd_90_f1),
        #("Random_925", rd_925_acc, rd_925_f1),
        #("Random_95", rd_95_acc, rd_95_f1),
    ]
    for name, acc_val, f1_val in random_dropouts:
        results[(dist_name, "Dropout", name, "Accuracy")] = acc_val
        results[(dist_name, "Dropout", name, "Macro_F1")] = f1_val

    results[(dist_name, "Consistency", "Num Samples", "Count")] = num_samples
    results[(dist_name, "Consistency", "Inconsistent Predictions", "Count")] = num_different_predictions

    # Map Feature Importance Dropout scores
    if feature_importances is not None:
        thresholds = ["0.1%", "0.5%", "1.0%", "2.0%"]
        for threshold, acc_val, f1_val in zip(thresholds, fi_acc_scores, fi_f1_scores):
            results[(dist_name, "Dropout", f"FI_{threshold}", "Accuracy")] = acc_val
            results[(dist_name, "Dropout", f"FI_{threshold}", "Macro_F1")] = f1_val
    
    return pd.DataFrame.from_dict([results])


# Tests the robustness of the given model on the given dataset (X, y) as well as on an out-of-distribution dataset loaded from the given path.
# The score and robustness are computed on both datasets and reported.
# If X is sparse then gene_names must be provided to convert it into a dataframe. If it is not provided the test will be skipped.
def test_robustness(
    model,
    X,
    y,
    id_donor_col=None,
    labels="scumi_clean_fine_grained",
    ood_dataset_paths=None,
    feature_importances=None,
    gene_names=None,
    log_to_console=True,
    log_to_file=False,
    scaler=None,
):
    # Setup Logger
    _setup_logger(log_to_console, log_to_file)

    logging.info("--- In distribution testset ---")
    if sp.issparse(X):
        X = _prepare_sparse_input(X, gene_names=gene_names)
        if X is None:
            # Sparse input could not be prepared -> skip robustness tests
            return

    id_results = compute_model_score_and_robustness(
        model, X, y, feature_importances=feature_importances, dist_name="In-Distribution", batch_obs=id_donor_col
    )

    train_classes = set(y.unique())

    logging.info("--- Out of data distribution ---")
    if ood_dataset_paths is None:
        logging.error(
            "No out-of-distribution dataset path provided. Skipping out-of-distribution tests."
        )
        id_results.columns = pd.MultiIndex.from_tuples(
            id_results.columns,
            names=["Distribution", "Category", "Sub-Category", "Metric"]
        )
        return id_results

    # Save mapping from gene name to index in training set for quick lookup
    train_gene_to_idx = {gene: i for i, gene in enumerate(X.columns)}

    M_train = len(X.columns)  # Number of genes in the training set

    all_results = [id_results]

    # Iterate over OOD Datasets
    for ds_name, ood_path in ood_dataset_paths.items():
        logging.info(f"--- Processing OOD dataset: {ds_name} ({ood_path}) ---")

        # Assume the dataset at the given path contains raw counts
        complete_adata = ad.io.read_h5ad(ood_path)
        adata = complete_adata[complete_adata.obs[labels].isin(train_classes)].copy()

        # Prepare Adata for Doublet Detection
        # 1. Remove NaN values from donor_id after filtering
        adata = adata[adata.obs["donor_id"].notna()].copy()
        
        # 2. Filter empty cells and genes
        sc.pp.filter_cells(adata, min_genes=1)
        sc.pp.filter_genes(adata, min_cells=1)

        # 3. Exclude too small batches
        min_cells_per_batch = 30
        batch_counts = adata.obs["donor_id"].value_counts()
        valid_batches = batch_counts[batch_counts >= min_cells_per_batch].index
        adata = adata[adata.obs["donor_id"].isin(valid_batches)].copy()

        # 3. Remove unused donor_ids
        if str(adata.obs["donor_id"].dtype) == "category":
            adata.obs["donor_id"] = (
                adata.obs["donor_id"].cat.remove_unused_categories()
            )

        # Preprocess the dataset in the same way as the training data
        adata = prepare_adata(adata, batch_key="donor_id")

        X_oodd = adata.X
        y_oodd = adata.obs[labels]

        # Filter genes that are not in the training set and reorder the remaining genes to match the training set
        M_test = adata.shape[1]  # Number of genes in the loaded dataset

        ## Create a sparse mapping matrix of shape M_test x M_train where P[i, j] = 1 if gene i in the test set matches gene j in the training set, else 0
        P = sp.lil_matrix((M_test, M_train))

        ## Fill the mapping matrix
        for test_idx, gene in enumerate(adata.var_names):
            if gene in train_gene_to_idx:
                train_idx = train_gene_to_idx[gene]
                P[test_idx, train_idx] = 1

        P = P.tocsr()  # More efficient for matrix multiplication

        ## Filter, reorder and zero-pad genes missing from the training set with a single matrix multiplication
        X_test = X_oodd @ P

        # Convert to dense DataFrame with training feature names so sklearn feature checks remain consistent.
        if sp.issparse(X_test):
            X_test = X_test.toarray()
        X_test = pd.DataFrame(X_test, index=adata.obs_names, columns=X.columns)

        # Print gene comparison and max value for debugging
        matched_genes = [gene for gene in adata.var_names if gene in train_gene_to_idx]
        logging.info(f"Genes expected in training set: {len(X.columns)}")
        logging.info(f"Genes actually matched in test set: {len(matched_genes)}")
        logging.info(f"Training data Max-Value: {np.max(X.values)}")
        logging.info(f"Test data Max-Value: {np.max(X_test.values)}")


        # Scale Data
        if scaler is not None:
            X_test = scaler.transform(X_test)

        ood_results = compute_model_score_and_robustness(model, X_test, y_oodd, feature_importances, dist_name=f"OOD_{ds_name}", batch_obs=adata.obs['donor_id'])

        all_results.append(ood_results)

    combined_results = pd.concat(all_results, axis=1)
    combined_results.columns = pd.MultiIndex.from_tuples(
        combined_results.columns,
        names=["Distribution", "Category", "Sub-Category", "Metric"]
    )
    return combined_results
