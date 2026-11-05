"""Custom stacking ensembles with gene-subset diversity."""

from __future__ import annotations

import random

import numpy as np
import pandas as pd
from sklearn.calibration import CalibratedClassifierCV
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier, StackingClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from skopt import BayesSearchCV
from skopt.space import Categorical, Integer, Real

from custom_stopper import CustomStopper

from ..logging_utils import PipelineError
from .base import ModelAdapter


def _base_estimator(
    base: str,
    params: dict,
    seed: int,
    calibration_cv: int = 5,
):
    params = dict(params or {})
    params["class_weight"] = "balanced"
    if base in {"randomforest", "rf"}:
        return RandomForestClassifier(
            random_state=seed,
            n_jobs=1,
            **params,
        )
    if base in {"linearsvc", "linsvc"}:
        svc = LinearSVC(random_state=seed, **params)
        return CalibratedClassifierCV(svc, cv=calibration_cv, n_jobs=1)
    raise PipelineError(f"Unknown custom ensemble base '{base}'. Valid: randomforest, linearsvc.")


def _tune_rf(X, y, tune_cfg: dict, seed: int, n_jobs: int) -> tuple[dict, dict]:
    search = BayesSearchCV(
        estimator=RandomForestClassifier(class_weight="balanced", random_state=seed),
        search_spaces={
            "n_estimators": Integer(100, 250, prior="log-uniform"),
            "max_depth": Integer(10, 30),
            "max_features": Categorical(["sqrt", "log2"]),
        },
        n_iter=int(tune_cfg.get("n_iter", 30)),
        cv=int(tune_cfg.get("cv", 5)),
        scoring="accuracy",
        n_jobs=n_jobs,
        verbose=10,
    )
    np.random.seed(seed)
    random.seed(seed)
    search.fit(X, y, callback=CustomStopper(patience=5, min_delta=0.002, min_iter=15))
    print(f"\nSearch terminated after {len(search.cv_results_['mean_test_score'])} Iterations.")
    print(f"Best hyperparameters: {search.best_params_}")
    print(f"Test-Split Accuracy:  {search.score(X, y):.4f}")
    cv_results = search.cv_results_
    mean_fit = np.asarray(cv_results.get("mean_fit_time", [0.0]))
    mean_score = np.asarray(cv_results.get("mean_score_time", [0.0]))
    return dict(search.best_params_), {
        "skipped": False,
        "cv": int(tune_cfg.get("cv", 5)),
        "n_iter": int(tune_cfg.get("n_iter", 30)),
        "best_score": float(search.best_score_),
        "avg_time_per_iteration_sec": float(
            np.mean(mean_fit + mean_score) * int(tune_cfg.get("cv", 5))
        ),
        "n_candidates": len(cv_results.get("params", [])),
    }


def _tune_linsvc(
    X,
    y,
    tune_cfg: dict,
    seed: int,
    n_jobs: int,
) -> tuple[dict, dict]:
    search = BayesSearchCV(
        estimator=LinearSVC(class_weight="balanced", random_state=seed),
        search_spaces=[
            {
                "C": Real(1e-3, 2.0, prior="log-uniform"),
                "penalty": Categorical(["l1"]),
                "dual": Categorical([False]),
                "tol": Real(1e-4, 1e-2, prior="log-uniform"),
            },
            {
                "C": Real(1e-3, 2.0, prior="log-uniform"),
                "penalty": Categorical(["l2"]),
                "dual": Categorical([True, False]),
                "tol": Real(1e-4, 1e-2, prior="log-uniform"),
            },
        ],
        n_iter=int(tune_cfg.get("n_iter", 30)),
        cv=int(tune_cfg.get("cv", 5)),
        scoring="accuracy",
        n_jobs=n_jobs,
        verbose=10,
    )
    np.random.seed(seed)
    random.seed(seed)
    search.fit(X, y, callback=CustomStopper(patience=5, min_delta=0.002, min_iter=15))
    print(f"\nSearch terminated after {len(search.cv_results_['mean_test_score'])} Iterations.")
    print(f"Best hyperparameters: {search.best_params_}")
    print(f"Test-Split Accuracy:  {search.score(X, y):.4f}")
    cv_results = search.cv_results_
    mean_fit = np.asarray(cv_results.get("mean_fit_time", [0.0]))
    mean_score = np.asarray(cv_results.get("mean_score_time", [0.0]))
    return dict(search.best_params_), {
        "skipped": False,
        "cv": int(tune_cfg.get("cv", 5)),
        "n_iter": int(tune_cfg.get("n_iter", 30)),
        "best_score": float(search.best_score_),
        "avg_time_per_iteration_sec": float(
            np.mean(mean_fit + mean_score) * int(tune_cfg.get("cv", 5))
        ),
        "n_candidates": len(cv_results.get("params", [])),
    }


