"""Prepare stage: shared preprocessing, split and hierarchy."""

from __future__ import annotations

import logging
import os
import resource
import time
from pathlib import Path

import anndata as ad
import numpy as np
import pandas as pd
import scanpy as sc
from scipy import sparse

# anndata >=0.11 refuses to write pandas nullable string arrays by default.
try:  # pragma: no cover - depends on anndata version
    ad.settings.allow_write_nullable_strings = True
except AttributeError:
    pass

from .config import cpu_count, load_config
from .features import feature_importance_differential_expression
from .io import (
    atomic_write_csv,
    atomic_write_json,
    atomic_write_pickle,
    cache_key,
    clear_success,
    ensure_dir,
    file_fingerprint,
    is_success,
    mark_success,
    read_json,
)
from .logging_utils import PipelineError, log_header

PREPARE_VERSION = "0.4.0"


def _peak_ram_gb() -> float:
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024)


def _safe_float(value, default: float = 0.0) -> float:
    try:
        value = float(value)
    except (TypeError, ValueError):
        return default
    return default if value != value else value  # NaN -> default


def _to_frame(adata: ad.AnnData) -> pd.DataFrame:
    matrix = adata.X.toarray() if hasattr(adata.X, "toarray") else adata.X
    return pd.DataFrame(
        np.asarray(matrix),
        index=adata.obs_names.astype(str),
        columns=adata.var_names.astype(str),
    )


def _make_h5ad_writable(adata: ad.AnnData) -> None:
    """Convert pandas nullable string columns to plain object for older anndata."""
    string_dtype = getattr(pd, "StringDtype", None)
    for frame in (adata.obs, adata.var):
        for column in frame.columns:
            dtype = frame[column].dtype
            if string_dtype is not None and isinstance(dtype, string_dtype):
                frame[column] = frame[column].astype(object)
    if string_dtype is not None and isinstance(adata.obs.index.dtype, string_dtype):
        adata.obs.index = adata.obs.index.astype(object)
    if string_dtype is not None and isinstance(adata.var.index.dtype, string_dtype):
        adata.var.index = adata.var.index.astype(object)


def _validate_dataset(dataset: dict) -> None:
    path = Path(dataset["path"])
    if not path.is_file():
        raise PipelineError(
            f"Raw dataset file not found: {path} (dataset='{dataset['name']}'). "
            "Check datasets.<name>.path in the config."
        )
    donors = dataset["donors"]
    if not donors["train"] or not donors["test"]:
        raise PipelineError(
            f"Dataset '{dataset['name']}' needs non-empty donors.train and donors.test. "
            f"Got train={donors['train']}, test={donors['test']}."
        )
    if set(donors["train"]) & set(donors["test"]):
        overlap = sorted(set(donors["train"]) & set(donors["test"]))
        raise PipelineError(
            f"Dataset '{dataset['name']}' has donors in both train and test: {overlap}"
        )
    if dataset["preprocess"].get("hvg"):
        n_top = dataset["preprocess"].get("hvg_n_top_genes")
        if n_top is not None and int(n_top) < 1:
            raise PipelineError(
                f"datasets.{dataset['name']}.preprocess.hvg_n_top_genes must be >= 1."
            )


def _align_genes(adata: ad.AnnData, genes: list[str]) -> ad.AnnData:
    """Subset to ``genes`` and add missing genes as all-zero columns."""
    missing = [gene for gene in genes if gene not in adata.var_names]
    if not missing:
        return adata[:, genes].copy()

    logging.info("Some genes are missing in the test split, filling them with zero")

    present = [gene for gene in genes if gene in adata.var_names]
    subset = adata[:, present].copy()
    if sparse.issparse(subset.X):
        zero_X = sparse.csr_matrix((subset.n_obs, len(missing)), dtype=subset.X.dtype)
    else:
        zero_X = np.zeros((subset.n_obs, len(missing)), dtype=subset.X.dtype)
    
    # Prepare layers for zero-Anndata if subset contains 'counts'
    layers_dict = {}
    if "counts" in subset.layers:
        if sparse.issparse(subset.layers["counts"]):
            layers_dict["counts"] = sparse.csr_matrix((subset.n_obs, len(missing)), dtype=subset.layers["counts"].dtype)
        else:
            layers_dict["counts"] = np.zeros((subset.n_obs, len(missing)), dtype=subset.layers["counts"].dtype)
    
    zero_adata = ad.AnnData(X=zero_X, obs=subset.obs.copy(), layers=layers_dict)
    zero_adata.var_names = missing

    combined = ad.concat([subset, zero_adata], axis=1, join="outer", merge="first")
    return combined[:, genes].copy()


