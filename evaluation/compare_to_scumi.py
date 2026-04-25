import anndata as adata
import json
import sys
import os


sys.path.append(os.path.abspath("../python_marker_based_annotation/src"))
from python_marker_based_annotation.model_selection import select_cluster_model
from scumi_wrapper import run_scumi_reference

# Read data from h5ad files
data = adata.io.read_h5ad('../blood/10x-rep1-kallisto-cellbender/10x-rep1-kallisto-cellbender.h5ad')
#TODO: use more than only this file

# Transform data
## Extract raw data as DataFrame
umi_df = data.to_df(layer="counts")

# Read marker genes
with open('../scumi-dev/R/marker_gene/human_pbmc_marker.json', 'r') as file:
    marker_genes = json.load(file)

# Run R package
#TODO: Scumi doesn't run because of required older version of Seurat
#res_scumi = run_scumi_reference(umi_df, marker_genes, '../scumi-dev/R/')
#print(res_scumi)

# Run python reimplementation
select_cluster_model(umi_df.T, marker_genes) #TODO: Use more params

# Make a scoring to evaluate them
