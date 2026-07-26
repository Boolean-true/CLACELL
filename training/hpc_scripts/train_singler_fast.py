import anndata as ad
import scanpy as sc
# For saving results on HPC Cluster
import joblib
import pandas as pd
import os
from sklearn.metrics import classification_report, accuracy_score, f1_score
from test_robustness import test_robustness
import pickle
import singler
import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.validation import check_is_fitted


# Load training data
adata = ad.read_h5ad('/home/hpc/iwbn/iwbn133h/data/CellTypistDataset/CountAdded_PIP_global_object_for_cellxgene_annotated.h5ad')

# Filter blood data
adata = adata[adata.obs['Organ'] == 'BLD'].copy()
print(adata)

# Use raw data instead of already preprocessed data
adata.X = adata.layers['counts'].copy()


# Preprocessing

# mitochondrial genes, "MT-" for human, "Mt-" for mouse
adata.var["mt"] = adata.var_names.str.startswith("MT-")
# ribosomal genes
adata.var["ribo"] = adata.var_names.str.startswith(("RPS", "RPL"))
# hemoglobin genes
adata.var["hb"] = adata.var_names.str.contains("^HB[^(P)]")

sc.pp.calculate_qc_metrics(adata, qc_vars=["mt", "ribo", "hb"], inplace=True, log1p=True)

# Remove mitochondrial, ribosomal and hemoglobin
adata = adata[:, ~adata.var["mt"]].copy()
adata = adata[:, ~adata.var["ribo"]].copy()
adata = adata[:, ~adata.var["hb"]].copy()

# Doublet Detection
sc.pp.scrublet(adata, batch_key="Donor")
adata = adata[adata.obs['predicted_doublet'] == False].copy()


# Normalization

# Saving count data
adata.layers["counts"] = adata.X.copy()

# Normalizing to median total counts
sc.pp.normalize_total(adata, target_sum=1e4)
# Logarithmize the data
sc.pp.log1p(adata)

# Filtering Highly variable genes
print('Before filtering highly variable genes ---')
print(adata)

sc.pp.highly_variable_genes(adata, n_top_genes=10000)

# Apply filter
adata = adata[:, adata.var['highly_variable']].copy()

print('After filtering highly variable genes ---')
print(adata)

# Create train test split

# All Donors: ['621B', '637C', 'A35', 'A36', 'D496', 'D503']
donor_train = ['637C', 'A35', 'A36', 'D503']
donor_test = ['621B', 'D496']

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
X_train = adata_train.to_df()
gene_names_train = adata_train.var_names
y_train = adata_train.obs['scumi-annotation']

X_test = adata_test.to_df()
gene_names_test = adata_test.var_names
y_test = adata_test.obs['scumi-annotation']


# Model training

class SingleRClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self):
        """
        Ein scikit-learn kompatibler Wrapper für die Python-Implementierung von SingleR.
        Optimal geeignet für Pipelines, Kreuzvalidierungen und Robustheitstests.
        """
        self.reference_ = None
        self.features_ = None
        self.classes_ = None

    def fit(self, X, y):
        """
        Trainiert den SingleR-Referenzindex.

        Parameters:
            X (pd.DataFrame): Trainingsdaten im Format (Zellen x Gene).
            y (array-like): Zelltyp-Labels für das Training.
        """
        if not isinstance(X, pd.DataFrame):
            raise TypeError("X muss ein pandas DataFrame sein, um Gen-Namen (Spalten) zu extrahieren.")

        # Features (Gene) und eindeutige Klassen speichern
        self.features_ = X.columns.tolist()
        self.classes_ = np.unique(y)

        # SingleR erwartet (Gene x Zellen) -> Transponieren
        X_transposed = X.values.T

        # Referenzindex bauen
        self.reference_ = singler.train_single(
            ref_data=X_transposed,
            ref_labels=list(y),
            ref_features=self.features_,
            test_features=self.features_  # Setzt voraus, dass Test-Features aligned werden
        )

        return self

    def predict(self, X):
        """
        Sagt die Zelltypen für das übergebene Testset voraus.

        Parameters:
            X (pd.DataFrame): Testdaten im Format (Zellen x Gene).
        Returns:
            np.ndarray: Array mit den vorhergesagten Labels.
        """
        # Überprüfen, ob fit() aufgerufen wurde
        if self.features_ is None:
            raise RuntimeError(
                "The model wasn't trained yet. Call 'train' or 'grid_search' first.")

        if not isinstance(X, pd.DataFrame):
            raise TypeError("X muss ein pandas DataFrame sein.")

        # ROBUSTHEITS-SCHUTZ: Spalten an das Trainingsset angleichen.
        # Fehlende Gene werden mit 0 aufgefüllt, zusätzliche Gene ignoriert.
        X_aligned = X.reindex(columns=self.features_, fill_value=0)

        # SingleR erwartet (Gene x Zellen) -> Transponieren
        X_transposed = X_aligned.values.T

        # Klassifikation durchführen
        output = singler.classify_single(X_transposed, ref_prebuilt=self.reference_)

        # Ergebnisse als klassisches numpy-Array zurückgeben
        return np.array(output["best"])


class FastSingleRClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, aggregate_ref=True):
        """
        Ein optimierter, scikit-learn kompatibler Wrapper für SingleR.

        Parameters:
            aggregate_ref (bool): Wenn True (empfohlen), werden die Referenzzellen
                                  pro Zelltyp gemittelt. Verhindert tagelange Laufzeiten.
        """
        self.aggregate_ref = aggregate_ref
        self.reference_ = None
        self.features_ = None
        self.classes_ = None

    def fit(self, X, y):
        if not isinstance(X, pd.DataFrame):
            raise TypeError("X muss ein pandas DataFrame sein, um Gen-Namen (Spalten) zu behalten.")

        self.features_ = X.columns.tolist()
        self.classes_ = np.unique(y)

        # --- DER SPEED-BOOST ---
        if self.aggregate_ref:
            # Berechne den Mittelwert (Pseudo-Bulk) pro Zelltyp.
            # Reduziert z.B. 50.000 Zeilen auf die Anzahl deiner eindeutigen Zelltypen.
            print(# Spezifischer Hinweis für den User
                f"Aggregiere Referenz-Matrix von {X.shape[0]} Zellen "
                f"auf {len(self.classes_)} Zelltyp-Profile..."
            )
            X_fit = X.groupby(y).mean()
            y_fit = X_fit.index.tolist()
        else:
            X_fit = X
            y_fit = y

        # SingleR erwartet (Gene x Zellen)
        X_transposed = X_fit.values.T

        # Referenzindex bauen
        self.reference_ = singler.train_single(
            ref_data=X_transposed,
            ref_labels=list(y_fit),
            ref_features=self.features_,
            test_features=self.features_
        )
        return self

    def predict(self, X):
        check_is_fitted(self, attributes=["reference_", "features_"])
        if not isinstance(X, pd.DataFrame):
            raise TypeError("X muss ein pandas DataFrame sein.")

        # Spalten-Layout absichern
        X_aligned = X.reindex(columns=self.features_, fill_value=0)
        X_transposed = X_aligned.values.T

        # Klassifikation
        output = singler.classify_single(X_transposed, ref_prebuilt=self.reference_)
        return np.array(output["best"])


best_model = FastSingleRClassifier()

# 2. Trainieren (X_train muss ein DataFrame sein)
best_model.fit(X_train, y_train)

# 3. Vorhersage auf dem Testset (X_test muss ein DataFrame sein)
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
    "scumi-annotation",
    'data/humancellatlas/5f29c29a-51c6-435c-8ff0-2b2a9d05ebee/BL_standard_design_annotated.h5ad',
    feature_importance,
    log_to_console=True,
    log_to_file=False,
)

