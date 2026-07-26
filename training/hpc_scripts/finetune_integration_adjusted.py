# %%
import copy
import gc
import json
import os
from pathlib import Path
import sys
import time
import traceback
from typing import List, Tuple, Dict, Union, Optional
import warnings

import torch
from anndata import AnnData
import scanpy as sc
from scipy.sparse import issparse
import numpy as np
import wandb
import matplotlib.pyplot as plt
from torch import nn
from torch.nn import functional as F
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split

from scgpt.tokenizer.gene_tokenizer import GeneVocab

sys.path.append("../")
import scgpt as scg
from scgpt.model import TransformerModel, AdversarialDiscriminator
from scgpt.tokenizer import tokenize_and_pad_batch, random_mask_value
from scgpt.loss import (
    masked_mse_loss,
    masked_relative_error,
    criterion_neg_log_bernoulli,
)
from scgpt.preprocess import Preprocessor
from scgpt import SubsetsBatchSampler
from scgpt.utils import set_seed, category_str2int, eval_scib_metrics

from test_robustness import test_robustness

import pandas as pd
import pickle
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
import random

sc.set_figure_params(figsize=(4, 4))
os.environ["KMP_WARNINGS"] = "off"
os.environ["WANDB_MODE"] = "offline"

hyperparameter_defaults = dict(
    seed=random.randint(0, 999999),
    dataset_name="CellTypistDataset",
    h5ad_path="/home/hpc/iwbn/iwbn133h/data/CellTypistDataset/CountAdded_PIP_global_object_for_cellxgene_annotated.h5ad",
    batch_col="Donor",
    do_train=True,
    load_model="/home/hpc/iwbn/iwbn133h/scGPT/save/scGPT_bc",
    mask_ratio=0.4,
    epochs=30,
    n_bins=51,
    GEPC=True,  # Masked value prediction for cell embedding
    ecs_thres=0.8,  # Elastic cell similarity objective, 0.0 to 1.0, 0.0 to disable
    dab_weight=1.0,
    lr=1e-4,
    batch_size=64,
    layer_size=128,
    nlayers=4,
    nhead=4,
    # if load model, batch_size, layer_size, nlayers, nhead will be ignored
    dropout=0.2,
    schedule_ratio=0.9,  # ratio of epochs for learning rate schedule
    save_eval_interval=5,
    log_interval=100,
    fast_transformer=True,
    pre_norm=False,
    amp=True,  # Automatic Mixed Precision
)
run = wandb.init(
    config=hyperparameter_defaults,
    project="scGPT",
    reinit=True,
    settings=wandb.Settings(start_method="fork"),
)
config = wandb.config
print(config)

print(f"Seed: {config.seed}")
set_seed(config.seed)

# %%
# settings for input and preprocessing
pad_token = "<pad>"
special_tokens = [pad_token, "<cls>", "<eoc>"]
mask_ratio = config.mask_ratio
mask_value = -1
pad_value = -2
n_input_bins = config.n_bins

n_hvg = 1200  # number of highly variable genes
max_seq_len = n_hvg + 1
per_seq_batch_sample = True
DSBN = True  # Domain-spec batchnorm
explicit_zero_prob = True  # whether explicit bernoulli for zeros

# %%
dataset_name = config.dataset_name
save_dir = Path(f"./save/dev_{dataset_name}-{time.strftime('%b%d-%H-%M')}/")
save_dir.mkdir(parents=True, exist_ok=True)
print(f"save to {save_dir}")
# save the whole script to the dir
os.system(f"cp {__file__} {save_dir}")

logger = scg.logger
scg.utils.add_file_handler(logger, save_dir / "run.log")


# %% [markdown]
# ## Loading and preparing data
adata = sc.read_h5ad(config.h5ad_path)
ori_batch_col = config.batch_col


# ==============================================================================
# My Preprocessing
# ==============================================================================

# mitochondrial genes, "MT-" for human, "Mt-" for mouse
adata.var["mt"] = adata.var_names.str.startswith("MT-")
# ribosomal genes
adata.var["ribo"] = adata.var_names.str.startswith(("RPS", "RPL"))
# hemoglobin genes
adata.var["hb"] = adata.var_names.str.contains("^HB[^(P)]")

sc.pp.calculate_qc_metrics(adata, qc_vars=["mt", "ribo", "hb"], inplace=True, log1p=True)

# Remove mitochondrial, ribosomal and hemoglobin
adata = adata[:, ~adata.var["mt"]].copy()
adata = adata[:, ~adata.var["ribo"]].copy()
adata = adata[:, ~adata.var["hb"]].copy()

# Doublet Detection
sc.pp.scrublet(adata, batch_key="Donor")
adata = adata[adata.obs['predicted_doublet'] == False].copy()


# Normalization

# Saving count data
adata.layers["counts"] = adata.X.copy()

# Normalizing to median total counts
sc.pp.normalize_total(adata, target_sum=1e4)
# Logarithmize the data
sc.pp.log1p(adata)

adata.var["gene_name"] = adata.var.index.tolist()

