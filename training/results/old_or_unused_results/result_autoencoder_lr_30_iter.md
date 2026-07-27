### Starting TaskPrologue of job 11996032 on w2315 at Sat Jun 27 20:47:21 CEST 2026
#   SLURM_JOB_NODELIST=w2315
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
Epoch [1/150], Loss: 0.9512
Epoch [10/150], Loss: 0.9051
Epoch [20/150], Loss: 0.8915
Epoch [30/150], Loss: 0.8837
Epoch [40/150], Loss: 0.8790
Epoch [50/150], Loss: 0.8754
Epoch [60/150], Loss: 0.8729
Epoch [70/150], Loss: 0.8708
Epoch [80/150], Loss: 0.8692
Epoch [90/150], Loss: 0.8676
Epoch [100/150], Loss: 0.8659
Epoch [110/150], Loss: 0.8649
Epoch [120/150], Loss: 0.8637
Epoch [130/150], Loss: 0.8629
Early Stopping after [133/150] Epochs!

Extract robust features...
Starte automatische Hyperparametersuche auf dem Latent Space...
Fitting 3 folds for each of 30 candidates, totalling 90 fits
[CV 1/3; 1/30] START C=0.0015014326822054608, class_weight=balanced, l1_ratio=1.0, tol=0.0052284732430044
[CV 1/3; 1/30] END C=0.0015014326822054608, class_weight=balanced, l1_ratio=1.0, tol=0.0052284732430044;, score=0.613 total time=  58.9s
[CV 2/3; 1/30] START C=0.0015014326822054608, class_weight=balanced, l1_ratio=1.0, tol=0.0052284732430044
[CV 2/3; 1/30] END C=0.0015014326822054608, class_weight=balanced, l1_ratio=1.0, tol=0.0052284732430044;, score=0.929 total time=  59.1s
[CV 3/3; 1/30] START C=0.0015014326822054608, class_weight=balanced, l1_ratio=1.0, tol=0.0052284732430044
[CV 3/3; 1/30] END C=0.0015014326822054608, class_weight=balanced, l1_ratio=1.0, tol=0.0052284732430044;, score=0.900 total time=  59.0s
[CV 1/3; 2/30] START C=0.03436690098327921, class_weight=balanced, l1_ratio=0.0, tol=0.09589338029015392
[CV 1/3; 2/30] END C=0.03436690098327921, class_weight=balanced, l1_ratio=0.0, tol=0.09589338029015392;, score=0.821 total time=   0.5s
[CV 2/3; 2/30] START C=0.03436690098327921, class_weight=balanced, l1_ratio=0.0, tol=0.09589338029015392
[CV 2/3; 2/30] END C=0.03436690098327921, class_weight=balanced, l1_ratio=0.0, tol=0.09589338029015392;, score=0.987 total time=   0.5s
[CV 3/3; 2/30] START C=0.03436690098327921, class_weight=balanced, l1_ratio=0.0, tol=0.09589338029015392
[CV 3/3; 2/30] END C=0.03436690098327921, class_weight=balanced, l1_ratio=0.0, tol=0.09589338029015392;, score=0.951 total time=   0.7s
[CV 1/3; 3/30] START C=0.12934773112964398, class_weight=None, l1_ratio=0.25, tol=0.022185576506833376
[CV 1/3; 3/30] END C=0.12934773112964398, class_weight=None, l1_ratio=0.25, tol=0.022185576506833376;, score=0.917 total time=   1.1s
[CV 2/3; 3/30] START C=0.12934773112964398, class_weight=None, l1_ratio=0.25, tol=0.022185576506833376
[CV 2/3; 3/30] END C=0.12934773112964398, class_weight=None, l1_ratio=0.25, tol=0.022185576506833376;, score=0.987 total time=   1.1s
[CV 3/3; 3/30] START C=0.12934773112964398, class_weight=None, l1_ratio=0.25, tol=0.022185576506833376
[CV 3/3; 3/30] END C=0.12934773112964398, class_weight=None, l1_ratio=0.25, tol=0.022185576506833376;, score=0.960 total time=   1.2s
[CV 1/3; 4/30] START C=0.01048155527125858, class_weight=None, l1_ratio=0.75, tol=0.007208988316891624
[CV 1/3; 4/30] END C=0.01048155527125858, class_weight=None, l1_ratio=0.75, tol=0.007208988316891624;, score=0.924 total time=   2.5s
[CV 2/3; 4/30] START C=0.01048155527125858, class_weight=None, l1_ratio=0.75, tol=0.007208988316891624
[CV 2/3; 4/30] END C=0.01048155527125858, class_weight=None, l1_ratio=0.75, tol=0.007208988316891624;, score=0.964 total time=   2.1s
[CV 3/3; 4/30] START C=0.01048155527125858, class_weight=None, l1_ratio=0.75, tol=0.007208988316891624
[CV 3/3; 4/30] END C=0.01048155527125858, class_weight=None, l1_ratio=0.75, tol=0.007208988316891624;, score=0.936 total time=   2.3s
[CV 1/3; 5/30] START C=0.22408914010022474, class_weight=None, l1_ratio=1.0, tol=0.017221983039313674
[CV 1/3; 5/30] END C=0.22408914010022474, class_weight=None, l1_ratio=1.0, tol=0.017221983039313674;, score=0.906 total time=   1.4s
[CV 2/3; 5/30] START C=0.22408914010022474, class_weight=None, l1_ratio=1.0, tol=0.017221983039313674
[CV 2/3; 5/30] END C=0.22408914010022474, class_weight=None, l1_ratio=1.0, tol=0.017221983039313674;, score=0.988 total time=   1.5s
[CV 3/3; 5/30] START C=0.22408914010022474, class_weight=None, l1_ratio=1.0, tol=0.017221983039313674
[CV 3/3; 5/30] END C=0.22408914010022474, class_weight=None, l1_ratio=1.0, tol=0.017221983039313674;, score=0.960 total time=   1.6s
[CV 1/3; 6/30] START C=0.13984917745544326, class_weight=balanced, l1_ratio=0.0, tol=0.07762963437721108
[CV 1/3; 6/30] END C=0.13984917745544326, class_weight=balanced, l1_ratio=0.0, tol=0.07762963437721108;, score=0.822 total time=   0.9s
[CV 2/3; 6/30] START C=0.13984917745544326, class_weight=balanced, l1_ratio=0.0, tol=0.07762963437721108
[CV 2/3; 6/30] END C=0.13984917745544326, class_weight=balanced, l1_ratio=0.0, tol=0.07762963437721108;, score=0.989 total time=   0.6s
[CV 3/3; 6/30] START C=0.13984917745544326, class_weight=balanced, l1_ratio=0.0, tol=0.07762963437721108
[CV 3/3; 6/30] END C=0.13984917745544326, class_weight=balanced, l1_ratio=0.0, tol=0.07762963437721108;, score=0.950 total time=   0.7s
[CV 1/3; 7/30] START C=0.22708280339623757, class_weight=balanced, l1_ratio=1.0, tol=0.05326870582095845
[CV 1/3; 7/30] END C=0.22708280339623757, class_weight=balanced, l1_ratio=1.0, tol=0.05326870582095845;, score=0.802 total time=   1.3s
[CV 2/3; 7/30] START C=0.22708280339623757, class_weight=balanced, l1_ratio=1.0, tol=0.05326870582095845
[CV 2/3; 7/30] END C=0.22708280339623757, class_weight=balanced, l1_ratio=1.0, tol=0.05326870582095845;, score=0.990 total time=   0.8s
[CV 3/3; 7/30] START C=0.22708280339623757, class_weight=balanced, l1_ratio=1.0, tol=0.05326870582095845
[CV 3/3; 7/30] END C=0.22708280339623757, class_weight=balanced, l1_ratio=1.0, tol=0.05326870582095845;, score=0.955 total time=   0.9s
[CV 1/3; 8/30] START C=0.0679066918036097, class_weight=balanced, l1_ratio=0.75, tol=0.0762921275226619
[CV 1/3; 8/30] END C=0.0679066918036097, class_weight=balanced, l1_ratio=0.75, tol=0.0762921275226619;, score=0.822 total time=   0.7s
[CV 2/3; 8/30] START C=0.0679066918036097, class_weight=balanced, l1_ratio=0.75, tol=0.0762921275226619
[CV 2/3; 8/30] END C=0.0679066918036097, class_weight=balanced, l1_ratio=0.75, tol=0.0762921275226619;, score=0.987 total time=   1.1s
[CV 3/3; 8/30] START C=0.0679066918036097, class_weight=balanced, l1_ratio=0.75, tol=0.0762921275226619
[CV 3/3; 8/30] END C=0.0679066918036097, class_weight=balanced, l1_ratio=0.75, tol=0.0762921275226619;, score=0.947 total time=   1.2s
[CV 1/3; 9/30] START C=0.010558457606222956, class_weight=None, l1_ratio=1.0, tol=0.04620325622219964
[CV 1/3; 9/30] END C=0.010558457606222956, class_weight=None, l1_ratio=1.0, tol=0.04620325622219964;, score=0.925 total time=   0.8s
[CV 2/3; 9/30] START C=0.010558457606222956, class_weight=None, l1_ratio=1.0, tol=0.04620325622219964
[CV 2/3; 9/30] END C=0.010558457606222956, class_weight=None, l1_ratio=1.0, tol=0.04620325622219964;, score=0.962 total time=   0.8s
[CV 3/3; 9/30] START C=0.010558457606222956, class_weight=None, l1_ratio=1.0, tol=0.04620325622219964
[CV 3/3; 9/30] END C=0.010558457606222956, class_weight=None, l1_ratio=1.0, tol=0.04620325622219964;, score=0.932 total time=   0.8s
[CV 1/3; 10/30] START C=0.09337663931612991, class_weight=None, l1_ratio=0.75, tol=0.056388521347207274
[CV 1/3; 10/30] END C=0.09337663931612991, class_weight=None, l1_ratio=0.75, tol=0.056388521347207274;, score=0.930 total time=   0.7s
[CV 2/3; 10/30] START C=0.09337663931612991, class_weight=None, l1_ratio=0.75, tol=0.056388521347207274
[CV 2/3; 10/30] END C=0.09337663931612991, class_weight=None, l1_ratio=0.75, tol=0.056388521347207274;, score=0.985 total time=   0.6s
[CV 3/3; 10/30] START C=0.09337663931612991, class_weight=None, l1_ratio=0.75, tol=0.056388521347207274
[CV 3/3; 10/30] END C=0.09337663931612991, class_weight=None, l1_ratio=0.75, tol=0.056388521347207274;, score=0.955 total time=   0.7s
[CV 1/3; 11/30] START C=0.005211609775817964, class_weight=None, l1_ratio=0.25, tol=0.00347569162481
[CV 1/3; 11/30] END C=0.005211609775817964, class_weight=None, l1_ratio=0.25, tol=0.00347569162481;, score=0.934 total time=   2.9s
[CV 2/3; 11/30] START C=0.005211609775817964, class_weight=None, l1_ratio=0.25, tol=0.00347569162481
[CV 2/3; 11/30] END C=0.005211609775817964, class_weight=None, l1_ratio=0.25, tol=0.00347569162481;, score=0.962 total time=   2.8s
[CV 3/3; 11/30] START C=0.005211609775817964, class_weight=None, l1_ratio=0.25, tol=0.00347569162481
[CV 3/3; 11/30] END C=0.005211609775817964, class_weight=None, l1_ratio=0.25, tol=0.00347569162481;, score=0.934 total time=   3.2s
[CV 1/3; 12/30] START C=0.028471058215616626, class_weight=balanced, l1_ratio=0.5, tol=0.09498558189523529
[CV 1/3; 12/30] END C=0.028471058215616626, class_weight=balanced, l1_ratio=0.5, tol=0.09498558189523529;, score=0.807 total time=   0.7s
[CV 2/3; 12/30] START C=0.028471058215616626, class_weight=balanced, l1_ratio=0.5, tol=0.09498558189523529
[CV 2/3; 12/30] END C=0.028471058215616626, class_weight=balanced, l1_ratio=0.5, tol=0.09498558189523529;, score=0.987 total time=   0.7s
[CV 3/3; 12/30] START C=0.028471058215616626, class_weight=balanced, l1_ratio=0.5, tol=0.09498558189523529
[CV 3/3; 12/30] END C=0.028471058215616626, class_weight=balanced, l1_ratio=0.5, tol=0.09498558189523529;, score=0.946 total time=   0.9s
[CV 1/3; 13/30] START C=0.0012149773272593564, class_weight=balanced, l1_ratio=0.0, tol=0.0019037248680354654
[CV 1/3; 13/30] END C=0.0012149773272593564, class_weight=balanced, l1_ratio=0.0, tol=0.0019037248680354654;, score=0.854 total time=  38.5s
[CV 2/3; 13/30] START C=0.0012149773272593564, class_weight=balanced, l1_ratio=0.0, tol=0.0019037248680354654
[CV 2/3; 13/30] END C=0.0012149773272593564, class_weight=balanced, l1_ratio=0.0, tol=0.0019037248680354654;, score=0.984 total time=  38.5s
[CV 3/3; 13/30] START C=0.0012149773272593564, class_weight=balanced, l1_ratio=0.0, tol=0.0019037248680354654
[CV 3/3; 13/30] END C=0.0012149773272593564, class_weight=balanced, l1_ratio=0.0, tol=0.0019037248680354654;, score=0.946 total time=  38.5s
[CV 1/3; 14/30] START C=0.037093905080066665, class_weight=None, l1_ratio=0.5, tol=0.0010397772369891648
[CV 1/3; 14/30] END C=0.037093905080066665, class_weight=None, l1_ratio=0.5, tol=0.0010397772369891648;, score=0.909 total time=   7.2s
[CV 2/3; 14/30] START C=0.037093905080066665, class_weight=None, l1_ratio=0.5, tol=0.0010397772369891648
[CV 2/3; 14/30] END C=0.037093905080066665, class_weight=None, l1_ratio=0.5, tol=0.0010397772369891648;, score=0.983 total time=   6.4s
[CV 3/3; 14/30] START C=0.037093905080066665, class_weight=None, l1_ratio=0.5, tol=0.0010397772369891648
[CV 3/3; 14/30] END C=0.037093905080066665, class_weight=None, l1_ratio=0.5, tol=0.0010397772369891648;, score=0.953 total time=   8.8s
[CV 1/3; 15/30] START C=0.030190566292439967, class_weight=balanced, l1_ratio=0.5, tol=0.011733172121471272
[CV 1/3; 15/30] END C=0.030190566292439967, class_weight=balanced, l1_ratio=0.5, tol=0.011733172121471272;, score=0.772 total time=   2.9s
[CV 2/3; 15/30] START C=0.030190566292439967, class_weight=balanced, l1_ratio=0.5, tol=0.011733172121471272
[CV 2/3; 15/30] END C=0.030190566292439967, class_weight=balanced, l1_ratio=0.5, tol=0.011733172121471272;, score=0.990 total time=  13.1s
[CV 3/3; 15/30] START C=0.030190566292439967, class_weight=balanced, l1_ratio=0.5, tol=0.011733172121471272
[CV 3/3; 15/30] END C=0.030190566292439967, class_weight=balanced, l1_ratio=0.5, tol=0.011733172121471272;, score=0.951 total time=   1.8s
[CV 1/3; 16/30] START C=0.9110065853800889, class_weight=balanced, l1_ratio=0.75, tol=0.002954321737724303
[CV 1/3; 16/30] END C=0.9110065853800889, class_weight=balanced, l1_ratio=0.75, tol=0.002954321737724303;, score=0.754 total time=   4.4s
[CV 2/3; 16/30] START C=0.9110065853800889, class_weight=balanced, l1_ratio=0.75, tol=0.002954321737724303
[CV 2/3; 16/30] END C=0.9110065853800889, class_weight=balanced, l1_ratio=0.75, tol=0.002954321737724303;, score=0.991 total time=   4.4s
[CV 3/3; 16/30] START C=0.9110065853800889, class_weight=balanced, l1_ratio=0.75, tol=0.002954321737724303
[CV 3/3; 16/30] END C=0.9110065853800889, class_weight=balanced, l1_ratio=0.75, tol=0.002954321737724303;, score=0.962 total time=   4.0s
[CV 1/3; 17/30] START C=0.00516674556727456, class_weight=balanced, l1_ratio=0.75, tol=0.04752936241032139
[CV 1/3; 17/30] END C=0.00516674556727456, class_weight=balanced, l1_ratio=0.75, tol=0.04752936241032139;, score=0.664 total time=  31.8s
[CV 2/3; 17/30] START C=0.00516674556727456, class_weight=balanced, l1_ratio=0.75, tol=0.04752936241032139
[CV 2/3; 17/30] END C=0.00516674556727456, class_weight=balanced, l1_ratio=0.75, tol=0.04752936241032139;, score=0.977 total time=  59.0s
[CV 3/3; 17/30] START C=0.00516674556727456, class_weight=balanced, l1_ratio=0.75, tol=0.04752936241032139
[CV 3/3; 17/30] END C=0.00516674556727456, class_weight=balanced, l1_ratio=0.75, tol=0.04752936241032139;, score=0.942 total time=   3.3s
[CV 1/3; 18/30] START C=0.0025156879661595868, class_weight=balanced, l1_ratio=0.5, tol=0.006700398778114461
[CV 1/3; 18/30] END C=0.0025156879661595868, class_weight=balanced, l1_ratio=0.5, tol=0.006700398778114461;, score=0.654 total time=  59.1s
[CV 2/3; 18/30] START C=0.0025156879661595868, class_weight=balanced, l1_ratio=0.5, tol=0.006700398778114461
[CV 2/3; 18/30] END C=0.0025156879661595868, class_weight=balanced, l1_ratio=0.5, tol=0.006700398778114461;, score=0.982 total time=  59.2s
[CV 3/3; 18/30] START C=0.0025156879661595868, class_weight=balanced, l1_ratio=0.5, tol=0.006700398778114461
[CV 3/3; 18/30] END C=0.0025156879661595868, class_weight=balanced, l1_ratio=0.5, tol=0.006700398778114461;, score=0.935 total time=  59.1s
[CV 1/3; 19/30] START C=0.007610786315553737, class_weight=None, l1_ratio=0.0, tol=0.02930597133315727
[CV 1/3; 19/30] END C=0.007610786315553737, class_weight=None, l1_ratio=0.0, tol=0.02930597133315727;, score=0.940 total time=   0.5s
[CV 2/3; 19/30] START C=0.007610786315553737, class_weight=None, l1_ratio=0.0, tol=0.02930597133315727
[CV 2/3; 19/30] END C=0.007610786315553737, class_weight=None, l1_ratio=0.0, tol=0.02930597133315727;, score=0.979 total time=   0.5s
[CV 3/3; 19/30] START C=0.007610786315553737, class_weight=None, l1_ratio=0.0, tol=0.02930597133315727
[CV 3/3; 19/30] END C=0.007610786315553737, class_weight=None, l1_ratio=0.0, tol=0.02930597133315727;, score=0.952 total time=   0.5s
[CV 1/3; 20/30] START C=0.3772407933645397, class_weight=balanced, l1_ratio=0.25, tol=0.029746314503251797
[CV 1/3; 20/30] END C=0.3772407933645397, class_weight=balanced, l1_ratio=0.25, tol=0.029746314503251797;, score=0.816 total time=   1.6s
[CV 2/3; 20/30] START C=0.3772407933645397, class_weight=balanced, l1_ratio=0.25, tol=0.029746314503251797
[CV 2/3; 20/30] END C=0.3772407933645397, class_weight=balanced, l1_ratio=0.25, tol=0.029746314503251797;, score=0.990 total time=   1.8s
[CV 3/3; 20/30] START C=0.3772407933645397, class_weight=balanced, l1_ratio=0.25, tol=0.029746314503251797
[CV 3/3; 20/30] END C=0.3772407933645397, class_weight=balanced, l1_ratio=0.25, tol=0.029746314503251797;, score=0.960 total time=   1.0s
[CV 1/3; 21/30] START C=0.014878020183853091, class_weight=balanced, l1_ratio=0.5, tol=0.0023521201104570117
[CV 1/3; 21/30] END C=0.014878020183853091, class_weight=balanced, l1_ratio=0.5, tol=0.0023521201104570117;, score=0.735 total time= 1.0min
[CV 2/3; 21/30] START C=0.014878020183853091, class_weight=balanced, l1_ratio=0.5, tol=0.0023521201104570117
[CV 2/3; 21/30] END C=0.014878020183853091, class_weight=balanced, l1_ratio=0.5, tol=0.0023521201104570117;, score=0.986 total time= 1.0min
[CV 3/3; 21/30] START C=0.014878020183853091, class_weight=balanced, l1_ratio=0.5, tol=0.0023521201104570117
[CV 3/3; 21/30] END C=0.014878020183853091, class_weight=balanced, l1_ratio=0.5, tol=0.0023521201104570117;, score=0.948 total time=   4.3s
[CV 1/3; 22/30] START C=0.8091566059462821, class_weight=None, l1_ratio=0.25, tol=0.0045680930865916475
[CV 1/3; 22/30] END C=0.8091566059462821, class_weight=None, l1_ratio=0.25, tol=0.0045680930865916475;, score=0.857 total time=   4.2s
[CV 2/3; 22/30] START C=0.8091566059462821, class_weight=None, l1_ratio=0.25, tol=0.0045680930865916475
[CV 2/3; 22/30] END C=0.8091566059462821, class_weight=None, l1_ratio=0.25, tol=0.0045680930865916475;, score=0.990 total time=   4.3s
[CV 3/3; 22/30] START C=0.8091566059462821, class_weight=None, l1_ratio=0.25, tol=0.0045680930865916475
[CV 3/3; 22/30] END C=0.8091566059462821, class_weight=None, l1_ratio=0.25, tol=0.0045680930865916475;, score=0.968 total time=   4.8s
[CV 1/3; 23/30] START C=0.006285802785527126, class_weight=balanced, l1_ratio=0.75, tol=0.00441482921840311
[CV 1/3; 23/30] END C=0.006285802785527126, class_weight=balanced, l1_ratio=0.75, tol=0.00441482921840311;, score=0.660 total time=  59.0s
[CV 2/3; 23/30] START C=0.006285802785527126, class_weight=balanced, l1_ratio=0.75, tol=0.00441482921840311
[CV 2/3; 23/30] END C=0.006285802785527126, class_weight=balanced, l1_ratio=0.75, tol=0.00441482921840311;, score=0.981 total time=  59.0s
[CV 3/3; 23/30] START C=0.006285802785527126, class_weight=balanced, l1_ratio=0.75, tol=0.00441482921840311
[CV 3/3; 23/30] END C=0.006285802785527126, class_weight=balanced, l1_ratio=0.75, tol=0.00441482921840311;, score=0.943 total time=  59.1s
[CV 1/3; 24/30] START C=0.07992183822229347, class_weight=None, l1_ratio=0.25, tol=0.004717145576854134
[CV 1/3; 24/30] END C=0.07992183822229347, class_weight=None, l1_ratio=0.25, tol=0.004717145576854134;, score=0.903 total time=   2.7s
[CV 2/3; 24/30] START C=0.07992183822229347, class_weight=None, l1_ratio=0.25, tol=0.004717145576854134
[CV 2/3; 24/30] END C=0.07992183822229347, class_weight=None, l1_ratio=0.25, tol=0.004717145576854134;, score=0.988 total time=   3.2s
[CV 3/3; 24/30] START C=0.07992183822229347, class_weight=None, l1_ratio=0.25, tol=0.004717145576854134
[CV 3/3; 24/30] END C=0.07992183822229347, class_weight=None, l1_ratio=0.25, tol=0.004717145576854134;, score=0.961 total time=   3.2s
[CV 1/3; 25/30] START C=0.005265921454729664, class_weight=balanced, l1_ratio=1.0, tol=0.050366834735907556
[CV 1/3; 25/30] END C=0.005265921454729664, class_weight=balanced, l1_ratio=1.0, tol=0.050366834735907556;, score=0.638 total time=   2.3s
[CV 2/3; 25/30] START C=0.005265921454729664, class_weight=balanced, l1_ratio=1.0, tol=0.050366834735907556
[CV 2/3; 25/30] END C=0.005265921454729664, class_weight=balanced, l1_ratio=1.0, tol=0.050366834735907556;, score=0.977 total time=  11.7s
[CV 3/3; 25/30] START C=0.005265921454729664, class_weight=balanced, l1_ratio=1.0, tol=0.050366834735907556
[CV 3/3; 25/30] END C=0.005265921454729664, class_weight=balanced, l1_ratio=1.0, tol=0.050366834735907556;, score=0.934 total time=   3.5s
[CV 1/3; 26/30] START C=0.024178578393312167, class_weight=None, l1_ratio=0.25, tol=0.09374296978935291
[CV 1/3; 26/30] END C=0.024178578393312167, class_weight=None, l1_ratio=0.25, tol=0.09374296978935291;, score=0.935 total time=   0.5s
[CV 2/3; 26/30] START C=0.024178578393312167, class_weight=None, l1_ratio=0.25, tol=0.09374296978935291
[CV 2/3; 26/30] END C=0.024178578393312167, class_weight=None, l1_ratio=0.25, tol=0.09374296978935291;, score=0.979 total time=   0.5s
[CV 3/3; 26/30] START C=0.024178578393312167, class_weight=None, l1_ratio=0.25, tol=0.09374296978935291
[CV 3/3; 26/30] END C=0.024178578393312167, class_weight=None, l1_ratio=0.25, tol=0.09374296978935291;, score=0.951 total time=   0.5s
[CV 1/3; 27/30] START C=0.1633678116069095, class_weight=None, l1_ratio=0.25, tol=0.005710062580201412
[CV 1/3; 27/30] END C=0.1633678116069095, class_weight=None, l1_ratio=0.25, tol=0.005710062580201412;, score=0.890 total time=   2.7s
[CV 2/3; 27/30] START C=0.1633678116069095, class_weight=None, l1_ratio=0.25, tol=0.005710062580201412
[CV 2/3; 27/30] END C=0.1633678116069095, class_weight=None, l1_ratio=0.25, tol=0.005710062580201412;, score=0.989 total time=   3.2s
[CV 3/3; 27/30] START C=0.1633678116069095, class_weight=None, l1_ratio=0.25, tol=0.005710062580201412
[CV 3/3; 27/30] END C=0.1633678116069095, class_weight=None, l1_ratio=0.25, tol=0.005710062580201412;, score=0.965 total time=   3.0s
[CV 1/3; 28/30] START C=0.6427628875712578, class_weight=None, l1_ratio=0.75, tol=0.028872736013565083
[CV 1/3; 28/30] END C=0.6427628875712578, class_weight=None, l1_ratio=0.75, tol=0.028872736013565083;, score=0.916 total time=   1.0s
[CV 2/3; 28/30] START C=0.6427628875712578, class_weight=None, l1_ratio=0.75, tol=0.028872736013565083
[CV 2/3; 28/30] END C=0.6427628875712578, class_weight=None, l1_ratio=0.75, tol=0.028872736013565083;, score=0.987 total time=   1.0s
[CV 3/3; 28/30] START C=0.6427628875712578, class_weight=None, l1_ratio=0.75, tol=0.028872736013565083
[CV 3/3; 28/30] END C=0.6427628875712578, class_weight=None, l1_ratio=0.75, tol=0.028872736013565083;, score=0.960 total time=   1.0s
[CV 1/3; 29/30] START C=0.031109419751300094, class_weight=None, l1_ratio=1.0, tol=0.09624267268812914
[CV 1/3; 29/30] END C=0.031109419751300094, class_weight=None, l1_ratio=1.0, tol=0.09624267268812914;, score=0.932 total time=   0.5s
[CV 2/3; 29/30] START C=0.031109419751300094, class_weight=None, l1_ratio=1.0, tol=0.09624267268812914
[CV 2/3; 29/30] END C=0.031109419751300094, class_weight=None, l1_ratio=1.0, tol=0.09624267268812914;, score=0.974 total time=   0.5s
[CV 3/3; 29/30] START C=0.031109419751300094, class_weight=None, l1_ratio=1.0, tol=0.09624267268812914
[CV 3/3; 29/30] END C=0.031109419751300094, class_weight=None, l1_ratio=1.0, tol=0.09624267268812914;, score=0.948 total time=   0.5s
[CV 1/3; 30/30] START C=0.762270744858908, class_weight=None, l1_ratio=0.25, tol=0.005309571526513011
[CV 1/3; 30/30] END C=0.762270744858908, class_weight=None, l1_ratio=0.25, tol=0.005309571526513011;, score=0.861 total time=   3.9s
[CV 2/3; 30/30] START C=0.762270744858908, class_weight=None, l1_ratio=0.25, tol=0.005309571526513011
[CV 2/3; 30/30] END C=0.762270744858908, class_weight=None, l1_ratio=0.25, tol=0.005309571526513011;, score=0.990 total time=   4.0s
[CV 3/3; 30/30] START C=0.762270744858908, class_weight=None, l1_ratio=0.25, tol=0.005309571526513011
[CV 3/3; 30/30] END C=0.762270744858908, class_weight=None, l1_ratio=0.25, tol=0.005309571526513011;, score=0.968 total time=   3.7s

