from typing import Any, Mapping, Sequence #TODO: old standard

import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.conversion import localconverter
from rpy2.robjects.vectors import BoolVector, FloatVector, IntVector, ListVector, StrVector
from rpy2.robjects.packages import importr

# Sets the path to the users R library
custom_libs = "~/R/library"
robjects.r(f'.libPaths(c(path.expand("{custom_libs}"), .libPaths()))')
s
rocr = importr('ROCR')
#seurat = importr('Seurat')
dplyr = importr('dplyr')

def _to_r_marker_list(marker_genes: Mapping[str, Sequence[str]]) -> ListVector:
    if not marker_genes:
        raise ValueError("marker_genes is empty")

    r_marker_data = {}
    for cell_type, markers in marker_genes.items():
        if not isinstance(cell_type, str):
            raise TypeError("Each marker key must be a string")
        if not isinstance(markers, Sequence):
            raise TypeError(f"Markers for '{cell_type}' must be a sequence of strings")
        r_marker_data[cell_type] = StrVector([str(gene) for gene in markers])

    return ListVector(r_marker_data)


def run_scumi_reference(umi_count, marker_genes, r_dir):
    # 1. Load R files
    robjects.r.source(f"{r_dir}/model_selection.R")
    robjects.r.source(f"{r_dir}/sc_compare_util.R")
    robjects.r.source(f"{r_dir}/assign_cluster.R")

    # 2. Extract the function
    SelectClusterModel = robjects.globalenv['SelectClusterModel']
    
    # 3. Call the function
    with localconverter(robjects.default_converter + pandas2ri.converter):
        r_umi_count = robjects.conversion.py2rpy(umi_count)
    
    r_marker_genes = _to_r_marker_list(marker_genes) #TODO: Or I load the markers from the Rdata file
    return SelectClusterModel(r_umi_count, r_marker_genes)