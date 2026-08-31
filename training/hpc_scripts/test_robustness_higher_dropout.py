import anndata as ad
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
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
import sys


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
    n_features = X.shape[1]
    n_drop = max(1, int(n_features * pct))
    drop_idx = rng.choice(n_features, size=n_drop, replace=False)

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

    print("Printed confusion matrix:")
    print(cm_abs.to_string(), flush=True)
    sys.stdout.flush()

    logging.info("\n" + "="*80)
    logging.info("2. PERCENTAGE SHIFT MATRIX (% per real cell type)")
    logging.info("="*80)
    cm_perc = pd.crosstab(
        pd.Series(y_true, name='True_Label'),
        pd.Series(y_pred, name='Pred_Model'),
        normalize='index'
    ) * 100
    #logging.info(cm_perc.round(1))
    for line in cm_perc.round(1).to_string().split('\n'):
        logging.info(line)


# Computes the score on all features (baseline)
def compute_baseline_score(model, X, y):
    y_pred = _predict_labels(model, X)
    accuracy = accuracy_score(y, y_pred)
    logging.info(f"Baseline accuracy score {accuracy:.4f}")
    logging.info(
        f"Classification Report:\n{classification_report(y, y_pred, zero_division=0)}"
    )

    _print_text_confusion_matrix(y, y_pred)

    return accuracy, classification_report(y, y_pred, zero_division=0, output_dict=True)


# Computes the robustness of the model by randomly dropping 10% of the features and evaluating the score again.
# This is done 10 times and the average score is reported.
def compute_robustness_random_dropout(model, X, y, drop_pct=0.10):
    scores = []
    for _ in range(10):
        rng = np.random.default_rng()
        dropped = _drop_features(X, drop_pct, rng)
        y_pred = _predict_labels(model, dropped)
        accuracy = accuracy_score(y, y_pred)
        scores.append(accuracy)
    logging.info(f"Random dropout accuracy score {np.mean(scores):.4f}")

    return np.mean(scores)


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
        for j in range(n_executions):
            for k in range(j + 1, n_executions):
                if results[j][i] != results[k][i]:
                    num_different_predictions += 1

    logging.info(f"Total samples: {num_samples}")
    logging.info(f"Number of inconsistent predictions: {num_different_predictions}")

    return num_samples, num_different_predictions


# Computes the robustness of the model by dropping the features with the highest importance scores and evaluating the score again.
# This is done for different percentages of dropped features and the scores are reported.
# feature_importances should be a pandas dataframe with columns "feature" and "importance" sorted by importance in descending order. The "feature" column can contain feature names that are not present in the dataset.
def compute_robustness_feature_importance_dropout(model, X, y, feature_importances):
    scores = []
    for pct in [0.001, 0.005, 0.01, 0.02]:
        n_features = X.shape[1]
        n_drop = max(1, int(n_features * pct))

        # Extract top features from feature_importances
        if hasattr(feature_importances, "iloc") and hasattr(
            feature_importances, "columns"
        ):
            feature_col = None
            for column in feature_importances.columns:
                if str(column).lower() == "feature":
                    feature_col = column
                    break

            if feature_col is None:
                if len(feature_importances.columns) >= 1:
                    feature_col = feature_importances.columns[0]
                    logging.warning(
                        f"Warning: could not find a column named 'feature'; using '{feature_col}' as feature column."
                    )
                else:
                    logging.error(
                        "feature_importances dataframe has no columns; skipping this pct"
                    )
                    continue

            top_features = feature_importances[feature_col].iloc[:n_drop].tolist()
        else:
            # assume list/array/series-like of feature identifiers (names or indices)
            try:
                top_features = list(feature_importances)[:n_drop]
            except Exception:
                logging.error(
                    "feature_importances has unexpected format; skipping this pct"
                )
                continue

        # Prepare a copy of X with selected features zeroed
        X_dropped = X.copy()
        drop_idx = []
        for feat in top_features:
            if feat in X_dropped.columns:
                drop_idx.append(X_dropped.columns.get_loc(feat))
            else:
                # If features were provided as integer indices, allow that too
                try:
                    idx = int(feat)
                    if 0 <= idx < n_features:
                        drop_idx.append(idx)
                    else:
                        logging.warning(
                            f"Warning: feature index {idx} out of range; skipping."
                        )
                except Exception:
                    logging.warning(
                        f"Warning: feature '{feat}' not found in X.columns; skipping."
                    )
                    continue

        if drop_idx:
            X_dropped.iloc[:, drop_idx] = 0

        y_pred = _predict_labels(model, X_dropped)
        accuracy = accuracy_score(y, y_pred)
        scores.append(accuracy)
        logging.info(
            f"Feature importance dropout ({pct*100:.1f}% features dropped) accuracy score {accuracy:.4f}"
        )

    return scores


