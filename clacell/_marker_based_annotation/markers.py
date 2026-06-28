from __future__ import annotations

from collections import Counter
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.metrics import roc_auc_score

from .types import MarkerDict


@dataclass(slots=True)
class ClusterAucResult:
    auc_assign: pd.Series
    cell_type_assign: pd.Series
    auc_table: pd.DataFrame
    cell_type_score: pd.DataFrame


@dataclass(slots=True)
class AucLabelResult:
    auc: pd.Series
    label: pd.Series


def split_marker(marker: MarkerDict) -> dict[str, tuple[list[str], list[str]]]:
    out: dict[str, tuple[list[str], list[str]]] = {}
    for cell_type, genes in marker.items():
        pos: list[str] = []
        neg: list[str] = []
        for token in genes:
            if not token:
                continue
            if token.endswith("-"):
                neg.append(token[:-1])
            elif token.endswith("+"):
                pos.append(token[:-1])
            else:
                pos.append(token)
        neg_set = set(neg)
        pos = [g for g in pos if g not in neg_set]
        out[cell_type] = (pos, neg)
    return out


def compute_marker_score(
    x: pd.DataFrame, marker_list: tuple[list[str], list[str]]
) -> pd.Series:
    total = x.sum(axis=0).replace(0, np.nan)

    gene_pos = [g for g in marker_list[0] if g in x.index]
    gene_neg = [g for g in marker_list[1] if g in x.index]

    if gene_pos and gene_neg:
        out = x.loc[gene_pos].sum(axis=0) - x.loc[gene_neg].sum(axis=0)
    elif gene_pos:
        out = x.loc[gene_pos].sum(axis=0)
    elif gene_neg:
        neg_sum = x.loc[gene_neg].sum(axis=0)
        out = neg_sum.max() - neg_sum
    else:
        out = pd.Series(0.0, index=x.columns)

    res = out / total * 10000.0
    res = res.fillna(0.0)
    res[res < 0] = 0.0
    return np.log1p(res)


def score_auc(score: pd.Series, label: pd.Series) -> float:
    if label.nunique() != 2:
        return 0.5
    try:
        return float(roc_auc_score(label.astype(int), score))
    except ValueError:
        return 0.5


