from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import anndata as ad
import numpy as np
import pandas as pd


MarkerDict = dict[str, list[str]]


@dataclass(slots=True)
class ClusterResult:
    adata: ad.AnnData
    clusters: pd.Series
    params: dict[str, Any]


@dataclass(slots=True)
class ModelCandidate:
    clusters: pd.Series
    auc: pd.Series
    silhouette: float
    num_clusters: int
    params: dict[str, Any]
    # store the clustering result so callers can reuse it and avoid recomputation
    model: ClusterResult | None = None
    adata: ad.AnnData | None = None


@dataclass(slots=True)
class SelectionResult:
    auc_final: dict[str, float]
    label_final: pd.Series
    params_final: dict[str, Any]
    model_final: ClusterResult
    candidates: list[ModelCandidate]
    auc_table: pd.DataFrame
    silhouette_table: pd.DataFrame
    cluster_table: pd.DataFrame


ArrayLike = np.ndarray | pd.DataFrame