# Computes the score and robustness of the given model on the given dataset (X, y) and feature importance
def compute_model_score_and_robustness(model, X, y, feature_importances=None, dist_name="In-Distribution"):
    # Baseline
    baseline_accuracy, baseline_report = compute_baseline_score(model, X, y)

    # Robustness
    random_dropout_score_10 = compute_robustness_random_dropout(model, X, y, drop_pct=0.10)
    random_dropout_score_50 = compute_robustness_random_dropout(model, X, y, drop_pct=0.50)
    random_dropout_score_90 = compute_robustness_random_dropout(model, X, y, drop_pct=0.90)
    random_dropout_score_925 = compute_robustness_random_dropout(model, X, y, drop_pct=0.925)
    random_dropout_score_95 = compute_robustness_random_dropout(model, X, y, drop_pct=0.95)
    num_samples, num_different_predictions = compute_robustness_multiple_executions(model, X, y, 5)
    if feature_importances is not None:
        feature_importance_dropout_scores = compute_robustness_feature_importance_dropout(model, X, y, feature_importances)

    # Combine results into a single DataFrame for easier comparison
    results = {}
    results[(dist_name, "Baseline", "Overall", "Accuracy")] = baseline_accuracy
    for class_name, metrics in baseline_report.items():
        if isinstance(metrics, dict):
            for metric_name, val in metrics.items():
                results[(dist_name, "Classification Report", class_name, metric_name)] = val
        else:
            # For the row "accuracy" in the report (it is a float not a dict)
            results[(dist_name, "Classification Report", "Total_Accuracy", class_name)] = metrics
    results[(dist_name, "Dropout", "Random", "score")] = random_dropout_score_10
    results[(dist_name, "Dropout", "Random_10", "score")] = random_dropout_score_10
    results[(dist_name, "Dropout", "Random_50", "score")] = random_dropout_score_50
    results[(dist_name, "Dropout", "Random_90", "score")] = random_dropout_score_90
    results[(dist_name, "Dropout", "Random_925", "score")] = random_dropout_score_925
    results[(dist_name, "Dropout", "Random_95", "score")] = random_dropout_score_95
    results[(dist_name, "Consistency", "Num Samples", "Count")] = num_samples
    results[(dist_name, "Consistency", "Inconsistent Predictions", "Count")] = num_different_predictions
    if feature_importances is not None:
        for threshold, score in zip(["0.1%", "0.5%", "1.0%", "2.0%"], feature_importance_dropout_scores):
            results[(dist_name, "Dropout", f"FI_{threshold}", "Accuracy")] = score
    
    return pd.DataFrame.from_dict([results])




# ==============================================================================
# Temporary test to analyse the OOD Dataset
# ==============================================================================
COARSE_MAPPING = {
    'CD14+ Monocyte': 'Myeloid', 'CD16+ Monocyte': 'Myeloid',
    'CD1C+ dendritic cell': 'Myeloid', 'Plasmacytoid dendritic cell': 'Myeloid',
    'CD4 Memory T cell': 'T_cell', 'CD4 Naive T cell': 'T_cell',
    'CD8 Memory T cell': 'T_cell', 'CD8 Naive T cell': 'T_cell',
    'Gamma-delta T cell': 'T_cell', 'MAIT': 'T_cell', 'T regulatory cell': 'T_cell',
    'NK cell': 'NK_cell',
    'Memory B cell': 'B_cell', 'Naive B cell': 'B_cell', 'Plasma cell': 'B_cell'
}

