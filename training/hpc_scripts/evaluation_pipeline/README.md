# CLACELL evaluation pipeline

Config-driven pipeline for evaluating hierarchical CLACELL models.
It keeps the existing `test_robustness_higher_dropout.py` and
`preprocess_data.py` untouched and only orchestrates preprocessing, tuning,
fitting and evaluation.

## Directory layout

```
submit_prepare.sh          # Slurm template (single job)
submit_features.sh         # Slurm template (array, one task per seed)
submit_tune.sh             # Slurm template (array)
submit_run.sh              # Slurm template (array)
submit_aggregate.sh        # Slurm template (single job)
evaluation_pipeline/
  configs/experiment.yaml  # <-- the only file to edit
  orchestrate.py           # submit stages / dry-run / status
  run_task.py              # one task (prepare|features|tune|run|aggregate|plan|status)
  pipeline/
    config.py              # config validation
    prepare.py             # preprocessing, cache, split, hierarchy
    features.py            # RF and LinearSVC ranking functions
    features_stage.py      # persistent per-seed feature rankings
    tuning.py              # fixed hyperparameters per dataset/model/node
    run.py                 # fit + test_robustness + technical metrics
    aggregate.py           # combined_result.csv + summary.csv
    hierarchy.py           # generic HierarchicalCascadeClassifier
    models/                # autoencoder, conditional AE, custom ensembles,
                            # reference adapters
```

## One-time configuration on the HPC

The submit scripts use the same environment as
`submit_hierarchical_custom_ensemble_rf_spatial_breast_run_multiple_stacking.sh`:

```bash
source /apps/python/3.12-conda/etc/profile.d/conda.sh
conda activate test_clacell
```

If the environment name changes, edit those two lines in the five
`submit_*.sh` files.

The pipeline itself needs `PyYAML` (`pip install pyyaml` if it is missing). The
SingleR reference additionally needs the `singler` package; it is imported
lazily and only when that model is enabled. See `requirements.txt`.

## Pilot workflow

The config is already set to:

- dataset: `breast`
- models: `autoencoder_linsvc`, `custom_ensemble_rf_stacking`
- seeds: `0..9` (10 runs, matching the old breast script)
- `tuning_per_seed: true` (one tuning job per run/seed, matching the old script)
- fixed marker-gene ranking for `test_robustness` via
  `feature_importance.robustness_file`, as in the old script

Run:

```bash
cd /path/to/hpc_scripts

# 1. Preprocess once and build the cache (also validates the config/paths)
python evaluation_pipeline/orchestrate.py \
  --config evaluation_pipeline/configs/experiment.yaml --stage prepare

# 2. Build the task manifests from the cache (hierarchy is now known)
python evaluation_pipeline/orchestrate.py \
  --config evaluation_pipeline/configs/experiment.yaml --stage plan

# 3. Compute and persist both feature rankings once per seed
python evaluation_pipeline/orchestrate.py \
  --config evaluation_pipeline/configs/experiment.yaml --stage features

# 4. Tune every model × hierarchy node once
python evaluation_pipeline/orchestrate.py \
  --config evaluation_pipeline/configs/experiment.yaml --stage tune

# 5. Fit/evaluate the selected seeds
python evaluation_pipeline/orchestrate.py \
  --config evaluation_pipeline/configs/experiment.yaml --stage run

# 6. Aggregate
python evaluation_pipeline/orchestrate.py \
  --config evaluation_pipeline/configs/experiment.yaml --stage aggregate
```

Or run the whole chain and block until it finishes:

```bash
python evaluation_pipeline/orchestrate.py \
  --config evaluation_pipeline/configs/experiment.yaml --stage all
```

`--dry-run` prints the `sbatch` commands without submitting. `--stage status`
shows done/missing features, tuning and run tasks.

## What the stages do

### prepare (1 job)

1. Loads the raw `.h5ad`.
2. Applies label filters and the configured donor split.
3. Runs QC, optional Scrublet, normalization and log1p. Gene filtering and
   HVG selection are fit on the training split only and then applied to the
   test split, so the test data cannot influence the training features. Genes
   missing from the test split are filled with zeros, and the test matrix uses
   the same gene order as the training matrix.
