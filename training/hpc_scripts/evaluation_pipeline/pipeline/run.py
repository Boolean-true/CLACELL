"""Run stage: fit a model for one seed and evaluate coarse + fine with test_robustness."""

from __future__ import annotations

import logging
import resource
import time
from pathlib import Path

import numpy as np
import pandas as pd

from . import bootstrap  # noqa: F401  (adds hpc_scripts/ and training/ to sys.path)
from .config import cpu_count, load_config, model_config
from .hierarchy import HierarchicalCascadeClassifier
from .io import (
    atomic_write_csv,
    atomic_write_json,
    atomic_write_text,
    clear_success,
    ensure_dir,
    read_json,
)
from .logging_utils import PipelineError, log_header
from .models.autoencoder import collect_epochs
from .models.registry import (
    make_factory,
    robustness_feature_importance,
)
from .tasks import (
    current_cache_key,
    features_dir,
    features_success,
    get_task,
    levels_for_model,
    load_cache,
    results_dir,
    run_key,
    run_success,
    tuning_dir,
    tuning_success,
)

from test_robustness_higher_dropout import test_robustness  # noqa: E402


class _CoarseWrapper:
    def __init__(self, model):
        self.model = model

    def predict(self, X):
        return self.model.predict_coarse(X)


class _FineWrapper:
    def __init__(self, model):
        self.model = model

    def predict(self, X):
        return self.model.predict_fine(X)


def _peak_ram_gb() -> float:
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024)


def _safe_float(value, default=float("nan")) -> float:
    try:
        if value is None:
            return default
        value = float(value)
        if np.isnan(value):
            return default
        return value
    except Exception:  # noqa: BLE001
        return default


def _load_params(config: dict, model_name: str, node: str) -> dict:
    model_cfg = model_config(config, model_name)
    path = tuning_dir(config, model_name, node) / "best_params.json"
    if model_cfg.get("tune") and not tuning_success(config, model_name, node):
        raise PipelineError(
            f"Tuning is missing, failed or stale for model='{model_name}' node='{node}'. "
            f"Expected success marker in {path.parent}. Re-run the tune stage."
        )
    if not path.is_file():
        if model_cfg.get("tune"):
            raise PipelineError(
                f"Missing tuned parameters for model='{model_name}' node='{node}': {path}. "
                "Run the tune stage for this model/node first."
            )
        return {}
    return read_json(path, default={})


def _tuning_meta(config: dict, model_name: str, node: str) -> dict:
    path = tuning_dir(config, model_name, node) / "tuning_meta.json"
    if not path.is_file():
        return {}
    return read_json(path, default={})


def _level_tuning_summary(
    config: dict,
    model_name: str,
    level: str,
    hierarchy: dict,
    hierarchical: bool = True,
) -> dict:
    if not hierarchical:
        nodes = [level]
    elif level == "coarse":
        nodes = ["coarse"]
    else:
        nodes = [
            node for node in hierarchy.get("nodes", {}) if node.startswith("fine:")
        ]
    metas = [_tuning_meta(config, model_name, node) for node in nodes]
    metas = [meta for meta in metas if meta]
    if not metas:
        return {
            "time_min": 0.0,
            "peak_ram_gb": float("nan"),
            "avg_time_per_iteration_sec": float("nan"),
        }
    time_min = sum(_safe_float(meta.get("tuning_time_min"), 0.0) for meta in metas)
    peak = max(_safe_float(meta.get("peak_ram_gb"), 0.0) for meta in metas)
    avg_values = [
        _safe_float(meta.get("avg_time_per_iteration_sec"))
        for meta in metas
        if meta.get("avg_time_per_iteration_sec") is not None
    ]
    avg = float(np.nanmean(avg_values)) if avg_values else float("nan")
    return {"time_min": time_min, "peak_ram_gb": peak, "avg_time_per_iteration_sec": avg}


