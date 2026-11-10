"""Configuration loading and validation."""

from __future__ import annotations

import copy
import os
from pathlib import Path
from typing import Any
import yaml


class ConfigError(RuntimeError):
    """Raised when the experiment configuration is invalid or incomplete."""


DEFAULT_RESOURCES = {
    "prepare": {"cpus": 32, "mem_gb": 200, "time": "24:00:00"},
    "features": {"cpus": 16, "mem_gb": 64, "time": "12:00:00"},
    "tune": {"cpus": 16, "mem_gb": 64, "time": "12:00:00"},
    "run": {"cpus": 16, "mem_gb": 64, "time": "12:00:00"},
    "aggregate": {"cpus": 4, "mem_gb": 16, "time": "01:00:00"},
}

DEFAULT_PREPROCESS = {
    "min_counts": 10,
    "min_cells": 3,
    "remove_mt_ribo_hb": True,
    "scrublet": True,
    "target_sum": 10000,
    "hvg": True,
    "hvg_n_top_genes": None,
}

DEFAULT_HIERARCHY = {
    "min_fine_classes": 2,
}

DEFAULT_FEATURE_IMPORTANCE = {
    "compute": ["randomforest", "linearsvc"],
    "label_level": "fine",
    # Ranking used by test_robustness. "differential_expression" is computed by
    # prepare from the training expression matrix (no external marker file).
    "robustness": "differential_expression",
}


def _deep_merge(base: dict, override: dict) -> dict:
    result = copy.deepcopy(base)
    for key, value in (override or {}).items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = _deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def load_config(path: str | os.PathLike) -> dict[str, Any]:
    path = Path(path).expanduser().resolve()
    if not path.is_file():
        raise ConfigError(f"Config file not found: {path}")
    with path.open("r", encoding="utf-8") as handle:
        try:
            config = yaml.safe_load(handle)
        except yaml.YAMLError as exc:
            raise ConfigError(f"Could not parse YAML config {path}: {exc}") from exc
    if not isinstance(config, dict):
        raise ConfigError(f"Config {path} must contain a mapping at the top level.")
    return resolve_config(config, source=path)