if config.load_model is not None:
    model_dir = Path(config.load_model)
    vocab_file = model_dir / "vocab.json"
    vocab = GeneVocab.from_file(vocab_file)
    for s in special_tokens:
        if s not in vocab:
            vocab.append_token(s)

    adata.var["id_in_vocab"] = [
        1 if gene in vocab else -1 for gene in adata.var["gene_name"]
    ]
    gene_ids_in_vocab = np.array(adata.var["id_in_vocab"])
    logger.info(
        f"match {np.sum(gene_ids_in_vocab >= 0)}/{len(gene_ids_in_vocab)} genes "
        f"in vocabulary of size {len(vocab)}."
    )
    adata = adata[:, adata.var["id_in_vocab"] >= 0].copy()

# Filtering Highly variable genes to n_hvg
sc.pp.highly_variable_genes(adata, n_top_genes=n_hvg, flavor="seurat")

# Apply filter
adata = adata[:, adata.var['highly_variable']].copy()

# Convert string labels in int labels
unique_labels = adata.obs["scumi-annotation"].unique()
label2id = {label: i for i, label in enumerate(unique_labels)}
id2label = {i: label for label, i in label2id.items()}

adata.obs["celltype"] = adata.obs["scumi-annotation"].map(label2id)

# Global scGPT-Binning
preprocessor = Preprocessor(
    use_key="X",
    filter_gene_by_counts=False,
    filter_cell_by_counts=False,
    normalize_total=None,
    log1p=False,
    subset_hvg=None,
    binning=config.n_bins,
    result_binned_key="X_binned",
)
preprocessor(adata, batch_key=None)

# Create the train test split
donor_train = ['637C', 'A35', 'A36', 'D503']
donor_test = ['621B', 'D496']

# Split train and test data based on donor
adata_test = adata[adata.obs["Donor"].isin(donor_test)].copy()
adata = adata[adata.obs["Donor"].isin(donor_train)].copy()


# %%
# make the batch category column
adata.obs["str_batch"] = adata.obs[ori_batch_col].astype(str)
batch_id_labels = adata.obs["str_batch"].astype("category").cat.codes.values
adata.obs["batch_id"] = batch_id_labels


if config.load_model is not None:
    model_config_file = model_dir / "args.json"
    model_file = model_dir / "best_model.pt"
    with open(model_config_file, "r") as f:
        model_configs = json.load(f)
    logger.info(
        f"Resume model from {model_file}, the model args will be overriden by the "
        f"config {model_config_file}."
    )
    embsize = model_configs["embsize"]
    nhead = model_configs["nheads"]
    d_hid = model_configs["d_hid"]
    nlayers = model_configs["nlayers"]
    n_layers_cls = model_configs["n_layers_cls"]
else:
    embsize = config.layer_size
    nhead = config.nhead
    nlayers = config.nlayers
    d_hid = config.layer_size


# %%
# Here was the preprocessing originally, I moved it up before the batch creation to avoid errors with the split on donor


# %%
if per_seq_batch_sample:
    # sort the adata by batch_id in advance
    adata_sorted = adata[adata.obs["batch_id"].argsort()].copy()

# %% [markdown]
# ## Tokenize input

# %%
input_layer_key = "X_binned"
all_counts = (
    adata.layers[input_layer_key].toarray()
    if issparse(adata.layers[input_layer_key])
    else adata.layers[input_layer_key]
)
genes = adata.var["gene_name"].tolist()

celltypes_labels = adata.obs["celltype"].tolist()  # make sure count from 0
num_types = len(set(celltypes_labels))
celltypes_labels = np.array(celltypes_labels)

batch_ids = adata.obs["batch_id"].tolist()
num_batch_types = len(set(batch_ids))
batch_ids = np.array(batch_ids)

(
    train_data,
    valid_data,
    train_celltype_labels,
    valid_celltype_labels,
    train_batch_labels,
    valid_batch_labels,
) = train_test_split(
    all_counts, celltypes_labels, batch_ids, test_size=0.1, shuffle=True, stratify=celltypes_labels
)


# I added Resampling for better score on smaller classes
target_threshold = 1000

print(f"--- Upsamle train data to {target_threshold} samples per class ---")
unique_train_cls, train_counts = np.unique(train_celltype_labels, return_counts=True)
upsampled_data = []
upsampled_celltypes = []
upsampled_batches = []

for cls in unique_train_cls:
    cls_indices = np.where(train_celltype_labels == cls)[0]
    current_count = len(cls_indices)

    if current_count < target_threshold:
        # Class is too small -> take all samples and then pick random samples to fill up
        needed = target_threshold - current_count
        extra_indices = np.random.choice(cls_indices, size=needed, replace=True)
        chosen_indices = np.concatenate([cls_indices, extra_indices])
    else:
        # Class is big enough -> leave it as it is
        chosen_indices = cls_indices

    upsampled_data.append(train_data[chosen_indices])
    upsampled_celltypes.append(train_celltype_labels[chosen_indices])
    upsampled_batches.append(train_batch_labels[chosen_indices])

# Merge data
train_data = np.concatenate(upsampled_data, axis=0)
train_celltype_labels = np.concatenate(upsampled_celltypes, axis=0)
train_batch_labels = np.concatenate(upsampled_batches, axis=0)