def _add_technical_metrics(
    frame: pd.DataFrame,
    *,
    preprocessing_time_min: float,
    feature_selection_time_min: float,
    tuning_time_min: float,
    training_time_min: float,
    eval_time_min: float,
    peak_ram_gb: float,
    preprocessing_peak_ram_gb: float,
    tuning_peak_ram_gb: float,
    autoencoder_epochs: float,
    avg_time_per_iteration_sec: float,
) -> pd.DataFrame:
    frame = frame.copy()
    base = ("All", "Technical_Metrics", "Resource_Usage")
    frame[base + ("Preprocessing_Time_Min",)] = round(float(preprocessing_time_min), 2)
    frame[base + ("Feature_Selection_Time_Min",)] = round(float(feature_selection_time_min), 2)
    frame[base + ("Hyperparameter_Tuning_Time_Min",)] = round(float(tuning_time_min), 2)
    frame[base + ("Training_Time_Min",)] = round(float(training_time_min), 2)
    frame[base + ("Inference_Evaluation_Time_Min",)] = round(float(eval_time_min), 2)
    frame[base + ("Total_Pipeline_Time_Min",)] = round(float(training_time_min + eval_time_min), 2)
    frame[base + ("End_To_End_Time_Min",)] = round(
        float(
            preprocessing_time_min
            + feature_selection_time_min
            + tuning_time_min
            + training_time_min
            + eval_time_min
        ),
        2,
    )
    frame[base + ("Peak_RAM_GB",)] = round(float(peak_ram_gb), 3)
    frame[base + ("Preprocessing_Peak_RAM_GB",)] = round(float(preprocessing_peak_ram_gb), 3)
    frame[base + ("Tuning_Peak_RAM_GB",)] = round(float(tuning_peak_ram_gb), 3)
    frame[base + ("Avg_Time_per_Iteration_Sec",)] = (
        round(float(avg_time_per_iteration_sec), 2)
        if not np.isnan(_safe_float(avg_time_per_iteration_sec))
        else np.nan
    )
    frame[("All", "Technical_Metrics", "Training_Convergence", "Autoencoder_Epochs")] = (
        float(autoencoder_epochs) if not np.isnan(_safe_float(autoencoder_epochs)) else np.nan
    )
    return frame


def _evaluate(
    wrapper,
    X_test: pd.DataFrame,
    y_test: pd.Series,
    donor_test: pd.Series,
    label_col: str,
    feature_importance: pd.DataFrame,
    model_name: str,
    level: str,
    eval_seed: int,
) -> tuple[pd.DataFrame, float]:
    start = time.time()
    result = test_robustness(
        wrapper,
        X_test,
        y_test,
        donor_test,
        label_col,
        None,
        feature_importance,
        log_to_console=True,
        log_to_file=False,
        seed=int(eval_seed),
    )
    elapsed = (time.time() - start) / 60.0
    if result is None:
        raise PipelineError(
            f"test_robustness returned None for model='{model_name}' level='{level}'. "
            "Check the input matrix and the model's predict method."
        )
    if not isinstance(result, pd.DataFrame):
        raise PipelineError(
            f"test_robustness returned {type(result).__name__} instead of DataFrame for "
            f"model='{model_name}' level='{level}'."
        )
    return result, elapsed


def _write_level(
    config: dict,
    model_name: str,
    level: str,
    seed_index: int,
    frame: pd.DataFrame,
    meta: dict,
) -> None:
    out_dir = ensure_dir(results_dir(config, model_name, level))
    csv_path = out_dir / f"result_{seed_index}.csv"
    json_path = out_dir / f"run_{seed_index}.json"
    meta = dict(meta)
    meta["cache_key"] = current_cache_key(config)
    meta["run_key"] = run_key(config, model_name, seed_index)
    atomic_write_csv(csv_path, frame, index=True)
    atomic_write_json(json_path, meta)
    atomic_write_text(out_dir / f"_SUCCESS_run_{seed_index}", "ok\n")


