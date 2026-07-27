### Starting TaskPrologue of job 11995956 on w2520 at Sat Jun 27 16:19:27 CEST 2026
#   SLURM_JOB_NODELIST=w2520
#   SLURM_JOB_NUM_NODES=1
#   SLURM_NTASKS=1
#   SLURM_NPROCS=1
#   SLURM_TASKS_PER_NODE=1
#   SLURM_JOB_CPUS_PER_NODE=32
#   SLURM_EXPORT_ENV=NONE
Running on cores 0-31 with govenor powersave
### Finished TaskPrologue
AnnData object with n_obs × n_vars = 27620 × 36473
    obs: 'Organ', 'Donor', 'Chemistry', 'Cell_category', 'Predicted_labels_CellTypist', 'Majority_voting_CellTypist', 'Majority_voting_CellTypist_high', 'Manually_curated_celltype', 'Sex', 'Age_range', 'n_genes_by_counts', 'log1p_n_genes_by_counts', 'total_counts', 'log1p_total_counts', 'pct_counts_in_top_50_genes', 'pct_counts_in_top_100_genes', 'pct_counts_in_top_200_genes', 'pct_counts_in_top_500_genes', 'total_counts_mt', 'log1p_total_counts_mt', 'pct_counts_mt', 'total_counts_ribo', 'log1p_total_counts_ribo', 'pct_counts_ribo', 'total_counts_hb', 'log1p_total_counts_hb', 'pct_counts_hb', 'n_genes', 'doublet_score', 'predicted_doublet', 'scumi-annotation'
    var: 'mt', 'ribo', 'hb', 'n_cells_by_counts', 'mean_counts', 'log1p_mean_counts', 'pct_dropout_by_counts', 'total_counts', 'log1p_total_counts'
    uns: 'Age_range_colors', 'Sex_colors', 'scrublet'
    obsm: 'X_umap'
    layers: 'counts'
Before filtering highly variable genes ---
AnnData object with n_obs × n_vars = 27573 × 36473
    obs: 'Organ', 'Donor', 'Chemistry', 'Cell_category', 'Predicted_labels_CellTypist', 'Majority_voting_CellTypist', 'Majority_voting_CellTypist_high', 'Manually_curated_celltype', 'Sex', 'Age_range', 'n_genes_by_counts', 'log1p_n_genes_by_counts', 'total_counts', 'log1p_total_counts', 'pct_counts_in_top_50_genes', 'pct_counts_in_top_100_genes', 'pct_counts_in_top_200_genes', 'pct_counts_in_top_500_genes', 'total_counts_mt', 'log1p_total_counts_mt', 'pct_counts_mt', 'total_counts_ribo', 'log1p_total_counts_ribo', 'pct_counts_ribo', 'total_counts_hb', 'log1p_total_counts_hb', 'pct_counts_hb', 'n_genes', 'doublet_score', 'predicted_doublet', 'scumi-annotation'
    var: 'mt', 'ribo', 'hb', 'n_cells_by_counts', 'mean_counts', 'log1p_mean_counts', 'pct_dropout_by_counts', 'total_counts', 'log1p_total_counts'
    uns: 'Age_range_colors', 'Sex_colors', 'scrublet', 'log1p'
    obsm: 'X_umap'
    layers: 'counts'
After filtering highly variable genes ---
AnnData object with n_obs × n_vars = 27573 × 10000
    obs: 'Organ', 'Donor', 'Chemistry', 'Cell_category', 'Predicted_labels_CellTypist', 'Majority_voting_CellTypist', 'Majority_voting_CellTypist_high', 'Manually_curated_celltype', 'Sex', 'Age_range', 'n_genes_by_counts', 'log1p_n_genes_by_counts', 'total_counts', 'log1p_total_counts', 'pct_counts_in_top_50_genes', 'pct_counts_in_top_100_genes', 'pct_counts_in_top_200_genes', 'pct_counts_in_top_500_genes', 'total_counts_mt', 'log1p_total_counts_mt', 'pct_counts_mt', 'total_counts_ribo', 'log1p_total_counts_ribo', 'pct_counts_ribo', 'total_counts_hb', 'log1p_total_counts_hb', 'pct_counts_hb', 'n_genes', 'doublet_score', 'predicted_doublet', 'scumi-annotation'
    var: 'mt', 'ribo', 'hb', 'n_cells_by_counts', 'mean_counts', 'log1p_mean_counts', 'pct_dropout_by_counts', 'total_counts', 'log1p_total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'Age_range_colors', 'Sex_colors', 'scrublet', 'log1p', 'hvg'
    obsm: 'X_umap'
    layers: 'counts'
