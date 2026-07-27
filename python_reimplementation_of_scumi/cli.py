from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd

from .io import read_count_matrix, read_markers
from .model_selection import select_cluster_model


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Marker-based annotation pipeline")
    p.add_argument(
        "--matrix", required=True, help="Gene x cell count matrix CSV (index=gene)"
    )
    p.add_argument("--markers", required=True, help="Markers as JSON or CSV/TSV")
    p.add_argument("--outdir", required=True, help="Output directory")
    p.add_argument("--species", default="human", choices=["human", "mouse"])
    p.add_argument("--min-cluster", type=int, default=3)
    p.add_argument("--max-cluster", type=int, default=20)
    p.add_argument("--seed", type=int, default=0)
    return p


def main() -> None:
    args = _build_parser().parse_args()

    matrix = read_count_matrix(args.matrix)
    markers = read_markers(args.markers)

    result = select_cluster_model(
        matrix,
        markers,
        min_cluster=args.min_cluster,
        max_cluster=args.max_cluster,
        species=args.species,
        random_state=args.seed,
    )

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    params_file = outdir / "best_params.json"
    with params_file.open("w", encoding="utf-8") as f:
        json.dump(result.params_final, f, indent=2)

    auc_file = outdir / "final_auc.json"
    with auc_file.open("w", encoding="utf-8") as f:
        json.dump(result.auc_final, f, indent=2)

    clusters = result.model_final.clusters.rename("cluster")
    cluster_labels = pd.DataFrame({"cell": clusters.index, "cluster": clusters.values})
    cluster_labels.to_csv(outdir / "clusters.csv", index=False)

    labels = pd.DataFrame(
        {
            "cell": result.label_final.index,
            "cell_type_label": result.label_final.values,
        }
    )
    labels.to_csv(outdir / "cell_type_labels.csv", index=False)

    result.auc_table.to_csv(outdir / "model_grid_auc.csv", index=False)
    result.silhouette_table.to_csv(outdir / "model_grid_silhouette.csv", index=False)
    result.cluster_table.to_csv(outdir / "model_grid_cluster_counts.csv", index=False)

    print(f"Done. Results written to: {outdir}")


if __name__ == "__main__":
    main()
