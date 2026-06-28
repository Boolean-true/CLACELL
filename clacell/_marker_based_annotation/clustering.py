from __future__ import annotations

import anndata as ad
import numpy as np
import pandas as pd
import scanpy as sc

from .types import ClusterResult


def _to_anndata(umi_count: pd.DataFrame) -> ad.AnnData:
    if not isinstance(umi_count, pd.DataFrame):
        raise TypeError(
            "umi_count must be a pandas DataFrame with genes as index and cells as columns"
        )
    adata = ad.AnnData(X=umi_count.T.copy())
    adata.var_names = umi_count.index.astype(str)
    adata.obs_names = umi_count.columns.astype(str)
    return adata


def cluster_scanpy(
    umi_count: pd.DataFrame,
    number_neighbor: int = 30,
    variable_gene: bool = False,
    resolution: float = 1.0,
    num_pc: int = 50,
    species: str = "human",
    normalize: bool = True,
    min_cells: int = 3,
    min_genes: int = 1,
    random_state: int = 0,
) -> ClusterResult:
    adata = _to_anndata(umi_count)

    sc.pp.filter_cells(adata, min_genes=min_genes)
    sc.pp.filter_genes(adata, min_cells=min_cells)

    if species == "human":
        adata.var["mito"] = adata.var_names.str.startswith("MT-")
    elif species == "mouse":
        adata.var["mito"] = adata.var_names.str.startswith("mt-")
    else:
        raise ValueError("species must be 'human' or 'mouse'")

    sc.pp.calculate_qc_metrics(
        adata, qc_vars=["mito"], percent_top=None, log1p=False, inplace=True
    )

    if normalize:
        sc.pp.normalize_total(adata, target_sum=10000)
        sc.pp.log1p(adata)
    else:
        adata.X = np.log1p(adata.X)

    if variable_gene:
        sc.pp.highly_variable_genes(adata, min_mean=0.0125, max_mean=3, min_disp=0.5)
        hvg_mask = adata.var["highly_variable"].to_numpy()
        if int(hvg_mask.sum()) == 0:
            adata_use = adata.copy()
        else:
            adata_use = adata[:, hvg_mask].copy()
    else:
        if species == "human":
            mt_rb = adata.var_names.str.contains(
                r"^MT-|^RPL|^RPS|^MRPS|^MRPL", regex=True
            )
        else:
            mt_rb = adata.var_names.str.contains(
                r"^mt-|^Rpl|^Rps|^Mrps|^Mrpl", regex=True
            )
        adata_use = adata[:, ~mt_rb].copy()

    if adata_use.n_vars == 0:
        adata_use = adata.copy()

    sc.pp.scale(adata_use)

    n_pc_eff = min(num_pc, adata_use.n_vars - 1, adata_use.n_obs - 1)
    n_pc_eff = max(n_pc_eff, 2)

    sc.tl.pca(
        adata_use,
        n_comps=n_pc_eff,
        random_state=random_state,
        mask_var=None,
    )
    sc.pp.neighbors(
        adata_use,
        n_neighbors=number_neighbor,
        n_pcs=n_pc_eff,
        random_state=random_state,
    )
    sc.tl.leiden(
        adata_use,
        resolution=resolution,
        random_state=random_state,
        key_added="cluster",
        flavor="igraph",
        n_iterations=2,
        directed=False,
    )
    sc.tl.tsne(adata_use, n_pcs=n_pc_eff, random_state=random_state)

    adata.obsm["X_pca"] = adata_use.obsm["X_pca"]
    adata.obsm["X_tsne"] = adata_use.obsm["X_tsne"]
    adata.obs["cluster"] = adata_use.obs["cluster"].astype(str)

    params = {
        "number_neighbor": number_neighbor,
        "variable_gene": variable_gene,
        "resolution": resolution,
        "num_pc": num_pc,
        "normalize": normalize,
        "min_cells": min_cells,
        "min_genes": min_genes,
        "species": species,
    }
    return ClusterResult(
        adata=adata, clusters=adata.obs["cluster"].copy(), params=params
    )