--- TUNING FINISHED ---
Beste Parameter: {'C': np.float64(0.007610786315553737), 'class_weight': None, 'l1_ratio': 0.0, 'tol': np.float64(0.02930597133315727)}
Bester CV-Score: 0.9571

--- EVALUATION AUF DEN TESTDATEN ---
Test Accuracy: 0.8542

Macro F1: 0.8029486278493914

--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.8542

                     precision    recall  f1-score   support

             B cell       0.96      0.98      0.97       120
     CD14+ monocyte       1.00      1.00      1.00      2575
        CD4+ T cell       0.78      1.00      0.88      3910
   Cytotoxic T cell       0.84      0.38      0.52      1824
     Dendritic cell       1.00      0.20      0.33         5
      Megakaryocyte       1.00      1.00      1.00         7
Natural killer cell       0.82      0.76      0.79       791
        Plasma cell       1.00      0.88      0.93        49

           accuracy                           0.85      9281
          macro avg       0.93      0.77      0.80      9281
       weighted avg       0.86      0.85      0.83      9281

Random dropout accuracy score 0.8301
Total samples: 9281
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.8508
Feature importance dropout (0.5% features dropped) accuracy score 0.8226
Feature importance dropout (1.0% features dropped) accuracy score 0.8038
Feature importance dropout (2.0% features dropped) accuracy score 0.7733
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8220

                     precision    recall  f1-score   support

             B cell       1.00      0.99      0.99      3960
     CD14+ monocyte       0.89      1.00      0.94      3135
        CD4+ T cell       0.83      1.00      0.91     13677
   Cytotoxic T cell       0.54      0.49      0.51      4843
     Dendritic cell       0.99      0.41      0.58       529
      Megakaryocyte       1.00      0.63      0.77        86
