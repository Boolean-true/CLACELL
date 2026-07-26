import os

os.environ["OPENBLAS_NUM_THREADS"] = "32"
os.environ["MKL_NUM_THREADS"] = "32"
os.environ["OMP_NUM_THREADS"] = "32"
os.environ["NUMEXPR_NUM_THREADS"] = "32"

import anndata as ad
import scanpy as sc
# For saving results on HPC Cluster
import joblib
import pandas as pd
import json
import sys

sys.path.append(os.path.abspath("python_marker_based_annotation/src"))
from python_marker_based_annotation.model_selection import select_cluster_model


# Load training data
adata = ad.read_h5ad('/home/hpc/iwbn/iwbn133h/data/CellTypistDataset/global.h5ad')

# Filter blood data
adata = adata[adata.obs['Organ'] == 'BLD'].copy()
print(adata)


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


# Extract raw data as DataFrame
#umi_df = adata.to_df(layer="counts")
umi_df = adata.to_df()
print(umi_df)


with open('scumi-dev/R/marker_gene/human_pbmc_marker.json', 'r') as file:
    marker_genes = json.load(file)

print(marker_genes)


# Run python reimplementation
result_python = select_cluster_model(umi_df.T, dict(marker_genes))

print(result_python)

adata.obs['scumi-annotation'] = result_python.label_final
print(adata)


# Save annotation
adata.write(filename=f"/home/hpc/iwbn/iwbn133h/data/CellTypistDataset/global_annotated.h5ad")
#adata.write(filename='../data/humancellatlas/5f29c29a-51c6-435c-8ff0-2b2a9d05ebee/BL_standard_design_annotated.h5ad')

# Save scumi params
with open(f'/home/hpc/iwbn/iwbn133h/data/CellTypistDataset/global_params.json', 'w') as file:
#with open(f'../data/humancellatlas/5f29c29a-51c6-435c-8ff0-2b2a9d05ebee/BL_standard_design_params.json', 'w') as file:
    file.write(json.dumps(result_python.params_final))
