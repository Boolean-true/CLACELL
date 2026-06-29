### Starting TaskPrologue of job 12000012 on w2316 at Mon Jun 29 09:08:41 CEST 2026
#   SLURM_JOB_NODELIST=w2316
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
Start Conditional DAE Training...
Epoch [1/150], Loss: 0.9430
Epoch [10/150], Loss: 0.9071
Epoch [20/150], Loss: 0.8995
Epoch [30/150], Loss: 0.8950
Epoch [40/150], Loss: 0.8933
Early Stopping after [40/150] Epochs!

Extract robust features...
Starte automatische Hyperparametersuche auf dem Latent Space...
Fitting 3 folds for each of 50 candidates, totalling 150 fits
[CV 1/3; 1/50] START C=0.0037901135851264238, class_weight=None, l1_ratio=0.5, tol=0.019654900404282125
[CV 1/3; 1/50] END C=0.0037901135851264238, class_weight=None, l1_ratio=0.5, tol=0.019654900404282125;, score=0.940 total time=   1.2s
[CV 2/3; 1/50] START C=0.0037901135851264238, class_weight=None, l1_ratio=0.5, tol=0.019654900404282125
[CV 2/3; 1/50] END C=0.0037901135851264238, class_weight=None, l1_ratio=0.5, tol=0.019654900404282125;, score=0.968 total time=   1.2s
[CV 3/3; 1/50] START C=0.0037901135851264238, class_weight=None, l1_ratio=0.5, tol=0.019654900404282125
[CV 3/3; 1/50] END C=0.0037901135851264238, class_weight=None, l1_ratio=0.5, tol=0.019654900404282125;, score=0.945 total time=   1.2s
[CV 1/3; 2/50] START C=0.04073071820454446, class_weight=None, l1_ratio=0.5, tol=0.007663645860354331
[CV 1/3; 2/50] END C=0.04073071820454446, class_weight=None, l1_ratio=0.5, tol=0.007663645860354331;, score=0.940 total time=   3.0s
[CV 2/3; 2/50] START C=0.04073071820454446, class_weight=None, l1_ratio=0.5, tol=0.007663645860354331
[CV 2/3; 2/50] END C=0.04073071820454446, class_weight=None, l1_ratio=0.5, tol=0.007663645860354331;, score=0.980 total time=   2.5s
[CV 3/3; 2/50] START C=0.04073071820454446, class_weight=None, l1_ratio=0.5, tol=0.007663645860354331
[CV 3/3; 2/50] END C=0.04073071820454446, class_weight=None, l1_ratio=0.5, tol=0.007663645860354331;, score=0.953 total time=   2.4s
[CV 1/3; 3/50] START C=0.0024841772536124086, class_weight=balanced, l1_ratio=0.5, tol=0.013590214068179242
[CV 1/3; 3/50] END C=0.0024841772536124086, class_weight=balanced, l1_ratio=0.5, tol=0.013590214068179242;, score=0.920 total time=   1.9s
[CV 2/3; 3/50] START C=0.0024841772536124086, class_weight=balanced, l1_ratio=0.5, tol=0.013590214068179242
[CV 2/3; 3/50] END C=0.0024841772536124086, class_weight=balanced, l1_ratio=0.5, tol=0.013590214068179242;, score=0.976 total time=   1.9s
[CV 3/3; 3/50] START C=0.0024841772536124086, class_weight=balanced, l1_ratio=0.5, tol=0.013590214068179242
[CV 3/3; 3/50] END C=0.0024841772536124086, class_weight=balanced, l1_ratio=0.5, tol=0.013590214068179242;, score=0.948 total time=   1.8s
[CV 1/3; 4/50] START C=0.5840575219934756, class_weight=None, l1_ratio=0.0, tol=0.08047385626397517
[CV 1/3; 4/50] END C=0.5840575219934756, class_weight=None, l1_ratio=0.0, tol=0.08047385626397517;, score=0.940 total time=   0.5s
[CV 2/3; 4/50] START C=0.5840575219934756, class_weight=None, l1_ratio=0.0, tol=0.08047385626397517
[CV 2/3; 4/50] END C=0.5840575219934756, class_weight=None, l1_ratio=0.0, tol=0.08047385626397517;, score=0.959 total time=   0.5s
[CV 3/3; 4/50] START C=0.5840575219934756, class_weight=None, l1_ratio=0.0, tol=0.08047385626397517
[CV 3/3; 4/50] END C=0.5840575219934756, class_weight=None, l1_ratio=0.0, tol=0.08047385626397517;, score=0.933 total time=   0.5s
[CV 1/3; 5/50] START C=0.031176450408368542, class_weight=None, l1_ratio=0.0, tol=0.05611086613848696
[CV 1/3; 5/50] END C=0.031176450408368542, class_weight=None, l1_ratio=0.0, tol=0.05611086613848696;, score=0.945 total time=   0.6s
[CV 2/3; 5/50] START C=0.031176450408368542, class_weight=None, l1_ratio=0.0, tol=0.05611086613848696
[CV 2/3; 5/50] END C=0.031176450408368542, class_weight=None, l1_ratio=0.0, tol=0.05611086613848696;, score=0.964 total time=   0.5s
[CV 3/3; 5/50] START C=0.031176450408368542, class_weight=None, l1_ratio=0.0, tol=0.05611086613848696
[CV 3/3; 5/50] END C=0.031176450408368542, class_weight=None, l1_ratio=0.0, tol=0.05611086613848696;, score=0.938 total time=   0.5s
[CV 1/3; 6/50] START C=0.006662287211499492, class_weight=balanced, l1_ratio=1.0, tol=0.0027438654856290234
[CV 1/3; 6/50] END C=0.006662287211499492, class_weight=balanced, l1_ratio=1.0, tol=0.0027438654856290234;, score=0.915 total time=   7.0s
[CV 2/3; 6/50] START C=0.006662287211499492, class_weight=balanced, l1_ratio=1.0, tol=0.0027438654856290234
[CV 2/3; 6/50] END C=0.006662287211499492, class_weight=balanced, l1_ratio=1.0, tol=0.0027438654856290234;, score=0.978 total time=   7.0s
[CV 3/3; 6/50] START C=0.006662287211499492, class_weight=balanced, l1_ratio=1.0, tol=0.0027438654856290234
[CV 3/3; 6/50] END C=0.006662287211499492, class_weight=balanced, l1_ratio=1.0, tol=0.0027438654856290234;, score=0.949 total time=   9.5s
[CV 1/3; 7/50] START C=0.028450690911870958, class_weight=None, l1_ratio=0.5, tol=0.02922861543133648
[CV 1/3; 7/50] END C=0.028450690911870958, class_weight=None, l1_ratio=0.5, tol=0.02922861543133648;, score=0.943 total time=   1.0s
[CV 2/3; 7/50] START C=0.028450690911870958, class_weight=None, l1_ratio=0.5, tol=0.02922861543133648
[CV 2/3; 7/50] END C=0.028450690911870958, class_weight=None, l1_ratio=0.5, tol=0.02922861543133648;, score=0.971 total time=   1.0s
[CV 3/3; 7/50] START C=0.028450690911870958, class_weight=None, l1_ratio=0.5, tol=0.02922861543133648
[CV 3/3; 7/50] END C=0.028450690911870958, class_weight=None, l1_ratio=0.5, tol=0.02922861543133648;, score=0.944 total time=   0.9s
[CV 1/3; 8/50] START C=0.010550347182694807, class_weight=balanced, l1_ratio=1.0, tol=0.02158774662521185
[CV 1/3; 8/50] END C=0.010550347182694807, class_weight=balanced, l1_ratio=1.0, tol=0.02158774662521185;, score=0.923 total time=   1.3s
[CV 2/3; 8/50] START C=0.010550347182694807, class_weight=balanced, l1_ratio=1.0, tol=0.02158774662521185
[CV 2/3; 8/50] END C=0.010550347182694807, class_weight=balanced, l1_ratio=1.0, tol=0.02158774662521185;, score=0.977 total time=   1.2s
[CV 3/3; 8/50] START C=0.010550347182694807, class_weight=balanced, l1_ratio=1.0, tol=0.02158774662521185
[CV 3/3; 8/50] END C=0.010550347182694807, class_weight=balanced, l1_ratio=1.0, tol=0.02158774662521185;, score=0.952 total time=   1.4s
[CV 1/3; 9/50] START C=0.007045463164131204, class_weight=None, l1_ratio=0.0, tol=0.09774376492290797
[CV 1/3; 9/50] END C=0.007045463164131204, class_weight=None, l1_ratio=0.0, tol=0.09774376492290797;, score=0.942 total time=   0.5s
[CV 2/3; 9/50] START C=0.007045463164131204, class_weight=None, l1_ratio=0.0, tol=0.09774376492290797
[CV 2/3; 9/50] END C=0.007045463164131204, class_weight=None, l1_ratio=0.0, tol=0.09774376492290797;, score=0.959 total time=   0.5s
[CV 3/3; 9/50] START C=0.007045463164131204, class_weight=None, l1_ratio=0.0, tol=0.09774376492290797
[CV 3/3; 9/50] END C=0.007045463164131204, class_weight=None, l1_ratio=0.0, tol=0.09774376492290797;, score=0.934 total time=   0.5s
[CV 1/3; 10/50] START C=0.4093794779165975, class_weight=None, l1_ratio=0.0, tol=0.07223729383206183
[CV 1/3; 10/50] END C=0.4093794779165975, class_weight=None, l1_ratio=0.0, tol=0.07223729383206183;, score=0.943 total time=   0.5s
[CV 2/3; 10/50] START C=0.4093794779165975, class_weight=None, l1_ratio=0.0, tol=0.07223729383206183
[CV 2/3; 10/50] END C=0.4093794779165975, class_weight=None, l1_ratio=0.0, tol=0.07223729383206183;, score=0.962 total time=   0.5s
[CV 3/3; 10/50] START C=0.4093794779165975, class_weight=None, l1_ratio=0.0, tol=0.07223729383206183
[CV 3/3; 10/50] END C=0.4093794779165975, class_weight=None, l1_ratio=0.0, tol=0.07223729383206183;, score=0.938 total time=   0.5s
[CV 1/3; 11/50] START C=0.010679009718868593, class_weight=None, l1_ratio=0.5, tol=0.009911268147716453
[CV 1/3; 11/50] END C=0.010679009718868593, class_weight=None, l1_ratio=0.5, tol=0.009911268147716453;, score=0.940 total time=   2.3s
[CV 2/3; 11/50] START C=0.010679009718868593, class_weight=None, l1_ratio=0.5, tol=0.009911268147716453
[CV 2/3; 11/50] END C=0.010679009718868593, class_weight=None, l1_ratio=0.5, tol=0.009911268147716453;, score=0.976 total time=   1.9s
[CV 3/3; 11/50] START C=0.010679009718868593, class_weight=None, l1_ratio=0.5, tol=0.009911268147716453
[CV 3/3; 11/50] END C=0.010679009718868593, class_weight=None, l1_ratio=0.5, tol=0.009911268147716453;, score=0.951 total time=   1.9s
[CV 1/3; 12/50] START C=0.030753643917794816, class_weight=balanced, l1_ratio=1.0, tol=0.03829672518539113
[CV 1/3; 12/50] END C=0.030753643917794816, class_weight=balanced, l1_ratio=1.0, tol=0.03829672518539113;, score=0.925 total time=   0.9s
[CV 2/3; 12/50] START C=0.030753643917794816, class_weight=balanced, l1_ratio=1.0, tol=0.03829672518539113
[CV 2/3; 12/50] END C=0.030753643917794816, class_weight=balanced, l1_ratio=1.0, tol=0.03829672518539113;, score=0.978 total time=   1.0s
[CV 3/3; 12/50] START C=0.030753643917794816, class_weight=balanced, l1_ratio=1.0, tol=0.03829672518539113
[CV 3/3; 12/50] END C=0.030753643917794816, class_weight=balanced, l1_ratio=1.0, tol=0.03829672518539113;, score=0.949 total time=   0.9s
[CV 1/3; 13/50] START C=0.04841974768891323, class_weight=None, l1_ratio=0.5, tol=0.08980489021507274
[CV 1/3; 13/50] END C=0.04841974768891323, class_weight=None, l1_ratio=0.5, tol=0.08980489021507274;, score=0.940 total time=   0.6s
[CV 2/3; 13/50] START C=0.04841974768891323, class_weight=None, l1_ratio=0.5, tol=0.08980489021507274
[CV 2/3; 13/50] END C=0.04841974768891323, class_weight=None, l1_ratio=0.5, tol=0.08980489021507274;, score=0.959 total time=   0.6s
[CV 3/3; 13/50] START C=0.04841974768891323, class_weight=None, l1_ratio=0.5, tol=0.08980489021507274
[CV 3/3; 13/50] END C=0.04841974768891323, class_weight=None, l1_ratio=0.5, tol=0.08980489021507274;, score=0.935 total time=   0.6s
[CV 1/3; 14/50] START C=0.005078422779052986, class_weight=balanced, l1_ratio=0.5, tol=0.002849654274186834
[CV 1/3; 14/50] END C=0.005078422779052986, class_weight=balanced, l1_ratio=0.5, tol=0.002849654274186834;, score=0.917 total time=   6.5s
[CV 2/3; 14/50] START C=0.005078422779052986, class_weight=balanced, l1_ratio=0.5, tol=0.002849654274186834
[CV 2/3; 14/50] END C=0.005078422779052986, class_weight=balanced, l1_ratio=0.5, tol=0.002849654274186834;, score=0.980 total time=   5.5s
[CV 3/3; 14/50] START C=0.005078422779052986, class_weight=balanced, l1_ratio=0.5, tol=0.002849654274186834
[CV 3/3; 14/50] END C=0.005078422779052986, class_weight=balanced, l1_ratio=0.5, tol=0.002849654274186834;, score=0.952 total time=   5.7s
[CV 1/3; 15/50] START C=0.02224187122028436, class_weight=None, l1_ratio=0.0, tol=0.028986931995239697
[CV 1/3; 15/50] END C=0.02224187122028436, class_weight=None, l1_ratio=0.0, tol=0.028986931995239697;, score=0.944 total time=   0.7s
[CV 2/3; 15/50] START C=0.02224187122028436, class_weight=None, l1_ratio=0.0, tol=0.028986931995239697
[CV 2/3; 15/50] END C=0.02224187122028436, class_weight=None, l1_ratio=0.0, tol=0.028986931995239697;, score=0.971 total time=   0.7s
[CV 3/3; 15/50] START C=0.02224187122028436, class_weight=None, l1_ratio=0.0, tol=0.028986931995239697
[CV 3/3; 15/50] END C=0.02224187122028436, class_weight=None, l1_ratio=0.0, tol=0.028986931995239697;, score=0.945 total time=   0.7s
[CV 1/3; 16/50] START C=0.004250967425366947, class_weight=None, l1_ratio=0.0, tol=0.0021810959876584846
[CV 1/3; 16/50] END C=0.004250967425366947, class_weight=None, l1_ratio=0.0, tol=0.0021810959876584846;, score=0.937 total time=   4.1s
[CV 2/3; 16/50] START C=0.004250967425366947, class_weight=None, l1_ratio=0.0, tol=0.0021810959876584846
[CV 2/3; 16/50] END C=0.004250967425366947, class_weight=None, l1_ratio=0.0, tol=0.0021810959876584846;, score=0.984 total time=   4.3s
[CV 3/3; 16/50] START C=0.004250967425366947, class_weight=None, l1_ratio=0.0, tol=0.0021810959876584846
[CV 3/3; 16/50] END C=0.004250967425366947, class_weight=None, l1_ratio=0.0, tol=0.0021810959876584846;, score=0.955 total time=   3.9s
[CV 1/3; 17/50] START C=0.004223863922562596, class_weight=None, l1_ratio=0.0, tol=0.0010751674340096415
[CV 1/3; 17/50] END C=0.004223863922562596, class_weight=None, l1_ratio=0.0, tol=0.0010751674340096415;, score=0.935 total time=   7.2s
[CV 2/3; 17/50] START C=0.004223863922562596, class_weight=None, l1_ratio=0.0, tol=0.0010751674340096415
[CV 2/3; 17/50] END C=0.004223863922562596, class_weight=None, l1_ratio=0.0, tol=0.0010751674340096415;, score=0.984 total time=   7.2s
[CV 3/3; 17/50] START C=0.004223863922562596, class_weight=None, l1_ratio=0.0, tol=0.0010751674340096415
[CV 3/3; 17/50] END C=0.004223863922562596, class_weight=None, l1_ratio=0.0, tol=0.0010751674340096415;, score=0.958 total time=   7.6s
[CV 1/3; 18/50] START C=0.0016764937627462859, class_weight=balanced, l1_ratio=0.5, tol=0.010941187252149724
[CV 1/3; 18/50] END C=0.0016764937627462859, class_weight=balanced, l1_ratio=0.5, tol=0.010941187252149724;, score=0.915 total time=   2.3s
[CV 2/3; 18/50] START C=0.0016764937627462859, class_weight=balanced, l1_ratio=0.5, tol=0.010941187252149724
[CV 2/3; 18/50] END C=0.0016764937627462859, class_weight=balanced, l1_ratio=0.5, tol=0.010941187252149724;, score=0.972 total time=   2.1s
[CV 3/3; 18/50] START C=0.0016764937627462859, class_weight=balanced, l1_ratio=0.5, tol=0.010941187252149724
[CV 3/3; 18/50] END C=0.0016764937627462859, class_weight=balanced, l1_ratio=0.5, tol=0.010941187252149724;, score=0.944 total time=   2.6s
[CV 1/3; 19/50] START C=0.005793218623302614, class_weight=balanced, l1_ratio=0.0, tol=0.028860810392249484
[CV 1/3; 19/50] END C=0.005793218623302614, class_weight=balanced, l1_ratio=0.0, tol=0.028860810392249484;, score=0.926 total time=   0.8s
[CV 2/3; 19/50] START C=0.005793218623302614, class_weight=balanced, l1_ratio=0.0, tol=0.028860810392249484
[CV 2/3; 19/50] END C=0.005793218623302614, class_weight=balanced, l1_ratio=0.0, tol=0.028860810392249484;, score=0.977 total time=   0.7s
[CV 3/3; 19/50] START C=0.005793218623302614, class_weight=balanced, l1_ratio=0.0, tol=0.028860810392249484
[CV 3/3; 19/50] END C=0.005793218623302614, class_weight=balanced, l1_ratio=0.0, tol=0.028860810392249484;, score=0.950 total time=   0.7s
[CV 1/3; 20/50] START C=0.001130990286794495, class_weight=balanced, l1_ratio=0.0, tol=0.0022179795632549216
[CV 1/3; 20/50] END C=0.001130990286794495, class_weight=balanced, l1_ratio=0.0, tol=0.0022179795632549216;, score=0.919 total time=   3.1s
[CV 2/3; 20/50] START C=0.001130990286794495, class_weight=balanced, l1_ratio=0.0, tol=0.0022179795632549216
[CV 2/3; 20/50] END C=0.001130990286794495, class_weight=balanced, l1_ratio=0.0, tol=0.0022179795632549216;, score=0.982 total time=   2.7s
[CV 3/3; 20/50] START C=0.001130990286794495, class_weight=balanced, l1_ratio=0.0, tol=0.0022179795632549216
[CV 3/3; 20/50] END C=0.001130990286794495, class_weight=balanced, l1_ratio=0.0, tol=0.0022179795632549216;, score=0.958 total time=   3.5s
[CV 1/3; 21/50] START C=0.0024110759541160817, class_weight=balanced, l1_ratio=1.0, tol=0.005388378541059072
[CV 1/3; 21/50] END C=0.0024110759541160817, class_weight=balanced, l1_ratio=1.0, tol=0.005388378541059072;, score=0.908 total time=   4.2s
[CV 2/3; 21/50] START C=0.0024110759541160817, class_weight=balanced, l1_ratio=1.0, tol=0.005388378541059072
[CV 2/3; 21/50] END C=0.0024110759541160817, class_weight=balanced, l1_ratio=1.0, tol=0.005388378541059072;, score=0.964 total time=  13.2s
[CV 3/3; 21/50] START C=0.0024110759541160817, class_weight=balanced, l1_ratio=1.0, tol=0.005388378541059072
[CV 3/3; 21/50] END C=0.0024110759541160817, class_weight=balanced, l1_ratio=1.0, tol=0.005388378541059072;, score=0.935 total time=   4.6s
[CV 1/3; 22/50] START C=1.9985411215223088, class_weight=None, l1_ratio=0.0, tol=0.00410421283248711
[CV 1/3; 22/50] END C=1.9985411215223088, class_weight=None, l1_ratio=0.0, tol=0.00410421283248711;, score=0.939 total time=   3.1s
[CV 2/3; 22/50] START C=1.9985411215223088, class_weight=None, l1_ratio=0.0, tol=0.00410421283248711
[CV 2/3; 22/50] END C=1.9985411215223088, class_weight=None, l1_ratio=0.0, tol=0.00410421283248711;, score=0.983 total time=   2.7s
[CV 3/3; 22/50] START C=1.9985411215223088, class_weight=None, l1_ratio=0.0, tol=0.00410421283248711
[CV 3/3; 22/50] END C=1.9985411215223088, class_weight=None, l1_ratio=0.0, tol=0.00410421283248711;, score=0.955 total time=   2.5s
[CV 1/3; 23/50] START C=0.005461285805027931, class_weight=None, l1_ratio=0.5, tol=0.0016106530930473546
[CV 1/3; 23/50] END C=0.005461285805027931, class_weight=None, l1_ratio=0.5, tol=0.0016106530930473546;, score=0.937 total time=  13.2s
[CV 2/3; 23/50] START C=0.005461285805027931, class_weight=None, l1_ratio=0.5, tol=0.0016106530930473546
[CV 2/3; 23/50] END C=0.005461285805027931, class_weight=None, l1_ratio=0.5, tol=0.0016106530930473546;, score=0.978 total time=   8.6s
[CV 3/3; 23/50] START C=0.005461285805027931, class_weight=None, l1_ratio=0.5, tol=0.0016106530930473546
[CV 3/3; 23/50] END C=0.005461285805027931, class_weight=None, l1_ratio=0.5, tol=0.0016106530930473546;, score=0.953 total time=  10.4s
[CV 1/3; 24/50] START C=0.014705808144017254, class_weight=balanced, l1_ratio=0.0, tol=0.0010329313105844843
[CV 1/3; 24/50] END C=0.014705808144017254, class_weight=balanced, l1_ratio=0.0, tol=0.0010329313105844843;, score=0.915 total time=   7.3s
[CV 2/3; 24/50] START C=0.014705808144017254, class_weight=balanced, l1_ratio=0.0, tol=0.0010329313105844843
[CV 2/3; 24/50] END C=0.014705808144017254, class_weight=balanced, l1_ratio=0.0, tol=0.0010329313105844843;, score=0.984 total time=   7.1s
[CV 3/3; 24/50] START C=0.014705808144017254, class_weight=balanced, l1_ratio=0.0, tol=0.0010329313105844843
[CV 3/3; 24/50] END C=0.014705808144017254, class_weight=balanced, l1_ratio=0.0, tol=0.0010329313105844843;, score=0.958 total time=   8.0s
[CV 1/3; 25/50] START C=0.2525723584030682, class_weight=None, l1_ratio=0.5, tol=0.009877693656177756
[CV 1/3; 25/50] END C=0.2525723584030682, class_weight=None, l1_ratio=0.5, tol=0.009877693656177756;, score=0.940 total time=   2.3s
[CV 2/3; 25/50] START C=0.2525723584030682, class_weight=None, l1_ratio=0.5, tol=0.009877693656177756
[CV 2/3; 25/50] END C=0.2525723584030682, class_weight=None, l1_ratio=0.5, tol=0.009877693656177756;, score=0.979 total time=   2.1s
[CV 3/3; 25/50] START C=0.2525723584030682, class_weight=None, l1_ratio=0.5, tol=0.009877693656177756
[CV 3/3; 25/50] END C=0.2525723584030682, class_weight=None, l1_ratio=0.5, tol=0.009877693656177756;, score=0.952 total time=   1.9s
[CV 1/3; 26/50] START C=0.0037348726724403445, class_weight=balanced, l1_ratio=1.0, tol=0.002095938571625005
[CV 1/3; 26/50] END C=0.0037348726724403445, class_weight=balanced, l1_ratio=1.0, tol=0.002095938571625005;, score=0.910 total time=  10.5s
[CV 2/3; 26/50] START C=0.0037348726724403445, class_weight=balanced, l1_ratio=1.0, tol=0.002095938571625005
[CV 2/3; 26/50] END C=0.0037348726724403445, class_weight=balanced, l1_ratio=1.0, tol=0.002095938571625005;, score=0.971 total time=  15.5s
[CV 3/3; 26/50] START C=0.0037348726724403445, class_weight=balanced, l1_ratio=1.0, tol=0.002095938571625005
[CV 3/3; 26/50] END C=0.0037348726724403445, class_weight=balanced, l1_ratio=1.0, tol=0.002095938571625005;, score=0.941 total time=   9.2s
[CV 1/3; 27/50] START C=0.14654232996378913, class_weight=balanced, l1_ratio=0.5, tol=0.01588999465151337
[CV 1/3; 27/50] END C=0.14654232996378913, class_weight=balanced, l1_ratio=0.5, tol=0.01588999465151337;, score=0.923 total time=   1.6s
[CV 2/3; 27/50] START C=0.14654232996378913, class_weight=balanced, l1_ratio=0.5, tol=0.01588999465151337
[CV 2/3; 27/50] END C=0.14654232996378913, class_weight=balanced, l1_ratio=0.5, tol=0.01588999465151337;, score=0.980 total time=   1.5s
[CV 3/3; 27/50] START C=0.14654232996378913, class_weight=balanced, l1_ratio=0.5, tol=0.01588999465151337
[CV 3/3; 27/50] END C=0.14654232996378913, class_weight=balanced, l1_ratio=0.5, tol=0.01588999465151337;, score=0.953 total time=   1.5s
[CV 1/3; 28/50] START C=1.7601627138068543, class_weight=balanced, l1_ratio=0.5, tol=0.017969150658740326
[CV 1/3; 28/50] END C=1.7601627138068543, class_weight=balanced, l1_ratio=0.5, tol=0.017969150658740326;, score=0.924 total time=   1.5s
[CV 2/3; 28/50] START C=1.7601627138068543, class_weight=balanced, l1_ratio=0.5, tol=0.017969150658740326
[CV 2/3; 28/50] END C=1.7601627138068543, class_weight=balanced, l1_ratio=0.5, tol=0.017969150658740326;, score=0.979 total time=   1.4s
[CV 3/3; 28/50] START C=1.7601627138068543, class_weight=balanced, l1_ratio=0.5, tol=0.017969150658740326
[CV 3/3; 28/50] END C=1.7601627138068543, class_weight=balanced, l1_ratio=0.5, tol=0.017969150658740326;, score=0.953 total time=   1.3s
[CV 1/3; 29/50] START C=0.043707277145916115, class_weight=None, l1_ratio=0.5, tol=0.08849354575896523
[CV 1/3; 29/50] END C=0.043707277145916115, class_weight=None, l1_ratio=0.5, tol=0.08849354575896523;, score=0.940 total time=   0.6s
[CV 2/3; 29/50] START C=0.043707277145916115, class_weight=None, l1_ratio=0.5, tol=0.08849354575896523
[CV 2/3; 29/50] END C=0.043707277145916115, class_weight=None, l1_ratio=0.5, tol=0.08849354575896523;, score=0.960 total time=   0.6s
[CV 3/3; 29/50] START C=0.043707277145916115, class_weight=None, l1_ratio=0.5, tol=0.08849354575896523
[CV 3/3; 29/50] END C=0.043707277145916115, class_weight=None, l1_ratio=0.5, tol=0.08849354575896523;, score=0.934 total time=   0.6s
[CV 1/3; 30/50] START C=0.2658054394421334, class_weight=balanced, l1_ratio=0.5, tol=0.005366949347657695
[CV 1/3; 30/50] END C=0.2658054394421334, class_weight=balanced, l1_ratio=0.5, tol=0.005366949347657695;, score=0.920 total time=   3.6s
[CV 2/3; 30/50] START C=0.2658054394421334, class_weight=balanced, l1_ratio=0.5, tol=0.005366949347657695
[CV 2/3; 30/50] END C=0.2658054394421334, class_weight=balanced, l1_ratio=0.5, tol=0.005366949347657695;, score=0.982 total time=   3.8s
[CV 3/3; 30/50] START C=0.2658054394421334, class_weight=balanced, l1_ratio=0.5, tol=0.005366949347657695
[CV 3/3; 30/50] END C=0.2658054394421334, class_weight=balanced, l1_ratio=0.5, tol=0.005366949347657695;, score=0.956 total time=   3.4s
[CV 1/3; 31/50] START C=0.1913494533618556, class_weight=balanced, l1_ratio=1.0, tol=0.002935842227139481
[CV 1/3; 31/50] END C=0.1913494533618556, class_weight=balanced, l1_ratio=1.0, tol=0.002935842227139481;, score=0.918 total time=   6.0s
[CV 2/3; 31/50] START C=0.1913494533618556, class_weight=balanced, l1_ratio=1.0, tol=0.002935842227139481
[CV 2/3; 31/50] END C=0.1913494533618556, class_weight=balanced, l1_ratio=1.0, tol=0.002935842227139481;, score=0.983 total time=   5.9s
[CV 3/3; 31/50] START C=0.1913494533618556, class_weight=balanced, l1_ratio=1.0, tol=0.002935842227139481
[CV 3/3; 31/50] END C=0.1913494533618556, class_weight=balanced, l1_ratio=1.0, tol=0.002935842227139481;, score=0.958 total time=   5.4s
[CV 1/3; 32/50] START C=0.303211371783339, class_weight=balanced, l1_ratio=0.0, tol=0.0015171474283726372
[CV 1/3; 32/50] END C=0.303211371783339, class_weight=balanced, l1_ratio=0.0, tol=0.0015171474283726372;, score=0.915 total time=   5.9s
[CV 2/3; 32/50] START C=0.303211371783339, class_weight=balanced, l1_ratio=0.0, tol=0.0015171474283726372
[CV 2/3; 32/50] END C=0.303211371783339, class_weight=balanced, l1_ratio=0.0, tol=0.0015171474283726372;, score=0.985 total time=   5.5s
[CV 3/3; 32/50] START C=0.303211371783339, class_weight=balanced, l1_ratio=0.0, tol=0.0015171474283726372
[CV 3/3; 32/50] END C=0.303211371783339, class_weight=balanced, l1_ratio=0.0, tol=0.0015171474283726372;, score=0.957 total time=   6.7s
[CV 1/3; 33/50] START C=0.018369313494789555, class_weight=balanced, l1_ratio=0.5, tol=0.09504059826082449
[CV 1/3; 33/50] END C=0.018369313494789555, class_weight=balanced, l1_ratio=0.5, tol=0.09504059826082449;, score=0.927 total time=   0.6s
[CV 2/3; 33/50] START C=0.018369313494789555, class_weight=balanced, l1_ratio=0.5, tol=0.09504059826082449
[CV 2/3; 33/50] END C=0.018369313494789555, class_weight=balanced, l1_ratio=0.5, tol=0.09504059826082449;, score=0.975 total time=   0.7s
[CV 3/3; 33/50] START C=0.018369313494789555, class_weight=balanced, l1_ratio=0.5, tol=0.09504059826082449
[CV 3/3; 33/50] END C=0.018369313494789555, class_weight=balanced, l1_ratio=0.5, tol=0.09504059826082449;, score=0.950 total time=   0.9s
[CV 1/3; 34/50] START C=0.6626879707720471, class_weight=balanced, l1_ratio=0.5, tol=0.03459256434787893
[CV 1/3; 34/50] END C=0.6626879707720471, class_weight=balanced, l1_ratio=0.5, tol=0.03459256434787893;, score=0.924 total time=   1.0s
[CV 2/3; 34/50] START C=0.6626879707720471, class_weight=balanced, l1_ratio=0.5, tol=0.03459256434787893
[CV 2/3; 34/50] END C=0.6626879707720471, class_weight=balanced, l1_ratio=0.5, tol=0.03459256434787893;, score=0.977 total time=   0.9s
[CV 3/3; 34/50] START C=0.6626879707720471, class_weight=balanced, l1_ratio=0.5, tol=0.03459256434787893
[CV 3/3; 34/50] END C=0.6626879707720471, class_weight=balanced, l1_ratio=0.5, tol=0.03459256434787893;, score=0.950 total time=   0.9s
[CV 1/3; 35/50] START C=0.005618607232828532, class_weight=balanced, l1_ratio=1.0, tol=0.0017741597396099221
[CV 1/3; 35/50] END C=0.005618607232828532, class_weight=balanced, l1_ratio=1.0, tol=0.0017741597396099221;, score=0.915 total time=  11.7s
[CV 2/3; 35/50] START C=0.005618607232828532, class_weight=balanced, l1_ratio=1.0, tol=0.0017741597396099221
[CV 2/3; 35/50] END C=0.005618607232828532, class_weight=balanced, l1_ratio=1.0, tol=0.0017741597396099221;, score=0.975 total time=   9.9s
[CV 3/3; 35/50] START C=0.005618607232828532, class_weight=balanced, l1_ratio=1.0, tol=0.0017741597396099221
[CV 3/3; 35/50] END C=0.005618607232828532, class_weight=balanced, l1_ratio=1.0, tol=0.0017741597396099221;, score=0.946 total time=  13.3s
[CV 1/3; 36/50] START C=0.04949528341420957, class_weight=None, l1_ratio=0.5, tol=0.0011986319746729198
[CV 1/3; 36/50] END C=0.04949528341420957, class_weight=None, l1_ratio=0.5, tol=0.0011986319746729198;, score=0.932 total time=  20.3s
[CV 2/3; 36/50] START C=0.04949528341420957, class_weight=None, l1_ratio=0.5, tol=0.0011986319746729198
[CV 2/3; 36/50] END C=0.04949528341420957, class_weight=None, l1_ratio=0.5, tol=0.0011986319746729198;, score=0.984 total time=  19.0s
[CV 3/3; 36/50] START C=0.04949528341420957, class_weight=None, l1_ratio=0.5, tol=0.0011986319746729198
[CV 3/3; 36/50] END C=0.04949528341420957, class_weight=None, l1_ratio=0.5, tol=0.0011986319746729198;, score=0.959 total time=  17.8s
[CV 1/3; 37/50] START C=0.1126462227765609, class_weight=None, l1_ratio=0.5, tol=0.021756775277401406
[CV 1/3; 37/50] END C=0.1126462227765609, class_weight=None, l1_ratio=0.5, tol=0.021756775277401406;, score=0.944 total time=   1.3s
[CV 2/3; 37/50] START C=0.1126462227765609, class_weight=None, l1_ratio=0.5, tol=0.021756775277401406
[CV 2/3; 37/50] END C=0.1126462227765609, class_weight=None, l1_ratio=0.5, tol=0.021756775277401406;, score=0.973 total time=   1.2s
[CV 3/3; 37/50] START C=0.1126462227765609, class_weight=None, l1_ratio=0.5, tol=0.021756775277401406
[CV 3/3; 37/50] END C=0.1126462227765609, class_weight=None, l1_ratio=0.5, tol=0.021756775277401406;, score=0.948 total time=   1.1s
[CV 1/3; 38/50] START C=1.6007427546110196, class_weight=balanced, l1_ratio=1.0, tol=0.0010505904501951094
[CV 1/3; 38/50] END C=1.6007427546110196, class_weight=balanced, l1_ratio=1.0, tol=0.0010505904501951094;, score=0.909 total time=  23.6s
[CV 2/3; 38/50] START C=1.6007427546110196, class_weight=balanced, l1_ratio=1.0, tol=0.0010505904501951094
[CV 2/3; 38/50] END C=1.6007427546110196, class_weight=balanced, l1_ratio=1.0, tol=0.0010505904501951094;, score=0.984 total time=  19.3s
[CV 3/3; 38/50] START C=1.6007427546110196, class_weight=balanced, l1_ratio=1.0, tol=0.0010505904501951094
[CV 3/3; 38/50] END C=1.6007427546110196, class_weight=balanced, l1_ratio=1.0, tol=0.0010505904501951094;, score=0.959 total time=  18.1s
[CV 1/3; 39/50] START C=0.885333904646105, class_weight=balanced, l1_ratio=1.0, tol=0.036963015797345004
[CV 1/3; 39/50] END C=0.885333904646105, class_weight=balanced, l1_ratio=1.0, tol=0.036963015797345004;, score=0.926 total time=   0.9s
[CV 2/3; 39/50] START C=0.885333904646105, class_weight=balanced, l1_ratio=1.0, tol=0.036963015797345004
[CV 2/3; 39/50] END C=0.885333904646105, class_weight=balanced, l1_ratio=1.0, tol=0.036963015797345004;, score=0.978 total time=   1.0s
[CV 3/3; 39/50] START C=0.885333904646105, class_weight=balanced, l1_ratio=1.0, tol=0.036963015797345004
[CV 3/3; 39/50] END C=0.885333904646105, class_weight=balanced, l1_ratio=1.0, tol=0.036963015797345004;, score=0.949 total time=   0.9s
[CV 1/3; 40/50] START C=0.3445110139330698, class_weight=None, l1_ratio=1.0, tol=0.0026886077958965947
[CV 1/3; 40/50] END C=0.3445110139330698, class_weight=None, l1_ratio=1.0, tol=0.0026886077958965947;, score=0.936 total time=   6.9s
[CV 2/3; 40/50] START C=0.3445110139330698, class_weight=None, l1_ratio=1.0, tol=0.0026886077958965947
[CV 2/3; 40/50] END C=0.3445110139330698, class_weight=None, l1_ratio=1.0, tol=0.0026886077958965947;, score=0.984 total time=   6.0s
[CV 3/3; 40/50] START C=0.3445110139330698, class_weight=None, l1_ratio=1.0, tol=0.0026886077958965947
[CV 3/3; 40/50] END C=0.3445110139330698, class_weight=None, l1_ratio=1.0, tol=0.0026886077958965947;, score=0.956 total time=   5.4s
[CV 1/3; 41/50] START C=0.0017551218517682708, class_weight=balanced, l1_ratio=0.5, tol=0.06780043768833548
[CV 1/3; 41/50] END C=0.0017551218517682708, class_weight=balanced, l1_ratio=0.5, tol=0.06780043768833548;, score=0.922 total time=   0.7s
[CV 2/3; 41/50] START C=0.0017551218517682708, class_weight=balanced, l1_ratio=0.5, tol=0.06780043768833548
[CV 2/3; 41/50] END C=0.0017551218517682708, class_weight=balanced, l1_ratio=0.5, tol=0.06780043768833548;, score=0.973 total time=   0.7s
[CV 3/3; 41/50] START C=0.0017551218517682708, class_weight=balanced, l1_ratio=0.5, tol=0.06780043768833548
[CV 3/3; 41/50] END C=0.0017551218517682708, class_weight=balanced, l1_ratio=0.5, tol=0.06780043768833548;, score=0.944 total time=   0.7s
[CV 1/3; 42/50] START C=0.021756143801527246, class_weight=None, l1_ratio=0.5, tol=0.006992740600712443
[CV 1/3; 42/50] END C=0.021756143801527246, class_weight=None, l1_ratio=0.5, tol=0.006992740600712443;, score=0.940 total time=   2.9s
[CV 2/3; 42/50] START C=0.021756143801527246, class_weight=None, l1_ratio=0.5, tol=0.006992740600712443
[CV 2/3; 42/50] END C=0.021756143801527246, class_weight=None, l1_ratio=0.5, tol=0.006992740600712443;, score=0.979 total time=   2.5s
[CV 3/3; 42/50] START C=0.021756143801527246, class_weight=None, l1_ratio=0.5, tol=0.006992740600712443
[CV 3/3; 42/50] END C=0.021756143801527246, class_weight=None, l1_ratio=0.5, tol=0.006992740600712443;, score=0.953 total time=   2.5s
[CV 1/3; 43/50] START C=0.0011802981774844698, class_weight=balanced, l1_ratio=1.0, tol=0.01191786839899373
[CV 1/3; 43/50] END C=0.0011802981774844698, class_weight=balanced, l1_ratio=1.0, tol=0.01191786839899373;, score=0.902 total time=   2.4s
[CV 2/3; 43/50] START C=0.0011802981774844698, class_weight=balanced, l1_ratio=1.0, tol=0.01191786839899373
[CV 2/3; 43/50] END C=0.0011802981774844698, class_weight=balanced, l1_ratio=1.0, tol=0.01191786839899373;, score=0.950 total time=   5.4s
[CV 3/3; 43/50] START C=0.0011802981774844698, class_weight=balanced, l1_ratio=1.0, tol=0.01191786839899373
[CV 3/3; 43/50] END C=0.0011802981774844698, class_weight=balanced, l1_ratio=1.0, tol=0.01191786839899373;, score=0.914 total time=   2.8s
[CV 1/3; 44/50] START C=0.15122050045589844, class_weight=None, l1_ratio=0.0, tol=0.020679327955553838
[CV 1/3; 44/50] END C=0.15122050045589844, class_weight=None, l1_ratio=0.0, tol=0.020679327955553838;, score=0.944 total time=   0.9s
[CV 2/3; 44/50] START C=0.15122050045589844, class_weight=None, l1_ratio=0.0, tol=0.020679327955553838
[CV 2/3; 44/50] END C=0.15122050045589844, class_weight=None, l1_ratio=0.0, tol=0.020679327955553838;, score=0.973 total time=   0.8s
[CV 3/3; 44/50] START C=0.15122050045589844, class_weight=None, l1_ratio=0.0, tol=0.020679327955553838
[CV 3/3; 44/50] END C=0.15122050045589844, class_weight=None, l1_ratio=0.0, tol=0.020679327955553838;, score=0.947 total time=   0.8s
[CV 1/3; 45/50] START C=0.04322753740649018, class_weight=None, l1_ratio=0.0, tol=0.09910299619565144
[CV 1/3; 45/50] END C=0.04322753740649018, class_weight=None, l1_ratio=0.0, tol=0.09910299619565144;, score=0.940 total time=   0.5s
[CV 2/3; 45/50] START C=0.04322753740649018, class_weight=None, l1_ratio=0.0, tol=0.09910299619565144
[CV 2/3; 45/50] END C=0.04322753740649018, class_weight=None, l1_ratio=0.0, tol=0.09910299619565144;, score=0.961 total time=   0.5s
[CV 3/3; 45/50] START C=0.04322753740649018, class_weight=None, l1_ratio=0.0, tol=0.09910299619565144
[CV 3/3; 45/50] END C=0.04322753740649018, class_weight=None, l1_ratio=0.0, tol=0.09910299619565144;, score=0.932 total time=   0.5s
[CV 1/3; 46/50] START C=0.007110983759744362, class_weight=balanced, l1_ratio=1.0, tol=0.014019686452307207
[CV 1/3; 46/50] END C=0.007110983759744362, class_weight=balanced, l1_ratio=1.0, tol=0.014019686452307207;, score=0.921 total time=   1.8s
[CV 2/3; 46/50] START C=0.007110983759744362, class_weight=balanced, l1_ratio=1.0, tol=0.014019686452307207
[CV 2/3; 46/50] END C=0.007110983759744362, class_weight=balanced, l1_ratio=1.0, tol=0.014019686452307207;, score=0.978 total time=   1.6s
[CV 3/3; 46/50] START C=0.007110983759744362, class_weight=balanced, l1_ratio=1.0, tol=0.014019686452307207
[CV 3/3; 46/50] END C=0.007110983759744362, class_weight=balanced, l1_ratio=1.0, tol=0.014019686452307207;, score=0.951 total time=   1.8s
[CV 1/3; 47/50] START C=0.015203053262728874, class_weight=None, l1_ratio=0.0, tol=0.036490493757176695
[CV 1/3; 47/50] END C=0.015203053262728874, class_weight=None, l1_ratio=0.0, tol=0.036490493757176695;, score=0.945 total time=   0.7s
[CV 2/3; 47/50] START C=0.015203053262728874, class_weight=None, l1_ratio=0.0, tol=0.036490493757176695
[CV 2/3; 47/50] END C=0.015203053262728874, class_weight=None, l1_ratio=0.0, tol=0.036490493757176695;, score=0.969 total time=   0.6s
[CV 3/3; 47/50] START C=0.015203053262728874, class_weight=None, l1_ratio=0.0, tol=0.036490493757176695
[CV 3/3; 47/50] END C=0.015203053262728874, class_weight=None, l1_ratio=0.0, tol=0.036490493757176695;, score=0.943 total time=   0.6s
[CV 1/3; 48/50] START C=0.0010181308266605698, class_weight=None, l1_ratio=0.0, tol=0.06535863069515857
[CV 1/3; 48/50] END C=0.0010181308266605698, class_weight=None, l1_ratio=0.0, tol=0.06535863069515857;, score=0.943 total time=   0.5s
[CV 2/3; 48/50] START C=0.0010181308266605698, class_weight=None, l1_ratio=0.0, tol=0.06535863069515857
[CV 2/3; 48/50] END C=0.0010181308266605698, class_weight=None, l1_ratio=0.0, tol=0.06535863069515857;, score=0.962 total time=   0.5s
[CV 3/3; 48/50] START C=0.0010181308266605698, class_weight=None, l1_ratio=0.0, tol=0.06535863069515857
[CV 3/3; 48/50] END C=0.0010181308266605698, class_weight=None, l1_ratio=0.0, tol=0.06535863069515857;, score=0.937 total time=   0.5s
[CV 1/3; 49/50] START C=0.4397620483932065, class_weight=None, l1_ratio=0.0, tol=0.0065699315647084885
[CV 1/3; 49/50] END C=0.4397620483932065, class_weight=None, l1_ratio=0.0, tol=0.0065699315647084885;, score=0.940 total time=   2.1s
[CV 2/3; 49/50] START C=0.4397620483932065, class_weight=None, l1_ratio=0.0, tol=0.0065699315647084885
[CV 2/3; 49/50] END C=0.4397620483932065, class_weight=None, l1_ratio=0.0, tol=0.0065699315647084885;, score=0.980 total time=   1.7s
[CV 3/3; 49/50] START C=0.4397620483932065, class_weight=None, l1_ratio=0.0, tol=0.0065699315647084885
[CV 3/3; 49/50] END C=0.4397620483932065, class_weight=None, l1_ratio=0.0, tol=0.0065699315647084885;, score=0.953 total time=   1.7s
[CV 1/3; 50/50] START C=0.6273328141050832, class_weight=balanced, l1_ratio=0.5, tol=0.015030561330720426
[CV 1/3; 50/50] END C=0.6273328141050832, class_weight=balanced, l1_ratio=0.5, tol=0.015030561330720426;, score=0.923 total time=   1.7s
[CV 2/3; 50/50] START C=0.6273328141050832, class_weight=balanced, l1_ratio=0.5, tol=0.015030561330720426
[CV 2/3; 50/50] END C=0.6273328141050832, class_weight=balanced, l1_ratio=0.5, tol=0.015030561330720426;, score=0.979 total time=   1.5s
[CV 3/3; 50/50] START C=0.6273328141050832, class_weight=balanced, l1_ratio=0.5, tol=0.015030561330720426
[CV 3/3; 50/50] END C=0.6273328141050832, class_weight=balanced, l1_ratio=0.5, tol=0.015030561330720426;, score=0.952 total time=   1.5s