# Shuffle data
shuffle_idx = np.random.permutation(len(train_celltype_labels))
train_data = train_data[shuffle_idx]
train_celltype_labels = train_celltype_labels[shuffle_idx]
train_batch_labels = train_batch_labels[shuffle_idx]




# %%
if config.load_model is None:
    vocab = GeneVocab(genes + special_tokens)   # bidirectional lookup [gene <-> int]
vocab.set_default_index(vocab["<pad>"])
gene_ids = np.array(vocab(genes), dtype=int)

# %%
tokenized_train = tokenize_and_pad_batch(
    train_data,
    gene_ids,
    max_len=max_seq_len,
    vocab=vocab,
    pad_token=pad_token,
    pad_value=pad_value,
    append_cls=True,  # append <cls> token at the beginning
    include_zero_gene=True,
)
tokenized_valid = tokenize_and_pad_batch(
    valid_data,
    gene_ids,
    max_len=max_seq_len,
    vocab=vocab,
    pad_token=pad_token,
    pad_value=pad_value,
    append_cls=True,
    include_zero_gene=True,
)
logger.info(
    f"train set number of samples: {tokenized_train['genes'].shape[0]}, "
    f"\n\t feature length: {tokenized_train['genes'].shape[1]}"
)
logger.info(
    f"valid set number of samples: {tokenized_valid['genes'].shape[0]}, "
    f"\n\t feature length: {tokenized_valid['genes'].shape[1]}"
)


# %%
def prepare_data(sort_seq_batch=False) -> Tuple[Dict[str, torch.Tensor]]:
    masked_values_train = random_mask_value(
        tokenized_train["values"],
        mask_ratio=mask_ratio,
        mask_value=mask_value,
        pad_value=pad_value,
    )
    masked_values_valid = random_mask_value(
        tokenized_valid["values"],
        mask_ratio=mask_ratio,
        mask_value=mask_value,
        pad_value=pad_value,
    )
    print(
        f"random masking at epoch {epoch:3d}, ratio of masked values in train: ",
        f"{(masked_values_train == mask_value).sum() / (masked_values_train - pad_value).count_nonzero():.4f}",
    )

    input_gene_ids_train, input_gene_ids_valid = (
        tokenized_train["genes"],
        tokenized_valid["genes"],
    )
    input_values_train, input_values_valid = masked_values_train, masked_values_valid
    target_values_train, target_values_valid = (
        tokenized_train["values"],
        tokenized_valid["values"],
    )

    tensor_batch_labels_train = torch.from_numpy(train_batch_labels).long()
    tensor_batch_labels_valid = torch.from_numpy(valid_batch_labels).long()
    tensor_celltype_labels_train = torch.from_numpy(train_celltype_labels).long()
    tensor_celltype_labels_valid = torch.from_numpy(valid_celltype_labels).long()

    if sort_seq_batch:
        train_sort_ids = np.argsort(train_batch_labels)
        input_gene_ids_train = input_gene_ids_train[train_sort_ids]
        input_values_train = input_values_train[train_sort_ids]
        target_values_train = target_values_train[train_sort_ids]
        tensor_batch_labels_train = tensor_batch_labels_train[train_sort_ids]
        tensor_celltype_labels_train = tensor_celltype_labels_train[train_sort_ids]

        valid_sort_ids = np.argsort(valid_batch_labels)
        input_gene_ids_valid = input_gene_ids_valid[valid_sort_ids]
        input_values_valid = input_values_valid[valid_sort_ids]
        target_values_valid = target_values_valid[valid_sort_ids]
        tensor_batch_labels_valid = tensor_batch_labels_valid[valid_sort_ids]
        tensor_celltype_labels_valid = tensor_celltype_labels_valid[valid_sort_ids]

    train_data_pt = {
        "gene_ids": input_gene_ids_train,
        "values": input_values_train,
        "target_values": target_values_train,
        "batch_labels": tensor_batch_labels_train,
        "celltype_labels": tensor_celltype_labels_train,
    }
    valid_data_pt = {
        "gene_ids": input_gene_ids_valid,
        "values": input_values_valid,
        "target_values": target_values_valid,
        "batch_labels": tensor_batch_labels_valid,
        "celltype_labels": tensor_celltype_labels_valid,
    }

    return train_data_pt, valid_data_pt


# dataset
class SeqDataset(Dataset):
    def __init__(self, data: Dict[str, torch.Tensor]):
        self.data = data

    def __len__(self):
        return self.data["gene_ids"].shape[0]

    def __getitem__(self, idx):
        return {k: v[idx] for k, v in self.data.items()}