['A36' 'A35' '637C' 'D503']
['621B' 'D496']
Fitting 3 folds for each of 50 candidates, totalling 150 fits
[CV 1/3; 1/50] START C=0.27631198311255345, alpha=0.00011524748205692024, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 1/50] END C=0.27631198311255345, alpha=0.00011524748205692024, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.784 total time=  25.8s
[CV 2/3; 1/50] START C=0.27631198311255345, alpha=0.00011524748205692024, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 1/50] END C=0.27631198311255345, alpha=0.00011524748205692024, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.990 total time=  28.1s
[CV 3/3; 1/50] START C=0.27631198311255345, alpha=0.00011524748205692024, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 1/50] END C=0.27631198311255345, alpha=0.00011524748205692024, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.962 total time=  23.4s
[CV 1/3; 2/50] START C=0.1535930033018052, alpha=0.0004456835720250792, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 2/50] END C=0.1535930033018052, alpha=0.0004456835720250792, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.771 total time=  36.4s
[CV 2/3; 2/50] START C=0.1535930033018052, alpha=0.0004456835720250792, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 2/50] END C=0.1535930033018052, alpha=0.0004456835720250792, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.991 total time=  28.4s
[CV 3/3; 2/50] START C=0.1535930033018052, alpha=0.0004456835720250792, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 2/50] END C=0.1535930033018052, alpha=0.0004456835720250792, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.955 total time=  28.2s
[CV 1/3; 3/50] START C=0.5220237551278456, alpha=0.0010797962840842894, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 1/3; 3/50] END C=0.5220237551278456, alpha=0.0010797962840842894, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.771 total time=  39.8s
[CV 2/3; 3/50] START C=0.5220237551278456, alpha=0.0010797962840842894, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 2/3; 3/50] END C=0.5220237551278456, alpha=0.0010797962840842894, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.989 total time=  43.7s
[CV 3/3; 3/50] START C=0.5220237551278456, alpha=0.0010797962840842894, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 3/3; 3/50] END C=0.5220237551278456, alpha=0.0010797962840842894, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.947 total time=  39.0s
[CV 1/3; 4/50] START C=1.3070369229046288, alpha=0.005805000350398745, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 4/50] END C=1.3070369229046288, alpha=0.005805000350398745, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.776 total time=  56.4s
[CV 2/3; 4/50] START C=1.3070369229046288, alpha=0.005805000350398745, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 4/50] END C=1.3070369229046288, alpha=0.005805000350398745, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.991 total time=  41.1s
[CV 3/3; 4/50] START C=1.3070369229046288, alpha=0.005805000350398745, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 4/50] END C=1.3070369229046288, alpha=0.005805000350398745, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.952 total time=  40.8s
[CV 1/3; 5/50] START C=0.6748980105538499, alpha=0.00021735027415085685, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 5/50] END C=0.6748980105538499, alpha=0.00021735027415085685, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.774 total time=  27.1s
[CV 2/3; 5/50] START C=0.6748980105538499, alpha=0.00021735027415085685, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 5/50] END C=0.6748980105538499, alpha=0.00021735027415085685, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.991 total time=  27.3s
[CV 3/3; 5/50] START C=0.6748980105538499, alpha=0.00021735027415085685, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 5/50] END C=0.6748980105538499, alpha=0.00021735027415085685, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.954 total time=  27.1s
[CV 1/3; 6/50] START C=0.07208697892411661, alpha=0.0014948242987486125, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 6/50] END C=0.07208697892411661, alpha=0.0014948242987486125, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.773 total time=  39.9s
[CV 2/3; 6/50] START C=0.07208697892411661, alpha=0.0014948242987486125, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 6/50] END C=0.07208697892411661, alpha=0.0014948242987486125, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.991 total time=  41.0s
[CV 3/3; 6/50] START C=0.07208697892411661, alpha=0.0014948242987486125, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 6/50] END C=0.07208697892411661, alpha=0.0014948242987486125, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.965 total time=  40.8s
[CV 1/3; 7/50] START C=0.13671638953235796, alpha=0.007021321523239415, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 1/3; 7/50] END C=0.13671638953235796, alpha=0.007021321523239415, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.773 total time=  28.3s
[CV 2/3; 7/50] START C=0.13671638953235796, alpha=0.007021321523239415, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 2/3; 7/50] END C=0.13671638953235796, alpha=0.007021321523239415, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.992 total time=  33.3s
[CV 3/3; 7/50] START C=0.13671638953235796, alpha=0.007021321523239415, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 3/3; 7/50] END C=0.13671638953235796, alpha=0.007021321523239415, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.943 total time=  33.7s
[CV 1/3; 8/50] START C=0.026201832613427577, alpha=0.0004096100701077185, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 1/3; 8/50] END C=0.026201832613427577, alpha=0.0004096100701077185, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.769 total time=  29.1s
[CV 2/3; 8/50] START C=0.026201832613427577, alpha=0.0004096100701077185, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 2/3; 8/50] END C=0.026201832613427577, alpha=0.0004096100701077185, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.993 total time=  32.4s
[CV 3/3; 8/50] START C=0.026201832613427577, alpha=0.0004096100701077185, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 3/3; 8/50] END C=0.026201832613427577, alpha=0.0004096100701077185, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.941 total time=  31.5s
[CV 1/3; 9/50] START C=0.019669368084071367, alpha=0.0028076649696810933, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 9/50] END C=0.019669368084071367, alpha=0.0028076649696810933, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.762 total time=  35.3s
[CV 2/3; 9/50] START C=0.019669368084071367, alpha=0.0028076649696810933, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 9/50] END C=0.019669368084071367, alpha=0.0028076649696810933, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.990 total time=  36.5s
[CV 3/3; 9/50] START C=0.019669368084071367, alpha=0.0028076649696810933, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 9/50] END C=0.019669368084071367, alpha=0.0028076649696810933, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.928 total time=  36.1s
[CV 1/3; 10/50] START C=1.0944266667193172, alpha=0.0023980316864903686, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 1/3; 10/50] END C=1.0944266667193172, alpha=0.0023980316864903686, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.768 total time=  33.7s
[CV 2/3; 10/50] START C=1.0944266667193172, alpha=0.0023980316864903686, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 2/3; 10/50] END C=1.0944266667193172, alpha=0.0023980316864903686, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.991 total time=  41.3s
[CV 3/3; 10/50] START C=1.0944266667193172, alpha=0.0023980316864903686, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 3/3; 10/50] END C=1.0944266667193172, alpha=0.0023980316864903686, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.948 total time=  39.5s
[CV 1/3; 11/50] START C=0.07584110118156318, alpha=0.007075165313007013, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 11/50] END C=0.07584110118156318, alpha=0.007075165313007013, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.794 total time=  40.3s
[CV 2/3; 11/50] START C=0.07584110118156318, alpha=0.007075165313007013, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 11/50] END C=0.07584110118156318, alpha=0.007075165313007013, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.991 total time=  41.2s
[CV 3/3; 11/50] START C=0.07584110118156318, alpha=0.007075165313007013, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 11/50] END C=0.07584110118156318, alpha=0.007075165313007013, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.967 total time=  40.9s
[CV 1/3; 12/50] START C=0.023384996999775014, alpha=0.00021262656405097302, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 12/50] END C=0.023384996999775014, alpha=0.00021262656405097302, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.778 total time=  27.3s
[CV 2/3; 12/50] START C=0.023384996999775014, alpha=0.00021262656405097302, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 12/50] END C=0.023384996999775014, alpha=0.00021262656405097302, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.991 total time=  27.4s
[CV 3/3; 12/50] START C=0.023384996999775014, alpha=0.00021262656405097302, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 12/50] END C=0.023384996999775014, alpha=0.00021262656405097302, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.965 total time=  27.2s
[CV 1/3; 13/50] START C=0.03731160442370569, alpha=0.00011444300260577057, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 13/50] END C=0.03731160442370569, alpha=0.00011444300260577057, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.775 total time=  25.8s
[CV 2/3; 13/50] START C=0.03731160442370569, alpha=0.00011444300260577057, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 13/50] END C=0.03731160442370569, alpha=0.00011444300260577057, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.990 total time=  26.3s
[CV 3/3; 13/50] START C=0.03731160442370569, alpha=0.00011444300260577057, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 13/50] END C=0.03731160442370569, alpha=0.00011444300260577057, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.965 total time=  26.2s
[CV 1/3; 14/50] START C=0.08644620294098898, alpha=0.00017853203778050322, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 14/50] END C=0.08644620294098898, alpha=0.00017853203778050322, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.778 total time=  30.8s
[CV 2/3; 14/50] START C=0.08644620294098898, alpha=0.00017853203778050322, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 14/50] END C=0.08644620294098898, alpha=0.00017853203778050322, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.991 total time=  30.7s
[CV 3/3; 14/50] START C=0.08644620294098898, alpha=0.00017853203778050322, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 14/50] END C=0.08644620294098898, alpha=0.00017853203778050322, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.968 total time=  30.7s
[CV 1/3; 15/50] START C=0.01835927698956005, alpha=0.002532097755848139, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 15/50] END C=0.01835927698956005, alpha=0.002532097755848139, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.779 total time=  31.9s
[CV 2/3; 15/50] START C=0.01835927698956005, alpha=0.002532097755848139, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 15/50] END C=0.01835927698956005, alpha=0.002532097755848139, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.986 total time=  35.9s
[CV 3/3; 15/50] START C=0.01835927698956005, alpha=0.002532097755848139, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 15/50] END C=0.01835927698956005, alpha=0.002532097755848139, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.948 total time=  35.0s
[CV 1/3; 16/50] START C=1.874126588807636, alpha=0.0017196610519663806, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 16/50] END C=1.874126588807636, alpha=0.0017196610519663806, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.766 total time=  40.2s
[CV 2/3; 16/50] START C=1.874126588807636, alpha=0.0017196610519663806, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 16/50] END C=1.874126588807636, alpha=0.0017196610519663806, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.992 total time=  41.1s
[CV 3/3; 16/50] START C=1.874126588807636, alpha=0.0017196610519663806, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 16/50] END C=1.874126588807636, alpha=0.0017196610519663806, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.957 total time=  40.9s
[CV 1/3; 17/50] START C=0.1735069813543116, alpha=0.0010483998344311958, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 17/50] END C=0.1735069813543116, alpha=0.0010483998344311958, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.768 total time=  39.1s
[CV 2/3; 17/50] START C=0.1735069813543116, alpha=0.0010483998344311958, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 17/50] END C=0.1735069813543116, alpha=0.0010483998344311958, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.993 total time=  39.6s
[CV 3/3; 17/50] START C=0.1735069813543116, alpha=0.0010483998344311958, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 17/50] END C=0.1735069813543116, alpha=0.0010483998344311958, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.958 total time=  39.6s
[CV 1/3; 18/50] START C=0.20699791876050289, alpha=0.0044201330166528125, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 18/50] END C=0.20699791876050289, alpha=0.0044201330166528125, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.771 total time=  35.3s
[CV 2/3; 18/50] START C=0.20699791876050289, alpha=0.0044201330166528125, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 18/50] END C=0.20699791876050289, alpha=0.0044201330166528125, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.992 total time=  36.5s
[CV 3/3; 18/50] START C=0.20699791876050289, alpha=0.0044201330166528125, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 18/50] END C=0.20699791876050289, alpha=0.0044201330166528125, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.968 total time=  36.2s
[CV 1/3; 19/50] START C=0.017644702549336633, alpha=0.00024019442751286514, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 1/3; 19/50] END C=0.017644702549336633, alpha=0.00024019442751286514, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.781 total time=  26.1s
[CV 2/3; 19/50] START C=0.017644702549336633, alpha=0.00024019442751286514, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 2/3; 19/50] END C=0.017644702549336633, alpha=0.00024019442751286514, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.992 total time=  30.0s
[CV 3/3; 19/50] START C=0.017644702549336633, alpha=0.00024019442751286514, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 3/3; 19/50] END C=0.017644702549336633, alpha=0.00024019442751286514, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.950 total time=  32.9s
[CV 1/3; 20/50] START C=0.016294703690369366, alpha=0.009808324661415495, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 1/3; 20/50] END C=0.016294703690369366, alpha=0.009808324661415495, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.785 total time=  29.2s
[CV 2/3; 20/50] START C=0.016294703690369366, alpha=0.009808324661415495, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 2/3; 20/50] END C=0.016294703690369366, alpha=0.009808324661415495, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.991 total time=  33.3s
[CV 3/3; 20/50] START C=0.016294703690369366, alpha=0.009808324661415495, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 3/3; 20/50] END C=0.016294703690369366, alpha=0.009808324661415495, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.978 total time=  29.6s
[CV 1/3; 21/50] START C=0.011120051655263417, alpha=0.00027433432792093893, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 1/3; 21/50] END C=0.011120051655263417, alpha=0.00027433432792093893, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.772 total time=  27.8s
[CV 2/3; 21/50] START C=0.011120051655263417, alpha=0.00027433432792093893, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 2/3; 21/50] END C=0.011120051655263417, alpha=0.00027433432792093893, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.991 total time=  30.7s
[CV 3/3; 21/50] START C=0.011120051655263417, alpha=0.00027433432792093893, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 3/3; 21/50] END C=0.011120051655263417, alpha=0.00027433432792093893, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.951 total time=  31.9s
[CV 1/3; 22/50] START C=0.012039348520089676, alpha=0.0005116062181970679, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 22/50] END C=0.012039348520089676, alpha=0.0005116062181970679, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.776 total time=  21.4s
[CV 2/3; 22/50] START C=0.012039348520089676, alpha=0.0005116062181970679, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 22/50] END C=0.012039348520089676, alpha=0.0005116062181970679, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.989 total time=  34.2s
[CV 3/3; 22/50] START C=0.012039348520089676, alpha=0.0005116062181970679, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 22/50] END C=0.012039348520089676, alpha=0.0005116062181970679, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.952 total time=  30.2s
[CV 1/3; 23/50] START C=1.989488127571618, alpha=0.00034890322007713237, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 23/50] END C=1.989488127571618, alpha=0.00034890322007713237, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.771 total time=  31.8s
[CV 2/3; 23/50] START C=1.989488127571618, alpha=0.00034890322007713237, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 23/50] END C=1.989488127571618, alpha=0.00034890322007713237, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.991 total time=  32.3s
[CV 3/3; 23/50] START C=1.989488127571618, alpha=0.00034890322007713237, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 23/50] END C=1.989488127571618, alpha=0.00034890322007713237, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.967 total time=  32.4s
[CV 1/3; 24/50] START C=0.016871808064463104, alpha=0.0006723682786845261, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 1/3; 24/50] END C=0.016871808064463104, alpha=0.0006723682786845261, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.779 total time=  28.2s
[CV 2/3; 24/50] START C=0.016871808064463104, alpha=0.0006723682786845261, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 2/3; 24/50] END C=0.016871808064463104, alpha=0.0006723682786845261, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.991 total time=  34.6s
[CV 3/3; 24/50] START C=0.016871808064463104, alpha=0.0006723682786845261, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 3/3; 24/50] END C=0.016871808064463104, alpha=0.0006723682786845261, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.957 total time=  36.5s
[CV 1/3; 25/50] START C=1.252791383047794, alpha=0.0037616541023570904, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 25/50] END C=1.252791383047794, alpha=0.0037616541023570904, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.767 total time=  35.3s
[CV 2/3; 25/50] START C=1.252791383047794, alpha=0.0037616541023570904, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 25/50] END C=1.252791383047794, alpha=0.0037616541023570904, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.985 total time=  36.5s
[CV 3/3; 25/50] START C=1.252791383047794, alpha=0.0037616541023570904, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 25/50] END C=1.252791383047794, alpha=0.0037616541023570904, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.957 total time=  36.1s
[CV 1/3; 26/50] START C=0.6319826257662895, alpha=0.00038742022005048676, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 26/50] END C=0.6319826257662895, alpha=0.00038742022005048676, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.774 total time=  27.9s
[CV 2/3; 26/50] START C=0.6319826257662895, alpha=0.00038742022005048676, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 26/50] END C=0.6319826257662895, alpha=0.00038742022005048676, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.990 total time=  28.7s
[CV 3/3; 26/50] START C=0.6319826257662895, alpha=0.00038742022005048676, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 26/50] END C=0.6319826257662895, alpha=0.00038742022005048676, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.966 total time=  28.4s
[CV 1/3; 27/50] START C=0.030067153997934953, alpha=0.00024129752439016266, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 27/50] END C=0.030067153997934953, alpha=0.00024129752439016266, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.776 total time=  31.2s
[CV 2/3; 27/50] START C=0.030067153997934953, alpha=0.00024129752439016266, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 27/50] END C=0.030067153997934953, alpha=0.00024129752439016266, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.991 total time=  30.9s
[CV 3/3; 27/50] START C=0.030067153997934953, alpha=0.00024129752439016266, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 27/50] END C=0.030067153997934953, alpha=0.00024129752439016266, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.954 total time=  30.8s
[CV 1/3; 28/50] START C=0.07742481410453278, alpha=0.0005653192173220674, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 28/50] END C=0.07742481410453278, alpha=0.0005653192173220674, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.773 total time=  28.0s
[CV 2/3; 28/50] START C=0.07742481410453278, alpha=0.0005653192173220674, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 28/50] END C=0.07742481410453278, alpha=0.0005653192173220674, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.989 total time=  29.1s
[CV 3/3; 28/50] START C=0.07742481410453278, alpha=0.0005653192173220674, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 28/50] END C=0.07742481410453278, alpha=0.0005653192173220674, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.959 total time=  28.8s
[CV 1/3; 29/50] START C=0.9129340424987065, alpha=0.003692457739989303, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 29/50] END C=0.9129340424987065, alpha=0.003692457739989303, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.765 total time=  35.3s
[CV 2/3; 29/50] START C=0.9129340424987065, alpha=0.003692457739989303, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 29/50] END C=0.9129340424987065, alpha=0.003692457739989303, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.987 total time=  36.5s
[CV 3/3; 29/50] START C=0.9129340424987065, alpha=0.003692457739989303, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 29/50] END C=0.9129340424987065, alpha=0.003692457739989303, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.932 total time=  36.1s
[CV 1/3; 30/50] START C=0.42183294777405306, alpha=0.0030432693488758886, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 1/3; 30/50] END C=0.42183294777405306, alpha=0.0030432693488758886, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.779 total time=  33.3s
[CV 2/3; 30/50] START C=0.42183294777405306, alpha=0.0030432693488758886, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 2/3; 30/50] END C=0.42183294777405306, alpha=0.0030432693488758886, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.991 total time=  38.6s
[CV 3/3; 30/50] START C=0.42183294777405306, alpha=0.0030432693488758886, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 3/3; 30/50] END C=0.42183294777405306, alpha=0.0030432693488758886, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.946 total time=  41.2s
[CV 1/3; 31/50] START C=0.4783181544448912, alpha=0.0004194588669311856, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 31/50] END C=0.4783181544448912, alpha=0.0004194588669311856, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.782 total time=  23.7s
[CV 2/3; 31/50] START C=0.4783181544448912, alpha=0.0004194588669311856, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 31/50] END C=0.4783181544448912, alpha=0.0004194588669311856, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.988 total time=  32.5s
[CV 3/3; 31/50] START C=0.4783181544448912, alpha=0.0004194588669311856, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 31/50] END C=0.4783181544448912, alpha=0.0004194588669311856, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.949 total time=  24.0s
[CV 1/3; 32/50] START C=0.08352236719346227, alpha=0.002939802752417472, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 32/50] END C=0.08352236719346227, alpha=0.002939802752417472, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.770 total time=  40.1s
[CV 2/3; 32/50] START C=0.08352236719346227, alpha=0.002939802752417472, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 32/50] END C=0.08352236719346227, alpha=0.002939802752417472, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.990 total time=  41.1s
[CV 3/3; 32/50] START C=0.08352236719346227, alpha=0.002939802752417472, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 32/50] END C=0.08352236719346227, alpha=0.002939802752417472, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.968 total time=  40.9s
[CV 1/3; 33/50] START C=0.06793948691246166, alpha=0.004005811414758291, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 33/50] END C=0.06793948691246166, alpha=0.004005811414758291, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.772 total time=  40.4s
[CV 2/3; 33/50] START C=0.06793948691246166, alpha=0.004005811414758291, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 33/50] END C=0.06793948691246166, alpha=0.004005811414758291, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.990 total time=  41.2s
[CV 3/3; 33/50] START C=0.06793948691246166, alpha=0.004005811414758291, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 33/50] END C=0.06793948691246166, alpha=0.004005811414758291, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.973 total time=  41.0s
[CV 1/3; 34/50] START C=0.05760805380886523, alpha=0.00038023223451839037, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 34/50] END C=0.05760805380886523, alpha=0.00038023223451839037, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.774 total time=  27.9s
[CV 2/3; 34/50] START C=0.05760805380886523, alpha=0.00038023223451839037, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 34/50] END C=0.05760805380886523, alpha=0.00038023223451839037, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.991 total time=  28.7s
[CV 3/3; 34/50] START C=0.05760805380886523, alpha=0.00038023223451839037, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 34/50] END C=0.05760805380886523, alpha=0.00038023223451839037, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.959 total time=  28.4s
[CV 1/3; 35/50] START C=0.0434187010561529, alpha=0.0002046389173327987, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 1/3; 35/50] END C=0.0434187010561529, alpha=0.0002046389173327987, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.775 total time=  27.6s
[CV 2/3; 35/50] START C=0.0434187010561529, alpha=0.0002046389173327987, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 2/3; 35/50] END C=0.0434187010561529, alpha=0.0002046389173327987, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.991 total time=  32.6s
[CV 3/3; 35/50] START C=0.0434187010561529, alpha=0.0002046389173327987, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 3/3; 35/50] END C=0.0434187010561529, alpha=0.0002046389173327987, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.951 total time=  28.5s
[CV 1/3; 36/50] START C=0.2700846421105831, alpha=0.00015918844528593223, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 36/50] END C=0.2700846421105831, alpha=0.00015918844528593223, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.775 total time=  30.7s
[CV 2/3; 36/50] START C=0.2700846421105831, alpha=0.00015918844528593223, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 36/50] END C=0.2700846421105831, alpha=0.00015918844528593223, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.990 total time=  30.6s
[CV 3/3; 36/50] START C=0.2700846421105831, alpha=0.00015918844528593223, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 36/50] END C=0.2700846421105831, alpha=0.00015918844528593223, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.969 total time=  30.4s
[CV 1/3; 37/50] START C=0.0174024439023549, alpha=0.00016901869616386045, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 37/50] END C=0.0174024439023549, alpha=0.00016901869616386045, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.771 total time=  26.7s
[CV 2/3; 37/50] START C=0.0174024439023549, alpha=0.00016901869616386045, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 37/50] END C=0.0174024439023549, alpha=0.00016901869616386045, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.990 total time=  26.8s
[CV 3/3; 37/50] START C=0.0174024439023549, alpha=0.00016901869616386045, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 37/50] END C=0.0174024439023549, alpha=0.00016901869616386045, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.971 total time=  26.9s
[CV 1/3; 38/50] START C=0.08166273884433714, alpha=0.00046219339967801373, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 38/50] END C=0.08166273884433714, alpha=0.00046219339967801373, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.768 total time=  32.1s
[CV 2/3; 38/50] START C=0.08166273884433714, alpha=0.00046219339967801373, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 38/50] END C=0.08166273884433714, alpha=0.00046219339967801373, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.992 total time=  33.8s
[CV 3/3; 38/50] START C=0.08166273884433714, alpha=0.00046219339967801373, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 38/50] END C=0.08166273884433714, alpha=0.00046219339967801373, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.967 total time=  33.7s
[CV 1/3; 39/50] START C=0.05292054850272244, alpha=0.002501969915918345, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 39/50] END C=0.05292054850272244, alpha=0.002501969915918345, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.762 total time=  35.3s
[CV 2/3; 39/50] START C=0.05292054850272244, alpha=0.002501969915918345, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 39/50] END C=0.05292054850272244, alpha=0.002501969915918345, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.990 total time=  36.5s
[CV 3/3; 39/50] START C=0.05292054850272244, alpha=0.002501969915918345, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 39/50] END C=0.05292054850272244, alpha=0.002501969915918345, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.959 total time=  36.1s
[CV 1/3; 40/50] START C=0.1262954219120332, alpha=0.005444327991854233, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 40/50] END C=0.1262954219120332, alpha=0.005444327991854233, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.780 total time=  28.8s
[CV 2/3; 40/50] START C=0.1262954219120332, alpha=0.005444327991854233, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 40/50] END C=0.1262954219120332, alpha=0.005444327991854233, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.986 total time=  33.3s
[CV 3/3; 40/50] START C=0.1262954219120332, alpha=0.005444327991854233, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 40/50] END C=0.1262954219120332, alpha=0.005444327991854233, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.953 total time=  31.9s
[CV 1/3; 41/50] START C=0.09174189425885466, alpha=0.005896125302544957, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 1/3; 41/50] END C=0.09174189425885466, alpha=0.005896125302544957, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.786 total time=  29.3s
[CV 2/3; 41/50] START C=0.09174189425885466, alpha=0.005896125302544957, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 2/3; 41/50] END C=0.09174189425885466, alpha=0.005896125302544957, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.991 total time=  33.2s
[CV 3/3; 41/50] START C=0.09174189425885466, alpha=0.005896125302544957, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 3/3; 41/50] END C=0.09174189425885466, alpha=0.005896125302544957, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.942 total time=  32.8s
[CV 1/3; 42/50] START C=0.06285118632441855, alpha=0.007749342421089683, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 42/50] END C=0.06285118632441855, alpha=0.007749342421089683, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.780 total time=  25.7s
[CV 2/3; 42/50] START C=0.06285118632441855, alpha=0.007749342421089683, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 42/50] END C=0.06285118632441855, alpha=0.007749342421089683, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.986 total time=  29.5s
[CV 3/3; 42/50] START C=0.06285118632441855, alpha=0.007749342421089683, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 42/50] END C=0.06285118632441855, alpha=0.007749342421089683, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.954 total time=  31.6s
[CV 1/3; 43/50] START C=0.5645222483344633, alpha=0.0034700100401993273, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 43/50] END C=0.5645222483344633, alpha=0.0034700100401993273, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.769 total time=  35.3s
[CV 2/3; 43/50] START C=0.5645222483344633, alpha=0.0034700100401993273, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 43/50] END C=0.5645222483344633, alpha=0.0034700100401993273, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.990 total time=  36.5s
[CV 3/3; 43/50] START C=0.5645222483344633, alpha=0.0034700100401993273, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 43/50] END C=0.5645222483344633, alpha=0.0034700100401993273, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.954 total time=  36.1s
[CV 1/3; 44/50] START C=0.2871556819569572, alpha=0.00021781487455193498, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 44/50] END C=0.2871556819569572, alpha=0.00021781487455193498, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.771 total time=  30.9s
[CV 2/3; 44/50] START C=0.2871556819569572, alpha=0.00021781487455193498, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 44/50] END C=0.2871556819569572, alpha=0.00021781487455193498, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.992 total time=  30.7s
[CV 3/3; 44/50] START C=0.2871556819569572, alpha=0.00021781487455193498, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 44/50] END C=0.2871556819569572, alpha=0.00021781487455193498, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.958 total time=  30.7s
[CV 1/3; 45/50] START C=0.19145269066789528, alpha=0.0002430823598642029, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 45/50] END C=0.19145269066789528, alpha=0.0002430823598642029, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.782 total time=  23.3s
[CV 2/3; 45/50] START C=0.19145269066789528, alpha=0.0002430823598642029, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 45/50] END C=0.19145269066789528, alpha=0.0002430823598642029, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.988 total time=  32.7s
[CV 3/3; 45/50] START C=0.19145269066789528, alpha=0.0002430823598642029, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 45/50] END C=0.19145269066789528, alpha=0.0002430823598642029, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.958 total time=  28.9s
[CV 1/3; 46/50] START C=0.1063946420753684, alpha=0.0007407343918344587, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 46/50] END C=0.1063946420753684, alpha=0.0007407343918344587, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.766 total time=  28.4s
[CV 2/3; 46/50] START C=0.1063946420753684, alpha=0.0007407343918344587, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 46/50] END C=0.1063946420753684, alpha=0.0007407343918344587, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.990 total time=  29.9s
[CV 3/3; 46/50] START C=0.1063946420753684, alpha=0.0007407343918344587, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 46/50] END C=0.1063946420753684, alpha=0.0007407343918344587, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.941 total time=  29.7s
[CV 1/3; 47/50] START C=0.10120862361477853, alpha=0.0001231308340350875, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 47/50] END C=0.10120862361477853, alpha=0.0001231308340350875, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.775 total time=  25.7s
[CV 2/3; 47/50] START C=0.10120862361477853, alpha=0.0001231308340350875, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 47/50] END C=0.10120862361477853, alpha=0.0001231308340350875, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.992 total time=  26.2s
[CV 3/3; 47/50] START C=0.10120862361477853, alpha=0.0001231308340350875, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 47/50] END C=0.10120862361477853, alpha=0.0001231308340350875, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.967 total time=  26.5s
[CV 1/3; 48/50] START C=0.7491075440643165, alpha=0.005474500918018134, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 1/3; 48/50] END C=0.7491075440643165, alpha=0.005474500918018134, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.776 total time=  28.6s
[CV 2/3; 48/50] START C=0.7491075440643165, alpha=0.005474500918018134, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 2/3; 48/50] END C=0.7491075440643165, alpha=0.005474500918018134, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.991 total time=  35.5s
[CV 3/3; 48/50] START C=0.7491075440643165, alpha=0.005474500918018134, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 3/3; 48/50] END C=0.7491075440643165, alpha=0.005474500918018134, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.964 total time=  33.4s
[CV 1/3; 49/50] START C=0.02839788285102342, alpha=0.002452451896419808, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 49/50] END C=0.02839788285102342, alpha=0.002452451896419808, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.762 total time=  30.8s
[CV 2/3; 49/50] START C=0.02839788285102342, alpha=0.002452451896419808, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 49/50] END C=0.02839788285102342, alpha=0.002452451896419808, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.989 total time=  34.8s
[CV 3/3; 49/50] START C=0.02839788285102342, alpha=0.002452451896419808, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 49/50] END C=0.02839788285102342, alpha=0.002452451896419808, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.947 total time=  35.3s
[CV 1/3; 50/50] START C=0.09504585350775806, alpha=0.006920246865966962, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 50/50] END C=0.09504585350775806, alpha=0.006920246865966962, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.768 total time=  25.2s
[CV 2/3; 50/50] START C=0.09504585350775806, alpha=0.006920246865966962, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 50/50] END C=0.09504585350775806, alpha=0.006920246865966962, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.990 total time=  29.8s
[CV 3/3; 50/50] START C=0.09504585350775806, alpha=0.006920246865966962, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 50/50] END C=0.09504585350775806, alpha=0.006920246865966962, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.950 total time=  29.6s
Beste Parameter: {'C': np.float64(0.016294703690369366), 'alpha': np.float64(0.009808324661415495), 'balance_cell_type': True, 'feature_selection': True, 'mini_batch': False, 'use_SGD': True}
Finished Training. Starting Prediction on Test Data...
CellTypist Test Accuracy: 0.8033
Macro F1: 0.719046725020217
--- In distribution testset ---
Baseline accuracy score 0.8033

                     precision    recall  f1-score   support

             B cell       1.00      0.91      0.95       120
     CD14+ monocyte       0.84      1.00      0.91      2575
        CD4+ T cell       0.77      1.00      0.87      3910
   Cytotoxic T cell       1.00      0.07      0.13      1824
     Dendritic cell       1.00      0.20      0.33         5
      Megakaryocyte       1.00      0.71      0.83         7
