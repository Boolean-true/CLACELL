"""Model registry and per-node fitting/tuning dispatch."""

from __future__ import annotations

import logging

import pandas as pd

from ..features import sorted_genes
from ..tasks import features_dir
from ..logging_utils import PipelineError
from .base import ConstantClassifier, ModelAdapter
from .custom_ensemble import build_custom_ensemble_adapter, tune_base_estimator
from .references import (
    CellTypistAdapter,
    ScGPTExternalAdapter,
    SingleRAdapter,
    tune_celltypist,
)


class ConfiguredModel(ModelAdapter):
    """Deferred adapter: the actual model is built on ``fit``."""

    def __init__(self, config: dict, model_name: str, node: str, node_params: dict, seed: int, n_jobs: int):
        self.config = config
        self.model_name = model_name
        self.node = node
        self.node_params = dict(node_params or {})
        self.seed = seed
        self.n_jobs = n_jobs
        self.inner: ModelAdapter | None = None
        self.epochs_ = None

    def fit(self, X: pd.DataFrame, y: pd.Series, meta: pd.DataFrame | None = None):
        self.inner = fit_model(
            config=self.config,
            model_name=self.model_name,
            node=self.node,
            node_params=self.node_params,
            seed=self.seed,
            n_jobs=self.n_jobs,
            X=X,
            y=y,
            meta=meta,
        )
        self.epochs_ = getattr(self.inner, "epochs_", None)
        return self

    def predict(self, X: pd.DataFrame, meta: pd.DataFrame | None = None):
        if self.inner is None:
            raise PipelineError(f"Model '{self.model_name}' node '{self.node}' is not fitted.")
        return self.inner.predict(X, meta)

    def predict_proba(self, X: pd.DataFrame, meta: pd.DataFrame | None = None):
        if self.inner is None:
            raise PipelineError(f"Model '{self.model_name}' node '{self.node}' is not fitted.")
        return self.inner.predict_proba(X, meta)

    @property
    def classes_(self):
        return getattr(self.inner, "classes_", None)


def model_config(config: dict, model_name: str) -> dict:
    try:
        return config["active_models"][model_name]
    except KeyError as exc:
        raise PipelineError(
            f"Model '{model_name}' is not active. Active: {sorted(config['active_models'])}"
        ) from exc


def internal_feature_importance(model_cfg: dict) -> str:
    """Ranking used *inside* the custom ensemble."""
    explicit = model_cfg.get("feature_importance")
    if explicit:
        return str(explicit).lower()
    base = str(model_cfg.get("base", "")).lower()
    if base in {"randomforest", "rf"}:
        return "linearsvc"
    if base in {"linearsvc", "linsvc"}:
        return "randomforest"
    dataset_cfg = model_cfg.get("_dataset_feature_importance", {})
    return str(dataset_cfg.get("robustness", "linearsvc")).lower()


def robustness_feature_importance(config: dict, model_name: str) -> str:
    dataset_cfg = config["active_dataset"]["feature_importance"]
    method = str(dataset_cfg.get("robustness", "linearsvc")).lower()
    if method == "model":
        return internal_feature_importance(model_config(config, model_name))
    return method


def _drop_rare_classes(
    X: pd.DataFrame,
    y: pd.Series,
    meta: pd.DataFrame | None,
    model_name: str,
    node: str,
) -> tuple[pd.DataFrame, pd.Series, pd.DataFrame | None]:
    """Drop classes with a single training cell for stacking CV feasibility."""
    counts = y.value_counts()
    rare = counts[counts < 2].index.tolist()
    if not rare:
        return X, y, meta
    logging.warning(
        "Model '%s' node '%s': dropping training classes with <2 cells for stacking CV: %s",
        model_name,
        node,
        {str(label): int(counts[label]) for label in rare},
    )
    keep = ~y.isin(rare)
    X = X.loc[keep]
    y = y.loc[keep]
    if meta is not None:
        meta = meta.loc[keep]
    return X, y, meta


def make_factory(
    config: dict,
    model_name: str,
    node: str,
    node_params: dict,
    seed: int,
    n_jobs: int,
):
    def factory() -> ModelAdapter:
        return ConfiguredModel(
            config=config,
            model_name=model_name,
            node=node,
            node_params=node_params,
            seed=seed,
            n_jobs=n_jobs,
        )

    return factory


