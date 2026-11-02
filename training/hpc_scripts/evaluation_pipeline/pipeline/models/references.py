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

from ..io import atomic_write_json, ensure_dir
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

    def fit(self, X, y):
        import celltypist

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
        )
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
    def __init__(self, params: dict | None = None, genes: list[str] | None = None):
        self.estimator = CellTypistWrapper(**dict(params or {}), genes=genes)

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
        estimator=CellTypistWrapper(genes=genes),
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
    """Path of the raw-count h5ad exported for the external scGPT run."""
    dataset = config["active_dataset"]
    return Path(config["cache_dir"]) / "scgpt" / f"{dataset['name']}_scgpt_input.h5ad"


def export_scgpt_input(config: dict) -> Path:
    """Export raw counts + standard label columns for finetune_integration_adjusted.py.

    The external script expects columns named 'Donor', 'scumi_clean_coarse' and
    optionally 'scumi_clean_fine_grained'. We do not modify that script; we only
    rename/copy the configured columns in the exported AnnData.
    """
    import anndata as ad

    try:  # pragma: no cover - depends on anndata version
        ad.settings.allow_write_nullable_strings = True
    except AttributeError:
        pass

    dataset = config["active_dataset"]
    out_path = scgpt_export_path(config)
    out_dir = ensure_dir(out_path.parent)
    manifest_path = out_dir / "scgpt_export.json"
    fine_col = dataset["labels"].get("fine")
    manifest = {
        "h5ad_path": str(out_path),
        "batch_col": "Donor",
        "coarse_label_col": "scumi_clean_coarse",
        "fine_label_col": "scumi_clean_fine_grained" if fine_col else None,
        "donor_train": list(dataset["donors"]["train"]),
        "donor_test": list(dataset["donors"]["test"]),
        "feature_importance_dir": str(Path(config["cache_dir"]) / "features"),
        "coarse_command": (
            "SCGPT_LABEL_COL=scumi_clean_coarse python finetune_integration_adjusted.py"
        ),
        "fine_command": (
            "SCGPT_LABEL_COL=scumi_clean_fine_grained python finetune_integration_adjusted.py"
        ),
        "note": (
            "Run finetune_integration_adjusted.py on the GPU cluster with "
            f"h5ad_path='{out_path}', batch_col='Donor' and the desired "
            "SCGPT_LABEL_COL. The CPU pipeline only exports the input."
        ),
    }
    if out_path.is_file():
        atomic_write_json(manifest_path, manifest)
        logging.info("scGPT input already exists: %s", out_path)
        return out_path

    logging.info("Exporting scGPT input from raw data: %s", dataset["path"])
    adata = ad.read_h5ad(dataset["path"])
    counts_layer = dataset.get("counts_layer")
    if counts_layer:
        if counts_layer not in adata.layers:
            raise PipelineError(
                f"counts_layer='{counts_layer}' not found while exporting scGPT input."
            )
        adata.X = adata.layers[counts_layer].copy()

    batch_key = dataset["batch_key"]
    coarse_col = dataset["labels"]["coarse"]
    adata.obs["Donor"] = adata.obs[batch_key].astype(str)
    adata.obs["scumi_clean_coarse"] = adata.obs[coarse_col].astype(str)
    if fine_col:
        adata.obs["scumi_clean_fine_grained"] = adata.obs[fine_col].astype(str)

    tmp = out_path.with_suffix(".tmp.h5ad")
    adata.write_h5ad(tmp)
    tmp.replace(out_path)
    atomic_write_json(manifest_path, manifest)
    logging.info("scGPT input written to %s", out_path)
    return out_path
