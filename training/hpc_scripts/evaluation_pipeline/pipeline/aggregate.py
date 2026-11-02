"""Aggregate per-run result CSVs into mean/std summaries."""

from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

from .config import load_config
from .io import atomic_write_csv, ensure_dir, read_json
from .logging_utils import log_header
from .tasks import results_dir, run_key

SUMMARY_METRICS = [
    ("In-Distribution", "Baseline", "Overall", "Accuracy"),
    ("In-Distribution", "Classification Report", "macro avg", "f1-score"),
    ("All", "Technical_Metrics", "Resource_Usage", "Preprocessing_Time_Min"),
    ("All", "Technical_Metrics", "Resource_Usage", "Feature_Selection_Time_Min"),
    ("All", "Technical_Metrics", "Resource_Usage", "Feature_Task_Time_Min"),
    ("All", "Technical_Metrics", "Resource_Usage", "Hyperparameter_Tuning_Time_Min"),
    ("All", "Technical_Metrics", "Resource_Usage", "Training_Time_Min"),
    ("All", "Technical_Metrics", "Resource_Usage", "Inference_Evaluation_Time_Min"),
    ("All", "Technical_Metrics", "Resource_Usage", "Run_With_Setup_Time_Min"),
    ("All", "Technical_Metrics", "Resource_Usage", "Total_Pipeline_Time_Min"),
    ("All", "Technical_Metrics", "Resource_Usage", "Peak_RAM_GB"),
]


def _read_run(path: Path, meta_path: Path, expected_run_key: str | None) -> pd.DataFrame | None:
    if not path.is_file() or not meta_path.is_file():
        return None
    meta = read_json(meta_path, default={})
    if expected_run_key is not None and meta.get("run_key") != expected_run_key:
        logging.warning("Skipping stale run %s (run key mismatch).", path)
        return None
    try:
        return pd.read_csv(path, header=[0, 1, 2, 3], index_col=0)
    except Exception as exc:  # noqa: BLE001
        logging.error("Could not read %s: %s", path, exc)
        return None


def _aggregate_level(config: dict, model: str, level: str) -> tuple[pd.DataFrame | None, pd.DataFrame]:
    out_dir = ensure_dir(results_dir(config, model, level))
    frames = []
    status_rows = []
    seeds = list(config["experiment"]["seeds"])
    for seed_index, seed in enumerate(seeds):
        csv_path = out_dir / f"result_{seed_index}.csv"
        meta_path = out_dir / f"run_{seed_index}.json"
        success = (out_dir / f"_SUCCESS_run_{seed_index}").is_file()
        expected = run_key(config, model, seed_index)
        frame = _read_run(csv_path, meta_path, expected) if success else None
        if frame is not None:
            frames.append(frame)
            status_rows.append(
                {
                    "model": model,
                    "level": level,
                    "seed_index": seed_index,
                    "seed": seed,
                    "status": "done",
                    "path": str(csv_path),
                }
            )
        else:
            status_rows.append(
                {
                    "model": model,
                    "level": level,
                    "seed_index": seed_index,
                    "seed": seed,
                    "status": "missing" if not csv_path.exists() else "incomplete",
                    "path": str(csv_path),
                }
            )
    status = pd.DataFrame(status_rows)
    if not frames:
        logging.warning("No completed runs for model=%s level=%s", model, level)
        return None, status

    combined = pd.concat(frames, axis=0)
    means = combined.mean(numeric_only=True)
    stds = combined.std(numeric_only=True)
    combined_str = means.round(4).astype(str) + " +- " + stds.round(4).astype(str)
    stats = pd.DataFrame(
        [means, stds, combined_str],
        index=["mean", "std", "mean +- std"],
        columns=means.index,
    )
    final = pd.concat([combined, stats], axis=0)
    atomic_write_csv(out_dir / "combined_result.csv", final, index=True)
    logging.info(
        "Aggregated model=%s level=%s: %d runs, %d rows",
        model,
        level,
        len(frames),
        len(final),
    )
    return final, status


def run_aggregate(config_path: str) -> None:
    config = load_config(config_path)
    dataset = config["active_dataset"]
    log_header("aggregate", dataset=dataset["name"], output=config["output_dir"])
    summary_rows = []
    status_frames = []

    for model_name in config["experiment"]["models"]:
        model_cfg = config["active_models"][model_name]
        if bool(model_cfg.get("hierarchy")):
            levels = ["coarse", "fine"]
        else:
            levels = list(config["experiment"].get("reference_levels", ["coarse", "fine"]))
            if not dataset["labels"].get("fine"):
                levels = [level for level in levels if level != "fine"]
        for level in levels:
            final, status = _aggregate_level(config, model_name, level)
            status_frames.append(status)
            if final is None:
                continue
            means = final.loc["mean"]
            stds = final.loc["std"]
            for metric in SUMMARY_METRICS:
                if metric not in means.index:
                    continue
                summary_rows.append(
                    {
                        "dataset": dataset["name"],
                        "model": model_name,
                        "level": level,
                        "metric": " / ".join(metric),
                        "mean": means[metric],
                        "std": stds[metric],
                        "n_runs": int(status["status"].eq("done").sum()),
                    }
                )

    out_dir = ensure_dir(Path(config["output_dir"]) / "aggregate")
    if summary_rows:
        atomic_write_csv(out_dir / "summary.csv", pd.DataFrame(summary_rows), index=False)
    if status_frames:
        atomic_write_csv(
            out_dir / "run_status.csv",
            pd.concat(status_frames, axis=0, ignore_index=True),
            index=False,
        )
    logging.info("Aggregation finished. Results in %s", out_dir)