# data_loader
def prepare_dataloader(
    data_pt: Dict[str, torch.Tensor],
    batch_size: int,
    shuffle: bool = False,
    intra_domain_shuffle: bool = False,
    drop_last: bool = False,
    num_workers: int = 0,
) -> DataLoader:
    dataset = SeqDataset(data_pt)

    if per_seq_batch_sample:
        # find the indices of samples in each seq batch
        subsets = []
        batch_labels_array = data_pt["batch_labels"].numpy()
        for batch_label in np.unique(batch_labels_array):
            batch_indices = np.where(batch_labels_array == batch_label)[0].tolist()
            subsets.append(batch_indices)
        data_loader = DataLoader(
            dataset=dataset,
            batch_sampler=SubsetsBatchSampler(
                subsets,
                batch_size,
                intra_subset_shuffle=intra_domain_shuffle,
                inter_subset_shuffle=shuffle,
                drop_last=drop_last,
            ),
            num_workers=num_workers,
            pin_memory=True,
        )
        return data_loader

    data_loader = DataLoader(
        dataset=dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        drop_last=drop_last,
        num_workers=num_workers,
        pin_memory=True,
    )
    return data_loader


# %% [markdown]
# # Create and finetune scGPT

# %%
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

ntokens = len(vocab)  # size of vocabulary
model = TransformerModel(
    ntokens,
    embsize,
    nhead,
    d_hid,
    nlayers,
    vocab=vocab,
    dropout=config.dropout,
    pad_token=pad_token,
    pad_value=pad_value,
    do_mvc=config.GEPC,
    do_dab=True,
    use_batch_labels=True,
    num_batch_labels=num_batch_types,
    domain_spec_batchnorm=DSBN,
    n_input_bins=n_input_bins,
    n_cls=num_types,
    ecs_threshold=config.ecs_thres,
    explicit_zero_prob=explicit_zero_prob,
    use_fast_transformer=config.fast_transformer,
    pre_norm=config.pre_norm,
)
if config.load_model is not None:
    try:
        model.load_state_dict(torch.load(model_file))
        logger.info(f"Loading all model params from {model_file}")
    except:
        # only load params that are in the model and match the size
        model_dict = model.state_dict()
        pretrained_dict = torch.load(model_file)
        pretrained_dict = {
            k: v
            for k, v in pretrained_dict.items()
            if k in model_dict and v.shape == model_dict[k].shape
        }
        for k, v in pretrained_dict.items():
            logger.info(f"Loading params {k} with shape {v.shape}")
        model_dict.update(pretrained_dict)
        model.load_state_dict(model_dict)

model.to(device)
wandb.watch(model)


criterion = masked_mse_loss
criterion_dab = nn.CrossEntropyLoss()
criterion_cls = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(
    model.parameters(), lr=config.lr, eps=1e-4 if config.amp else 1e-8
)
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, 1, gamma=config.schedule_ratio)

scaler = torch.cuda.amp.GradScaler(enabled=config.amp)


def train(model: nn.Module, loader: DataLoader) -> None:
    """
    Train the model for one epoch.
    """
    model.train()
    total_loss, total_mse, total_gepc = 0.0, 0.0, 0.0
    total_error = 0.0
    total_cls = 0.0
    log_interval = config.log_interval
    start_time = time.time()

    num_batches = len(loader)
    for batch, batch_data in enumerate(loader):
        input_gene_ids = batch_data["gene_ids"].to(device)
        input_values = batch_data["values"].to(device)
        target_values = batch_data["target_values"].to(device)
        batch_labels = batch_data["batch_labels"].to(device)
        celltype_labels = batch_data["celltype_labels"].to(device)

        src_key_padding_mask = input_gene_ids.eq(vocab[pad_token])
        with torch.cuda.amp.autocast(enabled=config.amp):
            output_dict = model(
                input_gene_ids,
                input_values,
                src_key_padding_mask=src_key_padding_mask,
                batch_labels=batch_labels if DSBN else None,
                CLS=True,
                MVC=config.GEPC,
                ECS=config.ecs_thres > 0,
            )

            masked_positions = input_values.eq(mask_value)  # the postions to predict
            loss = loss_mse = criterion(
                output_dict["mlm_output"], target_values, masked_positions
            )
            metrics_to_log = {"train/mse": loss_mse.item()}
            if explicit_zero_prob:
                loss_zero_log_prob = criterion_neg_log_bernoulli(
                    output_dict["mlm_zero_probs"], target_values, masked_positions
                )
                loss = loss + loss_zero_log_prob
                metrics_to_log.update({"train/nzlp": loss_zero_log_prob.item()})
            if config.GEPC:
                loss_gepc = criterion(
                    output_dict["mvc_output"], target_values, masked_positions
                )
                loss = loss + loss_gepc
                metrics_to_log.update({"train/mvc": loss_gepc.item()})
            if config.GEPC and explicit_zero_prob:
                loss_gepc_zero_log_prob = criterion_neg_log_bernoulli(
                    output_dict["mvc_zero_probs"], target_values, masked_positions
                )
                loss = loss + loss_gepc_zero_log_prob
                metrics_to_log.update(
                    {"train/mvc_nzlp": loss_gepc_zero_log_prob.item()}
                )
            if config.ecs_thres > 0:
                loss_ecs = 10 * output_dict["loss_ecs"]
                loss = loss + loss_ecs
                metrics_to_log.update({"train/ecs": loss_ecs.item()})
            loss_dab = criterion_dab(output_dict["dab_output"], batch_labels)
            loss = loss + config.dab_weight * loss_dab
            metrics_to_log.update({"train/dab": loss_dab.item()})
            loss_cls = criterion_cls(output_dict["cls_output"], celltype_labels)
            loss = loss + loss_cls
            metrics_to_log.update({"train/cls": loss_cls.item()})

        model.zero_grad()
        scaler.scale(loss).backward()
        scaler.unscale_(optimizer)
        with warnings.catch_warnings(record=True) as w:
            warnings.filterwarnings("always")
            torch.nn.utils.clip_grad_norm_(
                model.parameters(),
                1.0,
                error_if_nonfinite=False if scaler.is_enabled() else True,
            )
            if len(w) > 0:
                logger.warning(
                    f"Found infinite gradient. This may be caused by the gradient "
                    f"scaler. The current scale is {scaler.get_scale()}. This warning "
                    "can be ignored if no longer occurs after autoscaling of the scaler."
                )
        scaler.step(optimizer)
        scaler.update()

        wandb.log(metrics_to_log)

        with torch.no_grad():
            mre = masked_relative_error(
                output_dict["mlm_output"], target_values, masked_positions
            )

        total_loss += loss.item()
        total_mse += loss_mse.item()
        total_gepc += loss_gepc.item() if config.GEPC else 0.0
        total_error += mre.item()
        total_cls += loss_cls.item()
        if batch % log_interval == 0 and batch > 0:
            lr = scheduler.get_last_lr()[0]
            ms_per_batch = (time.time() - start_time) * 1000 / log_interval
            cur_loss = total_loss / log_interval
            cur_mse = total_mse / log_interval
            cur_gepc = total_gepc / log_interval if config.GEPC else 0.0
            cur_error = total_error / log_interval
            cur_cls = total_cls / log_interval
            logger.info(
                f"| epoch {epoch:3d} | {batch:3d}/{num_batches:3d} batches | "
                f"lr {lr:05.4f} | ms/batch {ms_per_batch:5.2f} | "
                f"loss {cur_loss:5.2f} | mse {cur_mse:5.2f} | mre {cur_error:5.2f} |"
                + (f"gepc {cur_gepc:5.2f} |" if config.GEPC else "")
                + f"cls {cur_cls:5.2f} |"
            )
            total_loss = 0
            total_mse = 0
            total_gepc = 0
            total_error = 0
            total_cls = 0
            start_time = time.time()


