import scanpy as sc

def prepare_adata(adata, batch_key):
    adata.var["mt"] = adata.var_names.str.startswith(("MT-")).to_numpy()
    adata.var["ribo"] = adata.var_names.str.startswith(("RPS", "RPL")).to_numpy()
    adata.var["hb"] = adata.var_names.str.contains("^HB[^(P)]").to_numpy()

    # QC-Metrics
    sc.pp.calculate_qc_metrics(adata, qc_vars=["mt", "ribo", "hb"], inplace=True, log1p=True)
    sc.pp.filter_cells(adata, min_counts=10)
    sc.pp.filter_genes(adata, min_cells=3)

    # Remove mitochondrial, ribosomal and hemoglobin
    adata = adata[:, ~adata.var["mt"]].copy()
    adata = adata[:, ~adata.var["ribo"]].copy()
    adata = adata[:, ~adata.var["hb"]].copy()
    
    # Doublet Detection
    sc.pp.scrublet(adata, batch_key=batch_key)
    adata = adata[adata.obs['predicted_doublet'] == False].copy()
    
    # Saving count data
    adata.layers["counts"] = adata.X.copy()

    # Normalization
    sc.pp.normalize_total(adata, target_sum=1e4)
    sc.pp.log1p(adata)

    # HVGs
    sc.pp.highly_variable_genes(adata)
    adata = adata[:, adata.var['highly_variable']].copy()

    return adata
