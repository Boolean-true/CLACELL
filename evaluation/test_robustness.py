import anndata as ad
import numpy as np
from sklearn.metrics import accuracy_score


def _drop_features(X, pct: float, rng: np.random.Generator):
    if pct <= 0:
        return X
    n_features = X.shape[1]
    n_drop = max(1, int(n_features * pct))
    drop_idx = rng.choice(n_features, size=n_drop, replace=False)

    # Keep DataFrame columns so sklearn models fitted with feature names still match.
    if hasattr(X, "iloc") and hasattr(X, "columns"):
        X_copy = X.copy()
        X_copy.iloc[:, drop_idx] = 0
        return X_copy

    print('No DataFrame')
    X_copy = np.array(X, copy=True)
    X_copy[:, drop_idx] = 0
    return X_copy


# Computes the score on all features (baseline)
def compute_baseline_score(model, X, y):
    y_pred = model.predict(X)
    accuracy = accuracy_score(y, y_pred)
    print(f"Baseline accuracy score {accuracy:.4f}")

# Computes the robustness of the model by randomly dropping 10% of the features and evaluating the score again.
# This is done 10 times and the average score is reported.
def compute_robustness_random_dropout(model, X, y):
    scores = []
    for _ in range(10):
        rng = np.random.default_rng()
        dropped = _drop_features(X, 0.10, rng)
        y_pred = model.predict(dropped)
        accuracy = accuracy_score(y, y_pred)
        scores.append(accuracy)
    print(f"Random dropout accuracy score {np.mean(scores):.4f}")

# Computes the robustness of the model by executing it multiple times and check if the predictions are consistent across executions.
# The average score is reported.
def compute_robustness_multiple_executions(model, X, y, n_executions=5):
    results = []
    for _ in range(n_executions):
        y_pred = model.predict(X)
        results.append(y_pred)
    
    # Check if the predictions are consistent across executions
    num_samples = len(y)
    num_different_predictions = 0
    for i in range(num_samples):
        for j in range(n_executions):
            for k in range(j + 1, n_executions):
                if results[j][i] != results[k][i]:
                    num_different_predictions += 1

    print(f"Total samples: {num_samples}")
    print(f"Number of inconsistent predictions: {num_different_predictions}")

# Computes the robustness of the model by dropping the features with the highest importance scores and evaluating the score again.
# This is done for different percentages of dropped features and the scores are reported.
# feature_importances should be a pandas dataframe with columns "feature" and "importance" sorted by importance in descending order. The "feature" column can contain feature names that are not present in the dataset.
def compute_robustness_feature_importance_dropout(model, X, y, feature_importances):
    scores = []
    for pct in [0.05, 0.10, 0.15, 0.20, 0.25, 0.30]:
        n_features = X.shape[1]
        n_drop = max(1, int(n_features * pct))

        # Extract top features from feature_importances
        if hasattr(feature_importances, "iloc") and hasattr(feature_importances, "columns"):
            feature_col = None
            for column in feature_importances.columns:
                if str(column).lower() == "feature":
                    feature_col = column
                    break

            if feature_col is None:
                if len(feature_importances.columns) >= 1:
                    feature_col = feature_importances.columns[0]
                    print(f"Warning: could not find a column named 'feature'; using '{feature_col}' as feature column.")
                else:
                    print("feature_importances dataframe has no columns; skipping this pct")
                    continue

            top_features = feature_importances[feature_col].iloc[:n_drop].tolist()
        else:
            # assume list/array/series-like of feature identifiers (names or indices)
            try:
                top_features = list(feature_importances)[:n_drop]
            except Exception:
                print("feature_importances has unexpected format; skipping this pct")
                continue

        # Prepare a copy of X with selected features zeroed
        if hasattr(X, "iloc") and hasattr(X, "columns"):
            # X has column names -> interpret top_features as names when possible
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
                            print(f"Warning: feature index {idx} out of range; skipping.")
                    except Exception:
                        print(f"Warning: feature '{feat}' not found in X.columns; skipping.")

            if drop_idx:
                X_dropped.iloc[:, drop_idx] = 0

        else:
            # X is array-like / sparse: interpret top_features as integer indices
            X_dropped = np.array(X, copy=True)
            int_idx = []
            for feat in top_features:
                if isinstance(feat, (int, np.integer)):
                    idx = int(feat)
                    if 0 <= idx < n_features:
                        int_idx.append(idx)
                    else:
                        print(f"Warning: feature index {idx} out of range; skipping.")
                else:
                    # cannot map string feature names to array columns
                    try:
                        # attempt numeric conversion
                        idx = int(feat)
                        if 0 <= idx < n_features:
                            int_idx.append(idx)
                    except Exception:
                        print(f"Warning: feature '{feat}' is not an integer and X has no column labels; skipping.")

            if int_idx:
                X_dropped[:, int_idx] = 0

        y_pred = model.predict(X_dropped)
        accuracy = accuracy_score(y, y_pred)
        scores.append(accuracy)
        print(f"Feature importance dropout ({pct*100:.0f}% features dropped) accuracy score {accuracy:.4f}")

    return scores


# Computes the score and robustness of the given model
# If X and y are not provided the dataset is loaded from the given path and the score and robustness are computed on that dataset.
def compute_model_score_and_robustness(model, X, y, dataset_path='../blood/10x-rep1-kallisto-cellbender/10x-rep1-kallisto-cellbender', feature_importances=None):
    if X is None or y is None:
        dataset = ad.io.read_h5ad(dataset_path)
        X = dataset.X#dataset.to_df(layer="counts")
        y = dataset.obs['anno']#dataset.obs['annotation']

    # Baseline
    compute_baseline_score(model, X, y)

    # Robustness
    compute_robustness_random_dropout(model, X, y)
    compute_robustness_multiple_executions(model, X, y, 5)
    if feature_importances is not None:
        compute_robustness_feature_importance_dropout(model, X, y, feature_importances)