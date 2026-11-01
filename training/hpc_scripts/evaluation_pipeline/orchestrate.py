#!/usr/bin/env python3
"""Submit the evaluation pipeline stages to Slurm.

Typical pilot usage
-------------------
python evaluation_pipeline/orchestrate.py --config evaluation_pipeline/configs/experiment.yaml --stage prepare
python evaluation_pipeline/orchestrate.py --config ... --stage plan
python evaluation_pipeline/orchestrate.py --config ... --stage features
python evaluation_pipeline/orchestrate.py --config ... --stage tune
python evaluation_pipeline/orchestrate.py --config ... --stage run
python evaluation_pipeline/orchestrate.py --config ... --stage aggregate

Or, for a hands-off pilot run:
python evaluation_pipeline/orchestrate.py --config ... --stage all
"""

from __future__ import annotations

import argparse
import json
import shlex
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # hpc_scripts/
PIPELINE = Path(__file__).resolve().parent
sys.path.insert(0, str(PIPELINE))

from pipeline.config import load_config  # noqa: E402
from pipeline.io import atomic_write_json, ensure_dir, read_json  # noqa: E402
from pipeline.tasks import cache_ready, generate_manifests, status  # noqa: E402


def _parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Submit CLACELL evaluation pipeline jobs")
    parser.add_argument("--config", required=True)
    parser.add_argument(
        "--stage",
        required=True,
        choices=["prepare", "plan", "features", "tune", "run", "aggregate", "all", "status"],
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-wait", action="store_true", help="For --stage all: do not block.")
    parser.add_argument("--max-parallel", type=int, default=None)
    return parser.parse_args()


def _resources(config: dict, stage: str) -> dict:
    return config["experiment"]["resources"][stage]


def _job_name(config: dict, stage: str) -> str:
    return f"clacell-{stage}-{config['active_dataset']['name']}"


def _state_path(config: dict) -> Path:
    return Path(config["output_dir"]) / "submission.json"


def _record_job(config: dict, stage: str, job_id: str | None) -> None:
    if not job_id:
        return
    path = _state_path(config)
    state = read_json(path, default={})
    state[stage] = job_id
    ensure_dir(path.parent)
    atomic_write_json(path, state)


def _last_job(config: dict, stage: str) -> str | None:
    state = read_json(_state_path(config), default={})
    return state.get(stage)


def _job_active(job_id: str | None) -> bool:
    if not job_id:
        return False
    try:
        result = subprocess.run(
            ["squeue", "-h", "-j", str(job_id)],
            text=True,
            capture_output=True,
        )
    except FileNotFoundError:
        return False
    return result.returncode == 0 and bool(result.stdout.strip())


def _sbatch(
    config: dict,
    stage: str,
    script: str,
    array: str | None = None,
    wait: bool = False,
    dry_run: bool = False,
    dependency: str | None = None,
) -> str | None:
    res = _resources(config, stage)
    logs = ROOT / "logs"
    logs.mkdir(parents=True, exist_ok=True)
    suffix = "%x_%A_%a" if array else "%x_%j"
    cmd = [
        "sbatch",
        "--parsable",
        f"--job-name={_job_name(config, stage)}",
        f"--cpus-per-task={int(res['cpus'])}",
        f"--mem={int(res['mem_gb'])}G",
        f"--time={res['time']}",
        f"--output={logs}/{suffix}.out",
        f"--error={logs}/{suffix}.err",
    ]
    if array:
        cmd.append(f"--array={array}")
    if dependency:
        cmd.append(f"--dependency={dependency}")
    if wait:
        cmd.append("--wait")
    cmd.extend([str(ROOT / script), str(Path(args.config).resolve())])
    printable = " ".join(shlex.quote(part) for part in cmd)
    if dry_run:
        print(printable)
        return None
    print("+", printable, flush=True)
    result = subprocess.run(cmd, text=True, capture_output=True)
    if result.returncode != 0:
        sys.stderr.write(result.stdout)
        sys.stderr.write(result.stderr)
        raise RuntimeError(f"sbatch failed for stage {stage}.")
    job_id = result.stdout.strip().splitlines()[-1] if result.stdout.strip() else None
    if job_id:
        _record_job(config, stage, job_id)
        print(f"{stage}: job {job_id}", flush=True)
    return job_id


def _plan(config: dict) -> dict:
    plan = generate_manifests(config)
    print(json.dumps(plan, indent=2), flush=True)
    return plan


def _submit_stage(config: dict, stage: str, wait: bool, max_parallel: int, dry_run: bool):
    if stage == "prepare":
        # Always submit prepare; run_prepare is a fast no-op on a valid cache and
        # rebuilds automatically when the dataset/preprocessing key changes.
        return _sbatch(config, "prepare", "submit_prepare.sh", wait=wait, dry_run=dry_run)
    if stage == "plan":
        return _plan(config)
    if stage in {"features", "tune", "run"}:
        plan = _plan(config)
        n_tasks = int(plan[f"{stage}_tasks"])
        if n_tasks == 0:
            print(f"No {stage} tasks in the manifest.")
            return None
        array = f"0-{n_tasks - 1}%{max_parallel}"
        script = {
            "features": "submit_features.sh",
            "tune": "submit_tune.sh",
            "run": "submit_run.sh",
        }[stage]
        dependency = None
        if stage == "run":
            active = [
                _last_job(config, upstream)
                for upstream in ("features", "tune")
                if _job_active(_last_job(config, upstream))
            ]
            if active:
                dependency = "afterok:" + ":".join(active)
        return _sbatch(
            config,
            stage,
            script,
            array=array,
            wait=wait,
            dry_run=dry_run,
            dependency=dependency,
        )
    if stage == "aggregate":
        dependency = None
        run_job = _last_job(config, "run")
        if _job_active(run_job):
            dependency = f"afterany:{run_job}"
        return _sbatch(
            config,
            "aggregate",
            "submit_aggregate.sh",
            wait=wait,
            dry_run=dry_run,
            dependency=dependency,
        )
    raise ValueError(f"Unknown stage {stage}")


def _run_main() -> int:
    global args
    args = _parse()
    config = load_config(args.config)
    max_parallel = args.max_parallel or int(config["experiment"].get("max_parallel", 4))

    if args.stage == "status":
        print(json.dumps(status(config), indent=2))
        return 0

    if args.stage == "plan":
        _plan(config)
        return 0

    if args.stage == "all":
        if args.dry_run:
            _submit_stage(config, "prepare", wait=False, max_parallel=max_parallel, dry_run=True)
            if not cache_ready(config):
                print("Prepare is required before the downstream commands can be planned.")
                return 0
            _plan(config)
            _submit_stage(config, "features", wait=False, max_parallel=max_parallel, dry_run=True)
            _submit_stage(config, "tune", wait=False, max_parallel=max_parallel, dry_run=True)
            _submit_stage(config, "run", wait=False, max_parallel=max_parallel, dry_run=True)
            _submit_stage(config, "aggregate", wait=False, max_parallel=max_parallel, dry_run=True)
            return 0
        wait = not args.no_wait
        _submit_stage(config, "prepare", wait=wait, max_parallel=max_parallel, dry_run=args.dry_run)
        if not wait:
            print("Prepare submitted. Re-run --stage all after it finishes, or use --stage plan/tune/run.")
            return 0
        # Re-load after prepare so the cache and manifests are current.
        config = load_config(args.config)
        _plan(config)
        _submit_stage(config, "features", wait=True, max_parallel=max_parallel, dry_run=args.dry_run)
        st = status(config)
        if st["features_missing"]:
            print("Some features tasks are missing/failed:", st["features_missing"])
            print("Check logs/ and failures/. Re-run the missing task IDs before the run stage.")
            return 1
        _submit_stage(config, "tune", wait=True, max_parallel=max_parallel, dry_run=args.dry_run)
        st = status(config)
        if st["tune_missing"]:
            print("Some tuning tasks are missing/failed:", st["tune_missing"])
            print("Check logs/ and failures/. Re-run the missing task IDs before the run stage.")
            return 1
        _submit_stage(config, "run", wait=True, max_parallel=max_parallel, dry_run=args.dry_run)
        _submit_stage(config, "aggregate", wait=True, max_parallel=max_parallel, dry_run=args.dry_run)
        print(json.dumps(status(config), indent=2))
        return 0

    _submit_stage(
        config,
        args.stage,
        wait=False,
        max_parallel=max_parallel,
        dry_run=args.dry_run,
    )
    return 0


def main() -> int:
    try:
        return _run_main()
    except Exception as exc:  # noqa: BLE001 - clear HPC-facing error
        sys.stderr.write(f"ERROR: {type(exc).__name__}: {exc}\n")
        sys.stderr.write("Check the stage logs under logs/ and the task status with --stage status.\n")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
