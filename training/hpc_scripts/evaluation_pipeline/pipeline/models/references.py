"""Reference model adapters: SingleR, CellTypist and scGPT export."""

from __future__ import annotations

import logging
import random
import time
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_is_fitted
from skopt import BayesSearchCV
from skopt.space import Categorical, Real

from custom_stopper import CustomStopper

from ..io import atomic_write_json, ensure_dir, read_json
from ..logging_utils import PipelineError
from .base import ModelAdapter


class FastSingleRClassifier(BaseEstimator, ClassifierMixin):
    """The sklearn wrapper from train_singler_fast.py (reference implementation)."""

    def __init__(self, aggregate_ref: bool = True):
        self.aggregate_ref = aggregate_ref
        self.reference_ = None
        self.features_ = None
        self.classes_ = None

    def fit(self, X, y):
        import singler

        if not isinstance(X, pd.DataFrame):
            raise TypeError("SingleR requires a pandas DataFrame with gene names.")
        self.features_ = X.columns.tolist()
        self.classes_ = np.unique(y)
        if self.aggregate_ref:
            X_fit = X.groupby(y).mean()
            y_fit = X_fit.index.tolist()
        else:
            X_fit = X
            y_fit = y
        self.reference_ = singler.train_single(
            ref_data=X_fit.values.T,
            ref_labels=list(y_fit),
            ref_features=self.features_,
            test_features=self.features_,
        )
        return self

    def predict(self, X):
        check_is_fitted(self, attributes=["reference_", "features_"])
        if not isinstance(X, pd.DataFrame):
            raise TypeError("SingleR requires a pandas DataFrame with gene names.")
        import singler

        X_aligned = X.reindex(columns=self.features_, fill_value=0)
        output = singler.classify_single(X_aligned.values.T, ref_prebuilt=self.reference_)
        return np.array(output["best"])


class SingleRAdapter(ModelAdapter):
    def __init__(self, params: dict | None = None):
        self.estimator = FastSingleRClassifier(**dict(params or {}))

    def fit(self, X, y, meta=None):
        self.estimator.fit(X, y)
        return self

    def predict(self, X, meta=None):
        return self.estimator.predict(X)

    @property
    def classes_(self):
        return getattr(self.estimator, "classes_", None)


class CellTypistWrapper(BaseEstimator, ClassifierMixin):
    """CellTypist wrapper copied from train_celltypist_bayessearch.py."""

    def __init__(
        self,
        C=1.0,
        solver="saga",
        use_SGD=False,
        alpha=0.0001,
        use_GPU=False,
        mini_batch=False,
        batch_number=100,
        batch_size=1000,
        epochs=10,
        balance_cell_type=False,
        feature_selection=False,
        genes=None,
        seed=None,
    ):
        self.C = C
        self.solver = solver
        self.use_SGD = use_SGD
        self.alpha = alpha
        self.use_GPU = use_GPU
        self.mini_batch = mini_batch
        self.batch_number = batch_number
        self.batch_size = batch_size
        self.epochs = epochs
        self.balance_cell_type = balance_cell_type
        self.feature_selection = feature_selection
        self.genes = genes
        self.seed = seed

    def fit(self, X, y):
        import celltypist

        # CellTypist's mini-batch sampler uses the global numpy/random RNG, so
        # seed it for the duration of the fit. Save and restore the surrounding
        # state so this does not reset the RNG used by BayesSearchCV/skopt.
        # The estimator-level random_state below controls the sklearn solver.
        np_state = np.random.get_state()
        py_state = random.getstate()
        train_kwargs = {}
        if self.seed is not None:
            np.random.seed(int(self.seed))
            random.seed(int(self.seed))
            if not self.use_GPU:
                train_kwargs["random_state"] = int(self.seed)

        try:
            self.model_ = celltypist.train(
                X=X,
                labels=y,
                C=self.C,
                solver=self.solver,
                max_iter=1000,
                n_jobs=-1,
                use_SGD=self.use_SGD,
                alpha=self.alpha,
                use_GPU=self.use_GPU,
                mini_batch=self.mini_batch,
                batch_number=self.batch_number,
                batch_size=self.batch_size,
                epochs=self.epochs,
                balance_cell_type=self.balance_cell_type,
                feature_selection=self.feature_selection,
                check_expression=False,
                genes=list(self.genes),
                **train_kwargs
            )
        finally:
            np.random.set_state(np_state)
            random.setstate(py_state)
        self.classes_ = np.unique(y)
        return self

    def predict(self, X):
        import anndata as ad
        import celltypist

        adata_tmp = ad.AnnData(X=X)
        adata_tmp.var_names = list(self.genes)
        predictions = celltypist.annotate(adata_tmp, model=self.model_)
        return predictions.predicted_labels["predicted_labels"].astype(str).values


class CellTypistAdapter(ModelAdapter):
    def __init__(
        self,
        params: dict | None = None,
        genes: list[str] | None = None,
        seed: int | None = None,
    ):
        self.estimator = CellTypistWrapper(**dict(params or {}), genes=genes, seed=seed)

    def fit(self, X, y, meta=None):
        self.estimator.fit(X.to_numpy(copy=False), y)
        return self

    def predict(self, X, meta=None):
        return self.estimator.predict(X.to_numpy(copy=False))

    @property
    def classes_(self):
        return getattr(self.estimator, "classes_", None)