def resolve_config(config: dict[str, Any], source: Path | None = None) -> dict[str, Any]:
    """Validate the active experiment and fill defaults."""
    exp = config.get("experiment")
    if not isinstance(exp, dict):
        raise ConfigError("Missing 'experiment' section in config.")

    datasets = config.get("datasets")
    models = config.get("models")
    if not isinstance(datasets, dict) or not datasets:
        raise ConfigError("Missing or empty 'datasets' section in config.")
    if not isinstance(models, dict) or not models:
        raise ConfigError("Missing or empty 'models' section in config.")

    dataset_name = exp.get("dataset")
    if not dataset_name:
        raise ConfigError("experiment.dataset is not set.")
    if dataset_name not in datasets:
        raise ConfigError(
            f"Unknown dataset '{dataset_name}'. Available: {', '.join(sorted(datasets))}"
        )

    model_names = exp.get("models") or []
    if isinstance(model_names, str):
        model_names = [model_names]
    if not model_names:
        raise ConfigError("experiment.models is empty.")
    unknown = [name for name in model_names if name not in models]
    if unknown:
        raise ConfigError(
            f"Unknown model(s) {unknown}. Available: {', '.join(sorted(models))}"
        )

    seeds = exp.get("seeds")
    if seeds is None:
        n_runs = int(exp.get("runs", 1))
        base_seed = int(exp.get("seed", 0))
        seeds = list(range(base_seed, base_seed + n_runs))
    if not isinstance(seeds, list) or not seeds:
        raise ConfigError("experiment.seeds must be a non-empty list of integers.")
    seeds = [int(seed) for seed in seeds]

    for key in ("name", "tuning_seed", "eval_seed_base", "max_parallel", "reference_levels"):
        if exp.get(key) is None:
            raise ConfigError(f"experiment.{key} is not set.")
    exp.setdefault("tuning_per_seed", False)
    invalid_levels = [level for level in exp["reference_levels"] if level not in {"coarse", "fine"}]
    if invalid_levels:
        raise ConfigError(
            f"experiment.reference_levels contains invalid values {invalid_levels}. "
            "Valid: coarse, fine."
        )
    exp["models"] = model_names
    exp["seeds"] = seeds

    hierarchy = _deep_merge(DEFAULT_HIERARCHY, exp.get("hierarchy", {}))
    exp["hierarchy"] = hierarchy

    resources = {}
    for stage, defaults in DEFAULT_RESOURCES.items():
        resources[stage] = _deep_merge(defaults, (exp.get("resources") or {}).get(stage, {}))
    exp["resources"] = resources

    for stage in ("cache_root", "output_root"):
        if not exp.get(stage):
            raise ConfigError(f"experiment.{stage} is not set.")
        exp[stage] = str(Path(exp[stage]).expanduser())

    # Normalise the active dataset.
    dataset = copy.deepcopy(datasets[dataset_name])
    dataset["name"] = dataset_name
    if not dataset.get("path"):
        raise ConfigError(f"datasets.{dataset_name}.path is not set.")
    dataset["path"] = str(Path(dataset["path"]).expanduser())
    if not dataset.get("batch_key"):
        raise ConfigError(f"datasets.{dataset_name}.batch_key is not set.")
    labels = dataset.get("labels") or {}
    if not labels.get("coarse"):
        raise ConfigError(f"datasets.{dataset_name}.labels.coarse is not set.")
    dataset["labels"] = {
        "coarse": labels.get("coarse"),
        "fine": labels.get("fine"),
    }
    dataset["exclude"] = _deep_merge(
        {"coarse": [], "fine": []}, dataset.get("exclude", {})
    )
    dataset["preprocess"] = _deep_merge(
        DEFAULT_PREPROCESS, dataset.get("preprocess", {})
    )
    dataset["feature_importance"] = _deep_merge(
        DEFAULT_FEATURE_IMPORTANCE, dataset.get("feature_importance", {})
    )
    donors = dataset.get("donors") or {}
    dataset["donors"] = {
        "train": [str(value) for value in (donors.get("train") or [])],
        "test": [str(value) for value in (donors.get("test") or [])],
    }
    if dataset["preprocess"].get("hvg") and not dataset["labels"].get("fine"):
        # Coarse-only datasets can still run a flat baseline, but the
        # hierarchical models need fine labels.
        pass
    config["active_dataset"] = dataset

    model_configs = {}
    for name in model_names:
        model = copy.deepcopy(models[name])
        model["name"] = name
        model.setdefault("params", {})
        if model.get("params") is None:
            model["params"] = {}
        model.setdefault("hierarchy", False)
        model.setdefault("tune", None)
        model.setdefault("family", None)
        if not model["family"]:
            raise ConfigError(f"models.{name}.family is not set.")
        if model["hierarchy"] and not dataset["labels"].get("fine"):
            raise ConfigError(
                f"Model '{name}' is hierarchical, but dataset '{dataset_name}' has no fine label column. "
                "Set datasets.<name>.labels.fine or set models.<name>.hierarchy: false."
            )
        model_configs[name] = model
    config["active_models"] = model_configs

    config["source"] = str(source) if source else None
    config["cache_dir"] = str(
        Path(exp["cache_root"]) / dataset_name
    )
    config["output_dir"] = str(
        Path(exp["output_root"]) / exp["name"] / dataset_name
    )
    return config


def active_model_names(config: dict) -> list[str]:
    return list(config["experiment"]["models"])


def model_config(config: dict, name: str) -> dict:
    try:
        return config["active_models"][name]
    except KeyError as exc:
        raise ConfigError(
            f"Model '{name}' is not active. Active models: {', '.join(active_model_names(config))}"
        ) from exc


def model_uses_scaled_features(model: dict) -> bool:
    """Whether this model is trained on the globally scaled feature matrix."""
    return (
        str(model.get("family", "")).lower() == "custom_ensemble"
        and bool((model.get("params") or {}).get("scale", False))
    )


def needs_scaled_feature_importance(config: dict) -> bool:
    """Whether any active custom ensemble is trained on scaled features."""
    return any(
        model_uses_scaled_features(model)
        for model in config.get("active_models", {}).values()
    )


def cpu_count(config: dict, stage: str) -> int:
    env_key = f"SLURM_CPUS_PER_TASK"
    if os.environ.get(env_key):
        try:
            return max(1, int(os.environ[env_key]))
        except ValueError:
            pass
    return max(1, int(config["experiment"]["resources"][stage].get("cpus", 1)))
