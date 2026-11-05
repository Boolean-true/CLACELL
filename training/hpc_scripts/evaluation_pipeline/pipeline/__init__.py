"""CLACELL evaluation pipeline package."""

__version__ = "0.4.0"

# Make the existing helper modules (test_robustness_higher_dropout.py,
# preprocess_data.py, custom_stopper.py) importable as soon as the package is
# imported.
from . import bootstrap as _bootstrap  # noqa: F401,E402
