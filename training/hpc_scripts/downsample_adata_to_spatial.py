import importlib
import sys
import pandas as pd
import resource
import time
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.ensemble import VotingClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.calibration import CalibratedClassifierCV
import anndata as ad
import scanpy as sc
# For saving results on HPC Cluster
import joblib
import pandas as pd
import os
from sklearn.metrics import classification_report, accuracy_score, f1_score
#from test_robustness import test_robustness
from test_robustness_higher_dropout import test_robustness
from preprocess_data import prepare_adata
from skopt import BayesSearchCV
from skopt.space import Integer, Real, Categorical
from custom_stopper import CustomStopper
from scipy.sparse import csr_matrix
import time
from scipy.optimize import root_scalar
from scipy.sparse import issparse
from scipy.stats import nbinom, poisson


# Load training data
adata = ad.read_h5ad('/home/woody/iwbn/iwbn133h/data/10x-gex/ovarian/f8f7f2b0-b8a5-4087-8048-8d3f5b6a49dd.h5ad')

# Use raw counts
adata = adata.raw.to_adata()

# Use gene names instead of ensemble ids
symbol_col = 'feature_name'

# Alt-Namen als Backup in var speichern
adata.var['ensembl_id'] = adata.var_names
print('saved backup of ensembl ids')
# Gen-Namen auf Symbole umstellen
adata.var_names = adata.var[symbol_col]
print('use gene names')
# Namenskonflikt verhindern (Index-Namen entfernen)
adata.var.index.name = None
# Duplikate behandeln (z.B. Gene_1, Gene_2 anhängen)
adata.var_names_make_unique()
print('make gene names unique')
# Preprocessing
#adata = prepare_adata(adata, batch_key="donor_id")


