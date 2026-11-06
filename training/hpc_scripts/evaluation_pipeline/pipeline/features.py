"""Dataset-level feature rankings.

The RandomForest and LinearSVC rankings are computed once per seed and
persisted. All models that use the same seed read the same two rankings. The
custom ensembles use the opposite ranking internally:

* custom_ensemble_linsvc_stacking -> RandomForest ranking
* custom_ensemble_rf_stacking     -> LinearSVC ranking

The robustness ranking is separate: ``feature_importance_differential_expression``
is computed once per dataset by the prepare stage from the training expression
matrix.
"""

from __future__ import annotations

import logging
import pickle
import time
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC

from . import __version__ as PIPELINE_VERSION
from .io import atomic_write_pickle
from .logging_utils import PipelineError


def fit_scaler(X) -> StandardScaler:
    scaler = StandardScaler(with_mean=False).set_output(transform="pandas")
    return scaler.fit(X)


def load_scaler(
    path: str | Path,
    expected_cache_key: str | None = None,
) -> StandardScaler:
    path = Path(path)
    if not path.is_file():
        raise PipelineError(
            f"Scaler not found at {path}. Run the features stage first."
        )
    with path.open("rb") as handle:
        payload = pickle.load(handle)
    if not isinstance(payload, dict) or "scaler" not in payload:
        raise PipelineError(
            f"Invalid scaler file at {path}. Re-run the features stage."
        )
    stored_version = payload.get("pipeline_version")
    if stored_version != PIPELINE_VERSION:
        raise PipelineError(
            f"Scaler at {path} was written by pipeline version '{stored_version}', "
            f"current is '{PIPELINE_VERSION}'. Re-run the features stage."
        )
    stored_key = payload.get("cache_key")
    if expected_cache_key is not None and stored_key != expected_cache_key:
        raise PipelineError(
            f"Scaler at {path} belongs to cache '{stored_key}', expected "
            f"'{expected_cache_key}'. Re-run the features stage."
        )
    return payload["scaler"]


def ensure_scaler(path: str | Path, X, cache_key: str | None) -> StandardScaler:
    """Reuse the dataset scaler if it is valid, otherwise fit and persist it."""
    path = Path(path)
    if path.is_file():
        try:
            return load_scaler(path, expected_cache_key=cache_key)
        except Exception as exc:  # noqa: BLE001 - rebuild corrupt/stale cache file
            logging.warning("Replacing unusable scaler at %s: %s", path, exc)
    scaler = fit_scaler(X)
    atomic_write_pickle(
        path,
        {
            "pipeline_version": PIPELINE_VERSION,
            "cache_key": cache_key,
            "scaler": scaler,
        },
    )
    return scaler


def feature_importance_differential_expression(
    adata,
    label_col: str,
) -> list[str]:
    """Interleaved Wilcoxon differential-expression ranking."""
    import scanpy as sc

    adata.obs[label_col] = adata.obs[label_col].astype(str)
    sc.tl.rank_genes_groups(adata, groupby=label_col, method="wilcoxon", use_raw=False)
    de_names_df = pd.DataFrame(adata.uns["rank_genes_groups"]["names"])

    de_genes_ordered = []
    seen = set()
    for row_idx in range(de_names_df.shape[0]):
        for cell_type in de_names_df.columns:
            gene = de_names_df.iloc[row_idx][cell_type]
            if gene not in seen:
                seen.add(gene)
                de_genes_ordered.append(gene)
    return de_genes_ordered


def _as_frame(features, importance: np.ndarray) -> pd.DataFrame:
    importance = np.asarray(importance)
    order = np.argsort(importance)[::-1]
    frame = pd.DataFrame(
        {
            "feature": np.asarray(features)[order],
            "importance": importance[order],
        }
    )
    return frame.reset_index(drop=True)


def feature_importance_randomforest(
    X: pd.DataFrame,
    y: pd.Series,
    seed: int,
    n_jobs: int = 1,
) -> tuple[pd.DataFrame, float]:
    """Impurity-based RandomForest ranking (same estimator as the old scripts)."""
    start = time.time()
    model = RandomForestClassifier(
        random_state=seed,
        n_jobs=max(1, int(n_jobs)),
    )
    model.fit(X, y)
    frame = _as_frame(X.columns, model.feature_importances_)
    return frame, (time.time() - start) / 60.0


def feature_importance_linearsvc(
    X: pd.DataFrame,
    y: pd.Series,
    seed: int,
) -> tuple[pd.DataFrame, float]:
    """Mean absolute LinearSVC coefficient ranking."""
    start = time.time()
    model = LinearSVC(random_state=seed)
    model.fit(X, y)
    importance = np.mean(np.abs(model.coef_), axis=0)
    frame = _as_frame(X.columns, importance)
    return frame, (time.time() - start) / 60.0


def load_ranking(features_dir: str | Path, method: str) -> pd.DataFrame:
    path = Path(features_dir) / f"feature_importance_{method}.pkl"
    if not path.is_file():
        available = sorted(p.name for p in Path(features_dir).glob("feature_importance_*.pkl"))
        raise PipelineError(
            f"Feature ranking '{method}' not found at {path}. Available: {available}. "
            "Run the features stage for this seed."
        )
    frame = pd.read_pickle(path)
    if "feature" not in frame.columns:
        frame = frame.rename(columns={frame.columns[0]: "feature"})
    return frame


def sorted_genes(features_dir: str | Path, method: str) -> list[str]:
    return list(load_ranking(features_dir, method)["feature"])
