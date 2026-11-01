"""Generic hierarchical cascade classifier.

Functionally identical to the previous
``HierarchicalCascadeClassifier`` from
``run_multiple_trainings_hierarchical_custom_ensemble_rf_stacking.py``:

1. fit one coarse classifier on all training cells,
2. fit one fine classifier per coarse label (on that coarse subset),
3. map leaf coarse labels to their single fine class,
4. predict coarse first, then route each test cell to its fine classifier.

The only difference is that the model factory is injected, so the same
wrapper can hold autoencoders, conditional autoencoders and custom ensembles.
"""

from __future__ import annotations

import logging
from typing import Callable

import numpy as np
import pandas as pd

from .logging_utils import PipelineError
from .models.base import ModelAdapter


class HierarchicalCascadeClassifier(ModelAdapter):
    def __init__(
        self,
        coarse_factory: Callable[[], ModelAdapter],
        fine_factories: dict[str, Callable[[], ModelAdapter]],
        min_fine_classes: int = 2,
        name: str = "hierarchical",
    ):
        self.coarse_factory = coarse_factory
        self.fine_factories = fine_factories
        self.min_fine_classes = int(min_fine_classes)
        self.name = name
        self.coarse_classifier = None
        self.fine_classifiers: dict[str, ModelAdapter] = {}
        self.hierarchy_mapping: dict[str, np.ndarray] = {}
        self.leaf_mapping: dict[str, str] = {}

    @staticmethod
    def _subset(X, mask):
        if hasattr(X, "iloc"):
            return X.iloc[mask]
        return X[mask]

    def fit(
        self,
        X: pd.DataFrame,
        y_coarse: pd.Series,
        y_fine: pd.Series,
        sample_meta: pd.DataFrame | None = None,
    ):
        if not isinstance(y_coarse, pd.Series):
            y_coarse = pd.Series(np.asarray(y_coarse), index=X.index)
        if not isinstance(y_fine, pd.Series):
            y_fine = pd.Series(np.asarray(y_fine), index=X.index)
        if len(y_coarse) != len(X) or len(y_fine) != len(X):
            raise PipelineError(
                f"Hierarchical fit length mismatch: X={len(X)}, "
                f"y_coarse={len(y_coarse)}, y_fine={len(y_fine)}."
            )
        y_coarse = y_coarse.astype(str)
        y_fine = y_fine.astype(str)

        logging.info("  -> fitting coarse model (%d cells)", len(X))
        self.coarse_classifier = self.coarse_factory()
        try:
            self.coarse_classifier.fit(X, y_coarse, sample_meta)
        except Exception as exc:  # noqa: BLE001 - add hierarchy context
            raise PipelineError(
                f"Coarse model fit failed for model '{self.name}' "
                f"({len(X)} cells, {y_coarse.nunique()} classes)."
            ) from exc

        for coarse_label in np.unique(y_coarse):
            coarse_label = str(coarse_label)
            mask = (y_coarse == coarse_label).to_numpy()
            X_subset = self._subset(X, mask)
            y_fine_subset = y_fine.iloc[mask]
            meta_subset = sample_meta.iloc[mask] if sample_meta is not None else None
            unique_fine = np.unique(y_fine_subset.astype(str))
            self.hierarchy_mapping[coarse_label] = unique_fine

            if len(unique_fine) >= self.min_fine_classes:
                factory = self.fine_factories.get(coarse_label)
                if factory is None:
                    raise PipelineError(
                        f"No fine model factory for coarse label '{coarse_label}'. "
                        f"Available: {sorted(self.fine_factories)}"
                    )
                logging.info(
                    "  -> fitting fine model '%s' (%d cells, %d fine classes)",
                    coarse_label,
                    len(X_subset),
                    len(unique_fine),
                )
                fine_model = factory()
                try:
                    fine_model.fit(X_subset, y_fine_subset, meta_subset)
                except Exception as exc:  # noqa: BLE001 - add hierarchy context
                    raise PipelineError(
                        f"Fine model fit failed for model '{self.name}', coarse label "
                        f"'{coarse_label}' ({len(X_subset)} cells, "
                        f"{len(unique_fine)} fine classes)."
                    ) from exc
                self.fine_classifiers[coarse_label] = fine_model
            else:
                self.leaf_mapping[coarse_label] = str(unique_fine[0])
                logging.info(
                    "  -> leaf coarse label '%s' -> '%s' (no fine model)",
                    coarse_label,
                    unique_fine[0],
                )

        all_fine = []
        for labels in self.hierarchy_mapping.values():
            all_fine.extend(labels.tolist())
        self.classes_ = np.unique(all_fine)
        return self

    def predict_coarse(self, X: pd.DataFrame, meta: pd.DataFrame | None = None):
        if self.coarse_classifier is None:
            raise PipelineError("Hierarchical model is not fitted (coarse classifier missing).")
        return self.coarse_classifier.predict(X, meta)

    def predict_fine(
        self,
        X: pd.DataFrame,
        coarse_preds=None,
        sample_meta: pd.DataFrame | None = None,
    ):
        if not self.fine_classifiers and not self.leaf_mapping:
            raise PipelineError("Hierarchical model is not fitted (no fine/leaf models).")
        if coarse_preds is None:
            coarse_preds = self.predict_coarse(X, sample_meta)
        coarse_preds = np.asarray(coarse_preds)
        fine_preds = np.empty_like(coarse_preds, dtype=object)
        for coarse_label_raw in np.unique(coarse_preds):
            coarse_label = str(coarse_label_raw)
            mask = coarse_preds == coarse_label_raw
            if coarse_label in self.fine_classifiers:
                X_subset = self._subset(X, mask)
                meta_subset = sample_meta.iloc[mask] if sample_meta is not None else None
                fine_preds[mask] = self.fine_classifiers[coarse_label].predict(
                    X_subset, meta_subset
                )
            elif coarse_label in self.leaf_mapping:
                fine_preds[mask] = self.leaf_mapping[coarse_label]
            elif coarse_label in self.hierarchy_mapping:
                fine_preds[mask] = self.hierarchy_mapping[coarse_label][0]
            else:
                raise PipelineError(
                    f"Coarse prediction '{coarse_label}' is not present in the fitted hierarchy. "
                    f"Known coarse labels: {sorted(self.hierarchy_mapping)}"
                )
        return fine_preds

    def predict(self, X: pd.DataFrame, meta: pd.DataFrame | None = None):
        coarse_preds = self.predict_coarse(X, meta)
        fine_preds = self.predict_fine(X, coarse_preds=coarse_preds, sample_meta=meta)
        return coarse_preds, fine_preds