def define_wandb_metrcis():
    wandb.define_metric("valid/mse", summary="min", step_metric="epoch")
    wandb.define_metric("valid/mre", summary="min", step_metric="epoch")
    wandb.define_metric("valid/dab", summary="min", step_metric="epoch")
    wandb.define_metric("valid/cls", summary="min", step_metric="epoch")
    wandb.define_metric("valid/cls_acc", summary="max", step_metric="epoch")
    wandb.define_metric("valid/sum_mse_dab", summary="min", step_metric="epoch")
    wandb.define_metric("test/avg_bio", summary="max")


def evaluate(model: nn.Module, loader: DataLoader) -> float:
    """
    Evaluate the model on the evaluation data.
    """
    model.eval()
    total_loss = 0.0
    total_error = 0.0
    total_dab = 0.0
    total_cls = 0.0
    cls_correct = 0
    cls_total = 0
    total_num = 0
    with torch.no_grad():
        for batch_data in loader:
            input_gene_ids = batch_data["gene_ids"].to(device)
            input_values = batch_data["values"].to(device)
            target_values = batch_data["target_values"].to(device)
            batch_labels = batch_data["batch_labels"].to(device)
            celltype_labels = batch_data["celltype_labels"].to(device)

            src_key_padding_mask = input_gene_ids.eq(vocab[pad_token])
            with torch.cuda.amp.autocast(enabled=config.amp):
                output_dict = model(
                    input_gene_ids,
                    input_values,
                    src_key_padding_mask=src_key_padding_mask,
                    batch_labels=batch_labels if DSBN else None,
                    CLS=True,
                )
                output_values = output_dict["mlm_output"]

                masked_positions = input_values.eq(mask_value)
                loss = criterion(output_values, target_values, masked_positions)
                loss_dab = criterion_dab(output_dict["dab_output"], batch_labels)
                loss_cls = criterion_cls(output_dict["cls_output"], celltype_labels)
                cls_pred = output_dict["cls_output"].argmax(dim=1)

            total_loss += loss.item() * len(input_gene_ids)
            total_error += masked_relative_error(
                output_values, target_values, masked_positions
            ).item() * len(input_gene_ids)
            total_dab += loss_dab.item() * len(input_gene_ids)
            total_cls += loss_cls.item() * len(input_gene_ids)
            cls_correct += (cls_pred == celltype_labels).sum().item()
            cls_total += len(celltype_labels)
            total_num += len(input_gene_ids)

    cls_acc = cls_correct / cls_total if cls_total > 0 else 0.0
    wandb.log(
        {
            "valid/mse": total_loss / total_num,
            "valid/mre": total_error / total_num,
            "valid/dab": total_dab / total_num,
            "valid/cls": total_cls / total_num,
            "valid/cls_acc": cls_acc,
            "valid/sum_mse_dab": (total_loss + config.dab_weight * total_dab)
            / total_num,
            "epoch": epoch,
        },
    )

    return total_loss / total_num, total_error / total_num


