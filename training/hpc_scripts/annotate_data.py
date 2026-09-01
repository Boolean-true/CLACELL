import os

os.environ["OPENBLAS_NUM_THREADS"] = "32"
os.environ["MKL_NUM_THREADS"] = "32"
os.environ["OMP_NUM_THREADS"] = "32"
os.environ["NUMEXPR_NUM_THREADS"] = "32"
os.environ["VECLIB_MAXIMUM_THREADS"] = "32"

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
#adata = ad.read_h5ad('/home/hpc/iwbn/iwbn133h/data/CellTypistDataset/global.h5ad')
#adata_raw = ad.read_h5ad('/home/woody/iwbn/iwbn133h/data/CellTypistDataset/CountAdded_PIP_global_object_for_cellxgene.h5ad')
#adata_raw = ad.read_h5ad('/home/woody/iwbn/iwbn133h/data/humancellatlas/5f29c29a-51c6-435c-8ff0-2b2a9d05ebee/BL_standard_design.h5ad')
adata_preprocessed = ad.read_h5ad('/home/woody/iwbn/iwbn133h/data/human_immune_health_atlas/human_immune_health_atlas_full.h5ad', backed="r")

# 1. Base subset: First 30,000 cells
base_obs = adata_preprocessed.obs.iloc[:75000]
rest_obs = adata_preprocessed.obs.iloc[75000:]

# 2. Filter Dendritic cells (AIFI_L1) and Plasma cells (AIFI_L2) from remaining data
dc_obs = rest_obs[rest_obs['AIFI_L1'] == 'DC']
plasma_obs = rest_obs[rest_obs['AIFI_L2'] == 'Plasma cell']
bright_nk_obs = rest_obs[rest_obs['AIFI_L2'] == 'CD56bright NK cell']
dim_nk_obs = rest_obs[rest_obs['AIFI_L2'] == 'CD56dim NK cell']

# 3. Sample 1,000 cells (depending on availability)
target_n = 1000
dc_sampled = dc_obs.sample(n=min(target_n, len(dc_obs)))
plasma_sampled = plasma_obs.sample(n=min(target_n, len(plasma_obs)))
bright_nk_sampled = bright_nk_obs.sample(n=min(target_n, len(bright_nk_obs)))
dim_nk_sampled = dim_nk_obs.sample(n=min(target_n, len(dim_nk_obs)))

# 4. Combine cell IDs
selected_cell_ids = list(base_obs.index) + list(dc_sampled.index) + list(plasma_sampled.index) + list(bright_nk_sampled.index) + list(dim_nk_sampled.index)

# 5. Extract raw data for selected subset into memory
adata_subset = adata_preprocessed[selected_cell_ids]
adata_raw = adata_subset.raw.to_adata()

adata_preprocessed.file.close()


# Delete log1p stamp to remove Warnings that data might be already log1p transformed even though we use raw data
if "log1p" in adata_raw.uns:
    del adata_raw.uns["log1p"]

# Limit Anndata object
#adata = adata_raw[:50000].copy()
adata = adata_raw


# Filter blood data
#adata = adata[adata.obs['Organ'] == 'BLD'].copy()
#print(adata)


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
if "batch_id" not in adata.obs:
    print(
        "WARNUNG: 'batch_id' existiert nicht! Vorhandene Spalten:",
        adata.obs.columns.tolist(),
    )
# 1. Remove NaN values from batch_id after filtering
adata = adata[adata.obs["batch_id"].notna()].copy()

# 2. Filter empty cells and genes
sc.pp.filter_cells(adata, min_genes=1)
sc.pp.filter_genes(adata, min_cells=1)

# 3. Exclude too small batches
min_cells_per_batch = 30
batch_counts = adata.obs["batch_id"].value_counts()
valid_batches = batch_counts[batch_counts > min_cells_per_batch].index
adata = adata[adata.obs["batch_id"].isin(valid_batches)].copy()

# 3. Remove unused batch_ids
if str(adata.obs["batch_id"].dtype) == "category":
    adata.obs["batch_id"] = (
        adata.obs["batch_id"].cat.remove_unused_categories()
    )

# 4. Detect Doublets
#sc.pp.scrublet(adata, batch_key="Donor")
sc.pp.scrublet(adata, batch_key="batch_id")

# No batch_key as there are no sufficient batches
#sc.pp.scrublet(adata)



# Extract raw data as DataFrame
#umi_df = adata.to_df(layer="counts")
umi_df = adata.to_df()
print(umi_df)


#with open('scumi-dev/R/marker_gene/human_pbmc_marker.json', 'r') as file:
with open('subtype_markers_simple.json', 'r') as file:
    marker_genes = json.load(file)

print(marker_genes)

print('Start with the annotation strategy')

# Run python reimplementation
result_python = select_cluster_model(umi_df.T, dict(marker_genes))

print(result_python)

adata.obs['scumi-annotation'] = result_python.label_final
print(adata)


# Save annotation
#adata.write(filename=f"/home/hpc/iwbn/iwbn133h/data/CellTypistDataset/global_annotated.h5ad")
#adata.write(filename=f"/home/woody/iwbn/iwbn133h/data/CellTypistDataset/CountAdded_PIP_global_object_for_cellxgene_annotated_fine_grained.h5ad")
#adata.write(filename=f"/home/woody/iwbn/iwbn133h/data/humancellatlas/5f29c29a-51c6-435c-8ff0-2b2a9d05ebee/BL_standard_design_annotated_fine_grained.h5ad")
adata.write(filename=f'/home/woody/iwbn/iwbn133h/data/human_immune_health_atlas/human_immune_health_atlas_full_annotated_fine_grained_more_nk_cells.h5ad')

# Save scumi params
#with open(f'/home/woody/iwbn/iwbn133h/data/CellTypistDataset/global_params_fine_grained.json', 'w') as file:
#with open(f'/home/woody/iwbn/iwbn133h/data/humancellatlas/5f29c29a-51c6-435c-8ff0-2b2a9d05ebee/BL_standard_design_annotated_params_fine_grained.json', 'w') as file:
with open(f'/home/woody/iwbn/iwbn133h/data/human_immune_health_atlas/human_immune_health_atlas_full_params_fine_grained_more_nk_cells.json', 'w') as file:
    file.write(json.dumps(result_python.params_final))
