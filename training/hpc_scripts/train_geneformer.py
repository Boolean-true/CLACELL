import anndata as ad
import scanpy as sc
from sklearn.linear_model import LogisticRegression
# For saving results on HPC Cluster
import joblib
import pandas as pd
import os
from sklearn.metrics import classification_report, accuracy_score, f1_score
from test_robustness import test_robustness
import pickle
import numpy as np
from geneformer import Classifier
from geneformer import TranscriptomeTokenizer
import tempfile
import torch
from transformers import BertForSequenceClassification
from datasets import load_from_disk
from gprofiler import GProfiler
import json
import glob

os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"


# =====================================================================
# PANDAS 2.0+ COMPATIBILITY PATCH FOR GENEFORMER
# =====================================================================
# Stellt das alte Pandas 1.x Verhalten für Series-Indexing wieder her,
# damit Geneformers interne Positions-Abfragen nicht crashen.
_old_getitem = pd.Series.__getitem__

def _patched_getitem(self, key):
    try:
        return _old_getitem(self, key)
    except KeyError as e:
        # Wenn der Index kein Integer-Index ist, die Abfrage aber aus Zahlen besteht -> Nutze .iloc
        if isinstance(key, (pd.Index, np.ndarray, list)):
            if hasattr(key, 'dtype') and key.dtype.kind in 'iu':
                return self.iloc[key]
            elif isinstance(key, list) and len(key) > 0 and isinstance(key[0], (int, np.integer)):
                return self.iloc[key]
        raise e

pd.Series.__getitem__ = _patched_getitem
# =====================================================================


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


# Convert genes to Ensembl-IDs
gp = GProfiler(return_dataframe=True)

# 2. Alle Gen-Symbole aus deinen Spalten extrahieren
gene_symbols = X_train.columns.tolist()

print(f"Start Conversion for {len(gene_symbols)} Genes...")

# 3. Lade Mapping-Tabelle
mapping_file = "gene_symbol_to_ensembl.json"
with open(mapping_file, "r") as f:
    symbol_to_ensembl = json.load(f)

# 5. DataFrame filtern und Spalten umbenennen
# Wir behalten nur die Spalten, für die wir eine Ensembl-ID gefunden haben
valid_cols = [col for col in X_train.columns if str(col).startswith("ENSG") or col in symbol_to_ensembl]
train_data_mapped = X_train[valid_cols].copy()
test_data_mapped = X_test[valid_cols].copy()

# Spaltennamen durch die ENSG-IDs ersetzen
train_data_mapped.columns = [
        symbol_to_ensembl[col] for col in train_data_mapped.columns
]
test_data_mapped.columns = [
        symbol_to_ensembl[col] for col in test_data_mapped.columns
]

# Remove duplicate Ensembl IDs
if train_data_mapped.columns.duplicated().any():
    print("Achtung: Duplizierte Ensembl-IDs gefunden! Werden zusammengeführt...")
    # Transponieren, nach Ensembl-ID gruppieren (summiert die Expressionswerte) und zurücktransponieren
    train_data_mapped = train_data_mapped.T.groupby(level=0).sum().T
    print(f"Finale Spaltenanzahl nach Duplikat-Bereinigung: {train_data_mapped.shape[1]}")

if test_data_mapped.columns.duplicated().any():
    print("Achtung: Duplizierte Ensembl-IDs gefunden! Werden zusammengeführt...")
    # Transponieren, nach Ensembl-ID gruppieren (summiert die Expressionswerte) und zurücktransponieren
    test_data_mapped = test_data_mapped.T.groupby(level=0).sum().T
    print(f"Finale Spaltenanzahl nach Duplikat-Bereinigung: {test_data_mapped.shape[1]}")

X_train = train_data_mapped.copy()
X_test = test_data_mapped.copy()
print("Finished Conversion")

# Model training
# 1. Lade deinen Trainings-DataFrame (Beispielstruktur: Zeilen = Zellen, Spalten = Gene)
# Stelle sicher, dass die Spaltennamen bereits Ensembl-IDs sind!
#df_train = pd.read_csv("path/to/your_train_df.csv", index_col=0) 

# 2. Erstelle das AnnData-Objekt (X MUSS rohe Counts enthalten)
adata = ad.AnnData(X=X_train.values)
adata.obs_names = X_train.index.tolist() #astype(str)
#adata.var_names = X_train.columns.astype(str)