4. Builds `hierarchy.json` (coarse labels, fine classes per coarse group,
   leaf nodes).
5. Writes the cache and `_SUCCESS`.

The cache is reused across all later model/seed jobs. It contains:

```
<cache_root>/<dataset>/
  prepared_train.h5ad / prepared_test.h5ad
  X_train.npy / X_test.npy          # preprocessing dtype, cells x genes
  genes.json
  obs_train.pkl / obs_test.pkl      # donor, coarse, fine, ...
  hierarchy.json
  prepare_meta.json                 # preprocessing time, RAM, cache key, versions
  scaler.pkl                        # written by features, only if a scaled custom ensemble is active
  _SUCCESS
```

A cache hit is detected via `_SUCCESS` plus a hash of the dataset config, raw
file fingerprint, preprocessing options and hierarchy options. If you change
the config or the raw file, prepare rebuilds the cache. `prepare_meta.json` is
required for a valid cache; if it is missing, the downstream stages fail
instead of silently using 0.0 as preprocessing time. When
`experiment.export_scgpt` is enabled, the export runs inside prepare and its
wall time is included in `preprocessing_time_min` (also when an existing cache
had to be completed with the export). Caches written by older versions may not
contain the export time; rerun prepare once if you need that value corrected.

### features (array: one task per seed)

Computes the configured ranking(s) on the training split with the **run seed**
and persists them permanently:

```
<cache_root>/<dataset>/features/seed_<seed>/
  feature_importance_randomforest.pkl/.csv
  feature_importance_linearsvc.pkl/.csv
  method_randomforest.json
  method_linearsvc.json
  features_meta.json
  _SUCCESS
```

All models with the same seed read exactly these two rankings; no model
recomputes them. If any active custom ensemble uses `params.scale: true`, the
features stage additionally fits one **dataset-wide**
`StandardScaler(with_mean=False)` on the full training matrix and stores it once
at `<cache_root>/<dataset>/scaler.pkl`. All seeds and all tuning/run tasks use
this same scaler; the per-seed features directories only contain the
`feature_importance_<method>_scaled.pkl` rankings computed with it.
Per-method markers make this resumable: if a job is interrupted after the
RandomForest ranking, a later job reuses it and only computes the missing
LinearSVC ranking. `features_meta.json` stores both
`feature_selection_time_min` (sum of the actual per-method compute times) and
`total_wall_time_min` (cumulative wall time of the features task across resumed
invocations, so a cache-hit restart does not shrink the reported time). The
ranking passed to `test_robustness` is controlled by
`feature_importance.robustness` (default `linearsvc`).

### tune (array: one task per model × node)

Hyperparameters are searched **once** per dataset, model and hierarchy node:

- `coarse` node: all training cells.
- `fine:<coarse_label>` node: only the cells of that coarse label.

The result is `best_params.json` plus `tuning_meta.json` (tuning wall time, CV,
`Avg_Time_per_Iteration_Sec`, peak RAM). With `experiment.tuning_per_seed:
true` there is one tuning task per model × node × seed, matching the old breast
script. With `false` the parameters are tuned once and reused for all seeds.
The run stage only loads the parameters; it does not tune.

For the custom ensembles the internal gene ranking is the one you specified:

- `custom_ensemble_linsvc_*` uses the **RandomForest** ranking.
- `custom_ensemble_rf_*` uses the **LinearSVC** ranking.

`combine` selects `stacking` (optionally with `passthrough: true`) or soft
`voting`. Set `params.scale: true` to use the single dataset-wide
`StandardScaler(with_mean=False)` fitted on the full training split. It is
stored once at `<cache_root>/<dataset>/scaler.pkl`, shared by every seed and by
tuning, and applied once to `X_train`/`X_test` before the ensemble; the custom
ensemble itself does not scale. The catalogue contains all combinations of base
estimator, combine mode and scaling.

The configured rankings are persisted per seed by the features stage. The
pipeline assumes that fine labels form a consistent hierarchy; ensure that each
fine label has exactly one intended coarse parent in your annotation. For the
breast pilot, `feature_importance.robustness_file` points to the same Pegasus
marker-gene pickle as the old script; adjust the path if needed.