def fit_model(
    config: dict,
    model_name: str,
    node: str,
    node_params: dict,
    seed: int,
    n_jobs: int,
    X: pd.DataFrame,
    y: pd.Series,
    meta: pd.DataFrame | None,
) -> ModelAdapter:
    model_cfg = model_config(config, model_name)
    family = str(model_cfg.get("family", "")).lower()
    dataset = config["active_dataset"]
    batch_key = dataset["batch_key"]

    if family == "autoencoder":
        from .autoencoder import build_autoencoder

        if len(X) < 2:
            raise PipelineError(
                f"Autoencoder model '{model_name}' node '{node}' has only {len(X)} cells; "
                "BatchNorm requires at least 2 training cells."
            )
        head = str(model_cfg.get("head", "linsvc")).lower()
        return build_autoencoder(
            X=X,
            y=y,
            params=dict(model_cfg.get("params", {})),
            head=head,
            head_params=node_params,
            seed=seed,
            n_jobs=n_jobs,
        )

    if family == "conditional_autoencoder":
        from .conditional_autoencoder import build_conditional_autoencoder

        if len(X) < 2:
            raise PipelineError(
                f"Conditional autoencoder model '{model_name}' node '{node}' has only "
                f"{len(X)} cells; BatchNorm requires at least 2 training cells."
            )
        head = str(model_cfg.get("head", "linsvc")).lower()
        return build_conditional_autoencoder(
            X=X,
            y=y,
            meta=meta,
            batch_key=batch_key,
            params=dict(model_cfg.get("params", {})),
            head=head,
            head_params=node_params,
            seed=seed,
            n_jobs=n_jobs,
        )

    if family == "custom_ensemble":
        original_y = y.copy()
        X, y, meta = _drop_rare_classes(X, y, meta, model_name, node)
        if len(y) == 0:
            label = str(original_y.value_counts().idxmax())
            logging.warning(
                "Model '%s' node '%s': no class has >=2 cells; using a constant "
                "classifier predicting '%s'.",
                model_name,
                node,
                label,
            )
            return ConstantClassifier(label)
        if y.nunique() < 2:
            label = str(y.value_counts().idxmax())
            logging.warning(
                "Model '%s' node '%s': only one class with >=2 cells remains; "
                "using a constant fine classifier predicting '%s'.",
                model_name,
                node,
                label,
            )
            return ConstantClassifier(label)
        ranking = internal_feature_importance(model_cfg)
        genes = sorted_genes(features_dir(config, seed), ranking)
        params_cfg = dict(model_cfg.get("params", {}))
        min_class = int(y.value_counts().min())
        params_cfg["stacking_cv"] = max(2, min(int(params_cfg.get("stacking_cv", 5)), min_class))
        params_cfg["calibration_cv"] = max(2, min(5, min_class))
        adapter = build_custom_ensemble_adapter(
            sorted_top_genes=genes,
            base=str(model_cfg.get("base", "randomforest")).lower(),
            tuned_params=dict(node_params or {}),
            params_cfg=params_cfg,
            seed=seed,
            n_jobs=n_jobs,
        )
        adapter.fit(X, y, meta)
        return adapter

    if family == "reference":
        adapter_name = str(model_cfg.get("adapter", "")).lower()
        if adapter_name == "singler":
            adapter = SingleRAdapter(model_cfg.get("params", {}))
        elif adapter_name == "celltypist":
            adapter = CellTypistAdapter(
                node_params, genes=X.columns.astype(str).tolist()
            )
        elif adapter_name in {"scgpt", "scgpt_external"}:
            adapter = ScGPTExternalAdapter(model_cfg.get("params", {}))
        else:
            raise PipelineError(
                f"Unknown reference adapter '{adapter_name}' for model '{model_name}'. "
                "Valid: singler, celltypist, scgpt_external."
            )
        adapter.fit(X, y, meta)
        return adapter

    raise PipelineError(
        f"Unknown model family '{family}' for model '{model_name}'. "
        "Valid: autoencoder, conditional_autoencoder, custom_ensemble, reference."
    )


def tune_model_node(
    config: dict,
    model_name: str,
    node: str,
    X: pd.DataFrame,
    y: pd.Series,
    meta: pd.DataFrame | None,
    seed: int,
    n_jobs: int,
) -> tuple[dict, dict]:
    model_cfg = model_config(config, model_name)
    family = str(model_cfg.get("family", "")).lower()
    tune_cfg = model_cfg.get("tune") or {}

    if family in {"autoencoder", "conditional_autoencoder"}:
        from .autoencoder import tune_autoencoder
        from .conditional_autoencoder import tune_conditional_autoencoder

        if len(X) < 2: #TODO: Das kann ich mir doch sparen, oder? Meine Datensätze haben immer mehr als 2 Zellen
            return {}, {
                "skipped": True,
                "skip_reason": f"only {len(X)} training cell(s); BatchNorm needs at least 2.",
                "cv": 0,
                "n_iter": 0,
                "best_score": float("nan"),
                "avg_time_per_iteration_sec": float("nan"),
            }
        head = str(model_cfg.get("head", "linsvc")).lower()
        params = dict(model_cfg.get("params", {}))
        if family == "autoencoder":
            return tune_autoencoder(X, y, params, head, tune_cfg, seed, n_jobs)
        dataset = config["active_dataset"]
        return tune_conditional_autoencoder(
            X,
            y,
            meta,
            dataset["batch_key"],
            params,
            head,
            tune_cfg,
            seed,
            n_jobs,
        )

    if family == "custom_ensemble":
        best_params, meta_info = tune_base_estimator(
            X=X,
            y=y,
            base=str(model_cfg.get("base", "randomforest")).lower(),
            tune_cfg=tune_cfg,
            seed=seed,
            n_jobs=n_jobs,
        )
        return best_params, meta_info

    if family == "reference":
        adapter_name = str(model_cfg.get("adapter", "")).lower()
        if adapter_name == "celltypist":
            return tune_celltypist(X, y, tune_cfg, seed, n_jobs)
        return {}, {
            "skipped": True,
            "skip_reason": "This reference model has no tunable hyperparameters.",
            "cv": 0,
            "n_iter": 0,
            "best_score": float("nan"),
            "avg_time_per_iteration_sec": float("nan"),
            "tuning_time_min": 0.0,
        }

    raise PipelineError(f"Cannot tune unknown model family '{family}' for '{model_name}'.")
