### Starting TaskPrologue of job 11995953 on w2518 at Sat Jun 27 16:14:55 CEST 2026
#   SLURM_JOB_NODELIST=w2518
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
Epoch [1/150], Loss: 0.9423
Epoch [10/150], Loss: 0.9065
Epoch [20/150], Loss: 0.9006
Epoch [30/150], Loss: 0.8953
Epoch [40/150], Loss: 0.8931
Epoch [50/150], Loss: 0.8923
Early Stopping after [50/150] Epochs!

Extract robust features...
Starte automatische Hyperparametersuche auf dem Latent Space...
Fitting 3 folds for each of 50 candidates, totalling 150 fits
[CV 1/3; 1/50] START C=0.012609936776883228, class_weight=None, l1_ratio=0.5, tol=0.017274013894718117
[CV 1/3; 1/50] END C=0.012609936776883228, class_weight=None, l1_ratio=0.5, tol=0.017274013894718117;, score=0.952 total time=   0.9s
[CV 2/3; 1/50] START C=0.012609936776883228, class_weight=None, l1_ratio=0.5, tol=0.017274013894718117
[CV 2/3; 1/50] END C=0.012609936776883228, class_weight=None, l1_ratio=0.5, tol=0.017274013894718117;, score=0.966 total time=   0.9s
[CV 3/3; 1/50] START C=0.012609936776883228, class_weight=None, l1_ratio=0.5, tol=0.017274013894718117
[CV 3/3; 1/50] END C=0.012609936776883228, class_weight=None, l1_ratio=0.5, tol=0.017274013894718117;, score=0.944 total time=   1.1s
[CV 1/3; 2/50] START C=0.20409361372676915, class_weight=balanced, l1_ratio=1.0, tol=0.031082723971043193
[CV 1/3; 2/50] END C=0.20409361372676915, class_weight=balanced, l1_ratio=1.0, tol=0.031082723971043193;, score=0.935 total time=   0.9s
[CV 2/3; 2/50] START C=0.20409361372676915, class_weight=balanced, l1_ratio=1.0, tol=0.031082723971043193
[CV 2/3; 2/50] END C=0.20409361372676915, class_weight=balanced, l1_ratio=1.0, tol=0.031082723971043193;, score=0.976 total time=   0.9s
[CV 3/3; 2/50] START C=0.20409361372676915, class_weight=balanced, l1_ratio=1.0, tol=0.031082723971043193
[CV 3/3; 2/50] END C=0.20409361372676915, class_weight=balanced, l1_ratio=1.0, tol=0.031082723971043193;, score=0.949 total time=   0.9s
[CV 1/3; 3/50] START C=0.11101869327815475, class_weight=balanced, l1_ratio=0.5, tol=0.08407464908238982
[CV 1/3; 3/50] END C=0.11101869327815475, class_weight=balanced, l1_ratio=0.5, tol=0.08407464908238982;, score=0.928 total time=   0.7s
[CV 2/3; 3/50] START C=0.11101869327815475, class_weight=balanced, l1_ratio=0.5, tol=0.08407464908238982
[CV 2/3; 3/50] END C=0.11101869327815475, class_weight=balanced, l1_ratio=0.5, tol=0.08407464908238982;, score=0.975 total time=   0.7s
[CV 3/3; 3/50] START C=0.11101869327815475, class_weight=balanced, l1_ratio=0.5, tol=0.08407464908238982
[CV 3/3; 3/50] END C=0.11101869327815475, class_weight=balanced, l1_ratio=0.5, tol=0.08407464908238982;, score=0.950 total time=   0.8s
[CV 1/3; 4/50] START C=0.0039689709908290296, class_weight=None, l1_ratio=0.5, tol=0.029334382581159908
[CV 1/3; 4/50] END C=0.0039689709908290296, class_weight=None, l1_ratio=0.5, tol=0.029334382581159908;, score=0.947 total time=   0.7s
[CV 2/3; 4/50] START C=0.0039689709908290296, class_weight=None, l1_ratio=0.5, tol=0.029334382581159908
[CV 2/3; 4/50] END C=0.0039689709908290296, class_weight=None, l1_ratio=0.5, tol=0.029334382581159908;, score=0.954 total time=   0.7s
[CV 3/3; 4/50] START C=0.0039689709908290296, class_weight=None, l1_ratio=0.5, tol=0.029334382581159908
[CV 3/3; 4/50] END C=0.0039689709908290296, class_weight=None, l1_ratio=0.5, tol=0.029334382581159908;, score=0.934 total time=   0.7s
[CV 1/3; 5/50] START C=0.7050461708052099, class_weight=balanced, l1_ratio=0.5, tol=0.07186665462831679
[CV 1/3; 5/50] END C=0.7050461708052099, class_weight=balanced, l1_ratio=0.5, tol=0.07186665462831679;, score=0.937 total time=   1.1s
[CV 2/3; 5/50] START C=0.7050461708052099, class_weight=balanced, l1_ratio=0.5, tol=0.07186665462831679
[CV 2/3; 5/50] END C=0.7050461708052099, class_weight=balanced, l1_ratio=0.5, tol=0.07186665462831679;, score=0.975 total time=   0.7s
[CV 3/3; 5/50] START C=0.7050461708052099, class_weight=balanced, l1_ratio=0.5, tol=0.07186665462831679
[CV 3/3; 5/50] END C=0.7050461708052099, class_weight=balanced, l1_ratio=0.5, tol=0.07186665462831679;, score=0.948 total time=   0.9s
[CV 1/3; 6/50] START C=0.6010112558922305, class_weight=balanced, l1_ratio=0.0, tol=0.004604941837593728
[CV 1/3; 6/50] END C=0.6010112558922305, class_weight=balanced, l1_ratio=0.0, tol=0.004604941837593728;, score=0.937 total time=   2.1s
[CV 2/3; 6/50] START C=0.6010112558922305, class_weight=balanced, l1_ratio=0.0, tol=0.004604941837593728
[CV 2/3; 6/50] END C=0.6010112558922305, class_weight=balanced, l1_ratio=0.0, tol=0.004604941837593728;, score=0.981 total time=   2.3s
[CV 3/3; 6/50] START C=0.6010112558922305, class_weight=balanced, l1_ratio=0.0, tol=0.004604941837593728
[CV 3/3; 6/50] END C=0.6010112558922305, class_weight=balanced, l1_ratio=0.0, tol=0.004604941837593728;, score=0.956 total time=   2.1s
[CV 1/3; 7/50] START C=0.19421967119995723, class_weight=None, l1_ratio=1.0, tol=0.004773231438313708
[CV 1/3; 7/50] END C=0.19421967119995723, class_weight=None, l1_ratio=1.0, tol=0.004773231438313708;, score=0.951 total time=   2.7s
[CV 2/3; 7/50] START C=0.19421967119995723, class_weight=None, l1_ratio=1.0, tol=0.004773231438313708
[CV 2/3; 7/50] END C=0.19421967119995723, class_weight=None, l1_ratio=1.0, tol=0.004773231438313708;, score=0.980 total time=   2.8s
[CV 3/3; 7/50] START C=0.19421967119995723, class_weight=None, l1_ratio=1.0, tol=0.004773231438313708
[CV 3/3; 7/50] END C=0.19421967119995723, class_weight=None, l1_ratio=1.0, tol=0.004773231438313708;, score=0.954 total time=   3.2s
[CV 1/3; 8/50] START C=0.057583854070639096, class_weight=None, l1_ratio=0.0, tol=0.024934438791777442
[CV 1/3; 8/50] END C=0.057583854070639096, class_weight=None, l1_ratio=0.0, tol=0.024934438791777442;, score=0.950 total time=   0.6s
[CV 2/3; 8/50] START C=0.057583854070639096, class_weight=None, l1_ratio=0.0, tol=0.024934438791777442
[CV 2/3; 8/50] END C=0.057583854070639096, class_weight=None, l1_ratio=0.0, tol=0.024934438791777442;, score=0.966 total time=   0.6s
[CV 3/3; 8/50] START C=0.057583854070639096, class_weight=None, l1_ratio=0.0, tol=0.024934438791777442
[CV 3/3; 8/50] END C=0.057583854070639096, class_weight=None, l1_ratio=0.0, tol=0.024934438791777442;, score=0.941 total time=   0.6s
[CV 1/3; 9/50] START C=1.451863667545072, class_weight=None, l1_ratio=0.5, tol=0.01152814328136457
[CV 1/3; 9/50] END C=1.451863667545072, class_weight=None, l1_ratio=0.5, tol=0.01152814328136457;, score=0.951 total time=   1.3s
[CV 2/3; 9/50] START C=1.451863667545072, class_weight=None, l1_ratio=0.5, tol=0.01152814328136457
[CV 2/3; 9/50] END C=1.451863667545072, class_weight=None, l1_ratio=0.5, tol=0.01152814328136457;, score=0.975 total time=   1.5s
[CV 3/3; 9/50] START C=1.451863667545072, class_weight=None, l1_ratio=0.5, tol=0.01152814328136457
[CV 3/3; 9/50] END C=1.451863667545072, class_weight=None, l1_ratio=0.5, tol=0.01152814328136457;, score=0.950 total time=   1.5s
[CV 1/3; 10/50] START C=0.014090182985195114, class_weight=balanced, l1_ratio=1.0, tol=0.0027415893917039124
[CV 1/3; 10/50] END C=0.014090182985195114, class_weight=balanced, l1_ratio=1.0, tol=0.0027415893917039124;, score=0.934 total time=   6.9s
[CV 2/3; 10/50] START C=0.014090182985195114, class_weight=balanced, l1_ratio=1.0, tol=0.0027415893917039124
[CV 2/3; 10/50] END C=0.014090182985195114, class_weight=balanced, l1_ratio=1.0, tol=0.0027415893917039124;, score=0.981 total time=   6.6s
[CV 3/3; 10/50] START C=0.014090182985195114, class_weight=balanced, l1_ratio=1.0, tol=0.0027415893917039124
[CV 3/3; 10/50] END C=0.014090182985195114, class_weight=balanced, l1_ratio=1.0, tol=0.0027415893917039124;, score=0.954 total time=   5.8s
[CV 1/3; 11/50] START C=0.02843931258963486, class_weight=None, l1_ratio=0.5, tol=0.07419808131474767
[CV 1/3; 11/50] END C=0.02843931258963486, class_weight=None, l1_ratio=0.5, tol=0.07419808131474767;, score=0.942 total time=   0.5s
[CV 2/3; 11/50] START C=0.02843931258963486, class_weight=None, l1_ratio=0.5, tol=0.07419808131474767
[CV 2/3; 11/50] END C=0.02843931258963486, class_weight=None, l1_ratio=0.5, tol=0.07419808131474767;, score=0.951 total time=   0.5s
[CV 3/3; 11/50] START C=0.02843931258963486, class_weight=None, l1_ratio=0.5, tol=0.07419808131474767
[CV 3/3; 11/50] END C=0.02843931258963486, class_weight=None, l1_ratio=0.5, tol=0.07419808131474767;, score=0.930 total time=   0.5s
[CV 1/3; 12/50] START C=0.25962126653214246, class_weight=balanced, l1_ratio=0.5, tol=0.05200809893337637
[CV 1/3; 12/50] END C=0.25962126653214246, class_weight=balanced, l1_ratio=0.5, tol=0.05200809893337637;, score=0.931 total time=   0.7s
[CV 2/3; 12/50] START C=0.25962126653214246, class_weight=balanced, l1_ratio=0.5, tol=0.05200809893337637
[CV 2/3; 12/50] END C=0.25962126653214246, class_weight=balanced, l1_ratio=0.5, tol=0.05200809893337637;, score=0.976 total time=   0.9s
[CV 3/3; 12/50] START C=0.25962126653214246, class_weight=balanced, l1_ratio=0.5, tol=0.05200809893337637
[CV 3/3; 12/50] END C=0.25962126653214246, class_weight=balanced, l1_ratio=0.5, tol=0.05200809893337637;, score=0.949 total time=   1.0s
[CV 1/3; 13/50] START C=0.3327935192871912, class_weight=None, l1_ratio=0.0, tol=0.03351269054097009
[CV 1/3; 13/50] END C=0.3327935192871912, class_weight=None, l1_ratio=0.0, tol=0.03351269054097009;, score=0.948 total time=   0.5s
[CV 2/3; 13/50] START C=0.3327935192871912, class_weight=None, l1_ratio=0.0, tol=0.03351269054097009
[CV 2/3; 13/50] END C=0.3327935192871912, class_weight=None, l1_ratio=0.0, tol=0.03351269054097009;, score=0.958 total time=   0.5s
[CV 3/3; 13/50] START C=0.3327935192871912, class_weight=None, l1_ratio=0.0, tol=0.03351269054097009
[CV 3/3; 13/50] END C=0.3327935192871912, class_weight=None, l1_ratio=0.0, tol=0.03351269054097009;, score=0.939 total time=   0.5s
[CV 1/3; 14/50] START C=0.2636787517689966, class_weight=None, l1_ratio=1.0, tol=0.0016990028303679094
[CV 1/3; 14/50] END C=0.2636787517689966, class_weight=None, l1_ratio=1.0, tol=0.0016990028303679094;, score=0.948 total time=   8.4s
[CV 2/3; 14/50] START C=0.2636787517689966, class_weight=None, l1_ratio=1.0, tol=0.0016990028303679094
[CV 2/3; 14/50] END C=0.2636787517689966, class_weight=None, l1_ratio=1.0, tol=0.0016990028303679094;, score=0.983 total time=  12.9s
[CV 3/3; 14/50] START C=0.2636787517689966, class_weight=None, l1_ratio=1.0, tol=0.0016990028303679094
[CV 3/3; 14/50] END C=0.2636787517689966, class_weight=None, l1_ratio=1.0, tol=0.0016990028303679094;, score=0.958 total time=   7.9s
[CV 1/3; 15/50] START C=0.22156596433218118, class_weight=None, l1_ratio=0.0, tol=0.0014882703288977798
[CV 1/3; 15/50] END C=0.22156596433218118, class_weight=None, l1_ratio=0.0, tol=0.0014882703288977798;, score=0.945 total time=   9.2s
[CV 2/3; 15/50] START C=0.22156596433218118, class_weight=None, l1_ratio=0.0, tol=0.0014882703288977798
[CV 2/3; 15/50] END C=0.22156596433218118, class_weight=None, l1_ratio=0.0, tol=0.0014882703288977798;, score=0.983 total time=   7.7s
[CV 3/3; 15/50] START C=0.22156596433218118, class_weight=None, l1_ratio=0.0, tol=0.0014882703288977798
[CV 3/3; 15/50] END C=0.22156596433218118, class_weight=None, l1_ratio=0.0, tol=0.0014882703288977798;, score=0.959 total time=   6.8s
[CV 1/3; 16/50] START C=0.013335370057853915, class_weight=None, l1_ratio=0.5, tol=0.024869782422235767
[CV 1/3; 16/50] END C=0.013335370057853915, class_weight=None, l1_ratio=0.5, tol=0.024869782422235767;, score=0.950 total time=   0.8s
[CV 2/3; 16/50] START C=0.013335370057853915, class_weight=None, l1_ratio=0.5, tol=0.024869782422235767
[CV 2/3; 16/50] END C=0.013335370057853915, class_weight=None, l1_ratio=0.5, tol=0.024869782422235767;, score=0.960 total time=   0.8s
[CV 3/3; 16/50] START C=0.013335370057853915, class_weight=None, l1_ratio=0.5, tol=0.024869782422235767
[CV 3/3; 16/50] END C=0.013335370057853915, class_weight=None, l1_ratio=0.5, tol=0.024869782422235767;, score=0.940 total time=   0.8s
[CV 1/3; 17/50] START C=0.013056016793119742, class_weight=None, l1_ratio=0.0, tol=0.005970417794584207
[CV 1/3; 17/50] END C=0.013056016793119742, class_weight=None, l1_ratio=0.0, tol=0.005970417794584207;, score=0.952 total time=   1.3s
[CV 2/3; 17/50] START C=0.013056016793119742, class_weight=None, l1_ratio=0.0, tol=0.005970417794584207
[CV 2/3; 17/50] END C=0.013056016793119742, class_weight=None, l1_ratio=0.0, tol=0.005970417794584207;, score=0.979 total time=   1.4s
[CV 3/3; 17/50] START C=0.013056016793119742, class_weight=None, l1_ratio=0.0, tol=0.005970417794584207
[CV 3/3; 17/50] END C=0.013056016793119742, class_weight=None, l1_ratio=0.0, tol=0.005970417794584207;, score=0.954 total time=   1.5s
[CV 1/3; 18/50] START C=0.0022675285138010312, class_weight=None, l1_ratio=1.0, tol=0.01614498847299075
[CV 1/3; 18/50] END C=0.0022675285138010312, class_weight=None, l1_ratio=1.0, tol=0.01614498847299075;, score=0.941 total time=   1.3s
[CV 2/3; 18/50] START C=0.0022675285138010312, class_weight=None, l1_ratio=1.0, tol=0.01614498847299075
[CV 2/3; 18/50] END C=0.0022675285138010312, class_weight=None, l1_ratio=1.0, tol=0.01614498847299075;, score=0.947 total time=   1.3s
[CV 3/3; 18/50] START C=0.0022675285138010312, class_weight=None, l1_ratio=1.0, tol=0.01614498847299075
[CV 3/3; 18/50] END C=0.0022675285138010312, class_weight=None, l1_ratio=1.0, tol=0.01614498847299075;, score=0.920 total time=   1.4s
[CV 1/3; 19/50] START C=0.005852580161255513, class_weight=None, l1_ratio=1.0, tol=0.09816340779126453
[CV 1/3; 19/50] END C=0.005852580161255513, class_weight=None, l1_ratio=1.0, tol=0.09816340779126453;, score=0.939 total time=   0.5s
[CV 2/3; 19/50] START C=0.005852580161255513, class_weight=None, l1_ratio=1.0, tol=0.09816340779126453
[CV 2/3; 19/50] END C=0.005852580161255513, class_weight=None, l1_ratio=1.0, tol=0.09816340779126453;, score=0.942 total time=   0.5s
[CV 3/3; 19/50] START C=0.005852580161255513, class_weight=None, l1_ratio=1.0, tol=0.09816340779126453
[CV 3/3; 19/50] END C=0.005852580161255513, class_weight=None, l1_ratio=1.0, tol=0.09816340779126453;, score=0.922 total time=   0.5s
[CV 1/3; 20/50] START C=0.006689312326763979, class_weight=balanced, l1_ratio=0.0, tol=0.05438832070786372
[CV 1/3; 20/50] END C=0.006689312326763979, class_weight=balanced, l1_ratio=0.0, tol=0.05438832070786372;, score=0.932 total time=   0.6s
[CV 2/3; 20/50] START C=0.006689312326763979, class_weight=balanced, l1_ratio=0.0, tol=0.05438832070786372
[CV 2/3; 20/50] END C=0.006689312326763979, class_weight=balanced, l1_ratio=0.0, tol=0.05438832070786372;, score=0.974 total time=   0.5s
[CV 3/3; 20/50] START C=0.006689312326763979, class_weight=balanced, l1_ratio=0.0, tol=0.05438832070786372
[CV 3/3; 20/50] END C=0.006689312326763979, class_weight=balanced, l1_ratio=0.0, tol=0.05438832070786372;, score=0.940 total time=   0.6s
[CV 1/3; 21/50] START C=0.2599115277756149, class_weight=balanced, l1_ratio=1.0, tol=0.01557838936570268
[CV 1/3; 21/50] END C=0.2599115277756149, class_weight=balanced, l1_ratio=1.0, tol=0.01557838936570268;, score=0.936 total time=   1.3s
[CV 2/3; 21/50] START C=0.2599115277756149, class_weight=balanced, l1_ratio=1.0, tol=0.01557838936570268
[CV 2/3; 21/50] END C=0.2599115277756149, class_weight=balanced, l1_ratio=1.0, tol=0.01557838936570268;, score=0.977 total time=   1.3s
[CV 3/3; 21/50] START C=0.2599115277756149, class_weight=balanced, l1_ratio=1.0, tol=0.01557838936570268
[CV 3/3; 21/50] END C=0.2599115277756149, class_weight=balanced, l1_ratio=1.0, tol=0.01557838936570268;, score=0.952 total time=   1.2s
[CV 1/3; 22/50] START C=0.10775084491944904, class_weight=None, l1_ratio=0.5, tol=0.022776604295820888
[CV 1/3; 22/50] END C=0.10775084491944904, class_weight=None, l1_ratio=0.5, tol=0.022776604295820888;, score=0.951 total time=   0.8s
[CV 2/3; 22/50] START C=0.10775084491944904, class_weight=None, l1_ratio=0.5, tol=0.022776604295820888
[CV 2/3; 22/50] END C=0.10775084491944904, class_weight=None, l1_ratio=0.5, tol=0.022776604295820888;, score=0.962 total time=   0.8s
[CV 3/3; 22/50] START C=0.10775084491944904, class_weight=None, l1_ratio=0.5, tol=0.022776604295820888
[CV 3/3; 22/50] END C=0.10775084491944904, class_weight=None, l1_ratio=0.5, tol=0.022776604295820888;, score=0.942 total time=   0.9s
[CV 1/3; 23/50] START C=0.2275809254785705, class_weight=balanced, l1_ratio=1.0, tol=0.08875267236305359
[CV 1/3; 23/50] END C=0.2275809254785705, class_weight=balanced, l1_ratio=1.0, tol=0.08875267236305359;, score=0.930 total time=   0.6s
[CV 2/3; 23/50] START C=0.2275809254785705, class_weight=balanced, l1_ratio=1.0, tol=0.08875267236305359
[CV 2/3; 23/50] END C=0.2275809254785705, class_weight=balanced, l1_ratio=1.0, tol=0.08875267236305359;, score=0.974 total time=   0.6s
[CV 3/3; 23/50] START C=0.2275809254785705, class_weight=balanced, l1_ratio=1.0, tol=0.08875267236305359
[CV 3/3; 23/50] END C=0.2275809254785705, class_weight=balanced, l1_ratio=1.0, tol=0.08875267236305359;, score=0.951 total time=   0.7s
[CV 1/3; 24/50] START C=0.0027917862030868916, class_weight=balanced, l1_ratio=1.0, tol=0.026225676689872305
[CV 1/3; 24/50] END C=0.0027917862030868916, class_weight=balanced, l1_ratio=1.0, tol=0.026225676689872305;, score=0.926 total time=   0.9s
[CV 2/3; 24/50] START C=0.0027917862030868916, class_weight=balanced, l1_ratio=1.0, tol=0.026225676689872305
[CV 2/3; 24/50] END C=0.0027917862030868916, class_weight=balanced, l1_ratio=1.0, tol=0.026225676689872305;, score=0.970 total time=   2.2s
[CV 3/3; 24/50] START C=0.0027917862030868916, class_weight=balanced, l1_ratio=1.0, tol=0.026225676689872305
[CV 3/3; 24/50] END C=0.0027917862030868916, class_weight=balanced, l1_ratio=1.0, tol=0.026225676689872305;, score=0.941 total time=   2.1s
[CV 1/3; 25/50] START C=1.0929127498276467, class_weight=balanced, l1_ratio=0.0, tol=0.02118604231356325
[CV 1/3; 25/50] END C=1.0929127498276467, class_weight=balanced, l1_ratio=0.0, tol=0.02118604231356325;, score=0.934 total time=   0.7s
[CV 2/3; 25/50] START C=1.0929127498276467, class_weight=balanced, l1_ratio=0.0, tol=0.02118604231356325
[CV 2/3; 25/50] END C=1.0929127498276467, class_weight=balanced, l1_ratio=0.0, tol=0.02118604231356325;, score=0.978 total time=   0.8s
[CV 3/3; 25/50] START C=1.0929127498276467, class_weight=balanced, l1_ratio=0.0, tol=0.02118604231356325
[CV 3/3; 25/50] END C=1.0929127498276467, class_weight=balanced, l1_ratio=0.0, tol=0.02118604231356325;, score=0.939 total time=   0.8s
[CV 1/3; 26/50] START C=0.010926973618609457, class_weight=balanced, l1_ratio=1.0, tol=0.005131754159224723
[CV 1/3; 26/50] END C=0.010926973618609457, class_weight=balanced, l1_ratio=1.0, tol=0.005131754159224723;, score=0.935 total time=   4.1s
[CV 2/3; 26/50] START C=0.010926973618609457, class_weight=balanced, l1_ratio=1.0, tol=0.005131754159224723
[CV 2/3; 26/50] END C=0.010926973618609457, class_weight=balanced, l1_ratio=1.0, tol=0.005131754159224723;, score=0.980 total time=   4.0s
[CV 3/3; 26/50] START C=0.010926973618609457, class_weight=balanced, l1_ratio=1.0, tol=0.005131754159224723
[CV 3/3; 26/50] END C=0.010926973618609457, class_weight=balanced, l1_ratio=1.0, tol=0.005131754159224723;, score=0.952 total time=   4.1s
[CV 1/3; 27/50] START C=0.004429248656605289, class_weight=None, l1_ratio=0.0, tol=0.024133507870397596
[CV 1/3; 27/50] END C=0.004429248656605289, class_weight=None, l1_ratio=0.0, tol=0.024133507870397596;, score=0.951 total time=   0.6s
[CV 2/3; 27/50] START C=0.004429248656605289, class_weight=None, l1_ratio=0.0, tol=0.024133507870397596
[CV 2/3; 27/50] END C=0.004429248656605289, class_weight=None, l1_ratio=0.0, tol=0.024133507870397596;, score=0.962 total time=   0.6s
[CV 3/3; 27/50] START C=0.004429248656605289, class_weight=None, l1_ratio=0.0, tol=0.024133507870397596
[CV 3/3; 27/50] END C=0.004429248656605289, class_weight=None, l1_ratio=0.0, tol=0.024133507870397596;, score=0.941 total time=   0.6s
[CV 1/3; 28/50] START C=1.35767544051319, class_weight=balanced, l1_ratio=1.0, tol=0.0076366080593919475
[CV 1/3; 28/50] END C=1.35767544051319, class_weight=balanced, l1_ratio=1.0, tol=0.0076366080593919475;, score=0.936 total time=   2.2s
[CV 2/3; 28/50] START C=1.35767544051319, class_weight=balanced, l1_ratio=1.0, tol=0.0076366080593919475
[CV 2/3; 28/50] END C=1.35767544051319, class_weight=balanced, l1_ratio=1.0, tol=0.0076366080593919475;, score=0.980 total time=   2.3s
[CV 3/3; 28/50] START C=1.35767544051319, class_weight=balanced, l1_ratio=1.0, tol=0.0076366080593919475
[CV 3/3; 28/50] END C=1.35767544051319, class_weight=balanced, l1_ratio=1.0, tol=0.0076366080593919475;, score=0.957 total time=   2.1s
[CV 1/3; 29/50] START C=0.06665365851190123, class_weight=None, l1_ratio=0.5, tol=0.05049502333284934
[CV 1/3; 29/50] END C=0.06665365851190123, class_weight=None, l1_ratio=0.5, tol=0.05049502333284934;, score=0.947 total time=   0.6s
[CV 2/3; 29/50] START C=0.06665365851190123, class_weight=None, l1_ratio=0.5, tol=0.05049502333284934
[CV 2/3; 29/50] END C=0.06665365851190123, class_weight=None, l1_ratio=0.5, tol=0.05049502333284934;, score=0.955 total time=   0.6s
[CV 3/3; 29/50] START C=0.06665365851190123, class_weight=None, l1_ratio=0.5, tol=0.05049502333284934
[CV 3/3; 29/50] END C=0.06665365851190123, class_weight=None, l1_ratio=0.5, tol=0.05049502333284934;, score=0.933 total time=   0.6s
[CV 1/3; 30/50] START C=0.2330198015203367, class_weight=None, l1_ratio=1.0, tol=0.0013828242820220946
[CV 1/3; 30/50] END C=0.2330198015203367, class_weight=None, l1_ratio=1.0, tol=0.0013828242820220946;, score=0.946 total time=  16.5s
[CV 2/3; 30/50] START C=0.2330198015203367, class_weight=None, l1_ratio=1.0, tol=0.0013828242820220946
[CV 2/3; 30/50] END C=0.2330198015203367, class_weight=None, l1_ratio=1.0, tol=0.0013828242820220946;, score=0.983 total time=  14.2s
[CV 3/3; 30/50] START C=0.2330198015203367, class_weight=None, l1_ratio=1.0, tol=0.0013828242820220946
[CV 3/3; 30/50] END C=0.2330198015203367, class_weight=None, l1_ratio=1.0, tol=0.0013828242820220946;, score=0.960 total time=  11.9s
[CV 1/3; 31/50] START C=0.0428271766562772, class_weight=None, l1_ratio=0.0, tol=0.01364237983428665
[CV 1/3; 31/50] END C=0.0428271766562772, class_weight=None, l1_ratio=0.0, tol=0.01364237983428665;, score=0.950 total time=   0.8s
[CV 2/3; 31/50] START C=0.0428271766562772, class_weight=None, l1_ratio=0.0, tol=0.01364237983428665
[CV 2/3; 31/50] END C=0.0428271766562772, class_weight=None, l1_ratio=0.0, tol=0.01364237983428665;, score=0.972 total time=   0.8s
[CV 3/3; 31/50] START C=0.0428271766562772, class_weight=None, l1_ratio=0.0, tol=0.01364237983428665
[CV 3/3; 31/50] END C=0.0428271766562772, class_weight=None, l1_ratio=0.0, tol=0.01364237983428665;, score=0.949 total time=   0.9s
[CV 1/3; 32/50] START C=0.732094999252387, class_weight=balanced, l1_ratio=0.0, tol=0.06831030332436447
[CV 1/3; 32/50] END C=0.732094999252387, class_weight=balanced, l1_ratio=0.0, tol=0.06831030332436447;, score=0.932 total time=   0.5s
[CV 2/3; 32/50] START C=0.732094999252387, class_weight=balanced, l1_ratio=0.0, tol=0.06831030332436447
[CV 2/3; 32/50] END C=0.732094999252387, class_weight=balanced, l1_ratio=0.0, tol=0.06831030332436447;, score=0.976 total time=   0.6s
[CV 3/3; 32/50] START C=0.732094999252387, class_weight=balanced, l1_ratio=0.0, tol=0.06831030332436447
[CV 3/3; 32/50] END C=0.732094999252387, class_weight=balanced, l1_ratio=0.0, tol=0.06831030332436447;, score=0.948 total time=   0.5s
[CV 1/3; 33/50] START C=0.004158861616189753, class_weight=None, l1_ratio=0.5, tol=0.051587171833462
[CV 1/3; 33/50] END C=0.004158861616189753, class_weight=None, l1_ratio=0.5, tol=0.051587171833462;, score=0.944 total time=   0.6s
[CV 2/3; 33/50] START C=0.004158861616189753, class_weight=None, l1_ratio=0.5, tol=0.051587171833462
[CV 2/3; 33/50] END C=0.004158861616189753, class_weight=None, l1_ratio=0.5, tol=0.051587171833462;, score=0.951 total time=   0.6s
[CV 3/3; 33/50] START C=0.004158861616189753, class_weight=None, l1_ratio=0.5, tol=0.051587171833462
[CV 3/3; 33/50] END C=0.004158861616189753, class_weight=None, l1_ratio=0.5, tol=0.051587171833462;, score=0.929 total time=   0.6s
[CV 1/3; 34/50] START C=0.0017222300430692233, class_weight=None, l1_ratio=0.5, tol=0.0179941927831321
[CV 1/3; 34/50] END C=0.0017222300430692233, class_weight=None, l1_ratio=0.5, tol=0.0179941927831321;, score=0.946 total time=   1.1s
[CV 2/3; 34/50] START C=0.0017222300430692233, class_weight=None, l1_ratio=0.5, tol=0.0179941927831321
[CV 2/3; 34/50] END C=0.0017222300430692233, class_weight=None, l1_ratio=0.5, tol=0.0179941927831321;, score=0.955 total time=   1.1s
[CV 3/3; 34/50] START C=0.0017222300430692233, class_weight=None, l1_ratio=0.5, tol=0.0179941927831321
[CV 3/3; 34/50] END C=0.0017222300430692233, class_weight=None, l1_ratio=0.5, tol=0.0179941927831321;, score=0.928 total time=   1.1s
[CV 1/3; 35/50] START C=0.10497113443418299, class_weight=None, l1_ratio=1.0, tol=0.026456401700130056
[CV 1/3; 35/50] END C=0.10497113443418299, class_weight=None, l1_ratio=1.0, tol=0.026456401700130056;, score=0.950 total time=   0.8s
[CV 2/3; 35/50] START C=0.10497113443418299, class_weight=None, l1_ratio=1.0, tol=0.026456401700130056
[CV 2/3; 35/50] END C=0.10497113443418299, class_weight=None, l1_ratio=1.0, tol=0.026456401700130056;, score=0.961 total time=   0.7s
[CV 3/3; 35/50] START C=0.10497113443418299, class_weight=None, l1_ratio=1.0, tol=0.026456401700130056
[CV 3/3; 35/50] END C=0.10497113443418299, class_weight=None, l1_ratio=1.0, tol=0.026456401700130056;, score=0.940 total time=   0.8s
[CV 1/3; 36/50] START C=0.00488045771571476, class_weight=balanced, l1_ratio=0.0, tol=0.0012289380995686016
[CV 1/3; 36/50] END C=0.00488045771571476, class_weight=balanced, l1_ratio=0.0, tol=0.0012289380995686016;, score=0.934 total time=   6.2s
[CV 2/3; 36/50] START C=0.00488045771571476, class_weight=balanced, l1_ratio=0.0, tol=0.0012289380995686016
[CV 2/3; 36/50] END C=0.00488045771571476, class_weight=balanced, l1_ratio=0.0, tol=0.0012289380995686016;, score=0.982 total time=   6.2s
[CV 3/3; 36/50] START C=0.00488045771571476, class_weight=balanced, l1_ratio=0.0, tol=0.0012289380995686016
[CV 3/3; 36/50] END C=0.00488045771571476, class_weight=balanced, l1_ratio=0.0, tol=0.0012289380995686016;, score=0.959 total time=   5.8s
[CV 1/3; 37/50] START C=0.08722092851514525, class_weight=None, l1_ratio=0.0, tol=0.09642051646786694
[CV 1/3; 37/50] END C=0.08722092851514525, class_weight=None, l1_ratio=0.0, tol=0.09642051646786694;, score=0.943 total time=   0.4s
[CV 2/3; 37/50] START C=0.08722092851514525, class_weight=None, l1_ratio=0.0, tol=0.09642051646786694
[CV 2/3; 37/50] END C=0.08722092851514525, class_weight=None, l1_ratio=0.0, tol=0.09642051646786694;, score=0.951 total time=   0.4s
[CV 3/3; 37/50] START C=0.08722092851514525, class_weight=None, l1_ratio=0.0, tol=0.09642051646786694
[CV 3/3; 37/50] END C=0.08722092851514525, class_weight=None, l1_ratio=0.0, tol=0.09642051646786694;, score=0.932 total time=   0.4s
[CV 1/3; 38/50] START C=0.07984903264620934, class_weight=None, l1_ratio=0.5, tol=0.031008731387463018
[CV 1/3; 38/50] END C=0.07984903264620934, class_weight=None, l1_ratio=0.5, tol=0.031008731387463018;, score=0.949 total time=   0.7s
[CV 2/3; 38/50] START C=0.07984903264620934, class_weight=None, l1_ratio=0.5, tol=0.031008731387463018
[CV 2/3; 38/50] END C=0.07984903264620934, class_weight=None, l1_ratio=0.5, tol=0.031008731387463018;, score=0.961 total time=   0.7s
[CV 3/3; 38/50] START C=0.07984903264620934, class_weight=None, l1_ratio=0.5, tol=0.031008731387463018
[CV 3/3; 38/50] END C=0.07984903264620934, class_weight=None, l1_ratio=0.5, tol=0.031008731387463018;, score=0.938 total time=   0.7s
[CV 1/3; 39/50] START C=0.3278552234917921, class_weight=None, l1_ratio=0.5, tol=0.03165944063594653
[CV 1/3; 39/50] END C=0.3278552234917921, class_weight=None, l1_ratio=0.5, tol=0.03165944063594653;, score=0.948 total time=   0.6s
[CV 2/3; 39/50] START C=0.3278552234917921, class_weight=None, l1_ratio=0.5, tol=0.03165944063594653
[CV 2/3; 39/50] END C=0.3278552234917921, class_weight=None, l1_ratio=0.5, tol=0.03165944063594653;, score=0.958 total time=   0.6s
[CV 3/3; 39/50] START C=0.3278552234917921, class_weight=None, l1_ratio=0.5, tol=0.03165944063594653
[CV 3/3; 39/50] END C=0.3278552234917921, class_weight=None, l1_ratio=0.5, tol=0.03165944063594653;, score=0.938 total time=   0.7s
[CV 1/3; 40/50] START C=0.002293007828624279, class_weight=balanced, l1_ratio=1.0, tol=0.013198942611838882
[CV 1/3; 40/50] END C=0.002293007828624279, class_weight=balanced, l1_ratio=1.0, tol=0.013198942611838882;, score=0.925 total time=   2.5s
[CV 2/3; 40/50] START C=0.002293007828624279, class_weight=balanced, l1_ratio=1.0, tol=0.013198942611838882
[CV 2/3; 40/50] END C=0.002293007828624279, class_weight=balanced, l1_ratio=1.0, tol=0.013198942611838882;, score=0.966 total time=   7.9s
[CV 3/3; 40/50] START C=0.002293007828624279, class_weight=balanced, l1_ratio=1.0, tol=0.013198942611838882
[CV 3/3; 40/50] END C=0.002293007828624279, class_weight=balanced, l1_ratio=1.0, tol=0.013198942611838882;, score=0.937 total time=   3.6s
[CV 1/3; 41/50] START C=1.586091900650653, class_weight=balanced, l1_ratio=0.0, tol=0.0012433377685756616
[CV 1/3; 41/50] END C=1.586091900650653, class_weight=balanced, l1_ratio=0.0, tol=0.0012433377685756616;, score=0.935 total time=   9.3s
[CV 2/3; 41/50] START C=1.586091900650653, class_weight=balanced, l1_ratio=0.0, tol=0.0012433377685756616
[CV 2/3; 41/50] END C=1.586091900650653, class_weight=balanced, l1_ratio=0.0, tol=0.0012433377685756616;, score=0.983 total time=   7.4s
[CV 3/3; 41/50] START C=1.586091900650653, class_weight=balanced, l1_ratio=0.0, tol=0.0012433377685756616
[CV 3/3; 41/50] END C=1.586091900650653, class_weight=balanced, l1_ratio=0.0, tol=0.0012433377685756616;, score=0.961 total time=   7.2s
[CV 1/3; 42/50] START C=0.09122174017161169, class_weight=balanced, l1_ratio=0.0, tol=0.011188144059467688
[CV 1/3; 42/50] END C=0.09122174017161169, class_weight=balanced, l1_ratio=0.0, tol=0.011188144059467688;, score=0.937 total time=   1.1s
[CV 2/3; 42/50] START C=0.09122174017161169, class_weight=balanced, l1_ratio=0.0, tol=0.011188144059467688
[CV 2/3; 42/50] END C=0.09122174017161169, class_weight=balanced, l1_ratio=0.0, tol=0.011188144059467688;, score=0.978 total time=   0.9s
[CV 3/3; 42/50] START C=0.09122174017161169, class_weight=balanced, l1_ratio=0.0, tol=0.011188144059467688
[CV 3/3; 42/50] END C=0.09122174017161169, class_weight=balanced, l1_ratio=0.0, tol=0.011188144059467688;, score=0.954 total time=   1.1s
[CV 1/3; 43/50] START C=0.0076478662131671945, class_weight=balanced, l1_ratio=0.5, tol=0.019699801515109798
[CV 1/3; 43/50] END C=0.0076478662131671945, class_weight=balanced, l1_ratio=0.5, tol=0.019699801515109798;, score=0.935 total time=   1.1s
[CV 2/3; 43/50] START C=0.0076478662131671945, class_weight=balanced, l1_ratio=0.5, tol=0.019699801515109798
[CV 2/3; 43/50] END C=0.0076478662131671945, class_weight=balanced, l1_ratio=0.5, tol=0.019699801515109798;, score=0.978 total time=   1.2s
[CV 3/3; 43/50] START C=0.0076478662131671945, class_weight=balanced, l1_ratio=0.5, tol=0.019699801515109798
[CV 3/3; 43/50] END C=0.0076478662131671945, class_weight=balanced, l1_ratio=0.5, tol=0.019699801515109798;, score=0.952 total time=   1.3s
[CV 1/3; 44/50] START C=0.22540223095604311, class_weight=balanced, l1_ratio=0.5, tol=0.004278948859697912
[CV 1/3; 44/50] END C=0.22540223095604311, class_weight=balanced, l1_ratio=0.5, tol=0.004278948859697912;, score=0.936 total time=   3.6s
[CV 2/3; 44/50] START C=0.22540223095604311, class_weight=balanced, l1_ratio=0.5, tol=0.004278948859697912
[CV 2/3; 44/50] END C=0.22540223095604311, class_weight=balanced, l1_ratio=0.5, tol=0.004278948859697912;, score=0.981 total time=   3.7s
[CV 3/3; 44/50] START C=0.22540223095604311, class_weight=balanced, l1_ratio=0.5, tol=0.004278948859697912
[CV 3/3; 44/50] END C=0.22540223095604311, class_weight=balanced, l1_ratio=0.5, tol=0.004278948859697912;, score=0.958 total time=   3.5s
[CV 1/3; 45/50] START C=1.0902902297685761, class_weight=None, l1_ratio=1.0, tol=0.002537522558441109
[CV 1/3; 45/50] END C=1.0902902297685761, class_weight=None, l1_ratio=1.0, tol=0.002537522558441109;, score=0.949 total time=   5.7s
[CV 2/3; 45/50] START C=1.0902902297685761, class_weight=None, l1_ratio=1.0, tol=0.002537522558441109
[CV 2/3; 45/50] END C=1.0902902297685761, class_weight=None, l1_ratio=1.0, tol=0.002537522558441109;, score=0.983 total time=   6.6s
[CV 3/3; 45/50] START C=1.0902902297685761, class_weight=None, l1_ratio=1.0, tol=0.002537522558441109
[CV 3/3; 45/50] END C=1.0902902297685761, class_weight=None, l1_ratio=1.0, tol=0.002537522558441109;, score=0.957 total time=   4.8s
[CV 1/3; 46/50] START C=0.0012098907414761651, class_weight=None, l1_ratio=0.0, tol=0.06432695171814079
[CV 1/3; 46/50] END C=0.0012098907414761651, class_weight=None, l1_ratio=0.0, tol=0.06432695171814079;, score=0.944 total time=   0.4s
[CV 2/3; 46/50] START C=0.0012098907414761651, class_weight=None, l1_ratio=0.0, tol=0.06432695171814079
[CV 2/3; 46/50] END C=0.0012098907414761651, class_weight=None, l1_ratio=0.0, tol=0.06432695171814079;, score=0.949 total time=   0.4s
[CV 3/3; 46/50] START C=0.0012098907414761651, class_weight=None, l1_ratio=0.0, tol=0.06432695171814079
[CV 3/3; 46/50] END C=0.0012098907414761651, class_weight=None, l1_ratio=0.0, tol=0.06432695171814079;, score=0.929 total time=   0.4s
[CV 1/3; 47/50] START C=0.07849988964303667, class_weight=balanced, l1_ratio=0.0, tol=0.026613948116312562
[CV 1/3; 47/50] END C=0.07849988964303667, class_weight=balanced, l1_ratio=0.0, tol=0.026613948116312562;, score=0.935 total time=   0.7s
[CV 2/3; 47/50] START C=0.07849988964303667, class_weight=balanced, l1_ratio=0.0, tol=0.026613948116312562
[CV 2/3; 47/50] END C=0.07849988964303667, class_weight=balanced, l1_ratio=0.0, tol=0.026613948116312562;, score=0.975 total time=   0.7s
[CV 3/3; 47/50] START C=0.07849988964303667, class_weight=balanced, l1_ratio=0.0, tol=0.026613948116312562
[CV 3/3; 47/50] END C=0.07849988964303667, class_weight=balanced, l1_ratio=0.0, tol=0.026613948116312562;, score=0.953 total time=   0.7s
[CV 1/3; 48/50] START C=0.08722477098860842, class_weight=balanced, l1_ratio=0.0, tol=0.014370786160752273
[CV 1/3; 48/50] END C=0.08722477098860842, class_weight=balanced, l1_ratio=0.0, tol=0.014370786160752273;, score=0.936 total time=   0.9s
[CV 2/3; 48/50] START C=0.08722477098860842, class_weight=balanced, l1_ratio=0.0, tol=0.014370786160752273
[CV 2/3; 48/50] END C=0.08722477098860842, class_weight=balanced, l1_ratio=0.0, tol=0.014370786160752273;, score=0.978 total time=   0.9s
[CV 3/3; 48/50] START C=0.08722477098860842, class_weight=balanced, l1_ratio=0.0, tol=0.014370786160752273
[CV 3/3; 48/50] END C=0.08722477098860842, class_weight=balanced, l1_ratio=0.0, tol=0.014370786160752273;, score=0.951 total time=   0.8s
[CV 1/3; 49/50] START C=0.3218150595982378, class_weight=None, l1_ratio=0.0, tol=0.014441938198517324
[CV 1/3; 49/50] END C=0.3218150595982378, class_weight=None, l1_ratio=0.0, tol=0.014441938198517324;, score=0.950 total time=   0.8s
[CV 2/3; 49/50] START C=0.3218150595982378, class_weight=None, l1_ratio=0.0, tol=0.014441938198517324
[CV 2/3; 49/50] END C=0.3218150595982378, class_weight=None, l1_ratio=0.0, tol=0.014441938198517324;, score=0.972 total time=   0.8s
[CV 3/3; 49/50] START C=0.3218150595982378, class_weight=None, l1_ratio=0.0, tol=0.014441938198517324
[CV 3/3; 49/50] END C=0.3218150595982378, class_weight=None, l1_ratio=0.0, tol=0.014441938198517324;, score=0.948 total time=   0.8s
[CV 1/3; 50/50] START C=0.2770278253617821, class_weight=None, l1_ratio=0.0, tol=0.0019489213147753446
[CV 1/3; 50/50] END C=0.2770278253617821, class_weight=None, l1_ratio=0.0, tol=0.0019489213147753446;, score=0.948 total time=   4.8s
[CV 2/3; 50/50] START C=0.2770278253617821, class_weight=None, l1_ratio=0.0, tol=0.0019489213147753446
[CV 2/3; 50/50] END C=0.2770278253617821, class_weight=None, l1_ratio=0.0, tol=0.0019489213147753446;, score=0.983 total time=   5.0s
[CV 3/3; 50/50] START C=0.2770278253617821, class_weight=None, l1_ratio=0.0, tol=0.0019489213147753446
[CV 3/3; 50/50] END C=0.2770278253617821, class_weight=None, l1_ratio=0.0, tol=0.0019489213147753446;, score=0.959 total time=   4.5s