### run (array: one task per model × seed)

For hierarchical models, one task:

1. fits the coarse model on all training cells,
2. fits one fine model per coarse label on the coarse subset,
3. routes test cells coarse → fine,
4. calls `test_robustness` separately for coarse and fine.

This is the same functional behaviour as the previous
`HierarchicalCascadeClassifier`.

Reference models (`singler`, `celltypist`) are flat baselines: they train one
model on coarse labels and a separate model on fine labels. They are not put
into the hierarchy.

Each run writes:

```
<output_root>/<experiment>/<dataset>/results/<model>/coarse/result_<i>.csv
<output_root>/<experiment>/<dataset>/results/<model>/fine/result_<i>.csv
```

and a `_SUCCESS_run_<i>` marker per level. If a job hits the walltime, only the
current seed is lost; finished seeds are skipped on resubmission.

### aggregate (1 job)

Reads every completed `result_<i>.csv`, writes the usual
`combined_result.csv` (raw runs + mean/std + `mean +- std`) per model/level,
plus `aggregate/summary.csv` and `aggregate/run_status.csv`.

## Technical metrics

The time metrics are **attributed compute times**, not wall-clock times of the
whole experiment. The stages run as separate Slurm jobs and can run in parallel
(`--array ...%N`), so queue time, job startup and parallelism are not included.
For comparing the compute cost of methods this is the intended metric; for
"when did the experiment finish" use the Slurm accounting data instead.

The existing metrics are preserved:

- `Training_Time_Min`
- `Inference_Evaluation_Time_Min`
- `Total_Pipeline_Time_Min` (attributed sum of preprocessing + features task
  incl. FI computation + tuning + cache/FI loading + training + evaluation;
  autoencoders exclude the features task, see below)
- `Run_With_Setup_Time_Min` (the same without dataset-wide preprocessing)
- `Peak_RAM_GB`
- `Autoencoder_Epochs`
- `Avg_Time_per_Iteration_Sec`

Additional metrics are added to the same 4-level MultiIndex:

- `Preprocessing_Time_Min` (once per dataset, copied into every run row)
- `Feature_Selection_Time_Min` (sum of the actual per-method FI compute times)
- `Feature_Task_Time_Min` (full features task including cache loading/writing;
  cumulative across resumed feature jobs)
- `Hyperparameter_Tuning_Time_Min` (hierarchical models: coarse node plus all
  fine nodes, identical in both level rows; flat models: the node of the
  respective level)
- `Preprocessing_Peak_RAM_GB`
- `Tuning_Peak_RAM_GB` (max over the tuning nodes attributed to the row)

The autoencoder and conditional-autoencoder families do not use the RF/LinearSVC
feature rankings for feature selection. For these models the two feature-time
columns are omitted and `Run_With_Setup_Time_Min` / `Total_Pipeline_Time_Min`
exclude the features task, so they are not charged for a stage they do not
consume.

For hierarchical models the shared costs describe the complete cascade and are
therefore identical in the coarse and the fine row:

- `Training_Time_Min` = coarse fit + all fine fits.
- `Hyperparameter_Tuning_Time_Min` = coarse node + all fine nodes.
- `Tuning_Peak_RAM_GB` = max over coarse and all fine nodes.
- `Avg_Time_per_Iteration_Sec` = mean over coarse and all fine nodes.
- `Run_With_Setup_Time_Min` / `Total_Pipeline_Time_Min` = complete run task
  (both fits and both evaluations) plus the complete tuning cost.

Only `Inference_Evaluation_Time_Min` stays level-specific: the coarse row times
the coarse evaluation, the fine row times the fine evaluation. The fine
evaluation routes every perturbed test matrix through the coarse model again,
so it also contains coarse inference time. `Run_With_Setup_Time_Min` and
`Total_Pipeline_Time_Min` still include both evaluations; a single row is
therefore larger than the sum of its displayed training, tuning and evaluation
columns by the other level's evaluation time (plus feature/setup overhead). The
coarse and fine rows must not be added together.

For flat models (`singler`, `celltypist`) one run task fits and evaluates both
levels. `Run_With_Setup_Time_Min` and `Total_Pipeline_Time_Min` therefore use
the complete task wall time for both the coarse and the fine row; they are not
per-level times. `Training_Time_Min`, `Hyperparameter_Tuning_Time_Min` and
`Inference_Evaluation_Time_Min` remain level-specific.

