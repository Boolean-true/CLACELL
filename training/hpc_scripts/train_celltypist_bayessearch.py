import anndata as ad
import scanpy as sc
import celltypist
from sklearn.metrics import classification_report, accuracy_score, f1_score
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.model_selection import RandomizedSearchCV
from skopt import BayesSearchCV
from skopt.space import Real, Categorical
from custom_stopper import CustomStopper
# For saving results on HPC Cluster
import joblib
import pandas as pd
import os
from test_robustness_celltypist import test_robustness
from preprocess_data import prepare_adata
import pickle
import scipy.stats as stats
import numpy as np


# Load training data
adata = ad.read_h5ad('/home/woody/iwbn/iwbn133h/data/CellTypist_HumanCellAtlas_Merged_cleaned_refined_cell_types.h5ad')

# Preprocessing
adata = prepare_adata(adata, batch_key="Donor")

# Create train test split

# All Donors: ['621B', '637C', 'A35', 'A36', 'D496', 'D503']
donor_train = ['637C', 'A35', 'A36', 'D503', '2', '3', '4', '6']
donor_test = ['621B', 'D496', '7', '8']

adata_train = adata[
    adata.obs["Donor"].isin(donor_train)
].copy()

adata_test = adata[
    adata.obs["Donor"].isin(donor_test)
].copy()

# Check split
print(adata_train.obs['Donor'].unique())
print(adata_test.obs['Donor'].unique())

# Prepare Data for training
X_train = adata_train.X#to_df()
gene_names_train = adata_train.var_names
#y_train = adata_train.obs['scumi-annotation']
#y_train = adata_train.obs['scumi_clean']
y_train = adata_train.obs['cell_type_final']

X_test = adata_test.to_df()
gene_names_test = adata_test.var_names
#y_test = adata_test.obs['scumi-annotation']
#y_test = adata_test.obs['scumi_clean']
y_test = adata_test.obs['cell_type_final']


class CellTypistWrapper(BaseEstimator, ClassifierMixin):
    def __init__(self, C=1.0, solver='saga', use_SGD=False, alpha=0.0001,
                 use_GPU=False, mini_batch=False, batch_number=100,
                 batch_size=1000, epochs=10, balance_cell_type=False,
                 feature_selection=False, genes=None):
        # Alle Hyperparameter initialisieren
        self.C = C
        self.solver = solver
        self.use_SGD = use_SGD
        self.alpha = alpha
        self.use_GPU = use_GPU
        self.mini_batch = mini_batch
        self.batch_number = batch_number
        self.batch_size = batch_size
        self.epochs = epochs
        self.balance_cell_type = balance_cell_type
        self.feature_selection = feature_selection
        self.genes = genes

    def fit(self, X, y):
        # Scikit-Learn übergibt hier Arrays aus dem CV-Split.
        # CellTypist kommt damit klar, solange check_expression=False ist.
        self.model_ = celltypist.train(
            X=X,
            labels=y,
            C=self.C,
            solver=self.solver,
            max_iter=1000,
            n_jobs=-1,
            use_SGD=self.use_SGD,
            alpha=self.alpha,
            use_GPU=self.use_GPU,
            mini_batch=self.mini_batch,
            batch_number=self.batch_number,
            batch_size=self.batch_size,
            epochs=self.epochs,
            balance_cell_type=self.balance_cell_type,
            feature_selection=self.feature_selection,
            check_expression=False, # Muss False sein, da wir keine Gen-Namen im CV-Split übergeben
            genes=list(self.genes)
        )
        self.classes_ = np.unique(y)
        return self

    def predict(self, X):
        # Für die Accuracy-Berechnung in BayesSearchCV müssen wir Labels vorhersagen
        # Create temporary anndata object for CellTypist
        adata_tmp = ad.AnnData(X=X)
        adata_tmp.var_names = list(self.genes)

        predictions = celltypist.annotate(
                adata_tmp,
                model=self.model_
                #genes=list(self.genes)
            )
        return predictions.predicted_labels['predicted_labels'].astype(str).values#.flatten()




param_distributions_old = {
    'C': stats.loguniform(1e-3, 2.0),
    'use_SGD': [True, False],
    'alpha': stats.loguniform(1e-4, 1e-2),
    'mini_batch': [True, False],
    'balance_cell_type': [True, False],
    'feature_selection': [True, False],
}

param_distributions = [
    {
        'C': Real(1e-2, 2.0, prior='log-uniform'),
        'alpha': Real(1e-4, 1e-2, prior='log-uniform'),
        'use_SGD': Categorical([True]),
        'mini_batch': Categorical([True, False]),
        'balance_cell_type': Categorical([True, False]),
        'feature_selection': Categorical([False]),
    },
    {
        'C': Real(1e-2, 2.0, prior='log-uniform'),
        'alpha': Real(1e-4, 1e-2, prior='log-uniform'),
        'use_SGD': Categorical([True]),
        'mini_batch': Categorical([True, False]),
        'balance_cell_type': Categorical([True, False]),
        'feature_selection': Categorical([True]),
    }
]

my_stopper = CustomStopper(patience=5, min_delta=0.002, min_iter=15) 
# Suche konfigurieren
opt = BayesSearchCV(
    estimator=CellTypistWrapper(genes=gene_names_train),
    search_spaces=param_distributions,
    n_iter=30,
    cv=5,
    scoring='accuracy',
    n_jobs=1, # Wichtig: CellTypist parallelisiert selbst, n_jobs=-1 crasht oft den RAM
    verbose=10
)

opt.fit(X_train, y_train, callback=my_stopper)

print(f"\nSearch terminated after {len(opt.cv_results_['mean_test_score'])} Iterations.")
print(f"Best hyperparameters: {opt.best_params_}")
print(f"Test-Split Accuracy:  {opt.score(X_test, y_test):.4f}")

best_model = opt.best_estimator_


#model.write('celltypist_model_randomsearch.pkl')
#with open("celltypist_model_randomsearch.pkl", "wb") as f:
#    pickle.dump(model, f)

#predictions = celltypist.annotate(
#    filename=adata_test, 
#    model=model,
#    majority_voting=False
#)

y_pred = best_model.predict(X_test)

# Finale Evaluation
print("\n--- EVALUATION AUF DEN TESTDATEN ---")
print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.4f}\n")
print(f"Macro F1: {f1_score(y_test, y_pred, average='macro')}")
#print(classification_report(y_test, y_pred))


# Compute model score and robustness
with open("master_feature_importance_interleaved_marker_genes.pkl", "rb") as f:
    feature_importance = pickle.load(f)

#feature_importance = feature_importance.sort_values('Importance', ascending=False)
robustness_results = test_robustness(
    best_model,
    X_test,
    y_test,
    #"scumi-annotation",
    "scumi_clean",
    '/home/woody/iwbn/iwbn133h/data/human_immune_health_atlas/human_immune_health_atlas_full_annotated_fine_grained_cleaned.h5ad',
    feature_importance,
    log_to_console=True,
    log_to_file=False,
)