--- TUNING FINISHED ---
Beste Parameter: {'C': np.float64(0.2770278253617821), 'class_weight': None, 'l1_ratio': 0.0, 'tol': np.float64(0.0019489213147753446)}
Bester CV-Score: 0.9631

--- EVALUATION AUF DEN TESTDATEN ---
Test Accuracy: 0.9148

Macro F1: 0.8929587750898407

--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9148

                     precision    recall  f1-score   support

             B cell       1.00      0.96      0.98       120
     CD14+ monocyte       1.00      1.00      1.00      2575
        CD4+ T cell       0.93      0.99      0.96      3910
   Cytotoxic T cell       0.88      0.69      0.77      1824
     Dendritic cell       1.00      0.60      0.75         5
      Megakaryocyte       1.00      1.00      1.00         7
Natural killer cell       0.65      0.77      0.70       791
        Plasma cell       1.00      0.96      0.98        49

           accuracy                           0.91      9281
          macro avg       0.93      0.87      0.89      9281
       weighted avg       0.92      0.91      0.91      9281

Random dropout accuracy score 0.9031
Total samples: 9281
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.9127
Feature importance dropout (0.5% features dropped) accuracy score 0.8909
Feature importance dropout (1.0% features dropped) accuracy score 0.8603
Feature importance dropout (2.0% features dropped) accuracy score 0.8303
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8669

                     precision    recall  f1-score   support

             B cell       1.00      0.96      0.98      3960
     CD14+ monocyte       0.81      1.00      0.89      3135
        CD4+ T cell       0.92      0.98      0.95     13677
   Cytotoxic T cell       0.73      0.58      0.65      4843
     Dendritic cell       0.99      0.49      0.66       529
      Megakaryocyte       1.00      0.77      0.87        86