# Downsample data similar to spatial data
def adjust_anndata_to_spatial(
    adata: ad.AnnData,
    spatial_ref_df: pd.DataFrame,
    weighted_dropout: bool = True,
    drop_missing_genes: bool = True,
) -> ad.AnnData:
    """Passt ein AnnData-Objekt an Spatial-Referenz-Statistiken an.

    - Filtert Gene, die nicht in der TSV-Tabelle enthalten sind.
    - Berechnet den Dispersionsparameter theta mathematisch aus der Detection
    Rate.
    - Nutzt Zero-Truncated Sampling (Werte >= 1), um Mittelwert-Verzerrungen
    zu vermeiden.
    """
    adata_adj = adata.copy()
    ref = spatial_ref_df.set_index("gene")

    print('start with overbiew')
    genes_adata = set(adata.var_names)
    genes_spatial = set(spatial_ref_df['gene'])
    common_genes = genes_adata.intersection(genes_spatial)
    only_in_adata = genes_adata - genes_spatial
    only_in_spatial = genes_spatial - genes_adata

    # 3. Übersicht ausgeben
    print(f"Gene in AnnData:              {len(genes_adata)}")
    print(f"Gene in Spatial Ref Table:    {len(genes_spatial)}")
    print(f"----------------------------------------")
    print(f"Gemeinsame Gene:              {len(common_genes)}")
    print(f"Nur in AnnData:               {len(only_in_adata)}")
    print(f"Nur in Spatial Ref Table:     {len(only_in_spatial)}")
    print(f"----------------------------------------")
    print(f"Abdeckung (AnnData -> Spatial): {len(common_genes) / len(genes_adata) * 100:.2f}%")

    # Gene filtern, die nicht in der Referenz-TSV stehen
    if drop_missing_genes:
        genes_to_keep = [g for g in adata_adj.var_names if g in ref.index]
        adata_adj = adata_adj[:, genes_to_keep].copy()

    # Sparse-Matrix gegebenenfalls in Dense-Array für Umwandlung umwandeln
    if issparse(adata_adj.X):
        X = adata_adj.X.toarray().astype(float)
    else:
        X = adata_adj.X.copy().astype(float)

    n_cells = X.shape[0]

    for col_idx, gene in enumerate(adata_adj.var_names):
        target_det_rate = ref.loc[gene, "detection_rate"]
        total_counts = ref.loc[gene, "total_counts"]
        n_spots_detected = ref.loc[gene, "n_spots_detected"]

        gene_counts = X[:, col_idx]

        # Sonderfall: Gen in Spatial gar nicht detektiert
        if (
            target_det_rate <= 0
            or n_spots_detected <= 0
            or total_counts <= 0
        ):
            X[:, col_idx] = 0.0
            continue

        # --- STUFE 1: Detection Rate anpassen (Dropout / Zero-Inflation) ---
        target_non_zero_count = int(round(target_det_rate * n_cells))
        current_non_zero_idx = np.where(gene_counts > 0)[0]
        current_non_zero_count = len(current_non_zero_idx)

        if current_non_zero_count > target_non_zero_count:
            n_to_zero = current_non_zero_count - target_non_zero_count

            if weighted_dropout:
                # Niedrige Werte droppen mit höherer Wahrscheinlichkeit auf 0
                vals = gene_counts[current_non_zero_idx]
                weights = 1.0 / (vals + 1e-6)
                probs = weights / np.sum(weights)
                zero_idx = np.random.choice(
                    current_non_zero_idx, size=n_to_zero, replace=False, p=probs
                )
            else:
                # Rein zufälliges Dropout
                zero_idx = np.random.choice(
                    current_non_zero_idx, size=n_to_zero, replace=False
                )

            gene_counts[zero_idx] = 0.0

        # Verbliebene Indizes mit Werten > 0
        remaining_non_zero_idx = np.where(gene_counts > 0)[0]
        n_remaining = len(remaining_non_zero_idx)

        # --- STUFE 2: Reads anpassen (Zero-Truncated Sampling) ---
        if n_remaining > 0:
            # Mittlere Reads pro Spot über den gesamten Datensatz
            mu_all = (total_counts * target_det_rate) / n_spots_detected
            p0 = 1.0 - target_det_rate

            # Überdispersion prüfen (p0 > exp(-mu_all) für Negativ-Binomial)
            if p0 > np.exp(-mu_all) and p0 < 1.0:
                # Nullstellen-Suche zur Bestimmung von theta
                def f(log_theta):
                    t = np.exp(log_theta)
                    return t * np.log(t / (mu_all + t)) - np.log(p0)

                try:
                    res = root_scalar(f, bracket=[-15, 15], method="brentq")
                    theta = np.exp(res.root)
                    n_param = theta
                    p_param = theta / (mu_all + theta)
                    
                    # Zero-Truncated NB Sampling: Ziehe Uniform auf [p0, 1.0]
                    # nbinom.ppf(u) liefert dadurch garantiert nur Werte >= 1
                    u = np.random.uniform(p0, 1.0, size=n_remaining)
                    new_counts = nbinom.ppf(u, n=n_param, p=p_param)
                except Exception:
                    # Fallback auf Poisson, falls Wurzel-Findung fehlschlägt
                    p0_poiss = np.exp(-mu_all)
                    u = np.random.uniform(p0_poiss, 1.0, size=n_remaining)
                    new_counts = poisson.ppf(u, mu=mu_all)
            else:
                # Zero-Truncated Poisson Sampling
                p0_poiss = max(1e-10, np.exp(-mu_all))
                u = np.random.uniform(p0_poiss, 1.0, size=n_remaining)
                new_counts = poisson.ppf(u, mu=mu_all)

            # Sicherheitsnetz gegen Rundungsfehler bei Extremwerten
            new_counts = np.maximum(1, new_counts)
            gene_counts[remaining_non_zero_idx] = new_counts

        X[:, col_idx] = gene_counts

    # Matrix vor dem Speichern wieder in eine Sparse-Matrix umwandeln
    adata_adj.X = csr_matrix(X)
    return adata_adj


# 1. TSV laden
df_spatial = pd.read_csv("/home/woody/iwbn/iwbn133h/data/10x-gex/ovarian/nucleus_gene_stats.tsv", sep="\t")
print('loaded tsv')
# 3. Transformation ausführen
adata_spatial = adjust_anndata_to_spatial(
    adata=adata,
    spatial_ref_df=df_spatial,
    weighted_dropout=False,
    drop_missing_genes=True,
)

print(f"Ursprüngliche Dimensionen: {adata.shape}")
print(f"Angepasste Dimensionen:    {adata_spatial.shape}")


adata_spatial.write(filename=f'/home/woody/iwbn/iwbn133h/data/10x-gex/ovarian/f8f7f2b0-b8a5-4087-8048-8d3f5b6a49dd_spatial.h5ad')
