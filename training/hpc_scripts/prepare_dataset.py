import argparse
import logging
from pathlib import Path

import anndata as ad
import numpy as np
import yaml

LOGGER = logging.getLogger(__name__)

CONFIG_PATH = Path(__file__).resolve().parent / "datasets.yaml"
OUTPUT_SUFFIX = "_fine_and_coarse_annotated.h5ad"
COARSE_COLUMN = "scumi_clean_coarse"
FINE_COLUMN = "scumi_clean_fine_grained"
FALLBACK_LABEL = "Unknown"

# anndata >= 0.11 refuses to write pandas nullable string arrays by default.
try:
    ad.settings.allow_write_nullable_strings = True
except AttributeError:
    pass


def prepare(
    input_path: str | Path | None,
    dataset: str,
    output_path: str | Path | None = None,
    config_path: str | Path = CONFIG_PATH,
) -> ad.AnnData:
    """Prepare the input using the dataset settings from datasets.yaml."""
    with Path(config_path).open("r", encoding="utf-8") as handle:
        dataset_config = yaml.safe_load(handle)["datasets"][dataset]

    input_path = Path(input_path or dataset_config["input"])
    counts = dataset_config.get("counts") or "x"
    adata = ad.read_h5ad(input_path)

    # Use raw counts according to the config
    if counts == "raw":
        adata = adata.raw.to_adata()
    elif counts.startswith("layer:"):
        adata.X = adata.layers[counts.split(":", 1)[1]].copy()

    # Make sure to use gene names and not ensembl ids
    symbol_column = dataset_config.get("symbol_column")
    if symbol_column:
        backup_column = dataset_config.get("backup_column") or "original_varnames"
        adata.var[backup_column] = adata.var_names
        adata.var_names = adata.var[symbol_column]
        adata.var.index.name = None
        adata.var_names_make_unique()

    label_column = dataset_config.get("label_column")
    if not label_column:
        raise ValueError(f"Dataset '{dataset}' has no label_column in datasets.yaml")

    mapping = dataset_config.get("mapping")
    if mapping is None:
        LOGGER.info(
            "Dataset '%s' has no mapping in datasets.yaml; writing '%s' as the "
            "fine label '%s' (no coarse label).",
            dataset,
            label_column,
            FINE_COLUMN,
        )
        adata.obs[FINE_COLUMN] = adata.obs[label_column]
    else:
        coarse, fine, unmapped = [], [], set()
        for label in adata.obs[label_column].astype(str):
            entry = mapping.get(label)
            if entry is None:
                unmapped.add(label)
                entry = (FALLBACK_LABEL, FALLBACK_LABEL)
            coarse.append(entry[0])
            fine.append(entry[1])

        adata.obs[COARSE_COLUMN] = coarse
        adata.obs[FINE_COLUMN] = fine
        if unmapped:
            LOGGER.warning("Labels not in the mapping: %s", sorted(unmapped))

    totals = np.asarray(adata.X.sum(axis=1)).ravel()
    LOGGER.info(
        "Per-cell counts: min=%.1f median=%.1f mean=%.1f max=%.1f",
        np.min(totals),
        np.median(totals),
        np.mean(totals),
        np.max(totals),
    )
    if COARSE_COLUMN in adata.obs:
        coarse_counts = adata.obs[COARSE_COLUMN].value_counts()
        LOGGER.info("Coarse labels (%d):\n%s", len(coarse_counts), coarse_counts.to_string())
    if FINE_COLUMN in adata.obs:
        fine_counts = adata.obs[FINE_COLUMN].value_counts()
        LOGGER.info("Fine labels (%d):\n%s", len(fine_counts), fine_counts.to_string())

    output_path = output_path or dataset_config.get("outputs", {}).get("prepare")
    if output_path is None:
        output_path = input_path.with_name(input_path.stem + OUTPUT_SUFFIX)
    output_path = Path(output_path)
    adata.write_h5ad(output_path)
    LOGGER.info("Wrote %s", output_path)
    return adata


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-d", "--dataset", required=True, help="Dataset key from datasets.yaml")
    parser.add_argument("-i", "--input", type=Path, help="Input .h5ad file (default: config)")
    parser.add_argument("-o", "--output", type=Path, help="Output .h5ad file (default: config)")
    parser.add_argument("-c", "--config", type=Path, default=CONFIG_PATH, help="Config file")
    args = parser.parse_args(argv)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )
    prepare(args.input, args.dataset, args.output, args.config)


if __name__ == "__main__":
    main()
