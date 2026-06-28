from __future__ import annotations

from itertools import product
import concurrent.futures
import os

import numpy as np
import pandas as pd
from scipy.spatial.distance import pdist, squareform
from sklearn.metrics import silhouette_samples

from .clustering import cluster_scanpy
from .markers import average_auc, calculate_auc
from .types import MarkerDict, ModelCandidate, SelectionResult


def _filter_matrix(
    umi_count: pd.DataFrame, min_cells: int, min_genes: int
) -> pd.DataFrame:
    gene_mask = (umi_count > 0).sum(axis=1) >= min_cells
    cell_mask = (umi_count > 0).sum(axis=0) >= min_genes
    return umi_count.loc[gene_mask, cell_mask]


def _marker_genes_from_marker(marker: MarkerDict) -> list[str]:
    genes: set[str] = set()
    for entries in marker.values():
        for g in entries:
            if g.endswith("+") or g.endswith("-"):
                genes.add(g[:-1])
            else:
                genes.add(g)
    return sorted(genes)


def _prepare_distance(
    umi_count: pd.DataFrame, marker: MarkerDict, normalize: bool
) -> pd.DataFrame:
    x = umi_count.astype(float)
    if normalize:
        col_sum = x.sum(axis=0).replace(0, np.nan)
        x = x.divide(col_sum, axis=1) * 10000.0
        x = np.log1p(x).fillna(0.0)
    else:
        x = np.log1p(x)

    genes = [g for g in _marker_genes_from_marker(marker) if g in x.index]
    if not genes:
        raise ValueError("No marker genes found in input matrix")

    print(len(genes), "marker genes found in input matrix")

    data = x.loc[genes].T.values
    d2 = squareform(pdist(data, metric="euclidean") ** 2)
    return pd.DataFrame(d2, index=x.columns, columns=x.columns)


def _mean_silhouette(labels: pd.Series, distance: pd.DataFrame) -> float:
    if labels.nunique() < 2:
        return -1.0
    idx = labels.index
    d = distance.loc[idx, idx].values
    s = silhouette_samples(d, labels.values, metric="precomputed")
    return float(np.mean(s))


def _score_signal(auc: pd.Series) -> float:
    if len(auc) == 0:
        return 0.0
    return float(float(auc.sum()) - 0.5 * len(auc))


def select_cluster_model(
    umi_count: pd.DataFrame,
    marker: MarkerDict,
    number_neighbor: tuple[int, ...] = (15, 30),
    resolution: tuple[float, ...] = (0.8, 1.0, 1.2, 1.5),
    num_pc: tuple[int, ...] = (20, 30, 50, 100),
    variable_gene: tuple[bool, ...] = (True, False),
    min_cluster: int = 3,
    max_cluster: int = 20,
    normalize: bool = True,
    min_cells: int = 3,
    min_genes: int = 1,
    species: str = "human",
    random_state: int = 0,
) -> SelectionResult:
    filtered = _filter_matrix(umi_count, min_cells=min_cells, min_genes=min_genes)
    distance = _prepare_distance(filtered, marker=marker, normalize=normalize)

    # prepare parameter grid
    param_list = [
        {"variable_gene": vg, "k": k, "resolution": r, "n_pc": n_pc}
        for vg, k, r, n_pc in product(variable_gene, number_neighbor, resolution, num_pc)
    ]

    def _eval_candidate(p: dict) -> ModelCandidate:
        # run clustering and scoring for one parameter combination
        model = cluster_scanpy(
            filtered,
            number_neighbor=p["k"],
            variable_gene=p["variable_gene"],
            resolution=p["resolution"],
            num_pc=p["n_pc"],
            species=species,
            normalize=normalize,
            min_cells=min_cells,
            min_genes=min_genes,
            random_state=random_state,
        )
        clusters = model.clusters.astype(str)
        cluster_count = clusters.value_counts()
        n_cluster = int(cluster_count.shape[0])

        sil = -1.0
        auc = pd.Series(dtype=float)
        if min_cluster <= n_cluster <= max_cluster:
            sil = _mean_silhouette(clusters, distance)

            min_cell_in_cluster = max(3, int(np.ceil(p["k"] / 5.0)))
            keep_clusters = set(cluster_count[cluster_count >= min_cell_in_cluster].index)
            keep_cells = clusters[clusters.isin(keep_clusters)].index

            auc_out = calculate_auc(filtered.loc[:, keep_cells], clusters.loc[keep_cells], marker)
            auc = auc_out.auc

        return ModelCandidate(
            clusters=clusters,
            auc=auc,
            silhouette=sil,
            num_clusters=n_cluster,
            params={
                "number_neighbor": p["k"],
                "variable_gene": p["variable_gene"],
                "resolution": p["resolution"],
                "num_pc": p["n_pc"],
            },
            model=model,
        )

    # choose reasonable number of workers
    max_workers = min(32, (os.cpu_count() or 1))
    candidates: list[ModelCandidate]
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = [ex.submit(_eval_candidate, p) for p in param_list]
        candidates = [f.result() for f in concurrent.futures.as_completed(futures)]

    valid_idx = [
        i
        for i, c in enumerate(candidates)
        if min_cluster <= c.num_clusters <= max_cluster
    ]
    if not valid_idx:
        valid_idx = list(range(len(candidates)))

    model_sil_idx = max(valid_idx, key=lambda i: candidates[i].silhouette)
    model_auc_idx = max(valid_idx, key=lambda i: average_auc(candidates[i].auc))

    auc_sil = calculate_auc(filtered, candidates[model_sil_idx].clusters, marker).auc
    auc_auc = calculate_auc(filtered, candidates[model_auc_idx].clusters, marker).auc

    final_idx = model_auc_idx
    if _score_signal(auc_sil) > _score_signal(auc_auc):
        final_idx = model_sil_idx

    final_params = candidates[final_idx].params
    # reuse the computed model if available to avoid recomputation
    final_model = None
    for c in candidates:
        if c.params == final_params and getattr(c, "model", None) is not None:
            final_model = c.model
            break
    if final_model is None:
        final_model = cluster_scanpy(
            filtered,
            number_neighbor=final_params["number_neighbor"],
            variable_gene=final_params["variable_gene"],
            resolution=final_params["resolution"],
            num_pc=final_params["num_pc"],
            species=species,
            normalize=normalize,
            min_cells=min_cells,
            min_genes=min_genes,
            random_state=random_state,
        )
    final_auc_result = calculate_auc(filtered, final_model.clusters, marker)
    auc_final = final_auc_result.auc
    label_final = final_auc_result.label

    auc_table = pd.DataFrame(
        [
            {
                **c.params,
                "avg_auc": average_auc(c.auc),
                "auc_signal": _score_signal(c.auc),
            }
            for c in candidates
        ]
    )
    silhouette_table = pd.DataFrame(
        [{**c.params, "silhouette": c.silhouette} for c in candidates]
    )
    cluster_table = pd.DataFrame(
        [{**c.params, "num_clusters": c.num_clusters} for c in candidates]
    )

    return SelectionResult(
        auc_final=auc_final,
        label_final=label_final,
        params_final=final_params,
        model_final=final_model,
        candidates=candidates,
        auc_table=auc_table,
        silhouette_table=silhouette_table,
        cluster_table=cluster_table,
    )
