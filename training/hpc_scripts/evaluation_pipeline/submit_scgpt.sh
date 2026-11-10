#!/bin/bash -l

#SBATCH --job-name=scgpt
#SBATCH --gres=gpu:a100:1
#SBATCH --partition=a100
#SBATCH --time=24:00:00
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
#SBATCH --export=NONE

set -eo pipefail
unset SLURM_EXPORT_ENV

DATA_DIR="${1:?usage: submit_scgpt.sh /path/to/scgpt_export_dir [coarse|fine] [num_runs]}"
LEVEL="${2:-coarse}"
NUM_RUNS="${3:-10}"
DATA_DIR="$(realpath "$DATA_DIR")"

HPC_DIR="/home/woody/iwbn/iwbn133h"
SCRIPT_DIR="$HPC_DIR/evaluation_pipeline"

source /apps/python/3.12-conda/etc/profile.d/conda.sh
conda activate scgpt_env

export PYTHONPATH="$HPC_DIR:$SCRIPT_DIR/pipeline/models${PYTHONPATH:+:$PYTHONPATH}"
if [ -d "$HPC_DIR/scGPT/examples" ]; then
  export PYTHONPATH="$HPC_DIR/scGPT/examples:$PYTHONPATH"
fi
export SCGPT_EXPORT_JSON="$DATA_DIR/scgpt_export.json"
export SCGPT_LABEL_LEVEL="$LEVEL"

for i in $(seq 0 $((NUM_RUNS - 1))); do
  echo "=== scGPT run $i ($LEVEL) ==="
  export SCGPT_SEED="$i"
  export SCGPT_RUN_INDEX="$i"
  export SCGPT_RESULT_CSV="$DATA_DIR/results/$LEVEL/result_$i.csv"
  python -u "$SCRIPT_DIR/pipeline/models/finetune_integration_adjusted.py"
done