def _run_hierarchical(
    config: dict,
    cache: dict,
    model_name: str,
    seed_index: int,
    seed: int,
    n_jobs: int,
) -> None:
    dataset = config["active_dataset"]
    coarse_col = dataset["labels"]["coarse"]
    fine_col = dataset["labels"]["fine"]
    hierarchy = cache["hierarchy"]
    min_fine_classes = int(config["experiment"]["hierarchy"].get("min_fine_classes", 2))

    coarse_params = _load_params(config, model_name, "coarse")
    fine_params = {}
    for node in hierarchy.get("nodes", {}):
        if node.startswith("fine:"):
            coarse_label = node.split(":", 1)[1]
            fine_params[coarse_label] = _load_params(config, model_name, node)

    coarse_factory = make_factory(config, model_name, "coarse", coarse_params, seed, n_jobs)
    fine_factories = {
        coarse_label: make_factory(config, model_name, f"fine:{coarse_label}", params, seed, n_jobs)
        for coarse_label, params in fine_params.items()
    }
    model = HierarchicalCascadeClassifier(
        coarse_factory=coarse_factory,
        fine_factories=fine_factories,
        min_fine_classes=min_fine_classes,
        name=model_name,
    )
    logging.info("Fitting hierarchical model=%s seed=%s", model_name, seed)
    start = time.time()
    model.fit(
        X=cache["X_train"],
        y_coarse=cache["obs_train"][coarse_col].astype(str),
        y_fine=cache["obs_train"][fine_col].astype(str),
        sample_meta=cache["obs_train"],
    )
    training_time_min = (time.time() - start) / 60.0

    fi_method = robustness_feature_importance(config, model_name)
    fi_dir = features_dir(config, seed)
    fi_path = fi_dir / f"feature_importance_{fi_method}.pkl"
    if not fi_path.is_file():
        raise PipelineError(
            f"Robustness feature importance '{fi_method}' not found at {fi_path}. "
            "Run the features stage for this seed."
        )
    feature_importance = pd.read_pickle(fi_path)

    X_test = cache["X_test"]
    donor_test = cache["obs_test"][dataset["batch_key"]].astype(str)
    y_test_coarse = cache["obs_test"][coarse_col].astype(str)
    y_test_fine = cache["obs_test"][fine_col].astype(str)

    logging.info("Evaluating coarse level (model=%s seed=%s)", model_name, seed)
    coarse_frame, coarse_eval_min = _evaluate(
        _CoarseWrapper(model),
        X_test,
        y_test_coarse,
        donor_test,
        coarse_col,
        feature_importance,
        model_name,
        "coarse",
        eval_seed=int(config["experiment"]["eval_seed_base"]) + seed_index,
    )
    logging.info("Evaluating fine level (model=%s seed=%s)", model_name, seed)
    fine_frame, fine_eval_min = _evaluate(
        _FineWrapper(model),
        X_test,
        y_test_fine,
        donor_test,
        fine_col,
        feature_importance,
        model_name,
        "fine",
        eval_seed=int(config["experiment"]["eval_seed_base"]) + seed_index,
    )

    peak_ram = _peak_ram_gb()
    prepare_meta = cache["prepare_meta"]
    features_meta = read_json(fi_dir / "features_meta.json", default={})
    preprocessing_time = _safe_float(prepare_meta.get("preprocessing_time_min"), 0.0)
    feature_selection_time = _safe_float(features_meta.get("feature_selection_time_min"), 0.0)
    preprocessing_peak = _safe_float(prepare_meta.get("peak_ram_gb"), 0.0)
    epochs = collect_epochs(model)

    for level, frame, eval_min in (
        ("coarse", coarse_frame, coarse_eval_min),
        ("fine", fine_frame, fine_eval_min),
    ):
        tuning = _level_tuning_summary(config, model_name, level, hierarchy)
        frame = _add_technical_metrics(
            frame,
            preprocessing_time_min=preprocessing_time,
            feature_selection_time_min=feature_selection_time,
            tuning_time_min=tuning["time_min"],
            training_time_min=training_time_min,
            eval_time_min=eval_min,
            peak_ram_gb=peak_ram,
            preprocessing_peak_ram_gb=preprocessing_peak,
            tuning_peak_ram_gb=tuning["peak_ram_gb"],
            autoencoder_epochs=epochs,
            avg_time_per_iteration_sec=tuning["avg_time_per_iteration_sec"],
        )
        meta = {
            "dataset": dataset["name"],
            "model": model_name,
            "mode": "hierarchical",
            "level": level,
            "seed_index": seed_index,
            "seed": seed,
            "eval_seed": int(config["experiment"]["eval_seed_base"]) + seed_index,
            "training_time_min": round(training_time_min, 4),
            "evaluation_time_min": round(eval_min, 4),
            "preprocessing_time_min": preprocessing_time,
            "feature_selection_time_min": feature_selection_time,
            "tuning_time_min": tuning["time_min"],
            "peak_ram_gb": round(peak_ram, 3),
            "autoencoder_epochs": epochs,
            "coarse_params": coarse_params,
            "fine_params": fine_params,
            "hierarchy_nodes": list(hierarchy.get("nodes", {}).keys()),
        }
        _write_level(config, model_name, level, seed_index, frame, meta)

    logging.info(
        "Finished hierarchical run model=%s seed=%s: train=%.2f min coarse_eval=%.2f min fine_eval=%.2f min",
        model_name,
        seed,
        training_time_min,
        coarse_eval_min,
        fine_eval_min,
    )


