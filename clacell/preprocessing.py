import scanpy as sc

def preprocess_data(adata):
    """
    Preprocesses the AnnData object for training and testing.
    """
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
    sc.pp.highly_variable_genes(adata, n_top_genes=10000)

    # Apply filter
    adata = adata[:, adata.var['highly_variable']].copy()

    return adata