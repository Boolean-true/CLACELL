#!/bin/bash -l

#SBATCH --job-name=run_multiple_scgpt
#SBATCH --gres=gpu:a100:1
#SBATCH --partition=a100
#SBATCH --time=24:00:00
#SBATCH --output=job_%j.out
#SBATCH --error=job_%j.err
#SBATCH --export=NONE

unset SLURM_EXPORT_ENV


#source /home/hpc/iwbn/iwbn133h/gpu/bin/activate
source /apps/python/3.12-conda/etc/profile.d/conda.sh

conda activate scgpt_env

# Start Python Script
python -u run_multiple_trainings_scgpt.py
