import anndata as ad
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report
import scipy.sparse as sp
import scanpy as sc
import celltypist
import logging
from pathlib import Path
from datetime import datetime
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


# Computes the score on all features (baseline)
def compute_baseline_score(model, X, y):
    y_pred = _predict_labels(model, X)
    accuracy = accuracy_score(y, y_pred)
    logging.info(f"Baseline accuracy score {accuracy:.4f}")
    logging.info(
        f"Classification Report:\n{classification_report(y, y_pred, zero_division=0)}"
    )

    return accuracy, classification_report(y, y_pred, zero_division=0, output_dict=True)


# Computes the robustness of the model by randomly dropping 10% of the features and evaluating the score again.
# This is done 10 times and the average score is reported.
def compute_robustness_random_dropout(model, X, y):
    scores = []
    for _ in range(10):
        rng = np.random.default_rng()
        dropped = _drop_features(X, 0.10, rng)
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
    random_dropout_score = compute_robustness_random_dropout(model, X, y)
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
    results[(dist_name, "Dropout", "Random", "score")] = random_dropout_score
    results[(dist_name, "Consistency", "Num Samples", "Count")] = num_samples
    results[(dist_name, "Consistency", "Inconsistent Predictions", "Count")] = num_different_predictions
    if feature_importances is not None:
        for threshold, score in zip(["0.1%", "0.5%", "1.0%", "2.0%"], feature_importance_dropout_scores):
            results[(dist_name, "Dropout", f"FI_{threshold}", "Accuracy")] = score
    
    return pd.DataFrame.from_dict([results])


# Tests the robustness of the given model on the given dataset (X, y) as well as on an out-of-distribution dataset loaded from the given path.
# The score and robustness are computed on both datasets and reported.
# If X is sparse then gene_names must be provided to convert it into a dataframe. If it is not provided the test will be skipped.
def test_robustness(
    model,
    X,
    y,
    labels="scumi-annotation",
    ood_dataset_path="../data/humancellatlas/5f29c29a-51c6-435c-8ff0-2b2a9d05ebee/BL_standard_design_annotated.h5ad",
    feature_importances=None,
    gene_names=None,
    log_to_console=True,
    log_to_file=False,
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

    # Preprocess the dataset in the same way as the training data

    # mitochondrial genes, "MT-" for human, "Mt-" for mouse
    adata.var["mt"] = adata.var_names.str.startswith("MT-")
    # ribosomal genes
    adata.var["ribo"] = adata.var_names.str.startswith(("RPS", "RPL"))
    # hemoglobin genes
    adata.var["hb"] = adata.var_names.str.contains("^HB[^(P)]")

    sc.pp.calculate_qc_metrics(
        adata, qc_vars=["mt", "ribo", "hb"], inplace=True, log1p=True
    )

    # Remove mitochondrial, ribosomal and hemoglobin
    adata = adata[:, ~adata.var["mt"]].copy()
    adata = adata[:, ~adata.var["ribo"]].copy()
    adata = adata[:, ~adata.var["hb"]].copy()

    # Doublet Detection
    sc.pp.scrublet(adata, batch_key="Donor")
    adata = adata[adata.obs["predicted_doublet"] == False].copy()

    # Normalization

    # Saving count data
    adata.layers["counts"] = adata.X.copy()

    # Normalizing to median total counts
    sc.pp.normalize_total(adata, target_sum=1e4)
    # Logarithmize the data
    sc.pp.log1p(adata)

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

    ood_results = compute_model_score_and_robustness(model, X_test, y_oodd, feature_importances, dist_name="Out-of-Distribution")

    combined_results = pd.concat([id_results, ood_results], axis=1)
    combined_results.columns = pd.MultiIndex.from_tuples(
        combined_results.columns,
        names=["Distribution", "Category", "Sub-Category", "Metric"]
    )
    return combined_results
