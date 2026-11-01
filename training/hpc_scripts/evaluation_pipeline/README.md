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

The submit scripts activate a Python environment. Override the default path if
needed:

```bash
export PIPELINE_VENV=/home/hpc/iwbn/iwbn133h/test_bayes/bin/activate #TODO
```

If your environment does not export `PIPELINE_VENV` to the job (because the
templates use `--export=NONE`), edit the default fallback in the five
`submit_*.sh` files. They default to
`/home/hpc/iwbn/iwbn133h/test_bayes/bin/activate`. #TODO

The pipeline itself needs `PyYAML` (`pip install pyyaml` if it is missing). The
SingleR reference additionally needs the `singler` package; it is imported
lazily and only when that model is enabled. See `requirements.txt`.

## Pilot workflow

The config is already set to:

- dataset: `tonsil`
- models: `autoencoder_linsvc`, `custom_ensemble_rf_stacking`
- seeds: `0..9` (10 runs; reduce to `[0, 1]` for a quick smoke test)

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
3. Runs QC, optional Scrublet, normalization, log1p and HVG selection.
4. Builds `hierarchy.json` (coarse labels, fine classes per coarse group,
   leaf nodes).
5. Writes the cache and `_SUCCESS`.

The cache is reused across all later model/seed jobs. It contains:

```
<cache_root>/<dataset>/
  prepared.h5ad
  X_train.npy / X_test.npy          # float32, cells x genes
  genes.json
  obs_train.pkl / obs_test.pkl      # donor, coarse, fine, ...
  hierarchy.json
  prepare_meta.json                 # preprocessing time, RAM, cache key, versions
  _SUCCESS
```

A cache hit is detected via `_SUCCESS` plus a hash of the dataset config, raw
file fingerprint, preprocessing options and hierarchy options. If you change
the config or the raw file, prepare rebuilds the cache.

### features (array: one task per seed)

Computes both rankings on the training split with the **run seed** and persists
them permanently:

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
recomputes them. Per-method markers make this resumable: if a job is interrupted
after the RandomForest ranking, a later job reuses it and only computes the
missing LinearSVC ranking. The ranking passed to `test_robustness` is controlled
by `feature_importance.robustness` (default `linearsvc`).

### tune (array: one task per model × node)

Hyperparameters are searched **once** per dataset, model and hierarchy node:

- `coarse` node: all training cells.
- `fine:<coarse_label>` node: only the cells of that coarse label.

The result is `best_params.json` plus `tuning_meta.json` (tuning wall time, CV,
`Avg_Time_per_Iteration_Sec`, peak RAM). The 10 runs only load these fixed
parameters; they do not tune again.

For the custom ensembles the internal gene ranking is the one you specified:

- `custom_ensemble_linsvc_stacking` uses the **RandomForest** ranking.
- `custom_ensemble_rf_stacking` uses the **LinearSVC** ranking.

Both rankings are persisted per seed by the features stage. The pipeline assumes
that fine labels form a consistent hierarchy; ensure that each fine label has
exactly one intended coarse parent in your annotation.

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
<output_root>/<experiment>/<dataset>/results/<model>/coarse/result_<i>.csv #TODO
<output_root>/<experiment>/<dataset>/results/<model>/fine/result_<i>.csv #TODO
```

and a `_SUCCESS_run_<i>` marker per level. If a job hits the walltime, only the
current seed is lost; finished seeds are skipped on resubmission.

### aggregate (1 job)

Reads every completed `result_<i>.csv`, writes the usual
`combined_result.csv` (raw runs + mean/std + `mean +- std`) per model/level,
plus `aggregate/summary.csv` and `aggregate/run_status.csv`.

## Technical metrics

The existing metrics are preserved:

- `Training_Time_Min`
- `Inference_Evaluation_Time_Min`
- `Total_Pipeline_Time_Min` (training + evaluation, old meaning)
- `Run_Task_Time_Min` (cache load + feature-ranking load + training +
  evaluation of the whole run task)
- `Peak_RAM_GB`
- `Autoencoder_Epochs`
- `Avg_Time_per_Iteration_Sec`

New stage metrics are added to the same 4-level MultiIndex:

- `Preprocessing_Time_Min` (once per dataset, copied into every run row)
- `Feature_Selection_Time_Min` (sum of the actual per-method FI compute times)
- `Feature_Task_Time_Min` (full features task including cache loading/writing)
- `Hyperparameter_Tuning_Time_Min` (coarse node for coarse rows; sum of fine
  nodes for fine rows)
- `Preprocessing_Peak_RAM_GB`
- `Tuning_Peak_RAM_GB`
- `End_To_End_Time_Min` (preprocessing + full features task + tuning + full run
  task). `Total_Pipeline_Time_Min` keeps its old meaning (training +
  evaluation).

Even when prepare/features/tune are served from cache, the persisted timings are
read from `prepare_meta.json`, `features_meta.json` and `tuning_meta.json` and
attached to every run CSV.

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

To switch datasets, change `experiment.dataset` to `breast`, `ovary` or
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
