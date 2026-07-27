### Starting TaskPrologue of job 11997795 on w2216 at Sun Jun 28 23:09:48 CEST 2026
#   SLURM_JOB_NODELIST=w2216
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
[CV 1/3; 1/50] START C=0.09624227903593045, alpha=0.0013773853273515867, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 1/50] END C=0.09624227903593045, alpha=0.0013773853273515867, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.774 total time=  40.9s
[CV 2/3; 1/50] START C=0.09624227903593045, alpha=0.0013773853273515867, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 1/50] END C=0.09624227903593045, alpha=0.0013773853273515867, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.992 total time=  41.7s
[CV 3/3; 1/50] START C=0.09624227903593045, alpha=0.0013773853273515867, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 1/50] END C=0.09624227903593045, alpha=0.0013773853273515867, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.968 total time=  41.5s
[CV 1/3; 2/50] START C=0.06008573205559141, alpha=0.003592890240949864, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 2/50] END C=0.06008573205559141, alpha=0.003592890240949864, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.788 total time=  35.8s
[CV 2/3; 2/50] START C=0.06008573205559141, alpha=0.003592890240949864, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 2/50] END C=0.06008573205559141, alpha=0.003592890240949864, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.990 total time=  36.9s
[CV 3/3; 2/50] START C=0.06008573205559141, alpha=0.003592890240949864, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 2/50] END C=0.06008573205559141, alpha=0.003592890240949864, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.967 total time=  36.6s
[CV 1/3; 3/50] START C=0.4583827888950748, alpha=0.0018825499761168513, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 1/3; 3/50] END C=0.4583827888950748, alpha=0.0018825499761168513, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.774 total time=  36.6s
[CV 2/3; 3/50] START C=0.4583827888950748, alpha=0.0018825499761168513, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 2/3; 3/50] END C=0.4583827888950748, alpha=0.0018825499761168513, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.991 total time=  45.1s
[CV 3/3; 3/50] START C=0.4583827888950748, alpha=0.0018825499761168513, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 3/3; 3/50] END C=0.4583827888950748, alpha=0.0018825499761168513, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.969 total time=  41.3s
[CV 1/3; 4/50] START C=0.796896444051975, alpha=0.0007982841717655957, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 1/3; 4/50] END C=0.796896444051975, alpha=0.0007982841717655957, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.771 total time=  30.0s
[CV 2/3; 4/50] START C=0.796896444051975, alpha=0.0007982841717655957, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 2/3; 4/50] END C=0.796896444051975, alpha=0.0007982841717655957, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.992 total time=  38.0s
[CV 3/3; 4/50] START C=0.796896444051975, alpha=0.0007982841717655957, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 3/3; 4/50] END C=0.796896444051975, alpha=0.0007982841717655957, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.939 total time=  33.5s
[CV 1/3; 5/50] START C=0.029925498818690503, alpha=0.0008743788459278157, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 5/50] END C=0.029925498818690503, alpha=0.0008743788459278157, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.768 total time=  32.0s
[CV 2/3; 5/50] START C=0.029925498818690503, alpha=0.0008743788459278157, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 5/50] END C=0.029925498818690503, alpha=0.0008743788459278157, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.990 total time=  32.8s
[CV 3/3; 5/50] START C=0.029925498818690503, alpha=0.0008743788459278157, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 5/50] END C=0.029925498818690503, alpha=0.0008743788459278157, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.956 total time=  32.6s
[CV 1/3; 6/50] START C=0.04831498787748873, alpha=0.0007233218352192343, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 1/3; 6/50] END C=0.04831498787748873, alpha=0.0007233218352192343, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.766 total time=  30.1s
[CV 2/3; 6/50] START C=0.04831498787748873, alpha=0.0007233218352192343, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 2/3; 6/50] END C=0.04831498787748873, alpha=0.0007233218352192343, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.991 total time=  39.0s
[CV 3/3; 6/50] START C=0.04831498787748873, alpha=0.0007233218352192343, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 3/3; 6/50] END C=0.04831498787748873, alpha=0.0007233218352192343, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.940 total time=  35.7s
[CV 1/3; 7/50] START C=1.0353162508329743, alpha=0.0003024843318332406, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 7/50] END C=1.0353162508329743, alpha=0.0003024843318332406, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.771 total time=  31.9s
[CV 2/3; 7/50] START C=1.0353162508329743, alpha=0.0003024843318332406, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 7/50] END C=1.0353162508329743, alpha=0.0003024843318332406, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.991 total time=  31.8s
[CV 3/3; 7/50] START C=1.0353162508329743, alpha=0.0003024843318332406, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 7/50] END C=1.0353162508329743, alpha=0.0003024843318332406, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.959 total time=  31.7s
[CV 1/3; 8/50] START C=0.024419636493748894, alpha=0.00011000719448786885, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 8/50] END C=0.024419636493748894, alpha=0.00011000719448786885, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.778 total time=  25.9s
[CV 2/3; 8/50] START C=0.024419636493748894, alpha=0.00011000719448786885, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 8/50] END C=0.024419636493748894, alpha=0.00011000719448786885, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.990 total time=  26.6s
[CV 3/3; 8/50] START C=0.024419636493748894, alpha=0.00011000719448786885, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 8/50] END C=0.024419636493748894, alpha=0.00011000719448786885, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.966 total time=  26.4s
[CV 1/3; 9/50] START C=0.4090766019613315, alpha=0.00042994670822498236, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 1/3; 9/50] END C=0.4090766019613315, alpha=0.00042994670822498236, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.765 total time=  25.4s
[CV 2/3; 9/50] START C=0.4090766019613315, alpha=0.00042994670822498236, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 2/3; 9/50] END C=0.4090766019613315, alpha=0.00042994670822498236, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.991 total time=  32.4s
[CV 3/3; 9/50] START C=0.4090766019613315, alpha=0.00042994670822498236, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 3/3; 9/50] END C=0.4090766019613315, alpha=0.00042994670822498236, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.950 total time=  33.9s
[CV 1/3; 10/50] START C=0.6279057354023192, alpha=0.004339500233404074, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 1/3; 10/50] END C=0.6279057354023192, alpha=0.004339500233404074, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.777 total time=  31.9s
[CV 2/3; 10/50] START C=0.6279057354023192, alpha=0.004339500233404074, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 2/3; 10/50] END C=0.6279057354023192, alpha=0.004339500233404074, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.990 total time=  36.6s
[CV 3/3; 10/50] START C=0.6279057354023192, alpha=0.004339500233404074, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 3/3; 10/50] END C=0.6279057354023192, alpha=0.004339500233404074, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.963 total time=  35.1s
[CV 1/3; 11/50] START C=1.1014826813653036, alpha=0.002831949176613663, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 11/50] END C=1.1014826813653036, alpha=0.002831949176613663, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.763 total time=  35.7s
[CV 2/3; 11/50] START C=1.1014826813653036, alpha=0.002831949176613663, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 11/50] END C=1.1014826813653036, alpha=0.002831949176613663, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.989 total time=  36.9s
[CV 3/3; 11/50] START C=1.1014826813653036, alpha=0.002831949176613663, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 11/50] END C=1.1014826813653036, alpha=0.002831949176613663, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.950 total time=  36.5s
[CV 1/3; 12/50] START C=0.17895486425817883, alpha=0.000992994686282329, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 12/50] END C=0.17895486425817883, alpha=0.000992994686282329, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.770 total time=  27.2s
[CV 2/3; 12/50] START C=0.17895486425817883, alpha=0.000992994686282329, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 12/50] END C=0.17895486425817883, alpha=0.000992994686282329, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.987 total time=  41.2s
[CV 3/3; 12/50] START C=0.17895486425817883, alpha=0.000992994686282329, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 12/50] END C=0.17895486425817883, alpha=0.000992994686282329, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.929 total time=  36.8s
[CV 1/3; 13/50] START C=1.618278314810471, alpha=0.003600861275521673, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 13/50] END C=1.618278314810471, alpha=0.003600861275521673, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.778 total time=  40.5s
[CV 2/3; 13/50] START C=1.618278314810471, alpha=0.003600861275521673, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 13/50] END C=1.618278314810471, alpha=0.003600861275521673, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.991 total time=  41.7s
[CV 3/3; 13/50] START C=1.618278314810471, alpha=0.003600861275521673, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 13/50] END C=1.618278314810471, alpha=0.003600861275521673, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.940 total time=  41.4s
[CV 1/3; 14/50] START C=0.1640469065667848, alpha=0.0011263963025906767, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 14/50] END C=0.1640469065667848, alpha=0.0011263963025906767, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.765 total time=  35.3s
[CV 2/3; 14/50] START C=0.1640469065667848, alpha=0.0011263963025906767, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 14/50] END C=0.1640469065667848, alpha=0.0011263963025906767, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.989 total time=  36.1s
[CV 3/3; 14/50] START C=0.1640469065667848, alpha=0.0011263963025906767, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 14/50] END C=0.1640469065667848, alpha=0.0011263963025906767, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.942 total time=  35.3s
[CV 1/3; 15/50] START C=0.03540277657769448, alpha=0.0004975916691617976, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 15/50] END C=0.03540277657769448, alpha=0.0004975916691617976, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.772 total time=  32.8s
[CV 2/3; 15/50] START C=0.03540277657769448, alpha=0.0004975916691617976, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 15/50] END C=0.03540277657769448, alpha=0.0004975916691617976, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.992 total time=  34.4s
[CV 3/3; 15/50] START C=0.03540277657769448, alpha=0.0004975916691617976, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 15/50] END C=0.03540277657769448, alpha=0.0004975916691617976, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.966 total time=  34.4s
[CV 1/3; 16/50] START C=0.12083792755334534, alpha=0.0004845106383562075, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 16/50] END C=0.12083792755334534, alpha=0.0004845106383562075, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.765 total time=  25.3s
[CV 2/3; 16/50] START C=0.12083792755334534, alpha=0.0004845106383562075, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 16/50] END C=0.12083792755334534, alpha=0.0004845106383562075, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.988 total time=  31.1s
[CV 3/3; 16/50] START C=0.12083792755334534, alpha=0.0004845106383562075, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 16/50] END C=0.12083792755334534, alpha=0.0004845106383562075, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.958 total time=  29.1s
[CV 1/3; 17/50] START C=0.1609950200843744, alpha=0.0003073121327441133, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 17/50] END C=0.1609950200843744, alpha=0.0003073121327441133, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.773 total time=  28.0s
[CV 2/3; 17/50] START C=0.1609950200843744, alpha=0.0003073121327441133, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 17/50] END C=0.1609950200843744, alpha=0.0003073121327441133, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.991 total time=  28.1s
[CV 3/3; 17/50] START C=0.1609950200843744, alpha=0.0003073121327441133, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 17/50] END C=0.1609950200843744, alpha=0.0003073121327441133, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.955 total time=  27.9s
[CV 1/3; 18/50] START C=0.03762124039307905, alpha=0.00012173168388996985, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 18/50] END C=0.03762124039307905, alpha=0.00012173168388996985, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.780 total time=  26.3s
[CV 2/3; 18/50] START C=0.03762124039307905, alpha=0.00012173168388996985, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 18/50] END C=0.03762124039307905, alpha=0.00012173168388996985, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.991 total time=  26.7s
[CV 3/3; 18/50] START C=0.03762124039307905, alpha=0.00012173168388996985, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 18/50] END C=0.03762124039307905, alpha=0.00012173168388996985, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.966 total time=  26.6s
[CV 1/3; 19/50] START C=0.23932101328875965, alpha=0.006058100701464204, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 19/50] END C=0.23932101328875965, alpha=0.006058100701464204, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.765 total time=  35.7s
[CV 2/3; 19/50] START C=0.23932101328875965, alpha=0.006058100701464204, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 19/50] END C=0.23932101328875965, alpha=0.006058100701464204, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.990 total time=  36.9s
[CV 3/3; 19/50] START C=0.23932101328875965, alpha=0.006058100701464204, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 19/50] END C=0.23932101328875965, alpha=0.006058100701464204, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.979 total time=  36.5s
[CV 1/3; 20/50] START C=0.018040741027901073, alpha=0.0017200191222883322, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 20/50] END C=0.018040741027901073, alpha=0.0017200191222883322, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.769 total time=  40.6s
[CV 2/3; 20/50] START C=0.018040741027901073, alpha=0.0017200191222883322, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 20/50] END C=0.018040741027901073, alpha=0.0017200191222883322, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.991 total time=  41.5s
[CV 3/3; 20/50] START C=0.018040741027901073, alpha=0.0017200191222883322, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 20/50] END C=0.018040741027901073, alpha=0.0017200191222883322, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.962 total time=  41.3s
[CV 1/3; 21/50] START C=0.02560958561624347, alpha=0.0010258760971895461, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 21/50] END C=0.02560958561624347, alpha=0.0010258760971895461, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.774 total time=  34.3s
[CV 2/3; 21/50] START C=0.02560958561624347, alpha=0.0010258760971895461, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 21/50] END C=0.02560958561624347, alpha=0.0010258760971895461, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.990 total time=  34.7s
[CV 3/3; 21/50] START C=0.02560958561624347, alpha=0.0010258760971895461, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 21/50] END C=0.02560958561624347, alpha=0.0010258760971895461, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.947 total time=  34.3s
[CV 1/3; 22/50] START C=0.16012114163585767, alpha=0.000550761068892421, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 22/50] END C=0.16012114163585767, alpha=0.000550761068892421, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.769 total time=  28.4s
[CV 2/3; 22/50] START C=0.16012114163585767, alpha=0.000550761068892421, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 22/50] END C=0.16012114163585767, alpha=0.000550761068892421, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.990 total time=  29.2s
[CV 3/3; 22/50] START C=0.16012114163585767, alpha=0.000550761068892421, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 22/50] END C=0.16012114163585767, alpha=0.000550761068892421, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.940 total time=  29.1s
[CV 1/3; 23/50] START C=0.04902913423085566, alpha=0.00012811015389942103, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 23/50] END C=0.04902913423085566, alpha=0.00012811015389942103, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.788 total time=  26.3s
[CV 2/3; 23/50] START C=0.04902913423085566, alpha=0.00012811015389942103, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 23/50] END C=0.04902913423085566, alpha=0.00012811015389942103, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.992 total time=  26.9s
[CV 3/3; 23/50] START C=0.04902913423085566, alpha=0.00012811015389942103, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 23/50] END C=0.04902913423085566, alpha=0.00012811015389942103, balance_cell_type=False, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.960 total time=  26.6s
[CV 1/3; 24/50] START C=0.1211189985726764, alpha=0.0002399564199658371, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 24/50] END C=0.1211189985726764, alpha=0.0002399564199658371, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.774 total time=  31.7s
[CV 2/3; 24/50] START C=0.1211189985726764, alpha=0.0002399564199658371, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 24/50] END C=0.1211189985726764, alpha=0.0002399564199658371, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.993 total time=  31.4s
[CV 3/3; 24/50] START C=0.1211189985726764, alpha=0.0002399564199658371, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 24/50] END C=0.1211189985726764, alpha=0.0002399564199658371, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.952 total time=  31.3s
[CV 1/3; 25/50] START C=1.9228351026509978, alpha=0.0002616213096944196, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 25/50] END C=1.9228351026509978, alpha=0.0002616213096944196, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.773 total time=  24.2s
[CV 2/3; 25/50] START C=1.9228351026509978, alpha=0.0002616213096944196, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 25/50] END C=1.9228351026509978, alpha=0.0002616213096944196, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.989 total time=  27.4s
[CV 3/3; 25/50] START C=1.9228351026509978, alpha=0.0002616213096944196, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 25/50] END C=1.9228351026509978, alpha=0.0002616213096944196, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.952 total time=  25.6s
[CV 1/3; 26/50] START C=0.015328825151590758, alpha=0.002824447530368774, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 26/50] END C=0.015328825151590758, alpha=0.002824447530368774, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.770 total time=  40.8s
[CV 2/3; 26/50] START C=0.015328825151590758, alpha=0.002824447530368774, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 26/50] END C=0.015328825151590758, alpha=0.002824447530368774, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.991 total time=  41.6s
[CV 3/3; 26/50] START C=0.015328825151590758, alpha=0.002824447530368774, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 26/50] END C=0.015328825151590758, alpha=0.002824447530368774, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.965 total time=  41.3s
[CV 1/3; 27/50] START C=0.5244887024965266, alpha=0.0003513495512043771, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 27/50] END C=0.5244887024965266, alpha=0.0003513495512043771, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.763 total time=  32.3s
[CV 2/3; 27/50] START C=0.5244887024965266, alpha=0.0003513495512043771, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 27/50] END C=0.5244887024965266, alpha=0.0003513495512043771, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.990 total time=  32.7s
[CV 3/3; 27/50] START C=0.5244887024965266, alpha=0.0003513495512043771, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 27/50] END C=0.5244887024965266, alpha=0.0003513495512043771, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.962 total time=  32.8s
[CV 1/3; 28/50] START C=1.3506324249433146, alpha=0.00014905881412155512, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 28/50] END C=1.3506324249433146, alpha=0.00014905881412155512, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.775 total time=  30.3s
[CV 2/3; 28/50] START C=1.3506324249433146, alpha=0.00014905881412155512, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 28/50] END C=1.3506324249433146, alpha=0.00014905881412155512, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.992 total time=  30.6s
[CV 3/3; 28/50] START C=1.3506324249433146, alpha=0.00014905881412155512, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 28/50] END C=1.3506324249433146, alpha=0.00014905881412155512, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.961 total time=  30.6s
[CV 1/3; 29/50] START C=0.5269709435377122, alpha=0.005291337645999877, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 29/50] END C=0.5269709435377122, alpha=0.005291337645999877, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.776 total time=  35.8s
[CV 2/3; 29/50] START C=0.5269709435377122, alpha=0.005291337645999877, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 29/50] END C=0.5269709435377122, alpha=0.005291337645999877, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.990 total time=  36.9s
[CV 3/3; 29/50] START C=0.5269709435377122, alpha=0.005291337645999877, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 29/50] END C=0.5269709435377122, alpha=0.005291337645999877, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.973 total time=  36.6s
[CV 1/3; 30/50] START C=0.012654864422119718, alpha=0.00042147779358739384, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 30/50] END C=0.012654864422119718, alpha=0.00042147779358739384, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.775 total time=  26.3s
[CV 2/3; 30/50] START C=0.012654864422119718, alpha=0.00042147779358739384, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 30/50] END C=0.012654864422119718, alpha=0.00042147779358739384, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.989 total time=  30.8s
[CV 3/3; 30/50] START C=0.012654864422119718, alpha=0.00042147779358739384, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 30/50] END C=0.012654864422119718, alpha=0.00042147779358739384, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.951 total time=  31.6s
[CV 1/3; 31/50] START C=0.9905573999067814, alpha=0.00014896366079209596, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 31/50] END C=0.9905573999067814, alpha=0.00014896366079209596, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.778 total time=  27.1s
[CV 2/3; 31/50] START C=0.9905573999067814, alpha=0.00014896366079209596, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 31/50] END C=0.9905573999067814, alpha=0.00014896366079209596, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.990 total time=  27.2s
[CV 3/3; 31/50] START C=0.9905573999067814, alpha=0.00014896366079209596, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 31/50] END C=0.9905573999067814, alpha=0.00014896366079209596, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.967 total time=  27.1s
[CV 1/3; 32/50] START C=0.029110113915632185, alpha=0.008600365551100034, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 1/3; 32/50] END C=0.029110113915632185, alpha=0.008600365551100034, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.775 total time=  27.0s
[CV 2/3; 32/50] START C=0.029110113915632185, alpha=0.008600365551100034, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 2/3; 32/50] END C=0.029110113915632185, alpha=0.008600365551100034, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.992 total time=  32.0s
[CV 3/3; 32/50] START C=0.029110113915632185, alpha=0.008600365551100034, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 3/3; 32/50] END C=0.029110113915632185, alpha=0.008600365551100034, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.951 total time=  32.1s
[CV 1/3; 33/50] START C=0.39174059120221166, alpha=0.0020569150660881014, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 33/50] END C=0.39174059120221166, alpha=0.0020569150660881014, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.778 total time=  40.9s
[CV 2/3; 33/50] START C=0.39174059120221166, alpha=0.0020569150660881014, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 33/50] END C=0.39174059120221166, alpha=0.0020569150660881014, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.991 total time=  41.7s
[CV 3/3; 33/50] START C=0.39174059120221166, alpha=0.0020569150660881014, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 33/50] END C=0.39174059120221166, alpha=0.0020569150660881014, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.965 total time=  41.4s
[CV 1/3; 34/50] START C=0.07050274305623888, alpha=0.0013504047054569558, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 34/50] END C=0.07050274305623888, alpha=0.0013504047054569558, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.768 total time=  40.7s
[CV 2/3; 34/50] START C=0.07050274305623888, alpha=0.0013504047054569558, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 34/50] END C=0.07050274305623888, alpha=0.0013504047054569558, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.991 total time=  41.4s
[CV 3/3; 34/50] START C=0.07050274305623888, alpha=0.0013504047054569558, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 34/50] END C=0.07050274305623888, alpha=0.0013504047054569558, balance_cell_type=False, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.963 total time=  41.0s
[CV 1/3; 35/50] START C=0.025145652157127597, alpha=0.00024185179583770212, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 35/50] END C=0.025145652157127597, alpha=0.00024185179583770212, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.770 total time=  25.5s
[CV 2/3; 35/50] START C=0.025145652157127597, alpha=0.00024185179583770212, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 35/50] END C=0.025145652157127597, alpha=0.00024185179583770212, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.991 total time=  26.0s
[CV 3/3; 35/50] START C=0.025145652157127597, alpha=0.00024185179583770212, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 35/50] END C=0.025145652157127597, alpha=0.00024185179583770212, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.954 total time=  29.1s
[CV 1/3; 36/50] START C=0.029685140336867016, alpha=0.00015708898959997347, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 1/3; 36/50] END C=0.029685140336867016, alpha=0.00015708898959997347, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.770 total time=  28.1s
[CV 2/3; 36/50] START C=0.029685140336867016, alpha=0.00015708898959997347, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 2/3; 36/50] END C=0.029685140336867016, alpha=0.00015708898959997347, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.992 total time=  32.5s
[CV 3/3; 36/50] START C=0.029685140336867016, alpha=0.00015708898959997347, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 3/3; 36/50] END C=0.029685140336867016, alpha=0.00015708898959997347, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.943 total time=  30.9s
[CV 1/3; 37/50] START C=0.03050982384607061, alpha=0.00012697165789137655, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 1/3; 37/50] END C=0.03050982384607061, alpha=0.00012697165789137655, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.789 total time=  26.4s
[CV 2/3; 37/50] START C=0.03050982384607061, alpha=0.00012697165789137655, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 2/3; 37/50] END C=0.03050982384607061, alpha=0.00012697165789137655, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.991 total time=  26.9s
[CV 3/3; 37/50] START C=0.03050982384607061, alpha=0.00012697165789137655, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True
[CV 3/3; 37/50] END C=0.03050982384607061, alpha=0.00012697165789137655, balance_cell_type=True, feature_selection=False, mini_batch=True, use_SGD=True;, score=0.965 total time=  26.7s
[CV 1/3; 38/50] START C=0.2662765393091652, alpha=0.00018375344256406652, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 1/3; 38/50] END C=0.2662765393091652, alpha=0.00018375344256406652, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.775 total time=  25.2s
[CV 2/3; 38/50] START C=0.2662765393091652, alpha=0.00018375344256406652, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 2/3; 38/50] END C=0.2662765393091652, alpha=0.00018375344256406652, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.991 total time=  30.0s
[CV 3/3; 38/50] START C=0.2662765393091652, alpha=0.00018375344256406652, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True
[CV 3/3; 38/50] END C=0.2662765393091652, alpha=0.00018375344256406652, balance_cell_type=False, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.946 total time=  27.5s
[CV 1/3; 39/50] START C=0.5299470418762908, alpha=0.00028248239489935966, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 39/50] END C=0.5299470418762908, alpha=0.00028248239489935966, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.774 total time=  26.0s
[CV 2/3; 39/50] START C=0.5299470418762908, alpha=0.00028248239489935966, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 39/50] END C=0.5299470418762908, alpha=0.00028248239489935966, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.990 total time=  29.4s
[CV 3/3; 39/50] START C=0.5299470418762908, alpha=0.00028248239489935966, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 39/50] END C=0.5299470418762908, alpha=0.00028248239489935966, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.946 total time=  30.5s
[CV 1/3; 40/50] START C=0.24229895642491278, alpha=0.0008044559009055417, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 40/50] END C=0.24229895642491278, alpha=0.0008044559009055417, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.762 total time=  24.2s
[CV 2/3; 40/50] START C=0.24229895642491278, alpha=0.0008044559009055417, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 40/50] END C=0.24229895642491278, alpha=0.0008044559009055417, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.988 total time=  32.0s
[CV 3/3; 40/50] START C=0.24229895642491278, alpha=0.0008044559009055417, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 40/50] END C=0.24229895642491278, alpha=0.0008044559009055417, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.934 total time=  30.9s
[CV 1/3; 41/50] START C=0.09263855046788462, alpha=0.00012658158073515667, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 1/3; 41/50] END C=0.09263855046788462, alpha=0.00012658158073515667, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.769 total time=  23.2s
[CV 2/3; 41/50] START C=0.09263855046788462, alpha=0.00012658158073515667, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 2/3; 41/50] END C=0.09263855046788462, alpha=0.00012658158073515667, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.991 total time=  28.3s
[CV 3/3; 41/50] START C=0.09263855046788462, alpha=0.00012658158073515667, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True
[CV 3/3; 41/50] END C=0.09263855046788462, alpha=0.00012658158073515667, balance_cell_type=True, feature_selection=True, mini_batch=False, use_SGD=True;, score=0.947 total time=  27.7s
[CV 1/3; 42/50] START C=0.013155623743567855, alpha=0.002155542577260544, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 42/50] END C=0.013155623743567855, alpha=0.002155542577260544, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.781 total time=  40.9s
[CV 2/3; 42/50] START C=0.013155623743567855, alpha=0.002155542577260544, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 42/50] END C=0.013155623743567855, alpha=0.002155542577260544, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.991 total time=  41.6s
[CV 3/3; 42/50] START C=0.013155623743567855, alpha=0.002155542577260544, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 42/50] END C=0.013155623743567855, alpha=0.002155542577260544, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.964 total time=  41.4s
[CV 1/3; 43/50] START C=0.047766491304896665, alpha=0.005979729641843526, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 43/50] END C=0.047766491304896665, alpha=0.005979729641843526, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.773 total time=  26.2s
[CV 2/3; 43/50] START C=0.047766491304896665, alpha=0.005979729641843526, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 43/50] END C=0.047766491304896665, alpha=0.005979729641843526, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.988 total time=  34.2s
[CV 3/3; 43/50] START C=0.047766491304896665, alpha=0.005979729641843526, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 43/50] END C=0.047766491304896665, alpha=0.005979729641843526, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.952 total time=  30.4s
[CV 1/3; 44/50] START C=0.03822988783487555, alpha=0.003930864961188602, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 44/50] END C=0.03822988783487555, alpha=0.003930864961188602, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.784 total time=  40.9s
[CV 2/3; 44/50] START C=0.03822988783487555, alpha=0.003930864961188602, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 44/50] END C=0.03822988783487555, alpha=0.003930864961188602, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.989 total time=  41.7s
[CV 3/3; 44/50] START C=0.03822988783487555, alpha=0.003930864961188602, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 44/50] END C=0.03822988783487555, alpha=0.003930864961188602, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.977 total time=  41.4s
[CV 1/3; 45/50] START C=0.716605743530366, alpha=0.00017229256250255896, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 1/3; 45/50] END C=0.716605743530366, alpha=0.00017229256250255896, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.770 total time=  31.1s
[CV 2/3; 45/50] START C=0.716605743530366, alpha=0.00017229256250255896, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 2/3; 45/50] END C=0.716605743530366, alpha=0.00017229256250255896, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.991 total time=  31.2s
[CV 3/3; 45/50] START C=0.716605743530366, alpha=0.00017229256250255896, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True
[CV 3/3; 45/50] END C=0.716605743530366, alpha=0.00017229256250255896, balance_cell_type=True, feature_selection=True, mini_batch=True, use_SGD=True;, score=0.973 total time=  31.1s
[CV 1/3; 46/50] START C=1.034427092926508, alpha=0.00365071613061691, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 46/50] END C=1.034427092926508, alpha=0.00365071613061691, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.768 total time=  29.4s
[CV 2/3; 46/50] START C=1.034427092926508, alpha=0.00365071613061691, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 46/50] END C=1.034427092926508, alpha=0.00365071613061691, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.989 total time=  32.5s
[CV 3/3; 46/50] START C=1.034427092926508, alpha=0.00365071613061691, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 46/50] END C=1.034427092926508, alpha=0.00365071613061691, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.967 total time=  35.0s
[CV 1/3; 47/50] START C=0.14826795704270804, alpha=0.0004489679167008958, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 47/50] END C=0.14826795704270804, alpha=0.0004489679167008958, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.764 total time=  23.5s
[CV 2/3; 47/50] START C=0.14826795704270804, alpha=0.0004489679167008958, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 47/50] END C=0.14826795704270804, alpha=0.0004489679167008958, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.987 total time=  31.6s
[CV 3/3; 47/50] START C=0.14826795704270804, alpha=0.0004489679167008958, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 47/50] END C=0.14826795704270804, alpha=0.0004489679167008958, balance_cell_type=False, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.941 total time=  28.9s
[CV 1/3; 48/50] START C=0.41410985617984947, alpha=0.00024299902032889374, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 48/50] END C=0.41410985617984947, alpha=0.00024299902032889374, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.774 total time=  25.5s
[CV 2/3; 48/50] START C=0.41410985617984947, alpha=0.00024299902032889374, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 48/50] END C=0.41410985617984947, alpha=0.00024299902032889374, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.990 total time=  28.6s
[CV 3/3; 48/50] START C=0.41410985617984947, alpha=0.00024299902032889374, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 48/50] END C=0.41410985617984947, alpha=0.00024299902032889374, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.946 total time=  27.3s
[CV 1/3; 49/50] START C=0.7948426417863084, alpha=0.00023544450108623882, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 49/50] END C=0.7948426417863084, alpha=0.00023544450108623882, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.783 total time=  21.3s
[CV 2/3; 49/50] START C=0.7948426417863084, alpha=0.00023544450108623882, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 49/50] END C=0.7948426417863084, alpha=0.00023544450108623882, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.989 total time=  32.9s
[CV 3/3; 49/50] START C=0.7948426417863084, alpha=0.00023544450108623882, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 49/50] END C=0.7948426417863084, alpha=0.00023544450108623882, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.951 total time=  26.3s
[CV 1/3; 50/50] START C=0.10262815879394588, alpha=0.0002091987916021266, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 1/3; 50/50] END C=0.10262815879394588, alpha=0.0002091987916021266, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.765 total time=  26.9s
[CV 2/3; 50/50] START C=0.10262815879394588, alpha=0.0002091987916021266, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 2/3; 50/50] END C=0.10262815879394588, alpha=0.0002091987916021266, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.989 total time=  28.5s
[CV 3/3; 50/50] START C=0.10262815879394588, alpha=0.0002091987916021266, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True
[CV 3/3; 50/50] END C=0.10262815879394588, alpha=0.0002091987916021266, balance_cell_type=True, feature_selection=False, mini_batch=False, use_SGD=True;, score=0.957 total time=  31.1s
Beste Parameter: {'C': np.float64(0.03822988783487555), 'alpha': np.float64(0.003930864961188602), 'balance_cell_type': True, 'feature_selection': True, 'mini_batch': True, 'use_SGD': True}
Finished Training. Starting Prediction on Test Data...
CellTypist Test Accuracy: 0.8291
Macro F1: 0.7584650986866037
--- In distribution testset ---
Baseline accuracy score 0.8291

                     precision    recall  f1-score   support

             B cell       1.00      0.98      0.99       120
     CD14+ monocyte       0.99      1.00      1.00      2575
        CD4+ T cell       0.74      1.00      0.85      3910
   Cytotoxic T cell       0.98      0.16      0.27      1824
     Dendritic cell       1.00      0.20      0.33         5
      Megakaryocyte       1.00      0.71      0.83         7
