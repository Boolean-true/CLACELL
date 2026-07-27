### Starting TaskPrologue of job 11997741 on w2333 at Sun Jun 28 21:58:51 CEST 2026
#   SLURM_JOB_NODELIST=w2333
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
Epoch [1/150], Loss: 0.9418
Epoch [10/150], Loss: 0.9062
Epoch [20/150], Loss: 0.8988
Early Stopping after [29/150] Epochs!

Extract robust features...
Starte automatische Hyperparametersuche auf dem Latent Space...
Fitting 3 folds for each of 50 candidates, totalling 150 fits
[CV 1/3; 1/50] START C=0.020122468026732516, class_weight=None, l1_ratio=0.5, tol=0.003585449263385848
[CV 1/3; 1/50] END C=0.020122468026732516, class_weight=None, l1_ratio=0.5, tol=0.003585449263385848;, score=0.946 total time=   3.5s
[CV 2/3; 1/50] START C=0.020122468026732516, class_weight=None, l1_ratio=0.5, tol=0.003585449263385848
[CV 2/3; 1/50] END C=0.020122468026732516, class_weight=None, l1_ratio=0.5, tol=0.003585449263385848;, score=0.985 total time=   5.2s
[CV 3/3; 1/50] START C=0.020122468026732516, class_weight=None, l1_ratio=0.5, tol=0.003585449263385848
[CV 3/3; 1/50] END C=0.020122468026732516, class_weight=None, l1_ratio=0.5, tol=0.003585449263385848;, score=0.951 total time=   4.0s
[CV 1/3; 2/50] START C=0.005842691439715142, class_weight=balanced, l1_ratio=0.0, tol=0.02967100914211511
[CV 1/3; 2/50] END C=0.005842691439715142, class_weight=balanced, l1_ratio=0.0, tol=0.02967100914211511;, score=0.921 total time=   0.7s
[CV 2/3; 2/50] START C=0.005842691439715142, class_weight=balanced, l1_ratio=0.0, tol=0.02967100914211511
[CV 2/3; 2/50] END C=0.005842691439715142, class_weight=balanced, l1_ratio=0.0, tol=0.02967100914211511;, score=0.982 total time=   0.7s
[CV 3/3; 2/50] START C=0.005842691439715142, class_weight=balanced, l1_ratio=0.0, tol=0.02967100914211511
[CV 3/3; 2/50] END C=0.005842691439715142, class_weight=balanced, l1_ratio=0.0, tol=0.02967100914211511;, score=0.949 total time=   0.7s
[CV 1/3; 3/50] START C=0.09596144459163233, class_weight=balanced, l1_ratio=0.5, tol=0.01236904538417259
[CV 1/3; 3/50] END C=0.09596144459163233, class_weight=balanced, l1_ratio=0.5, tol=0.01236904538417259;, score=0.921 total time=   1.5s
[CV 2/3; 3/50] START C=0.09596144459163233, class_weight=balanced, l1_ratio=0.5, tol=0.01236904538417259
[CV 2/3; 3/50] END C=0.09596144459163233, class_weight=balanced, l1_ratio=0.5, tol=0.01236904538417259;, score=0.984 total time=   1.5s
[CV 3/3; 3/50] START C=0.09596144459163233, class_weight=balanced, l1_ratio=0.5, tol=0.01236904538417259
[CV 3/3; 3/50] END C=0.09596144459163233, class_weight=balanced, l1_ratio=0.5, tol=0.01236904538417259;, score=0.952 total time=   1.4s
[CV 1/3; 4/50] START C=0.05196685174951564, class_weight=None, l1_ratio=1.0, tol=0.001661770419927145
[CV 1/3; 4/50] END C=0.05196685174951564, class_weight=None, l1_ratio=1.0, tol=0.001661770419927145;, score=0.944 total time=   6.4s
[CV 2/3; 4/50] START C=0.05196685174951564, class_weight=None, l1_ratio=1.0, tol=0.001661770419927145
[CV 2/3; 4/50] END C=0.05196685174951564, class_weight=None, l1_ratio=1.0, tol=0.001661770419927145;, score=0.986 total time=  10.0s
[CV 3/3; 4/50] START C=0.05196685174951564, class_weight=None, l1_ratio=1.0, tol=0.001661770419927145
[CV 3/3; 4/50] END C=0.05196685174951564, class_weight=None, l1_ratio=1.0, tol=0.001661770419927145;, score=0.953 total time=   7.6s
[CV 1/3; 5/50] START C=1.9711954739253938, class_weight=balanced, l1_ratio=0.0, tol=0.0013655931161075426
[CV 1/3; 5/50] END C=1.9711954739253938, class_weight=balanced, l1_ratio=0.0, tol=0.0013655931161075426;, score=0.917 total time=   7.2s
[CV 2/3; 5/50] START C=1.9711954739253938, class_weight=balanced, l1_ratio=0.0, tol=0.0013655931161075426
[CV 2/3; 5/50] END C=1.9711954739253938, class_weight=balanced, l1_ratio=0.0, tol=0.0013655931161075426;, score=0.988 total time=   7.3s
[CV 3/3; 5/50] START C=1.9711954739253938, class_weight=balanced, l1_ratio=0.0, tol=0.0013655931161075426
[CV 3/3; 5/50] END C=1.9711954739253938, class_weight=balanced, l1_ratio=0.0, tol=0.0013655931161075426;, score=0.956 total time=   7.3s
[CV 1/3; 6/50] START C=0.013869760322702795, class_weight=balanced, l1_ratio=0.5, tol=0.032431724351875836
[CV 1/3; 6/50] END C=0.013869760322702795, class_weight=balanced, l1_ratio=0.5, tol=0.032431724351875836;, score=0.920 total time=   0.8s
[CV 2/3; 6/50] START C=0.013869760322702795, class_weight=balanced, l1_ratio=0.5, tol=0.032431724351875836
[CV 2/3; 6/50] END C=0.013869760322702795, class_weight=balanced, l1_ratio=0.5, tol=0.032431724351875836;, score=0.983 total time=   1.3s
[CV 3/3; 6/50] START C=0.013869760322702795, class_weight=balanced, l1_ratio=0.5, tol=0.032431724351875836
[CV 3/3; 6/50] END C=0.013869760322702795, class_weight=balanced, l1_ratio=0.5, tol=0.032431724351875836;, score=0.952 total time=   1.0s
[CV 1/3; 7/50] START C=0.0027496262033892523, class_weight=balanced, l1_ratio=1.0, tol=0.003463958748857518
[CV 1/3; 7/50] END C=0.0027496262033892523, class_weight=balanced, l1_ratio=1.0, tol=0.003463958748857518;, score=0.918 total time=   6.7s
[CV 2/3; 7/50] START C=0.0027496262033892523, class_weight=balanced, l1_ratio=1.0, tol=0.003463958748857518
[CV 2/3; 7/50] END C=0.0027496262033892523, class_weight=balanced, l1_ratio=1.0, tol=0.003463958748857518;, score=0.979 total time=  10.5s
[CV 3/3; 7/50] START C=0.0027496262033892523, class_weight=balanced, l1_ratio=1.0, tol=0.003463958748857518
[CV 3/3; 7/50] END C=0.0027496262033892523, class_weight=balanced, l1_ratio=1.0, tol=0.003463958748857518;, score=0.939 total time=   7.8s
[CV 1/3; 8/50] START C=1.4248874086730465, class_weight=balanced, l1_ratio=0.0, tol=0.025510916590861937
[CV 1/3; 8/50] END C=1.4248874086730465, class_weight=balanced, l1_ratio=0.0, tol=0.025510916590861937;, score=0.921 total time=   0.7s
[CV 2/3; 8/50] START C=1.4248874086730465, class_weight=balanced, l1_ratio=0.0, tol=0.025510916590861937
[CV 2/3; 8/50] END C=1.4248874086730465, class_weight=balanced, l1_ratio=0.0, tol=0.025510916590861937;, score=0.982 total time=   0.8s
[CV 3/3; 8/50] START C=1.4248874086730465, class_weight=balanced, l1_ratio=0.0, tol=0.025510916590861937
[CV 3/3; 8/50] END C=1.4248874086730465, class_weight=balanced, l1_ratio=0.0, tol=0.025510916590861937;, score=0.951 total time=   0.7s
[CV 1/3; 9/50] START C=1.0808283326251567, class_weight=None, l1_ratio=0.5, tol=0.013840238362147126
[CV 1/3; 9/50] END C=1.0808283326251567, class_weight=None, l1_ratio=0.5, tol=0.013840238362147126;, score=0.947 total time=   1.1s
[CV 2/3; 9/50] START C=1.0808283326251567, class_weight=None, l1_ratio=0.5, tol=0.013840238362147126
[CV 2/3; 9/50] END C=1.0808283326251567, class_weight=None, l1_ratio=0.5, tol=0.013840238362147126;, score=0.977 total time=   1.3s
[CV 3/3; 9/50] START C=1.0808283326251567, class_weight=None, l1_ratio=0.5, tol=0.013840238362147126
[CV 3/3; 9/50] END C=1.0808283326251567, class_weight=None, l1_ratio=0.5, tol=0.013840238362147126;, score=0.948 total time=   1.3s
[CV 1/3; 10/50] START C=0.17934604867888912, class_weight=None, l1_ratio=0.0, tol=0.006005698135601735
[CV 1/3; 10/50] END C=0.17934604867888912, class_weight=None, l1_ratio=0.0, tol=0.006005698135601735;, score=0.947 total time=   1.4s
[CV 2/3; 10/50] START C=0.17934604867888912, class_weight=None, l1_ratio=0.0, tol=0.006005698135601735
[CV 2/3; 10/50] END C=0.17934604867888912, class_weight=None, l1_ratio=0.0, tol=0.006005698135601735;, score=0.985 total time=   1.9s
[CV 3/3; 10/50] START C=0.17934604867888912, class_weight=None, l1_ratio=0.0, tol=0.006005698135601735
[CV 3/3; 10/50] END C=0.17934604867888912, class_weight=None, l1_ratio=0.0, tol=0.006005698135601735;, score=0.951 total time=   1.5s
[CV 1/3; 11/50] START C=0.001259232707089496, class_weight=balanced, l1_ratio=1.0, tol=0.0021386344804048855
[CV 1/3; 11/50] END C=0.001259232707089496, class_weight=balanced, l1_ratio=1.0, tol=0.0021386344804048855;, score=0.921 total time=  15.8s
[CV 2/3; 11/50] START C=0.001259232707089496, class_weight=balanced, l1_ratio=1.0, tol=0.0021386344804048855
[CV 2/3; 11/50] END C=0.001259232707089496, class_weight=balanced, l1_ratio=1.0, tol=0.0021386344804048855;, score=0.970 total time=  19.8s
[CV 3/3; 11/50] START C=0.001259232707089496, class_weight=balanced, l1_ratio=1.0, tol=0.0021386344804048855
[CV 3/3; 11/50] END C=0.001259232707089496, class_weight=balanced, l1_ratio=1.0, tol=0.0021386344804048855;, score=0.929 total time=  21.4s
[CV 1/3; 12/50] START C=0.21508788516457183, class_weight=balanced, l1_ratio=0.5, tol=0.0030450699852962435
[CV 1/3; 12/50] END C=0.21508788516457183, class_weight=balanced, l1_ratio=0.5, tol=0.0030450699852962435;, score=0.919 total time=   4.9s
[CV 2/3; 12/50] START C=0.21508788516457183, class_weight=balanced, l1_ratio=0.5, tol=0.0030450699852962435
[CV 2/3; 12/50] END C=0.21508788516457183, class_weight=balanced, l1_ratio=0.5, tol=0.0030450699852962435;, score=0.987 total time=   4.8s
[CV 3/3; 12/50] START C=0.21508788516457183, class_weight=balanced, l1_ratio=0.5, tol=0.0030450699852962435
[CV 3/3; 12/50] END C=0.21508788516457183, class_weight=balanced, l1_ratio=0.5, tol=0.0030450699852962435;, score=0.954 total time=   4.8s
[CV 1/3; 13/50] START C=1.138724146058488, class_weight=None, l1_ratio=0.0, tol=0.008432601813665067
[CV 1/3; 13/50] END C=1.138724146058488, class_weight=None, l1_ratio=0.0, tol=0.008432601813665067;, score=0.948 total time=   1.1s
[CV 2/3; 13/50] START C=1.138724146058488, class_weight=None, l1_ratio=0.0, tol=0.008432601813665067
[CV 2/3; 13/50] END C=1.138724146058488, class_weight=None, l1_ratio=0.0, tol=0.008432601813665067;, score=0.983 total time=   1.3s
[CV 3/3; 13/50] START C=1.138724146058488, class_weight=None, l1_ratio=0.0, tol=0.008432601813665067
[CV 3/3; 13/50] END C=1.138724146058488, class_weight=None, l1_ratio=0.0, tol=0.008432601813665067;, score=0.950 total time=   1.1s
[CV 1/3; 14/50] START C=0.4027511960159287, class_weight=balanced, l1_ratio=0.0, tol=0.009653700235592116
[CV 1/3; 14/50] END C=0.4027511960159287, class_weight=balanced, l1_ratio=0.0, tol=0.009653700235592116;, score=0.920 total time=   1.2s
[CV 2/3; 14/50] START C=0.4027511960159287, class_weight=balanced, l1_ratio=0.0, tol=0.009653700235592116
[CV 2/3; 14/50] END C=0.4027511960159287, class_weight=balanced, l1_ratio=0.0, tol=0.009653700235592116;, score=0.985 total time=   1.2s
[CV 3/3; 14/50] START C=0.4027511960159287, class_weight=balanced, l1_ratio=0.0, tol=0.009653700235592116
[CV 3/3; 14/50] END C=0.4027511960159287, class_weight=balanced, l1_ratio=0.0, tol=0.009653700235592116;, score=0.951 total time=   1.1s
[CV 1/3; 15/50] START C=0.012619823958212874, class_weight=None, l1_ratio=0.5, tol=0.0028391986204013343
[CV 1/3; 15/50] END C=0.012619823958212874, class_weight=None, l1_ratio=0.5, tol=0.0028391986204013343;, score=0.947 total time=   4.6s
[CV 2/3; 15/50] START C=0.012619823958212874, class_weight=None, l1_ratio=0.5, tol=0.0028391986204013343
[CV 2/3; 15/50] END C=0.012619823958212874, class_weight=None, l1_ratio=0.5, tol=0.0028391986204013343;, score=0.984 total time=   7.3s
[CV 3/3; 15/50] START C=0.012619823958212874, class_weight=None, l1_ratio=0.5, tol=0.0028391986204013343
[CV 3/3; 15/50] END C=0.012619823958212874, class_weight=None, l1_ratio=0.5, tol=0.0028391986204013343;, score=0.951 total time=   4.8s
[CV 1/3; 16/50] START C=0.009420334070844, class_weight=None, l1_ratio=0.0, tol=0.06340430530932345
[CV 1/3; 16/50] END C=0.009420334070844, class_weight=None, l1_ratio=0.0, tol=0.06340430530932345;, score=0.936 total time=   0.5s
[CV 2/3; 16/50] START C=0.009420334070844, class_weight=None, l1_ratio=0.0, tol=0.06340430530932345
[CV 2/3; 16/50] END C=0.009420334070844, class_weight=None, l1_ratio=0.0, tol=0.06340430530932345;, score=0.959 total time=   0.5s
[CV 3/3; 16/50] START C=0.009420334070844, class_weight=None, l1_ratio=0.0, tol=0.06340430530932345
[CV 3/3; 16/50] END C=0.009420334070844, class_weight=None, l1_ratio=0.0, tol=0.06340430530932345;, score=0.936 total time=   0.5s
[CV 1/3; 17/50] START C=0.010436924952733136, class_weight=balanced, l1_ratio=0.0, tol=0.00239082948268903
[CV 1/3; 17/50] END C=0.010436924952733136, class_weight=balanced, l1_ratio=0.0, tol=0.00239082948268903;, score=0.919 total time=   3.1s
[CV 2/3; 17/50] START C=0.010436924952733136, class_weight=balanced, l1_ratio=0.0, tol=0.00239082948268903
[CV 2/3; 17/50] END C=0.010436924952733136, class_weight=balanced, l1_ratio=0.0, tol=0.00239082948268903;, score=0.987 total time=   3.7s
[CV 3/3; 17/50] START C=0.010436924952733136, class_weight=balanced, l1_ratio=0.0, tol=0.00239082948268903
[CV 3/3; 17/50] END C=0.010436924952733136, class_weight=balanced, l1_ratio=0.0, tol=0.00239082948268903;, score=0.954 total time=   3.0s
[CV 1/3; 18/50] START C=0.0030722737983497972, class_weight=None, l1_ratio=0.0, tol=0.018125449832291873
[CV 1/3; 18/50] END C=0.0030722737983497972, class_weight=None, l1_ratio=0.0, tol=0.018125449832291873;, score=0.946 total time=   0.7s
[CV 2/3; 18/50] START C=0.0030722737983497972, class_weight=None, l1_ratio=0.0, tol=0.018125449832291873
[CV 2/3; 18/50] END C=0.0030722737983497972, class_weight=None, l1_ratio=0.0, tol=0.018125449832291873;, score=0.974 total time=   0.7s
[CV 3/3; 18/50] START C=0.0030722737983497972, class_weight=None, l1_ratio=0.0, tol=0.018125449832291873
[CV 3/3; 18/50] END C=0.0030722737983497972, class_weight=None, l1_ratio=0.0, tol=0.018125449832291873;, score=0.945 total time=   0.7s
[CV 1/3; 19/50] START C=0.36102530604759553, class_weight=balanced, l1_ratio=1.0, tol=0.0943571581131058
[CV 1/3; 19/50] END C=0.36102530604759553, class_weight=balanced, l1_ratio=1.0, tol=0.0943571581131058;, score=0.914 total time=   0.6s
[CV 2/3; 19/50] START C=0.36102530604759553, class_weight=balanced, l1_ratio=1.0, tol=0.0943571581131058
[CV 2/3; 19/50] END C=0.36102530604759553, class_weight=balanced, l1_ratio=1.0, tol=0.0943571581131058;, score=0.981 total time=   0.8s
[CV 3/3; 19/50] START C=0.36102530604759553, class_weight=balanced, l1_ratio=1.0, tol=0.0943571581131058
[CV 3/3; 19/50] END C=0.36102530604759553, class_weight=balanced, l1_ratio=1.0, tol=0.0943571581131058;, score=0.943 total time=   0.6s
[CV 1/3; 20/50] START C=0.06409921961140704, class_weight=None, l1_ratio=0.0, tol=0.003343332010464328
[CV 1/3; 20/50] END C=0.06409921961140704, class_weight=None, l1_ratio=0.0, tol=0.003343332010464328;, score=0.947 total time=   2.6s
[CV 2/3; 20/50] START C=0.06409921961140704, class_weight=None, l1_ratio=0.0, tol=0.003343332010464328
[CV 2/3; 20/50] END C=0.06409921961140704, class_weight=None, l1_ratio=0.0, tol=0.003343332010464328;, score=0.986 total time=   3.6s
[CV 3/3; 20/50] START C=0.06409921961140704, class_weight=None, l1_ratio=0.0, tol=0.003343332010464328
[CV 3/3; 20/50] END C=0.06409921961140704, class_weight=None, l1_ratio=0.0, tol=0.003343332010464328;, score=0.953 total time=   2.5s
[CV 1/3; 21/50] START C=1.3904462997440663, class_weight=balanced, l1_ratio=0.0, tol=0.009279706077312903
[CV 1/3; 21/50] END C=1.3904462997440663, class_weight=balanced, l1_ratio=0.0, tol=0.009279706077312903;, score=0.920 total time=   1.2s
[CV 2/3; 21/50] START C=1.3904462997440663, class_weight=balanced, l1_ratio=0.0, tol=0.009279706077312903
[CV 2/3; 21/50] END C=1.3904462997440663, class_weight=balanced, l1_ratio=0.0, tol=0.009279706077312903;, score=0.985 total time=   1.2s
[CV 3/3; 21/50] START C=1.3904462997440663, class_weight=balanced, l1_ratio=0.0, tol=0.009279706077312903
[CV 3/3; 21/50] END C=1.3904462997440663, class_weight=balanced, l1_ratio=0.0, tol=0.009279706077312903;, score=0.952 total time=   1.1s
[CV 1/3; 22/50] START C=1.4752441316340505, class_weight=None, l1_ratio=1.0, tol=0.03984220190282987
[CV 1/3; 22/50] END C=1.4752441316340505, class_weight=None, l1_ratio=1.0, tol=0.03984220190282987;, score=0.939 total time=   0.7s
[CV 2/3; 22/50] START C=1.4752441316340505, class_weight=None, l1_ratio=1.0, tol=0.03984220190282987
[CV 2/3; 22/50] END C=1.4752441316340505, class_weight=None, l1_ratio=1.0, tol=0.03984220190282987;, score=0.963 total time=   0.6s
[CV 3/3; 22/50] START C=1.4752441316340505, class_weight=None, l1_ratio=1.0, tol=0.03984220190282987
[CV 3/3; 22/50] END C=1.4752441316340505, class_weight=None, l1_ratio=1.0, tol=0.03984220190282987;, score=0.938 total time=   0.6s
[CV 1/3; 23/50] START C=0.36731298879455143, class_weight=balanced, l1_ratio=0.5, tol=0.0012724988466906778
[CV 1/3; 23/50] END C=0.36731298879455143, class_weight=balanced, l1_ratio=0.5, tol=0.0012724988466906778;, score=0.917 total time=  12.3s
[CV 2/3; 23/50] START C=0.36731298879455143, class_weight=balanced, l1_ratio=0.5, tol=0.0012724988466906778
[CV 2/3; 23/50] END C=0.36731298879455143, class_weight=balanced, l1_ratio=0.5, tol=0.0012724988466906778;, score=0.988 total time=  12.3s
[CV 3/3; 23/50] START C=0.36731298879455143, class_weight=balanced, l1_ratio=0.5, tol=0.0012724988466906778
[CV 3/3; 23/50] END C=0.36731298879455143, class_weight=balanced, l1_ratio=0.5, tol=0.0012724988466906778;, score=0.955 total time=  14.7s
[CV 1/3; 24/50] START C=0.002335364302823669, class_weight=balanced, l1_ratio=1.0, tol=0.024718284116515915
[CV 1/3; 24/50] END C=0.002335364302823669, class_weight=balanced, l1_ratio=1.0, tol=0.024718284116515915;, score=0.921 total time=   1.3s
[CV 2/3; 24/50] START C=0.002335364302823669, class_weight=balanced, l1_ratio=1.0, tol=0.024718284116515915
[CV 2/3; 24/50] END C=0.002335364302823669, class_weight=balanced, l1_ratio=1.0, tol=0.024718284116515915;, score=0.980 total time=   1.7s
[CV 3/3; 24/50] START C=0.002335364302823669, class_weight=balanced, l1_ratio=1.0, tol=0.024718284116515915
[CV 3/3; 24/50] END C=0.002335364302823669, class_weight=balanced, l1_ratio=1.0, tol=0.024718284116515915;, score=0.940 total time=   1.5s
[CV 1/3; 25/50] START C=0.0015982554373313994, class_weight=balanced, l1_ratio=0.5, tol=0.016465350690765684
[CV 1/3; 25/50] END C=0.0015982554373313994, class_weight=balanced, l1_ratio=0.5, tol=0.016465350690765684;, score=0.920 total time=   1.6s
[CV 2/3; 25/50] START C=0.0015982554373313994, class_weight=balanced, l1_ratio=0.5, tol=0.016465350690765684
[CV 2/3; 25/50] END C=0.0015982554373313994, class_weight=balanced, l1_ratio=0.5, tol=0.016465350690765684;, score=0.981 total time=   3.0s
[CV 3/3; 25/50] START C=0.0015982554373313994, class_weight=balanced, l1_ratio=0.5, tol=0.016465350690765684
[CV 3/3; 25/50] END C=0.0015982554373313994, class_weight=balanced, l1_ratio=0.5, tol=0.016465350690765684;, score=0.941 total time=   2.4s
[CV 1/3; 26/50] START C=0.36000727761504986, class_weight=None, l1_ratio=0.0, tol=0.0018296145892740413
[CV 1/3; 26/50] END C=0.36000727761504986, class_weight=None, l1_ratio=0.0, tol=0.0018296145892740413;, score=0.942 total time=   4.9s
[CV 2/3; 26/50] START C=0.36000727761504986, class_weight=None, l1_ratio=0.0, tol=0.0018296145892740413
[CV 2/3; 26/50] END C=0.36000727761504986, class_weight=None, l1_ratio=0.0, tol=0.0018296145892740413;, score=0.987 total time=   5.2s
[CV 3/3; 26/50] START C=0.36000727761504986, class_weight=None, l1_ratio=0.0, tol=0.0018296145892740413
[CV 3/3; 26/50] END C=0.36000727761504986, class_weight=None, l1_ratio=0.0, tol=0.0018296145892740413;, score=0.956 total time=   4.6s
[CV 1/3; 27/50] START C=0.08969950401577952, class_weight=balanced, l1_ratio=0.0, tol=0.0713449516288808
[CV 1/3; 27/50] END C=0.08969950401577952, class_weight=balanced, l1_ratio=0.0, tol=0.0713449516288808;, score=0.917 total time=   0.5s
[CV 2/3; 27/50] START C=0.08969950401577952, class_weight=balanced, l1_ratio=0.0, tol=0.0713449516288808
[CV 2/3; 27/50] END C=0.08969950401577952, class_weight=balanced, l1_ratio=0.0, tol=0.0713449516288808;, score=0.979 total time=   0.6s
[CV 3/3; 27/50] START C=0.08969950401577952, class_weight=balanced, l1_ratio=0.0, tol=0.0713449516288808
[CV 3/3; 27/50] END C=0.08969950401577952, class_weight=balanced, l1_ratio=0.0, tol=0.0713449516288808;, score=0.950 total time=   0.6s
[CV 1/3; 28/50] START C=0.7229347506917322, class_weight=balanced, l1_ratio=0.0, tol=0.002504466576203216
[CV 1/3; 28/50] END C=0.7229347506917322, class_weight=balanced, l1_ratio=0.0, tol=0.002504466576203216;, score=0.918 total time=   3.9s
[CV 2/3; 28/50] START C=0.7229347506917322, class_weight=balanced, l1_ratio=0.0, tol=0.002504466576203216
[CV 2/3; 28/50] END C=0.7229347506917322, class_weight=balanced, l1_ratio=0.0, tol=0.002504466576203216;, score=0.987 total time=   4.0s
[CV 3/3; 28/50] START C=0.7229347506917322, class_weight=balanced, l1_ratio=0.0, tol=0.002504466576203216
[CV 3/3; 28/50] END C=0.7229347506917322, class_weight=balanced, l1_ratio=0.0, tol=0.002504466576203216;, score=0.954 total time=   2.8s
[CV 1/3; 29/50] START C=1.2763484275367711, class_weight=balanced, l1_ratio=0.0, tol=0.003342616567506176
[CV 1/3; 29/50] END C=1.2763484275367711, class_weight=balanced, l1_ratio=0.0, tol=0.003342616567506176;, score=0.921 total time=   2.5s
[CV 2/3; 29/50] START C=1.2763484275367711, class_weight=balanced, l1_ratio=0.0, tol=0.003342616567506176
[CV 2/3; 29/50] END C=1.2763484275367711, class_weight=balanced, l1_ratio=0.0, tol=0.003342616567506176;, score=0.987 total time=   2.9s
[CV 3/3; 29/50] START C=1.2763484275367711, class_weight=balanced, l1_ratio=0.0, tol=0.003342616567506176
[CV 3/3; 29/50] END C=1.2763484275367711, class_weight=balanced, l1_ratio=0.0, tol=0.003342616567506176;, score=0.953 total time=   2.6s
[CV 1/3; 30/50] START C=0.013152196348512555, class_weight=balanced, l1_ratio=1.0, tol=0.0033866628532728815
[CV 1/3; 30/50] END C=0.013152196348512555, class_weight=balanced, l1_ratio=1.0, tol=0.0033866628532728815;, score=0.919 total time=   4.2s
[CV 2/3; 30/50] START C=0.013152196348512555, class_weight=balanced, l1_ratio=1.0, tol=0.0033866628532728815
[CV 2/3; 30/50] END C=0.013152196348512555, class_weight=balanced, l1_ratio=1.0, tol=0.0033866628532728815;, score=0.986 total time=   5.7s
[CV 3/3; 30/50] START C=0.013152196348512555, class_weight=balanced, l1_ratio=1.0, tol=0.0033866628532728815
[CV 3/3; 30/50] END C=0.013152196348512555, class_weight=balanced, l1_ratio=1.0, tol=0.0033866628532728815;, score=0.952 total time=   4.5s
[CV 1/3; 31/50] START C=0.8146626034761146, class_weight=None, l1_ratio=0.0, tol=0.0038740375247455225
[CV 1/3; 31/50] END C=0.8146626034761146, class_weight=None, l1_ratio=0.0, tol=0.0038740375247455225;, score=0.947 total time=   2.3s
[CV 2/3; 31/50] START C=0.8146626034761146, class_weight=None, l1_ratio=0.0, tol=0.0038740375247455225
[CV 2/3; 31/50] END C=0.8146626034761146, class_weight=None, l1_ratio=0.0, tol=0.0038740375247455225;, score=0.986 total time=   2.8s
[CV 3/3; 31/50] START C=0.8146626034761146, class_weight=None, l1_ratio=0.0, tol=0.0038740375247455225
[CV 3/3; 31/50] END C=0.8146626034761146, class_weight=None, l1_ratio=0.0, tol=0.0038740375247455225;, score=0.953 total time=   2.3s
[CV 1/3; 32/50] START C=0.04445664814505041, class_weight=balanced, l1_ratio=1.0, tol=0.003964854861854192
[CV 1/3; 32/50] END C=0.04445664814505041, class_weight=balanced, l1_ratio=1.0, tol=0.003964854861854192;, score=0.920 total time=   3.4s
[CV 2/3; 32/50] START C=0.04445664814505041, class_weight=balanced, l1_ratio=1.0, tol=0.003964854861854192
[CV 2/3; 32/50] END C=0.04445664814505041, class_weight=balanced, l1_ratio=1.0, tol=0.003964854861854192;, score=0.986 total time=   3.8s
[CV 3/3; 32/50] START C=0.04445664814505041, class_weight=balanced, l1_ratio=1.0, tol=0.003964854861854192
[CV 3/3; 32/50] END C=0.04445664814505041, class_weight=balanced, l1_ratio=1.0, tol=0.003964854861854192;, score=0.955 total time=   3.7s
[CV 1/3; 33/50] START C=0.18992775640763848, class_weight=balanced, l1_ratio=0.0, tol=0.022794845006157017
[CV 1/3; 33/50] END C=0.18992775640763848, class_weight=balanced, l1_ratio=0.0, tol=0.022794845006157017;, score=0.921 total time=   0.7s
[CV 2/3; 33/50] START C=0.18992775640763848, class_weight=balanced, l1_ratio=0.0, tol=0.022794845006157017
[CV 2/3; 33/50] END C=0.18992775640763848, class_weight=balanced, l1_ratio=0.0, tol=0.022794845006157017;, score=0.983 total time=   0.9s
[CV 3/3; 33/50] START C=0.18992775640763848, class_weight=balanced, l1_ratio=0.0, tol=0.022794845006157017
[CV 3/3; 33/50] END C=0.18992775640763848, class_weight=balanced, l1_ratio=0.0, tol=0.022794845006157017;, score=0.950 total time=   0.7s
[CV 1/3; 34/50] START C=0.004330717470036612, class_weight=None, l1_ratio=1.0, tol=0.020481299399489228
[CV 1/3; 34/50] END C=0.004330717470036612, class_weight=None, l1_ratio=1.0, tol=0.020481299399489228;, score=0.937 total time=   0.9s
[CV 2/3; 34/50] START C=0.004330717470036612, class_weight=None, l1_ratio=1.0, tol=0.020481299399489228
[CV 2/3; 34/50] END C=0.004330717470036612, class_weight=None, l1_ratio=1.0, tol=0.020481299399489228;, score=0.961 total time=   0.9s
[CV 3/3; 34/50] START C=0.004330717470036612, class_weight=None, l1_ratio=1.0, tol=0.020481299399489228
[CV 3/3; 34/50] END C=0.004330717470036612, class_weight=None, l1_ratio=1.0, tol=0.020481299399489228;, score=0.937 total time=   1.2s
[CV 1/3; 35/50] START C=0.37725279760803704, class_weight=balanced, l1_ratio=0.0, tol=0.00211290273222105
[CV 1/3; 35/50] END C=0.37725279760803704, class_weight=balanced, l1_ratio=0.0, tol=0.00211290273222105;, score=0.918 total time=   4.0s
[CV 2/3; 35/50] START C=0.37725279760803704, class_weight=balanced, l1_ratio=0.0, tol=0.00211290273222105
[CV 2/3; 35/50] END C=0.37725279760803704, class_weight=balanced, l1_ratio=0.0, tol=0.00211290273222105;, score=0.987 total time=   4.0s
[CV 3/3; 35/50] START C=0.37725279760803704, class_weight=balanced, l1_ratio=0.0, tol=0.00211290273222105
[CV 3/3; 35/50] END C=0.37725279760803704, class_weight=balanced, l1_ratio=0.0, tol=0.00211290273222105;, score=0.954 total time=   3.8s
[CV 1/3; 36/50] START C=0.004560289925980964, class_weight=None, l1_ratio=1.0, tol=0.0031112803716672826
[CV 1/3; 36/50] END C=0.004560289925980964, class_weight=None, l1_ratio=1.0, tol=0.0031112803716672826;, score=0.939 total time=   4.7s
[CV 2/3; 36/50] START C=0.004560289925980964, class_weight=None, l1_ratio=1.0, tol=0.0031112803716672826
[CV 2/3; 36/50] END C=0.004560289925980964, class_weight=None, l1_ratio=1.0, tol=0.0031112803716672826;, score=0.971 total time=   6.2s
[CV 3/3; 36/50] START C=0.004560289925980964, class_weight=None, l1_ratio=1.0, tol=0.0031112803716672826
[CV 3/3; 36/50] END C=0.004560289925980964, class_weight=None, l1_ratio=1.0, tol=0.0031112803716672826;, score=0.941 total time=   4.8s
[CV 1/3; 37/50] START C=0.45847571182560704, class_weight=balanced, l1_ratio=0.5, tol=0.004158090128216652
[CV 1/3; 37/50] END C=0.45847571182560704, class_weight=balanced, l1_ratio=0.5, tol=0.004158090128216652;, score=0.920 total time=   3.5s
[CV 2/3; 37/50] START C=0.45847571182560704, class_weight=balanced, l1_ratio=0.5, tol=0.004158090128216652
[CV 2/3; 37/50] END C=0.45847571182560704, class_weight=balanced, l1_ratio=0.5, tol=0.004158090128216652;, score=0.986 total time=   3.7s
[CV 3/3; 37/50] START C=0.45847571182560704, class_weight=balanced, l1_ratio=0.5, tol=0.004158090128216652
[CV 3/3; 37/50] END C=0.45847571182560704, class_weight=balanced, l1_ratio=0.5, tol=0.004158090128216652;, score=0.954 total time=   3.6s
[CV 1/3; 38/50] START C=0.058740732771874166, class_weight=balanced, l1_ratio=1.0, tol=0.0010290226777727477
[CV 1/3; 38/50] END C=0.058740732771874166, class_weight=balanced, l1_ratio=1.0, tol=0.0010290226777727477;, score=0.917 total time=  10.3s
[CV 2/3; 38/50] START C=0.058740732771874166, class_weight=balanced, l1_ratio=1.0, tol=0.0010290226777727477
[CV 2/3; 38/50] END C=0.058740732771874166, class_weight=balanced, l1_ratio=1.0, tol=0.0010290226777727477;, score=0.987 total time=  10.7s
[CV 3/3; 38/50] START C=0.058740732771874166, class_weight=balanced, l1_ratio=1.0, tol=0.0010290226777727477
[CV 3/3; 38/50] END C=0.058740732771874166, class_weight=balanced, l1_ratio=1.0, tol=0.0010290226777727477;, score=0.955 total time=  24.9s
[CV 1/3; 39/50] START C=0.0027505570196345868, class_weight=None, l1_ratio=0.0, tol=0.07908338542644996
[CV 1/3; 39/50] END C=0.0027505570196345868, class_weight=None, l1_ratio=0.0, tol=0.07908338542644996;, score=0.933 total time=   0.4s
[CV 2/3; 39/50] START C=0.0027505570196345868, class_weight=None, l1_ratio=0.0, tol=0.07908338542644996
[CV 2/3; 39/50] END C=0.0027505570196345868, class_weight=None, l1_ratio=0.0, tol=0.07908338542644996;, score=0.953 total time=   0.4s
[CV 3/3; 39/50] START C=0.0027505570196345868, class_weight=None, l1_ratio=0.0, tol=0.07908338542644996
[CV 3/3; 39/50] END C=0.0027505570196345868, class_weight=None, l1_ratio=0.0, tol=0.07908338542644996;, score=0.929 total time=   0.4s
[CV 1/3; 40/50] START C=1.6815691065219271, class_weight=balanced, l1_ratio=0.0, tol=0.05321191357859731
[CV 1/3; 40/50] END C=1.6815691065219271, class_weight=balanced, l1_ratio=0.0, tol=0.05321191357859731;, score=0.917 total time=   0.5s
[CV 2/3; 40/50] START C=1.6815691065219271, class_weight=balanced, l1_ratio=0.0, tol=0.05321191357859731
[CV 2/3; 40/50] END C=1.6815691065219271, class_weight=balanced, l1_ratio=0.0, tol=0.05321191357859731;, score=0.980 total time=   0.6s
[CV 3/3; 40/50] START C=1.6815691065219271, class_weight=balanced, l1_ratio=0.0, tol=0.05321191357859731
[CV 3/3; 40/50] END C=1.6815691065219271, class_weight=balanced, l1_ratio=0.0, tol=0.05321191357859731;, score=0.949 total time=   0.7s
[CV 1/3; 41/50] START C=0.6178839264580976, class_weight=balanced, l1_ratio=0.0, tol=0.016812816807934325
[CV 1/3; 41/50] END C=0.6178839264580976, class_weight=balanced, l1_ratio=0.0, tol=0.016812816807934325;, score=0.921 total time=   0.8s
[CV 2/3; 41/50] START C=0.6178839264580976, class_weight=balanced, l1_ratio=0.0, tol=0.016812816807934325
[CV 2/3; 41/50] END C=0.6178839264580976, class_weight=balanced, l1_ratio=0.0, tol=0.016812816807934325;, score=0.983 total time=   0.9s
[CV 3/3; 41/50] START C=0.6178839264580976, class_weight=balanced, l1_ratio=0.0, tol=0.016812816807934325
[CV 3/3; 41/50] END C=0.6178839264580976, class_weight=balanced, l1_ratio=0.0, tol=0.016812816807934325;, score=0.949 total time=   1.0s
[CV 1/3; 42/50] START C=0.09599543522483903, class_weight=balanced, l1_ratio=1.0, tol=0.057082467278877655
[CV 1/3; 42/50] END C=0.09599543522483903, class_weight=balanced, l1_ratio=1.0, tol=0.057082467278877655;, score=0.921 total time=   0.7s
[CV 2/3; 42/50] START C=0.09599543522483903, class_weight=balanced, l1_ratio=1.0, tol=0.057082467278877655
[CV 2/3; 42/50] END C=0.09599543522483903, class_weight=balanced, l1_ratio=1.0, tol=0.057082467278877655;, score=0.980 total time=   0.7s
[CV 3/3; 42/50] START C=0.09599543522483903, class_weight=balanced, l1_ratio=1.0, tol=0.057082467278877655
[CV 3/3; 42/50] END C=0.09599543522483903, class_weight=balanced, l1_ratio=1.0, tol=0.057082467278877655;, score=0.950 total time=   0.9s
[CV 1/3; 43/50] START C=0.0444698498329451, class_weight=balanced, l1_ratio=0.5, tol=0.07664370120312543
[CV 1/3; 43/50] END C=0.0444698498329451, class_weight=balanced, l1_ratio=0.5, tol=0.07664370120312543;, score=0.919 total time=   0.7s
[CV 2/3; 43/50] START C=0.0444698498329451, class_weight=balanced, l1_ratio=0.5, tol=0.07664370120312543
[CV 2/3; 43/50] END C=0.0444698498329451, class_weight=balanced, l1_ratio=0.5, tol=0.07664370120312543;, score=0.980 total time=   0.8s
[CV 3/3; 43/50] START C=0.0444698498329451, class_weight=balanced, l1_ratio=0.5, tol=0.07664370120312543
[CV 3/3; 43/50] END C=0.0444698498329451, class_weight=balanced, l1_ratio=0.5, tol=0.07664370120312543;, score=0.949 total time=   0.7s
[CV 1/3; 44/50] START C=0.00622334739551427, class_weight=balanced, l1_ratio=0.0, tol=0.0035265628438475097
[CV 1/3; 44/50] END C=0.00622334739551427, class_weight=balanced, l1_ratio=0.0, tol=0.0035265628438475097;, score=0.920 total time=   2.3s
[CV 2/3; 44/50] START C=0.00622334739551427, class_weight=balanced, l1_ratio=0.0, tol=0.0035265628438475097
[CV 2/3; 44/50] END C=0.00622334739551427, class_weight=balanced, l1_ratio=0.0, tol=0.0035265628438475097;, score=0.986 total time=   2.6s
[CV 3/3; 44/50] START C=0.00622334739551427, class_weight=balanced, l1_ratio=0.0, tol=0.0035265628438475097
[CV 3/3; 44/50] END C=0.00622334739551427, class_weight=balanced, l1_ratio=0.0, tol=0.0035265628438475097;, score=0.954 total time=   2.1s
[CV 1/3; 45/50] START C=0.026706402274906907, class_weight=None, l1_ratio=0.5, tol=0.014359192014604654
[CV 1/3; 45/50] END C=0.026706402274906907, class_weight=None, l1_ratio=0.5, tol=0.014359192014604654;, score=0.946 total time=   1.1s
[CV 2/3; 45/50] START C=0.026706402274906907, class_weight=None, l1_ratio=0.5, tol=0.014359192014604654
[CV 2/3; 45/50] END C=0.026706402274906907, class_weight=None, l1_ratio=0.5, tol=0.014359192014604654;, score=0.976 total time=   1.2s
[CV 3/3; 45/50] START C=0.026706402274906907, class_weight=None, l1_ratio=0.5, tol=0.014359192014604654
[CV 3/3; 45/50] END C=0.026706402274906907, class_weight=None, l1_ratio=0.5, tol=0.014359192014604654;, score=0.947 total time=   1.2s
[CV 1/3; 46/50] START C=0.014853486484596534, class_weight=None, l1_ratio=1.0, tol=0.036816569795857824
[CV 1/3; 46/50] END C=0.014853486484596534, class_weight=None, l1_ratio=1.0, tol=0.036816569795857824;, score=0.937 total time=   0.6s
[CV 2/3; 46/50] START C=0.014853486484596534, class_weight=None, l1_ratio=1.0, tol=0.036816569795857824
[CV 2/3; 46/50] END C=0.014853486484596534, class_weight=None, l1_ratio=1.0, tol=0.036816569795857824;, score=0.960 total time=   0.6s
[CV 3/3; 46/50] START C=0.014853486484596534, class_weight=None, l1_ratio=1.0, tol=0.036816569795857824
[CV 3/3; 46/50] END C=0.014853486484596534, class_weight=None, l1_ratio=1.0, tol=0.036816569795857824;, score=0.939 total time=   0.7s
[CV 1/3; 47/50] START C=0.1122699715385801, class_weight=None, l1_ratio=0.5, tol=0.002898121140432545
[CV 1/3; 47/50] END C=0.1122699715385801, class_weight=None, l1_ratio=0.5, tol=0.002898121140432545;, score=0.945 total time=   5.2s
[CV 2/3; 47/50] START C=0.1122699715385801, class_weight=None, l1_ratio=0.5, tol=0.002898121140432545
[CV 2/3; 47/50] END C=0.1122699715385801, class_weight=None, l1_ratio=0.5, tol=0.002898121140432545;, score=0.986 total time=   6.3s
[CV 3/3; 47/50] START C=0.1122699715385801, class_weight=None, l1_ratio=0.5, tol=0.002898121140432545
[CV 3/3; 47/50] END C=0.1122699715385801, class_weight=None, l1_ratio=0.5, tol=0.002898121140432545;, score=0.953 total time=   5.5s
[CV 1/3; 48/50] START C=1.8809687685860288, class_weight=None, l1_ratio=1.0, tol=0.038981012969457794
[CV 1/3; 48/50] END C=1.8809687685860288, class_weight=None, l1_ratio=1.0, tol=0.038981012969457794;, score=0.939 total time=   0.6s
[CV 2/3; 48/50] START C=1.8809687685860288, class_weight=None, l1_ratio=1.0, tol=0.038981012969457794
[CV 2/3; 48/50] END C=1.8809687685860288, class_weight=None, l1_ratio=1.0, tol=0.038981012969457794;, score=0.963 total time=   0.6s
[CV 3/3; 48/50] START C=1.8809687685860288, class_weight=None, l1_ratio=1.0, tol=0.038981012969457794
[CV 3/3; 48/50] END C=1.8809687685860288, class_weight=None, l1_ratio=1.0, tol=0.038981012969457794;, score=0.942 total time=   0.7s
[CV 1/3; 49/50] START C=0.15875539471748848, class_weight=None, l1_ratio=0.5, tol=0.0015319982195377533
[CV 1/3; 49/50] END C=0.15875539471748848, class_weight=None, l1_ratio=0.5, tol=0.0015319982195377533;, score=0.942 total time=   8.2s
[CV 2/3; 49/50] START C=0.15875539471748848, class_weight=None, l1_ratio=0.5, tol=0.0015319982195377533
[CV 2/3; 49/50] END C=0.15875539471748848, class_weight=None, l1_ratio=0.5, tol=0.0015319982195377533;, score=0.988 total time=  16.2s
[CV 3/3; 49/50] START C=0.15875539471748848, class_weight=None, l1_ratio=0.5, tol=0.0015319982195377533
[CV 3/3; 49/50] END C=0.15875539471748848, class_weight=None, l1_ratio=0.5, tol=0.0015319982195377533;, score=0.956 total time=   8.3s
[CV 1/3; 50/50] START C=0.001140620016267105, class_weight=None, l1_ratio=1.0, tol=0.013424594402086815
[CV 1/3; 50/50] END C=0.001140620016267105, class_weight=None, l1_ratio=1.0, tol=0.013424594402086815;, score=0.906 total time=   1.4s
[CV 2/3; 50/50] START C=0.001140620016267105, class_weight=None, l1_ratio=1.0, tol=0.013424594402086815
[CV 2/3; 50/50] END C=0.001140620016267105, class_weight=None, l1_ratio=1.0, tol=0.013424594402086815;, score=0.928 total time=   1.2s
[CV 3/3; 50/50] START C=0.001140620016267105, class_weight=None, l1_ratio=1.0, tol=0.013424594402086815
[CV 3/3; 50/50] END C=0.001140620016267105, class_weight=None, l1_ratio=1.0, tol=0.013424594402086815;, score=0.902 total time=   1.6s