def tune_celltypist(
    X: pd.DataFrame,
    y: pd.Series,
    tune_cfg: dict,
    seed: int,
    n_jobs: int,
) -> tuple[dict, dict]:
    """Same wrapper, search space and BayesSearchCV setup as the old script."""
    genes = X.columns.astype(str).tolist()
    X_values = X.to_numpy(copy=False)
    param_distributions = [
        {
            "C": Real(1e-2, 2.0, prior="log-uniform"),
            "alpha": Real(1e-4, 1e-2, prior="log-uniform"),
            "use_SGD": Categorical([True]),
            "mini_batch": Categorical([True, False]),
            "balance_cell_type": Categorical([True, False]),
            "feature_selection": Categorical([False]),
        },
        {
            "C": Real(1e-2, 2.0, prior="log-uniform"),
            "alpha": Real(1e-4, 1e-2, prior="log-uniform"),
            "use_SGD": Categorical([True]),
            "mini_batch": Categorical([True, False]),
            "balance_cell_type": Categorical([True, False]),
            "feature_selection": Categorical([True]),
        },
    ]
    min_class = int(pd.Series(y).astype(str).value_counts().min())
    cv = min(int(tune_cfg.get("cv", 5)), min_class)
    if cv < 2:
        return {}, {
            "skipped": True,
            "skip_reason": f"min class count is {min_class}; CV needs at least 2.",
            "cv": cv,
            "n_iter": 0,
            "best_score": float("nan"),
            "avg_time_per_iteration_sec": float("nan"),
        }
    opt = BayesSearchCV(
        estimator=CellTypistWrapper(genes=genes, seed=seed),
        search_spaces=param_distributions,
        n_iter=int(tune_cfg.get("n_iter", 30)),
        cv=cv,
        scoring="accuracy",
        n_jobs=1,
        verbose=10,
    )
    stopper = CustomStopper(patience=5, min_delta=0.002, min_iter=15)
    np.random.seed(seed)
    random.seed(seed)
    start = time.time()
    opt.fit(X_values, y, callback=stopper)
    elapsed = (time.time() - start) / 60.0
    cv_results = opt.cv_results_
    mean_fit = np.asarray(cv_results.get("mean_fit_time", [0.0]))
    mean_score = np.asarray(cv_results.get("mean_score_time", [0.0]))
    return dict(opt.best_params_), {
        "skipped": False,
        "cv": cv,
        "n_iter": int(tune_cfg.get("n_iter", 30)),
        "best_score": float(opt.best_score_),
        "avg_time_per_iteration_sec": float(np.mean(mean_fit + mean_score) * cv),
        "search_time_min": elapsed,
        "n_candidates": len(cv_results.get("params", [])),
    }


class ScGPTExternalAdapter(ModelAdapter):
    """scGPT runs on a separate GPU cluster; this adapter is deliberately external."""

    def __init__(self, params: dict | None = None):
        self.params = dict(params or {})

    def fit(self, X, y, meta=None):
        raise PipelineError(
            "scGPT is an external GPU model. It is not trained on the CPU pipeline. "
            "Enable scgpt.params.export_input and run the export stage, then run "
            "finetune_integration_adjusted.py on the GPU cluster with the exported h5ad."
        )

    def predict(self, X, meta=None):
        raise PipelineError(
            "scGPT predictions are produced on the external GPU cluster and are not "
            "available inside the CPU pipeline."
        )


def scgpt_export_path(config: dict) -> Path:
    """Manifest describing the pipeline-prepared input for the external scGPT run."""
    return Path(config["cache_dir"]) / "scgpt" / "scgpt_export.json"


def export_scgpt_input(config: dict, prepare_key: str | None = None) -> Path:
    """Write the manifest for the external scGPT script.

    scGPT reads the existing prepared_train.h5ad / prepared_test.h5ad from the
    cache. Only the dataset-specific column names have to be passed along.
    """
    dataset = config["active_dataset"]
    cache_dir = Path(config["cache_dir"])
    for split in ("train", "test"):
        prepared_path = cache_dir / f"prepared_{split}.h5ad"
        if not prepared_path.is_file():
            raise PipelineError(
                f"Preprocessed {split} data not found at {prepared_path}. "
                "Run the prepare stage first."
            )

    if prepare_key is None:
        prepare_key = read_json(cache_dir / "prepare_meta.json", default={}).get("cache_key")
    manifest = {
        "train_h5ad": "prepared_train.h5ad",
        "test_h5ad": "prepared_test.h5ad",
        "batch_col": dataset["batch_key"],
        "label_cols": {
            "coarse": dataset["labels"]["coarse"],
            "fine": dataset["labels"]["fine"],
        },
        "feature_importance": "feature_importance_differential_expression.pkl",
        "prepare_cache_key": prepare_key,
        "eval_seed_base": int(config["experiment"].get("eval_seed_base", 0)),
        "note": (
            "Run evaluation_pipeline/submit_scgpt.sh on the GPU cluster with this "
            "directory. Paths are relative to the dataset cache directory."
        ),
    }
    out_path = scgpt_export_path(config)
    ensure_dir(out_path.parent)
    atomic_write_json(out_path, manifest)
    logging.info("scGPT input manifest written to %s", out_path)
    return out_path
