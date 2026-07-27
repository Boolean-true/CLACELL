import anndata as ad
import scanpy as sc
# For saving results on HPC Cluster
import joblib
import pandas as pd
import os
from sklearn.metrics import classification_report, accuracy_score, f1_score
from test_robustness import test_robustness
import pickle
import numpy as np
import scvi
from typing import Union


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
#sc.pp.normalize_total(adata, target_sum=1e4)
# Logarithmize the data
#sc.pp.log1p(adata)

# Filtering Highly variable genes
print('Before filtering highly variable genes ---')
print(adata)

sc.pp.highly_variable_genes(adata, n_top_genes=10000, flavor="seurat_v3")

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


class SCANVIDataFrameWrapper:
    def __init__(self, n_latent: int = 30, n_layers: int = 2,
                 max_epochs_scvi: int = 200, max_epochs_scanvi: int = 20):
        """
        Wrapper für scANVI, der direkt mit Pandas DataFrames interagiert.
        """
        self.n_latent = n_latent
        self.n_layers = n_layers
        self.max_epochs_scvi = max_epochs_scvi
        self.max_epochs_scanvi = max_epochs_scanvi

        # Interne Modell- und Feature-Speicher
        self.scvi_model = None
        self.scanvi_model = None
        self.var_names = None  # Speichert die Gen-IDs aus dem Training
        self.cell_type_categories = None

    def fit(self, X_train: pd.DataFrame, y_train: Union[pd.Series, np.ndarray]):
        """
        Trainiert scVI und scANVI ausschließlich auf den Trainingsdaten.

        Parameters:
        -----------
        X_train: pd.DataFrame, Shape (Zellen, Gene) mit Roh-Counts
        y_train: Array-like, True Labels der Trainingszellen
        """
        # 1. Gen-Metadaten für Konsistenzprüfung sichern
        self.var_names = X_train.columns.tolist()

        # 2. Internes AnnData für das Training bauen
        adata_train = ad.AnnData(X=X_train.values.copy())
        adata_train.var_names = self.var_names
        adata_train.obs_names = X_train.index.astype(str)

        # 3. Kategorien vorbereiten (inkl. der "Unknown"-Maske für scANVI)
        self.cell_type_categories = list(set(y_train)) + ["Unknown"]
        adata_train.obs["cell_type"] = pd.Series(
            y_train,
            index=adata_train.obs_names,
            dtype=pd.CategoricalDtype(categories=self.cell_type_categories)
        )

        # 4. scvi-tools Daten-Setup
        scvi.model.SCVI.setup_anndata(adata_train, labels_key="cell_type")

        # 5. scVI Basis-Modell trainieren
        print("Starte Basis-Training (scVI)...")
        self.scvi_model = scvi.model.SCVI(
            adata_train,
            n_latent=self.n_latent,
            n_layers=self.n_layers
        )
        self.scvi_model.train(accelerator="cpu", max_epochs=self.max_epochs_scvi)

        # 6. scANVI Modell ableiten und finetunen
        print("Starte semi-überwachtes Tuning (scANVI)...")
        self.scanvi_model = scvi.model.SCANVI.from_scvi_model(
            self.scvi_model,
            unlabeled_category="Unknown",
        )
        self.scanvi_model.train(accelerator="cpu", max_epochs=self.max_epochs_scanvi)

        print("Training erfolgreich abgeschlossen.")
        return self

    def predict(self, X_test: pd.DataFrame) -> pd.Series:
        """
        Sagt Zelltypen für ein reines Hold-Out-DataFrame voraus,
        ohne das Modell zu verändern.

        Parameters:
        -----------
        X_test: pd.DataFrame, Shape (Zellen, Gene)

        Returns:
        --------
        pd.Series mit den Vorhersagen und dem originalen Test-Index
        """
        if self.scanvi_model is None:
            raise ValueError("Das Modell wurde noch nicht trainiert. Rufe zuerst .fit() auf.")

        # 1. Feature-Abgleich: Stimmen die Gene überein?
        if list(X_test.columns) != self.var_names:
            print("Hinweis: Test-Spalten weichen ab. Versuche automatische Anpassung an Trainings-Gene...")
            try:
                # Richtige Spalten herausfiltern und in die exakte Reihenfolge bringen
                X_test = X_test[self.var_names]
            except KeyError:
                raise KeyError(
                    "Das Testset enthält nicht alle Gene, auf denen das Modell trainiert wurde!"
                )

        # 2. Internes AnnData für das Testset bauen
        adata_test = ad.AnnData(X=X_test.values.copy())
        adata_test.var_names = self.var_names
        adata_test.obs_names = X_test.index.astype(str)
        adata_test.obs["cell_type"] = "Unknown"

        # 3. Out-of-Sample Vorhersage über das neuronale Netz
        predictions = self.scanvi_model.predict(adata=adata_test)

        # 4. Rückgabe als saubere Pandas Series mit den originalen Cell-IDs als Index
        return pd.Series(predictions, index=X_test.index, name="predicted_cell_type")



best_model = SCANVIDataFrameWrapper(
    n_latent=30, 
    n_layers=2, 
    max_epochs_scvi=150, 
    max_epochs_scanvi=15
)

best_model.fit(X_train, y_train)

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

