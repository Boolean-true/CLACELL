import argparse
import logging
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
import yaml
from scipy.optimize import root_scalar
from scipy.sparse import csr_matrix, issparse
from scipy.stats import nbinom, poisson

LOGGER = logging.getLogger(__name__)

CONFIG_PATH = Path(__file__).resolve().parent / "datasets.yaml"
OUTPUT_SUFFIX = "_spatial.h5ad"

# anndata >= 0.11 refuses to write pandas nullable string arrays by default.
try:
    ad.settings.allow_write_nullable_strings = True
except AttributeError:
    pass


def adjust_anndata_to_spatial(
    adata: ad.AnnData,
    spatial_ref_df: pd.DataFrame,
    weighted_dropout: bool = True,
    drop_missing_genes: bool = True,
    rng: np.random.Generator | None = None,
) -> ad.AnnData:
    """Passt ein AnnData-Objekt an Spatial-Referenz-Statistiken an.

    - Filtert Gene, die nicht in der TSV-Tabelle enthalten sind.
    - Berechnet den Dispersionsparameter theta mathematisch aus der Detection
      Rate.
    - Nutzt Zero-Truncated Sampling (Werte >= 1), um Mittelwert-Verzerrungen
      zu vermeiden.
    """
    if rng is None:
        rng = np.random.default_rng()

    adata_adj = adata.copy()
    ref = spatial_ref_df.set_index("gene")

    genes_adata = set(adata.var_names)
    genes_spatial = set(spatial_ref_df["gene"])
    common_genes = genes_adata.intersection(genes_spatial)
    LOGGER.info(
        "Genes: AnnData=%d, spatial=%d, common=%d, coverage=%.2f%%",
        len(genes_adata),
        len(genes_spatial),
        len(common_genes),
        len(common_genes) / len(genes_adata) * 100 if genes_adata else 0.0,
    )

    # Filter genes that are not in the reference tsv
    if drop_missing_genes:
        genes_to_keep = [g for g in adata_adj.var_names if g in ref.index]
        adata_adj = adata_adj[:, genes_to_keep].copy()

    # Convert sparse matrix to dense array
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

        # Special case: gene is not detected in spatial -> set it to 0
        if target_det_rate <= 0 or n_spots_detected <= 0 or total_counts <= 0:
            X[:, col_idx] = 0.0
            continue

        # STEP 1: adjust the occurrence count (detection rate) of all genes to the spatial reference data
        target_non_zero_count = int(round(target_det_rate * n_cells))
        current_non_zero_idx = np.where(gene_counts > 0)[0]

        if len(current_non_zero_idx) > target_non_zero_count:
            n_to_zero = len(current_non_zero_idx) - target_non_zero_count

            if weighted_dropout:
                # Set low counts with higher probability to 0
                vals = gene_counts[current_non_zero_idx]
                weights = 1.0 / (vals + 1e-6)
                probs = weights / np.sum(weights)
                zero_idx = rng.choice(
                    current_non_zero_idx, size=n_to_zero, replace=False, p=probs
                )
            else:
                # Random dropout
                zero_idx = rng.choice(
                    current_non_zero_idx, size=n_to_zero, replace=False
                )

            gene_counts[zero_idx] = 0.0

        # STEP 2: adjust the reads of all genes to match the spatial reference data
        remaining_non_zero_idx = np.where(gene_counts > 0)[0]
        n_remaining = len(remaining_non_zero_idx)

        if n_remaining > 0:
            mu_all = (total_counts * target_det_rate) / n_spots_detected
            p0 = 1.0 - target_det_rate

            if p0 > np.exp(-mu_all) and p0 < 1.0:

                def f(log_theta):
                    t = np.exp(log_theta)
                    return t * np.log(t / (mu_all + t)) - np.log(p0)

                try:
                    theta = np.exp(
                        root_scalar(f, bracket=[-15, 15], method="brentq").root
                    )
                    p_param = theta / (mu_all + theta)
                    u = rng.uniform(p0, 1.0, size=n_remaining)
                    new_counts = nbinom.ppf(u, n=theta, p=p_param)
                except Exception:
                    u = rng.uniform(np.exp(-mu_all), 1.0, size=n_remaining)
                    new_counts = poisson.ppf(u, mu=mu_all)
            else:
                u = rng.uniform(max(1e-10, np.exp(-mu_all)), 1.0, size=n_remaining)
                new_counts = poisson.ppf(u, mu=mu_all)

            gene_counts[remaining_non_zero_idx] = np.maximum(1, new_counts)

        X[:, col_idx] = gene_counts

    adata_adj.X = csr_matrix(X)
    return adata_adj


def downsample(
    input_path: str | Path | None,
    dataset: str,
    output_path: str | Path | None = None,
    seed: int = 0,
    config_path: str | Path = CONFIG_PATH,
) -> ad.AnnData:
    """Downsample the input using the dataset settings from datasets.yaml."""
    with Path(config_path).open("r", encoding="utf-8") as handle:
        dataset_config = yaml.safe_load(handle)["datasets"][dataset]

    from_prepared = input_path is None and dataset_config.get("downsample_from") == "prepare"
    if from_prepared:
        input_path = Path(dataset_config["outputs"]["prepare"])
        adata = ad.read_h5ad(input_path)
    else:
        input_path = Path(input_path or dataset_config["input"])
        counts = dataset_config.get("counts") or "x"
        adata = ad.read_h5ad(input_path)
        if counts == "raw":
            adata = adata.raw.to_adata()
        elif counts.startswith("layer:"):
            adata.X = adata.layers[counts.split(":", 1)[1]].copy()

        symbol_column = dataset_config.get("symbol_column")
        if symbol_column:
            backup_column = dataset_config.get("backup_column") or "original_varnames"
            adata.var[backup_column] = adata.var_names
            adata.var_names = adata.var[symbol_column]
            adata.var.index.name = None
            adata.var_names_make_unique()

    stats_path = (
        dataset_config.get("spatial_stats")
        or input_path.parent / "nucleus_gene_stats.tsv"
    )
    LOGGER.info("Downsampling %s using %s", input_path, stats_path)
    spatial_ref = pd.read_csv(stats_path, sep="\t")

    adata_spatial = adjust_anndata_to_spatial(
        adata=adata,
        spatial_ref_df=spatial_ref,
        weighted_dropout=False,
        drop_missing_genes=True,
        rng=np.random.default_rng(seed),
    )

    output_path = output_path or dataset_config.get("outputs", {}).get("downsample")
    if output_path is None:
        output_path = input_path.with_name(input_path.stem + OUTPUT_SUFFIX)
    output_path = Path(output_path)
    LOGGER.info("Dimensions: %s -> %s", adata.shape, adata_spatial.shape)
    adata_spatial.write_h5ad(output_path)
    LOGGER.info("Wrote %s", output_path)
    return adata_spatial


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-d", "--dataset", required=True, help="Dataset key from datasets.yaml")
    parser.add_argument("-i", "--input", type=Path, help="Input .h5ad file (default: config)")
    parser.add_argument("-o", "--output", type=Path, help="Output .h5ad file (default: config)")
    parser.add_argument("--seed", type=int, default=0, help="Random seed")
    parser.add_argument("-c", "--config", type=Path, default=CONFIG_PATH, help="Config file")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )
    downsample(args.input, args.dataset, args.output, args.seed, args.config)


if __name__ == "__main__":
    main()
