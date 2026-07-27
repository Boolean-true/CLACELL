### Starting TaskPrologue of job 11995954 on w2519 at Sat Jun 27 16:18:17 CEST 2026
#   SLURM_JOB_NODELIST=w2519
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
Epoch [10/150], Loss: 0.9055
Epoch [20/150], Loss: 0.8918
Epoch [30/150], Loss: 0.8839
Epoch [40/150], Loss: 0.8787
Epoch [50/150], Loss: 0.8751
Epoch [60/150], Loss: 0.8726
Epoch [70/150], Loss: 0.8704
Epoch [80/150], Loss: 0.8682
Epoch [90/150], Loss: 0.8677
Epoch [100/150], Loss: 0.8654
Early Stopping after [106/150] Epochs!

Extract robust features...
Starte automatische Hyperparametersuche auf dem Latent Space...
Fitting 3 folds for each of 50 candidates, totalling 150 fits
[CV 1/3; 1/50] START C=0.01953172425882642, class_weight=None, l1_ratio=1.0, tol=0.09588739054016986
[CV 1/3; 1/50] END C=0.01953172425882642, class_weight=None, l1_ratio=1.0, tol=0.09588739054016986;, score=0.908 total time=   0.5s
[CV 2/3; 1/50] START C=0.01953172425882642, class_weight=None, l1_ratio=1.0, tol=0.09588739054016986
[CV 2/3; 1/50] END C=0.01953172425882642, class_weight=None, l1_ratio=1.0, tol=0.09588739054016986;, score=0.971 total time=   0.5s
[CV 3/3; 1/50] START C=0.01953172425882642, class_weight=None, l1_ratio=1.0, tol=0.09588739054016986
[CV 3/3; 1/50] END C=0.01953172425882642, class_weight=None, l1_ratio=1.0, tol=0.09588739054016986;, score=0.939 total time=   0.5s
[CV 1/3; 2/50] START C=0.04451624615387537, class_weight=None, l1_ratio=0.0, tol=0.07984012468384667
[CV 1/3; 2/50] END C=0.04451624615387537, class_weight=None, l1_ratio=0.0, tol=0.07984012468384667;, score=0.930 total time=   0.5s
[CV 2/3; 2/50] START C=0.04451624615387537, class_weight=None, l1_ratio=0.0, tol=0.07984012468384667
[CV 2/3; 2/50] END C=0.04451624615387537, class_weight=None, l1_ratio=0.0, tol=0.07984012468384667;, score=0.986 total time=   0.5s
[CV 3/3; 2/50] START C=0.04451624615387537, class_weight=None, l1_ratio=0.0, tol=0.07984012468384667
[CV 3/3; 2/50] END C=0.04451624615387537, class_weight=None, l1_ratio=0.0, tol=0.07984012468384667;, score=0.956 total time=   0.5s
[CV 1/3; 3/50] START C=0.2768253945864596, class_weight=None, l1_ratio=0.75, tol=0.01128584779291734
[CV 1/3; 3/50] END C=0.2768253945864596, class_weight=None, l1_ratio=0.75, tol=0.01128584779291734;, score=0.854 total time=   2.1s
[CV 2/3; 3/50] START C=0.2768253945864596, class_weight=None, l1_ratio=0.75, tol=0.01128584779291734
[CV 2/3; 3/50] END C=0.2768253945864596, class_weight=None, l1_ratio=0.75, tol=0.01128584779291734;, score=0.990 total time=   1.7s
[CV 3/3; 3/50] START C=0.2768253945864596, class_weight=None, l1_ratio=0.75, tol=0.01128584779291734
[CV 3/3; 3/50] END C=0.2768253945864596, class_weight=None, l1_ratio=0.75, tol=0.01128584779291734;, score=0.962 total time=   1.9s
[CV 1/3; 4/50] START C=0.11211477154519704, class_weight=balanced, l1_ratio=0.75, tol=0.002106547670003569
[CV 1/3; 4/50] END C=0.11211477154519704, class_weight=balanced, l1_ratio=0.75, tol=0.002106547670003569;, score=0.637 total time=   7.4s
[CV 2/3; 4/50] START C=0.11211477154519704, class_weight=balanced, l1_ratio=0.75, tol=0.002106547670003569
[CV 2/3; 4/50] END C=0.11211477154519704, class_weight=balanced, l1_ratio=0.75, tol=0.002106547670003569;, score=0.990 total time=  10.5s
[CV 3/3; 4/50] START C=0.11211477154519704, class_weight=balanced, l1_ratio=0.75, tol=0.002106547670003569
[CV 3/3; 4/50] END C=0.11211477154519704, class_weight=balanced, l1_ratio=0.75, tol=0.002106547670003569;, score=0.954 total time=   8.0s
[CV 1/3; 5/50] START C=0.009699159198900643, class_weight=None, l1_ratio=1.0, tol=0.02499932020892508
[CV 1/3; 5/50] END C=0.009699159198900643, class_weight=None, l1_ratio=1.0, tol=0.02499932020892508;, score=0.896 total time=   1.1s
[CV 2/3; 5/50] START C=0.009699159198900643, class_weight=None, l1_ratio=1.0, tol=0.02499932020892508
[CV 2/3; 5/50] END C=0.009699159198900643, class_weight=None, l1_ratio=1.0, tol=0.02499932020892508;, score=0.957 total time=   1.1s
[CV 3/3; 5/50] START C=0.009699159198900643, class_weight=None, l1_ratio=1.0, tol=0.02499932020892508
[CV 3/3; 5/50] END C=0.009699159198900643, class_weight=None, l1_ratio=1.0, tol=0.02499932020892508;, score=0.921 total time=   1.0s
[CV 1/3; 6/50] START C=0.0068080592149730845, class_weight=balanced, l1_ratio=0.0, tol=0.014856201913103627
[CV 1/3; 6/50] END C=0.0068080592149730845, class_weight=balanced, l1_ratio=0.0, tol=0.014856201913103627;, score=0.822 total time=   2.9s
[CV 2/3; 6/50] START C=0.0068080592149730845, class_weight=balanced, l1_ratio=0.0, tol=0.014856201913103627
[CV 2/3; 6/50] END C=0.0068080592149730845, class_weight=balanced, l1_ratio=0.0, tol=0.014856201913103627;, score=0.990 total time=   1.0s
[CV 3/3; 6/50] START C=0.0068080592149730845, class_weight=balanced, l1_ratio=0.0, tol=0.014856201913103627
[CV 3/3; 6/50] END C=0.0068080592149730845, class_weight=balanced, l1_ratio=0.0, tol=0.014856201913103627;, score=0.951 total time=   1.2s
[CV 1/3; 7/50] START C=0.09677011704505789, class_weight=balanced, l1_ratio=0.75, tol=0.026440860455575768
[CV 1/3; 7/50] END C=0.09677011704505789, class_weight=balanced, l1_ratio=0.75, tol=0.026440860455575768;, score=0.693 total time=   0.9s
[CV 2/3; 7/50] START C=0.09677011704505789, class_weight=balanced, l1_ratio=0.75, tol=0.026440860455575768
[CV 2/3; 7/50] END C=0.09677011704505789, class_weight=balanced, l1_ratio=0.75, tol=0.026440860455575768;, score=0.990 total time=   1.1s
[CV 3/3; 7/50] START C=0.09677011704505789, class_weight=balanced, l1_ratio=0.75, tol=0.026440860455575768
[CV 3/3; 7/50] END C=0.09677011704505789, class_weight=balanced, l1_ratio=0.75, tol=0.026440860455575768;, score=0.954 total time=   1.0s
[CV 1/3; 8/50] START C=0.4535947004931655, class_weight=balanced, l1_ratio=0.5, tol=0.00969363714910667
[CV 1/3; 8/50] END C=0.4535947004931655, class_weight=balanced, l1_ratio=0.5, tol=0.00969363714910667;, score=0.757 total time=   1.1s
[CV 2/3; 8/50] START C=0.4535947004931655, class_weight=balanced, l1_ratio=0.5, tol=0.00969363714910667
[CV 2/3; 8/50] END C=0.4535947004931655, class_weight=balanced, l1_ratio=0.5, tol=0.00969363714910667;, score=0.990 total time=   1.3s
[CV 3/3; 8/50] START C=0.4535947004931655, class_weight=balanced, l1_ratio=0.5, tol=0.00969363714910667
[CV 3/3; 8/50] END C=0.4535947004931655, class_weight=balanced, l1_ratio=0.5, tol=0.00969363714910667;, score=0.955 total time=   1.2s
[CV 1/3; 9/50] START C=0.08490004744741898, class_weight=None, l1_ratio=0.75, tol=0.039606845789421474
[CV 1/3; 9/50] END C=0.08490004744741898, class_weight=None, l1_ratio=0.75, tol=0.039606845789421474;, score=0.903 total time=   0.9s
[CV 2/3; 9/50] START C=0.08490004744741898, class_weight=None, l1_ratio=0.75, tol=0.039606845789421474
[CV 2/3; 9/50] END C=0.08490004744741898, class_weight=None, l1_ratio=0.75, tol=0.039606845789421474;, score=0.986 total time=   0.7s
[CV 3/3; 9/50] START C=0.08490004744741898, class_weight=None, l1_ratio=0.75, tol=0.039606845789421474
[CV 3/3; 9/50] END C=0.08490004744741898, class_weight=None, l1_ratio=0.75, tol=0.039606845789421474;, score=0.957 total time=   0.8s
[CV 1/3; 10/50] START C=0.4521641955208261, class_weight=balanced, l1_ratio=0.75, tol=0.005036099079189309
[CV 1/3; 10/50] END C=0.4521641955208261, class_weight=balanced, l1_ratio=0.75, tol=0.005036099079189309;, score=0.747 total time=   1.9s
[CV 2/3; 10/50] START C=0.4521641955208261, class_weight=balanced, l1_ratio=0.75, tol=0.005036099079189309
[CV 2/3; 10/50] END C=0.4521641955208261, class_weight=balanced, l1_ratio=0.75, tol=0.005036099079189309;, score=0.990 total time=   1.3s
[CV 3/3; 10/50] START C=0.4521641955208261, class_weight=balanced, l1_ratio=0.75, tol=0.005036099079189309
[CV 3/3; 10/50] END C=0.4521641955208261, class_weight=balanced, l1_ratio=0.75, tol=0.005036099079189309;, score=0.955 total time=   1.7s
[CV 1/3; 11/50] START C=0.24180267505506914, class_weight=None, l1_ratio=0.25, tol=0.05508029184879069
[CV 1/3; 11/50] END C=0.24180267505506914, class_weight=None, l1_ratio=0.25, tol=0.05508029184879069;, score=0.927 total time=   0.6s
[CV 2/3; 11/50] START C=0.24180267505506914, class_weight=None, l1_ratio=0.25, tol=0.05508029184879069
[CV 2/3; 11/50] END C=0.24180267505506914, class_weight=None, l1_ratio=0.25, tol=0.05508029184879069;, score=0.987 total time=   0.7s
[CV 3/3; 11/50] START C=0.24180267505506914, class_weight=None, l1_ratio=0.25, tol=0.05508029184879069
[CV 3/3; 11/50] END C=0.24180267505506914, class_weight=None, l1_ratio=0.25, tol=0.05508029184879069;, score=0.957 total time=   0.6s
[CV 1/3; 12/50] START C=1.1504429559745393, class_weight=None, l1_ratio=0.5, tol=0.001522644132073902
[CV 1/3; 12/50] END C=1.1504429559745393, class_weight=None, l1_ratio=0.5, tol=0.001522644132073902;, score=0.748 total time=  12.6s
[CV 2/3; 12/50] START C=1.1504429559745393, class_weight=None, l1_ratio=0.5, tol=0.001522644132073902
[CV 2/3; 12/50] END C=1.1504429559745393, class_weight=None, l1_ratio=0.5, tol=0.001522644132073902;, score=0.991 total time=  17.2s
[CV 3/3; 12/50] START C=1.1504429559745393, class_weight=None, l1_ratio=0.5, tol=0.001522644132073902
[CV 3/3; 12/50] END C=1.1504429559745393, class_weight=None, l1_ratio=0.5, tol=0.001522644132073902;, score=0.965 total time=  20.9s
[CV 1/3; 13/50] START C=0.14629547015049546, class_weight=balanced, l1_ratio=1.0, tol=0.013998547755633544
[CV 1/3; 13/50] END C=0.14629547015049546, class_weight=balanced, l1_ratio=1.0, tol=0.013998547755633544;, score=0.759 total time=   1.1s
[CV 2/3; 13/50] START C=0.14629547015049546, class_weight=balanced, l1_ratio=1.0, tol=0.013998547755633544
[CV 2/3; 13/50] END C=0.14629547015049546, class_weight=balanced, l1_ratio=1.0, tol=0.013998547755633544;, score=0.991 total time=   1.1s
[CV 3/3; 13/50] START C=0.14629547015049546, class_weight=balanced, l1_ratio=1.0, tol=0.013998547755633544
[CV 3/3; 13/50] END C=0.14629547015049546, class_weight=balanced, l1_ratio=1.0, tol=0.013998547755633544;, score=0.955 total time=   1.1s
[CV 1/3; 14/50] START C=0.9001400099457124, class_weight=None, l1_ratio=0.75, tol=0.001976006552529455
[CV 1/3; 14/50] END C=0.9001400099457124, class_weight=None, l1_ratio=0.75, tol=0.001976006552529455;, score=0.769 total time=   7.8s
[CV 2/3; 14/50] START C=0.9001400099457124, class_weight=None, l1_ratio=0.75, tol=0.001976006552529455
[CV 2/3; 14/50] END C=0.9001400099457124, class_weight=None, l1_ratio=0.75, tol=0.001976006552529455;, score=0.991 total time=  11.2s
[CV 3/3; 14/50] START C=0.9001400099457124, class_weight=None, l1_ratio=0.75, tol=0.001976006552529455
[CV 3/3; 14/50] END C=0.9001400099457124, class_weight=None, l1_ratio=0.75, tol=0.001976006552529455;, score=0.965 total time=  13.4s
[CV 1/3; 15/50] START C=0.009435639067438608, class_weight=balanced, l1_ratio=1.0, tol=0.019285542763560818
[CV 1/3; 15/50] END C=0.009435639067438608, class_weight=balanced, l1_ratio=1.0, tol=0.019285542763560818;, score=0.610 total time=  13.7s
[CV 2/3; 15/50] START C=0.009435639067438608, class_weight=balanced, l1_ratio=1.0, tol=0.019285542763560818
[CV 2/3; 15/50] END C=0.009435639067438608, class_weight=balanced, l1_ratio=1.0, tol=0.019285542763560818;, score=0.978 total time=  58.9s
[CV 3/3; 15/50] START C=0.009435639067438608, class_weight=balanced, l1_ratio=1.0, tol=0.019285542763560818
[CV 3/3; 15/50] END C=0.009435639067438608, class_weight=balanced, l1_ratio=1.0, tol=0.019285542763560818;, score=0.938 total time=  58.8s
[CV 1/3; 16/50] START C=0.009401825955658224, class_weight=None, l1_ratio=0.75, tol=0.010182232199630692
[CV 1/3; 16/50] END C=0.009401825955658224, class_weight=None, l1_ratio=0.75, tol=0.010182232199630692;, score=0.894 total time=   1.7s
[CV 2/3; 16/50] START C=0.009401825955658224, class_weight=None, l1_ratio=0.75, tol=0.010182232199630692
[CV 2/3; 16/50] END C=0.009401825955658224, class_weight=None, l1_ratio=0.75, tol=0.010182232199630692;, score=0.962 total time=   1.6s
[CV 3/3; 16/50] START C=0.009401825955658224, class_weight=None, l1_ratio=0.75, tol=0.010182232199630692
[CV 3/3; 16/50] END C=0.009401825955658224, class_weight=None, l1_ratio=0.75, tol=0.010182232199630692;, score=0.926 total time=   1.7s
[CV 1/3; 17/50] START C=0.012777927848353979, class_weight=None, l1_ratio=0.75, tol=0.0012393749466745672
[CV 1/3; 17/50] END C=0.012777927848353979, class_weight=None, l1_ratio=0.75, tol=0.0012393749466745672;, score=0.882 total time=   6.3s
[CV 2/3; 17/50] START C=0.012777927848353979, class_weight=None, l1_ratio=0.75, tol=0.0012393749466745672
[CV 2/3; 17/50] END C=0.012777927848353979, class_weight=None, l1_ratio=0.75, tol=0.0012393749466745672;, score=0.971 total time=   6.1s
[CV 3/3; 17/50] START C=0.012777927848353979, class_weight=None, l1_ratio=0.75, tol=0.0012393749466745672
[CV 3/3; 17/50] END C=0.012777927848353979, class_weight=None, l1_ratio=0.75, tol=0.0012393749466745672;, score=0.934 total time=   5.9s
[CV 1/3; 18/50] START C=0.006120745361841037, class_weight=balanced, l1_ratio=0.0, tol=0.03879265684782511
[CV 1/3; 18/50] END C=0.006120745361841037, class_weight=balanced, l1_ratio=0.0, tol=0.03879265684782511;, score=0.803 total time=   2.8s
[CV 2/3; 18/50] START C=0.006120745361841037, class_weight=balanced, l1_ratio=0.0, tol=0.03879265684782511
[CV 2/3; 18/50] END C=0.006120745361841037, class_weight=balanced, l1_ratio=0.0, tol=0.03879265684782511;, score=0.990 total time=   3.1s
[CV 3/3; 18/50] START C=0.006120745361841037, class_weight=balanced, l1_ratio=0.0, tol=0.03879265684782511
[CV 3/3; 18/50] END C=0.006120745361841037, class_weight=balanced, l1_ratio=0.0, tol=0.03879265684782511;, score=0.951 total time=   0.9s
[CV 1/3; 19/50] START C=0.01383942847981824, class_weight=None, l1_ratio=0.5, tol=0.04322010603182397
[CV 1/3; 19/50] END C=0.01383942847981824, class_weight=None, l1_ratio=0.5, tol=0.04322010603182397;, score=0.912 total time=   0.8s
[CV 2/3; 19/50] START C=0.01383942847981824, class_weight=None, l1_ratio=0.5, tol=0.04322010603182397
[CV 2/3; 19/50] END C=0.01383942847981824, class_weight=None, l1_ratio=0.5, tol=0.04322010603182397;, score=0.975 total time=   0.7s
[CV 3/3; 19/50] START C=0.01383942847981824, class_weight=None, l1_ratio=0.5, tol=0.04322010603182397
[CV 3/3; 19/50] END C=0.01383942847981824, class_weight=None, l1_ratio=0.5, tol=0.04322010603182397;, score=0.944 total time=   0.8s
[CV 1/3; 20/50] START C=0.002079749897230386, class_weight=None, l1_ratio=1.0, tol=0.0010400127089929706
[CV 1/3; 20/50] END C=0.002079749897230386, class_weight=None, l1_ratio=1.0, tol=0.0010400127089929706;, score=0.810 total time=   2.7s
[CV 2/3; 20/50] START C=0.002079749897230386, class_weight=None, l1_ratio=1.0, tol=0.0010400127089929706
[CV 2/3; 20/50] END C=0.002079749897230386, class_weight=None, l1_ratio=1.0, tol=0.0010400127089929706;, score=0.895 total time=   2.8s
[CV 3/3; 20/50] START C=0.002079749897230386, class_weight=None, l1_ratio=1.0, tol=0.0010400127089929706
[CV 3/3; 20/50] END C=0.002079749897230386, class_weight=None, l1_ratio=1.0, tol=0.0010400127089929706;, score=0.851 total time=   2.7s
[CV 1/3; 21/50] START C=0.00181536000941734, class_weight=None, l1_ratio=0.5, tol=0.0010762701527984335
[CV 1/3; 21/50] END C=0.00181536000941734, class_weight=None, l1_ratio=0.5, tol=0.0010762701527984335;, score=0.833 total time=   2.5s
[CV 2/3; 21/50] START C=0.00181536000941734, class_weight=None, l1_ratio=0.5, tol=0.0010762701527984335
[CV 2/3; 21/50] END C=0.00181536000941734, class_weight=None, l1_ratio=0.5, tol=0.0010762701527984335;, score=0.904 total time=   2.4s
[CV 3/3; 21/50] START C=0.00181536000941734, class_weight=None, l1_ratio=0.5, tol=0.0010762701527984335
[CV 3/3; 21/50] END C=0.00181536000941734, class_weight=None, l1_ratio=0.5, tol=0.0010762701527984335;, score=0.863 total time=   2.5s
[CV 1/3; 22/50] START C=0.05593404322485223, class_weight=None, l1_ratio=0.75, tol=0.003430758771985927
[CV 1/3; 22/50] END C=0.05593404322485223, class_weight=None, l1_ratio=0.75, tol=0.003430758771985927;, score=0.808 total time=   4.1s
[CV 2/3; 22/50] START C=0.05593404322485223, class_weight=None, l1_ratio=0.75, tol=0.003430758771985927
[CV 2/3; 22/50] END C=0.05593404322485223, class_weight=None, l1_ratio=0.75, tol=0.003430758771985927;, score=0.987 total time=   5.3s
[CV 3/3; 22/50] START C=0.05593404322485223, class_weight=None, l1_ratio=0.75, tol=0.003430758771985927
[CV 3/3; 22/50] END C=0.05593404322485223, class_weight=None, l1_ratio=0.75, tol=0.003430758771985927;, score=0.952 total time=   5.3s
[CV 1/3; 23/50] START C=0.030425967982785938, class_weight=balanced, l1_ratio=1.0, tol=0.08789901794659519
[CV 1/3; 23/50] END C=0.030425967982785938, class_weight=balanced, l1_ratio=1.0, tol=0.08789901794659519;, score=0.676 total time=   0.7s
[CV 2/3; 23/50] START C=0.030425967982785938, class_weight=balanced, l1_ratio=1.0, tol=0.08789901794659519
[CV 2/3; 23/50] END C=0.030425967982785938, class_weight=balanced, l1_ratio=1.0, tol=0.08789901794659519;, score=0.985 total time=   0.6s
[CV 3/3; 23/50] START C=0.030425967982785938, class_weight=balanced, l1_ratio=1.0, tol=0.08789901794659519
[CV 3/3; 23/50] END C=0.030425967982785938, class_weight=balanced, l1_ratio=1.0, tol=0.08789901794659519;, score=0.941 total time=   1.0s
[CV 1/3; 24/50] START C=0.009442742673349235, class_weight=balanced, l1_ratio=0.75, tol=0.0019908957392944277
[CV 1/3; 24/50] END C=0.009442742673349235, class_weight=balanced, l1_ratio=0.75, tol=0.0019908957392944277;, score=0.632 total time=  59.3s
[CV 2/3; 24/50] START C=0.009442742673349235, class_weight=balanced, l1_ratio=0.75, tol=0.0019908957392944277
[CV 2/3; 24/50] END C=0.009442742673349235, class_weight=balanced, l1_ratio=0.75, tol=0.0019908957392944277;, score=0.983 total time=  59.1s
[CV 3/3; 24/50] START C=0.009442742673349235, class_weight=balanced, l1_ratio=0.75, tol=0.0019908957392944277
[CV 3/3; 24/50] END C=0.009442742673349235, class_weight=balanced, l1_ratio=0.75, tol=0.0019908957392944277;, score=0.944 total time=  59.2s
[CV 1/3; 25/50] START C=0.4739384717771735, class_weight=None, l1_ratio=1.0, tol=0.003908023140408751
[CV 1/3; 25/50] END C=0.4739384717771735, class_weight=None, l1_ratio=1.0, tol=0.003908023140408751;, score=0.773 total time=   5.9s
[CV 2/3; 25/50] START C=0.4739384717771735, class_weight=None, l1_ratio=1.0, tol=0.003908023140408751
[CV 2/3; 25/50] END C=0.4739384717771735, class_weight=None, l1_ratio=1.0, tol=0.003908023140408751;, score=0.991 total time=   5.7s
[CV 3/3; 25/50] START C=0.4739384717771735, class_weight=None, l1_ratio=1.0, tol=0.003908023140408751
[CV 3/3; 25/50] END C=0.4739384717771735, class_weight=None, l1_ratio=1.0, tol=0.003908023140408751;, score=0.962 total time=   5.5s
[CV 1/3; 26/50] START C=1.1016582333850946, class_weight=balanced, l1_ratio=0.75, tol=0.004878823086449528
[CV 1/3; 26/50] END C=1.1016582333850946, class_weight=balanced, l1_ratio=0.75, tol=0.004878823086449528;, score=0.792 total time=   1.5s
[CV 2/3; 26/50] START C=1.1016582333850946, class_weight=balanced, l1_ratio=0.75, tol=0.004878823086449528
[CV 2/3; 26/50] END C=1.1016582333850946, class_weight=balanced, l1_ratio=0.75, tol=0.004878823086449528;, score=0.991 total time=   1.6s
[CV 3/3; 26/50] START C=1.1016582333850946, class_weight=balanced, l1_ratio=0.75, tol=0.004878823086449528
[CV 3/3; 26/50] END C=1.1016582333850946, class_weight=balanced, l1_ratio=0.75, tol=0.004878823086449528;, score=0.956 total time=   1.6s
[CV 1/3; 27/50] START C=0.006106072941784858, class_weight=balanced, l1_ratio=0.25, tol=0.0027907793454763547
[CV 1/3; 27/50] END C=0.006106072941784858, class_weight=balanced, l1_ratio=0.25, tol=0.0027907793454763547;, score=0.750 total time= 1.0min
[CV 2/3; 27/50] START C=0.006106072941784858, class_weight=balanced, l1_ratio=0.25, tol=0.0027907793454763547
[CV 2/3; 27/50] END C=0.006106072941784858, class_weight=balanced, l1_ratio=0.25, tol=0.0027907793454763547;, score=0.986 total time= 1.0min
[CV 3/3; 27/50] START C=0.006106072941784858, class_weight=balanced, l1_ratio=0.25, tol=0.0027907793454763547
[CV 3/3; 27/50] END C=0.006106072941784858, class_weight=balanced, l1_ratio=0.25, tol=0.0027907793454763547;, score=0.947 total time=  23.4s
[CV 1/3; 28/50] START C=0.3665682409386545, class_weight=None, l1_ratio=0.5, tol=0.09013945007365622
[CV 1/3; 28/50] END C=0.3665682409386545, class_weight=None, l1_ratio=0.5, tol=0.09013945007365622;, score=0.931 total time=   0.5s
[CV 2/3; 28/50] START C=0.3665682409386545, class_weight=None, l1_ratio=0.5, tol=0.09013945007365622
[CV 2/3; 28/50] END C=0.3665682409386545, class_weight=None, l1_ratio=0.5, tol=0.09013945007365622;, score=0.986 total time=   0.5s
[CV 3/3; 28/50] START C=0.3665682409386545, class_weight=None, l1_ratio=0.5, tol=0.09013945007365622
[CV 3/3; 28/50] END C=0.3665682409386545, class_weight=None, l1_ratio=0.5, tol=0.09013945007365622;, score=0.955 total time=   0.6s
[CV 1/3; 29/50] START C=0.009182377257382905, class_weight=balanced, l1_ratio=1.0, tol=0.010689630310524615
[CV 1/3; 29/50] END C=0.009182377257382905, class_weight=balanced, l1_ratio=1.0, tol=0.010689630310524615;, score=0.608 total time=  59.1s
[CV 2/3; 29/50] START C=0.009182377257382905, class_weight=balanced, l1_ratio=1.0, tol=0.010689630310524615
[CV 2/3; 29/50] END C=0.009182377257382905, class_weight=balanced, l1_ratio=1.0, tol=0.010689630310524615;, score=0.972 total time=  59.1s
[CV 3/3; 29/50] START C=0.009182377257382905, class_weight=balanced, l1_ratio=1.0, tol=0.010689630310524615
[CV 3/3; 29/50] END C=0.009182377257382905, class_weight=balanced, l1_ratio=1.0, tol=0.010689630310524615;, score=0.943 total time=  58.9s
[CV 1/3; 30/50] START C=0.06288298398113464, class_weight=balanced, l1_ratio=1.0, tol=0.0019618792772858615
[CV 1/3; 30/50] END C=0.06288298398113464, class_weight=balanced, l1_ratio=1.0, tol=0.0019618792772858615;, score=0.604 total time=   8.8s
[CV 2/3; 30/50] START C=0.06288298398113464, class_weight=balanced, l1_ratio=1.0, tol=0.0019618792772858615
[CV 2/3; 30/50] END C=0.06288298398113464, class_weight=balanced, l1_ratio=1.0, tol=0.0019618792772858615;, score=0.989 total time=  11.2s
[CV 3/3; 30/50] START C=0.06288298398113464, class_weight=balanced, l1_ratio=1.0, tol=0.0019618792772858615
[CV 3/3; 30/50] END C=0.06288298398113464, class_weight=balanced, l1_ratio=1.0, tol=0.0019618792772858615;, score=0.950 total time=   9.8s
[CV 1/3; 31/50] START C=0.16611335025305668, class_weight=None, l1_ratio=0.25, tol=0.023885115767979304
[CV 1/3; 31/50] END C=0.16611335025305668, class_weight=None, l1_ratio=0.25, tol=0.023885115767979304;, score=0.899 total time=   1.1s
[CV 2/3; 31/50] START C=0.16611335025305668, class_weight=None, l1_ratio=0.25, tol=0.023885115767979304
[CV 2/3; 31/50] END C=0.16611335025305668, class_weight=None, l1_ratio=0.25, tol=0.023885115767979304;, score=0.988 total time=   1.0s
[CV 3/3; 31/50] START C=0.16611335025305668, class_weight=None, l1_ratio=0.25, tol=0.023885115767979304
[CV 3/3; 31/50] END C=0.16611335025305668, class_weight=None, l1_ratio=0.25, tol=0.023885115767979304;, score=0.959 total time=   1.0s
[CV 1/3; 32/50] START C=0.006013786455333925, class_weight=balanced, l1_ratio=0.75, tol=0.001513327132023436
[CV 1/3; 32/50] END C=0.006013786455333925, class_weight=balanced, l1_ratio=0.75, tol=0.001513327132023436;, score=0.631 total time=  59.1s
[CV 2/3; 32/50] START C=0.006013786455333925, class_weight=balanced, l1_ratio=0.75, tol=0.001513327132023436
[CV 2/3; 32/50] END C=0.006013786455333925, class_weight=balanced, l1_ratio=0.75, tol=0.001513327132023436;, score=0.978 total time=  59.3s
[CV 3/3; 32/50] START C=0.006013786455333925, class_weight=balanced, l1_ratio=0.75, tol=0.001513327132023436
[CV 3/3; 32/50] END C=0.006013786455333925, class_weight=balanced, l1_ratio=0.75, tol=0.001513327132023436;, score=0.937 total time=  59.4s
[CV 1/3; 33/50] START C=0.0023221106665016885, class_weight=None, l1_ratio=0.75, tol=0.00834589646487771
[CV 1/3; 33/50] END C=0.0023221106665016885, class_weight=None, l1_ratio=0.75, tol=0.00834589646487771;, score=0.838 total time=   1.6s
[CV 2/3; 33/50] START C=0.0023221106665016885, class_weight=None, l1_ratio=0.75, tol=0.00834589646487771
[CV 2/3; 33/50] END C=0.0023221106665016885, class_weight=None, l1_ratio=0.75, tol=0.00834589646487771;, score=0.901 total time=   1.6s
[CV 3/3; 33/50] START C=0.0023221106665016885, class_weight=None, l1_ratio=0.75, tol=0.00834589646487771
[CV 3/3; 33/50] END C=0.0023221106665016885, class_weight=None, l1_ratio=0.75, tol=0.00834589646487771;, score=0.861 total time=   1.7s
[CV 1/3; 34/50] START C=0.023853184601797684, class_weight=balanced, l1_ratio=0.25, tol=0.014609965042030113
[CV 1/3; 34/50] END C=0.023853184601797684, class_weight=balanced, l1_ratio=0.25, tol=0.014609965042030113;, score=0.725 total time=   6.6s
[CV 2/3; 34/50] START C=0.023853184601797684, class_weight=balanced, l1_ratio=0.25, tol=0.014609965042030113
[CV 2/3; 34/50] END C=0.023853184601797684, class_weight=balanced, l1_ratio=0.25, tol=0.014609965042030113;, score=0.990 total time=   7.9s
[CV 3/3; 34/50] START C=0.023853184601797684, class_weight=balanced, l1_ratio=0.25, tol=0.014609965042030113
[CV 3/3; 34/50] END C=0.023853184601797684, class_weight=balanced, l1_ratio=0.25, tol=0.014609965042030113;, score=0.952 total time=   2.1s
[CV 1/3; 35/50] START C=0.011233431717731494, class_weight=balanced, l1_ratio=0.75, tol=0.07872258954261567
[CV 1/3; 35/50] END C=0.011233431717731494, class_weight=balanced, l1_ratio=0.75, tol=0.07872258954261567;, score=0.684 total time=   0.9s
[CV 2/3; 35/50] START C=0.011233431717731494, class_weight=balanced, l1_ratio=0.75, tol=0.07872258954261567
[CV 2/3; 35/50] END C=0.011233431717731494, class_weight=balanced, l1_ratio=0.75, tol=0.07872258954261567;, score=0.983 total time=   1.0s
[CV 3/3; 35/50] START C=0.011233431717731494, class_weight=balanced, l1_ratio=0.75, tol=0.07872258954261567
[CV 3/3; 35/50] END C=0.011233431717731494, class_weight=balanced, l1_ratio=0.75, tol=0.07872258954261567;, score=0.943 total time=   1.5s
[CV 1/3; 36/50] START C=1.4044688682612798, class_weight=balanced, l1_ratio=0.75, tol=0.052469672659489854
[CV 1/3; 36/50] END C=1.4044688682612798, class_weight=balanced, l1_ratio=0.75, tol=0.052469672659489854;, score=0.828 total time=   0.8s
[CV 2/3; 36/50] START C=1.4044688682612798, class_weight=balanced, l1_ratio=0.75, tol=0.052469672659489854
[CV 2/3; 36/50] END C=1.4044688682612798, class_weight=balanced, l1_ratio=0.75, tol=0.052469672659489854;, score=0.989 total time=   0.8s
[CV 3/3; 36/50] START C=1.4044688682612798, class_weight=balanced, l1_ratio=0.75, tol=0.052469672659489854
[CV 3/3; 36/50] END C=1.4044688682612798, class_weight=balanced, l1_ratio=0.75, tol=0.052469672659489854;, score=0.955 total time=   0.6s
[CV 1/3; 37/50] START C=0.17524608592251062, class_weight=None, l1_ratio=0.5, tol=0.038808558310148775
[CV 1/3; 37/50] END C=0.17524608592251062, class_weight=None, l1_ratio=0.5, tol=0.038808558310148775;, score=0.911 total time=   0.9s
[CV 2/3; 37/50] START C=0.17524608592251062, class_weight=None, l1_ratio=0.5, tol=0.038808558310148775
[CV 2/3; 37/50] END C=0.17524608592251062, class_weight=None, l1_ratio=0.5, tol=0.038808558310148775;, score=0.987 total time=   0.8s
[CV 3/3; 37/50] START C=0.17524608592251062, class_weight=None, l1_ratio=0.5, tol=0.038808558310148775
[CV 3/3; 37/50] END C=0.17524608592251062, class_weight=None, l1_ratio=0.5, tol=0.038808558310148775;, score=0.958 total time=   0.7s
[CV 1/3; 38/50] START C=0.008494605751462514, class_weight=balanced, l1_ratio=0.25, tol=0.04282130065978013
[CV 1/3; 38/50] END C=0.008494605751462514, class_weight=balanced, l1_ratio=0.25, tol=0.04282130065978013;, score=0.739 total time=   4.6s
[CV 2/3; 38/50] START C=0.008494605751462514, class_weight=balanced, l1_ratio=0.25, tol=0.04282130065978013
[CV 2/3; 38/50] END C=0.008494605751462514, class_weight=balanced, l1_ratio=0.25, tol=0.04282130065978013;, score=0.987 total time=   8.4s
[CV 3/3; 38/50] START C=0.008494605751462514, class_weight=balanced, l1_ratio=0.25, tol=0.04282130065978013
[CV 3/3; 38/50] END C=0.008494605751462514, class_weight=balanced, l1_ratio=0.25, tol=0.04282130065978013;, score=0.947 total time=   2.5s
[CV 1/3; 39/50] START C=0.0018093703139043442, class_weight=None, l1_ratio=0.75, tol=0.01566611833823202
[CV 1/3; 39/50] END C=0.0018093703139043442, class_weight=None, l1_ratio=0.75, tol=0.01566611833823202;, score=0.813 total time=   1.3s
[CV 2/3; 39/50] START C=0.0018093703139043442, class_weight=None, l1_ratio=0.75, tol=0.01566611833823202
[CV 2/3; 39/50] END C=0.0018093703139043442, class_weight=None, l1_ratio=0.75, tol=0.01566611833823202;, score=0.898 total time=   1.2s
[CV 3/3; 39/50] START C=0.0018093703139043442, class_weight=None, l1_ratio=0.75, tol=0.01566611833823202
[CV 3/3; 39/50] END C=0.0018093703139043442, class_weight=None, l1_ratio=0.75, tol=0.01566611833823202;, score=0.854 total time=   1.3s
[CV 1/3; 40/50] START C=1.6810902961442453, class_weight=None, l1_ratio=0.0, tol=0.0011116300275050065
[CV 1/3; 40/50] END C=1.6810902961442453, class_weight=None, l1_ratio=0.0, tol=0.0011116300275050065;, score=0.747 total time=   7.8s
[CV 2/3; 40/50] START C=1.6810902961442453, class_weight=None, l1_ratio=0.0, tol=0.0011116300275050065
[CV 2/3; 40/50] END C=1.6810902961442453, class_weight=None, l1_ratio=0.0, tol=0.0011116300275050065;, score=0.991 total time=  10.4s
[CV 3/3; 40/50] START C=1.6810902961442453, class_weight=None, l1_ratio=0.0, tol=0.0011116300275050065
[CV 3/3; 40/50] END C=1.6810902961442453, class_weight=None, l1_ratio=0.0, tol=0.0011116300275050065;, score=0.969 total time=  12.1s
[CV 1/3; 41/50] START C=1.068377356934616, class_weight=balanced, l1_ratio=0.0, tol=0.02605549464223087
[CV 1/3; 41/50] END C=1.068377356934616, class_weight=balanced, l1_ratio=0.0, tol=0.02605549464223087;, score=0.818 total time=   0.9s
[CV 2/3; 41/50] START C=1.068377356934616, class_weight=balanced, l1_ratio=0.0, tol=0.02605549464223087
[CV 2/3; 41/50] END C=1.068377356934616, class_weight=balanced, l1_ratio=0.0, tol=0.02605549464223087;, score=0.991 total time=   0.8s
[CV 3/3; 41/50] START C=1.068377356934616, class_weight=balanced, l1_ratio=0.0, tol=0.02605549464223087
[CV 3/3; 41/50] END C=1.068377356934616, class_weight=balanced, l1_ratio=0.0, tol=0.02605549464223087;, score=0.952 total time=   0.6s
[CV 1/3; 42/50] START C=0.0016510550944110302, class_weight=balanced, l1_ratio=0.5, tol=0.04717449619795827
[CV 1/3; 42/50] END C=0.0016510550944110302, class_weight=balanced, l1_ratio=0.5, tol=0.04717449619795827;, score=0.705 total time=  59.3s
[CV 2/3; 42/50] START C=0.0016510550944110302, class_weight=balanced, l1_ratio=0.5, tol=0.04717449619795827
[CV 2/3; 42/50] END C=0.0016510550944110302, class_weight=balanced, l1_ratio=0.5, tol=0.04717449619795827;, score=0.968 total time=  59.3s
[CV 3/3; 42/50] START C=0.0016510550944110302, class_weight=balanced, l1_ratio=0.5, tol=0.04717449619795827
[CV 3/3; 42/50] END C=0.0016510550944110302, class_weight=balanced, l1_ratio=0.5, tol=0.04717449619795827;, score=0.909 total time=  59.0s
[CV 1/3; 43/50] START C=0.0019407626990621313, class_weight=balanced, l1_ratio=0.5, tol=0.012624787188439634
[CV 1/3; 43/50] END C=0.0019407626990621313, class_weight=balanced, l1_ratio=0.5, tol=0.012624787188439634;, score=0.700 total time=  59.0s
[CV 2/3; 43/50] START C=0.0019407626990621313, class_weight=balanced, l1_ratio=0.5, tol=0.012624787188439634
[CV 2/3; 43/50] END C=0.0019407626990621313, class_weight=balanced, l1_ratio=0.5, tol=0.012624787188439634;, score=0.965 total time=  59.0s
[CV 3/3; 43/50] START C=0.0019407626990621313, class_weight=balanced, l1_ratio=0.5, tol=0.012624787188439634
[CV 3/3; 43/50] END C=0.0019407626990621313, class_weight=balanced, l1_ratio=0.5, tol=0.012624787188439634;, score=0.930 total time=  59.1s
[CV 1/3; 44/50] START C=0.0033871233024201828, class_weight=None, l1_ratio=0.75, tol=0.009265946046241189
[CV 1/3; 44/50] END C=0.0033871233024201828, class_weight=None, l1_ratio=0.75, tol=0.009265946046241189;, score=0.874 total time=   1.5s
[CV 2/3; 44/50] START C=0.0033871233024201828, class_weight=None, l1_ratio=0.75, tol=0.009265946046241189
[CV 2/3; 44/50] END C=0.0033871233024201828, class_weight=None, l1_ratio=0.75, tol=0.009265946046241189;, score=0.912 total time=   1.8s
[CV 3/3; 44/50] START C=0.0033871233024201828, class_weight=None, l1_ratio=0.75, tol=0.009265946046241189
[CV 3/3; 44/50] END C=0.0033871233024201828, class_weight=None, l1_ratio=0.75, tol=0.009265946046241189;, score=0.880 total time=   1.9s
[CV 1/3; 45/50] START C=0.032153793294586404, class_weight=None, l1_ratio=0.75, tol=0.04342323831099849
[CV 1/3; 45/50] END C=0.032153793294586404, class_weight=None, l1_ratio=0.75, tol=0.04342323831099849;, score=0.895 total time=   0.9s
[CV 2/3; 45/50] START C=0.032153793294586404, class_weight=None, l1_ratio=0.75, tol=0.04342323831099849
[CV 2/3; 45/50] END C=0.032153793294586404, class_weight=None, l1_ratio=0.75, tol=0.04342323831099849;, score=0.982 total time=   0.7s
[CV 3/3; 45/50] START C=0.032153793294586404, class_weight=None, l1_ratio=0.75, tol=0.04342323831099849
[CV 3/3; 45/50] END C=0.032153793294586404, class_weight=None, l1_ratio=0.75, tol=0.04342323831099849;, score=0.948 total time=   0.8s
[CV 1/3; 46/50] START C=0.009056418626331005, class_weight=None, l1_ratio=0.25, tol=0.018962577082547373
[CV 1/3; 46/50] END C=0.009056418626331005, class_weight=None, l1_ratio=0.25, tol=0.018962577082547373;, score=0.922 total time=   0.9s
[CV 2/3; 46/50] START C=0.009056418626331005, class_weight=None, l1_ratio=0.25, tol=0.018962577082547373
[CV 2/3; 46/50] END C=0.009056418626331005, class_weight=None, l1_ratio=0.25, tol=0.018962577082547373;, score=0.974 total time=   0.8s
[CV 3/3; 46/50] START C=0.009056418626331005, class_weight=None, l1_ratio=0.25, tol=0.018962577082547373
[CV 3/3; 46/50] END C=0.009056418626331005, class_weight=None, l1_ratio=0.25, tol=0.018962577082547373;, score=0.945 total time=   0.8s
[CV 1/3; 47/50] START C=0.10217973005149451, class_weight=balanced, l1_ratio=1.0, tol=0.07433992494640584
[CV 1/3; 47/50] END C=0.10217973005149451, class_weight=balanced, l1_ratio=1.0, tol=0.07433992494640584;, score=0.693 total time=   1.2s
[CV 2/3; 47/50] START C=0.10217973005149451, class_weight=balanced, l1_ratio=1.0, tol=0.07433992494640584
[CV 2/3; 47/50] END C=0.10217973005149451, class_weight=balanced, l1_ratio=1.0, tol=0.07433992494640584;, score=0.990 total time=   0.8s
[CV 3/3; 47/50] START C=0.10217973005149451, class_weight=balanced, l1_ratio=1.0, tol=0.07433992494640584
[CV 3/3; 47/50] END C=0.10217973005149451, class_weight=balanced, l1_ratio=1.0, tol=0.07433992494640584;, score=0.946 total time=   0.5s
[CV 1/3; 48/50] START C=1.1805600580099593, class_weight=None, l1_ratio=1.0, tol=0.08671325037968315
[CV 1/3; 48/50] END C=1.1805600580099593, class_weight=None, l1_ratio=1.0, tol=0.08671325037968315;, score=0.928 total time=   0.6s
[CV 2/3; 48/50] START C=1.1805600580099593, class_weight=None, l1_ratio=1.0, tol=0.08671325037968315
[CV 2/3; 48/50] END C=1.1805600580099593, class_weight=None, l1_ratio=1.0, tol=0.08671325037968315;, score=0.987 total time=   0.6s
[CV 3/3; 48/50] START C=1.1805600580099593, class_weight=None, l1_ratio=1.0, tol=0.08671325037968315
[CV 3/3; 48/50] END C=1.1805600580099593, class_weight=None, l1_ratio=1.0, tol=0.08671325037968315;, score=0.956 total time=   0.6s
[CV 1/3; 49/50] START C=0.7008481917782963, class_weight=balanced, l1_ratio=0.5, tol=0.0010420981658979824
[CV 1/3; 49/50] END C=0.7008481917782963, class_weight=balanced, l1_ratio=0.5, tol=0.0010420981658979824;, score=0.668 total time=  15.9s
[CV 2/3; 49/50] START C=0.7008481917782963, class_weight=balanced, l1_ratio=0.5, tol=0.0010420981658979824
[CV 2/3; 49/50] END C=0.7008481917782963, class_weight=balanced, l1_ratio=0.5, tol=0.0010420981658979824;, score=0.993 total time=  16.5s
[CV 3/3; 49/50] START C=0.7008481917782963, class_weight=balanced, l1_ratio=0.5, tol=0.0010420981658979824
[CV 3/3; 49/50] END C=0.7008481917782963, class_weight=balanced, l1_ratio=0.5, tol=0.0010420981658979824;, score=0.964 total time=  21.3s
[CV 1/3; 50/50] START C=0.0235197394744825, class_weight=balanced, l1_ratio=0.25, tol=0.001584731927477609
[CV 1/3; 50/50] END C=0.0235197394744825, class_weight=balanced, l1_ratio=0.25, tol=0.001584731927477609;, score=0.724 total time=   3.9s
[CV 2/3; 50/50] START C=0.0235197394744825, class_weight=balanced, l1_ratio=0.25, tol=0.001584731927477609
[CV 2/3; 50/50] END C=0.0235197394744825, class_weight=balanced, l1_ratio=0.25, tol=0.001584731927477609;, score=0.990 total time=   6.1s
[CV 3/3; 50/50] START C=0.0235197394744825, class_weight=balanced, l1_ratio=0.25, tol=0.001584731927477609
[CV 3/3; 50/50] END C=0.0235197394744825, class_weight=balanced, l1_ratio=0.25, tol=0.001584731927477609;, score=0.953 total time=   5.4s