Natural killer cell       0.82      0.89      0.85       791
        Plasma cell       1.00      0.78      0.87        49

           accuracy                           0.80      9281
          macro avg       0.93      0.69      0.72      9281
       weighted avg       0.84      0.80      0.73      9281

Random dropout accuracy score 0.7782
Total samples: 9281
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.8000
Feature importance dropout (0.5% features dropped) accuracy score 0.7659
Feature importance dropout (1.0% features dropped) accuracy score 0.7438
Feature importance dropout (2.0% features dropped) accuracy score 0.7044
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.7067

                     precision    recall  f1-score   support

             B cell       1.00      0.52      0.68      3960
     CD14+ monocyte       0.33      1.00      0.50      3135
        CD4+ T cell       0.88      1.00      0.93     13677
   Cytotoxic T cell       0.82      0.16      0.27      4843
     Dendritic cell       1.00      0.12      0.22       529
      Megakaryocyte       1.00      0.49      0.66        86
Natural killer cell       0.88      0.29      0.43      2751
        Plasma cell       1.00      0.22      0.36        23

           accuracy                           0.71     29004
          macro avg       0.86      0.47      0.51     29004
       weighted avg       0.83      0.71      0.68     29004

Random dropout accuracy score 0.6388
Total samples: 29004
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.6901
Feature importance dropout (0.5% features dropped) accuracy score 0.5942
Feature importance dropout (1.0% features dropped) accuracy score 0.5793
Feature importance dropout (2.0% features dropped) accuracy score 0.5772
=== JOB_STATISTICS ===
=== current date     : Sat Jun 27 17:54:50 CEST 2026
= Job-ID             : 11995956 on woody
= Job-Name           : celltypist_bayes_search_celltype
= Job-Command        : /home/hpc/iwbn/iwbn133h/submit_celltypist_randomsearch_job.sh
= Initial workdir    : /home/hpc/iwbn/iwbn133h
= Queue/Partition    : work
= Slurm account      : iwbn with QOS=normal
= Features           : icx
= Requested resources:  for 1-00:00:00
= Elapsed runtime    : 01:35:25
= Total RAM usage    : 13.2 GiB of requested  GiB (%)   
= Node list          : w2520
= Subm/Elig/Start/End: 2026-06-27T16:19:24 / 2026-06-27T16:19:24 / 2026-06-27T16:19:25 / 2026-06-27T17:54:50
======================
=== Quota infos ======
    Path                 Used     SoftQ    HardQ    Gracetime  Filec    FileQ    FiHaQ    FileGrace    
    /home/woody           982.1M  1000.0G  1500.0G        N/A  29,019    5,000K   7,500K        N/A    
    /home/hpc              86.2G   104.9G   209.7G        N/A     139K     500K   1,000K        N/A    
    /home/vault             0.0K  1048.6G  2097.2G        N/A       1      200K     400K        N/A    