def eval_testdata(
    model: nn.Module,
    adata_t: AnnData,
    include_types: List[str] = ["cls"],
) -> Optional[Dict]:
    """evaluate the model on test dataset of adata_t"""
    model.eval()

    # copy adata_t to avoid reuse previously computed results stored in adata_t
    adata_t = adata_t.copy()

    all_counts = (
        adata_t.layers[input_layer_key].toarray()
        if issparse(adata_t.layers[input_layer_key])
        else adata_t.layers[input_layer_key]
    )

    celltypes_labels = adata_t.obs["celltype"].tolist()
    celltypes_labels = np.array(celltypes_labels)

    batch_ids = adata_t.obs["batch_id"].tolist()
    batch_ids = np.array(batch_ids)

    # Evaluate cls cell embeddings
    if "cls" in include_types:
        logger.info("Evaluating cls cell embeddings")
        tokenized_all = tokenize_and_pad_batch(
            all_counts,
            gene_ids,
            max_len=max_seq_len,
            vocab=vocab,
            pad_token=pad_token,
            pad_value=pad_value,
            append_cls=True,  # append <cls> token at the beginning
            include_zero_gene=True,
        )
        all_gene_ids, all_values = tokenized_all["genes"], tokenized_all["values"]
        src_key_padding_mask = all_gene_ids.eq(vocab[pad_token])
        with torch.no_grad(), torch.cuda.amp.autocast(enabled=config.amp):
            cell_embeddings = model.encode_batch(
                all_gene_ids,
                all_values.float(),
                src_key_padding_mask=src_key_padding_mask,
                batch_size=config.batch_size,
                batch_labels=torch.from_numpy(batch_ids).long() if DSBN else None,
                time_step=0,
                return_np=True,
            )
        cell_embeddings = cell_embeddings / np.linalg.norm(
            cell_embeddings, axis=1, keepdims=True
        )

        adata_t.obsm["X_scGPT"] = cell_embeddings

        results = {}
        try:
            results = eval_scib_metrics(adata_t)
        except Exception as e:
            traceback.print_exc()
            logger.error(e)

        sc.pp.neighbors(adata_t, use_rep="X_scGPT")
        sc.tl.umap(adata_t, min_dist=0.3)
        fig = sc.pl.umap(
            adata_t,
            color=["str_batch"],
            title=[f"batch, avg_bio = {results.get('avg_bio', 0.0):.4f}"],
            frameon=False,
            return_fig=True,
            show=False,
        )

        results["batch_umap"] = fig

        sc.pp.neighbors(adata_t, use_rep="X_scGPT")
        sc.tl.umap(adata_t, min_dist=0.3)
        fig = sc.pl.umap(
            adata_t,
            color=["celltype"],
            title=[
                f"celltype, avg_bio = {results.get('avg_bio', 0.0):.4f}",
            ],
            frameon=False,
            return_fig=True,
            show=False,
        )

        results["celltype_umap"] = fig

    if len(include_types) == 1:
        return results


# %%
best_val_loss = float("inf")
best_avg_bio = 0.0
best_model = None
define_wandb_metrcis()
epoch_times = []

for epoch in range(1, config.epochs + 1):
    epoch_start_time = time.time()
    train_data_pt, valid_data_pt = prepare_data(sort_seq_batch=per_seq_batch_sample)
    train_loader = prepare_dataloader(
        train_data_pt,
        batch_size=config.batch_size,
        shuffle=False,
        intra_domain_shuffle=True,
        drop_last=False,
    )
    valid_loader = prepare_dataloader(
        valid_data_pt,
        batch_size=config.batch_size,
        shuffle=False,
        intra_domain_shuffle=False,
        drop_last=False,
    )

    if config.do_train:
        train(
            model,
            loader=train_loader,
        )
    val_loss, val_mre = evaluate(
        model,
        loader=valid_loader,
    )
    elapsed = time.time() - epoch_start_time
    epoch_times.append(elapsed)
    logger.info("-" * 89)
    logger.info(
        f"| end of epoch {epoch:3d} | time: {elapsed:5.2f}s | "
        f"valid loss/mse {val_loss:5.4f} | mre {val_mre:5.4f}"
    )
    logger.info("-" * 89)

    if val_loss < best_val_loss:
        best_val_loss = val_loss
        best_model = copy.deepcopy(model)
        best_model_epoch = epoch
        logger.info(f"Best model with score {best_val_loss:5.4f}")

    if epoch % config.save_eval_interval == 0 or epoch == config.epochs:
        logger.info(f"Saving model to {save_dir}")
        torch.save(best_model.state_dict(), save_dir / f"model_e{best_model_epoch}.pt")

        # eval on testdata
        results = eval_testdata(
            best_model,
            adata_t=adata_sorted if per_seq_batch_sample else adata,
            include_types=["cls"],
        )
        results["batch_umap"].savefig(
            save_dir / f"embeddings_batch_umap[cls]_e{best_model_epoch}.png", dpi=300
        )

        results["celltype_umap"].savefig(
            save_dir / f"embeddings_celltype_umap[cls]_e{best_model_epoch}.png", dpi=300
        )
        metrics_to_log = {"test/" + k: v for k, v in results.items()}
        metrics_to_log["test/batch_umap"] = wandb.Image(
            str(save_dir / f"embeddings_batch_umap[cls]_e{best_model_epoch}.png"),
            caption=f"celltype avg_bio epoch {best_model_epoch}",
        )

        metrics_to_log["test/celltype_umap"] = wandb.Image(
            str(save_dir / f"embeddings_celltype_umap[cls]_e{best_model_epoch}.png"),
            caption=f"celltype avg_bio epoch {best_model_epoch}",
        )
        metrics_to_log["test/best_model_epoch"] = best_model_epoch
        wandb.log(metrics_to_log)
        wandb.log({"avg_bio": results.get("avg_bio", 0.0)})

    scheduler.step()


