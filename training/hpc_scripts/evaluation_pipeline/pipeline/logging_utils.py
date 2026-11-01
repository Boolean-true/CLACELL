"""Logging and error-context helpers."""

from __future__ import annotations

import json
import logging
import os
import sys
import traceback
from contextlib import contextmanager
from pathlib import Path
from typing import Any

from .io import atomic_write_json, ensure_dir


class PipelineError(RuntimeError):
    """Base error for pipeline failures with a machine-readable context."""

    def __init__(self, message: str, **context: Any):
        self.context = {key: value for key, value in context.items() if value is not None}
        suffix = " ".join(f"{key}={value!r}" for key, value in self.context.items())
        super().__init__(f"{message}" + (f" [{suffix}]" if suffix else ""))


def task_context(**kwargs: Any) -> str:
    return " ".join(f"{key}={value!r}" for key, value in kwargs.items() if value is not None)


def setup_logging(level: int = logging.INFO) -> None:
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)-7s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        stream=sys.stdout,
        force=True,
    )


def log_header(stage: str, **context: Any) -> None:
    logging.info("=" * 78)
    logging.info("STAGE %s | %s", stage, task_context(**context))
    logging.info("=" * 78)


def failure_path(config: dict, stage: str, **context: Any) -> Path:
    base = Path(config["output_dir"]) / "failures"
    ensure_dir(base)
    parts = [stage]
    for key in ("model", "node", "seed_index", "dataset"):
        if context.get(key) is not None:
            parts.append(f"{key}-{context[key]}")
    safe = "_".join(str(part).replace("/", "_").replace(":", "_") for part in parts)
    return base / f"{safe}.json"


def record_failure(config: dict, stage: str, error: BaseException, **context: Any) -> Path:
    payload = {
        "stage": stage,
        "context": {key: value for key, value in context.items() if value is not None},
        "error_type": type(error).__name__,
        "error": str(error),
        "traceback": traceback.format_exc(),
    }
    path = failure_path(config, stage, **context)
    atomic_write_json(path, payload)
    logging.error("Failure details written to %s", path)
    return path


@contextmanager
def stage_guard(config: dict, stage: str, **context: Any):
    """Log a descriptive failure, write FAILED.json and re-raise."""
    try:
        yield
    except Exception as exc:  # noqa: BLE001 - intentionally broad for HPC logs
        context_str = task_context(**context)
        logging.error("FAILED stage=%s %s", stage, context_str)
        logging.error("%s: %s", type(exc).__name__, exc)
        logging.error("Traceback:\n%s", traceback.format_exc())
        record_failure(config, stage, exc, **context)
        raise