--- TUNING FINISHED ---
Beste Parameter: {'C': np.float64(0.15875539471748848), 'class_weight': None, 'l1_ratio': 0.5, 'tol': np.float64(0.0015319982195377533)}
Bester CV-Score: 0.9622

--- EVALUATION AUF DEN TESTDATEN ---
Test Accuracy: 0.9039

Macro F1: 0.892635837040564

--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9039

                     precision    recall  f1-score   support

             B cell       1.00      0.98      0.99       120
     CD14+ monocyte       0.99      1.00      0.99      2575
        CD4+ T cell       0.88      1.00      0.94      3910
   Cytotoxic T cell       0.90      0.61      0.73      1824
     Dendritic cell       1.00      0.60      0.75         5
      Megakaryocyte       1.00      1.00      1.00         7
Natural killer cell       0.75      0.80      0.77       791
        Plasma cell       1.00      0.94      0.97        49

           accuracy                           0.90      9281
          macro avg       0.94      0.87      0.89      9281
       weighted avg       0.91      0.90      0.90      9281

Random dropout accuracy score 0.8964
Total samples: 9281
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.9010
Feature importance dropout (0.5% features dropped) accuracy score 0.8800
Feature importance dropout (1.0% features dropped) accuracy score 0.8580
Feature importance dropout (2.0% features dropped) accuracy score 0.8080
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8604

                     precision    recall  f1-score   support

             B cell       1.00      0.98      0.99      3959
     CD14+ monocyte       0.74      1.00      0.85      3135
        CD4+ T cell       0.94      0.97      0.95     13664
   Cytotoxic T cell       0.65      0.72      0.68      4839
     Dendritic cell       0.99      0.59      0.74       529
      Megakaryocyte       0.99      0.77      0.86        86
