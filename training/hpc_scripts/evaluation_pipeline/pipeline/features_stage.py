"""Persistent per-seed feature rankings.

Each feature task handles one seed and writes both rankings permanently under
``<cache_root>/<dataset>/features/seed_<seed>/``. Per-method success markers make
the computation resumable: if a job is interrupted after the RandomForest
ranking, a later job reuses it and only computes the missing LinearSVC ranking.
All models with the same seed read the exact same two files.
"""

from __future__ import annotations

import logging
import resource
import time
from pathlib import Path

from .config import cpu_count, load_config
from .features import (
    feature_importance_linearsvc,
    feature_importance_randomforest,
)
from .io import (
    atomic_write_csv,
    atomic_write_json,
    atomic_write_pickle,
    atomic_write_text,
    clear_success,
    ensure_dir,
    mark_success,
    read_json,
)
from .logging_utils import PipelineError, log_header
from .tasks import features_dir, features_key, features_success, get_task, load_cache


def _peak_ram_gb() -> float:
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024)


def _safe_float(value, default: float = 0.0) -> float:
    try:
        if value is None:
            return default
        value = float(value)
        if value != value:  # NaN
            return default
        return value
    except (TypeError, ValueError):
        return default


def _canonical_method(method: str) -> str:
    method = str(method).lower()
    if method in {"randomforest", "rf"}:
        return "randomforest"
    if method in {"linearsvc", "linsvc"}:
        return "linearsvc"
    raise PipelineError(
        f"Unknown feature-importance method '{method}'. Valid: randomforest, linearsvc."
    )


def _method_done(directory: Path, method: str, expected_key: str | None) -> tuple[bool, float]:
    marker = directory / f"_SUCCESS_{method}"
    meta_path = directory / f"method_{method}.json"
    pkl_path = directory / f"feature_importance_{method}.pkl"
    if not (marker.is_file() and meta_path.is_file() and pkl_path.is_file()):
        return False, 0.0
    meta = read_json(meta_path, default={})
    if expected_key is not None and meta.get("features_key") != expected_key:
        return False, 0.0
    return True, _safe_float(meta.get("time_min"), 0.0)


def run_features(config_path: str, task_id: int) -> None:
    config = load_config(config_path)
    task = get_task(config, "features", task_id)
    if task is None:
        logging.info("Features task %s is outside the manifest; nothing to do.", task_id)
        return
    dataset = config["active_dataset"]
    seed = int(task["seed"])
    out_dir = ensure_dir(features_dir(config, seed))
    log_header("features", dataset=dataset["name"], seed=seed, task_id=task_id)
    if features_success(config, seed):
        logging.info("Features cache hit for seed=%s at %s", seed, out_dir)
        return

    expected_key = features_key(config, seed)
    old_success = read_json(out_dir / "_SUCCESS.json", default={})
    if old_success and old_success.get("features_key") != expected_key:
        clear_success(out_dir)

    # A resumed task reuses methods from earlier invocations. Keep their wall
    # time so total_wall_time_min stays cumulative instead of shrinking to the
    # duration of the cache-hit restart.
    old_meta = read_json(out_dir / "features_meta.json", default={})
    previous_wall_min = 0.0
    if old_meta.get("features_key") == expected_key:
        previous_wall_min = max(
            0.0, _safe_float(old_meta.get("total_wall_time_min"), 0.0)
        )

    start = time.time()
    cache = load_cache(config)
    fi_cfg = dataset["feature_importance"]
    label_level = fi_cfg.get("label_level", "fine")
    coarse_col = dataset["labels"]["coarse"]
    fine_col = dataset["labels"].get("fine")
    if label_level == "fine" and not fine_col:
        logging.warning("feature_importance.label_level='fine' but no fine labels; using coarse.")
        label_level = "coarse"
    y = cache["obs_train"][coarse_col if label_level == "coarse" else fine_col].astype(str)

    methods = list(dict.fromkeys(
        _canonical_method(method) for method in fi_cfg.get("compute", [])
    ))
    if not methods:
        raise PipelineError(
            f"datasets.{dataset['name']}.feature_importance.compute is empty."
        )
    n_jobs = cpu_count(config, "features")
    times: dict[str, float] = {}

    for method in methods:
        done, stored_time = _method_done(out_dir, method, expected_key)
        if done:
            times[method] = stored_time
            logging.info("Reusing existing %s ranking for seed=%s", method, seed)
            continue
        logging.info("Computing %s ranking for seed=%s", method, seed)
        method_start = time.time()
        if method == "randomforest":
            frame, _ = feature_importance_randomforest(cache["X_train"], y, seed, n_jobs)
        else:
            frame, _ = feature_importance_linearsvc(cache["X_train"], y, seed)
        elapsed = (time.time() - method_start) / 60.0
        times[method] = elapsed
        atomic_write_pickle(out_dir / f"feature_importance_{method}.pkl", frame)
        atomic_write_csv(out_dir / f"feature_importance_{method}.csv", frame, index=False)
        atomic_write_json(
            out_dir / f"method_{method}.json",
            {
                "features_key": expected_key,
                "seed": seed,
                "method": method,
                "label_level": label_level,
                "time_min": round(elapsed, 4),
                "peak_ram_gb": round(_peak_ram_gb(), 3),
            },
        )
        atomic_write_text(out_dir / f"_SUCCESS_{method}", "ok\n")

    invocation_wall_min = (time.time() - start) / 60.0
    feature_selection_time_min = sum(times.values())
    # If the previous metadata was lost (for example a kill between the method
    # writes and the features_meta write), the sum of the persisted method
    # times is the best available lower bound for the cumulative wall time.
    total_wall_min = max(
        previous_wall_min + invocation_wall_min,
        feature_selection_time_min,
    )
    meta = {
        "features_key": expected_key,
        "dataset": dataset["name"],
        "seed": seed,
        "label_level": label_level,
        "methods": methods,
        "method_times_min": {key: round(value, 4) for key, value in times.items()},
        "feature_selection_time_min": round(feature_selection_time_min, 4),
        "total_wall_time_min": round(total_wall_min, 4),
        "last_invocation_wall_time_min": round(invocation_wall_min, 4),
        "n_train_cells": int(len(cache["X_train"])),
        "n_genes": int(cache["X_train"].shape[1]),
        "peak_ram_gb": round(_peak_ram_gb(), 3),
    }
    atomic_write_json(out_dir / "features_meta.json", meta)
    mark_success(
        out_dir,
        {"features_key": expected_key, "seed": seed, "methods": methods},
    )
    logging.info(
        "Features finished for seed=%s: %s (compute %.2f min, cumulative wall %.2f min, "
        "this invocation %.2f min)",
        seed,
        methods,
        meta["feature_selection_time_min"],
        total_wall_min,
        invocation_wall_min,
    )
