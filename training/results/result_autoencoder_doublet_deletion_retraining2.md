### Starting TaskPrologue of job 12000011 on w2314 at Mon Jun 29 09:08:36 CEST 2026
#   SLURM_JOB_NODELIST=w2314
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
Epoch [1/150], Loss: 0.9520
Epoch [10/150], Loss: 0.9057
Epoch [20/150], Loss: 0.8915
Epoch [30/150], Loss: 0.8833
Epoch [40/150], Loss: 0.8782
Epoch [50/150], Loss: 0.8746
Epoch [60/150], Loss: 0.8720
Epoch [70/150], Loss: 0.8698
Epoch [80/150], Loss: 0.8677
Epoch [90/150], Loss: 0.8664
Epoch [100/150], Loss: 0.8649
Epoch [110/150], Loss: 0.8641
Epoch [120/150], Loss: 0.8626
Epoch [130/150], Loss: 0.8618
Epoch [140/150], Loss: 0.8607
Epoch [150/150], Loss: 0.8601

Extract robust features...
Starte automatische Hyperparametersuche auf dem Latent Space...
Fitting 3 folds for each of 50 candidates, totalling 150 fits
[CV 1/3; 1/50] START C=0.08598409911703409, class_weight=None, l1_ratio=0.75, tol=0.072424692332114
[CV 1/3; 1/50] END C=0.08598409911703409, class_weight=None, l1_ratio=0.75, tol=0.072424692332114;, score=0.951 total time=   0.5s
[CV 2/3; 1/50] START C=0.08598409911703409, class_weight=None, l1_ratio=0.75, tol=0.072424692332114
[CV 2/3; 1/50] END C=0.08598409911703409, class_weight=None, l1_ratio=0.75, tol=0.072424692332114;, score=0.980 total time=   0.5s
[CV 3/3; 1/50] START C=0.08598409911703409, class_weight=None, l1_ratio=0.75, tol=0.072424692332114
[CV 3/3; 1/50] END C=0.08598409911703409, class_weight=None, l1_ratio=0.75, tol=0.072424692332114;, score=0.952 total time=   0.6s
[CV 1/3; 2/50] START C=0.5486121249310815, class_weight=None, l1_ratio=0.0, tol=0.008854102445599666
[CV 1/3; 2/50] END C=0.5486121249310815, class_weight=None, l1_ratio=0.0, tol=0.008854102445599666;, score=0.891 total time=   1.3s
[CV 2/3; 2/50] START C=0.5486121249310815, class_weight=None, l1_ratio=0.0, tol=0.008854102445599666
[CV 2/3; 2/50] END C=0.5486121249310815, class_weight=None, l1_ratio=0.0, tol=0.008854102445599666;, score=0.989 total time=   1.7s
[CV 3/3; 2/50] START C=0.5486121249310815, class_weight=None, l1_ratio=0.0, tol=0.008854102445599666
[CV 3/3; 2/50] END C=0.5486121249310815, class_weight=None, l1_ratio=0.0, tol=0.008854102445599666;, score=0.959 total time=   1.6s
[CV 1/3; 3/50] START C=0.03498608441520707, class_weight=balanced, l1_ratio=0.5, tol=0.01429348960839428
[CV 1/3; 3/50] END C=0.03498608441520707, class_weight=balanced, l1_ratio=0.5, tol=0.01429348960839428;, score=0.856 total time=   1.5s
[CV 2/3; 3/50] START C=0.03498608441520707, class_weight=balanced, l1_ratio=0.5, tol=0.01429348960839428
[CV 2/3; 3/50] END C=0.03498608441520707, class_weight=balanced, l1_ratio=0.5, tol=0.01429348960839428;, score=0.990 total time=   1.6s
[CV 3/3; 3/50] START C=0.03498608441520707, class_weight=balanced, l1_ratio=0.5, tol=0.01429348960839428
[CV 3/3; 3/50] END C=0.03498608441520707, class_weight=balanced, l1_ratio=0.5, tol=0.01429348960839428;, score=0.950 total time=   1.7s
[CV 1/3; 4/50] START C=0.005367030603255032, class_weight=None, l1_ratio=0.75, tol=0.03267478304458455
[CV 1/3; 4/50] END C=0.005367030603255032, class_weight=None, l1_ratio=0.75, tol=0.03267478304458455;, score=0.939 total time=   0.8s
[CV 2/3; 4/50] START C=0.005367030603255032, class_weight=None, l1_ratio=0.75, tol=0.03267478304458455
[CV 2/3; 4/50] END C=0.005367030603255032, class_weight=None, l1_ratio=0.75, tol=0.03267478304458455;, score=0.944 total time=   0.8s
[CV 3/3; 4/50] START C=0.005367030603255032, class_weight=None, l1_ratio=0.75, tol=0.03267478304458455
[CV 3/3; 4/50] END C=0.005367030603255032, class_weight=None, l1_ratio=0.75, tol=0.03267478304458455;, score=0.909 total time=   0.8s
[CV 1/3; 5/50] START C=0.5166700017459332, class_weight=None, l1_ratio=1.0, tol=0.0023372496210957213
[CV 1/3; 5/50] END C=0.5166700017459332, class_weight=None, l1_ratio=1.0, tol=0.0023372496210957213;, score=0.776 total time=  10.7s
[CV 2/3; 5/50] START C=0.5166700017459332, class_weight=None, l1_ratio=1.0, tol=0.0023372496210957213
[CV 2/3; 5/50] END C=0.5166700017459332, class_weight=None, l1_ratio=1.0, tol=0.0023372496210957213;, score=0.990 total time=   9.3s
[CV 3/3; 5/50] START C=0.5166700017459332, class_weight=None, l1_ratio=1.0, tol=0.0023372496210957213
[CV 3/3; 5/50] END C=0.5166700017459332, class_weight=None, l1_ratio=1.0, tol=0.0023372496210957213;, score=0.963 total time=   9.9s
[CV 1/3; 6/50] START C=0.16122690396511483, class_weight=balanced, l1_ratio=0.5, tol=0.09565886740189382
[CV 1/3; 6/50] END C=0.16122690396511483, class_weight=balanced, l1_ratio=0.5, tol=0.09565886740189382;, score=0.865 total time=   0.5s
[CV 2/3; 6/50] START C=0.16122690396511483, class_weight=balanced, l1_ratio=0.5, tol=0.09565886740189382
[CV 2/3; 6/50] END C=0.16122690396511483, class_weight=balanced, l1_ratio=0.5, tol=0.09565886740189382;, score=0.990 total time=   0.6s
[CV 3/3; 6/50] START C=0.16122690396511483, class_weight=balanced, l1_ratio=0.5, tol=0.09565886740189382
[CV 3/3; 6/50] END C=0.16122690396511483, class_weight=balanced, l1_ratio=0.5, tol=0.09565886740189382;, score=0.948 total time=   0.6s
[CV 1/3; 7/50] START C=0.009475925363822921, class_weight=None, l1_ratio=0.75, tol=0.019936838069744167
[CV 1/3; 7/50] END C=0.009475925363822921, class_weight=None, l1_ratio=0.75, tol=0.019936838069744167;, score=0.948 total time=   0.9s
[CV 2/3; 7/50] START C=0.009475925363822921, class_weight=None, l1_ratio=0.75, tol=0.019936838069744167
[CV 2/3; 7/50] END C=0.009475925363822921, class_weight=None, l1_ratio=0.75, tol=0.019936838069744167;, score=0.960 total time=   1.0s
[CV 3/3; 7/50] START C=0.009475925363822921, class_weight=None, l1_ratio=0.75, tol=0.019936838069744167
[CV 3/3; 7/50] END C=0.009475925363822921, class_weight=None, l1_ratio=0.75, tol=0.019936838069744167;, score=0.929 total time=   1.0s
[CV 1/3; 8/50] START C=0.7123270538360073, class_weight=None, l1_ratio=0.0, tol=0.05631638148689078
[CV 1/3; 8/50] END C=0.7123270538360073, class_weight=None, l1_ratio=0.0, tol=0.05631638148689078;, score=0.942 total time=   0.5s
[CV 2/3; 8/50] START C=0.7123270538360073, class_weight=None, l1_ratio=0.0, tol=0.05631638148689078
[CV 2/3; 8/50] END C=0.7123270538360073, class_weight=None, l1_ratio=0.0, tol=0.05631638148689078;, score=0.984 total time=   0.5s
[CV 3/3; 8/50] START C=0.7123270538360073, class_weight=None, l1_ratio=0.0, tol=0.05631638148689078
[CV 3/3; 8/50] END C=0.7123270538360073, class_weight=None, l1_ratio=0.0, tol=0.05631638148689078;, score=0.953 total time=   0.5s
[CV 1/3; 9/50] START C=0.0031745257561040033, class_weight=balanced, l1_ratio=1.0, tol=0.0019539270099593383
[CV 1/3; 9/50] END C=0.0031745257561040033, class_weight=balanced, l1_ratio=1.0, tol=0.0019539270099593383;, score=0.888 total time=   2.5s
[CV 2/3; 9/50] START C=0.0031745257561040033, class_weight=balanced, l1_ratio=1.0, tol=0.0019539270099593383
[CV 2/3; 9/50] END C=0.0031745257561040033, class_weight=balanced, l1_ratio=1.0, tol=0.0019539270099593383;, score=0.951 total time=  20.2s
[CV 3/3; 9/50] START C=0.0031745257561040033, class_weight=balanced, l1_ratio=1.0, tol=0.0019539270099593383
[CV 3/3; 9/50] END C=0.0031745257561040033, class_weight=balanced, l1_ratio=1.0, tol=0.0019539270099593383;, score=0.903 total time=  59.3s
[CV 1/3; 10/50] START C=0.06647514742548473, class_weight=None, l1_ratio=0.5, tol=0.0023748450339655582
[CV 1/3; 10/50] END C=0.06647514742548473, class_weight=None, l1_ratio=0.5, tol=0.0023748450339655582;, score=0.911 total time=   5.3s
[CV 2/3; 10/50] START C=0.06647514742548473, class_weight=None, l1_ratio=0.5, tol=0.0023748450339655582
[CV 2/3; 10/50] END C=0.06647514742548473, class_weight=None, l1_ratio=0.5, tol=0.0023748450339655582;, score=0.984 total time=   4.5s
[CV 3/3; 10/50] START C=0.06647514742548473, class_weight=None, l1_ratio=0.5, tol=0.0023748450339655582
[CV 3/3; 10/50] END C=0.06647514742548473, class_weight=None, l1_ratio=0.5, tol=0.0023748450339655582;, score=0.956 total time=   4.3s
[CV 1/3; 11/50] START C=0.6736266648390306, class_weight=None, l1_ratio=0.25, tol=0.05925716901595763
[CV 1/3; 11/50] END C=0.6736266648390306, class_weight=None, l1_ratio=0.25, tol=0.05925716901595763;, score=0.943 total time=   0.7s
[CV 2/3; 11/50] START C=0.6736266648390306, class_weight=None, l1_ratio=0.25, tol=0.05925716901595763
[CV 2/3; 11/50] END C=0.6736266648390306, class_weight=None, l1_ratio=0.25, tol=0.05925716901595763;, score=0.982 total time=   0.6s
[CV 3/3; 11/50] START C=0.6736266648390306, class_weight=None, l1_ratio=0.25, tol=0.05925716901595763
[CV 3/3; 11/50] END C=0.6736266648390306, class_weight=None, l1_ratio=0.25, tol=0.05925716901595763;, score=0.953 total time=   0.6s
[CV 1/3; 12/50] START C=0.1933581911578089, class_weight=balanced, l1_ratio=0.5, tol=0.0011457208973199003
[CV 1/3; 12/50] END C=0.1933581911578089, class_weight=balanced, l1_ratio=0.5, tol=0.0011457208973199003;, score=0.730 total time=  11.7s
[CV 2/3; 12/50] START C=0.1933581911578089, class_weight=balanced, l1_ratio=0.5, tol=0.0011457208973199003
[CV 2/3; 12/50] END C=0.1933581911578089, class_weight=balanced, l1_ratio=0.5, tol=0.0011457208973199003;, score=0.991 total time=  12.9s
[CV 3/3; 12/50] START C=0.1933581911578089, class_weight=balanced, l1_ratio=0.5, tol=0.0011457208973199003
[CV 3/3; 12/50] END C=0.1933581911578089, class_weight=balanced, l1_ratio=0.5, tol=0.0011457208973199003;, score=0.955 total time=  16.5s
[CV 1/3; 13/50] START C=0.004377454268743107, class_weight=balanced, l1_ratio=0.5, tol=0.009728567217884431
[CV 1/3; 13/50] END C=0.004377454268743107, class_weight=balanced, l1_ratio=0.5, tol=0.009728567217884431;, score=0.915 total time=   1.3s
[CV 2/3; 13/50] START C=0.004377454268743107, class_weight=balanced, l1_ratio=0.5, tol=0.009728567217884431
[CV 2/3; 13/50] END C=0.004377454268743107, class_weight=balanced, l1_ratio=0.5, tol=0.009728567217884431;, score=0.980 total time=   3.1s
[CV 3/3; 13/50] START C=0.004377454268743107, class_weight=balanced, l1_ratio=0.5, tol=0.009728567217884431
[CV 3/3; 13/50] END C=0.004377454268743107, class_weight=balanced, l1_ratio=0.5, tol=0.009728567217884431;, score=0.937 total time=  14.6s
[CV 1/3; 14/50] START C=0.004815064941403429, class_weight=None, l1_ratio=0.25, tol=0.07335886521084674
[CV 1/3; 14/50] END C=0.004815064941403429, class_weight=None, l1_ratio=0.25, tol=0.07335886521084674;, score=0.955 total time=   0.5s
[CV 2/3; 14/50] START C=0.004815064941403429, class_weight=None, l1_ratio=0.25, tol=0.07335886521084674
[CV 2/3; 14/50] END C=0.004815064941403429, class_weight=None, l1_ratio=0.25, tol=0.07335886521084674;, score=0.958 total time=   0.5s
[CV 3/3; 14/50] START C=0.004815064941403429, class_weight=None, l1_ratio=0.25, tol=0.07335886521084674
[CV 3/3; 14/50] END C=0.004815064941403429, class_weight=None, l1_ratio=0.25, tol=0.07335886521084674;, score=0.923 total time=   0.6s
[CV 1/3; 15/50] START C=0.6428650554358417, class_weight=None, l1_ratio=0.25, tol=0.061928827621967275
[CV 1/3; 15/50] END C=0.6428650554358417, class_weight=None, l1_ratio=0.25, tol=0.061928827621967275;, score=0.941 total time=   0.6s
[CV 2/3; 15/50] START C=0.6428650554358417, class_weight=None, l1_ratio=0.25, tol=0.061928827621967275
[CV 2/3; 15/50] END C=0.6428650554358417, class_weight=None, l1_ratio=0.25, tol=0.061928827621967275;, score=0.983 total time=   0.6s
[CV 3/3; 15/50] START C=0.6428650554358417, class_weight=None, l1_ratio=0.25, tol=0.061928827621967275
[CV 3/3; 15/50] END C=0.6428650554358417, class_weight=None, l1_ratio=0.25, tol=0.061928827621967275;, score=0.953 total time=   0.6s
[CV 1/3; 16/50] START C=0.004570008642358991, class_weight=balanced, l1_ratio=0.25, tol=0.01179030537701962
[CV 1/3; 16/50] END C=0.004570008642358991, class_weight=balanced, l1_ratio=0.25, tol=0.01179030537701962;, score=0.907 total time=   4.3s
[CV 2/3; 16/50] START C=0.004570008642358991, class_weight=balanced, l1_ratio=0.25, tol=0.01179030537701962
[CV 2/3; 16/50] END C=0.004570008642358991, class_weight=balanced, l1_ratio=0.25, tol=0.01179030537701962;, score=0.985 total time=   4.1s
[CV 3/3; 16/50] START C=0.004570008642358991, class_weight=balanced, l1_ratio=0.25, tol=0.01179030537701962
[CV 3/3; 16/50] END C=0.004570008642358991, class_weight=balanced, l1_ratio=0.25, tol=0.01179030537701962;, score=0.944 total time= 1.0min
[CV 1/3; 17/50] START C=0.006838809842237949, class_weight=balanced, l1_ratio=0.75, tol=0.0025410254775717323
[CV 1/3; 17/50] END C=0.006838809842237949, class_weight=balanced, l1_ratio=0.75, tol=0.0025410254775717323;, score=0.909 total time=   7.8s
[CV 2/3; 17/50] START C=0.006838809842237949, class_weight=balanced, l1_ratio=0.75, tol=0.0025410254775717323
[CV 2/3; 17/50] END C=0.006838809842237949, class_weight=balanced, l1_ratio=0.75, tol=0.0025410254775717323;, score=0.978 total time=   5.8s
[CV 3/3; 17/50] START C=0.006838809842237949, class_weight=balanced, l1_ratio=0.75, tol=0.0025410254775717323
[CV 3/3; 17/50] END C=0.006838809842237949, class_weight=balanced, l1_ratio=0.75, tol=0.0025410254775717323;, score=0.935 total time=  29.4s
[CV 1/3; 18/50] START C=0.0036671496045529066, class_weight=None, l1_ratio=0.0, tol=0.01702214848804159
[CV 1/3; 18/50] END C=0.0036671496045529066, class_weight=None, l1_ratio=0.0, tol=0.01702214848804159;, score=0.959 total time=   0.5s
[CV 2/3; 18/50] START C=0.0036671496045529066, class_weight=None, l1_ratio=0.0, tol=0.01702214848804159
[CV 2/3; 18/50] END C=0.0036671496045529066, class_weight=None, l1_ratio=0.0, tol=0.01702214848804159;, score=0.968 total time=   0.5s
[CV 3/3; 18/50] START C=0.0036671496045529066, class_weight=None, l1_ratio=0.0, tol=0.01702214848804159
[CV 3/3; 18/50] END C=0.0036671496045529066, class_weight=None, l1_ratio=0.0, tol=0.01702214848804159;, score=0.939 total time=   0.5s
[CV 1/3; 19/50] START C=0.0012908804794309547, class_weight=None, l1_ratio=1.0, tol=0.0025703406756318217
[CV 1/3; 19/50] END C=0.0012908804794309547, class_weight=None, l1_ratio=1.0, tol=0.0025703406756318217;, score=0.839 total time=   1.8s
[CV 2/3; 19/50] START C=0.0012908804794309547, class_weight=None, l1_ratio=1.0, tol=0.0025703406756318217
[CV 2/3; 19/50] END C=0.0012908804794309547, class_weight=None, l1_ratio=1.0, tol=0.0025703406756318217;, score=0.886 total time=   2.0s
[CV 3/3; 19/50] START C=0.0012908804794309547, class_weight=None, l1_ratio=1.0, tol=0.0025703406756318217
[CV 3/3; 19/50] END C=0.0012908804794309547, class_weight=None, l1_ratio=1.0, tol=0.0025703406756318217;, score=0.833 total time=   1.8s
[CV 1/3; 20/50] START C=0.007743231574333871, class_weight=None, l1_ratio=0.5, tol=0.019789621660623178
[CV 1/3; 20/50] END C=0.007743231574333871, class_weight=None, l1_ratio=0.5, tol=0.019789621660623178;, score=0.952 total time=   0.8s
[CV 2/3; 20/50] START C=0.007743231574333871, class_weight=None, l1_ratio=0.5, tol=0.019789621660623178
[CV 2/3; 20/50] END C=0.007743231574333871, class_weight=None, l1_ratio=0.5, tol=0.019789621660623178;, score=0.960 total time=   0.9s
[CV 3/3; 20/50] START C=0.007743231574333871, class_weight=None, l1_ratio=0.5, tol=0.019789621660623178
[CV 3/3; 20/50] END C=0.007743231574333871, class_weight=None, l1_ratio=0.5, tol=0.019789621660623178;, score=0.928 total time=   0.9s
[CV 1/3; 21/50] START C=0.001156640663138696, class_weight=None, l1_ratio=1.0, tol=0.006632560875258517
[CV 1/3; 21/50] END C=0.001156640663138696, class_weight=None, l1_ratio=1.0, tol=0.006632560875258517;, score=0.827 total time=   1.7s
[CV 2/3; 21/50] START C=0.001156640663138696, class_weight=None, l1_ratio=1.0, tol=0.006632560875258517
[CV 2/3; 21/50] END C=0.001156640663138696, class_weight=None, l1_ratio=1.0, tol=0.006632560875258517;, score=0.880 total time=   1.2s
[CV 3/3; 21/50] START C=0.001156640663138696, class_weight=None, l1_ratio=1.0, tol=0.006632560875258517
[CV 3/3; 21/50] END C=0.001156640663138696, class_weight=None, l1_ratio=1.0, tol=0.006632560875258517;, score=0.827 total time=   1.4s
[CV 1/3; 22/50] START C=0.006594025206501659, class_weight=None, l1_ratio=0.75, tol=0.057510593229977494
[CV 1/3; 22/50] END C=0.006594025206501659, class_weight=None, l1_ratio=0.75, tol=0.057510593229977494;, score=0.944 total time=   0.7s
[CV 2/3; 22/50] START C=0.006594025206501659, class_weight=None, l1_ratio=0.75, tol=0.057510593229977494
[CV 2/3; 22/50] END C=0.006594025206501659, class_weight=None, l1_ratio=0.75, tol=0.057510593229977494;, score=0.952 total time=   0.7s
[CV 3/3; 22/50] START C=0.006594025206501659, class_weight=None, l1_ratio=0.75, tol=0.057510593229977494
[CV 3/3; 22/50] END C=0.006594025206501659, class_weight=None, l1_ratio=0.75, tol=0.057510593229977494;, score=0.918 total time=   0.7s
[CV 1/3; 23/50] START C=0.009749483926383497, class_weight=balanced, l1_ratio=1.0, tol=0.013729227164268616
[CV 1/3; 23/50] END C=0.009749483926383497, class_weight=balanced, l1_ratio=1.0, tol=0.013729227164268616;, score=0.908 total time=   1.4s
[CV 2/3; 23/50] START C=0.009749483926383497, class_weight=balanced, l1_ratio=1.0, tol=0.013729227164268616
[CV 2/3; 23/50] END C=0.009749483926383497, class_weight=balanced, l1_ratio=1.0, tol=0.013729227164268616;, score=0.976 total time=   9.7s
[CV 3/3; 23/50] START C=0.009749483926383497, class_weight=balanced, l1_ratio=1.0, tol=0.013729227164268616
[CV 3/3; 23/50] END C=0.009749483926383497, class_weight=balanced, l1_ratio=1.0, tol=0.013729227164268616;, score=0.930 total time=  40.1s
[CV 1/3; 24/50] START C=0.0437199421681428, class_weight=balanced, l1_ratio=0.25, tol=0.009449293684544096
[CV 1/3; 24/50] END C=0.0437199421681428, class_weight=balanced, l1_ratio=0.25, tol=0.009449293684544096;, score=0.832 total time=   1.9s
[CV 2/3; 24/50] START C=0.0437199421681428, class_weight=balanced, l1_ratio=0.25, tol=0.009449293684544096
[CV 2/3; 24/50] END C=0.0437199421681428, class_weight=balanced, l1_ratio=0.25, tol=0.009449293684544096;, score=0.991 total time=   1.7s
[CV 3/3; 24/50] START C=0.0437199421681428, class_weight=balanced, l1_ratio=0.25, tol=0.009449293684544096
[CV 3/3; 24/50] END C=0.0437199421681428, class_weight=balanced, l1_ratio=0.25, tol=0.009449293684544096;, score=0.953 total time=   1.9s
[CV 1/3; 25/50] START C=0.005614304922237251, class_weight=None, l1_ratio=1.0, tol=0.026117141228188593
[CV 1/3; 25/50] END C=0.005614304922237251, class_weight=None, l1_ratio=1.0, tol=0.026117141228188593;, score=0.934 total time=   0.8s
[CV 2/3; 25/50] START C=0.005614304922237251, class_weight=None, l1_ratio=1.0, tol=0.026117141228188593
[CV 2/3; 25/50] END C=0.005614304922237251, class_weight=None, l1_ratio=1.0, tol=0.026117141228188593;, score=0.936 total time=   0.8s
[CV 3/3; 25/50] START C=0.005614304922237251, class_weight=None, l1_ratio=1.0, tol=0.026117141228188593
[CV 3/3; 25/50] END C=0.005614304922237251, class_weight=None, l1_ratio=1.0, tol=0.026117141228188593;, score=0.903 total time=   0.8s
[CV 1/3; 26/50] START C=0.0019276158645987877, class_weight=balanced, l1_ratio=0.25, tol=0.011121366710724603
[CV 1/3; 26/50] END C=0.0019276158645987877, class_weight=balanced, l1_ratio=0.25, tol=0.011121366710724603;, score=0.924 total time=   3.1s
[CV 2/3; 26/50] START C=0.0019276158645987877, class_weight=balanced, l1_ratio=0.25, tol=0.011121366710724603
[CV 2/3; 26/50] END C=0.0019276158645987877, class_weight=balanced, l1_ratio=0.25, tol=0.011121366710724603;, score=0.980 total time=  36.2s
[CV 3/3; 26/50] START C=0.0019276158645987877, class_weight=balanced, l1_ratio=0.25, tol=0.011121366710724603
[CV 3/3; 26/50] END C=0.0019276158645987877, class_weight=balanced, l1_ratio=0.25, tol=0.011121366710724603;, score=0.938 total time= 1.0min
[CV 1/3; 27/50] START C=0.016781260301873508, class_weight=None, l1_ratio=0.25, tol=0.007754708079292941
[CV 1/3; 27/50] END C=0.016781260301873508, class_weight=None, l1_ratio=0.25, tol=0.007754708079292941;, score=0.950 total time=   1.3s
[CV 2/3; 27/50] START C=0.016781260301873508, class_weight=None, l1_ratio=0.25, tol=0.007754708079292941
[CV 2/3; 27/50] END C=0.016781260301873508, class_weight=None, l1_ratio=0.25, tol=0.007754708079292941;, score=0.977 total time=   1.2s
[CV 3/3; 27/50] START C=0.016781260301873508, class_weight=None, l1_ratio=0.25, tol=0.007754708079292941
[CV 3/3; 27/50] END C=0.016781260301873508, class_weight=None, l1_ratio=0.25, tol=0.007754708079292941;, score=0.947 total time=   1.3s
[CV 1/3; 28/50] START C=0.0020813836715588645, class_weight=balanced, l1_ratio=0.75, tol=0.006153766879681267
[CV 1/3; 28/50] END C=0.0020813836715588645, class_weight=balanced, l1_ratio=0.75, tol=0.006153766879681267;, score=0.895 total time=   1.3s
[CV 2/3; 28/50] START C=0.0020813836715588645, class_weight=balanced, l1_ratio=0.75, tol=0.006153766879681267
[CV 2/3; 28/50] END C=0.0020813836715588645, class_weight=balanced, l1_ratio=0.75, tol=0.006153766879681267;, score=0.958 total time=   1.3s
[CV 3/3; 28/50] START C=0.0020813836715588645, class_weight=balanced, l1_ratio=0.75, tol=0.006153766879681267
[CV 3/3; 28/50] END C=0.0020813836715588645, class_weight=balanced, l1_ratio=0.75, tol=0.006153766879681267;, score=0.911 total time=   3.9s
[CV 1/3; 29/50] START C=0.18578509701893903, class_weight=None, l1_ratio=0.0, tol=0.0023932093902744134
[CV 1/3; 29/50] END C=0.18578509701893903, class_weight=None, l1_ratio=0.0, tol=0.0023932093902744134;, score=0.868 total time=   2.4s
[CV 2/3; 29/50] START C=0.18578509701893903, class_weight=None, l1_ratio=0.0, tol=0.0023932093902744134
[CV 2/3; 29/50] END C=0.18578509701893903, class_weight=None, l1_ratio=0.0, tol=0.0023932093902744134;, score=0.989 total time=   2.8s
[CV 3/3; 29/50] START C=0.18578509701893903, class_weight=None, l1_ratio=0.0, tol=0.0023932093902744134
[CV 3/3; 29/50] END C=0.18578509701893903, class_weight=None, l1_ratio=0.0, tol=0.0023932093902744134;, score=0.961 total time=   3.0s
[CV 1/3; 30/50] START C=0.1703537838382531, class_weight=None, l1_ratio=1.0, tol=0.008851194767858632
[CV 1/3; 30/50] END C=0.1703537838382531, class_weight=None, l1_ratio=1.0, tol=0.008851194767858632;, score=0.900 total time=   2.6s
[CV 2/3; 30/50] START C=0.1703537838382531, class_weight=None, l1_ratio=1.0, tol=0.008851194767858632
[CV 2/3; 30/50] END C=0.1703537838382531, class_weight=None, l1_ratio=1.0, tol=0.008851194767858632;, score=0.986 total time=   2.3s
[CV 3/3; 30/50] START C=0.1703537838382531, class_weight=None, l1_ratio=1.0, tol=0.008851194767858632
[CV 3/3; 30/50] END C=0.1703537838382531, class_weight=None, l1_ratio=1.0, tol=0.008851194767858632;, score=0.957 total time=   2.5s
[CV 1/3; 31/50] START C=0.00484927143837009, class_weight=balanced, l1_ratio=0.25, tol=0.03762964225758183
[CV 1/3; 31/50] END C=0.00484927143837009, class_weight=balanced, l1_ratio=0.25, tol=0.03762964225758183;, score=0.894 total time=   0.9s
[CV 2/3; 31/50] START C=0.00484927143837009, class_weight=balanced, l1_ratio=0.25, tol=0.03762964225758183
[CV 2/3; 31/50] END C=0.00484927143837009, class_weight=balanced, l1_ratio=0.25, tol=0.03762964225758183;, score=0.988 total time=   0.9s
[CV 3/3; 31/50] START C=0.00484927143837009, class_weight=balanced, l1_ratio=0.25, tol=0.03762964225758183
[CV 3/3; 31/50] END C=0.00484927143837009, class_weight=balanced, l1_ratio=0.25, tol=0.03762964225758183;, score=0.946 total time=   1.8s
[CV 1/3; 32/50] START C=0.5626025570246128, class_weight=None, l1_ratio=1.0, tol=0.0011143497389414219
[CV 1/3; 32/50] END C=0.5626025570246128, class_weight=None, l1_ratio=1.0, tol=0.0011143497389414219;, score=0.765 total time=  13.7s
[CV 2/3; 32/50] START C=0.5626025570246128, class_weight=None, l1_ratio=1.0, tol=0.0011143497389414219
[CV 2/3; 32/50] END C=0.5626025570246128, class_weight=None, l1_ratio=1.0, tol=0.0011143497389414219;, score=0.990 total time=  11.9s
[CV 3/3; 32/50] START C=0.5626025570246128, class_weight=None, l1_ratio=1.0, tol=0.0011143497389414219
[CV 3/3; 32/50] END C=0.5626025570246128, class_weight=None, l1_ratio=1.0, tol=0.0011143497389414219;, score=0.965 total time=  14.1s
[CV 1/3; 33/50] START C=0.1619261634200429, class_weight=None, l1_ratio=0.75, tol=0.009721115728783673
[CV 1/3; 33/50] END C=0.1619261634200429, class_weight=None, l1_ratio=0.75, tol=0.009721115728783673;, score=0.910 total time=   2.1s
[CV 2/3; 33/50] START C=0.1619261634200429, class_weight=None, l1_ratio=0.75, tol=0.009721115728783673
[CV 2/3; 33/50] END C=0.1619261634200429, class_weight=None, l1_ratio=0.75, tol=0.009721115728783673;, score=0.987 total time=   2.1s
[CV 3/3; 33/50] START C=0.1619261634200429, class_weight=None, l1_ratio=0.75, tol=0.009721115728783673
[CV 3/3; 33/50] END C=0.1619261634200429, class_weight=None, l1_ratio=0.75, tol=0.009721115728783673;, score=0.957 total time=   1.9s
[CV 1/3; 34/50] START C=0.03524247164651489, class_weight=balanced, l1_ratio=0.25, tol=0.008567221404021356
[CV 1/3; 34/50] END C=0.03524247164651489, class_weight=balanced, l1_ratio=0.25, tol=0.008567221404021356;, score=0.838 total time=   1.6s
[CV 2/3; 34/50] START C=0.03524247164651489, class_weight=balanced, l1_ratio=0.25, tol=0.008567221404021356
[CV 2/3; 34/50] END C=0.03524247164651489, class_weight=balanced, l1_ratio=0.25, tol=0.008567221404021356;, score=0.991 total time=   1.7s
[CV 3/3; 34/50] START C=0.03524247164651489, class_weight=balanced, l1_ratio=0.25, tol=0.008567221404021356
[CV 3/3; 34/50] END C=0.03524247164651489, class_weight=balanced, l1_ratio=0.25, tol=0.008567221404021356;, score=0.950 total time=   2.9s
[CV 1/3; 35/50] START C=0.40644079430353885, class_weight=balanced, l1_ratio=0.75, tol=0.01033296833392727
[CV 1/3; 35/50] END C=0.40644079430353885, class_weight=balanced, l1_ratio=0.75, tol=0.01033296833392727;, score=0.820 total time=   1.5s
[CV 2/3; 35/50] START C=0.40644079430353885, class_weight=balanced, l1_ratio=0.75, tol=0.01033296833392727
[CV 2/3; 35/50] END C=0.40644079430353885, class_weight=balanced, l1_ratio=0.75, tol=0.01033296833392727;, score=0.991 total time=   1.6s
[CV 3/3; 35/50] START C=0.40644079430353885, class_weight=balanced, l1_ratio=0.75, tol=0.01033296833392727
[CV 3/3; 35/50] END C=0.40644079430353885, class_weight=balanced, l1_ratio=0.75, tol=0.01033296833392727;, score=0.953 total time=   1.6s
[CV 1/3; 36/50] START C=0.0022772141707269188, class_weight=None, l1_ratio=0.25, tol=0.07407283573291575
[CV 1/3; 36/50] END C=0.0022772141707269188, class_weight=None, l1_ratio=0.25, tol=0.07407283573291575;, score=0.937 total time=   0.6s
[CV 2/3; 36/50] START C=0.0022772141707269188, class_weight=None, l1_ratio=0.25, tol=0.07407283573291575
[CV 2/3; 36/50] END C=0.0022772141707269188, class_weight=None, l1_ratio=0.25, tol=0.07407283573291575;, score=0.935 total time=   0.5s
[CV 3/3; 36/50] START C=0.0022772141707269188, class_weight=None, l1_ratio=0.25, tol=0.07407283573291575
[CV 3/3; 36/50] END C=0.0022772141707269188, class_weight=None, l1_ratio=0.25, tol=0.07407283573291575;, score=0.893 total time=   0.5s
[CV 1/3; 37/50] START C=1.9295390896134932, class_weight=None, l1_ratio=0.75, tol=0.002695753108561177
[CV 1/3; 37/50] END C=1.9295390896134932, class_weight=None, l1_ratio=0.75, tol=0.002695753108561177;, score=0.810 total time=   6.4s
[CV 2/3; 37/50] START C=1.9295390896134932, class_weight=None, l1_ratio=0.75, tol=0.002695753108561177
[CV 2/3; 37/50] END C=1.9295390896134932, class_weight=None, l1_ratio=0.75, tol=0.002695753108561177;, score=0.990 total time=   8.3s
[CV 3/3; 37/50] START C=1.9295390896134932, class_weight=None, l1_ratio=0.75, tol=0.002695753108561177
[CV 3/3; 37/50] END C=1.9295390896134932, class_weight=None, l1_ratio=0.75, tol=0.002695753108561177;, score=0.966 total time=   7.7s
[CV 1/3; 38/50] START C=0.1547710526693868, class_weight=balanced, l1_ratio=0.75, tol=0.03518726063667983
[CV 1/3; 38/50] END C=0.1547710526693868, class_weight=balanced, l1_ratio=0.75, tol=0.03518726063667983;, score=0.841 total time=   0.7s
[CV 2/3; 38/50] START C=0.1547710526693868, class_weight=balanced, l1_ratio=0.75, tol=0.03518726063667983
[CV 2/3; 38/50] END C=0.1547710526693868, class_weight=balanced, l1_ratio=0.75, tol=0.03518726063667983;, score=0.990 total time=   1.1s
[CV 3/3; 38/50] START C=0.1547710526693868, class_weight=balanced, l1_ratio=0.75, tol=0.03518726063667983
[CV 3/3; 38/50] END C=0.1547710526693868, class_weight=balanced, l1_ratio=0.75, tol=0.03518726063667983;, score=0.953 total time=   1.0s
[CV 1/3; 39/50] START C=0.04879259359231704, class_weight=None, l1_ratio=1.0, tol=0.0314659428973729
[CV 1/3; 39/50] END C=0.04879259359231704, class_weight=None, l1_ratio=1.0, tol=0.0314659428973729;, score=0.943 total time=   1.0s
[CV 2/3; 39/50] START C=0.04879259359231704, class_weight=None, l1_ratio=1.0, tol=0.0314659428973729
[CV 2/3; 39/50] END C=0.04879259359231704, class_weight=None, l1_ratio=1.0, tol=0.0314659428973729;, score=0.977 total time=   0.9s
[CV 3/3; 39/50] START C=0.04879259359231704, class_weight=None, l1_ratio=1.0, tol=0.0314659428973729
[CV 3/3; 39/50] END C=0.04879259359231704, class_weight=None, l1_ratio=1.0, tol=0.0314659428973729;, score=0.948 total time=   1.0s
[CV 1/3; 40/50] START C=0.003923575147551568, class_weight=None, l1_ratio=0.25, tol=0.001309474049128516
[CV 1/3; 40/50] END C=0.003923575147551568, class_weight=None, l1_ratio=0.25, tol=0.001309474049128516;, score=0.948 total time=   3.5s
[CV 2/3; 40/50] START C=0.003923575147551568, class_weight=None, l1_ratio=0.25, tol=0.001309474049128516
[CV 2/3; 40/50] END C=0.003923575147551568, class_weight=None, l1_ratio=0.25, tol=0.001309474049128516;, score=0.953 total time=   3.4s
[CV 3/3; 40/50] START C=0.003923575147551568, class_weight=None, l1_ratio=0.25, tol=0.001309474049128516
[CV 3/3; 40/50] END C=0.003923575147551568, class_weight=None, l1_ratio=0.25, tol=0.001309474049128516;, score=0.915 total time=   3.5s
[CV 1/3; 41/50] START C=0.007639747776768697, class_weight=None, l1_ratio=0.75, tol=0.023354909575220104
[CV 1/3; 41/50] END C=0.007639747776768697, class_weight=None, l1_ratio=0.75, tol=0.023354909575220104;, score=0.945 total time=   1.0s
[CV 2/3; 41/50] START C=0.007639747776768697, class_weight=None, l1_ratio=0.75, tol=0.023354909575220104
[CV 2/3; 41/50] END C=0.007639747776768697, class_weight=None, l1_ratio=0.75, tol=0.023354909575220104;, score=0.956 total time=   0.9s
[CV 3/3; 41/50] START C=0.007639747776768697, class_weight=None, l1_ratio=0.75, tol=0.023354909575220104
[CV 3/3; 41/50] END C=0.007639747776768697, class_weight=None, l1_ratio=0.75, tol=0.023354909575220104;, score=0.922 total time=   0.9s
[CV 1/3; 42/50] START C=0.015403628684891056, class_weight=None, l1_ratio=0.0, tol=0.01754272175552513
[CV 1/3; 42/50] END C=0.015403628684891056, class_weight=None, l1_ratio=0.0, tol=0.01754272175552513;, score=0.951 total time=   0.6s
[CV 2/3; 42/50] START C=0.015403628684891056, class_weight=None, l1_ratio=0.0, tol=0.01754272175552513
[CV 2/3; 42/50] END C=0.015403628684891056, class_weight=None, l1_ratio=0.0, tol=0.01754272175552513;, score=0.981 total time=   0.6s
[CV 3/3; 42/50] START C=0.015403628684891056, class_weight=None, l1_ratio=0.0, tol=0.01754272175552513
[CV 3/3; 42/50] END C=0.015403628684891056, class_weight=None, l1_ratio=0.0, tol=0.01754272175552513;, score=0.950 total time=   0.6s
[CV 1/3; 43/50] START C=1.241974875941478, class_weight=None, l1_ratio=0.75, tol=0.05926428316687501
[CV 1/3; 43/50] END C=1.241974875941478, class_weight=None, l1_ratio=0.75, tol=0.05926428316687501;, score=0.943 total time=   0.6s
[CV 2/3; 43/50] START C=1.241974875941478, class_weight=None, l1_ratio=0.75, tol=0.05926428316687501
[CV 2/3; 43/50] END C=1.241974875941478, class_weight=None, l1_ratio=0.75, tol=0.05926428316687501;, score=0.983 total time=   0.6s
[CV 3/3; 43/50] START C=1.241974875941478, class_weight=None, l1_ratio=0.75, tol=0.05926428316687501
[CV 3/3; 43/50] END C=1.241974875941478, class_weight=None, l1_ratio=0.75, tol=0.05926428316687501;, score=0.953 total time=   0.6s
[CV 1/3; 44/50] START C=1.2050972434964364, class_weight=balanced, l1_ratio=0.75, tol=0.012046515085839817
[CV 1/3; 44/50] END C=1.2050972434964364, class_weight=balanced, l1_ratio=0.75, tol=0.012046515085839817;, score=0.814 total time=   1.4s
[CV 2/3; 44/50] START C=1.2050972434964364, class_weight=balanced, l1_ratio=0.75, tol=0.012046515085839817
[CV 2/3; 44/50] END C=1.2050972434964364, class_weight=balanced, l1_ratio=0.75, tol=0.012046515085839817;, score=0.991 total time=   1.5s
[CV 3/3; 44/50] START C=1.2050972434964364, class_weight=balanced, l1_ratio=0.75, tol=0.012046515085839817
[CV 3/3; 44/50] END C=1.2050972434964364, class_weight=balanced, l1_ratio=0.75, tol=0.012046515085839817;, score=0.953 total time=   1.5s
[CV 1/3; 45/50] START C=0.04792998738804747, class_weight=balanced, l1_ratio=0.25, tol=0.08484926981239534
[CV 1/3; 45/50] END C=0.04792998738804747, class_weight=balanced, l1_ratio=0.25, tol=0.08484926981239534;, score=0.853 total time=   0.6s
[CV 2/3; 45/50] START C=0.04792998738804747, class_weight=balanced, l1_ratio=0.25, tol=0.08484926981239534
[CV 2/3; 45/50] END C=0.04792998738804747, class_weight=balanced, l1_ratio=0.25, tol=0.08484926981239534;, score=0.991 total time=   0.7s
[CV 3/3; 45/50] START C=0.04792998738804747, class_weight=balanced, l1_ratio=0.25, tol=0.08484926981239534
[CV 3/3; 45/50] END C=0.04792998738804747, class_weight=balanced, l1_ratio=0.25, tol=0.08484926981239534;, score=0.951 total time=   0.9s
[CV 1/3; 46/50] START C=0.7630254690940719, class_weight=None, l1_ratio=0.25, tol=0.06579924568095913
[CV 1/3; 46/50] END C=0.7630254690940719, class_weight=None, l1_ratio=0.25, tol=0.06579924568095913;, score=0.947 total time=   0.6s
[CV 2/3; 46/50] START C=0.7630254690940719, class_weight=None, l1_ratio=0.25, tol=0.06579924568095913
[CV 2/3; 46/50] END C=0.7630254690940719, class_weight=None, l1_ratio=0.25, tol=0.06579924568095913;, score=0.982 total time=   0.6s
[CV 3/3; 46/50] START C=0.7630254690940719, class_weight=None, l1_ratio=0.25, tol=0.06579924568095913
[CV 3/3; 46/50] END C=0.7630254690940719, class_weight=None, l1_ratio=0.25, tol=0.06579924568095913;, score=0.953 total time=   0.6s
[CV 1/3; 47/50] START C=0.37852622941307273, class_weight=None, l1_ratio=0.5, tol=0.012543412568905527
[CV 1/3; 47/50] END C=0.37852622941307273, class_weight=None, l1_ratio=0.5, tol=0.012543412568905527;, score=0.911 total time=   1.5s
[CV 2/3; 47/50] START C=0.37852622941307273, class_weight=None, l1_ratio=0.5, tol=0.012543412568905527
[CV 2/3; 47/50] END C=0.37852622941307273, class_weight=None, l1_ratio=0.5, tol=0.012543412568905527;, score=0.989 total time=   1.9s
[CV 3/3; 47/50] START C=0.37852622941307273, class_weight=None, l1_ratio=0.5, tol=0.012543412568905527
[CV 3/3; 47/50] END C=0.37852622941307273, class_weight=None, l1_ratio=0.5, tol=0.012543412568905527;, score=0.958 total time=   1.6s
[CV 1/3; 48/50] START C=0.3337259211186397, class_weight=balanced, l1_ratio=0.0, tol=0.0010864610471193474
[CV 1/3; 48/50] END C=0.3337259211186397, class_weight=balanced, l1_ratio=0.0, tol=0.0010864610471193474;, score=0.742 total time=   4.3s
[CV 2/3; 48/50] START C=0.3337259211186397, class_weight=balanced, l1_ratio=0.0, tol=0.0010864610471193474
[CV 2/3; 48/50] END C=0.3337259211186397, class_weight=balanced, l1_ratio=0.0, tol=0.0010864610471193474;, score=0.991 total time=   7.1s
[CV 3/3; 48/50] START C=0.3337259211186397, class_weight=balanced, l1_ratio=0.0, tol=0.0010864610471193474
[CV 3/3; 48/50] END C=0.3337259211186397, class_weight=balanced, l1_ratio=0.0, tol=0.0010864610471193474;, score=0.961 total time=   9.0s
[CV 1/3; 49/50] START C=0.012633429543293119, class_weight=None, l1_ratio=0.5, tol=0.0708503522842181
[CV 1/3; 49/50] END C=0.012633429543293119, class_weight=None, l1_ratio=0.5, tol=0.0708503522842181;, score=0.953 total time=   0.6s
[CV 2/3; 49/50] START C=0.012633429543293119, class_weight=None, l1_ratio=0.5, tol=0.0708503522842181
[CV 2/3; 49/50] END C=0.012633429543293119, class_weight=None, l1_ratio=0.5, tol=0.0708503522842181;, score=0.967 total time=   0.6s
[CV 3/3; 49/50] START C=0.012633429543293119, class_weight=None, l1_ratio=0.5, tol=0.0708503522842181
[CV 3/3; 49/50] END C=0.012633429543293119, class_weight=None, l1_ratio=0.5, tol=0.0708503522842181;, score=0.940 total time=   0.6s
[CV 1/3; 50/50] START C=1.418059616302639, class_weight=None, l1_ratio=0.0, tol=0.05279911359319414
[CV 1/3; 50/50] END C=1.418059616302639, class_weight=None, l1_ratio=0.0, tol=0.05279911359319414;, score=0.943 total time=   0.5s
[CV 2/3; 50/50] START C=1.418059616302639, class_weight=None, l1_ratio=0.0, tol=0.05279911359319414
[CV 2/3; 50/50] END C=1.418059616302639, class_weight=None, l1_ratio=0.0, tol=0.05279911359319414;, score=0.983 total time=   0.5s
[CV 3/3; 50/50] START C=1.418059616302639, class_weight=None, l1_ratio=0.0, tol=0.05279911359319414
[CV 3/3; 50/50] END C=1.418059616302639, class_weight=None, l1_ratio=0.0, tol=0.05279911359319414;, score=0.954 total time=   0.5s