def tune_base_estimator(
    X: pd.DataFrame,
    y: pd.Series,
    base: str,
    tune_cfg: dict,
    seed: int,
    n_jobs: int,
) -> tuple[dict, dict]:
    min_class = int(pd.Series(y).astype(str).value_counts().min())
    effective_cv = min(int(tune_cfg.get("cv", 5)), min_class)
    if effective_cv < 2:
        return {}, {
            "skipped": True,
            "skip_reason": f"min class count is {min_class}; CV needs at least 2.",
            "cv": effective_cv,
            "n_iter": 0,
            "best_score": float("nan"),
            "avg_time_per_iteration_sec": float("nan"),
        }
    tune_cfg = dict(tune_cfg)
    tune_cfg["cv"] = effective_cv
    search_mode = str(tune_cfg.get("search", "bayes")).lower()
    if search_mode != "bayes":
        raise PipelineError(
            f"Custom ensembles use BayesSearchCV; got tune.search='{search_mode}'."
        )
    if base in {"randomforest", "rf"}:
        return _tune_rf(X, y, tune_cfg, seed, n_jobs)
    if base in {"linearsvc", "linsvc"}:
        return _tune_linsvc(X, y, tune_cfg, seed, n_jobs)
    raise PipelineError(f"Unknown custom ensemble base '{base}'. Valid: randomforest, linearsvc.")


def build_custom_ensemble(
    sorted_top_genes: list[str],
    base: str,
    tuned_params: dict,
    params_cfg: dict,
    seed: int,
    n_jobs: int,
):
    total_genes = len(sorted_top_genes)
    if total_genes == 0:
        raise PipelineError("Cannot build a custom ensemble with zero genes.")
    drop_fractions = params_cfg.get("drop_fractions", [0.0075, 0.015, 0.025])
    subsets = [sorted_top_genes]
    for fraction in drop_fractions:
        n_drop = int(total_genes * float(fraction))
        subsets.append(sorted_top_genes[n_drop:])
    subset_names = ["all"] + [str(fraction).replace(".", "_") for fraction in drop_fractions]
    calibration_cv = max(2, int(params_cfg.get("calibration_cv", 5)))
    combine = str(params_cfg.get("combine", "stacking")).lower()

    estimators = []
    for name, features in zip(subset_names, subsets):
        model = _base_estimator(base, tuned_params, seed, calibration_cv)
        estimators.append(
            (
                name,
                Pipeline(
                    [
                        (
                            "select",
                            ColumnTransformer(
                                transformers=[("keep", "passthrough", features)],
                                remainder="drop",
                            ),
                        ),
                        (f"{base}_{name}", model),
                    ]
                ),
            )
        )

    if combine == "stacking":
        ensemble = StackingClassifier(
            estimators=estimators,
            final_estimator=LogisticRegression(max_iter=1000),
            cv=int(params_cfg.get("stacking_cv", 5)),
            n_jobs=n_jobs,
            passthrough=bool(params_cfg.get("passthrough", False)),
        )
    elif combine == "voting":
        ensemble = VotingClassifier(
            estimators=estimators,
            voting="soft",
        )
    else:
        raise PipelineError(
            f"Unknown custom ensemble combine '{combine}'. Valid: stacking, voting."
        )

    return ensemble


class _CustomEnsembleAdapter(ModelAdapter):
    def __init__(self, estimator):
        self.estimator = estimator

    def fit(self, X, y, meta=None):
        self.estimator.fit(X, y)
        return self

    def predict(self, X, meta=None):
        return self.estimator.predict(X)

    def predict_proba(self, X, meta=None):
        return self.estimator.predict_proba(X)

    @property
    def classes_(self):
        return getattr(self.estimator, "classes_", None)


def build_custom_ensemble_adapter(
    sorted_top_genes: list[str],
    base: str,
    tuned_params: dict,
    params_cfg: dict,
    seed: int,
    n_jobs: int,
) -> ModelAdapter:
    return _CustomEnsembleAdapter(
        build_custom_ensemble(
            sorted_top_genes=sorted_top_genes,
            base=base,
            tuned_params=tuned_params,
            params_cfg=params_cfg,
            seed=seed,
            n_jobs=n_jobs,
        )
    )