# %%
# save the best model
if best_model is None:
    best_model = model
#torch.save(best_model.state_dict(), save_dir / "best_model.pt")

# %% [markdown]
# ## Cell Type Prediction and Robustness

# --- Prepare test data ---
#X_test_robustness = pd.DataFrame(
#    adata_test.X.toarray() if issparse(adata_test.X) else np.array(adata_test.X),
#    index=adata_test.obs_names,
#    columns=adata_test.var["gene_name"].tolist(),
#)
X_test_robustness = adata_test.to_df()
y_test_robustness = adata_test.obs["scumi-annotation"]

logger.info(
    f"Test data: {X_test_robustness.shape[0]} cells, "
    f"{X_test_robustness.shape[1]} genes, "
    f"{len(y_test_robustness.unique())} classes"
)

# %%
# --- Wrapper class that uses scGPT's built-in cls_decoder ---
class ScGPTPredictor:
    def __init__(
        self, model, vocab, gene_ids, genes, n_bins, n_hvg, device,
        pad_token="<pad>", pad_value=-2, max_seq_len=None, id2label=id2label,
        baseline_df=X_test_robustness, adata_test=adata_test,
    ):
        self.model = model
        self.vocab = vocab
        self.gene_ids = gene_ids
        self.genes = genes
        self.n_bins = n_bins
        self.n_hvg = n_hvg
        self.device = device
        self.pad_token = pad_token
        self.pad_value = pad_value
        self.max_seq_len = max_seq_len or (n_hvg + 1)
        self.id2label = id2label
        self.baseline_df = baseline_df
        self.adata_test = adata_test

    def predict(self, X):
        # X: pd.DataFrame with gene names as columns, cells as rows
        # Values: normalized log1p expression

        n_cells = X.shape[0]
        n_genes = len(self.genes)
        
        # If X is the in distribution Testset, use the existing global binning
        if self.baseline_df is not None and X is self.baseline_df:
            all_counts = self.adata_test.layers["X_binned"]
        # Fallback for Out of Distribution datasets: Create binning
        else:
            # Align genes to training order, zero-pad missing
            X_aligned = np.zeros((n_cells, n_genes))

            train_gene_to_idx = {g: i for i, g in enumerate(self.genes)}
            for g in X.columns:
                if g in train_gene_to_idx:
                    X_aligned[:, train_gene_to_idx[g]] = X[g].values
                else:
                    # Tmp test print
                    print(f"Gene {g} not found!")
            

            # Bin the data
            adata_tmp = sc.AnnData(X_aligned)
            preprocessor = Preprocessor(
                use_key="X",
                filter_gene_by_counts=False,
                filter_cell_by_counts=False,
                normalize_total=None,
                log1p=False,
                subset_hvg=None,
                binning=self.n_bins,
                result_binned_key="X_binned",
            )
            preprocessor(adata_tmp, batch_key=None)
            all_counts = adata_tmp.layers["X_binned"]

        if issparse(all_counts):
            all_counts = all_counts.toarray()

        # Tokenize
        tokenized = tokenize_and_pad_batch(
            all_counts,
            self.gene_ids,
            max_len=self.max_seq_len,
            vocab=self.vocab,
            pad_token=self.pad_token,
            pad_value=self.pad_value,
            append_cls=True,
            include_zero_gene=True,
        )

        # Don't copy samples directly on the GPU, batch them to save VRAM
        all_gene_ids_pt = tokenized["genes"]
        all_values_pt = tokenized["values"].float()

        batch_size = config.batch_size
        predictions = []

        self.model.eval()

        # Forward pass with CLS head – scGPT predicts cell types directly
        with torch.no_grad(), torch.cuda.amp.autocast(enabled=True):
            # Batch samples to save VRAM
            for start in range(0, n_cells, batch_size):
                end = min(start + batch_size, n_cells)

                gene_ids = all_gene_ids_pt[start:end].to(self.device)
                values = all_values_pt[start:end].to(self.device)

                src_key_padding_mask = gene_ids.eq(self.vocab[self.pad_token])

                # Use dummy batch labels (0) since DSBN expects them during forward
                dummy_batch_labels = torch.zeros(
                    gene_ids.size(0),
                    dtype=torch.long,
                    device=self.device,
                )

                output_dict = self.model(
                    gene_ids,
                    values,
                    src_key_padding_mask=src_key_padding_mask,
                    batch_labels=dummy_batch_labels,
                    CLS=True,
                )

                predictions.append(
                    output_dict["cls_output"].argmax(dim=1).cpu()
                )

        predictions = torch.cat(predictions).numpy()

        # Convert internal class IDs back to original labels
        predictions = np.array(
            [self.id2label[int(pred)] for pred in predictions]
        )

        return predictions