--- TUNING FINISHED ---
Beste Parameter: {'C': np.float64(0.3665682409386545), 'class_weight': None, 'l1_ratio': 0.5, 'tol': np.float64(0.09013945007365622)}
Bester CV-Score: 0.9574

--- EVALUATION AUF DEN TESTDATEN ---
Test Accuracy: 0.8798

Macro F1: 0.8279733582786954

--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.8798

                     precision    recall  f1-score   support

             B cell       0.98      0.99      0.99       120
     CD14+ monocyte       1.00      1.00      1.00      2575
        CD4+ T cell       0.83      1.00      0.90      3910
   Cytotoxic T cell       0.87      0.48      0.62      1824
     Dendritic cell       1.00      0.20      0.33         5
      Megakaryocyte       1.00      1.00      1.00         7
Natural killer cell       0.80      0.82      0.81       791
        Plasma cell       1.00      0.94      0.97        49

           accuracy                           0.88      9281
          macro avg       0.94      0.80      0.83      9281
       weighted avg       0.88      0.88      0.87      9281

Random dropout accuracy score 0.8566
Total samples: 9281
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.8801
Feature importance dropout (0.5% features dropped) accuracy score 0.8542
Feature importance dropout (1.0% features dropped) accuracy score 0.8293
Feature importance dropout (2.0% features dropped) accuracy score 0.7800
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8440

                     precision    recall  f1-score   support

             B cell       1.00      1.00      1.00      3960
     CD14+ monocyte       0.90      1.00      0.94      3135
        CD4+ T cell       0.87      1.00      0.93     13677
   Cytotoxic T cell       0.58      0.59      0.59      4843
     Dendritic cell       0.99      0.40      0.57       529
      Megakaryocyte       1.00      0.66      0.80        86