--- TUNING FINISHED ---
Beste Parameter: {'C': np.float64(0.004223863922562596), 'class_weight': None, 'l1_ratio': 0.0, 'tol': np.float64(0.0010751674340096415)}
Bester CV-Score: 0.9588

--- EVALUATION AUF DEN TESTDATEN ---
Test Accuracy: 0.9052

Macro F1: 0.8694627789180688

--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9052

                     precision    recall  f1-score   support

             B cell       1.00      0.98      0.99       120
     CD14+ monocyte       0.99      1.00      0.99      2575
        CD4+ T cell       0.90      0.99      0.94      3910
   Cytotoxic T cell       0.88      0.63      0.73      1824
     Dendritic cell       1.00      0.40      0.57         5
      Megakaryocyte       1.00      1.00      1.00         7
Natural killer cell       0.72      0.80      0.75       791
        Plasma cell       1.00      0.94      0.97        49

           accuracy                           0.91      9281
          macro avg       0.94      0.84      0.87      9281
       weighted avg       0.91      0.91      0.90      9281

Random dropout accuracy score 0.8951
Total samples: 9281
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.9023
Feature importance dropout (0.5% features dropped) accuracy score 0.8757
Feature importance dropout (1.0% features dropped) accuracy score 0.8458
Feature importance dropout (2.0% features dropped) accuracy score 0.8057
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8533

                     precision    recall  f1-score   support

             B cell       1.00      0.97      0.99      3959
     CD14+ monocyte       0.66      1.00      0.80      3135
        CD4+ T cell       0.94      0.93      0.94     13664
   Cytotoxic T cell       0.73      0.65      0.68      4839
     Dendritic cell       0.98      0.44      0.61       529
      Megakaryocyte       1.00      0.73      0.85        86
