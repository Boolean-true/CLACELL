### Starting TaskPrologue of job 11997759 on w2214 at Sun Jun 28 22:16:44 CEST 2026
#   SLURM_JOB_NODELIST=w2214
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
Epoch [10/150], Loss: 0.9049
Epoch [20/150], Loss: 0.8905
Epoch [30/150], Loss: 0.8819
Epoch [40/150], Loss: 0.8762
Epoch [50/150], Loss: 0.8726
Epoch [60/150], Loss: 0.8700
Epoch [70/150], Loss: 0.8679
Epoch [80/150], Loss: 0.8661
Epoch [90/150], Loss: 0.8646
Epoch [100/150], Loss: 0.8631
Epoch [110/150], Loss: 0.8621
Early Stopping after [118/150] Epochs!

Extract robust features...
Starte automatische Hyperparametersuche auf dem Latent Space...
Fitting 3 folds for each of 50 candidates, totalling 150 fits
[CV 1/3; 1/50] START C=0.06025644244847547, class_weight=balanced, dual=True, penalty=l2, tol=0.04900646522990686
[CV 1/3; 1/50] END C=0.06025644244847547, class_weight=balanced, dual=True, penalty=l2, tol=0.04900646522990686;, score=0.619 total time=   0.4s
[CV 2/3; 1/50] START C=0.06025644244847547, class_weight=balanced, dual=True, penalty=l2, tol=0.04900646522990686
[CV 2/3; 1/50] END C=0.06025644244847547, class_weight=balanced, dual=True, penalty=l2, tol=0.04900646522990686;, score=0.992 total time=   0.4s
[CV 3/3; 1/50] START C=0.06025644244847547, class_weight=balanced, dual=True, penalty=l2, tol=0.04900646522990686
[CV 3/3; 1/50] END C=0.06025644244847547, class_weight=balanced, dual=True, penalty=l2, tol=0.04900646522990686;, score=0.967 total time=   0.4s
[CV 1/3; 2/50] START C=0.6273722031811344, class_weight=balanced, dual=True, penalty=l2, tol=0.055503130271187466
[CV 1/3; 2/50] END C=0.6273722031811344, class_weight=balanced, dual=True, penalty=l2, tol=0.055503130271187466;, score=0.643 total time=   0.5s
[CV 2/3; 2/50] START C=0.6273722031811344, class_weight=balanced, dual=True, penalty=l2, tol=0.055503130271187466
[CV 2/3; 2/50] END C=0.6273722031811344, class_weight=balanced, dual=True, penalty=l2, tol=0.055503130271187466;, score=0.993 total time=   0.6s
[CV 3/3; 2/50] START C=0.6273722031811344, class_weight=balanced, dual=True, penalty=l2, tol=0.055503130271187466
[CV 3/3; 2/50] END C=0.6273722031811344, class_weight=balanced, dual=True, penalty=l2, tol=0.055503130271187466;, score=0.967 total time=   0.6s
[CV 1/3; 3/50] START C=0.010331524193695686, class_weight=None, dual=False, penalty=l2, tol=0.013949832883069998
[CV 1/3; 3/50] END C=0.010331524193695686, class_weight=None, dual=False, penalty=l2, tol=0.013949832883069998;, score=0.713 total time=   0.5s
[CV 2/3; 3/50] START C=0.010331524193695686, class_weight=None, dual=False, penalty=l2, tol=0.013949832883069998
[CV 2/3; 3/50] END C=0.010331524193695686, class_weight=None, dual=False, penalty=l2, tol=0.013949832883069998;, score=0.988 total time=   0.5s
[CV 3/3; 3/50] START C=0.010331524193695686, class_weight=None, dual=False, penalty=l2, tol=0.013949832883069998
[CV 3/3; 3/50] END C=0.010331524193695686, class_weight=None, dual=False, penalty=l2, tol=0.013949832883069998;, score=0.961 total time=   0.5s
[CV 1/3; 4/50] START C=0.7025452370586998, class_weight=balanced, dual=False, penalty=l2, tol=0.04810083288996589
[CV 1/3; 4/50] END C=0.7025452370586998, class_weight=balanced, dual=False, penalty=l2, tol=0.04810083288996589;, score=0.614 total time=   0.5s
[CV 2/3; 4/50] START C=0.7025452370586998, class_weight=balanced, dual=False, penalty=l2, tol=0.04810083288996589
[CV 2/3; 4/50] END C=0.7025452370586998, class_weight=balanced, dual=False, penalty=l2, tol=0.04810083288996589;, score=0.991 total time=   0.6s
[CV 3/3; 4/50] START C=0.7025452370586998, class_weight=balanced, dual=False, penalty=l2, tol=0.04810083288996589
[CV 3/3; 4/50] END C=0.7025452370586998, class_weight=balanced, dual=False, penalty=l2, tol=0.04810083288996589;, score=0.961 total time=   0.5s
[CV 1/3; 5/50] START C=0.001128061091785296, class_weight=None, dual=False, penalty=l2, tol=0.05039774665420268
[CV 1/3; 5/50] END C=0.001128061091785296, class_weight=None, dual=False, penalty=l2, tol=0.05039774665420268;, score=0.844 total time=   0.5s
[CV 2/3; 5/50] START C=0.001128061091785296, class_weight=None, dual=False, penalty=l2, tol=0.05039774665420268
[CV 2/3; 5/50] END C=0.001128061091785296, class_weight=None, dual=False, penalty=l2, tol=0.05039774665420268;, score=0.981 total time=   0.5s
[CV 3/3; 5/50] START C=0.001128061091785296, class_weight=None, dual=False, penalty=l2, tol=0.05039774665420268
[CV 3/3; 5/50] END C=0.001128061091785296, class_weight=None, dual=False, penalty=l2, tol=0.05039774665420268;, score=0.951 total time=   0.5s
[CV 1/3; 6/50] START C=0.11521643219249753, class_weight=balanced, dual=False, penalty=l2, tol=0.006924962375245954
[CV 1/3; 6/50] END C=0.11521643219249753, class_weight=balanced, dual=False, penalty=l2, tol=0.006924962375245954;, score=0.627 total time=   0.6s
[CV 2/3; 6/50] START C=0.11521643219249753, class_weight=balanced, dual=False, penalty=l2, tol=0.006924962375245954
[CV 2/3; 6/50] END C=0.11521643219249753, class_weight=balanced, dual=False, penalty=l2, tol=0.006924962375245954;, score=0.992 total time=   0.6s
[CV 3/3; 6/50] START C=0.11521643219249753, class_weight=balanced, dual=False, penalty=l2, tol=0.006924962375245954
[CV 3/3; 6/50] END C=0.11521643219249753, class_weight=balanced, dual=False, penalty=l2, tol=0.006924962375245954;, score=0.965 total time=   1.0s
[CV 1/3; 7/50] START C=0.0021558670106387023, class_weight=None, dual=True, penalty=l2, tol=0.02281422210377158
[CV 1/3; 7/50] END C=0.0021558670106387023, class_weight=None, dual=True, penalty=l2, tol=0.02281422210377158;, score=0.810 total time=   0.4s
[CV 2/3; 7/50] START C=0.0021558670106387023, class_weight=None, dual=True, penalty=l2, tol=0.02281422210377158
[CV 2/3; 7/50] END C=0.0021558670106387023, class_weight=None, dual=True, penalty=l2, tol=0.02281422210377158;, score=0.985 total time=   0.4s
[CV 3/3; 7/50] START C=0.0021558670106387023, class_weight=None, dual=True, penalty=l2, tol=0.02281422210377158
[CV 3/3; 7/50] END C=0.0021558670106387023, class_weight=None, dual=True, penalty=l2, tol=0.02281422210377158;, score=0.959 total time=   0.4s
[CV 1/3; 8/50] START C=0.08630825508285565, class_weight=balanced, dual=False, penalty=l2, tol=0.002980824618917506
[CV 1/3; 8/50] END C=0.08630825508285565, class_weight=balanced, dual=False, penalty=l2, tol=0.002980824618917506;, score=0.612 total time=   0.6s
[CV 2/3; 8/50] START C=0.08630825508285565, class_weight=balanced, dual=False, penalty=l2, tol=0.002980824618917506
[CV 2/3; 8/50] END C=0.08630825508285565, class_weight=balanced, dual=False, penalty=l2, tol=0.002980824618917506;, score=0.992 total time=   0.7s
[CV 3/3; 8/50] START C=0.08630825508285565, class_weight=balanced, dual=False, penalty=l2, tol=0.002980824618917506
[CV 3/3; 8/50] END C=0.08630825508285565, class_weight=balanced, dual=False, penalty=l2, tol=0.002980824618917506;, score=0.967 total time=   1.0s
[CV 1/3; 9/50] START C=0.0685717601104951, class_weight=None, dual=False, penalty=l2, tol=0.005611529342226497
[CV 1/3; 9/50] END C=0.0685717601104951, class_weight=None, dual=False, penalty=l2, tol=0.005611529342226497;, score=0.654 total time=   0.5s
[CV 2/3; 9/50] START C=0.0685717601104951, class_weight=None, dual=False, penalty=l2, tol=0.005611529342226497
[CV 2/3; 9/50] END C=0.0685717601104951, class_weight=None, dual=False, penalty=l2, tol=0.005611529342226497;, score=0.991 total time=   0.5s
[CV 3/3; 9/50] START C=0.0685717601104951, class_weight=None, dual=False, penalty=l2, tol=0.005611529342226497
[CV 3/3; 9/50] END C=0.0685717601104951, class_weight=None, dual=False, penalty=l2, tol=0.005611529342226497;, score=0.965 total time=   0.5s
[CV 1/3; 10/50] START C=0.43469372562359676, class_weight=balanced, dual=False, penalty=l2, tol=0.001572704649813727
[CV 1/3; 10/50] END C=0.43469372562359676, class_weight=balanced, dual=False, penalty=l2, tol=0.001572704649813727;, score=0.645 total time=   1.0s
[CV 2/3; 10/50] START C=0.43469372562359676, class_weight=balanced, dual=False, penalty=l2, tol=0.001572704649813727
[CV 2/3; 10/50] END C=0.43469372562359676, class_weight=balanced, dual=False, penalty=l2, tol=0.001572704649813727;, score=0.993 total time=   1.2s
[CV 3/3; 10/50] START C=0.43469372562359676, class_weight=balanced, dual=False, penalty=l2, tol=0.001572704649813727
[CV 3/3; 10/50] END C=0.43469372562359676, class_weight=balanced, dual=False, penalty=l2, tol=0.001572704649813727;, score=0.967 total time=   1.8s
[CV 1/3; 11/50] START C=0.6872234373633369, class_weight=None, dual=False, penalty=l2, tol=0.0022353762830958275
[CV 1/3; 11/50] END C=0.6872234373633369, class_weight=None, dual=False, penalty=l2, tol=0.0022353762830958275;, score=0.675 total time=   0.6s
[CV 2/3; 11/50] START C=0.6872234373633369, class_weight=None, dual=False, penalty=l2, tol=0.0022353762830958275
[CV 2/3; 11/50] END C=0.6872234373633369, class_weight=None, dual=False, penalty=l2, tol=0.0022353762830958275;, score=0.992 total time=   0.6s
[CV 3/3; 11/50] START C=0.6872234373633369, class_weight=None, dual=False, penalty=l2, tol=0.0022353762830958275
[CV 3/3; 11/50] END C=0.6872234373633369, class_weight=None, dual=False, penalty=l2, tol=0.0022353762830958275;, score=0.966 total time=   0.6s
[CV 1/3; 12/50] START C=0.2131767505865927, class_weight=balanced, dual=True, penalty=l2, tol=0.05872403440892959
[CV 1/3; 12/50] END C=0.2131767505865927, class_weight=balanced, dual=True, penalty=l2, tol=0.05872403440892959;, score=0.637 total time=   0.5s
[CV 2/3; 12/50] START C=0.2131767505865927, class_weight=balanced, dual=True, penalty=l2, tol=0.05872403440892959
[CV 2/3; 12/50] END C=0.2131767505865927, class_weight=balanced, dual=True, penalty=l2, tol=0.05872403440892959;, score=0.993 total time=   0.5s
[CV 3/3; 12/50] START C=0.2131767505865927, class_weight=balanced, dual=True, penalty=l2, tol=0.05872403440892959
[CV 3/3; 12/50] END C=0.2131767505865927, class_weight=balanced, dual=True, penalty=l2, tol=0.05872403440892959;, score=0.968 total time=   0.5s
[CV 1/3; 13/50] START C=0.9778694780690537, class_weight=balanced, dual=False, penalty=l2, tol=0.0015825543649592034
[CV 1/3; 13/50] END C=0.9778694780690537, class_weight=balanced, dual=False, penalty=l2, tol=0.0015825543649592034;, score=0.645 total time=   0.8s
[CV 2/3; 13/50] START C=0.9778694780690537, class_weight=balanced, dual=False, penalty=l2, tol=0.0015825543649592034
[CV 2/3; 13/50] END C=0.9778694780690537, class_weight=balanced, dual=False, penalty=l2, tol=0.0015825543649592034;, score=0.993 total time=   1.6s
[CV 3/3; 13/50] START C=0.9778694780690537, class_weight=balanced, dual=False, penalty=l2, tol=0.0015825543649592034
[CV 3/3; 13/50] END C=0.9778694780690537, class_weight=balanced, dual=False, penalty=l2, tol=0.0015825543649592034;, score=0.967 total time=   1.6s
[CV 1/3; 14/50] START C=0.004700325515602533, class_weight=balanced, dual=False, penalty=l2, tol=0.00784433264421656
[CV 1/3; 14/50] END C=0.004700325515602533, class_weight=balanced, dual=False, penalty=l2, tol=0.00784433264421656;, score=0.704 total time=   0.5s
[CV 2/3; 14/50] START C=0.004700325515602533, class_weight=balanced, dual=False, penalty=l2, tol=0.00784433264421656
[CV 2/3; 14/50] END C=0.004700325515602533, class_weight=balanced, dual=False, penalty=l2, tol=0.00784433264421656;, score=0.991 total time=   0.6s
[CV 3/3; 14/50] START C=0.004700325515602533, class_weight=balanced, dual=False, penalty=l2, tol=0.00784433264421656
[CV 3/3; 14/50] END C=0.004700325515602533, class_weight=balanced, dual=False, penalty=l2, tol=0.00784433264421656;, score=0.963 total time=   0.6s
[CV 1/3; 15/50] START C=0.08229861600362949, class_weight=balanced, dual=True, penalty=l2, tol=0.023533682799871312
[CV 1/3; 15/50] END C=0.08229861600362949, class_weight=balanced, dual=True, penalty=l2, tol=0.023533682799871312;, score=0.623 total time=   0.5s
[CV 2/3; 15/50] START C=0.08229861600362949, class_weight=balanced, dual=True, penalty=l2, tol=0.023533682799871312
[CV 2/3; 15/50] END C=0.08229861600362949, class_weight=balanced, dual=True, penalty=l2, tol=0.023533682799871312;, score=0.992 total time=   0.5s
[CV 3/3; 15/50] START C=0.08229861600362949, class_weight=balanced, dual=True, penalty=l2, tol=0.023533682799871312
[CV 3/3; 15/50] END C=0.08229861600362949, class_weight=balanced, dual=True, penalty=l2, tol=0.023533682799871312;, score=0.967 total time=   0.5s
[CV 1/3; 16/50] START C=0.001786549376806633, class_weight=balanced, dual=False, penalty=l2, tol=0.0921443638266478
[CV 1/3; 16/50] END C=0.001786549376806633, class_weight=balanced, dual=False, penalty=l2, tol=0.0921443638266478;, score=0.761 total time=   0.5s
[CV 2/3; 16/50] START C=0.001786549376806633, class_weight=balanced, dual=False, penalty=l2, tol=0.0921443638266478
[CV 2/3; 16/50] END C=0.001786549376806633, class_weight=balanced, dual=False, penalty=l2, tol=0.0921443638266478;, score=0.990 total time=   0.5s
[CV 3/3; 16/50] START C=0.001786549376806633, class_weight=balanced, dual=False, penalty=l2, tol=0.0921443638266478
[CV 3/3; 16/50] END C=0.001786549376806633, class_weight=balanced, dual=False, penalty=l2, tol=0.0921443638266478;, score=0.960 total time=   0.5s
[CV 1/3; 17/50] START C=0.1359199091595449, class_weight=None, dual=False, penalty=l2, tol=0.005651374375277766
[CV 1/3; 17/50] END C=0.1359199091595449, class_weight=None, dual=False, penalty=l2, tol=0.005651374375277766;, score=0.657 total time=   0.5s
[CV 2/3; 17/50] START C=0.1359199091595449, class_weight=None, dual=False, penalty=l2, tol=0.005651374375277766
[CV 2/3; 17/50] END C=0.1359199091595449, class_weight=None, dual=False, penalty=l2, tol=0.005651374375277766;, score=0.991 total time=   0.6s
[CV 3/3; 17/50] START C=0.1359199091595449, class_weight=None, dual=False, penalty=l2, tol=0.005651374375277766
[CV 3/3; 17/50] END C=0.1359199091595449, class_weight=None, dual=False, penalty=l2, tol=0.005651374375277766;, score=0.966 total time=   0.6s
[CV 1/3; 18/50] START C=0.04717099924822449, class_weight=None, dual=True, penalty=l2, tol=0.0052532382479232274
[CV 1/3; 18/50] END C=0.04717099924822449, class_weight=None, dual=True, penalty=l2, tol=0.0052532382479232274;, score=0.678 total time=   0.4s
[CV 2/3; 18/50] START C=0.04717099924822449, class_weight=None, dual=True, penalty=l2, tol=0.0052532382479232274
[CV 2/3; 18/50] END C=0.04717099924822449, class_weight=None, dual=True, penalty=l2, tol=0.0052532382479232274;, score=0.991 total time=   0.4s
[CV 3/3; 18/50] START C=0.04717099924822449, class_weight=None, dual=True, penalty=l2, tol=0.0052532382479232274
[CV 3/3; 18/50] END C=0.04717099924822449, class_weight=None, dual=True, penalty=l2, tol=0.0052532382479232274;, score=0.967 total time=   0.5s
[CV 1/3; 19/50] START C=0.006141821677873538, class_weight=None, dual=True, penalty=l2, tol=0.005560730423480962
[CV 1/3; 19/50] END C=0.006141821677873538, class_weight=None, dual=True, penalty=l2, tol=0.005560730423480962;, score=0.746 total time=   0.4s
[CV 2/3; 19/50] START C=0.006141821677873538, class_weight=None, dual=True, penalty=l2, tol=0.005560730423480962
[CV 2/3; 19/50] END C=0.006141821677873538, class_weight=None, dual=True, penalty=l2, tol=0.005560730423480962;, score=0.988 total time=   0.4s
[CV 3/3; 19/50] START C=0.006141821677873538, class_weight=None, dual=True, penalty=l2, tol=0.005560730423480962
[CV 3/3; 19/50] END C=0.006141821677873538, class_weight=None, dual=True, penalty=l2, tol=0.005560730423480962;, score=0.963 total time=   0.4s
[CV 1/3; 20/50] START C=0.4114275544280096, class_weight=balanced, dual=False, penalty=l2, tol=0.001968879202879717
[CV 1/3; 20/50] END C=0.4114275544280096, class_weight=balanced, dual=False, penalty=l2, tol=0.001968879202879717;, score=0.642 total time=   0.9s
[CV 2/3; 20/50] START C=0.4114275544280096, class_weight=balanced, dual=False, penalty=l2, tol=0.001968879202879717
[CV 2/3; 20/50] END C=0.4114275544280096, class_weight=balanced, dual=False, penalty=l2, tol=0.001968879202879717;, score=0.993 total time=   1.0s
[CV 3/3; 20/50] START C=0.4114275544280096, class_weight=balanced, dual=False, penalty=l2, tol=0.001968879202879717
[CV 3/3; 20/50] END C=0.4114275544280096, class_weight=balanced, dual=False, penalty=l2, tol=0.001968879202879717;, score=0.967 total time=   2.4s
[CV 1/3; 21/50] START C=0.0027835899000448663, class_weight=None, dual=True, penalty=l2, tol=0.0019626603659389464
[CV 1/3; 21/50] END C=0.0027835899000448663, class_weight=None, dual=True, penalty=l2, tol=0.0019626603659389464;, score=0.794 total time=   0.4s
[CV 2/3; 21/50] START C=0.0027835899000448663, class_weight=None, dual=True, penalty=l2, tol=0.0019626603659389464
[CV 2/3; 21/50] END C=0.0027835899000448663, class_weight=None, dual=True, penalty=l2, tol=0.0019626603659389464;, score=0.986 total time=   0.4s
[CV 3/3; 21/50] START C=0.0027835899000448663, class_weight=None, dual=True, penalty=l2, tol=0.0019626603659389464
[CV 3/3; 21/50] END C=0.0027835899000448663, class_weight=None, dual=True, penalty=l2, tol=0.0019626603659389464;, score=0.959 total time=   0.4s
[CV 1/3; 22/50] START C=0.014920061787028751, class_weight=balanced, dual=True, penalty=l2, tol=0.01617079852437494
[CV 1/3; 22/50] END C=0.014920061787028751, class_weight=balanced, dual=True, penalty=l2, tol=0.01617079852437494;, score=0.650 total time=   0.4s
[CV 2/3; 22/50] START C=0.014920061787028751, class_weight=balanced, dual=True, penalty=l2, tol=0.01617079852437494
[CV 2/3; 22/50] END C=0.014920061787028751, class_weight=balanced, dual=True, penalty=l2, tol=0.01617079852437494;, score=0.991 total time=   0.4s
[CV 3/3; 22/50] START C=0.014920061787028751, class_weight=balanced, dual=True, penalty=l2, tol=0.01617079852437494
[CV 3/3; 22/50] END C=0.014920061787028751, class_weight=balanced, dual=True, penalty=l2, tol=0.01617079852437494;, score=0.966 total time=   0.4s
[CV 1/3; 23/50] START C=0.7294972125492344, class_weight=None, dual=False, penalty=l2, tol=0.08323398334702206
[CV 1/3; 23/50] END C=0.7294972125492344, class_weight=None, dual=False, penalty=l2, tol=0.08323398334702206;, score=0.756 total time=   0.5s
[CV 2/3; 23/50] START C=0.7294972125492344, class_weight=None, dual=False, penalty=l2, tol=0.08323398334702206
[CV 2/3; 23/50] END C=0.7294972125492344, class_weight=None, dual=False, penalty=l2, tol=0.08323398334702206;, score=0.988 total time=   0.5s
[CV 3/3; 23/50] START C=0.7294972125492344, class_weight=None, dual=False, penalty=l2, tol=0.08323398334702206
[CV 3/3; 23/50] END C=0.7294972125492344, class_weight=None, dual=False, penalty=l2, tol=0.08323398334702206;, score=0.958 total time=   0.5s
[CV 1/3; 24/50] START C=0.17413720873473146, class_weight=None, dual=False, penalty=l2, tol=0.002927419528442093
[CV 1/3; 24/50] END C=0.17413720873473146, class_weight=None, dual=False, penalty=l2, tol=0.002927419528442093;, score=0.664 total time=   0.6s
[CV 2/3; 24/50] START C=0.17413720873473146, class_weight=None, dual=False, penalty=l2, tol=0.002927419528442093
[CV 2/3; 24/50] END C=0.17413720873473146, class_weight=None, dual=False, penalty=l2, tol=0.002927419528442093;, score=0.992 total time=   0.6s
[CV 3/3; 24/50] START C=0.17413720873473146, class_weight=None, dual=False, penalty=l2, tol=0.002927419528442093
[CV 3/3; 24/50] END C=0.17413720873473146, class_weight=None, dual=False, penalty=l2, tol=0.002927419528442093;, score=0.968 total time=   0.6s
[CV 1/3; 25/50] START C=0.03617951885238961, class_weight=None, dual=True, penalty=l2, tol=0.029697474816555172
[CV 1/3; 25/50] END C=0.03617951885238961, class_weight=None, dual=True, penalty=l2, tol=0.029697474816555172;, score=0.676 total time=   0.4s
[CV 2/3; 25/50] START C=0.03617951885238961, class_weight=None, dual=True, penalty=l2, tol=0.029697474816555172
[CV 2/3; 25/50] END C=0.03617951885238961, class_weight=None, dual=True, penalty=l2, tol=0.029697474816555172;, score=0.991 total time=   0.4s
[CV 3/3; 25/50] START C=0.03617951885238961, class_weight=None, dual=True, penalty=l2, tol=0.029697474816555172
[CV 3/3; 25/50] END C=0.03617951885238961, class_weight=None, dual=True, penalty=l2, tol=0.029697474816555172;, score=0.967 total time=   0.4s
[CV 1/3; 26/50] START C=1.71980888487255, class_weight=None, dual=True, penalty=l2, tol=0.021377729596053198
[CV 1/3; 26/50] END C=1.71980888487255, class_weight=None, dual=True, penalty=l2, tol=0.021377729596053198;, score=0.659 total time=   0.6s
[CV 2/3; 26/50] START C=1.71980888487255, class_weight=None, dual=True, penalty=l2, tol=0.021377729596053198
[CV 2/3; 26/50] END C=1.71980888487255, class_weight=None, dual=True, penalty=l2, tol=0.021377729596053198;, score=0.992 total time=   0.6s
[CV 3/3; 26/50] START C=1.71980888487255, class_weight=None, dual=True, penalty=l2, tol=0.021377729596053198
[CV 3/3; 26/50] END C=1.71980888487255, class_weight=None, dual=True, penalty=l2, tol=0.021377729596053198;, score=0.965 total time=   0.6s
[CV 1/3; 27/50] START C=0.963406911709387, class_weight=None, dual=True, penalty=l2, tol=0.004154835352794472
[CV 1/3; 27/50] END C=0.963406911709387, class_weight=None, dual=True, penalty=l2, tol=0.004154835352794472;, score=0.660 total time=   0.6s
[CV 2/3; 27/50] START C=0.963406911709387, class_weight=None, dual=True, penalty=l2, tol=0.004154835352794472
[CV 2/3; 27/50] END C=0.963406911709387, class_weight=None, dual=True, penalty=l2, tol=0.004154835352794472;, score=0.992 total time=   0.6s
[CV 3/3; 27/50] START C=0.963406911709387, class_weight=None, dual=True, penalty=l2, tol=0.004154835352794472
[CV 3/3; 27/50] END C=0.963406911709387, class_weight=None, dual=True, penalty=l2, tol=0.004154835352794472;, score=0.966 total time=   0.6s
[CV 1/3; 28/50] START C=0.08365506845029887, class_weight=None, dual=False, penalty=l2, tol=0.00934140975627621
[CV 1/3; 28/50] END C=0.08365506845029887, class_weight=None, dual=False, penalty=l2, tol=0.00934140975627621;, score=0.663 total time=   0.5s
[CV 2/3; 28/50] START C=0.08365506845029887, class_weight=None, dual=False, penalty=l2, tol=0.00934140975627621
[CV 2/3; 28/50] END C=0.08365506845029887, class_weight=None, dual=False, penalty=l2, tol=0.00934140975627621;, score=0.991 total time=   0.6s
[CV 3/3; 28/50] START C=0.08365506845029887, class_weight=None, dual=False, penalty=l2, tol=0.00934140975627621
[CV 3/3; 28/50] END C=0.08365506845029887, class_weight=None, dual=False, penalty=l2, tol=0.00934140975627621;, score=0.964 total time=   0.5s
[CV 1/3; 29/50] START C=0.001248778833652541, class_weight=None, dual=False, penalty=l2, tol=0.054263632503439824
[CV 1/3; 29/50] END C=0.001248778833652541, class_weight=None, dual=False, penalty=l2, tol=0.054263632503439824;, score=0.845 total time=   0.5s
[CV 2/3; 29/50] START C=0.001248778833652541, class_weight=None, dual=False, penalty=l2, tol=0.054263632503439824
[CV 2/3; 29/50] END C=0.001248778833652541, class_weight=None, dual=False, penalty=l2, tol=0.054263632503439824;, score=0.982 total time=   0.5s
[CV 3/3; 29/50] START C=0.001248778833652541, class_weight=None, dual=False, penalty=l2, tol=0.054263632503439824
[CV 3/3; 29/50] END C=0.001248778833652541, class_weight=None, dual=False, penalty=l2, tol=0.054263632503439824;, score=0.952 total time=   0.5s
[CV 1/3; 30/50] START C=0.002123589907225951, class_weight=None, dual=False, penalty=l2, tol=0.0035840343047933783
[CV 1/3; 30/50] END C=0.002123589907225951, class_weight=None, dual=False, penalty=l2, tol=0.0035840343047933783;, score=0.811 total time=   0.5s
[CV 2/3; 30/50] START C=0.002123589907225951, class_weight=None, dual=False, penalty=l2, tol=0.0035840343047933783
[CV 2/3; 30/50] END C=0.002123589907225951, class_weight=None, dual=False, penalty=l2, tol=0.0035840343047933783;, score=0.985 total time=   0.5s
[CV 3/3; 30/50] START C=0.002123589907225951, class_weight=None, dual=False, penalty=l2, tol=0.0035840343047933783
[CV 3/3; 30/50] END C=0.002123589907225951, class_weight=None, dual=False, penalty=l2, tol=0.0035840343047933783;, score=0.959 total time=   0.5s
[CV 1/3; 31/50] START C=0.0017330911645664884, class_weight=balanced, dual=False, penalty=l2, tol=0.021516805700326956
[CV 1/3; 31/50] END C=0.0017330911645664884, class_weight=balanced, dual=False, penalty=l2, tol=0.021516805700326956;, score=0.739 total time=   0.5s
[CV 2/3; 31/50] START C=0.0017330911645664884, class_weight=balanced, dual=False, penalty=l2, tol=0.021516805700326956
[CV 2/3; 31/50] END C=0.0017330911645664884, class_weight=balanced, dual=False, penalty=l2, tol=0.021516805700326956;, score=0.990 total time=   0.5s
[CV 3/3; 31/50] START C=0.0017330911645664884, class_weight=balanced, dual=False, penalty=l2, tol=0.021516805700326956
[CV 3/3; 31/50] END C=0.0017330911645664884, class_weight=balanced, dual=False, penalty=l2, tol=0.021516805700326956;, score=0.961 total time=   0.5s
[CV 1/3; 32/50] START C=0.10561538507903344, class_weight=balanced, dual=True, penalty=l2, tol=0.010361880453547832
[CV 1/3; 32/50] END C=0.10561538507903344, class_weight=balanced, dual=True, penalty=l2, tol=0.010361880453547832;, score=0.623 total time=   0.5s
[CV 2/3; 32/50] START C=0.10561538507903344, class_weight=balanced, dual=True, penalty=l2, tol=0.010361880453547832
[CV 2/3; 32/50] END C=0.10561538507903344, class_weight=balanced, dual=True, penalty=l2, tol=0.010361880453547832;, score=0.992 total time=   0.5s
[CV 3/3; 32/50] START C=0.10561538507903344, class_weight=balanced, dual=True, penalty=l2, tol=0.010361880453547832
[CV 3/3; 32/50] END C=0.10561538507903344, class_weight=balanced, dual=True, penalty=l2, tol=0.010361880453547832;, score=0.968 total time=   0.5s
[CV 1/3; 33/50] START C=0.18414389552301577, class_weight=balanced, dual=True, penalty=l2, tol=0.0014643491719400269
[CV 1/3; 33/50] END C=0.18414389552301577, class_weight=balanced, dual=True, penalty=l2, tol=0.0014643491719400269;, score=0.632 total time=   0.5s
[CV 2/3; 33/50] START C=0.18414389552301577, class_weight=balanced, dual=True, penalty=l2, tol=0.0014643491719400269
[CV 2/3; 33/50] END C=0.18414389552301577, class_weight=balanced, dual=True, penalty=l2, tol=0.0014643491719400269;, score=0.993 total time=   0.6s
[CV 3/3; 33/50] START C=0.18414389552301577, class_weight=balanced, dual=True, penalty=l2, tol=0.0014643491719400269
[CV 3/3; 33/50] END C=0.18414389552301577, class_weight=balanced, dual=True, penalty=l2, tol=0.0014643491719400269;, score=0.968 total time=   0.5s
[CV 1/3; 34/50] START C=0.640325962700428, class_weight=None, dual=True, penalty=l2, tol=0.018100309975360974
[CV 1/3; 34/50] END C=0.640325962700428, class_weight=None, dual=True, penalty=l2, tol=0.018100309975360974;, score=0.661 total time=   0.6s
[CV 2/3; 34/50] START C=0.640325962700428, class_weight=None, dual=True, penalty=l2, tol=0.018100309975360974
[CV 2/3; 34/50] END C=0.640325962700428, class_weight=None, dual=True, penalty=l2, tol=0.018100309975360974;, score=0.992 total time=   0.6s
[CV 3/3; 34/50] START C=0.640325962700428, class_weight=None, dual=True, penalty=l2, tol=0.018100309975360974
[CV 3/3; 34/50] END C=0.640325962700428, class_weight=None, dual=True, penalty=l2, tol=0.018100309975360974;, score=0.967 total time=   0.6s
[CV 1/3; 35/50] START C=0.0012063310154057318, class_weight=balanced, dual=True, penalty=l2, tol=0.01198528979788855
[CV 1/3; 35/50] END C=0.0012063310154057318, class_weight=balanced, dual=True, penalty=l2, tol=0.01198528979788855;, score=0.755 total time=   0.4s
[CV 2/3; 35/50] START C=0.0012063310154057318, class_weight=balanced, dual=True, penalty=l2, tol=0.01198528979788855
[CV 2/3; 35/50] END C=0.0012063310154057318, class_weight=balanced, dual=True, penalty=l2, tol=0.01198528979788855;, score=0.990 total time=   0.4s
[CV 3/3; 35/50] START C=0.0012063310154057318, class_weight=balanced, dual=True, penalty=l2, tol=0.01198528979788855
[CV 3/3; 35/50] END C=0.0012063310154057318, class_weight=balanced, dual=True, penalty=l2, tol=0.01198528979788855;, score=0.961 total time=   0.4s
[CV 1/3; 36/50] START C=0.015408515665453237, class_weight=balanced, dual=True, penalty=l2, tol=0.029769778641730072
[CV 1/3; 36/50] END C=0.015408515665453237, class_weight=balanced, dual=True, penalty=l2, tol=0.029769778641730072;, score=0.650 total time=   0.4s
[CV 2/3; 36/50] START C=0.015408515665453237, class_weight=balanced, dual=True, penalty=l2, tol=0.029769778641730072
[CV 2/3; 36/50] END C=0.015408515665453237, class_weight=balanced, dual=True, penalty=l2, tol=0.029769778641730072;, score=0.991 total time=   0.4s
[CV 3/3; 36/50] START C=0.015408515665453237, class_weight=balanced, dual=True, penalty=l2, tol=0.029769778641730072
[CV 3/3; 36/50] END C=0.015408515665453237, class_weight=balanced, dual=True, penalty=l2, tol=0.029769778641730072;, score=0.966 total time=   0.4s
[CV 1/3; 37/50] START C=0.0011044201656011192, class_weight=None, dual=True, penalty=l2, tol=0.011601621128674567
[CV 1/3; 37/50] END C=0.0011044201656011192, class_weight=None, dual=True, penalty=l2, tol=0.011601621128674567;, score=0.842 total time=   0.4s
[CV 2/3; 37/50] START C=0.0011044201656011192, class_weight=None, dual=True, penalty=l2, tol=0.011601621128674567
[CV 2/3; 37/50] END C=0.0011044201656011192, class_weight=None, dual=True, penalty=l2, tol=0.011601621128674567;, score=0.981 total time=   0.4s
[CV 3/3; 37/50] START C=0.0011044201656011192, class_weight=None, dual=True, penalty=l2, tol=0.011601621128674567
[CV 3/3; 37/50] END C=0.0011044201656011192, class_weight=None, dual=True, penalty=l2, tol=0.011601621128674567;, score=0.955 total time=   0.4s
[CV 1/3; 38/50] START C=0.009278705334489889, class_weight=None, dual=True, penalty=l2, tol=0.0090122119762852
[CV 1/3; 38/50] END C=0.009278705334489889, class_weight=None, dual=True, penalty=l2, tol=0.0090122119762852;, score=0.722 total time=   0.4s
[CV 2/3; 38/50] START C=0.009278705334489889, class_weight=None, dual=True, penalty=l2, tol=0.0090122119762852
[CV 2/3; 38/50] END C=0.009278705334489889, class_weight=None, dual=True, penalty=l2, tol=0.0090122119762852;, score=0.989 total time=   0.4s
[CV 3/3; 38/50] START C=0.009278705334489889, class_weight=None, dual=True, penalty=l2, tol=0.0090122119762852
[CV 3/3; 38/50] END C=0.009278705334489889, class_weight=None, dual=True, penalty=l2, tol=0.0090122119762852;, score=0.964 total time=   0.4s
[CV 1/3; 39/50] START C=0.001159924390882601, class_weight=None, dual=True, penalty=l2, tol=0.023019923017343562
[CV 1/3; 39/50] END C=0.001159924390882601, class_weight=None, dual=True, penalty=l2, tol=0.023019923017343562;, score=0.840 total time=   0.4s
[CV 2/3; 39/50] START C=0.001159924390882601, class_weight=None, dual=True, penalty=l2, tol=0.023019923017343562
[CV 2/3; 39/50] END C=0.001159924390882601, class_weight=None, dual=True, penalty=l2, tol=0.023019923017343562;, score=0.982 total time=   0.4s
[CV 3/3; 39/50] START C=0.001159924390882601, class_weight=None, dual=True, penalty=l2, tol=0.023019923017343562
[CV 3/3; 39/50] END C=0.001159924390882601, class_weight=None, dual=True, penalty=l2, tol=0.023019923017343562;, score=0.955 total time=   0.4s
[CV 1/3; 40/50] START C=0.03874369390027694, class_weight=balanced, dual=False, penalty=l2, tol=0.08999654768577617
[CV 1/3; 40/50] END C=0.03874369390027694, class_weight=balanced, dual=False, penalty=l2, tol=0.08999654768577617;, score=0.652 total time=   0.5s
[CV 2/3; 40/50] START C=0.03874369390027694, class_weight=balanced, dual=False, penalty=l2, tol=0.08999654768577617
[CV 2/3; 40/50] END C=0.03874369390027694, class_weight=balanced, dual=False, penalty=l2, tol=0.08999654768577617;, score=0.991 total time=   0.5s
[CV 3/3; 40/50] START C=0.03874369390027694, class_weight=balanced, dual=False, penalty=l2, tol=0.08999654768577617
[CV 3/3; 40/50] END C=0.03874369390027694, class_weight=balanced, dual=False, penalty=l2, tol=0.08999654768577617;, score=0.961 total time=   0.5s
[CV 1/3; 41/50] START C=0.07446970586139393, class_weight=balanced, dual=True, penalty=l2, tol=0.0013735479468745863
[CV 1/3; 41/50] END C=0.07446970586139393, class_weight=balanced, dual=True, penalty=l2, tol=0.0013735479468745863;, score=0.621 total time=   0.5s
[CV 2/3; 41/50] START C=0.07446970586139393, class_weight=balanced, dual=True, penalty=l2, tol=0.0013735479468745863
[CV 2/3; 41/50] END C=0.07446970586139393, class_weight=balanced, dual=True, penalty=l2, tol=0.0013735479468745863;, score=0.992 total time=   0.5s
[CV 3/3; 41/50] START C=0.07446970586139393, class_weight=balanced, dual=True, penalty=l2, tol=0.0013735479468745863
[CV 3/3; 41/50] END C=0.07446970586139393, class_weight=balanced, dual=True, penalty=l2, tol=0.0013735479468745863;, score=0.967 total time=   0.5s
[CV 1/3; 42/50] START C=0.16002987731780127, class_weight=balanced, dual=False, penalty=l2, tol=0.019920512638943334
[CV 1/3; 42/50] END C=0.16002987731780127, class_weight=balanced, dual=False, penalty=l2, tol=0.019920512638943334;, score=0.585 total time=   0.5s
[CV 2/3; 42/50] START C=0.16002987731780127, class_weight=balanced, dual=False, penalty=l2, tol=0.019920512638943334
[CV 2/3; 42/50] END C=0.16002987731780127, class_weight=balanced, dual=False, penalty=l2, tol=0.019920512638943334;, score=0.991 total time=   0.6s
[CV 3/3; 42/50] START C=0.16002987731780127, class_weight=balanced, dual=False, penalty=l2, tol=0.019920512638943334
[CV 3/3; 42/50] END C=0.16002987731780127, class_weight=balanced, dual=False, penalty=l2, tol=0.019920512638943334;, score=0.963 total time=   0.6s
[CV 1/3; 43/50] START C=0.0011979611795979723, class_weight=balanced, dual=True, penalty=l2, tol=0.002331579244409196
[CV 1/3; 43/50] END C=0.0011979611795979723, class_weight=balanced, dual=True, penalty=l2, tol=0.002331579244409196;, score=0.755 total time=   0.4s
[CV 2/3; 43/50] START C=0.0011979611795979723, class_weight=balanced, dual=True, penalty=l2, tol=0.002331579244409196
[CV 2/3; 43/50] END C=0.0011979611795979723, class_weight=balanced, dual=True, penalty=l2, tol=0.002331579244409196;, score=0.990 total time=   0.4s
[CV 3/3; 43/50] START C=0.0011979611795979723, class_weight=balanced, dual=True, penalty=l2, tol=0.002331579244409196
[CV 3/3; 43/50] END C=0.0011979611795979723, class_weight=balanced, dual=True, penalty=l2, tol=0.002331579244409196;, score=0.961 total time=   0.4s
[CV 1/3; 44/50] START C=1.1745705444535357, class_weight=None, dual=True, penalty=l2, tol=0.0030202662912748447
[CV 1/3; 44/50] END C=1.1745705444535357, class_weight=None, dual=True, penalty=l2, tol=0.0030202662912748447;, score=0.661 total time=   0.6s
[CV 2/3; 44/50] START C=1.1745705444535357, class_weight=None, dual=True, penalty=l2, tol=0.0030202662912748447
[CV 2/3; 44/50] END C=1.1745705444535357, class_weight=None, dual=True, penalty=l2, tol=0.0030202662912748447;, score=0.992 total time=   0.6s
[CV 3/3; 44/50] START C=1.1745705444535357, class_weight=None, dual=True, penalty=l2, tol=0.0030202662912748447
[CV 3/3; 44/50] END C=1.1745705444535357, class_weight=None, dual=True, penalty=l2, tol=0.0030202662912748447;, score=0.965 total time=   0.6s
[CV 1/3; 45/50] START C=0.718496358855664, class_weight=balanced, dual=True, penalty=l2, tol=0.016043192594951777
[CV 1/3; 45/50] END C=0.718496358855664, class_weight=balanced, dual=True, penalty=l2, tol=0.016043192594951777;, score=0.643 total time=   0.6s
[CV 2/3; 45/50] START C=0.718496358855664, class_weight=balanced, dual=True, penalty=l2, tol=0.016043192594951777
[CV 2/3; 45/50] END C=0.718496358855664, class_weight=balanced, dual=True, penalty=l2, tol=0.016043192594951777;, score=0.993 total time=   0.6s
[CV 3/3; 45/50] START C=0.718496358855664, class_weight=balanced, dual=True, penalty=l2, tol=0.016043192594951777
[CV 3/3; 45/50] END C=0.718496358855664, class_weight=balanced, dual=True, penalty=l2, tol=0.016043192594951777;, score=0.967 total time=   0.6s
[CV 1/3; 46/50] START C=0.038380671785084725, class_weight=None, dual=False, penalty=l2, tol=0.0013100725843168078
[CV 1/3; 46/50] END C=0.038380671785084725, class_weight=None, dual=False, penalty=l2, tol=0.0013100725843168078;, score=0.677 total time=   0.5s
[CV 2/3; 46/50] START C=0.038380671785084725, class_weight=None, dual=False, penalty=l2, tol=0.0013100725843168078
[CV 2/3; 46/50] END C=0.038380671785084725, class_weight=None, dual=False, penalty=l2, tol=0.0013100725843168078;, score=0.991 total time=   0.6s
[CV 3/3; 46/50] START C=0.038380671785084725, class_weight=None, dual=False, penalty=l2, tol=0.0013100725843168078
[CV 3/3; 46/50] END C=0.038380671785084725, class_weight=None, dual=False, penalty=l2, tol=0.0013100725843168078;, score=0.967 total time=   0.6s
[CV 1/3; 47/50] START C=0.012459433680745535, class_weight=balanced, dual=True, penalty=l2, tol=0.08676049101830814
[CV 1/3; 47/50] END C=0.012459433680745535, class_weight=balanced, dual=True, penalty=l2, tol=0.08676049101830814;, score=0.656 total time=   0.4s
[CV 2/3; 47/50] START C=0.012459433680745535, class_weight=balanced, dual=True, penalty=l2, tol=0.08676049101830814
[CV 2/3; 47/50] END C=0.012459433680745535, class_weight=balanced, dual=True, penalty=l2, tol=0.08676049101830814;, score=0.991 total time=   0.4s
[CV 3/3; 47/50] START C=0.012459433680745535, class_weight=balanced, dual=True, penalty=l2, tol=0.08676049101830814
[CV 3/3; 47/50] END C=0.012459433680745535, class_weight=balanced, dual=True, penalty=l2, tol=0.08676049101830814;, score=0.965 total time=   0.4s
[CV 1/3; 48/50] START C=0.06411107849812371, class_weight=balanced, dual=False, penalty=l2, tol=0.019157791588555302
[CV 1/3; 48/50] END C=0.06411107849812371, class_weight=balanced, dual=False, penalty=l2, tol=0.019157791588555302;, score=0.618 total time=   0.5s
[CV 2/3; 48/50] START C=0.06411107849812371, class_weight=balanced, dual=False, penalty=l2, tol=0.019157791588555302
[CV 2/3; 48/50] END C=0.06411107849812371, class_weight=balanced, dual=False, penalty=l2, tol=0.019157791588555302;, score=0.991 total time=   0.6s
[CV 3/3; 48/50] START C=0.06411107849812371, class_weight=balanced, dual=False, penalty=l2, tol=0.019157791588555302
[CV 3/3; 48/50] END C=0.06411107849812371, class_weight=balanced, dual=False, penalty=l2, tol=0.019157791588555302;, score=0.963 total time=   0.6s
[CV 1/3; 49/50] START C=0.0926508622978339, class_weight=None, dual=True, penalty=l2, tol=0.014608780124461979
[CV 1/3; 49/50] END C=0.0926508622978339, class_weight=None, dual=True, penalty=l2, tol=0.014608780124461979;, score=0.680 total time=   0.5s
[CV 2/3; 49/50] START C=0.0926508622978339, class_weight=None, dual=True, penalty=l2, tol=0.014608780124461979
[CV 2/3; 49/50] END C=0.0926508622978339, class_weight=None, dual=True, penalty=l2, tol=0.014608780124461979;, score=0.992 total time=   0.5s
[CV 3/3; 49/50] START C=0.0926508622978339, class_weight=None, dual=True, penalty=l2, tol=0.014608780124461979
[CV 3/3; 49/50] END C=0.0926508622978339, class_weight=None, dual=True, penalty=l2, tol=0.014608780124461979;, score=0.968 total time=   0.5s
[CV 1/3; 50/50] START C=0.15842825141966616, class_weight=None, dual=True, penalty=l2, tol=0.03394761206111789
[CV 1/3; 50/50] END C=0.15842825141966616, class_weight=None, dual=True, penalty=l2, tol=0.03394761206111789;, score=0.680 total time=   0.5s
[CV 2/3; 50/50] START C=0.15842825141966616, class_weight=None, dual=True, penalty=l2, tol=0.03394761206111789
[CV 2/3; 50/50] END C=0.15842825141966616, class_weight=None, dual=True, penalty=l2, tol=0.03394761206111789;, score=0.992 total time=   0.5s
[CV 3/3; 50/50] START C=0.15842825141966616, class_weight=None, dual=True, penalty=l2, tol=0.03394761206111789
[CV 3/3; 50/50] END C=0.15842825141966616, class_weight=None, dual=True, penalty=l2, tol=0.03394761206111789;, score=0.967 total time=   0.5s