def _run_flat(
    config: dict,
    cache: dict,
    model_name: str,
    seed_index: int,
    seed: int,
    n_jobs: int,
) -> None:
    dataset = config["active_dataset"]
    coarse_col = dataset["labels"]["coarse"]
    fine_col = dataset["labels"].get("fine")
    levels = [level for level in config["experiment"].get("reference_levels", ["coarse", "fine"]) if level != "fine" or fine_col]
    hierarchy = cache["hierarchy"]
    prepare_meta = cache["prepare_meta"]
    fi_method = robustness_feature_importance(config, model_name)
    fi_dir = features_dir(config, seed)
    fi_path = fi_dir / f"feature_importance_{fi_method}.pkl"
    if not fi_path.is_file():
        raise PipelineError(
            f"Robustness feature importance '{fi_method}' not found at {fi_path}. "
            "Run the features stage for this seed."
        )
    feature_importance = pd.read_pickle(fi_path)

    features_meta = read_json(fi_dir / "features_meta.json", default={})
    preprocessing_time = _safe_float(prepare_meta.get("preprocessing_time_min"), 0.0)
    feature_selection_time = _safe_float(features_meta.get("feature_selection_time_min"), 0.0)
    preprocessing_peak = _safe_float(prepare_meta.get("peak_ram_gb"), 0.0)

    X_test = cache["X_test"]
    donor_test = cache["obs_test"][dataset["batch_key"]].astype(str)
    epochs_total = 0.0
    epoch_seen = False

    for level in levels:
        label_col = coarse_col if level == "coarse" else fine_col
        y_train = cache["obs_train"][label_col].astype(str)
        y_test = cache["obs_test"][label_col].astype(str)
        params = _load_params(config, model_name, level)
        factory = make_factory(config, model_name, level, params, seed, n_jobs)
        model = factory()
        logging.info("Fitting flat model=%s level=%s seed=%s", model_name, level, seed)
        start = time.time()
        model.fit(cache["X_train"], y_train, cache["obs_train"])
        training_time_min = (time.time() - start) / 60.0
        if getattr(model, "epochs_", None) is not None:
            epochs_total += float(model.epochs_)
            epoch_seen = True

        logging.info("Evaluating flat model=%s level=%s seed=%s", model_name, level, seed)
        frame, eval_min = _evaluate(
            model,
            X_test,
            y_test,
            donor_test,
            label_col,
            feature_importance,
            model_name,
            level,
            eval_seed=int(config["experiment"]["eval_seed_base"]) + seed_index,
        )
        tuning = _level_tuning_summary(
            config, model_name, level, hierarchy, hierarchical=False
        )
        frame = _add_technical_metrics(
            frame,
            preprocessing_time_min=preprocessing_time,
            feature_selection_time_min=feature_selection_time,
            tuning_time_min=tuning["time_min"],
            training_time_min=training_time_min,
            eval_time_min=eval_min,
            peak_ram_gb=_peak_ram_gb(),
            preprocessing_peak_ram_gb=preprocessing_peak,
            tuning_peak_ram_gb=tuning["peak_ram_gb"],
            autoencoder_epochs=epochs_total if epoch_seen else float("nan"),
            avg_time_per_iteration_sec=tuning["avg_time_per_iteration_sec"],
        )
        meta = {
            "dataset": dataset["name"],
            "model": model_name,
            "mode": "flat",
            "level": level,
            "seed_index": seed_index,
            "seed": seed,
            "eval_seed": int(config["experiment"]["eval_seed_base"]) + seed_index,
            "training_time_min": round(training_time_min, 4),
            "evaluation_time_min": round(eval_min, 4),
            "preprocessing_time_min": preprocessing_time,
            "feature_selection_time_min": feature_selection_time,
            "tuning_time_min": tuning["time_min"],
            "params": params,
        }
        _write_level(config, model_name, level, seed_index, frame, meta)


def run_run(config_path: str, task_id: int) -> None:
    config = load_config(config_path)
    task = get_task(config, "run", task_id)
    if task is None:
        logging.info("Run task %s is outside the manifest; nothing to do.", task_id)
        return
    dataset = config["active_dataset"]
    model_name = str(task["model"])
    seed_index = int(task["seed_index"])
    seed = int(task["seed"])
    log_header(
        "run",
        dataset=dataset["name"],
        model=model_name,
        seed_index=seed_index,
        seed=seed,
        task_id=task_id,
    )
    if run_success(config, model_name, seed_index):
        logging.info("Run cache hit for model=%s seed_index=%s", model_name, seed_index)
        return
    for level in levels_for_model(config, model_name):
        directory = results_dir(config, model_name, level)
        clear_success(directory)
        ensure_dir(directory)

    cache = load_cache(config)
    if not features_success(config, seed):
        raise PipelineError(
            f"Feature rankings for seed={seed} are missing or stale in "
            f"{features_dir(config, seed)}. Run the features stage first."
        )
    model_cfg = model_config(config, model_name)
    n_jobs = cpu_count(config, "run")
    if bool(model_cfg.get("hierarchy")):
        _run_hierarchical(config, cache, model_name, seed_index, seed, n_jobs)
    else:
        _run_flat(config, cache, model_name, seed_index, seed, n_jobs)
