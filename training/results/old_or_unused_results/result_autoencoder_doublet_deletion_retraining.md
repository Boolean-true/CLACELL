### Starting TaskPrologue of job 11997753 on w2206 at Sun Jun 28 22:15:13 CEST 2026
#   SLURM_JOB_NODELIST=w2206
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
['A36', 'A35', '637C', 'D503']
Categories (4, object): ['637C', 'A35', 'A36', 'D503']
['621B', 'D496']
Categories (2, object): ['621B', 'D496']
Start DAE Training...
Epoch [1/150], Loss: 0.9510
Epoch [10/150], Loss: 0.9048
Epoch [20/150], Loss: 0.8910
Epoch [30/150], Loss: 0.8828
Epoch [40/150], Loss: 0.8777
Epoch [50/150], Loss: 0.8740
Epoch [60/150], Loss: 0.8717
Epoch [70/150], Loss: 0.8693
Epoch [80/150], Loss: 0.8678
Epoch [90/150], Loss: 0.8662
Epoch [100/150], Loss: 0.8648
Epoch [110/150], Loss: 0.8638
Epoch [120/150], Loss: 0.8625
Epoch [130/150], Loss: 0.8614
Epoch [140/150], Loss: 0.8607
Early Stopping after [140/150] Epochs!

Extract robust features...
Starte automatische Hyperparametersuche auf dem Latent Space...
Fitting 3 folds for each of 50 candidates, totalling 150 fits
[CV 1/3; 1/50] START C=0.052957169851790206, class_weight=None, l1_ratio=0.75, tol=0.006719322243347594
[CV 1/3; 1/50] END C=0.052957169851790206, class_weight=None, l1_ratio=0.75, tol=0.006719322243347594;, score=0.801 total time=   2.6s
[CV 2/3; 1/50] START C=0.052957169851790206, class_weight=None, l1_ratio=0.75, tol=0.006719322243347594
[CV 2/3; 1/50] END C=0.052957169851790206, class_weight=None, l1_ratio=0.75, tol=0.006719322243347594;, score=0.986 total time=   2.9s
[CV 3/3; 1/50] START C=0.052957169851790206, class_weight=None, l1_ratio=0.75, tol=0.006719322243347594
[CV 3/3; 1/50] END C=0.052957169851790206, class_weight=None, l1_ratio=0.75, tol=0.006719322243347594;, score=0.952 total time=   3.0s
[CV 1/3; 2/50] START C=0.0017614187207335478, class_weight=balanced, l1_ratio=0.25, tol=0.001107699290586321
[CV 1/3; 2/50] END C=0.0017614187207335478, class_weight=balanced, l1_ratio=0.25, tol=0.001107699290586321;, score=0.617 total time=  59.8s
[CV 2/3; 2/50] START C=0.0017614187207335478, class_weight=balanced, l1_ratio=0.25, tol=0.001107699290586321
[CV 2/3; 2/50] END C=0.0017614187207335478, class_weight=balanced, l1_ratio=0.25, tol=0.001107699290586321;, score=0.988 total time=  14.6s
[CV 3/3; 2/50] START C=0.0017614187207335478, class_weight=balanced, l1_ratio=0.25, tol=0.001107699290586321
[CV 3/3; 2/50] END C=0.0017614187207335478, class_weight=balanced, l1_ratio=0.25, tol=0.001107699290586321;, score=0.950 total time=   2.3s
[CV 1/3; 3/50] START C=0.0017717769277643103, class_weight=None, l1_ratio=0.25, tol=0.07841963872458212
[CV 1/3; 3/50] END C=0.0017717769277643103, class_weight=None, l1_ratio=0.25, tol=0.07841963872458212;, score=0.892 total time=   0.5s
[CV 2/3; 3/50] START C=0.0017717769277643103, class_weight=None, l1_ratio=0.25, tol=0.07841963872458212
[CV 2/3; 3/50] END C=0.0017717769277643103, class_weight=None, l1_ratio=0.25, tol=0.07841963872458212;, score=0.914 total time=   0.5s
[CV 3/3; 3/50] START C=0.0017717769277643103, class_weight=None, l1_ratio=0.25, tol=0.07841963872458212
[CV 3/3; 3/50] END C=0.0017717769277643103, class_weight=None, l1_ratio=0.25, tol=0.07841963872458212;, score=0.881 total time=   0.5s
[CV 1/3; 4/50] START C=0.002585332978355639, class_weight=None, l1_ratio=0.25, tol=0.004077023847207935
[CV 1/3; 4/50] END C=0.002585332978355639, class_weight=None, l1_ratio=0.25, tol=0.004077023847207935;, score=0.906 total time=   2.2s
[CV 2/3; 4/50] START C=0.002585332978355639, class_weight=None, l1_ratio=0.25, tol=0.004077023847207935
[CV 2/3; 4/50] END C=0.002585332978355639, class_weight=None, l1_ratio=0.25, tol=0.004077023847207935;, score=0.924 total time=   2.3s
[CV 3/3; 4/50] START C=0.002585332978355639, class_weight=None, l1_ratio=0.25, tol=0.004077023847207935
[CV 3/3; 4/50] END C=0.002585332978355639, class_weight=None, l1_ratio=0.25, tol=0.004077023847207935;, score=0.884 total time=   2.2s
[CV 1/3; 5/50] START C=0.8004053608570384, class_weight=balanced, l1_ratio=0.75, tol=0.0012228084510442147
[CV 1/3; 5/50] END C=0.8004053608570384, class_weight=balanced, l1_ratio=0.75, tol=0.0012228084510442147;, score=0.648 total time=  14.4s
[CV 2/3; 5/50] START C=0.8004053608570384, class_weight=balanced, l1_ratio=0.75, tol=0.0012228084510442147
[CV 2/3; 5/50] END C=0.8004053608570384, class_weight=balanced, l1_ratio=0.75, tol=0.0012228084510442147;, score=0.991 total time=  16.1s
[CV 3/3; 5/50] START C=0.8004053608570384, class_weight=balanced, l1_ratio=0.75, tol=0.0012228084510442147
[CV 3/3; 5/50] END C=0.8004053608570384, class_weight=balanced, l1_ratio=0.75, tol=0.0012228084510442147;, score=0.965 total time=  14.2s
[CV 1/3; 6/50] START C=0.03791944501179161, class_weight=balanced, l1_ratio=0.5, tol=0.0031765029063701806
[CV 1/3; 6/50] END C=0.03791944501179161, class_weight=balanced, l1_ratio=0.5, tol=0.0031765029063701806;, score=0.621 total time=   3.6s
[CV 2/3; 6/50] START C=0.03791944501179161, class_weight=balanced, l1_ratio=0.5, tol=0.0031765029063701806
[CV 2/3; 6/50] END C=0.03791944501179161, class_weight=balanced, l1_ratio=0.5, tol=0.0031765029063701806;, score=0.990 total time=   4.2s
[CV 3/3; 6/50] START C=0.03791944501179161, class_weight=balanced, l1_ratio=0.5, tol=0.0031765029063701806
[CV 3/3; 6/50] END C=0.03791944501179161, class_weight=balanced, l1_ratio=0.5, tol=0.0031765029063701806;, score=0.954 total time=   5.7s
[CV 1/3; 7/50] START C=0.9021670103436745, class_weight=None, l1_ratio=0.0, tol=0.0021358466678335773
[CV 1/3; 7/50] END C=0.9021670103436745, class_weight=None, l1_ratio=0.0, tol=0.0021358466678335773;, score=0.781 total time=   4.8s
[CV 2/3; 7/50] START C=0.9021670103436745, class_weight=None, l1_ratio=0.0, tol=0.0021358466678335773
[CV 2/3; 7/50] END C=0.9021670103436745, class_weight=None, l1_ratio=0.0, tol=0.0021358466678335773;, score=0.990 total time=   5.4s
[CV 3/3; 7/50] START C=0.9021670103436745, class_weight=None, l1_ratio=0.0, tol=0.0021358466678335773
[CV 3/3; 7/50] END C=0.9021670103436745, class_weight=None, l1_ratio=0.0, tol=0.0021358466678335773;, score=0.972 total time=   5.2s
[CV 1/3; 8/50] START C=0.6426525385116115, class_weight=None, l1_ratio=0.75, tol=0.013614829691779276
[CV 1/3; 8/50] END C=0.6426525385116115, class_weight=None, l1_ratio=0.75, tol=0.013614829691779276;, score=0.869 total time=   1.6s
[CV 2/3; 8/50] START C=0.6426525385116115, class_weight=None, l1_ratio=0.75, tol=0.013614829691779276
[CV 2/3; 8/50] END C=0.6426525385116115, class_weight=None, l1_ratio=0.75, tol=0.013614829691779276;, score=0.988 total time=   1.5s
[CV 3/3; 8/50] START C=0.6426525385116115, class_weight=None, l1_ratio=0.75, tol=0.013614829691779276
[CV 3/3; 8/50] END C=0.6426525385116115, class_weight=None, l1_ratio=0.75, tol=0.013614829691779276;, score=0.961 total time=   1.4s
[CV 1/3; 9/50] START C=0.023492937279565102, class_weight=balanced, l1_ratio=0.75, tol=0.054550323605850284
[CV 1/3; 9/50] END C=0.023492937279565102, class_weight=balanced, l1_ratio=0.75, tol=0.054550323605850284;, score=0.620 total time=   0.8s
[CV 2/3; 9/50] START C=0.023492937279565102, class_weight=balanced, l1_ratio=0.75, tol=0.054550323605850284
[CV 2/3; 9/50] END C=0.023492937279565102, class_weight=balanced, l1_ratio=0.75, tol=0.054550323605850284;, score=0.989 total time=   0.9s
[CV 3/3; 9/50] START C=0.023492937279565102, class_weight=balanced, l1_ratio=0.75, tol=0.054550323605850284
[CV 3/3; 9/50] END C=0.023492937279565102, class_weight=balanced, l1_ratio=0.75, tol=0.054550323605850284;, score=0.951 total time=   0.9s
[CV 1/3; 10/50] START C=0.0537112658247494, class_weight=None, l1_ratio=1.0, tol=0.03798468616477835
[CV 1/3; 10/50] END C=0.0537112658247494, class_weight=None, l1_ratio=1.0, tol=0.03798468616477835;, score=0.885 total time=   0.8s
[CV 2/3; 10/50] START C=0.0537112658247494, class_weight=None, l1_ratio=1.0, tol=0.03798468616477835
[CV 2/3; 10/50] END C=0.0537112658247494, class_weight=None, l1_ratio=1.0, tol=0.03798468616477835;, score=0.984 total time=   1.0s
[CV 3/3; 10/50] START C=0.0537112658247494, class_weight=None, l1_ratio=1.0, tol=0.03798468616477835
[CV 3/3; 10/50] END C=0.0537112658247494, class_weight=None, l1_ratio=1.0, tol=0.03798468616477835;, score=0.949 total time=   1.0s
[CV 1/3; 11/50] START C=0.028834919669315864, class_weight=balanced, l1_ratio=0.25, tol=0.005152527924447728
[CV 1/3; 11/50] END C=0.028834919669315864, class_weight=balanced, l1_ratio=0.25, tol=0.005152527924447728;, score=0.643 total time=   2.4s
[CV 2/3; 11/50] START C=0.028834919669315864, class_weight=balanced, l1_ratio=0.25, tol=0.005152527924447728
[CV 2/3; 11/50] END C=0.028834919669315864, class_weight=balanced, l1_ratio=0.25, tol=0.005152527924447728;, score=0.991 total time=   2.3s
[CV 3/3; 11/50] START C=0.028834919669315864, class_weight=balanced, l1_ratio=0.25, tol=0.005152527924447728
[CV 3/3; 11/50] END C=0.028834919669315864, class_weight=balanced, l1_ratio=0.25, tol=0.005152527924447728;, score=0.955 total time=   3.3s
[CV 1/3; 12/50] START C=0.012821280629813964, class_weight=None, l1_ratio=0.75, tol=0.041699730449406155
[CV 1/3; 12/50] END C=0.012821280629813964, class_weight=None, l1_ratio=0.75, tol=0.041699730449406155;, score=0.915 total time=   0.8s
[CV 2/3; 12/50] START C=0.012821280629813964, class_weight=None, l1_ratio=0.75, tol=0.041699730449406155
[CV 2/3; 12/50] END C=0.012821280629813964, class_weight=None, l1_ratio=0.75, tol=0.041699730449406155;, score=0.972 total time=   0.8s
[CV 3/3; 12/50] START C=0.012821280629813964, class_weight=None, l1_ratio=0.75, tol=0.041699730449406155
[CV 3/3; 12/50] END C=0.012821280629813964, class_weight=None, l1_ratio=0.75, tol=0.041699730449406155;, score=0.934 total time=   0.8s
[CV 1/3; 13/50] START C=0.5536133794899253, class_weight=balanced, l1_ratio=0.25, tol=0.010225013348985078
[CV 1/3; 13/50] END C=0.5536133794899253, class_weight=balanced, l1_ratio=0.25, tol=0.010225013348985078;, score=0.726 total time=   1.7s
[CV 2/3; 13/50] START C=0.5536133794899253, class_weight=balanced, l1_ratio=0.25, tol=0.010225013348985078
[CV 2/3; 13/50] END C=0.5536133794899253, class_weight=balanced, l1_ratio=0.25, tol=0.010225013348985078;, score=0.991 total time=   1.4s
[CV 3/3; 13/50] START C=0.5536133794899253, class_weight=balanced, l1_ratio=0.25, tol=0.010225013348985078
[CV 3/3; 13/50] END C=0.5536133794899253, class_weight=balanced, l1_ratio=0.25, tol=0.010225013348985078;, score=0.955 total time=   1.4s
[CV 1/3; 14/50] START C=0.759182419050525, class_weight=balanced, l1_ratio=1.0, tol=0.02576640361529961
[CV 1/3; 14/50] END C=0.759182419050525, class_weight=balanced, l1_ratio=1.0, tol=0.02576640361529961;, score=0.725 total time=   1.0s
[CV 2/3; 14/50] START C=0.759182419050525, class_weight=balanced, l1_ratio=1.0, tol=0.02576640361529961
[CV 2/3; 14/50] END C=0.759182419050525, class_weight=balanced, l1_ratio=1.0, tol=0.02576640361529961;, score=0.991 total time=   0.8s
[CV 3/3; 14/50] START C=0.759182419050525, class_weight=balanced, l1_ratio=1.0, tol=0.02576640361529961
[CV 3/3; 14/50] END C=0.759182419050525, class_weight=balanced, l1_ratio=1.0, tol=0.02576640361529961;, score=0.952 total time=   1.1s
[CV 1/3; 15/50] START C=0.009084828146345491, class_weight=balanced, l1_ratio=0.0, tol=0.06368386051601695
[CV 1/3; 15/50] END C=0.009084828146345491, class_weight=balanced, l1_ratio=0.0, tol=0.06368386051601695;, score=0.741 total time=   0.6s
[CV 2/3; 15/50] START C=0.009084828146345491, class_weight=balanced, l1_ratio=0.0, tol=0.06368386051601695
[CV 2/3; 15/50] END C=0.009084828146345491, class_weight=balanced, l1_ratio=0.0, tol=0.06368386051601695;, score=0.992 total time=   0.5s
[CV 3/3; 15/50] START C=0.009084828146345491, class_weight=balanced, l1_ratio=0.0, tol=0.06368386051601695
[CV 3/3; 15/50] END C=0.009084828146345491, class_weight=balanced, l1_ratio=0.0, tol=0.06368386051601695;, score=0.956 total time=   0.8s
[CV 1/3; 16/50] START C=0.3057386019567192, class_weight=balanced, l1_ratio=0.5, tol=0.09029826394122877
[CV 1/3; 16/50] END C=0.3057386019567192, class_weight=balanced, l1_ratio=0.5, tol=0.09029826394122877;, score=0.732 total time=   0.7s
[CV 2/3; 16/50] START C=0.3057386019567192, class_weight=balanced, l1_ratio=0.5, tol=0.09029826394122877
[CV 2/3; 16/50] END C=0.3057386019567192, class_weight=balanced, l1_ratio=0.5, tol=0.09029826394122877;, score=0.991 total time=   0.6s
[CV 3/3; 16/50] START C=0.3057386019567192, class_weight=balanced, l1_ratio=0.5, tol=0.09029826394122877
[CV 3/3; 16/50] END C=0.3057386019567192, class_weight=balanced, l1_ratio=0.5, tol=0.09029826394122877;, score=0.954 total time=   0.7s
[CV 1/3; 17/50] START C=0.0019893975817334157, class_weight=balanced, l1_ratio=0.25, tol=0.07788870432327988
[CV 1/3; 17/50] END C=0.0019893975817334157, class_weight=balanced, l1_ratio=0.25, tol=0.07788870432327988;, score=0.618 total time=   0.5s
[CV 2/3; 17/50] START C=0.0019893975817334157, class_weight=balanced, l1_ratio=0.25, tol=0.07788870432327988
[CV 2/3; 17/50] END C=0.0019893975817334157, class_weight=balanced, l1_ratio=0.25, tol=0.07788870432327988;, score=0.989 total time=   0.6s
[CV 3/3; 17/50] START C=0.0019893975817334157, class_weight=balanced, l1_ratio=0.25, tol=0.07788870432327988
[CV 3/3; 17/50] END C=0.0019893975817334157, class_weight=balanced, l1_ratio=0.25, tol=0.07788870432327988;, score=0.952 total time=   0.7s
[CV 1/3; 18/50] START C=0.0028265159538665473, class_weight=balanced, l1_ratio=0.0, tol=0.0028096052951808777
[CV 1/3; 18/50] END C=0.0028265159538665473, class_weight=balanced, l1_ratio=0.0, tol=0.0028096052951808777;, score=0.750 total time=   2.2s
[CV 2/3; 18/50] START C=0.0028265159538665473, class_weight=balanced, l1_ratio=0.0, tol=0.0028096052951808777
[CV 2/3; 18/50] END C=0.0028265159538665473, class_weight=balanced, l1_ratio=0.0, tol=0.0028096052951808777;, score=0.992 total time=  39.0s
[CV 3/3; 18/50] START C=0.0028265159538665473, class_weight=balanced, l1_ratio=0.0, tol=0.0028096052951808777
[CV 3/3; 18/50] END C=0.0028265159538665473, class_weight=balanced, l1_ratio=0.0, tol=0.0028096052951808777;, score=0.954 total time=  39.0s
[CV 1/3; 19/50] START C=0.16719225915522357, class_weight=balanced, l1_ratio=0.5, tol=0.001022160491405854
[CV 1/3; 19/50] END C=0.16719225915522357, class_weight=balanced, l1_ratio=0.5, tol=0.001022160491405854;, score=0.633 total time=  12.8s
[CV 2/3; 19/50] START C=0.16719225915522357, class_weight=balanced, l1_ratio=0.5, tol=0.001022160491405854
[CV 2/3; 19/50] END C=0.16719225915522357, class_weight=balanced, l1_ratio=0.5, tol=0.001022160491405854;, score=0.991 total time=  10.8s
[CV 3/3; 19/50] START C=0.16719225915522357, class_weight=balanced, l1_ratio=0.5, tol=0.001022160491405854
[CV 3/3; 19/50] END C=0.16719225915522357, class_weight=balanced, l1_ratio=0.5, tol=0.001022160491405854;, score=0.960 total time=  15.3s
[CV 1/3; 20/50] START C=0.00917489453936111, class_weight=None, l1_ratio=1.0, tol=0.09359432956598211
[CV 1/3; 20/50] END C=0.00917489453936111, class_weight=None, l1_ratio=1.0, tol=0.09359432956598211;, score=0.921 total time=   0.6s
[CV 2/3; 20/50] START C=0.00917489453936111, class_weight=None, l1_ratio=1.0, tol=0.09359432956598211
[CV 2/3; 20/50] END C=0.00917489453936111, class_weight=None, l1_ratio=1.0, tol=0.09359432956598211;, score=0.957 total time=   0.6s
[CV 3/3; 20/50] START C=0.00917489453936111, class_weight=None, l1_ratio=1.0, tol=0.09359432956598211
[CV 3/3; 20/50] END C=0.00917489453936111, class_weight=None, l1_ratio=1.0, tol=0.09359432956598211;, score=0.913 total time=   0.5s
[CV 1/3; 21/50] START C=0.004811460603884574, class_weight=None, l1_ratio=0.75, tol=0.005291496516968972
[CV 1/3; 21/50] END C=0.004811460603884574, class_weight=None, l1_ratio=0.75, tol=0.005291496516968972;, score=0.907 total time=   1.9s
[CV 2/3; 21/50] START C=0.004811460603884574, class_weight=None, l1_ratio=0.75, tol=0.005291496516968972
[CV 2/3; 21/50] END C=0.004811460603884574, class_weight=None, l1_ratio=0.75, tol=0.005291496516968972;, score=0.918 total time=   2.4s
[CV 3/3; 21/50] START C=0.004811460603884574, class_weight=None, l1_ratio=0.75, tol=0.005291496516968972
[CV 3/3; 21/50] END C=0.004811460603884574, class_weight=None, l1_ratio=0.75, tol=0.005291496516968972;, score=0.880 total time=   2.4s
[CV 1/3; 22/50] START C=0.0941659669640943, class_weight=None, l1_ratio=0.0, tol=0.0018866469428197117
[CV 1/3; 22/50] END C=0.0941659669640943, class_weight=None, l1_ratio=0.0, tol=0.0018866469428197117;, score=0.867 total time=   2.8s
[CV 2/3; 22/50] START C=0.0941659669640943, class_weight=None, l1_ratio=0.0, tol=0.0018866469428197117
[CV 2/3; 22/50] END C=0.0941659669640943, class_weight=None, l1_ratio=0.0, tol=0.0018866469428197117;, score=0.989 total time=   2.9s
[CV 3/3; 22/50] START C=0.0941659669640943, class_weight=None, l1_ratio=0.0, tol=0.0018866469428197117
[CV 3/3; 22/50] END C=0.0941659669640943, class_weight=None, l1_ratio=0.0, tol=0.0018866469428197117;, score=0.965 total time=   2.9s
[CV 1/3; 23/50] START C=1.558862347362609, class_weight=balanced, l1_ratio=0.75, tol=0.0015248619180830358
[CV 1/3; 23/50] END C=1.558862347362609, class_weight=balanced, l1_ratio=0.75, tol=0.0015248619180830358;, score=0.669 total time=   9.1s
[CV 2/3; 23/50] START C=1.558862347362609, class_weight=balanced, l1_ratio=0.75, tol=0.0015248619180830358
[CV 2/3; 23/50] END C=1.558862347362609, class_weight=balanced, l1_ratio=0.75, tol=0.0015248619180830358;, score=0.991 total time=   7.5s
[CV 3/3; 23/50] START C=1.558862347362609, class_weight=balanced, l1_ratio=0.75, tol=0.0015248619180830358
[CV 3/3; 23/50] END C=1.558862347362609, class_weight=balanced, l1_ratio=0.75, tol=0.0015248619180830358;, score=0.965 total time=   7.7s
[CV 1/3; 24/50] START C=0.0022142257594822, class_weight=balanced, l1_ratio=0.0, tol=0.003619090522231293
[CV 1/3; 24/50] END C=0.0022142257594822, class_weight=balanced, l1_ratio=0.0, tol=0.003619090522231293;, score=0.753 total time=   1.2s
[CV 2/3; 24/50] START C=0.0022142257594822, class_weight=balanced, l1_ratio=0.0, tol=0.003619090522231293
[CV 2/3; 24/50] END C=0.0022142257594822, class_weight=balanced, l1_ratio=0.0, tol=0.003619090522231293;, score=0.991 total time=  38.5s
[CV 3/3; 24/50] START C=0.0022142257594822, class_weight=balanced, l1_ratio=0.0, tol=0.003619090522231293
[CV 3/3; 24/50] END C=0.0022142257594822, class_weight=balanced, l1_ratio=0.0, tol=0.003619090522231293;, score=0.954 total time=  38.5s
[CV 1/3; 25/50] START C=0.002554987736486714, class_weight=balanced, l1_ratio=1.0, tol=0.047641004454757135
[CV 1/3; 25/50] END C=0.002554987736486714, class_weight=balanced, l1_ratio=1.0, tol=0.047641004454757135;, score=0.579 total time=   1.0s
[CV 2/3; 25/50] START C=0.002554987736486714, class_weight=balanced, l1_ratio=1.0, tol=0.047641004454757135
[CV 2/3; 25/50] END C=0.002554987736486714, class_weight=balanced, l1_ratio=1.0, tol=0.047641004454757135;, score=0.982 total time=   1.7s
[CV 3/3; 25/50] START C=0.002554987736486714, class_weight=balanced, l1_ratio=1.0, tol=0.047641004454757135
[CV 3/3; 25/50] END C=0.002554987736486714, class_weight=balanced, l1_ratio=1.0, tol=0.047641004454757135;, score=0.932 total time=   1.9s
[CV 1/3; 26/50] START C=0.01867505990141344, class_weight=None, l1_ratio=0.75, tol=0.010525890823125987
[CV 1/3; 26/50] END C=0.01867505990141344, class_weight=None, l1_ratio=0.75, tol=0.010525890823125987;, score=0.876 total time=   1.7s
[CV 2/3; 26/50] START C=0.01867505990141344, class_weight=None, l1_ratio=0.75, tol=0.010525890823125987
[CV 2/3; 26/50] END C=0.01867505990141344, class_weight=None, l1_ratio=0.75, tol=0.010525890823125987;, score=0.978 total time=   2.1s
[CV 3/3; 26/50] START C=0.01867505990141344, class_weight=None, l1_ratio=0.75, tol=0.010525890823125987
[CV 3/3; 26/50] END C=0.01867505990141344, class_weight=None, l1_ratio=0.75, tol=0.010525890823125987;, score=0.942 total time=   1.7s
[CV 1/3; 27/50] START C=0.003652179634641305, class_weight=None, l1_ratio=0.5, tol=0.016847269016677012
[CV 1/3; 27/50] END C=0.003652179634641305, class_weight=None, l1_ratio=0.5, tol=0.016847269016677012;, score=0.903 total time=   1.4s
[CV 2/3; 27/50] START C=0.003652179634641305, class_weight=None, l1_ratio=0.5, tol=0.016847269016677012
[CV 2/3; 27/50] END C=0.003652179634641305, class_weight=None, l1_ratio=0.5, tol=0.016847269016677012;, score=0.918 total time=   1.2s
[CV 3/3; 27/50] START C=0.003652179634641305, class_weight=None, l1_ratio=0.5, tol=0.016847269016677012
[CV 3/3; 27/50] END C=0.003652179634641305, class_weight=None, l1_ratio=0.5, tol=0.016847269016677012;, score=0.881 total time=   1.2s
[CV 1/3; 28/50] START C=0.0034258287976066987, class_weight=None, l1_ratio=1.0, tol=0.052118083009653114
[CV 1/3; 28/50] END C=0.0034258287976066987, class_weight=None, l1_ratio=1.0, tol=0.052118083009653114;, score=0.872 total time=   0.7s
[CV 2/3; 28/50] START C=0.0034258287976066987, class_weight=None, l1_ratio=1.0, tol=0.052118083009653114
[CV 2/3; 28/50] END C=0.0034258287976066987, class_weight=None, l1_ratio=1.0, tol=0.052118083009653114;, score=0.905 total time=   0.9s
[CV 3/3; 28/50] START C=0.0034258287976066987, class_weight=None, l1_ratio=1.0, tol=0.052118083009653114
[CV 3/3; 28/50] END C=0.0034258287976066987, class_weight=None, l1_ratio=1.0, tol=0.052118083009653114;, score=0.865 total time=   0.8s
[CV 1/3; 29/50] START C=0.004738986411808208, class_weight=None, l1_ratio=0.5, tol=0.05673055136490322
[CV 1/3; 29/50] END C=0.004738986411808208, class_weight=None, l1_ratio=0.5, tol=0.05673055136490322;, score=0.929 total time=   0.6s
[CV 2/3; 29/50] START C=0.004738986411808208, class_weight=None, l1_ratio=0.5, tol=0.05673055136490322
[CV 2/3; 29/50] END C=0.004738986411808208, class_weight=None, l1_ratio=0.5, tol=0.05673055136490322;, score=0.941 total time=   0.6s
[CV 3/3; 29/50] START C=0.004738986411808208, class_weight=None, l1_ratio=0.5, tol=0.05673055136490322
[CV 3/3; 29/50] END C=0.004738986411808208, class_weight=None, l1_ratio=0.5, tol=0.05673055136490322;, score=0.897 total time=   0.6s
[CV 1/3; 30/50] START C=0.9822668410364551, class_weight=None, l1_ratio=0.5, tol=0.0035037017347077535
[CV 1/3; 30/50] END C=0.9822668410364551, class_weight=None, l1_ratio=0.5, tol=0.0035037017347077535;, score=0.802 total time=   4.8s
[CV 2/3; 30/50] START C=0.9822668410364551, class_weight=None, l1_ratio=0.5, tol=0.0035037017347077535
[CV 2/3; 30/50] END C=0.9822668410364551, class_weight=None, l1_ratio=0.5, tol=0.0035037017347077535;, score=0.989 total time=   4.8s
[CV 3/3; 30/50] START C=0.9822668410364551, class_weight=None, l1_ratio=0.5, tol=0.0035037017347077535
[CV 3/3; 30/50] END C=0.9822668410364551, class_weight=None, l1_ratio=0.5, tol=0.0035037017347077535;, score=0.969 total time=   5.1s
[CV 1/3; 31/50] START C=1.5217342777221403, class_weight=balanced, l1_ratio=0.75, tol=0.054987091381956114
[CV 1/3; 31/50] END C=1.5217342777221403, class_weight=balanced, l1_ratio=0.75, tol=0.054987091381956114;, score=0.750 total time=   0.7s
[CV 2/3; 31/50] START C=1.5217342777221403, class_weight=balanced, l1_ratio=0.75, tol=0.054987091381956114
[CV 2/3; 31/50] END C=1.5217342777221403, class_weight=balanced, l1_ratio=0.75, tol=0.054987091381956114;, score=0.990 total time=   0.8s
[CV 3/3; 31/50] START C=1.5217342777221403, class_weight=balanced, l1_ratio=0.75, tol=0.054987091381956114
[CV 3/3; 31/50] END C=1.5217342777221403, class_weight=balanced, l1_ratio=0.75, tol=0.054987091381956114;, score=0.957 total time=   0.8s
[CV 1/3; 32/50] START C=0.0016276649982237554, class_weight=None, l1_ratio=1.0, tol=0.020568137709768577
[CV 1/3; 32/50] END C=0.0016276649982237554, class_weight=None, l1_ratio=1.0, tol=0.020568137709768577;, score=0.827 total time=   1.2s
[CV 2/3; 32/50] START C=0.0016276649982237554, class_weight=None, l1_ratio=1.0, tol=0.020568137709768577
[CV 2/3; 32/50] END C=0.0016276649982237554, class_weight=None, l1_ratio=1.0, tol=0.020568137709768577;, score=0.886 total time=   0.9s
[CV 3/3; 32/50] START C=0.0016276649982237554, class_weight=None, l1_ratio=1.0, tol=0.020568137709768577
[CV 3/3; 32/50] END C=0.0016276649982237554, class_weight=None, l1_ratio=1.0, tol=0.020568137709768577;, score=0.846 total time=   1.2s
[CV 1/3; 33/50] START C=0.06020303708553688, class_weight=None, l1_ratio=0.75, tol=0.02449914419400834
[CV 1/3; 33/50] END C=0.06020303708553688, class_weight=None, l1_ratio=0.75, tol=0.02449914419400834;, score=0.876 total time=   1.1s
[CV 2/3; 33/50] START C=0.06020303708553688, class_weight=None, l1_ratio=0.75, tol=0.02449914419400834
[CV 2/3; 33/50] END C=0.06020303708553688, class_weight=None, l1_ratio=0.75, tol=0.02449914419400834;, score=0.986 total time=   1.3s
[CV 3/3; 33/50] START C=0.06020303708553688, class_weight=None, l1_ratio=0.75, tol=0.02449914419400834
[CV 3/3; 33/50] END C=0.06020303708553688, class_weight=None, l1_ratio=0.75, tol=0.02449914419400834;, score=0.951 total time=   1.3s
[CV 1/3; 34/50] START C=0.007027973784068397, class_weight=None, l1_ratio=0.25, tol=0.02241795012223404
[CV 1/3; 34/50] END C=0.007027973784068397, class_weight=None, l1_ratio=0.25, tol=0.02241795012223404;, score=0.940 total time=   0.8s
[CV 2/3; 34/50] START C=0.007027973784068397, class_weight=None, l1_ratio=0.25, tol=0.02241795012223404
[CV 2/3; 34/50] END C=0.007027973784068397, class_weight=None, l1_ratio=0.25, tol=0.02241795012223404;, score=0.969 total time=   0.8s
[CV 3/3; 34/50] START C=0.007027973784068397, class_weight=None, l1_ratio=0.25, tol=0.02241795012223404
[CV 3/3; 34/50] END C=0.007027973784068397, class_weight=None, l1_ratio=0.25, tol=0.02241795012223404;, score=0.937 total time=   0.8s
[CV 1/3; 35/50] START C=0.7186337962715937, class_weight=None, l1_ratio=0.0, tol=0.0017489947886684526
[CV 1/3; 35/50] END C=0.7186337962715937, class_weight=None, l1_ratio=0.0, tol=0.0017489947886684526;, score=0.781 total time=   4.8s
[CV 2/3; 35/50] START C=0.7186337962715937, class_weight=None, l1_ratio=0.0, tol=0.0017489947886684526
[CV 2/3; 35/50] END C=0.7186337962715937, class_weight=None, l1_ratio=0.0, tol=0.0017489947886684526;, score=0.990 total time=   5.4s
[CV 3/3; 35/50] START C=0.7186337962715937, class_weight=None, l1_ratio=0.0, tol=0.0017489947886684526
[CV 3/3; 35/50] END C=0.7186337962715937, class_weight=None, l1_ratio=0.0, tol=0.0017489947886684526;, score=0.972 total time=   5.9s
[CV 1/3; 36/50] START C=0.0074569124790931345, class_weight=None, l1_ratio=0.5, tol=0.0040136315047229615
[CV 1/3; 36/50] END C=0.0074569124790931345, class_weight=None, l1_ratio=0.5, tol=0.0040136315047229615;, score=0.932 total time=   3.1s
[CV 2/3; 36/50] START C=0.0074569124790931345, class_weight=None, l1_ratio=0.5, tol=0.0040136315047229615
[CV 2/3; 36/50] END C=0.0074569124790931345, class_weight=None, l1_ratio=0.5, tol=0.0040136315047229615;, score=0.962 total time=   3.2s
[CV 3/3; 36/50] START C=0.0074569124790931345, class_weight=None, l1_ratio=0.5, tol=0.0040136315047229615
[CV 3/3; 36/50] END C=0.0074569124790931345, class_weight=None, l1_ratio=0.5, tol=0.0040136315047229615;, score=0.920 total time=   2.8s
[CV 1/3; 37/50] START C=0.08247601689123883, class_weight=None, l1_ratio=0.75, tol=0.026122455462084266
[CV 1/3; 37/50] END C=0.08247601689123883, class_weight=None, l1_ratio=0.75, tol=0.026122455462084266;, score=0.891 total time=   1.0s
[CV 2/3; 37/50] START C=0.08247601689123883, class_weight=None, l1_ratio=0.75, tol=0.026122455462084266
[CV 2/3; 37/50] END C=0.08247601689123883, class_weight=None, l1_ratio=0.75, tol=0.026122455462084266;, score=0.985 total time=   1.0s
[CV 3/3; 37/50] START C=0.08247601689123883, class_weight=None, l1_ratio=0.75, tol=0.026122455462084266
[CV 3/3; 37/50] END C=0.08247601689123883, class_weight=None, l1_ratio=0.75, tol=0.026122455462084266;, score=0.952 total time=   1.2s
[CV 1/3; 38/50] START C=0.24885881167739285, class_weight=None, l1_ratio=1.0, tol=0.00906404448358285
[CV 1/3; 38/50] END C=0.24885881167739285, class_weight=None, l1_ratio=1.0, tol=0.00906404448358285;, score=0.822 total time=   2.1s
[CV 2/3; 38/50] START C=0.24885881167739285, class_weight=None, l1_ratio=1.0, tol=0.00906404448358285
[CV 2/3; 38/50] END C=0.24885881167739285, class_weight=None, l1_ratio=1.0, tol=0.00906404448358285;, score=0.988 total time=   2.4s
[CV 3/3; 38/50] START C=0.24885881167739285, class_weight=None, l1_ratio=1.0, tol=0.00906404448358285
[CV 3/3; 38/50] END C=0.24885881167739285, class_weight=None, l1_ratio=1.0, tol=0.00906404448358285;, score=0.959 total time=   2.6s
[CV 1/3; 39/50] START C=0.08768479153766093, class_weight=balanced, l1_ratio=1.0, tol=0.002032472272087387
[CV 1/3; 39/50] END C=0.08768479153766093, class_weight=balanced, l1_ratio=1.0, tol=0.002032472272087387;, score=0.615 total time=   7.9s
[CV 2/3; 39/50] START C=0.08768479153766093, class_weight=balanced, l1_ratio=1.0, tol=0.002032472272087387
[CV 2/3; 39/50] END C=0.08768479153766093, class_weight=balanced, l1_ratio=1.0, tol=0.002032472272087387;, score=0.990 total time=   9.3s
[CV 3/3; 39/50] START C=0.08768479153766093, class_weight=balanced, l1_ratio=1.0, tol=0.002032472272087387
[CV 3/3; 39/50] END C=0.08768479153766093, class_weight=balanced, l1_ratio=1.0, tol=0.002032472272087387;, score=0.952 total time=   7.8s
[CV 1/3; 40/50] START C=0.05075098447194432, class_weight=None, l1_ratio=0.5, tol=0.09976617054880073
[CV 1/3; 40/50] END C=0.05075098447194432, class_weight=None, l1_ratio=0.5, tol=0.09976617054880073;, score=0.935 total time=   0.6s
[CV 2/3; 40/50] START C=0.05075098447194432, class_weight=None, l1_ratio=0.5, tol=0.09976617054880073
[CV 2/3; 40/50] END C=0.05075098447194432, class_weight=None, l1_ratio=0.5, tol=0.09976617054880073;, score=0.983 total time=   0.5s
[CV 3/3; 40/50] START C=0.05075098447194432, class_weight=None, l1_ratio=0.5, tol=0.09976617054880073
[CV 3/3; 40/50] END C=0.05075098447194432, class_weight=None, l1_ratio=0.5, tol=0.09976617054880073;, score=0.949 total time=   0.6s
[CV 1/3; 41/50] START C=0.002144332863396596, class_weight=None, l1_ratio=0.5, tol=0.03698282397062603
[CV 1/3; 41/50] END C=0.002144332863396596, class_weight=None, l1_ratio=0.5, tol=0.03698282397062603;, score=0.873 total time=   1.0s
[CV 2/3; 41/50] START C=0.002144332863396596, class_weight=None, l1_ratio=0.5, tol=0.03698282397062603
[CV 2/3; 41/50] END C=0.002144332863396596, class_weight=None, l1_ratio=0.5, tol=0.03698282397062603;, score=0.907 total time=   0.9s
[CV 3/3; 41/50] START C=0.002144332863396596, class_weight=None, l1_ratio=0.5, tol=0.03698282397062603
[CV 3/3; 41/50] END C=0.002144332863396596, class_weight=None, l1_ratio=0.5, tol=0.03698282397062603;, score=0.872 total time=   0.9s
[CV 1/3; 42/50] START C=0.43898163114257244, class_weight=balanced, l1_ratio=0.5, tol=0.01174352928145076
[CV 1/3; 42/50] END C=0.43898163114257244, class_weight=balanced, l1_ratio=0.5, tol=0.01174352928145076;, score=0.707 total time=   1.5s
[CV 2/3; 42/50] START C=0.43898163114257244, class_weight=balanced, l1_ratio=0.5, tol=0.01174352928145076
[CV 2/3; 42/50] END C=0.43898163114257244, class_weight=balanced, l1_ratio=0.5, tol=0.01174352928145076;, score=0.990 total time=   1.4s
[CV 3/3; 42/50] START C=0.43898163114257244, class_weight=balanced, l1_ratio=0.5, tol=0.01174352928145076
[CV 3/3; 42/50] END C=0.43898163114257244, class_weight=balanced, l1_ratio=0.5, tol=0.01174352928145076;, score=0.957 total time=   1.0s
[CV 1/3; 43/50] START C=0.0013924288469168856, class_weight=balanced, l1_ratio=0.0, tol=0.018865131349757914
[CV 1/3; 43/50] END C=0.0013924288469168856, class_weight=balanced, l1_ratio=0.0, tol=0.018865131349757914;, score=0.759 total time=   1.7s
[CV 2/3; 43/50] START C=0.0013924288469168856, class_weight=balanced, l1_ratio=0.0, tol=0.018865131349757914
[CV 2/3; 43/50] END C=0.0013924288469168856, class_weight=balanced, l1_ratio=0.0, tol=0.018865131349757914;, score=0.991 total time=  36.9s
[CV 3/3; 43/50] START C=0.0013924288469168856, class_weight=balanced, l1_ratio=0.0, tol=0.018865131349757914
[CV 3/3; 43/50] END C=0.0013924288469168856, class_weight=balanced, l1_ratio=0.0, tol=0.018865131349757914;, score=0.944 total time=  39.1s
[CV 1/3; 44/50] START C=0.008172568535086506, class_weight=None, l1_ratio=0.25, tol=0.005768682795378904
[CV 1/3; 44/50] END C=0.008172568535086506, class_weight=None, l1_ratio=0.25, tol=0.005768682795378904;, score=0.932 total time=   2.3s
[CV 2/3; 44/50] START C=0.008172568535086506, class_weight=None, l1_ratio=0.25, tol=0.005768682795378904
[CV 2/3; 44/50] END C=0.008172568535086506, class_weight=None, l1_ratio=0.25, tol=0.005768682795378904;, score=0.973 total time=   2.6s
[CV 3/3; 44/50] START C=0.008172568535086506, class_weight=None, l1_ratio=0.25, tol=0.005768682795378904
[CV 3/3; 44/50] END C=0.008172568535086506, class_weight=None, l1_ratio=0.25, tol=0.005768682795378904;, score=0.939 total time=   2.3s
[CV 1/3; 45/50] START C=0.0010342858472308363, class_weight=balanced, l1_ratio=1.0, tol=0.06921092058077323
[CV 1/3; 45/50] END C=0.0010342858472308363, class_weight=balanced, l1_ratio=1.0, tol=0.06921092058077323;, score=0.422 total time=   1.7s
[CV 2/3; 45/50] START C=0.0010342858472308363, class_weight=balanced, l1_ratio=1.0, tol=0.06921092058077323
[CV 2/3; 45/50] END C=0.0010342858472308363, class_weight=balanced, l1_ratio=1.0, tol=0.06921092058077323;, score=0.442 total time=   1.6s
[CV 3/3; 45/50] START C=0.0010342858472308363, class_weight=balanced, l1_ratio=1.0, tol=0.06921092058077323
[CV 3/3; 45/50] END C=0.0010342858472308363, class_weight=balanced, l1_ratio=1.0, tol=0.06921092058077323;, score=0.405 total time=   1.3s
[CV 1/3; 46/50] START C=0.010870505673043335, class_weight=balanced, l1_ratio=0.75, tol=0.0625516763040173
[CV 1/3; 46/50] END C=0.010870505673043335, class_weight=balanced, l1_ratio=0.75, tol=0.0625516763040173;, score=0.615 total time=   0.8s
[CV 2/3; 46/50] START C=0.010870505673043335, class_weight=balanced, l1_ratio=0.75, tol=0.0625516763040173
[CV 2/3; 46/50] END C=0.010870505673043335, class_weight=balanced, l1_ratio=0.75, tol=0.0625516763040173;, score=0.988 total time=   1.7s
[CV 3/3; 46/50] START C=0.010870505673043335, class_weight=balanced, l1_ratio=0.75, tol=0.0625516763040173
[CV 3/3; 46/50] END C=0.010870505673043335, class_weight=balanced, l1_ratio=0.75, tol=0.0625516763040173;, score=0.949 total time=   1.0s
[CV 1/3; 47/50] START C=0.14901804910443534, class_weight=None, l1_ratio=0.75, tol=0.005732920129270331
[CV 1/3; 47/50] END C=0.14901804910443534, class_weight=None, l1_ratio=0.75, tol=0.005732920129270331;, score=0.793 total time=   2.8s
[CV 2/3; 47/50] START C=0.14901804910443534, class_weight=None, l1_ratio=0.75, tol=0.005732920129270331
[CV 2/3; 47/50] END C=0.14901804910443534, class_weight=None, l1_ratio=0.75, tol=0.005732920129270331;, score=0.988 total time=   4.4s
[CV 3/3; 47/50] START C=0.14901804910443534, class_weight=None, l1_ratio=0.75, tol=0.005732920129270331
[CV 3/3; 47/50] END C=0.14901804910443534, class_weight=None, l1_ratio=0.75, tol=0.005732920129270331;, score=0.957 total time=   3.7s
[CV 1/3; 48/50] START C=0.5655386760154387, class_weight=None, l1_ratio=0.5, tol=0.012825342729092372
[CV 1/3; 48/50] END C=0.5655386760154387, class_weight=None, l1_ratio=0.5, tol=0.012825342729092372;, score=0.875 total time=   1.7s
[CV 2/3; 48/50] START C=0.5655386760154387, class_weight=None, l1_ratio=0.5, tol=0.012825342729092372
[CV 2/3; 48/50] END C=0.5655386760154387, class_weight=None, l1_ratio=0.5, tol=0.012825342729092372;, score=0.988 total time=   1.5s
[CV 3/3; 48/50] START C=0.5655386760154387, class_weight=None, l1_ratio=0.5, tol=0.012825342729092372
[CV 3/3; 48/50] END C=0.5655386760154387, class_weight=None, l1_ratio=0.5, tol=0.012825342729092372;, score=0.962 total time=   1.5s
[CV 1/3; 49/50] START C=0.46527918762854226, class_weight=balanced, l1_ratio=0.0, tol=0.09678309001444518
[CV 1/3; 49/50] END C=0.46527918762854226, class_weight=balanced, l1_ratio=0.0, tol=0.09678309001444518;, score=0.739 total time=   0.5s
[CV 2/3; 49/50] START C=0.46527918762854226, class_weight=balanced, l1_ratio=0.0, tol=0.09678309001444518
[CV 2/3; 49/50] END C=0.46527918762854226, class_weight=balanced, l1_ratio=0.0, tol=0.09678309001444518;, score=0.990 total time=   0.5s
[CV 3/3; 49/50] START C=0.46527918762854226, class_weight=balanced, l1_ratio=0.0, tol=0.09678309001444518
[CV 3/3; 49/50] END C=0.46527918762854226, class_weight=balanced, l1_ratio=0.0, tol=0.09678309001444518;, score=0.958 total time=   0.7s
[CV 1/3; 50/50] START C=0.01853121637142899, class_weight=None, l1_ratio=0.5, tol=0.048041749337683584
[CV 1/3; 50/50] END C=0.01853121637142899, class_weight=None, l1_ratio=0.5, tol=0.048041749337683584;, score=0.922 total time=   0.7s
[CV 2/3; 50/50] START C=0.01853121637142899, class_weight=None, l1_ratio=0.5, tol=0.048041749337683584
[CV 2/3; 50/50] END C=0.01853121637142899, class_weight=None, l1_ratio=0.5, tol=0.048041749337683584;, score=0.979 total time=   0.8s
[CV 3/3; 50/50] START C=0.01853121637142899, class_weight=None, l1_ratio=0.5, tol=0.048041749337683584
[CV 3/3; 50/50] END C=0.01853121637142899, class_weight=None, l1_ratio=0.5, tol=0.048041749337683584;, score=0.944 total time=   0.7s

