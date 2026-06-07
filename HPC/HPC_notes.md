# HPC notes

## Setting up python environment

### Install packages with Spack

spack install python@3.10
spack install py-pandas
spack install py-joblib
spack install py-scikit-learn

### Active Spack environment (then python is activated)

eval `spack load --sh python@3.10 py-pandas py-joblib py-scikit-learn`

### Initialize python environment

Create new directory test_bayes (don't move files into it)

python -m venv --system-site-packages test_bayes

source test_bayes/bin/activate
(now an interactive shell with pip opens)

### Install packages with pip

pip install --no-cache-dir --ignore-installed anndata scanpy scrublet scikit-learn scikit-optimize joblib pandas pytz python-dateutil


## Copying data to HPC

### Upload folder

scp -r /home/boolean/Documents/Uni/Semester_2/Project_CLACELL/data/ csnhr.nhr.fau.de:data

### For the second command the directories already have to be created on the HPC Cluster
scp -r /home/boolean/Documents/Uni/Semester_2/Project_CLACELL/data/CellTypistDataset/ csnhr.nhr.fau.de:/home/hpc/iwbn/iwbn133h/data

### Upload single file
scp -r /home/boolean/Documents/Uni/Semester_2/Project_CLACELL/training/custom_stopper.py  csnhr.nhr.fau.de:custom_stopper.py



## Batch Jobs

Submitted batch job 11828366
Submitted batch job 11828908
Submitted batch job 11829010
Submitted batch job 11829046
Submitted batch job 11829068
Submitted batch job 11835882

### Final Jobs
LogisitcRegression: Submitted batch job 11839954
RandomForest: Submitted batch job 11839951
XGBoost: Submitted batch job 11841014