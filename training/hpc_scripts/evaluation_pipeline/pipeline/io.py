"""Small I/O helpers: atomic writes, cache keys and success markers."""

from __future__ import annotations

import hashlib
import json
import os
import pickle
import shutil
import tempfile
from pathlib import Path
from typing import Any

import pandas as pd


def ensure_dir(path: str | os.PathLike) -> Path:
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def atomic_write_text(path: str | os.PathLike, text: str) -> None:
    path = Path(path)
    ensure_dir(path.parent)
    fd, tmp = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def atomic_write_json(path: str | os.PathLike, payload: Any) -> None:
    atomic_write_text(path, json.dumps(payload, indent=2, sort_keys=True, default=_json_default))


def _json_default(value: Any) -> Any:
    import numpy as np

    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, (np.floating,)):
        return float(value)
    if isinstance(value, np.ndarray):
        return value.tolist()
    if isinstance(value, Path):
        return str(value)
    return str(value)


def atomic_write_pickle(path: str | os.PathLike, payload: Any) -> None:
    path = Path(path)
    ensure_dir(path.parent)
    fd, tmp = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    try:
        with os.fdopen(fd, "wb") as handle:
            pickle.dump(payload, handle)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def atomic_write_csv(path: str | os.PathLike, frame: pd.DataFrame, index: bool = True) -> None:
    path = Path(path)
    ensure_dir(path.parent)
    fd, tmp = tempfile.mkstemp(prefix=f".{path.name}.", dir=str(path.parent))
    os.close(fd)
    try:
        frame.to_csv(tmp, index=index)
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def read_json(path: str | os.PathLike, default: Any = None) -> Any:
    path = Path(path)
    if not path.is_file():
        return default
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def mark_success(directory: str | os.PathLike, payload: dict | None = None) -> None:
    directory = ensure_dir(directory)
    if payload is not None:
        atomic_write_json(directory / "_SUCCESS.json", payload)
    atomic_write_text(directory / "_SUCCESS", "ok\n")


def is_success(directory: str | os.PathLike) -> bool:
    return (Path(directory) / "_SUCCESS").is_file()


def clear_success(directory: str | os.PathLike) -> None:
    for name in ("_SUCCESS", "_SUCCESS.json", "FAILED.json"):
        path = Path(directory) / name
        if path.exists():
            path.unlink()


def cache_key(payload: dict) -> str:
    encoded = json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()[:20]


def file_fingerprint(path: str | os.PathLike) -> dict:
    path = Path(path)
    stat = path.stat()
    return {
        "path": str(path.resolve()),
        "size": int(stat.st_size),
        "mtime_ns": int(stat.st_mtime_ns),
    }


def replace_dir(tmp_dir: str | os.PathLike, final_dir: str | os.PathLike) -> None:
    tmp_dir = Path(tmp_dir)
    final_dir = Path(final_dir)
    if final_dir.exists():
        shutil.rmtree(final_dir)
    os.replace(tmp_dir, final_dir)