Natural killer cell       0.91      0.21      0.35      2751
        Plasma cell       0.88      0.91      0.89        23

           accuracy                           0.84     29004
          macro avg       0.89      0.72      0.76     29004
       weighted avg       0.85      0.84      0.82     29004

Random dropout accuracy score 0.8283
Total samples: 29004
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.8441
Feature importance dropout (0.5% features dropped) accuracy score 0.8232
Feature importance dropout (1.0% features dropped) accuracy score 0.7989
Feature importance dropout (2.0% features dropped) accuracy score 0.7247
=== JOB_STATISTICS ===
=== current date     : Sat Jun 27 18:39:37 CEST 2026
= Job-ID             : 11995954 on woody
= Job-Name           : autoencoder_lr
= Job-Command        : /home/hpc/iwbn/iwbn133h/submit_autoencoder_lr_v1.sh
= Initial workdir    : /home/hpc/iwbn/iwbn133h
= Queue/Partition    : work
= Slurm account      : iwbn with QOS=normal
= Features           : icx
= Requested resources:  for 17:00:00
= Elapsed runtime    : 02:21:22
= Total RAM usage    : 19.1 GiB of requested  GiB (%)   
= Node list          : w2519
= Subm/Elig/Start/End: 2026-06-27T16:18:14 / 2026-06-27T16:18:14 / 2026-06-27T16:18:15 / 2026-06-27T18:39:37
======================
=== Quota infos ======
    Path                 Used     SoftQ    HardQ    Gracetime  Filec    FileQ    FiHaQ    FileGrace    
    /home/woody           982.1M  1000.0G  1500.0G        N/A  29,019    5,000K   7,500K        N/A    
    /home/hpc              86.2G   104.9G   209.7G        N/A     139K     500K   1,000K        N/A    
    /home/vault             0.0K  1048.6G  2097.2G        N/A       1      200K     400K        N/A    
