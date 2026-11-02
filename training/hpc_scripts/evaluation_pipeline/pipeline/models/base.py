"""Common adapter interface for all model families."""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd


class ModelAdapter:
    """Minimal interface used by the hierarchical wrapper and the evaluator."""

    def fit(self, X: pd.DataFrame, y: pd.Series, meta: pd.DataFrame | None = None):
        raise NotImplementedError

    def predict(self, X: pd.DataFrame, meta: pd.DataFrame | None = None):
        raise NotImplementedError


class ConstantClassifier(ModelAdapter):
    """Fallback for a hierarchy node with only one usable class."""

    def __init__(self, label: str):
        self.label = str(label)
        self.classes_ = np.array([self.label])

    def fit(self, X, y, meta=None):
        return self

    def predict(self, X, meta=None):
        return np.full(len(X), self.label, dtype=object)

    def predict_proba(self, X, meta=None):
        proba = np.zeros((len(X), 1), dtype=float)
        proba[:, 0] = 1.0
        return proba


def collect_epochs(model: Any) -> float:
    """Sum epochs over a flat model or a fitted hierarchical cascade."""
    total = 0
    seen = 0
    if hasattr(model, "coarse_classifier"):
        inner = getattr(model, "coarse_classifier", None)
        epoch = getattr(inner, "epochs_", None) if inner is not None else None
        if epoch is not None:
            total += int(epoch)
            seen += 1
        for inner in getattr(model, "fine_classifiers", {}).values():
            epoch = getattr(inner, "epochs_", None)
            if epoch is not None:
                total += int(epoch)
                seen += 1
    else:
        epoch = getattr(model, "epochs_", None)
        if epoch is not None:
            total += int(epoch)
            seen += 1
    return float(total) if seen else float("nan")