def run_full_ood_evaluation(model, X_ood, y_true_ood, output_prefix="ood_metrics"):
    """
    Führt alle OOD-Analysen durch und gibt Ergebnisse im Terminal sowie als Datei aus.
    """
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', 1000)

    # 1. Modell-Vorhersagen & Wahrscheinlichkeiten
    y_pred_ood = model.predict(X_ood)
    probs_ood = model.predict_proba(X_ood)

    # 2. Text-Ausgabe der Confusion Matrix
    print("\n" + "="*80)
    print("--- OOD TEXT CONFUSION MATRIX (%) ---")
    print("="*80)
    cm_perc = pd.crosstab(
        pd.Series(y_true_ood, name='True_Author'),
        pd.Series(y_pred_ood, name='Pred_Model'),
        normalize='index'
    ) * 100
    print(cm_perc.round(1))
    cm_perc.to_csv(f"{output_prefix}_confusion_matrix_perc.csv")

    # 3. Standard Classification Report (Fine Level)
    print("\n" + "="*80)
    print("--- FINE LEVEL CLASSIFICATION REPORT ---")
    print("="*80)
    report_fine_str = classification_report(y_true_ood, y_pred_ood, digits=4)
    print(report_fine_str)

    report_fine_dict = classification_report(y_true_ood, y_pred_ood, output_dict=True)

    # 4. Hierarchische Evaluierung (Coarse Level)
    y_true_coarse = [COARSE_MAPPING.get(lbl, 'Unknown') for lbl in y_true_ood]
    y_pred_coarse = [COARSE_MAPPING.get(lbl, 'Unknown') for lbl in y_pred_ood]

    print("\n" + "="*80)
    print("--- COARSE LEVEL (LINEAGE) CLASSIFICATION REPORT ---")
    print("="*80)
    report_coarse_str = classification_report(y_true_coarse, y_pred_coarse, digits=4)
    print(report_coarse_str)

    # 5. Konfidenz- & Entropie-Analyse
    max_probs = np.max(probs_ood, axis=1)
    pred_entropies = entropy(probs_ood.T)

    conf_df = pd.DataFrame({
        'true_label': y_true_ood,
        'pred_label': y_pred_ood,
        'confidence': max_probs,
        'entropy': pred_entropies,
        'is_correct': (np.array(y_true_ood) == np.array(y_pred_ood))
    })

    print("\n" + "="*80)
    print("--- MODELL-KONFIDENZ UND ENTROPIE PRO ZELLTYP ---")
    print("="*80)
    summary_conf = conf_df.groupby('true_label').agg(
        mean_confidence=('confidence', 'mean'),
        mean_entropy=('entropy', 'mean'),
        accuracy=('is_correct', 'mean')
    ).round(4)
    print(summary_conf)

    # 6. JSON Export aller aggregierten Kennzahlen (für lokales Plotten)
    metrics_summary = {
        'overall_accuracy_fine': float(accuracy_score(y_true_ood, y_pred_ood)),
        'macro_f1_fine': float(f1_score(y_true_ood, y_pred_ood, average='macro')),
        'overall_accuracy_coarse': float(accuracy_score(y_true_coarse, y_pred_coarse)),
        'macro_f1_coarse': float(f1_score(y_true_coarse, y_pred_coarse, average='macro')),
        'mean_ood_confidence': float(np.mean(max_probs)),
        'mean_ood_entropy': float(np.mean(pred_entropies))
    }

    with open(f"{output_prefix}_summary.json", "w") as f:
        json.dump(metrics_summary, f, indent=4)

    conf_df.to_csv(f"{output_prefix}_confidence_per_cell.csv", index=False)
    print(f"\n[INFO] Evaluierung abgeschlossen. Dateien '{output_prefix}_*' wurden gespeichert.")



# Tests the robustness of the given model on the given dataset (X, y) as well as on an out-of-distribution dataset loaded from the given path.
# The score and robustness are computed on both datasets and reported.
# If X is sparse then gene_names must be provided to convert it into a dataframe. If it is not provided the test will be skipped.
def test_robustness(
    model,
    X,
    y,
    labels="scumi-annotation",
    ood_dataset_path="data/humancellatlas/5f29c29a-51c6-435c-8ff0-2b2a9d05ebee/BL_standard_design_annotated.h5ad",
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
        model, X, y, feature_importances=feature_importances, dist_name="In-Distribution"
    )

    train_classes = set(y.unique())

    logging.info("--- Out of data distribution ---")
    if ood_dataset_path is None:
        logging.error(
            "No out-of-distribution dataset path provided. Skipping out-of-distribution tests."
        )
        return
    # Assume the dataset at the given path contains raw counts
    complete_adata = ad.io.read_h5ad(ood_dataset_path)
    adata = complete_adata[complete_adata.obs[labels].isin(train_classes)].copy()

    # Prepare Adata for Doublet Detection
    # 1. Remove NaN values from batch_id after filtering
    adata = adata[adata.obs["batch_id"].notna()].copy()
    sc.pp.filter_cells(adata, min_genes=1)
    sc.pp.filter_genes(adata, min_cells=1)
    
    # 2. Filter empty cells and genes
    sc.pp.filter_cells(adata, min_genes=1)
    sc.pp.filter_genes(adata, min_cells=1)

    # 3. Exclude too small batches
    min_cells_per_batch = 30
    batch_counts = adata.obs["batch_id"].value_counts()
    valid_batches = batch_counts[batch_counts >= min_cells_per_batch].index
    adata = adata[adata.obs["batch_id"].isin(valid_batches)].copy()

    # 3. Remove unused batch_ids
    if str(adata.obs["batch_id"].dtype) == "category":
        adata.obs["batch_id"] = (
            adata.obs["batch_id"].cat.remove_unused_categories()
        )

    # Preprocess the dataset in the same way as the training data
    adata = prepare_adata(adata, batch_key="batch_id")

    X_oodd = adata.X
    y_oodd = adata.obs[labels]

    # Filter genes that are not in the training set and reorder the remaining genes to match the training set
    ## Save mapping from gene name to index in training set for quick lookup
    train_gene_to_idx = {gene: i for i, gene in enumerate(X.columns)}

    M_test = adata.shape[1]  # Number of genes in the loaded dataset
    M_train = len(X.columns)  # Number of genes in the training set

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

    ood_results = compute_model_score_and_robustness(model, X_test, y_oodd, feature_importances, dist_name="Out-of-Distribution")

    # Temporary test OOD Dataset
    run_full_ood_evaluation(model=model, X_ood=X_test, y_true_ood=y_oodd, output_prefix="results/results_new_labels")

    combined_results = pd.concat([id_results, ood_results], axis=1)
    combined_results.columns = pd.MultiIndex.from_tuples(
        combined_results.columns,
        names=["Distribution", "Category", "Sub-Category", "Metric"]
    )
    return combined_results