# --- Create predictor (no external classifier – scGPT cls_decoder) ---
scgpt_predictor = ScGPTPredictor(
    model=best_model,
    vocab=vocab,
    gene_ids=gene_ids,
    genes=genes,
    n_bins=config.n_bins,
    n_hvg=n_hvg,
    device=device,
    max_seq_len=max_seq_len,
    id2label=id2label,
    baseline_df=X_test_robustness,
    adata_test=adata_test,
)

# Tmp prints
print("--- Label to ID Mapping ---")
print(f"label2id: {label2id}")
print(f"id2label: {id2label}")

print("--- Comparison of gene ordering in train and test ---")
print(f"train: {genes[:20]}")
print(f"adata test: {adata_test.var['gene_name'].tolist()[:20]}")
print(f"df test: {list(X_test_robustness.columns[:20])}")

print("--- Samples per class in train and valid split ---")
print("Train split:")
classes, counts = np.unique(train_celltype_labels, return_counts=True)
for c, n in zip(classes, counts):
    print(f"{id2label[c]} ({c}): {n}")

print("\nValidation split:")
classes, counts = np.unique(valid_celltype_labels, return_counts=True)
for c, n in zip(classes, counts):
    print(f"{id2label[c]} ({c}): {n}")


# --- Evaluate on test data ---
y_pred = scgpt_predictor.predict(X_test_robustness)
print("\n--- EVALUATION AUF DEN TESTDATEN ---")
acc = accuracy_score(y_test_robustness, y_pred)
f1_macro = f1_score(y_test_robustness, y_pred, average="macro")
print(f"Test Accuracy: {acc:.4f}")
print(f"Macro F1: {f1_macro:.4f}")
logger.info(f"Test Accuracy: {acc:.4f}, Macro F1: {f1_macro:.4f}")

print("\n--- Confusion Matrix ---")
#Order of the classes
labels = list(label2id.keys())
cm = confusion_matrix(
    y_test_robustness,
    y_pred,
    labels=labels,
)
cm_df = pd.DataFrame(
    cm,
    index=labels,
    columns=labels,
)
cm_df.to_csv("confusion_matrix.csv")
print(cm_df)

print("\n--- Normalized Confusion Matrix ---")
cm_norm = cm.astype(float) / cm.sum(axis=1, keepdims=True)
cm_norm_df = pd.DataFrame(
    cm_norm,
    index=labels,
    columns=labels,
)
cm_norm_df.to_csv("confusion_matrix_normalized.csv")
print(cm_norm_df.round(3))

# --- Robustness Evaluation ---
print("\n--- Robustness Evaluation ---")
with open("master_feature_importance_interleaved_marker_genes.pkl", "rb") as f:
    feature_importance = pickle.load(f)

# For fair comparison filter only genes from feoature_importance that are in test dataset
test_genes = set(X_test_robustness.columns)

if isinstance(feature_importance, dict):
    # Wenn es ein Dictionary ist (z.B. {'GEN1': 0.5, 'GEN2': 0.1})
    feature_importance = {gene: score for gene, score in feature_importance.items() if gene in test_genes}
    print(f"Feature Importance (Dict) filtered. Remaining Genes: {len(feature_importance)}")

elif isinstance(feature_importance, pd.Series):
    # Wenn es eine Pandas Series ist (Index = Genname)
    feature_importance = feature_importance[feature_importance.index.isin(test_genes)]
    print(f"Feature Importance (Series) filtered. Remaining Genes: {len(feature_importance)}")

elif isinstance(feature_importance, pd.DataFrame):
    # Wenn es ein Dataframe ist (entweder Genname im Index oder in einer Spalte 'gene')
    if 'gene' in feature_importance.columns:
        feature_importance = feature_importance[feature_importance['gene'].isin(test_genes)]
    else:
        feature_importance = feature_importance[feature_importance.index.isin(test_genes)]
    print(f"Feature Importance (DataFrame) filtered. Remaining genes: {len(feature_importance)}")


test_robustness(
    scgpt_predictor,
    X_test_robustness,
    y_test_robustness,
    #labels="scumi-annotation",
    ood_dataset_path="data/humancellatlas/5f29c29a-51c6-435c-8ff0-2b2a9d05ebee/BL_standard_design_annotated.h5ad",
    feature_importances=feature_importance,
)

# %%
#artifact = wandb.Artifact(f"best_model", type="model")
#artifact.add_file(str(save_dir / "best_model.pt"))
#run.log_artifact(artifact)

run.finish()
wandb.finish()
gc.collect()
