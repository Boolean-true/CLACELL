"""Task manifests, cache loading and status helpers."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from . import __version__ as PIPELINE_VERSION
from .config import needs_scaled_feature_importance
from .io import atomic_write_json, cache_key, ensure_dir, is_success, read_json
from .logging_utils import PipelineError


def node_slug(node: str) -> str:
    return str(node).replace(":", "__").replace("/", "_")


def manifests_dir(config: dict) -> Path:
    return Path(config["output_dir"]) / "manifests"


def tuning_dir(config: dict, model: str, node: str, seed: int | None = None) -> Path:
    base = Path(config["output_dir"]) / "tuning" / model / node_slug(node)
    if seed is not None and config["experiment"].get("tuning_per_seed"):
        base = base / f"seed_{int(seed)}"
    return base


def results_dir(config: dict, model: str, level: str) -> Path:
    return Path(config["output_dir"]) / "results" / model / level


def features_dir(config: dict, seed: int) -> Path:
    return Path(config["cache_dir"]) / "features" / f"seed_{int(seed)}"


def scaler_path(config: dict) -> Path:
    """Dataset-wide scaler shared by all seeds and tuning runs."""
    return Path(config["cache_dir"]) / "scaler.pkl"


def cache_ready(config: dict) -> bool:
    cache_dir = Path(config["cache_dir"])
    required = [
        cache_dir / "_SUCCESS",
        cache_dir / "prepare_meta.json",
        cache_dir / "hierarchy.json",
        cache_dir / "X_train.npy",
        cache_dir / "X_test.npy",
        cache_dir / "obs_train.pkl",
        cache_dir / "obs_test.pkl",
        cache_dir / "genes.json",
    ]
    return all(path.exists() for path in required)


def require_cache(config: dict) -> None:
    if not cache_ready(config):
        raise PipelineError(
            f"Preprocessing cache is missing or incomplete for dataset "
            f"'{config['active_dataset']['name']}' at {config['cache_dir']}. "
            "Run the prepare stage first."
        )


def load_cache(config: dict) -> dict:
    require_cache(config)
    cache_dir = Path(config["cache_dir"])
    with (cache_dir / "genes.json").open("r", encoding="utf-8") as handle:
        genes = json.load(handle)
    X_train = np.load(cache_dir / "X_train.npy")
    X_test = np.load(cache_dir / "X_test.npy")
    obs_train = pd.read_pickle(cache_dir / "obs_train.pkl")
    obs_test = pd.read_pickle(cache_dir / "obs_test.pkl")
    hierarchy = read_json(cache_dir / "hierarchy.json")
    meta = read_json(cache_dir / "prepare_meta.json", default={})
    if len(obs_train) != X_train.shape[0]:
        raise PipelineError(
            f"Cache mismatch: X_train has {X_train.shape[0]} rows, obs_train has {len(obs_train)}. "
            "Re-run prepare."
        )
    if len(obs_test) != X_test.shape[0]:
        raise PipelineError(
            f"Cache mismatch: X_test has {X_test.shape[0]} rows, obs_test has {len(obs_test)}. "
            "Re-run prepare."
        )
    return {
        "X_train": pd.DataFrame(X_train, index=obs_train.index.astype(str), columns=genes),
        "X_test": pd.DataFrame(X_test, index=obs_test.index.astype(str), columns=genes),
        "obs_train": obs_train,
        "obs_test": obs_test,
        "genes": genes,
        "hierarchy": hierarchy,
        "prepare_meta": meta,
    }


def node_data(config: dict, cache: dict, node: str) -> tuple[pd.DataFrame, pd.Series, pd.DataFrame]:
    dataset = config["active_dataset"]
    coarse_col = dataset["labels"]["coarse"]
    fine_col = dataset["labels"].get("fine")
    obs = cache["obs_train"]
    X = cache["X_train"]
    if node == "coarse":
        return X, obs[coarse_col].astype(str), obs
    if node == "fine":
        if not fine_col:
            raise PipelineError(
                f"Node 'fine' requested but dataset '{dataset['name']}' has no fine label column."
            )
        return X, obs[fine_col].astype(str), obs
    if node.startswith("fine:"):
        if not fine_col:
            raise PipelineError(
                f"Node '{node}' requested but dataset '{dataset['name']}' has no fine label column."
            )
        coarse_label = node.split(":", 1)[1]
        mask = obs[coarse_col].astype(str) == coarse_label
        if not mask.any():
            raise PipelineError(
                f"Node '{node}' has no training cells for coarse label '{coarse_label}'. "
                f"Known labels: {sorted(obs[coarse_col].astype(str).unique())}"
            )
        return X.loc[mask], obs.loc[mask, fine_col].astype(str), obs.loc[mask]
    raise PipelineError(
        f"Unknown node '{node}'. Expected 'coarse', 'fine' or 'fine:<coarse_label>'."
    )


def hierarchy_nodes(config: dict, hierarchy: dict) -> list[str]:
    nodes = ["coarse"]
    for node_name in hierarchy.get("nodes", {}):
        if node_name.startswith("fine:"):
            nodes.append(node_name)
    return nodes


def generate_manifests(config: dict) -> dict:
    require_cache(config)
    cache_dir = Path(config["cache_dir"])
    hierarchy = read_json(cache_dir / "hierarchy.json")
    dataset = config["active_dataset"]
    has_fine = bool(dataset["labels"].get("fine"))

    features_rows = [
        {"task_id": index, "dataset": dataset["name"], "seed": int(seed)}
        for index, seed in enumerate(config["experiment"]["seeds"])
    ]
    tune_rows = []
    run_rows = []
    tune_id = 0
    run_id = 0
    for model_name in config["experiment"]["models"]:
        model_cfg = config["active_models"][model_name]
        if model_cfg.get("tune"):
            nodes = (
                hierarchy_nodes(config, hierarchy)
                if bool(model_cfg.get("hierarchy"))
                else ["coarse"] + (["fine"] if has_fine else [])
            )
            if config["experiment"].get("tuning_per_seed"):
                for seed_index, seed in enumerate(config["experiment"]["seeds"]):
                    for node in nodes:
                        tune_rows.append(
                            {
                                "task_id": tune_id,
                                "dataset": dataset["name"],
                                "model": model_name,
                                "node": node,
                                "seed_index": seed_index,
                                "seed": int(seed),
                            }
                        )
                        tune_id += 1
            else:
                for node in nodes:
                    tune_rows.append(
                        {
                            "task_id": tune_id,
                            "dataset": dataset["name"],
                            "model": model_name,
                            "node": node,
                            "seed_index": -1,
                            "seed": -1,
                        }
                    )
                    tune_id += 1
        for seed_index, seed in enumerate(config["experiment"]["seeds"]):
            run_rows.append(
                {
                    "task_id": run_id,
                    "dataset": dataset["name"],
                    "model": model_name,
                    "seed_index": seed_index,
                    "seed": int(seed),
                    "nodes": "coarse+fine" if model_cfg.get("hierarchy") else "coarse,fine",
                }
            )
            run_id += 1

    features_frame = pd.DataFrame(features_rows)
    tune_frame = pd.DataFrame(tune_rows)
    run_frame = pd.DataFrame(run_rows)
    out_dir = ensure_dir(manifests_dir(config))
    features_path = out_dir / "features.tsv"
    tune_path = out_dir / "tune.tsv"
    run_path = out_dir / "run.tsv"
    features_frame.to_csv(features_path, sep="\t", index=False)
    if len(tune_frame):
        tune_frame.to_csv(tune_path, sep="\t", index=False)
    else:
        pd.DataFrame(columns=["task_id", "dataset", "model", "node"]).to_csv(
            tune_path, sep="\t", index=False
        )
    run_frame.to_csv(run_path, sep="\t", index=False)

    plan = {
        "dataset": dataset["name"],
        "models": list(config["experiment"]["models"]),
        "seeds": list(config["experiment"]["seeds"]),
        "features_tasks": int(len(features_frame)),
        "tune_tasks": int(len(tune_frame)),
        "run_tasks": int(len(run_frame)),
        "hierarchy_nodes": hierarchy_nodes(config, hierarchy),
        "features_manifest": str(features_path),
        "tune_manifest": str(tune_path),
        "run_manifest": str(run_path),
    }
    atomic_write_json(out_dir / "plan.json", plan)
    return plan


def read_manifest(config: dict, stage: str) -> pd.DataFrame:
    path = manifests_dir(config) / f"{stage}.tsv"
    if not path.is_file():
        raise PipelineError(
            f"Manifest {path} not found. Run 'python orchestrate.py --stage plan' first."
        )
    return pd.read_csv(path, sep="\t")


def get_task(config: dict, stage: str, task_id: int) -> dict | None:
    frame = read_manifest(config, stage)
    if task_id < 0 or task_id >= len(frame):
        return None
    return frame.iloc[task_id].to_dict()


def current_cache_key(config: dict) -> str | None:
    meta = read_json(Path(config["cache_dir"]) / "prepare_meta.json", default={})
    return meta.get("cache_key")


def features_key(config: dict, seed: int) -> str | None:
    cache = current_cache_key(config)
    if cache is None:
        return None
    dataset = config["active_dataset"]
    payload = {
        "pipeline_version": PIPELINE_VERSION,
        "cache_key": cache,
        "seed": int(seed),
        "feature_importance": dataset["feature_importance"],
    }
    if needs_scaled_feature_importance(config):
        payload["scaled_feature_importance"] = True
    return cache_key(payload)


def features_success(config: dict, seed: int) -> bool:
    expected = features_key(config, seed)
    if expected is None:
        return False
    directory = features_dir(config, seed)
    if not is_success(directory):
        return False
    success = read_json(directory / "_SUCCESS.json", default={})
    if success.get("features_key") != expected:
        return False
    methods = success.get("methods", [])
    meta_path = directory / "features_meta.json"
    if not methods or not meta_path.is_file():
        return False
    meta = read_json(meta_path, default={})
    if any(
        meta.get(key) is None
        for key in ("feature_selection_time_min", "total_wall_time_min")
    ):
        return False
    if not all(
        (directory / f"feature_importance_{method}.pkl").is_file()
        for method in methods
    ):
        return False
    if needs_scaled_feature_importance(config) and not scaler_path(config).is_file():
        return False
    return True


def tuning_key(config: dict, model: str, node: str, seed: int | None = None) -> str | None:
    cache = current_cache_key(config)
    if cache is None:
        return None
    payload = {
        "pipeline_version": PIPELINE_VERSION,
        "cache_key": cache,
        "model": config["active_models"][model],
        "node": node,
        "seed": int(seed) if seed is not None else None,
        "tuning_seed": int(config["experiment"]["tuning_seed"]),
    }
    return cache_key(payload)


def tuning_success(config: dict, model: str, node: str, seed: int | None = None) -> bool:
    expected = tuning_key(config, model, node, seed)
    if expected is None:
        return False
    directory = tuning_dir(config, model, node, seed)
    if not is_success(directory):
        return False
    success = read_json(directory / "_SUCCESS.json", default={})
    if success.get("tuning_key") != expected:
        return False
    meta = read_json(directory / "tuning_meta.json", default={})
    return meta.get("tuning_time_min") is not None


def levels_for_model(config: dict, model: str) -> list[str]:
    model_cfg = config["active_models"][model]
    if bool(model_cfg.get("hierarchy")):
        return ["coarse", "fine"]
    levels = list(config["experiment"].get("reference_levels", ["coarse", "fine"]))
    if not config["active_dataset"]["labels"].get("fine"):
        levels = [level for level in levels if level != "fine"]
    return levels


def run_key(config: dict, model: str, seed_index: int) -> str | None:
    cache = current_cache_key(config)
    if cache is None:
        return None
    model_cfg = config["active_models"][model]
    hierarchy_path = Path(config["cache_dir"]) / "hierarchy.json"
    hierarchy = read_json(hierarchy_path, default={})
    if bool(model_cfg.get("hierarchy")):
        nodes = ["coarse"] + [
            node for node in hierarchy.get("nodes", {}) if node.startswith("fine:")
        ]
    else:
        nodes = levels_for_model(config, model)
    seed = int(config["experiment"]["seeds"][seed_index])
    tuning_params = {
        node: read_json(
            tuning_dir(config, model, node, seed) / "best_params.json", default=None
        )
        for node in nodes
    }
    payload = {
        "pipeline_version": PIPELINE_VERSION,
        "cache_key": cache,
        "features_key": features_key(config, seed),
        "model": model_cfg,
        "seed_index": int(seed_index),
        "seed": seed,
        "eval_seed": int(config["experiment"]["eval_seed_base"]) + int(seed_index),
        "tuning_params": tuning_params,
    }
    return cache_key(payload)


def run_success(config: dict, model: str, seed_index: int) -> bool:
    expected = run_key(config, model, seed_index)
    if expected is None:
        return False
    for level in levels_for_model(config, model):
        directory = results_dir(config, model, level)
        if not (directory / f"_SUCCESS_run_{seed_index}").is_file():
            return False
        meta = read_json(directory / f"run_{seed_index}.json", default={})
        if meta.get("run_key") != expected:
            return False
    return True


def status(config: dict) -> dict:
    features_path = manifests_dir(config) / "features.tsv"
    tune_path = manifests_dir(config) / "tune.tsv"
    run_path = manifests_dir(config) / "run.tsv"
    features = pd.read_csv(features_path, sep="\t") if features_path.is_file() else pd.DataFrame()
    tune = pd.read_csv(tune_path, sep="\t") if tune_path.is_file() else pd.DataFrame()
    run = pd.read_csv(run_path, sep="\t") if run_path.is_file() else pd.DataFrame()
    features_done, features_missing = 0, []
    for _, row in features.iterrows():
        if features_success(config, int(row["seed"])):
            features_done += 1
        else:
            features_missing.append(int(row["task_id"]))
    tune_done, tune_missing = 0, []
    for _, row in tune.iterrows():
        seed_value = row.get("seed")
        seed = None if pd.isna(seed_value) or int(seed_value) < 0 else int(seed_value)
        if tuning_success(config, row["model"], row["node"], seed):
            tune_done += 1
        else:
            tune_missing.append(int(row["task_id"]))
    run_done, run_missing = 0, []
    for _, row in run.iterrows():
        if run_success(config, row["model"], int(row["seed_index"])):
            run_done += 1
        else:
            run_missing.append(int(row["task_id"]))
    return {
        "features_total": int(len(features)),
        "features_done": features_done,
        "features_missing": features_missing,
        "tune_total": int(len(tune)),
        "tune_done": tune_done,
        "tune_missing": tune_missing,
        "run_total": int(len(run)),
        "run_done": run_done,
        "run_missing": run_missing,
    }