Natural killer cell       0.65      0.62      0.63      2751
        Plasma cell       0.96      1.00      0.98        23

           accuracy                           0.87     29004
          macro avg       0.88      0.80      0.83     29004
       weighted avg       0.86      0.87      0.86     29004

Random dropout accuracy score 0.8457
Total samples: 29004
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.8624
Feature importance dropout (0.5% features dropped) accuracy score 0.8341
Feature importance dropout (1.0% features dropped) accuracy score 0.7975
Feature importance dropout (2.0% features dropped) accuracy score 0.7262
=== JOB_STATISTICS ===
=== current date     : Sat Jun 27 17:22:05 CEST 2026
= Job-ID             : 11995953 on woody
= Job-Name           : conditional_autoencoder_lr
= Job-Command        : /home/hpc/iwbn/iwbn133h/submit_conditional_autoencoder_lr_v1.sh
= Initial workdir    : /home/hpc/iwbn/iwbn133h
= Queue/Partition    : work
= Slurm account      : iwbn with QOS=normal
= Features           : icx
= Requested resources:  for 17:00:00
= Elapsed runtime    : 01:07:13
= Total RAM usage    : 20.8 GiB of requested  GiB (%)   
= Node list          : w2518
= Subm/Elig/Start/End: 2026-06-27T16:14:51 / 2026-06-27T16:14:51 / 2026-06-27T16:14:52 / 2026-06-27T17:22:05
======================
=== Quota infos ======
    Path                 Used     SoftQ    HardQ    Gracetime  Filec    FileQ    FiHaQ    FileGrace    
    /home/woody           982.1M  1000.0G  1500.0G        N/A  29,019    5,000K   7,500K        N/A    
    /home/hpc              86.2G   104.9G   209.7G        N/A     139K     500K   1,000K        N/A    
    /home/vault             0.0K  1048.6G  2097.2G        N/A       1      200K     400K        N/A    
