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


# Computes the score and robustness of the given model
# If X and y are not provided the dataset is loaded from the given path and the score and robustness are computed on that dataset.
def compute_model_score_and_robustness(model, X, y, dataset_path='../blood/10x-rep1-kallisto-cellbender/10x-rep1-kallisto-cellbender'):
    if X is None or y is None:
        dataset = ad.io.read_h5ad(dataset_path)
        X = dataset.X #TODO: Ist das der richtige Weg um die Genexpressionsdaten zu erhalten?
        y = dataset.obs['annotation']

    # Basline
    compute_baseline_score(model, X, y)

    # Robustness
    compute_robustness_random_dropout(model, X, y)