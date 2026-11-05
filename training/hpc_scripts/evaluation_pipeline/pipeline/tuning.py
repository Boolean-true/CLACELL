"""Tuning stage: one fixed hyperparameter set per dataset/model/hierarchy node."""

from __future__ import annotations

import logging
import resource
import time

import pandas as pd

from .config import cpu_count, load_config, model_uses_scaled_features
from .features import load_scaler
from .io import atomic_write_json, clear_success, ensure_dir
from .logging_utils import log_header
from .models.registry import tune_model_node
from .tasks import (
    current_cache_key,
    get_task,
    load_cache,
    node_data,
    scaler_path,
    tuning_dir,
    tuning_key,
    tuning_success,
)


def _peak_ram_gb() -> float:
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024)


def run_tune(config_path: str, task_id: int) -> None:
    config = load_config(config_path)
    task = get_task(config, "tune", task_id)
    if task is None:
        logging.info("Tune task %s is outside the manifest; nothing to do.", task_id)
        return
    dataset = config["active_dataset"]
    model_name = str(task["model"])
    node = str(task["node"])
    seed_value = task.get("seed")
    seed = None if pd.isna(seed_value) or int(seed_value) < 0 else int(seed_value)
    out_dir = tuning_dir(config, model_name, node, seed)
    log_header(
        "tune",
        dataset=dataset["name"],
        model=model_name,
        node=node,
        seed=seed,
        task_id=task_id,
    )
    if tuning_success(config, model_name, node, seed):
        logging.info("Tuning cache hit: %s", out_dir)
        return
    start = time.time()
    clear_success(out_dir)
    ensure_dir(out_dir)

    cache = load_cache(config)
    X, y, meta = node_data(config, cache, node)
    model_cfg = config["active_models"][model_name]
    tune_cfg = model_cfg.get("tune") or {}
    search_seed = seed if seed is not None else int(config["experiment"]["tuning_seed"])
    n_jobs = cpu_count(config, "tune")

    if model_uses_scaled_features(model_cfg):
        scaler = load_scaler(scaler_path(config), current_cache_key(config))
        X = scaler.transform(X)

    logging.info(
        "Tuning model=%s node=%s seed=%s: %d cells, %d classes, min class=%d",
        model_name,
        node,
        seed,
        len(X),
        y.nunique(),
        int(y.value_counts().min()),
    )
    best_params, meta_info = tune_model_node(
        config=config,
        model_name=model_name,
        node=node,
        X=X,
        y=y,
        meta=meta,
        seed=search_seed,
        n_jobs=n_jobs,
    )
    elapsed = (time.time() - start) / 60.0
    meta_info = dict(meta_info or {})
    # The head search may report search_time_min; report the full task wall time
    # (including representation training) as tuning_time_min.
    meta_info.setdefault("search_time_min", None)
    meta_info["tuning_time_min"] = elapsed
    meta_info["tuning_wall_time_min"] = round(elapsed, 4)
    meta_info["peak_ram_gb"] = round(_peak_ram_gb(), 3)
    meta_info["dataset"] = dataset["name"]
    meta_info["model"] = model_name
    meta_info["node"] = node
    meta_info["seed"] = seed
    meta_info["search_seed"] = search_seed
    meta_info["cache_key"] = current_cache_key(config)
    meta_info["tuning_key"] = tuning_key(config, model_name, node, seed)
    meta_info["n_train_cells"] = int(len(X))
    meta_info["n_classes"] = int(y.nunique())
    meta_info["min_train_class_count"] = int(y.value_counts().min())
    meta_info["class_counts"] = {str(k): int(v) for k, v in y.value_counts().items()}

    atomic_write_json(out_dir / "best_params.json", best_params)
    atomic_write_json(out_dir / "tuning_meta.json", meta_info)
    atomic_write_json(
        out_dir / "_SUCCESS.json",
        {
            "model": model_name,
            "node": node,
            "dataset": dataset["name"],
            "cache_key": current_cache_key(config),
            "tuning_key": tuning_key(config, model_name, node, seed),
            "best_params": best_params,
            "tuning_time_min": round(elapsed, 4),
        },
    )
    (out_dir / "_SUCCESS").write_text("ok\n", encoding="utf-8")
    logging.info(
        "Tuning finished model=%s node=%s in %.2f min; best=%s",
        model_name,
        node,
        elapsed,
        best_params,
    )