# 3. Geneformers Pflicht-Attribute hinzufügen
adata.var["ensembl_id"] = X_train.columns.tolist() #adata.var_names # Spalte 'ensembl_id' im .var-Verzeichnis
adata.obs["cell_type"] = y_train.values     # Deine Zielvariable
adata.obs["n_counts"] = adata.X.sum(axis=1) # Gesamte Counts pro Zelle


os.makedirs("h5ad_train_dir", exist_ok=True)
adata.write_h5ad("h5ad_train_dir/blood_cells_train.h5ad")
print("AnnData erfolgreich für Geneformer vorbereitet.")


# Initialisiere den Tokenizer.
# nproc definiert die CPU-Kerne für die Parallelisierung auf dem HPC.
tk = TranscriptomeTokenizer({"cell_type": "cell_type"}, nproc=8)

# Tokenisierung starten
tk.tokenize_data(
    data_directory="h5ad_train_dir",       # Eingabe-Ordner mit der .h5ad
    output_directory="tokenized_train_dir", # Ausgabe-Ordner
    output_prefix="blood_cells",
    file_format="h5ad"
)
print("Tokenisierung abgeschlossen.")



# HPC-Optimierung: Verhindert Logging-Spam von Weights & Biases falls nicht genutzt
os.environ["WANDB_DISABLED"] = "true"

# Definiere die Trainings-Hyperparameter
training_args = {
    "learning_rate": 5e-5,
    "do_train": True,
    "output_dir": "./geneformer_checkpoints",
    "per_device_train_batch_size": 4, # Passe dies an deinen GPU-Speicher an (z.B. 12 oder 16 für 40GB A100)
    "num_train_epochs": 3,              # 3-5 Epochen reichen meist für Cell-Type-Classification
    "weight_decay": 0.01,
    "warmup_steps": 500,
    "logging_steps": 10,
    "save_strategy": "epoch",           # Speichert am Ende jeder Epoche einen Checkpoint
    "fp16": True,                       # Aktiviert Mixed-Precision (beschleunigt das Training auf GPUs)
}

# Classifier-Instanz erstellen
cc = Classifier(
    classifier="cell",
    cell_state_dict={"state_key": "cell_type", "states": "all"},
    training_args=training_args,
    #max_input_size=4096,   # 2048 für Geneformer V1, 4096 falls du die neuere V2 nutzt
    freeze_layers=0,       # 0 = Alle Layer werden gefinetuned
    num_crossval_splits=1,  # Wichtig: Verhindert internes Splitting, nutzt 100% der Daten zum Trainieren
    forward_batch_size=4
)

os.makedirs("classifier_input_dir", exist_ok=True)

# Bereitet die Labels vor und mappt sie zu Integern
cc.prepare_data(
    input_data_file="tokenized_train_dir/blood_cells.dataset",
    output_directory="classifier_input_dir",
    output_prefix="blood_cells_labeled"
)

print("Tatsächlicher Inhalt von classifier_input_dir:", os.listdir("classifier_input_dir"))
# Starte das eigentliche Fine-Tuning
# Ersetze "ctheodoris/Geneformer" durch den lokalen Pfad, falls du das Modell vorab auf den HPC geladen hast.
cc.validate(
    model_directory="Geneformer",
    prepared_input_data_file="classifier_input_dir/blood_cells_labeled_labeled_test.dataset",
    id_class_dict_file="classifier_input_dir/blood_cells_labeled_id_class_dict.pkl",
    output_directory="classifier_output_dir",
    output_prefix="blood_cells_eval"
)

print("Finished Fine tuning")