Natural killer cell       0.75      0.31      0.44      2751
        Plasma cell       0.77      1.00      0.87        23

           accuracy                           0.86     28986
          macro avg       0.85      0.79      0.80     28986
       weighted avg       0.86      0.86      0.85     28986

Random dropout accuracy score 0.8337
Total samples: 28986
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.8566
Feature importance dropout (0.5% features dropped) accuracy score 0.8313
Feature importance dropout (1.0% features dropped) accuracy score 0.7959
Feature importance dropout (2.0% features dropped) accuracy score 0.7316
=== JOB_STATISTICS ===
=== current date     : Sun Jun 28 22:51:02 CEST 2026
= Job-ID             : 11997741 on woody
= Job-Name           : conditional_autoencoder_lr
= Job-Command        : /home/hpc/iwbn/iwbn133h/submit_conditional_autoencoder_lr_v1.sh
= Initial workdir    : /home/hpc/iwbn/iwbn133h
= Queue/Partition    : work
= Slurm account      : iwbn with QOS=normal
= Features           : icx
= Requested resources:  for 17:00:00
= Elapsed runtime    : 00:52:13
= Total RAM usage    : 20.8 GiB of requested  GiB (%)   
= Node list          : w2333
= Subm/Elig/Start/End: 2026-06-28T21:58:48 / 2026-06-28T21:58:48 / 2026-06-28T21:58:49 / 2026-06-28T22:51:02
======================
=== Quota infos ======
    Path                 Used     SoftQ    HardQ    Gracetime  Filec    FileQ    FiHaQ    FileGrace    
    /home/woody           982.1M  1000.0G  1500.0G        N/A  29,019    5,000K   7,500K        N/A    
    /home/hpc              86.2G   104.9G   209.7G        N/A     139K     500K   1,000K        N/A    
    /home/vault             0.0K  1048.6G  2097.2G        N/A       1      200K     400K        N/A    