Even when prepare/features/tune are served from cache, the persisted timings are
read from `prepare_meta.json`, `features_meta.json` and `tuning_meta.json` and
attached to every run CSV. If a required timing field is missing, the run stage
fails with a clear error instead of silently writing 0.0.

`test_robustness_higher_dropout.py` is called with
`seed=eval_seed_base + run_index`; the random dropout therefore uses a
reproducible seed and all models in the same run see the same perturbation
draws. The log line `No out-of-distribution dataset path provided. Skipping ...`
is expected for the non-blood datasets, which have only a train/test split.

The conditional autoencoder uses the real donor one-hot matrix during
training/tuning and the same all-zero neutral donor vector at inference as the
old implementation. The old LinearSVC conditional wrapper did not apply its
scaler at inference; this pipeline applies the scaler consistently for both
LinearSVC and RandomForest heads.

## Extending after the pilot

Only edit `experiment` in `configs/experiment.yaml`:

```yaml
experiment:
  dataset: tonsil
  models:
    - autoencoder_linsvc
    - autoencoder_rf
    - conditional_autoencoder_linsvc
    - conditional_autoencoder_rf
    - custom_ensemble_linsvc_stacking
    - custom_ensemble_rf_stacking
    - singler
    - celltypist
  seeds: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Then run the same stages. Existing prepare/features/tune results are reused; only the
new model/node/seed tasks are executed.

To switch datasets, change `experiment.dataset` to `tonsil`, `ovary` or
`pancreas` and fill the corresponding catalogue entry if needed. Each dataset
has its own cache and result tree.

## Reference models

- `singler`: sklearn-compatible `FastSingleRClassifier` from the old script.
- `celltypist`: uses the `CellTypistWrapper`/BayesSearchCV implementation from
  `train_celltypist_bayessearch.py`; it tunes `C`, `alpha`, `use_SGD`,
  `mini_batch`, `balance_cell_type` and `feature_selection` on the cached
  expression and predicts through `celltypist.annotate`.
- `scgpt`: external GPU model. Set `experiment.export_scgpt: true` (or run
  `python evaluation_pipeline/run_task.py export-scgpt --config ...`) to write
  `scgpt_input.h5ad` with raw counts and standard columns
  (`Donor`, `scumi_clean_coarse`, `scumi_clean_fine_grained`). Then run
  `finetune_integration_adjusted.py` on the GPU cluster with that file. The
  script has only small, backwards-compatible hooks:
  `SCGPT_LABEL_COL` (coarse or fine labels), `SCGPT_FEATURE_IMPORTANCE` (the
  ranking produced by the features stage), and `SCGPT_RESULT_CSV` (writes the standard
  robustness result CSV). The hard-coded OOD blood datasets were set to `None`
  for the non-blood evaluation; restore them only for blood runs. Example:
  `SCGPT_LABEL_COL=scumi_clean_fine_grained SCGPT_FEATURE_IMPORTANCE=<cache>/features/seed_0/feature_importance_linearsvc.pkl SCGPT_RESULT_CSV=scgpt_fine.csv python finetune_integration_adjusted.py`.
  The `h5ad_path` and `donor_train`/`donor_test` in that script's
  `hyperparameter_defaults` still have to be set for the target dataset; the
  export manifest (`scgpt_export.json`) contains the donor lists.

## Debugging

Every task logs a header with dataset/model/node/seed. On failure:

- the full traceback is printed to stdout/stderr (Slurm `.out`/`.err`),
- a JSON record is written under
  `<output_root>/<experiment>/<dataset>/failures/`,
- the log line starts with `FAILED stage=... dataset=... model=...`.

Common causes:

- `Missing tuned parameters ...` → run the tune stage first.
- `Preprocessing cache is missing ...` → run prepare first.
- `Feature rankings for seed=... are missing ...` → run the features stage first.
- `Donors missing from dataset ...` → the donor split does not match `obs`.
- `min class count is 1` → tuning is skipped for that node and the default head
  parameters are used; the run still works.