class GeneformerPredictor:
    def __init__(self, model_directory, id_class_dict_path, batch_size=12, max_input_size=4096, nproc=16):
        """
        Minimaler Wrapper rein für die Inference auf trainierten Geneformer-Modellen.

        Parameters:
        - model_directory: Pfad zum spezifischen Checkpoint-Ordner (z.B. './geneformer_checkpoints/checkpoint-500')
        - id_class_dict_path: Pfad zur pkl-Datei aus dem Training (z.B. '..._id_class_dict.pkl')
        """
        self.model_directory = model_directory
        self.batch_size = batch_size
        self.max_input_size = max_input_size
        self.nproc = nproc

        # Label-Mapping direkt laden
        with open(id_class_dict_path, "rb") as f:
            self.id_class_dict = pickle.load(f)

    def predict(self, X):
        """Sagt die Zelltypen für einen DataFrame (Zellen x Ensembl-IDs) voraus."""
        device = "cuda" if torch.cuda.is_available() else "cpu"

        # 1. Modell laden
        model = BertForSequenceClassification.from_pretrained(self.model_directory).to(device)
        model.eval()

        # 2. Temporäre Tokenisierung auf der Festplatte
        with tempfile.TemporaryDirectory() as tmpdir:
            h5ad_dir = os.path.join(tmpdir, "h5ad")
            tokenized_dir = os.path.join(tmpdir, "tokenized")
            os.makedirs(h5ad_dir, exist_ok=True)

            # Minimales AnnData-Objekt mit Dummy-Labels erstellen
            adata = ad.AnnData(X=X.values)
            adata.obs_names = X.index.tolist() #astype(str)
            adata.var_names = X.columns.tolist() #astype(str)
            adata.var["ensembl_id"] = adata.var_names
            adata.obs["cell_type"] = ["unknown"] * len(X) # Dummy
            adata.obs["n_counts"] = adata.X.sum(axis=1)
            adata.write_h5ad(os.path.join(h5ad_dir, "input.h5ad"))

            # Tokenizer ausführen
            tk = TranscriptomeTokenizer({"cell_type": "cell_type"}, nproc=self.nproc)
            tk.tokenize_data(h5ad_dir, tokenized_dir, "data", file_format="h5ad")

            dataset = load_from_disk(os.path.join(tokenized_dir, "data.dataset"))
            all_preds = []

            # 3. Inference-Schleife mit dynamischem Batch-Padding
            with torch.no_grad():
                for i in range(0, len(dataset), self.batch_size):
                    batch = dataset[i : i + self.batch_size]
                    input_ids_list = batch["input_ids"]

                    max_len = max(len(x) for x in input_ids_list)
                    padded_input_ids = [x + [0] * (max_len - len(x)) for x in input_ids_list]
                    input_ids_tensor = torch.tensor(padded_input_ids).to(device)

                    attention_mask = [[1] * len(x) + [0] * (max_len - len(x)) for x in input_ids_list]
                    attention_mask_tensor = torch.tensor(attention_mask).to(device)

                    outputs = model(input_ids=input_ids_tensor, attention_mask=attention_mask_tensor)

                    # Logits direkt zu Klassen-IDs konvertieren
                    preds = torch.argmax(outputs.logits, dim=-1).cpu().numpy()
                    all_preds.extend(preds)

        # 4. Numerische IDs zurück zu den echten Zelltyp-Strings mappen
        return np.array([self.id_class_dict[p] for p in all_preds])


id_class_dict_speicherort = "classifier_input_dir/blood_cells_labeled_id_class_dict.pkl"

# Sucht automatisch nach dem neuesten Checkpoint-Ordner da drin
checkpoint_pattern = os.path.join("classifier_output_dir", "**", "checkpoint-*")
checkpoints = glob.glob(checkpoint_pattern, recursive=True)
if not checkpoints:
    print("Tatsächlicher Inhalt von classifier_output_dir:", os.listdir("classifier_output_dir"))
    raise FileNotFoundError("Kein Checkpoint-Ordner in classifier_output_dir gefunden!")

# Nimmt den neuesten/höchsten Checkpoint
tatsaechlicher_model_pfad = max(checkpoints, key=os.path.getctime)
#tatsaechlicher_model_pfad = max(checkpoints, key=os.path.getpath if hasattr(os, 'getpath') else os.path.getctime)
print(f"Lade trainiertes Modell aus: {tatsaechlicher_model_pfad}")

best_model = GeneformerPredictor(
    model_directory=tatsaechlicher_model_pfad,
    id_class_dict_path=id_class_dict_speicherort,
    batch_size=16
)
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
    '/home/hpc/iwbn/iwbn133h/data/humancellatlas/5f29c29a-51c6-435c-8ff0-2b2a9d05ebee/BL_standard_design_annotated.h5ad',
    feature_importance,
    log_to_console=True,
    log_to_file=False,
)
