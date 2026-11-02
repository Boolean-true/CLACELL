#!/bin/bash -l

#SBATCH --job-name=clacell-prepare
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=200G
#SBATCH --time=24:00:00
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
#SBATCH --constraint=icx
#SBATCH --export=NONE

set -eo pipefail
unset SLURM_EXPORT_ENV

CONFIG="${1:?usage: submit_prepare.sh /absolute/path/to/experiment.yaml}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG="$(realpath "$CONFIG")"
cd "$SCRIPT_DIR"

export OMP_PLACES=cores
export OMP_PROC_BIND=true
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-32}"
export MKL_NUM_THREADS="${SLURM_CPUS_PER_TASK:-32}"
export OPENBLAS_NUM_THREADS="${SLURM_CPUS_PER_TASK:-32}"
export NUMEXPR_NUM_THREADS="${SLURM_CPUS_PER_TASK:-32}"
export VECLIB_MAXIMUM_THREADS="${SLURM_CPUS_PER_TASK:-32}"

source /apps/python/3.12-conda/etc/profile.d/conda.sh
conda activate test_clacell

echo "Host: $(hostname)"
echo "Config: $CONFIG"
echo "Python: $(which python)"
python -c "import sys; print(sys.version)"

python evaluation_pipeline/run_task.py prepare --config "$CONFIG"