Natural killer cell       0.71      0.56      0.63      2751
        Plasma cell       0.96      1.00      0.98        23

           accuracy                           0.85     28986
          macro avg       0.87      0.79      0.81     28986
       weighted avg       0.86      0.85      0.85     28986

Random dropout accuracy score 0.8188
Total samples: 28986
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.8442
Feature importance dropout (0.5% features dropped) accuracy score 0.8005
Feature importance dropout (1.0% features dropped) accuracy score 0.7363
Feature importance dropout (2.0% features dropped) accuracy score 0.6457
=== JOB_STATISTICS ===
=== current date     : Mon Jun 29 10:11:58 CEST 2026
= Job-ID             : 12000012 on woody
= Job-Name           : conditional_autoencoder_lr
= Job-Command        : /home/hpc/iwbn/iwbn133h/submit_conditional_autoencoder_lr_v1.sh
= Initial workdir    : /home/hpc/iwbn/iwbn133h
= Queue/Partition    : work
= Slurm account      : iwbn with QOS=normal
= Features           : icx
= Requested resources:  for 17:00:00
= Elapsed runtime    : 01:03:19
= Total RAM usage    : 20.9 GiB of requested  GiB (%)   
= Node list          : w2316
= Subm/Elig/Start/End: 2026-06-29T09:08:38 / 2026-06-29T09:08:38 / 2026-06-29T09:08:39 / 2026-06-29T10:11:58
======================
=== Quota infos ======
    Path                 Used     SoftQ    HardQ    Gracetime  Filec    FileQ    FiHaQ    FileGrace    
    /home/woody           982.1M  1000.0G  1500.0G        N/A  29,019    5,000K   7,500K        N/A    
    /home/hpc              86.2G   104.9G   209.7G        N/A     139K     500K   1,000K        N/A    
    /home/vault             0.0K  1048.6G  2097.2G        N/A       1      200K     400K        N/A    