Natural killer cell       0.81      0.97      0.89       791
        Plasma cell       1.00      0.84      0.91        49

           accuracy                           0.83      9281
          macro avg       0.94      0.73      0.76      9281
       weighted avg       0.87      0.83      0.78      9281

Random dropout accuracy score 0.8078
Total samples: 9281
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.8256
Feature importance dropout (0.5% features dropped) accuracy score 0.7982
Feature importance dropout (1.0% features dropped) accuracy score 0.7795
Feature importance dropout (2.0% features dropped) accuracy score 0.7318
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8110

                     precision    recall  f1-score   support

             B cell       1.00      0.74      0.85      3959
     CD14+ monocyte       0.63      1.00      0.78      3135
        CD4+ T cell       0.85      1.00      0.92     13664
   Cytotoxic T cell       0.70      0.44      0.54      4839
     Dendritic cell       1.00      0.11      0.19       529
      Megakaryocyte       1.00      0.42      0.59        86
Natural killer cell       0.87      0.58      0.69      2751
        Plasma cell       1.00      0.30      0.47        23

           accuracy                           0.81     28986
          macro avg       0.88      0.57      0.63     28986
       weighted avg       0.82      0.81      0.79     28986

Random dropout accuracy score 0.7573
Total samples: 28986
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.8027
Feature importance dropout (0.5% features dropped) accuracy score 0.6882
Feature importance dropout (1.0% features dropped) accuracy score 0.6418
Feature importance dropout (2.0% features dropped) accuracy score 0.5849
=== JOB_STATISTICS ===
=== current date     : Mon Jun 29 00:45:31 CEST 2026
= Job-ID             : 11997795 on woody
= Job-Name           : celltypist_bayes_search_celltype
= Job-Command        : /home/hpc/iwbn/iwbn133h/submit_celltypist_randomsearch_job.sh
= Initial workdir    : /home/hpc/iwbn/iwbn133h
= Queue/Partition    : work
= Slurm account      : iwbn with QOS=normal
= Features           : icx
= Requested resources:  for 1-00:00:00
= Elapsed runtime    : 01:35:45
= Total RAM usage    : 15.2 GiB of requested  GiB (%)   
= Node list          : w2216
= Subm/Elig/Start/End: 2026-06-28T23:09:45 / 2026-06-28T23:09:45 / 2026-06-28T23:09:46 / 2026-06-29T00:45:31
======================
=== Quota infos ======
    Path                 Used     SoftQ    HardQ    Gracetime  Filec    FileQ    FiHaQ    FileGrace    
    /home/woody           982.1M  1000.0G  1500.0G        N/A  29,019    5,000K   7,500K        N/A    
    /home/hpc              86.2G   104.9G   209.7G        N/A     139K     500K   1,000K        N/A    
    /home/vault             0.0K  1048.6G  2097.2G        N/A       1      200K     400K        N/A    
