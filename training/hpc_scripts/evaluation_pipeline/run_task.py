#!/usr/bin/env python3
"""Command-line entry point for one pipeline task.

Examples
--------
python evaluation_pipeline/run_task.py prepare   --config evaluation_pipeline/configs/experiment.yaml
python evaluation_pipeline/run_task.py features  --config ... --task-id 0
python evaluation_pipeline/run_task.py tune      --config ... --task-id 0
python evaluation_pipeline/run_task.py run       --config ... --task-id 0
python evaluation_pipeline/run_task.py aggregate --config ...
python evaluation_pipeline/run_task.py plan      --config ...
python evaluation_pipeline/run_task.py status    --config ...
"""

from __future__ import annotations

import argparse
import json
import logging
import sys
import traceback
from pathlib import Path

# Make ``pipeline`` importable when this file is executed directly.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from pipeline.aggregate import run_aggregate  # noqa: E402
from pipeline.config import load_config  # noqa: E402
from pipeline.logging_utils import (  # noqa: E402
    record_failure,
    setup_logging,
    task_context,
)
from pipeline.tasks import generate_manifests, status  # noqa: E402


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CLACELL evaluation pipeline task runner")
    parser.add_argument(
        "command",
        choices=["prepare", "features", "plan", "tune", "run", "aggregate", "status", "export-scgpt"],
    )
    parser.add_argument("--config", required=True, help="Path to the experiment YAML.")
    parser.add_argument("--task-id", type=int, default=None, help="Array task id.")
    parser.add_argument("--log-level", default="INFO")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    setup_logging(getattr(logging, str(args.log_level).upper(), logging.INFO))
    context = {"command": args.command, "task_id": args.task_id}

    config = None
    try:
        config = load_config(args.config)
        context["dataset"] = config["active_dataset"]["name"]
    except Exception:  # noqa: BLE001 - config might be broken; still report clearly
        logging.error("Could not load config %s", args.config)
        traceback.print_exc()
        return 2

    if args.command in {"features", "tune", "run"} and args.task_id is not None:
        try:
            from pipeline.tasks import get_task

            task = get_task(config, args.command, args.task_id)
            if task:
                context["model"] = task.get("model")
                if args.command == "tune":
                    context["node"] = task.get("node")
                else:
                    context["seed_index"] = task.get("seed_index")
                    context["seed"] = task.get("seed")
        except Exception:  # noqa: BLE001 - do not hide the real task failure
            pass

    try:
        if args.command == "prepare":
            from pipeline.prepare import run_prepare

            run_prepare(args.config)
        elif args.command == "features":
            if args.task_id is None:
                raise SystemExit("--task-id is required for the features command")
            from pipeline.features_stage import run_features

            run_features(args.config, args.task_id)
        elif args.command == "plan":
            plan = generate_manifests(config)
            print(json.dumps(plan, indent=2))
        elif args.command == "tune":
            if args.task_id is None:
                raise SystemExit("--task-id is required for the tune command")
            from pipeline.tuning import run_tune

            run_tune(args.config, args.task_id)
        elif args.command == "run":
            if args.task_id is None:
                raise SystemExit("--task-id is required for the run command")
            from pipeline.run import run_run

            run_run(args.config, args.task_id)
        elif args.command == "aggregate":
            run_aggregate(args.config)
        elif args.command == "status":
            print(json.dumps(status(config), indent=2))
        elif args.command == "export-scgpt":
            from pipeline.models.references import export_scgpt_input

            path = export_scgpt_input(config)
            print(path)
        else:  # pragma: no cover - argparse prevents this
            parser.error(f"Unknown command {args.command}")
        return 0
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001 - HPC logs need full context
        logging.error("FAILED %s", task_context(**context))
        logging.error("%s: %s", type(exc).__name__, exc)
        logging.error("Traceback:\n%s", traceback.format_exc())
        try:
            record_failure(config, args.command, exc, **context)
        except Exception:  # noqa: BLE001
            logging.error("Could not write failure record.")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
