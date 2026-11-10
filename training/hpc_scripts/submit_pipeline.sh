#!/bin/bash -l

#SBATCH --job-name=clacell-submit-pipeline
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=200G
#SBATCH --time=1:00:00
#SBATCH --constraint=icx
#SBATCH --export=NONE
#SBATCH --output=clacell-submit_%j.out
#SBATCH --error=clacell-submit_%j.err

set -euo pipefail
unset SLURM_EXPORT_ENV

# SCRIPT_DIR is hardcoded because the job does not inherit the submit directory.
SCRIPT_DIR="/home/woody/iwbn/iwbn133h"

source /apps/python/3.12-conda/etc/profile.d/conda.sh
conda activate test_clacell

CONFIG="${1:-$SCRIPT_DIR/evaluation_pipeline/configs/experiment.yaml}"
CONFIG="$(realpath "$CONFIG")"

if ! command -v sbatch >/dev/null 2>&1; then
  echo "ERROR: sbatch ist auf diesem Node nicht verfuegbar." >&2
  exit 1
fi

# 1) Prepare (Cache-Hit = sofort fertig)
python evaluation_pipeline/run_task.py prepare --config "$CONFIG"

# 2) Manifeste erzeugen
python evaluation_pipeline/orchestrate.py --config "$CONFIG" --stage plan

# 3) Task-Zahlen aus plan.json lesen
read -r FEATURES_TASKS TUNE_TASKS RUN_TASKS MAX_PARALLEL < <(
python - "$CONFIG" <<'PY'
import json, sys
from pathlib import Path
sys.path.insert(0, "evaluation_pipeline")
from pipeline.config import load_config

cfg = load_config(sys.argv[1])
plan = json.loads(
    (Path(cfg["output_dir"]) / "manifests" / "plan.json").read_text()
)
print(
    plan["features_tasks"],
    plan["tune_tasks"],
    plan["run_tasks"],
    int(cfg["experiment"].get("max_parallel", 4)),
)
PY
)

[ "$MAX_PARALLEL" -ge 1 ] || MAX_PARALLEL=1

# 4) Features
FEATURES_JOB=$(sbatch --parsable \
  --array="0-$((FEATURES_TASKS - 1))%${MAX_PARALLEL}" \
  --output="$SCRIPT_DIR/logs/%x_%A_%a.out" \
  --error="$SCRIPT_DIR/logs/%x_%A_%a.err" \
  "$SCRIPT_DIR/submit_features.sh" "$CONFIG")
echo "features: $FEATURES_JOB (${FEATURES_TASKS} Tasks)"

# 5) Tune
TUNE_JOB=""
if [ "$TUNE_TASKS" -gt 0 ]; then
  TUNE_JOB=$(sbatch --parsable \
    --dependency="afterok:${FEATURES_JOB}" \
    --array="0-$((TUNE_TASKS - 1))%${MAX_PARALLEL}" \
    --output="$SCRIPT_DIR/logs/%x_%A_%a.out" \
    --error="$SCRIPT_DIR/logs/%x_%A_%a.err" \
    "$SCRIPT_DIR/submit_tune.sh" "$CONFIG")
  echo "tune: $TUNE_JOB (${TUNE_TASKS} Tasks)"
else
  echo "tune: keine Tasks"
fi

# 6) Run
RUN_DEP="afterok:${FEATURES_JOB}"
if [ -n "$TUNE_JOB" ]; then
  RUN_DEP="${RUN_DEP}:${TUNE_JOB}"
fi

RUN_JOB=$(sbatch --parsable \
  --dependency="$RUN_DEP" \
  --array="0-$((RUN_TASKS - 1))%${MAX_PARALLEL}" \
  --output="$SCRIPT_DIR/logs/%x_%A_%a.out" \
  --error="$SCRIPT_DIR/logs/%x_%A_%a.err" \
  "$SCRIPT_DIR/submit_run.sh" "$CONFIG")
echo "run: $RUN_JOB (${RUN_TASKS} Tasks)"

# 7) Aggregate
AGG_JOB=$(sbatch --parsable \
  --dependency="afterany:${RUN_JOB}" \
  --output="$SCRIPT_DIR/logs/%x_%j.out" \
  --error="$SCRIPT_DIR/logs/%x_%j.err" \
  "$SCRIPT_DIR/submit_aggregate.sh" "$CONFIG")
echo "aggregate: $AGG_JOB"