--- TUNING FINISHED ---
Beste Parameter: {'C': np.float64(0.05075098447194432), 'class_weight': None, 'l1_ratio': 0.5, 'tol': np.float64(0.09976617054880073)}
Bester CV-Score: 0.9559

--- EVALUATION AUF DEN TESTDATEN ---
Test Accuracy: 0.8910

Macro F1: 0.849982615422788

--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.8910

                     precision    recall  f1-score   support

             B cell       0.99      0.98      0.99       120
     CD14+ monocyte       1.00      1.00      1.00      2575
        CD4+ T cell       0.85      0.99      0.92      3910
   Cytotoxic T cell       0.94      0.50      0.66      1824
     Dendritic cell       1.00      0.40      0.57         5
      Megakaryocyte       1.00      1.00      1.00         7
Natural killer cell       0.74      0.92      0.82       791
        Plasma cell       0.97      0.76      0.85        49

           accuracy                           0.89      9281
          macro avg       0.94      0.82      0.85      9281
       weighted avg       0.90      0.89      0.88      9281

Random dropout accuracy score 0.8830
Total samples: 9281
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.8891
Feature importance dropout (0.5% features dropped) accuracy score 0.8657
Feature importance dropout (1.0% features dropped) accuracy score 0.8481
Feature importance dropout (2.0% features dropped) accuracy score 0.8130
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8620

                     precision    recall  f1-score   support

             B cell       1.00      0.99      1.00      3959
     CD14+ monocyte       0.93      1.00      0.96      3135
        CD4+ T cell       0.88      1.00      0.94     13664
   Cytotoxic T cell       0.62      0.62      0.62      4839
     Dendritic cell       0.99      0.67      0.80       529
      Megakaryocyte       1.00      0.63      0.77        86
