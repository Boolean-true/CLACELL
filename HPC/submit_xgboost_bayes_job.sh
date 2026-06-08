#!/bin/bash -l

#SBATCH --job-name=xgboost_bayes_search_celltype
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=200G
#SBATCH --time=17:00:00
#SBATCH --output=job_%j.out
#SBATCH --error=job_%j.err
#SBATCH --constraint=icx
#SBATCH --export=NONE

unset SLURM_EXPORT_ENV

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export OMP_PLACES=cores
export OMP_PROC_BIND=true

source /home/hpc/iwbn/iwbn133h/test_bayes/bin/activate

# Start Python Script
python train_xgboost_bayes.py