def assign_cluster(auc_table: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    auc_assign = pd.Series(index=auc_table.columns, dtype=float)
    cell_type_assign = pd.Series(index=auc_table.columns, dtype=object)
    for cluster in auc_table.columns:
        col = auc_table[cluster]
        best_type = str(col.idxmax())
        auc_assign.loc[cluster] = float(col.loc[best_type])
        cell_type_assign.loc[cluster] = best_type
    return auc_assign, cell_type_assign


def _cluster_to_celltype_map(auc_table: pd.DataFrame) -> dict[str, str]:
    return {
        str(cluster): str(auc_table[cluster].idxmax()) for cluster in auc_table.columns
    }


def _merge_detector(
    x: pd.DataFrame,
    cluster_name: str,
    cell_type: str,
    cluster_all: pd.Series,
    cluster_to_type: dict[str, str],
) -> float:
    if cluster_to_type[cluster_name] == cell_type:
        return 0.5

    cluster_rm = [k for k, v in cluster_to_type.items() if v == cell_type]
    keep = cluster_all.isin([cluster_name] + cluster_rm)
    cluster_keep = cluster_all[keep]
    score = x.loc[keep, cluster_to_type[cluster_name]]
    return score_auc(score, cluster_keep == cluster_name)


def _reassign_cluster(
    x: pd.DataFrame,
    cluster: pd.Series,
    auc_table: pd.DataFrame,
) -> tuple[pd.Series, pd.Series, pd.DataFrame]:
    cluster_names = list(auc_table.columns.astype(str))
    cluster_to_type = _cluster_to_celltype_map(auc_table)
    cell_type_candidates = sorted(set(cluster_to_type.values()))
    auc_table_update = auc_table.loc[cell_type_candidates, :].copy()

    for cl in cluster_names:
        if float(auc_table_update[cl].max()) > 0.9:
            continue

        scores: dict[str, float] = {}
        for ct in cell_type_candidates:
            auc_one = _merge_detector(x, cl, ct, cluster, cluster_to_type)

            current_type = cluster_to_type[cl]
            if (
                sum(v == current_type for v in cluster_to_type.values()) == 1
                and auc_one > 0.55
            ):
                continue

            cluster_rm = [k for k, v in cluster_to_type.items() if v == ct and k != cl]
            keep_mask = ~cluster.isin(cluster_rm)
            cluster_keep = cluster[keep_mask]
            cluster_score = x.loc[keep_mask, ct]
            scores[ct] = score_auc(cluster_score, cluster_keep == cl)

        for ct, val in scores.items():
            auc_table_update.loc[ct, cl] = val

    auc_assign, cell_type_assign = assign_cluster(auc_table_update)
    return auc_assign, cell_type_assign, auc_table_update


def compute_merge_cluster_auc(
    x: pd.DataFrame,
    cluster: pd.Series,
    auc: pd.Series,
    auc_table: pd.DataFrame,
    merge: bool = True,
    unassigned_threshold: float = 0.65,
) -> AucLabelResult:
    auc_curr = auc.copy()
    auc_table_curr = auc_table.copy()
    _, cell_type_curr = assign_cluster(auc_table_curr)

    if merge:
        auc_update, cell_type_update, auc_table_update = _reassign_cluster(
            x, cluster, auc_table_curr
        )
        num_iter = 1
        while not cell_type_curr.equals(cell_type_update) and num_iter <= 5:
            num_iter += 1
            auc_curr = auc_update
            cell_type_curr = cell_type_update
            auc_table_curr = auc_table_update
            auc_update, cell_type_update, auc_table_update = _reassign_cluster(
                x, cluster, auc_table_curr
            )
        auc_curr = auc_update
        cell_type_curr = cell_type_update
        auc_table_curr = auc_table_update

    cluster_names = list(auc_table_curr.columns.astype(str))
    cluster_to_type = _cluster_to_celltype_map(auc_table_curr)

    unassigned_clusters = [
        c
        for c in cluster_names
        if float(auc_table_curr[c].max()) < unassigned_threshold
    ]
    for c in unassigned_clusters:
        cluster_to_type[c] = "Unassigned"

    merged_auc: dict[str, float] = {}
    for ct in sorted(set(cluster_to_type.values())):
        if ct == "Unassigned":
            continue
        merge_clusters = [c for c, v in cluster_to_type.items() if v == ct]
        merged_auc[ct] = score_auc(x[ct], cluster.isin(merge_clusters))

    if unassigned_clusters:
        vals = [
            float(auc_curr.loc[c]) for c in unassigned_clusters if c in auc_curr.index
        ]
        if vals:
            merged_auc["Unassigned"] = float(np.mean(vals))

    label = cluster.astype(str).map(cluster_to_type)
    return AucLabelResult(auc=pd.Series(merged_auc, dtype=float), label=label)


def compute_cluster_auc(
    x: pd.DataFrame, cluster: pd.Series, marker: MarkerDict
) -> ClusterAucResult:
    marker_split = split_marker(marker)
    cell_type_score = pd.DataFrame(
        {
            cell_type: compute_marker_score(x=x, marker_list=marker_set)
            for cell_type, marker_set in marker_split.items()
        }
    )

    uniq_cluster = pd.Index(cluster.astype(str).unique())
    auc_table = pd.DataFrame(
        index=list(marker_split.keys()), columns=uniq_cluster, dtype=float
    )
    for cell_type in marker_split.keys():
        for cl in uniq_cluster:
            auc_table.loc[cell_type, cl] = score_auc(
                cell_type_score[cell_type], cluster.astype(str) == cl
            )

    auc_assign, cell_type_assign = assign_cluster(auc_table)
    return ClusterAucResult(
        auc_assign=auc_assign,
        cell_type_assign=cell_type_assign,
        auc_table=auc_table,
        cell_type_score=cell_type_score,
    )


def calculate_auc(
    umi_count: pd.DataFrame,
    cluster: pd.Series,
    marker: MarkerDict,
    merge: bool = True,
    unassigned_threshold: float = 0.65,
) -> AucLabelResult:
    res = compute_cluster_auc(umi_count, cluster.astype(str), marker)
    return compute_merge_cluster_auc(
        res.cell_type_score,
        cluster.astype(str),
        res.auc_assign,
        res.auc_table,
        merge=merge,
        unassigned_threshold=unassigned_threshold,
    )


def average_auc(auc: pd.Series) -> float:
    counts = Counter(auc.index.tolist())
    if len(auc) >= len(counts) * 2:
        return 0.0
    score = [float(auc.loc[ct]) - 0.7 for ct in counts.keys()]
    return float(np.sum(score))