--- TUNING FINISHED ---
Beste Parameter: {'C': np.float64(0.08598409911703409), 'class_weight': None, 'l1_ratio': 0.75, 'tol': np.float64(0.072424692332114)}
Bester CV-Score: 0.9609

--- EVALUATION AUF DEN TESTDATEN ---
Test Accuracy: 0.9004

Macro F1: 0.8349882991289508

--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9004

                     precision    recall  f1-score   support

             B cell       0.98      1.00      0.99       120
     CD14+ monocyte       1.00      1.00      1.00      2575
        CD4+ T cell       0.87      0.99      0.93      3910
   Cytotoxic T cell       0.93      0.56      0.70      1824
     Dendritic cell       1.00      0.20      0.33         5
      Megakaryocyte       1.00      1.00      1.00         7
Natural killer cell       0.74      0.91      0.81       791
        Plasma cell       1.00      0.86      0.92        49

           accuracy                           0.90      9281
          macro avg       0.94      0.81      0.83      9281
       weighted avg       0.91      0.90      0.89      9281

Random dropout accuracy score 0.8848
Total samples: 9281
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.8982
Feature importance dropout (0.5% features dropped) accuracy score 0.8818
Feature importance dropout (1.0% features dropped) accuracy score 0.8708
Feature importance dropout (2.0% features dropped) accuracy score 0.8412
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8496

                     precision    recall  f1-score   support

             B cell       1.00      0.99      0.99      3959
     CD14+ monocyte       0.92      1.00      0.96      3135
        CD4+ T cell       0.88      1.00      0.94     13664
   Cytotoxic T cell       0.58      0.62      0.60      4839
     Dendritic cell       1.00      0.61      0.76       529
      Megakaryocyte       0.98      0.62      0.76        86