def _preprocess(
    adata: ad.AnnData,
    dataset: dict,
    n_jobs: int,
    train: bool = True,
    genes: list[str] | None = None,
) -> ad.AnnData:
    """Same steps as preprocess_data.prepare_adata, with config options.

    Gene filtering and HVG selection are fit on the training split only. For
    the test split (``train=False``) the already fitted ``genes`` are applied
    in the training order; genes missing in the test split are filled with 0.
    """
    cfg = dataset["preprocess"]
    batch_key = dataset["batch_key"]

    if cfg.get("remove_mt_ribo_hb", True):
        adata.var["mt"] = adata.var_names.str.startswith("MT-").to_numpy()
        adata.var["ribo"] = adata.var_names.str.startswith(("RPS", "RPL")).to_numpy()
        adata.var["hb"] = adata.var_names.str.contains("^HB[^(P)]").to_numpy()
        sc.pp.calculate_qc_metrics(
            adata,
            qc_vars=["mt", "ribo", "hb"],
            inplace=True,
            log1p=True,
        )
    else:
        sc.pp.calculate_qc_metrics(adata, inplace=True, log1p=True)

    sc.pp.filter_cells(adata, min_counts=int(cfg.get("min_counts", 10)))
    if train:
        sc.pp.filter_genes(adata, min_cells=int(cfg.get("min_cells", 3)))

    if cfg.get("remove_mt_ribo_hb", True):
        adata = adata[:, ~adata.var["mt"]].copy()
        adata = adata[:, ~adata.var["ribo"]].copy()
        adata = adata[:, ~adata.var["hb"]].copy()

    if cfg.get("scrublet", True):
        try:
            sc.pp.scrublet(adata, batch_key=batch_key)
        except Exception as exc:  # noqa: BLE001 - add batch context
            raise PipelineError(
                f"Scrublet failed for dataset '{dataset['name']}' with batch_key='{batch_key}'. "
                f"Check that every batch has enough cells. Original error: {exc}"
            ) from exc
        if "predicted_doublet" in adata.obs:
            adata = adata[adata.obs["predicted_doublet"] == False].copy()  # noqa: E712

    adata.layers["counts"] = adata.X.copy()
    sc.pp.normalize_total(adata, target_sum=float(cfg.get("target_sum", 10000)))
    sc.pp.log1p(adata)

    if train:
        if cfg.get("hvg", True):
            n_top = cfg.get("hvg_n_top_genes")
            if n_top is None:
                sc.pp.highly_variable_genes(adata)
            else:
                sc.pp.highly_variable_genes(adata, n_top_genes=int(n_top))
            adata = adata[:, adata.var["highly_variable"]].copy()
    else:
        if genes is None:
            raise PipelineError("genes must be provided when train=False.")
        adata = _align_genes(adata, genes)

    return adata


def _build_hierarchy(
    obs_train: pd.DataFrame,
    dataset: dict,
    hierarchy_cfg: dict,
) -> dict:
    """Build coarse/fine groups from the training labels.

    The configuration is responsible for a biologically consistent hierarchy;
    the pipeline does not try to repair ambiguous fine labels.
    """
    coarse_col = dataset["labels"]["coarse"]
    fine_col = dataset["labels"].get("fine")
    train = obs_train.copy()
    train[coarse_col] = train[coarse_col].astype(str)
    if fine_col:
        train[fine_col] = train[fine_col].astype(str)

    coarse_labels = sorted(train[coarse_col].unique().tolist())
    fine_by_coarse: dict[str, list[str]] = {}
    nodes: dict[str, dict] = {}
    leaf_coarse: list[str] = []
    min_fine_classes = int(hierarchy_cfg.get("min_fine_classes", 2))

    coarse_counts = train[coarse_col].value_counts()
    nodes["coarse"] = {
        "node": "coarse",
        "coarse_label": None,
        "classes": coarse_labels,
        "n_train": int(len(train)),
        "min_train_class_count": int(coarse_counts.min()),
    }

    for coarse_label in coarse_labels:
        group = train[train[coarse_col] == coarse_label]
        fine_labels = sorted(group[fine_col].unique().tolist()) if fine_col else []
        fine_by_coarse[coarse_label] = fine_labels
        if len(fine_labels) < min_fine_classes:
            leaf_coarse.append(coarse_label)
            continue
        counts = group[fine_col].value_counts()
        nodes[f"fine:{coarse_label}"] = {
            "node": f"fine:{coarse_label}",
            "coarse_label": coarse_label,
            "classes": fine_labels,
            "n_train": int(len(group)),
            "min_train_class_count": int(counts.min()),
        }

    return {
        "coarse_labels": coarse_labels,
        "fine_by_coarse": fine_by_coarse,
        "leaf_coarse": leaf_coarse,
        "nodes": nodes,
    }