Natural killer cell       0.83      0.18      0.30      2751
        Plasma cell       0.66      0.83      0.73        23

           accuracy                           0.82     29004
          macro avg       0.84      0.69      0.72     29004
       weighted avg       0.82      0.82      0.79     29004

Random dropout accuracy score 0.8076
Total samples: 29004
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.8200
Feature importance dropout (0.5% features dropped) accuracy score 0.7955
Feature importance dropout (1.0% features dropped) accuracy score 0.7729
Feature importance dropout (2.0% features dropped) accuracy score 0.7030
=== JOB_STATISTICS ===
=== current date     : Sat Jun 27 23:31:12 CEST 2026
= Job-ID             : 11996032 on woody
= Job-Name           : autoencoder_lr
= Job-Command        : /home/hpc/iwbn/iwbn133h/submit_autoencoder_lr_v1.sh
= Initial workdir    : /home/hpc/iwbn/iwbn133h
= Queue/Partition    : work
= Slurm account      : iwbn with QOS=normal
= Features           : icx
= Requested resources:  for 17:00:00
= Elapsed runtime    : 02:43:54
= Total RAM usage    : 19.1 GiB of requested  GiB (%)   
= Node list          : w2315
= Subm/Elig/Start/End: 2026-06-27T20:47:17 / 2026-06-27T20:47:17 / 2026-06-27T20:47:18 / 2026-06-27T23:31:12
======================
=== Quota infos ======
    Path                 Used     SoftQ    HardQ    Gracetime  Filec    FileQ    FiHaQ    FileGrace    
    /home/woody           982.1M  1000.0G  1500.0G        N/A  29,019    5,000K   7,500K        N/A    
    /home/hpc              86.2G   104.9G   209.7G        N/A     139K     500K   1,000K        N/A    
    /home/vault             0.0K  1048.6G  2097.2G        N/A       1      200K     400K        N/A    