--- TUNING FINISHED ---
Beste Parameter: {'C': np.float64(0.001248778833652541), 'class_weight': None, 'dual': False, 'penalty': 'l2', 'tol': np.float64(0.054263632503439824)}
Bester CV-Score: 0.9264

--- EVALUATION AUF DEN TESTDATEN ---
Test Accuracy: 0.8664

Macro F1: 0.8426818497454333

--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.8664

                     precision    recall  f1-score   support

             B cell       0.99      0.97      0.98       120
     CD14+ monocyte       1.00      1.00      1.00      2575
        CD4+ T cell       0.80      1.00      0.89      3910
   Cytotoxic T cell       0.94      0.37      0.53      1824
     Dendritic cell       1.00      0.40      0.57         5
      Megakaryocyte       1.00      1.00      1.00         7
Natural killer cell       0.78      0.93      0.85       791
        Plasma cell       0.92      0.94      0.93        49

           accuracy                           0.87      9281
          macro avg       0.93      0.82      0.84      9281
       weighted avg       0.88      0.87      0.85      9281

Random dropout accuracy score 0.8472
Total samples: 9281
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.8652
Feature importance dropout (0.5% features dropped) accuracy score 0.8433
Feature importance dropout (1.0% features dropped) accuracy score 0.8270
Feature importance dropout (2.0% features dropped) accuracy score 0.7979
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8465

                     precision    recall  f1-score   support

             B cell       1.00      0.99      0.99      3959
     CD14+ monocyte       0.89      1.00      0.94      3135
        CD4+ T cell       0.88      0.99      0.93     13664
   Cytotoxic T cell       0.58      0.60      0.59      4839
     Dendritic cell       1.00      0.66      0.79       529
      Megakaryocyte       1.00      0.65      0.79        86