Natural killer cell       0.90      0.31      0.46      2751
        Plasma cell       1.00      0.78      0.88        23

           accuracy                           0.86     28986
          macro avg       0.92      0.75      0.80     28986
       weighted avg       0.86      0.86      0.85     28986

Random dropout accuracy score 0.8495
Total samples: 28986
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.8612
Feature importance dropout (0.5% features dropped) accuracy score 0.8347
Feature importance dropout (1.0% features dropped) accuracy score 0.8109
Feature importance dropout (2.0% features dropped) accuracy score 0.6964
=== JOB_STATISTICS ===
=== current date     : Mon Jun 29 00:59:45 CEST 2026
= Job-ID             : 11997753 on woody
= Job-Name           : autoencoder_lr
= Job-Command        : /home/hpc/iwbn/iwbn133h/submit_autoencoder_lr_v1.sh
= Initial workdir    : /home/hpc/iwbn/iwbn133h
= Queue/Partition    : work
= Slurm account      : iwbn with QOS=normal
= Features           : icx
= Requested resources:  for 17:00:00
= Elapsed runtime    : 02:44:35
= Total RAM usage    : 19.0 GiB of requested  GiB (%)   
= Node list          : w2206
= Subm/Elig/Start/End: 2026-06-28T22:15:09 / 2026-06-28T22:15:09 / 2026-06-28T22:15:10 / 2026-06-29T00:59:45
======================
=== Quota infos ======
    Path                 Used     SoftQ    HardQ    Gracetime  Filec    FileQ    FiHaQ    FileGrace    
    /home/woody           982.1M  1000.0G  1500.0G        N/A  29,019    5,000K   7,500K        N/A    
    /home/hpc              86.2G   104.9G   209.7G        N/A     139K     500K   1,000K        N/A    
    /home/vault             0.0K  1048.6G  2097.2G        N/A       1      200K     400K        N/A    
