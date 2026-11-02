"""Denoising autoencoder with a scikit-learn classifier head (CPU only)."""

from __future__ import annotations

import random
import time
from typing import Any

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from scipy.stats import loguniform, randint
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from torch.utils.data import DataLoader, TensorDataset

from ..logging_utils import PipelineError
from .base import ModelAdapter


def set_torch_seed(seed: int, n_jobs: int = 1) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.set_num_threads(max(1, int(n_jobs)))
    torch.use_deterministic_algorithms(False)


class DenoisingAutoencoder(nn.Module):
    def __init__(self, input_dim: int, latent_dim: int = 128, noise_factor: float = 0.3):
        super().__init__()
        self.noise_factor = noise_factor
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(256, latent_dim),
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(256, input_dim),
        )

    def forward(self, x):
        if self.training:
            x_noisy = x + torch.randn_like(x) * self.noise_factor
        else:
            x_noisy = x
        latent = self.encoder(x_noisy)
        reconstructed = self.decoder(latent)
        return reconstructed, latent


class ScRNADAEClassifier(ModelAdapter):
    def __init__(self, dae, classifier, scaler=None):
        self.dae = dae
        self.classifier = classifier
        self.scaler = scaler
        # DAE permanent in den Evaluationsmodus versetzen (schaltet Rauschen ab)
        self.dae.eval()
        # Erkennen, ob das Modell auf CPU oder GPU liegt
        self.device = next(dae.parameters()).device
        self.epochs_ = None

    def _transform_to_latent(self, X):
        if hasattr(X, "toarray"):
            X = X.toarray()
        X = np.asarray(X, dtype=np.float32)
        if self.scaler is not None:
            X = self.scaler.transform(X)
        tensor = torch.tensor(X, dtype=torch.float32).to(self.device)
        with torch.no_grad():
            _, latent = self.dae(tensor)
        return latent.cpu().numpy()

    def predict(self, X, meta=None):
        return self.classifier.predict(self._transform_to_latent(X))

    def predict_proba(self, X, meta=None):
        if not hasattr(self.classifier, "predict_proba"):
            raise AttributeError("The autoencoder head does not implement predict_proba.")
        return self.classifier.predict_proba(self._transform_to_latent(X))

    @property
    def classes_(self):
        return getattr(self.classifier, "classes_", None)


def _make_head(head: str, params: dict | None = None):
    params = dict(params or {})
    if head == "linsvc":
        return LinearSVC(class_weight="balanced", **params)
    if head == "rf":
        return RandomForestClassifier(class_weight="balanced", **params)
    raise PipelineError(f"Unknown autoencoder head '{head}'. Valid: linsvc, rf.")


def _head_search_space(head: str):
    if head == "linsvc":
        return {
            "C": loguniform(1e-3, 2.0),
            "penalty": ["l2"],
            "dual": [True, False],
            "tol": loguniform(1e-3, 1e-1),
        }
    if head == "rf":
        return {
            "n_estimators": randint(100, 250),
            "max_depth": randint(10, 31),
            "max_features": ["sqrt", "log2"],
        }
    raise PipelineError(f"Unknown autoencoder head '{head}'. Valid: linsvc, rf.")


def _train_dae(
    X_scaled: np.ndarray,
    params: dict,
    seed: int,
    n_jobs: int,
) -> tuple[DenoisingAutoencoder, int]:
    set_torch_seed(seed, n_jobs)
    device = torch.device("cpu")
    dae = DenoisingAutoencoder(
        input_dim=X_scaled.shape[1],
        latent_dim=int(params.get("latent_dim", 128)),
        noise_factor=float(params.get("noise_factor", 0.3)),
    ).to(device)

    tensor = torch.tensor(X_scaled, dtype=torch.float32)
    batch_size = int(params.get("batch_size", 128))
    # A final batch of size 1 would crash BatchNorm1d in training mode.
    drop_last = bool(len(tensor) > batch_size and len(tensor) % batch_size == 1)
    loader = DataLoader(
        TensorDataset(tensor),
        batch_size=batch_size,
        shuffle=True,
        generator=torch.Generator().manual_seed(seed),
        drop_last=drop_last,
    )

    criterion = nn.MSELoss()
    optimizer = optim.AdamW(
        dae.parameters(),
        lr=float(params.get("lr", 1e-3)),
        weight_decay=float(params.get("weight_decay", 1e-4)),
    )
    max_epochs = int(params.get("epochs", 150))
    patience = int(params.get("patience", 5))
    delta = float(params.get("delta_loss", 2e-4))
    best_loss = float("inf")
    patience_counter = 0
    epochs_run = 0
    dae.train()

    print("Start DAE Training...")
    for epoch in range(max_epochs):
        epoch_loss = 0.0
        for batch in loader:
            inputs = batch[0].to(device)
            optimizer.zero_grad()
            reconstructed, _ = dae(inputs)
            loss = criterion(reconstructed, inputs)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item() * inputs.size(0)
        total_loss = epoch_loss / len(loader.dataset)
        epochs_run = epoch + 1
        if epochs_run % 10 == 0 or epochs_run == 1 or epochs_run == max_epochs:
            print(f"Epoch [{epochs_run}/{max_epochs}], Loss: {total_loss:.4f}")
        if total_loss < best_loss - delta:
            best_loss = total_loss
            patience_counter = 0
        else:
            patience_counter += 1
        if patience_counter >= patience:
            print(f"Early Stopping after [{epochs_run}/{max_epochs}] Epochs!")
            break
    dae.eval()
    return dae, epochs_run