Natural killer cell       0.87      0.19      0.31      2751
        Plasma cell       0.86      0.52      0.65        23

           accuracy                           0.85     28986
          macro avg       0.89      0.69      0.75     28986
       weighted avg       0.85      0.85      0.83     28986

Random dropout accuracy score 0.8413
Total samples: 28986
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.8498
Feature importance dropout (0.5% features dropped) accuracy score 0.8295
Feature importance dropout (1.0% features dropped) accuracy score 0.8105
Feature importance dropout (2.0% features dropped) accuracy score 0.7294
=== JOB_STATISTICS ===
=== current date     : Mon Jun 29 12:04:47 CEST 2026
= Job-ID             : 12000011 on woody
= Job-Name           : autoencoder_lr
= Job-Command        : /home/hpc/iwbn/iwbn133h/submit_autoencoder_lr_v1.sh
= Initial workdir    : /home/hpc/iwbn/iwbn133h
= Queue/Partition    : work
= Slurm account      : iwbn with QOS=normal
= Features           : icx
= Requested resources:  for 17:00:00
= Elapsed runtime    : 02:56:12
= Total RAM usage    : 19.1 GiB of requested  GiB (%)   
= Node list          : w2314
= Subm/Elig/Start/End: 2026-06-29T09:08:32 / 2026-06-29T09:08:32 / 2026-06-29T09:08:34 / 2026-06-29T12:04:46
======================
=== Quota infos ======
    Path                 Used     SoftQ    HardQ    Gracetime  Filec    FileQ    FiHaQ    FileGrace    
    /home/woody           982.1M  1000.0G  1500.0G        N/A  29,019    5,000K   7,500K        N/A    
    /home/hpc              86.2G   104.9G   209.7G        N/A     139K     500K   1,000K        N/A    
    /home/vault             0.0K  1048.6G  2097.2G        N/A       1      200K     400K        N/A    
