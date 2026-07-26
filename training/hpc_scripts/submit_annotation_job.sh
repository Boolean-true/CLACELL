#!/bin/bash -l

#SBATCH --job-name=annotation
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=500G
#SBATCH --time=10:00:00
#SBATCH --output=job_%j.out
#SBATCH --error=job_%j.err

unset SLURM_EXPORT_ENV

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export OMP_PLACES=cores
export OMP_PROC_BIND=true

# Regulators against Segfault
export OPENBLAS_NUM_THREADS=$SLURM_CPUS_PER_TASK
export MKL_NUM_THREADS=$SLURM_CPUS_PER_TASK
export NUMEXPR_NUM_THREADS=$SLURM_CPUS_PER_TASK

source /home/hpc/iwbn/iwbn133h/annotate_tinyfat/bin/activate

# Start Python Script
python annotate_data.py
