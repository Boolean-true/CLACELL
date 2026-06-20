import anndata as ad
import numpy as np
import scanpy as sc


def load_and_preprocess(path: str) -> ad.AnnData:
    adata = ad.read_h5ad(path)

    # Match the training preprocessing up to normalization.
    adata = adata[adata.obs["Organ"] == "BLD"].copy()

    adata.var["mt"] = adata.var_names.str.startswith("MT-")
    adata.var["ribo"] = adata.var_names.str.startswith(("RPS", "RPL"))
    adata.var["hb"] = adata.var_names.str.contains("^HB[^(P)]")

    sc.pp.calculate_qc_metrics(adata, qc_vars=["mt", "ribo", "hb"], inplace=True, log1p=True)

    adata = adata[:, ~adata.var["mt"]].copy()
    adata = adata[:, ~adata.var["ribo"]].copy()
    adata = adata[:, ~adata.var["hb"]].copy()

    sc.pp.scrublet(adata, batch_key="Donor")

    return adata


def compute_target_sum(adata: ad.AnnData) -> float:
    if hasattr(adata.X, "sum"):
        per_cell_totals = np.asarray(adata.X.sum(axis=1)).ravel()
    else:
        per_cell_totals = np.sum(adata.X, axis=1)

    print("min:", np.min(per_cell_totals))
    print("median:", np.median(per_cell_totals))
    print("mean:", np.mean(per_cell_totals))
    print("max:", np.max(per_cell_totals))

    return float(np.median(per_cell_totals))


def main() -> None:
    adata = load_and_preprocess("../data/CellTypistDataset/global.h5ad")
    #adata = load_and_preprocess("../data/humancellatlas/5f29c29a-51c6-435c-8ff0-2b2a9d05ebee/BL_standard_design_annotated_not_normalized.h5ad")
    target_sum = compute_target_sum(adata)

    print(f"n_cells={adata.n_obs}")
    print(f"n_genes_after_qc={adata.n_vars}")
    print(f"target_sum={target_sum:.6f}")


if __name__ == "__main__":
    main()