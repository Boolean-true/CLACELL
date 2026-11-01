"""Dataset-level feature rankings.

Both rankings are computed once per seed and persisted. All models that use the
same seed read the same two rankings. The custom ensembles use the opposite
ranking internally:

* custom_ensemble_linsvc_stacking -> RandomForest ranking
* custom_ensemble_rf_stacking     -> LinearSVC ranking
"""

from __future__ import annotations

import time
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC

from .logging_utils import PipelineError


def _as_frame(features, importance: np.ndarray) -> pd.DataFrame:
    frame = pd.DataFrame({"feature": list(features), "importance": np.asarray(importance)})
    frame = frame.sort_values("importance", ascending=False, kind="mergesort")
    frame.reset_index(drop=True, inplace=True)
    return frame


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
