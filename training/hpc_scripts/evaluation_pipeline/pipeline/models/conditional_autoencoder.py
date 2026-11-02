"""Conditional denoising autoencoder (donor-conditioned, CPU only)."""

from __future__ import annotations

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from torch.utils.data import DataLoader, TensorDataset

from ..logging_utils import PipelineError
from .autoencoder import _make_head, set_torch_seed, tune_autoencoder_head
from .base import ModelAdapter


class ConditionalDAE(nn.Module):
    def __init__(self, input_dim: int, num_donors: int, latent_dim: int = 128, noise_factor: float = 0.3):
        super().__init__()
        self.noise_factor = noise_factor
        self.encoder = nn.Sequential(
            nn.Linear(input_dim + num_donors, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(256, latent_dim),
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim + num_donors, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(0.1),
            nn.Linear(256, input_dim),
        )

    def forward(self, x, cond):
        if self.training:
            x_noisy = x + torch.randn_like(x) * self.noise_factor
        else:
            x_noisy = x
        # Combine Gene data and Donor ID for the Encoder
        x_cond = torch.cat([x_noisy, cond], dim=1)
        latent = self.encoder(x_cond)
        # Combine Latent space and Donor ID for the Decoder
        latent_cond = torch.cat([latent, cond], dim=1)
        reconstructed = self.decoder(latent_cond)
        return reconstructed, latent


class ScRNACVAEClassifier(ModelAdapter):
    def __init__(self, cdae, classifier, scaler, num_donors):
        self.cdae = cdae
        self.classifier = classifier
        self.scaler = scaler
        self.num_donors = num_donors
        self.cdae.eval()
        self.device = next(cdae.parameters()).device
        self.epochs_ = None

    def _transform_to_latent(self, X):
        if hasattr(X, "toarray"):
            X = X.toarray()
        X = np.asarray(X, dtype=np.float32)
        if self.scaler is not None:
            X = self.scaler.transform(X)
        tensor = torch.tensor(X, dtype=torch.float32).to(self.device)
        # Same neutral donor vector at inference as the old implementation.
        cond_dummy = torch.zeros((tensor.shape[0], self.num_donors), dtype=torch.float32).to(self.device)
        with torch.no_grad():
            _, latent = self.cdae(tensor, cond_dummy)
        return latent.cpu().numpy()

    def predict(self, X, meta=None):
        return self.classifier.predict(self._transform_to_latent(X))

    def predict_proba(self, X, meta=None):
        if not hasattr(self.classifier, "predict_proba"):
            raise AttributeError("The conditional autoencoder head does not implement predict_proba.")
        return self.classifier.predict_proba(self._transform_to_latent(X))

    @property
    def classes_(self):
        return getattr(self.classifier, "classes_", None)


def _one_hot(meta: pd.DataFrame, batch_key: str) -> tuple[np.ndarray, OneHotEncoder]:
    if meta is None:
        raise PipelineError(
            f"Conditional autoencoder needs metadata with batch key '{batch_key}'."
        )
    if batch_key not in meta.columns:
        raise PipelineError(
            f"Conditional autoencoder metadata is missing batch key '{batch_key}'. "
            f"Available: {list(meta.columns)}"
        )
    encoder = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
    values = meta[batch_key].astype(str).to_numpy().reshape(-1, 1)
    return encoder.fit_transform(values).astype(np.float32), encoder


def _train_cdae(
    X_scaled: np.ndarray,
    cond: np.ndarray,
    params: dict,
    seed: int,
    n_jobs: int,
) -> tuple[ConditionalDAE, int]:
    set_torch_seed(seed, n_jobs)
    device = torch.device("cpu")
    cdae = ConditionalDAE(
        input_dim=X_scaled.shape[1],
        num_donors=cond.shape[1],
        latent_dim=int(params.get("latent_dim", 128)),
        noise_factor=float(params.get("noise_factor", 0.3)),
    ).to(device)
    x_tensor = torch.tensor(X_scaled, dtype=torch.float32)
    c_tensor = torch.tensor(cond, dtype=torch.float32)
    batch_size = int(params.get("batch_size", 128))
    drop_last = bool(len(x_tensor) > batch_size and len(x_tensor) % batch_size == 1)
    loader = DataLoader(
        TensorDataset(x_tensor, c_tensor),
        batch_size=batch_size,
        shuffle=True,
        generator=torch.Generator().manual_seed(seed),
        drop_last=drop_last,
    )
    criterion = nn.MSELoss()
    optimizer = optim.AdamW(
        cdae.parameters(),
        lr=float(params.get("lr", 1e-3)),
        weight_decay=float(params.get("weight_decay", 1e-4)),
    )
    max_epochs = int(params.get("epochs", 150))
    patience = int(params.get("patience", 5))
    delta = float(params.get("delta_loss", 2e-4))
    best_loss = float("inf")
    patience_counter = 0
    epochs_run = 0
    cdae.train()

    print("Start Conditional DAE Training...")
    for epoch in range(max_epochs):
        epoch_loss = 0.0
        for x_batch, c_batch in loader:
            x_batch = x_batch.to(device)
            c_batch = c_batch.to(device)
            optimizer.zero_grad()
            reconstructed, _ = cdae(x_batch, c_batch)
            loss = criterion(reconstructed, x_batch)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item() * x_batch.size(0)
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
    cdae.eval()
    return cdae, epochs_run


def _fit_representation(
    X: pd.DataFrame,
    meta: pd.DataFrame,
    batch_key: str,
    params: dict,
    seed: int,
    n_jobs: int,
) -> tuple[ConditionalDAE, StandardScaler, OneHotEncoder, np.ndarray, int]:
    set_torch_seed(seed, n_jobs)
    X_arr = X.to_numpy(dtype=np.float32, copy=False)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_arr).astype(np.float32)
    cond, encoder = _one_hot(meta, batch_key)
    cdae, epochs = _train_cdae(X_scaled, cond, params, seed, n_jobs)
    tensor = torch.tensor(scaler.transform(X_arr), dtype=torch.float32).to(next(cdae.parameters()).device)
    cond_tensor = torch.tensor(cond, dtype=torch.float32).to(next(cdae.parameters()).device)
    with torch.no_grad():
        _, latent = cdae(tensor, cond_tensor)
    return cdae, scaler, encoder, latent.cpu().numpy(), epochs


def tune_conditional_autoencoder(
    X: pd.DataFrame,
    y: pd.Series,
    meta: pd.DataFrame,
    batch_key: str,
    params: dict,
    head: str,
    tune_cfg: dict,
    seed: int,
    n_jobs: int,
) -> tuple[dict, dict]:
    _, _, _, latent, epochs = _fit_representation(X, meta, batch_key, params, seed, n_jobs)
    best_params, meta_info = tune_autoencoder_head(latent, y, head, tune_cfg, seed, n_jobs)
    meta_info["autoencoder_epochs_tuning"] = epochs
    return best_params, meta_info


def build_conditional_autoencoder(
    X: pd.DataFrame,
    y: pd.Series,
    meta: pd.DataFrame,
    batch_key: str,
    params: dict,
    head: str,
    head_params: dict | None,
    seed: int,
    n_jobs: int,
) -> ScRNACVAEClassifier:
    cdae, scaler, encoder, latent, epochs = _fit_representation(
        X, meta, batch_key, params, seed, n_jobs
    )
    classifier = _make_head(head, head_params or {})
    classifier.fit(latent, y)
    model = ScRNACVAEClassifier(
        cdae=cdae,
        classifier=classifier,
        scaler=scaler,
        num_donors=len(encoder.categories_[0]),
    )
    model.epochs_ = epochs
    return model
