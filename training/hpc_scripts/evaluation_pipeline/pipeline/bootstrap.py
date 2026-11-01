"""Make the existing CLACELL helper modules importable.

The user copies ``evaluation_pipeline`` as a sub-directory of ``hpc_scripts``.
The canonical ``test_robustness_higher_dropout.py``, ``preprocess_data.py`` and
``custom_stopper.py`` therefore live one or two directories above this package.
This module adds those directories to ``sys.path`` without touching the files.
"""

from __future__ import annotations

import sys
from pathlib import Path


def bootstrap() -> list[Path]:
    here = Path(__file__).resolve()
    candidates = [
        here.parents[2],  # hpc_scripts/
        here.parents[3],  # training/ (custom_stopper.py)
        Path.cwd(),       # current Slurm working directory
    ]
    added: list[Path] = []
    for candidate in candidates:
        if candidate.is_dir() and str(candidate) not in sys.path:
            sys.path.insert(0, str(candidate))
            added.append(candidate)
    return added


bootstrap()
