#!/bin/bash -l

#SBATCH --job-name=clacell-aggregate
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=200G
#SBATCH --time=01:00:00
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
#SBATCH --constraint=icx
#SBATCH --export=NONE

set -eo pipefail
unset SLURM_EXPORT_ENV

CONFIG="${1:?usage: submit_aggregate.sh /absolute/path/to/experiment.yaml}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG="$(realpath "$CONFIG")"
cd "$SCRIPT_DIR"

export OMP_PLACES=cores
export OMP_PROC_BIND=true
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-4}"
export MKL_NUM_THREADS="${SLURM_CPUS_PER_TASK:-4}"
export OPENBLAS_NUM_THREADS="${SLURM_CPUS_PER_TASK:-4}"
export NUMEXPR_NUM_THREADS="${SLURM_CPUS_PER_TASK:-4}"

source /apps/python/3.12-conda/etc/profile.d/conda.sh
conda activate test_clacell

echo "Host: $(hostname)"
echo "Config: $CONFIG"
echo "Python: $(which python)"

python evaluation_pipeline/run_task.py aggregate --config "$CONFIG"