def run_prepare(config_path: str) -> None:
    config = load_config(config_path)
    dataset = config["active_dataset"]
    cache_dir = Path(config["cache_dir"])
    _validate_dataset(dataset)
    log_header("prepare", dataset=dataset["name"], cache=cache_dir)
    ensure_dir(cache_dir)

    fi_cfg = dataset["feature_importance"]
    prepare_payload = {
        "dataset": {
            key: value for key, value in dataset.items() if key != "feature_importance"
        },
        "preprocess": dataset["preprocess"],
        "hierarchy": config["experiment"]["hierarchy"],
        "feature_importance_label_level": fi_cfg.get("label_level", "fine"),
        "raw": file_fingerprint(dataset["path"]),
        "prepare_version": PREPARE_VERSION,
    }
    expected_key = cache_key(prepare_payload)
    meta_path = cache_dir / "prepare_meta.json"
    old_meta = read_json(meta_path, default={})
    if is_success(cache_dir) and old_meta.get("cache_key") == expected_key:
        logging.info("Cache hit for dataset '%s' at %s", dataset["name"], cache_dir)
        if config["experiment"].get("export_scgpt", False):
            from .models.references import export_scgpt_input, scgpt_export_path

            export_path = scgpt_export_path(config)
            if export_path.is_file():
                export_scgpt_input(config)
            else:
                # The export is part of preprocessing. If it was enabled after
                # the cache was built, charge its wall time to the cached
                # preprocessing metadata instead of silently dropping it.
                export_start = time.time()
                export_scgpt_input(config)
                export_min = (time.time() - export_start) / 60.0
                old_meta["preprocessing_time_min"] = round(
                    _safe_float(old_meta.get("preprocessing_time_min")) + export_min,
                    4,
                )
                old_meta["scgpt_export_time_min"] = round(
                    _safe_float(old_meta.get("scgpt_export_time_min")) + export_min,
                    4,
                )
                atomic_write_json(meta_path, old_meta)
                atomic_write_json(cache_dir / "_SUCCESS.json", old_meta)
                logging.info(
                    "scGPT export finished in %.2f min; updated cached preprocessing time.",
                    export_min,
                )
        return
    clear_success(cache_dir)
    for stale in cache_dir.glob(".prepared.*.h5ad"):
        stale.unlink(missing_ok=True)

    total_start = time.time()
    logging.info("Reading raw dataset: %s", dataset["path"])
    adata = ad.read_h5ad(dataset["path"])

    counts_layer = dataset.get("counts_layer")
    if counts_layer:
        if counts_layer not in adata.layers:
            raise PipelineError(
                f"datasets.{dataset['name']}.counts_layer='{counts_layer}' not found. "
                f"Available layers: {list(adata.layers.keys())}"
            )
        adata.X = adata.layers[counts_layer].copy()

    coarse_col = dataset["labels"]["coarse"]
    fine_col = dataset["labels"].get("fine")
    if coarse_col not in adata.obs:
        raise PipelineError(
            f"Coarse label column '{coarse_col}' not found for dataset '{dataset['name']}'. "
            f"Available obs columns: {list(adata.obs.columns)}"
        )
    if fine_col and fine_col not in adata.obs:
        raise PipelineError(
            f"Fine label column '{fine_col}' not found for dataset '{dataset['name']}'. "
            f"Available obs columns: {list(adata.obs.columns)}"
        )

    mask = adata.obs[coarse_col].notna()
    exclude_coarse = [str(v) for v in dataset["exclude"].get("coarse", [])]
    if exclude_coarse:
        mask &= ~adata.obs[coarse_col].astype(str).isin(exclude_coarse)
    if fine_col:
        mask &= adata.obs[fine_col].notna()
        exclude_fine = [str(v) for v in dataset["exclude"].get("fine", [])]
        if exclude_fine:
            mask &= ~adata.obs[fine_col].astype(str).isin(exclude_fine)
    n_before = adata.n_obs
    adata = adata[mask].copy()
    n_after_label_filter = adata.n_obs
    logging.info("Kept %d/%d cells after label filtering.", adata.n_obs, n_before)

    batch_key = dataset["batch_key"]
    if batch_key not in adata.obs:
        raise PipelineError(
            f"Batch key '{batch_key}' not found for dataset '{dataset['name']}'. "
            f"Available obs columns: {list(adata.obs.columns)}"
        )
    donors = dataset["donors"]
    missing_donors = sorted(
        set(donors["train"] + donors["test"]) - set(adata.obs[batch_key].astype(str).unique())
    )
    if missing_donors:
        raise PipelineError(
            f"Donors missing from dataset '{dataset['name']}' after preprocessing: {missing_donors}. "
            f"Available donors: {sorted(adata.obs[batch_key].astype(str).unique().tolist())}"
        )
    train_mask = adata.obs[batch_key].astype(str).isin(donors["train"])
    test_mask = adata.obs[batch_key].astype(str).isin(donors["test"])
    if train_mask.sum() == 0 or test_mask.sum() == 0:
        raise PipelineError(
            f"Empty train or test split for dataset '{dataset['name']}' "
            f"(train={int(train_mask.sum())}, test={int(test_mask.sum())})."
        )
    adata_train = adata[train_mask].copy()
    adata_test = adata[test_mask].copy()

    n_jobs = cpu_count(config, "prepare")
    adata_train = _preprocess(adata_train, dataset, n_jobs, train=True)
    genes = adata_train.var_names.astype(str).tolist()
    adata_test = _preprocess(adata_test, dataset, n_jobs, train=False, genes=genes)
    n_after_qc = int(adata_train.n_obs + adata_test.n_obs)
    logging.info(
        "After preprocessing: train=%d cells, test=%d cells, %d genes",
        adata_train.n_obs,
        adata_test.n_obs,
        len(genes),
    )
    if adata_train.n_obs == 0 or adata_test.n_obs == 0:
        raise PipelineError(
            f"No cells left after preprocessing for dataset '{dataset['name']}' "
            f"(train={adata_train.n_obs}, test={adata_test.n_obs}). "
            "Check min_counts/min_cells/label filters."
        )

    train_coarse = set(adata_train.obs[coarse_col].astype(str).unique())
    keep = adata_test.obs[coarse_col].astype(str).isin(train_coarse)
    unseen_coarse = sorted(set(adata_test.obs[coarse_col].astype(str).unique()) - train_coarse)
    unseen_fine = []
    if fine_col:
        train_fine = set(adata_train.obs[fine_col].astype(str).unique())
        keep &= adata_test.obs[fine_col].astype(str).isin(train_fine)
        unseen_fine = sorted(set(adata_test.obs[fine_col].astype(str).unique()) - train_fine)
    unseen_frame = pd.DataFrame(
        {
            "level": ["coarse"] * len(unseen_coarse) + ["fine"] * len(unseen_fine),
            "label": unseen_coarse + unseen_fine,
        }
    )
    if len(unseen_frame):
        logging.warning(
            "Dropping unseen test classes: coarse=%s fine=%s", unseen_coarse, unseen_fine
        )
        adata_test = adata_test[keep].copy()
    if len(adata_test) == 0:
        raise PipelineError(
            f"No test cells left for dataset '{dataset['name']}' after dropping unseen classes."
        )

    hierarchy = _build_hierarchy(
        adata_train.obs, dataset, config["experiment"]["hierarchy"]
    )
    X_train = _to_frame(adata_train)
    X_test = _to_frame(adata_test)
    if list(X_train.columns) != list(X_test.columns):
        raise PipelineError(
            "Train and test preprocessing produced different gene columns."
        )
    obs_train = adata_train.obs.copy()
    obs_test = adata_test.obs.copy()
    obs_train.index = obs_train.index.astype(str)
    obs_test.index = obs_test.index.astype(str)

    for split, split_adata in (("train", adata_train), ("test", adata_test)):
        prepared_path = cache_dir / f"prepared_{split}.h5ad"
        tmp_h5ad = cache_dir / f".prepared_{split}.{os.getpid()}.h5ad"
        _make_h5ad_writable(split_adata)
        split_adata.write_h5ad(tmp_h5ad)
        os.replace(tmp_h5ad, prepared_path)

    # npy is faster to load than h5ad for every seed/model task; the metadata
    # needed to reconstruct the DataFrame lives in genes.json and obs_*.pkl.
    np.save(cache_dir / "X_train.npy", X_train.to_numpy(copy=False))
    np.save(cache_dir / "X_test.npy", X_test.to_numpy(copy=False))
    atomic_write_json(cache_dir / "genes.json", list(X_train.columns))
    atomic_write_pickle(cache_dir / "obs_train.pkl", obs_train)
    atomic_write_pickle(cache_dir / "obs_test.pkl", obs_test)
    atomic_write_json(cache_dir / "hierarchy.json", hierarchy)
    if len(unseen_frame):
        atomic_write_csv(cache_dir / "unseen_test_classes.csv", unseen_frame, index=False)

    # Robustness ranking from differential expression on the preprocessed
    # training data only (no test labels involved).
    de_label_col = (
        coarse_col
        if fi_cfg.get("label_level", "fine") == "coarse"
        else (fine_col or coarse_col)
    )
    logging.info("Computing DE feature importance grouped by '%s'", de_label_col)
    de_genes = feature_importance_differential_expression(adata_train, de_label_col)
    atomic_write_pickle(
        cache_dir / "feature_importance_differential_expression.pkl", de_genes
    )
    logging.info("DE feature importance: %d genes", len(de_genes))

    if config["experiment"].get("export_scgpt", False):
        from .models.references import export_scgpt_input

        export_start = time.time()
        export_scgpt_input(config)
        scgpt_export_time_min = (time.time() - export_start) / 60.0
    else:
        scgpt_export_time_min = 0.0

    # The scGPT export is part of preprocessing; measure it before the total so
    # Preprocessing_Time_Min and Total_Pipeline_Time_Min include it.
    preprocessing_time_min = (time.time() - total_start) / 60.0
    meta = {
        "dataset": dataset["name"],
        "cache_key": expected_key,
        "raw_path": dataset["path"],
        "raw_fingerprint": prepare_payload["raw"],
        "n_cells_raw": int(n_before),
        "n_cells_after_label_filter": int(n_after_label_filter),
        "n_cells_after_qc": n_after_qc,
        "n_cells_train": int(len(X_train)),
        "n_cells_test": int(len(X_test)),
        "n_genes": int(X_train.shape[1]),
        "coarse_labels": hierarchy["coarse_labels"],
        "fine_label_column": fine_col,
        "preprocessing_time_min": round(preprocessing_time_min, 4),
        "scgpt_export_time_min": round(scgpt_export_time_min, 4),
        "peak_ram_gb": round(_peak_ram_gb(), 3),
        "package_versions": _package_versions(),
    }
    atomic_write_json(meta_path, meta)
    mark_success(cache_dir, meta)

    logging.info(
        "Prepare finished: train=%d test=%d genes=%d coarse=%d fine_nodes=%d in %.2f min",
        len(X_train),
        len(X_test),
        X_train.shape[1],
        len(hierarchy["coarse_labels"]),
        len([n for n in hierarchy["nodes"] if n.startswith("fine:")]),
        preprocessing_time_min,
    )


def _package_versions() -> dict[str, str]:
    import importlib.metadata

    versions = {}
    for name in ("anndata", "scanpy", "numpy", "pandas", "scikit-learn", "torch", "scipy"):
        try:
            versions[name] = importlib.metadata.version(name)
        except Exception:  # noqa: BLE001
            versions[name] = "not-installed"
    return versions
