#!/bin/bash -l

#SBATCH --job-name=clacell-tune
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=200G
#SBATCH --time=24:00:00
#SBATCH --array=0-0
#SBATCH --output=logs/%x_%A_%a.out
#SBATCH --error=logs/%x_%A_%a.err
#SBATCH --constraint=icx
#SBATCH --export=NONE
#SBATCH --requeue

set -eo pipefail
unset SLURM_EXPORT_ENV

CONFIG="${1:?usage: submit_tune.sh /absolute/path/to/experiment.yaml}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG="$(realpath "$CONFIG")"
cd "$SCRIPT_DIR"

export OMP_PLACES=cores
export OMP_PROC_BIND=true
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-16}"
export MKL_NUM_THREADS="${SLURM_CPUS_PER_TASK:-16}"
export OPENBLAS_NUM_THREADS="${SLURM_CPUS_PER_TASK:-16}"
export NUMEXPR_NUM_THREADS="${SLURM_CPUS_PER_TASK:-16}"
export VECLIB_MAXIMUM_THREADS="${SLURM_CPUS_PER_TASK:-16}"

source /apps/python/3.12-conda/etc/profile.d/conda.sh
conda activate test_clacell

echo "Host: $(hostname)"
echo "Config: $CONFIG"
echo "Array task: ${SLURM_ARRAY_TASK_ID:?}"
echo "Python: $(which python)"

python evaluation_pipeline/run_task.py tune \
  --config "$CONFIG" \
  --task-id "${SLURM_ARRAY_TASK_ID:?}"