def _fit_representation(
    X: pd.DataFrame,
    params: dict,
    seed: int,
    n_jobs: int,
) -> tuple[DenoisingAutoencoder, StandardScaler, np.ndarray, int]:
    set_torch_seed(seed, n_jobs)
    X_arr = X.to_numpy(dtype=np.float32, copy=False)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_arr).astype(np.float32)
    dae, epochs = _train_dae(X_scaled, params, seed, n_jobs)
    tensor = torch.tensor(scaler.transform(X_arr), dtype=torch.float32).to(next(dae.parameters()).device)
    with torch.no_grad():
        _, latent = dae(tensor)
    return dae, scaler, latent.cpu().numpy(), epochs


def tune_autoencoder_head(
    latent: np.ndarray,
    y: pd.Series,
    head: str,
    tune_cfg: dict,
    seed: int,
    n_jobs: int,
) -> tuple[dict, dict]:
    min_class = int(pd.Series(y).astype(str).value_counts().min())
    effective_cv = min(int(tune_cfg.get("cv", 5)), min_class)
    n_iter = int(tune_cfg.get("n_iter", 50))
    if effective_cv < 2:
        return {}, {
            "skipped": True,
            "skip_reason": f"min class count is {min_class}; CV needs at least 2.",
            "cv": effective_cv,
            "n_iter": 0,
            "best_score": float("nan"),
            "avg_time_per_iteration_sec": float("nan"),
        }
    search = RandomizedSearchCV(
        estimator=_make_head(head),
        param_distributions=_head_search_space(head),
        n_iter=n_iter,
        cv=effective_cv,
        scoring="accuracy",
        n_jobs=n_jobs,
        random_state=seed,
        verbose=10,
    )
    start = time.time()
    search.fit(latent, y)
    print("\n--- TUNING FINISHED ---")
    print(f"Beste Parameter: {search.best_params_}")
    print(f"Bester CV-Score: {search.best_score_:.4f}")
    search_time_min = (time.time() - start) / 60.0
    cv_results = search.cv_results_
    mean_fit = np.asarray(cv_results.get("mean_fit_time", [0.0]))
    mean_score = np.asarray(cv_results.get("mean_score_time", [0.0]))
    return dict(search.best_params_), {
        "skipped": False,
        "cv": effective_cv,
        "n_iter": n_iter,
        "best_score": float(search.best_score_),
        "avg_time_per_iteration_sec": float(np.mean(mean_fit + mean_score) * effective_cv),
        "search_time_min": search_time_min,
        "n_candidates": len(cv_results.get("params", [])),
    }


def tune_autoencoder(
    X: pd.DataFrame,
    y: pd.Series,
    params: dict,
    head: str,
    tune_cfg: dict,
    seed: int,
    n_jobs: int,
) -> tuple[dict, dict]:
    _, _, latent, epochs = _fit_representation(X, params, seed, n_jobs)
    best_params, meta = tune_autoencoder_head(latent, y, head, tune_cfg, seed, n_jobs)
    meta["autoencoder_epochs_tuning"] = epochs
    return best_params, meta


def build_autoencoder(
    X: pd.DataFrame,
    y: pd.Series,
    params: dict,
    head: str,
    head_params: dict | None,
    seed: int,
    n_jobs: int,
) -> ScRNADAEClassifier:
    dae, scaler, latent, epochs = _fit_representation(X, params, seed, n_jobs)
    classifier = _make_head(head, head_params or {})
    classifier.fit(latent, y)
    model = ScRNADAEClassifier(dae=dae, classifier=classifier, scaler=scaler)
    model.epochs_ = epochs
    return model
