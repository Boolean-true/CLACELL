from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from .types import MarkerDict


def read_count_matrix(path: str | Path) -> pd.DataFrame:
    matrix = pd.read_csv(path, index_col=0)
    return matrix


def read_markers(path: str | Path) -> MarkerDict:
    p = Path(path)
    if p.suffix.lower() == ".json":
        with p.open("r", encoding="utf-8") as f:
            obj = json.load(f)
        return {str(k): [str(x) for x in v] for k, v in obj.items()}

    if p.suffix.lower() in {".csv", ".tsv"}:
        sep = "\t" if p.suffix.lower() == ".tsv" else ","
        df = pd.read_csv(p, sep=sep)
        required = {"cell_type", "marker"}
        if not required.issubset(set(df.columns)):
            raise ValueError("Marker table must contain columns: cell_type, marker")
        out: MarkerDict = {}
        for ct, grp in df.groupby("cell_type"):
            out[str(ct)] = [str(x) for x in grp["marker"].tolist()]
        return out

    raise ValueError("Unsupported marker format. Use .json, .csv, or .tsv")