Natural killer cell       0.86      0.23      0.36      2751
        Plasma cell       0.56      0.96      0.71        23

           accuracy                           0.85     28986
          macro avg       0.85      0.76      0.76     28986
       weighted avg       0.85      0.85      0.83     28986

Random dropout accuracy score 0.8402
Total samples: 28986
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.8474
Feature importance dropout (0.5% features dropped) accuracy score 0.8333
Feature importance dropout (1.0% features dropped) accuracy score 0.8222
Feature importance dropout (2.0% features dropped) accuracy score 0.7831
=== JOB_STATISTICS ===
=== current date     : Mon Jun 29 00:30:25 CEST 2026
= Job-ID             : 11997759 on woody
= Job-Name           : autoencoder_linsvc
= Job-Command        : /home/hpc/iwbn/iwbn133h/submit_autoencoder_linsvc_v1.sh
= Initial workdir    : /home/hpc/iwbn/iwbn133h
= Queue/Partition    : work
= Slurm account      : iwbn with QOS=normal
= Features           : icx
= Requested resources:  for 17:00:00
= Elapsed runtime    : 02:13:43
= Total RAM usage    : 19.0 GiB of requested  GiB (%)   
= Node list          : w2214
= Subm/Elig/Start/End: 2026-06-28T22:16:41 / 2026-06-28T22:16:41 / 2026-06-28T22:16:42 / 2026-06-29T00:30:25
======================
=== Quota infos ======
    Path                 Used     SoftQ    HardQ    Gracetime  Filec    FileQ    FiHaQ    FileGrace    
    /home/woody           982.1M  1000.0G  1500.0G        N/A  29,019    5,000K   7,500K        N/A    
    /home/hpc              86.2G   104.9G   209.7G        N/A     139K     500K   1,000K        N/A    
    /home/vault             0.0K  1048.6G  2097.2G        N/A       1      200K     400K        N/A    
