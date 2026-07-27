### Starting TaskPrologue of job 11997760 on w2215 at Sun Jun 28 22:16:49 CEST 2026
#   SLURM_JOB_NODELIST=w2215
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
Epoch [1/150], Loss: 0.9432
Epoch [10/150], Loss: 0.9067
Epoch [20/150], Loss: 0.9001
Epoch [30/150], Loss: 0.8960
Epoch [40/150], Loss: 0.8943
Epoch [50/150], Loss: 0.8927
Epoch [60/150], Loss: 0.8913
Epoch [70/150], Loss: 0.8908
Early Stopping after [72/150] Epochs!

Extract robust features...
Starte automatische Hyperparametersuche auf dem Latent Space...
Fitting 3 folds for each of 50 candidates, totalling 150 fits
[CV 1/3; 1/50] START C=0.02713553117977271, class_weight=None, dual=True, penalty=l2, tol=0.01298017600524389
[CV 1/3; 1/50] END C=0.02713553117977271, class_weight=None, dual=True, penalty=l2, tol=0.01298017600524389;, score=0.929 total time=   1.2s
[CV 2/3; 1/50] START C=0.02713553117977271, class_weight=None, dual=True, penalty=l2, tol=0.01298017600524389
[CV 2/3; 1/50] END C=0.02713553117977271, class_weight=None, dual=True, penalty=l2, tol=0.01298017600524389;, score=0.982 total time=   2.1s
[CV 3/3; 1/50] START C=0.02713553117977271, class_weight=None, dual=True, penalty=l2, tol=0.01298017600524389
[CV 3/3; 1/50] END C=0.02713553117977271, class_weight=None, dual=True, penalty=l2, tol=0.01298017600524389;, score=0.964 total time=   1.8s
[CV 1/3; 2/50] START C=0.00322480435137453, class_weight=balanced, dual=False, penalty=l2, tol=0.017031980615966523
[CV 1/3; 2/50] END C=0.00322480435137453, class_weight=balanced, dual=False, penalty=l2, tol=0.017031980615966523;, score=0.934 total time=   1.3s
[CV 2/3; 2/50] START C=0.00322480435137453, class_weight=balanced, dual=False, penalty=l2, tol=0.017031980615966523
[CV 2/3; 2/50] END C=0.00322480435137453, class_weight=balanced, dual=False, penalty=l2, tol=0.017031980615966523;, score=0.982 total time=   3.3s
[CV 3/3; 2/50] START C=0.00322480435137453, class_weight=balanced, dual=False, penalty=l2, tol=0.017031980615966523
[CV 3/3; 2/50] END C=0.00322480435137453, class_weight=balanced, dual=False, penalty=l2, tol=0.017031980615966523;, score=0.967 total time=   1.5s
[CV 1/3; 3/50] START C=0.4784424032061752, class_weight=None, dual=True, penalty=l2, tol=0.005468970047727093
[CV 1/3; 3/50] END C=0.4784424032061752, class_weight=None, dual=True, penalty=l2, tol=0.005468970047727093;, score=0.925 total time=   1.5s
[CV 2/3; 3/50] START C=0.4784424032061752, class_weight=None, dual=True, penalty=l2, tol=0.005468970047727093
[CV 2/3; 3/50] END C=0.4784424032061752, class_weight=None, dual=True, penalty=l2, tol=0.005468970047727093;, score=0.981 total time=   3.6s
[CV 3/3; 3/50] START C=0.4784424032061752, class_weight=None, dual=True, penalty=l2, tol=0.005468970047727093
[CV 3/3; 3/50] END C=0.4784424032061752, class_weight=None, dual=True, penalty=l2, tol=0.005468970047727093;, score=0.960 total time=   2.7s
[CV 1/3; 4/50] START C=0.22738666242504585, class_weight=None, dual=False, penalty=l2, tol=0.001062671185725568
[CV 1/3; 4/50] END C=0.22738666242504585, class_weight=None, dual=False, penalty=l2, tol=0.001062671185725568;, score=0.928 total time=   1.7s
[CV 2/3; 4/50] START C=0.22738666242504585, class_weight=None, dual=False, penalty=l2, tol=0.001062671185725568
[CV 2/3; 4/50] END C=0.22738666242504585, class_weight=None, dual=False, penalty=l2, tol=0.001062671185725568;, score=0.981 total time=   2.3s
[CV 3/3; 4/50] START C=0.22738666242504585, class_weight=None, dual=False, penalty=l2, tol=0.001062671185725568
[CV 3/3; 4/50] END C=0.22738666242504585, class_weight=None, dual=False, penalty=l2, tol=0.001062671185725568;, score=0.964 total time=   1.8s
[CV 1/3; 5/50] START C=0.024921158450804826, class_weight=balanced, dual=False, penalty=l2, tol=0.010300673338746666
[CV 1/3; 5/50] END C=0.024921158450804826, class_weight=balanced, dual=False, penalty=l2, tol=0.010300673338746666;, score=0.925 total time=   2.5s
[CV 2/3; 5/50] START C=0.024921158450804826, class_weight=balanced, dual=False, penalty=l2, tol=0.010300673338746666
[CV 2/3; 5/50] END C=0.024921158450804826, class_weight=balanced, dual=False, penalty=l2, tol=0.010300673338746666;, score=0.983 total time=   5.0s
[CV 3/3; 5/50] START C=0.024921158450804826, class_weight=balanced, dual=False, penalty=l2, tol=0.010300673338746666
[CV 3/3; 5/50] END C=0.024921158450804826, class_weight=balanced, dual=False, penalty=l2, tol=0.010300673338746666;, score=0.967 total time=   4.5s
[CV 1/3; 6/50] START C=0.9619750057495978, class_weight=balanced, dual=True, penalty=l2, tol=0.0024233821432785236
[CV 1/3; 6/50] END C=0.9619750057495978, class_weight=balanced, dual=True, penalty=l2, tol=0.0024233821432785236;, score=0.926 total time=   1.5s
[CV 2/3; 6/50] START C=0.9619750057495978, class_weight=balanced, dual=True, penalty=l2, tol=0.0024233821432785236
[CV 2/3; 6/50] END C=0.9619750057495978, class_weight=balanced, dual=True, penalty=l2, tol=0.0024233821432785236;, score=0.974 total time=   3.4s
[CV 3/3; 6/50] START C=0.9619750057495978, class_weight=balanced, dual=True, penalty=l2, tol=0.0024233821432785236
[CV 3/3; 6/50] END C=0.9619750057495978, class_weight=balanced, dual=True, penalty=l2, tol=0.0024233821432785236;, score=0.941 total time=   2.6s
[CV 1/3; 7/50] START C=0.01642613557581926, class_weight=None, dual=True, penalty=l2, tol=0.0046486869423979435
[CV 1/3; 7/50] END C=0.01642613557581926, class_weight=None, dual=True, penalty=l2, tol=0.0046486869423979435;, score=0.929 total time=   1.2s
[CV 2/3; 7/50] START C=0.01642613557581926, class_weight=None, dual=True, penalty=l2, tol=0.0046486869423979435
[CV 2/3; 7/50] END C=0.01642613557581926, class_weight=None, dual=True, penalty=l2, tol=0.0046486869423979435;, score=0.982 total time=   2.0s
[CV 3/3; 7/50] START C=0.01642613557581926, class_weight=None, dual=True, penalty=l2, tol=0.0046486869423979435
[CV 3/3; 7/50] END C=0.01642613557581926, class_weight=None, dual=True, penalty=l2, tol=0.0046486869423979435;, score=0.963 total time=   1.8s
[CV 1/3; 8/50] START C=0.4229495883478086, class_weight=balanced, dual=False, penalty=l2, tol=0.011577074769465618
[CV 1/3; 8/50] END C=0.4229495883478086, class_weight=balanced, dual=False, penalty=l2, tol=0.011577074769465618;, score=0.926 total time=   2.6s
[CV 2/3; 8/50] START C=0.4229495883478086, class_weight=balanced, dual=False, penalty=l2, tol=0.011577074769465618
[CV 2/3; 8/50] END C=0.4229495883478086, class_weight=balanced, dual=False, penalty=l2, tol=0.011577074769465618;, score=0.983 total time=   5.1s
[CV 3/3; 8/50] START C=0.4229495883478086, class_weight=balanced, dual=False, penalty=l2, tol=0.011577074769465618
[CV 3/3; 8/50] END C=0.4229495883478086, class_weight=balanced, dual=False, penalty=l2, tol=0.011577074769465618;, score=0.967 total time=   4.1s
[CV 1/3; 9/50] START C=0.41096357599659245, class_weight=None, dual=True, penalty=l2, tol=0.06193689404600351
[CV 1/3; 9/50] END C=0.41096357599659245, class_weight=None, dual=True, penalty=l2, tol=0.06193689404600351;, score=0.931 total time=   1.4s
[CV 2/3; 9/50] START C=0.41096357599659245, class_weight=None, dual=True, penalty=l2, tol=0.06193689404600351
[CV 2/3; 9/50] END C=0.41096357599659245, class_weight=None, dual=True, penalty=l2, tol=0.06193689404600351;, score=0.982 total time=   3.6s
[CV 3/3; 9/50] START C=0.41096357599659245, class_weight=None, dual=True, penalty=l2, tol=0.06193689404600351
[CV 3/3; 9/50] END C=0.41096357599659245, class_weight=None, dual=True, penalty=l2, tol=0.06193689404600351;, score=0.959 total time=   2.6s
[CV 1/3; 10/50] START C=0.2347251242949309, class_weight=None, dual=True, penalty=l2, tol=0.04482024201928143
[CV 1/3; 10/50] END C=0.2347251242949309, class_weight=None, dual=True, penalty=l2, tol=0.04482024201928143;, score=0.925 total time=   1.5s
[CV 2/3; 10/50] START C=0.2347251242949309, class_weight=None, dual=True, penalty=l2, tol=0.04482024201928143
[CV 2/3; 10/50] END C=0.2347251242949309, class_weight=None, dual=True, penalty=l2, tol=0.04482024201928143;, score=0.982 total time=   3.3s
[CV 3/3; 10/50] START C=0.2347251242949309, class_weight=None, dual=True, penalty=l2, tol=0.04482024201928143
[CV 3/3; 10/50] END C=0.2347251242949309, class_weight=None, dual=True, penalty=l2, tol=0.04482024201928143;, score=0.961 total time=   2.5s
[CV 1/3; 11/50] START C=0.26225285370842927, class_weight=balanced, dual=False, penalty=l2, tol=0.08198159166489095
[CV 1/3; 11/50] END C=0.26225285370842927, class_weight=balanced, dual=False, penalty=l2, tol=0.08198159166489095;, score=0.934 total time=   0.8s
[CV 2/3; 11/50] START C=0.26225285370842927, class_weight=balanced, dual=False, penalty=l2, tol=0.08198159166489095
[CV 2/3; 11/50] END C=0.26225285370842927, class_weight=balanced, dual=False, penalty=l2, tol=0.08198159166489095;, score=0.982 total time=   1.3s
[CV 3/3; 11/50] START C=0.26225285370842927, class_weight=balanced, dual=False, penalty=l2, tol=0.08198159166489095
[CV 3/3; 11/50] END C=0.26225285370842927, class_weight=balanced, dual=False, penalty=l2, tol=0.08198159166489095;, score=0.963 total time=   1.0s
[CV 1/3; 12/50] START C=0.49015649358459673, class_weight=None, dual=False, penalty=l2, tol=0.009711906016230886
[CV 1/3; 12/50] END C=0.49015649358459673, class_weight=None, dual=False, penalty=l2, tol=0.009711906016230886;, score=0.928 total time=   0.9s
[CV 2/3; 12/50] START C=0.49015649358459673, class_weight=None, dual=False, penalty=l2, tol=0.009711906016230886
[CV 2/3; 12/50] END C=0.49015649358459673, class_weight=None, dual=False, penalty=l2, tol=0.009711906016230886;, score=0.982 total time=   1.0s
[CV 3/3; 12/50] START C=0.49015649358459673, class_weight=None, dual=False, penalty=l2, tol=0.009711906016230886
[CV 3/3; 12/50] END C=0.49015649358459673, class_weight=None, dual=False, penalty=l2, tol=0.009711906016230886;, score=0.965 total time=   0.9s
[CV 1/3; 13/50] START C=1.1054221634333024, class_weight=None, dual=True, penalty=l2, tol=0.001363701557596002
[CV 1/3; 13/50] END C=1.1054221634333024, class_weight=None, dual=True, penalty=l2, tol=0.001363701557596002;, score=0.926 total time=   1.5s
[CV 2/3; 13/50] START C=1.1054221634333024, class_weight=None, dual=True, penalty=l2, tol=0.001363701557596002
[CV 2/3; 13/50] END C=1.1054221634333024, class_weight=None, dual=True, penalty=l2, tol=0.001363701557596002;, score=0.982 total time=   3.7s
[CV 3/3; 13/50] START C=1.1054221634333024, class_weight=None, dual=True, penalty=l2, tol=0.001363701557596002
[CV 3/3; 13/50] END C=1.1054221634333024, class_weight=None, dual=True, penalty=l2, tol=0.001363701557596002;, score=0.960 total time=   2.9s
[CV 1/3; 14/50] START C=0.02681924312357274, class_weight=balanced, dual=True, penalty=l2, tol=0.0019420434312585142
[CV 1/3; 14/50] END C=0.02681924312357274, class_weight=balanced, dual=True, penalty=l2, tol=0.0019420434312585142;, score=0.922 total time=   1.2s
[CV 2/3; 14/50] START C=0.02681924312357274, class_weight=balanced, dual=True, penalty=l2, tol=0.0019420434312585142
[CV 2/3; 14/50] END C=0.02681924312357274, class_weight=balanced, dual=True, penalty=l2, tol=0.0019420434312585142;, score=0.983 total time=   2.1s
[CV 3/3; 14/50] START C=0.02681924312357274, class_weight=balanced, dual=True, penalty=l2, tol=0.0019420434312585142
[CV 3/3; 14/50] END C=0.02681924312357274, class_weight=balanced, dual=True, penalty=l2, tol=0.0019420434312585142;, score=0.964 total time=   1.8s
[CV 1/3; 15/50] START C=0.12147484211690987, class_weight=balanced, dual=True, penalty=l2, tol=0.0408605913263294
[CV 1/3; 15/50] END C=0.12147484211690987, class_weight=balanced, dual=True, penalty=l2, tol=0.0408605913263294;, score=0.920 total time=   1.3s
[CV 2/3; 15/50] START C=0.12147484211690987, class_weight=balanced, dual=True, penalty=l2, tol=0.0408605913263294
[CV 2/3; 15/50] END C=0.12147484211690987, class_weight=balanced, dual=True, penalty=l2, tol=0.0408605913263294;, score=0.983 total time=   2.5s
[CV 3/3; 15/50] START C=0.12147484211690987, class_weight=balanced, dual=True, penalty=l2, tol=0.0408605913263294
[CV 3/3; 15/50] END C=0.12147484211690987, class_weight=balanced, dual=True, penalty=l2, tol=0.0408605913263294;, score=0.962 total time=   2.1s
[CV 1/3; 16/50] START C=0.043530935042477695, class_weight=balanced, dual=False, penalty=l2, tol=0.0014765328156670092
[CV 1/3; 16/50] END C=0.043530935042477695, class_weight=balanced, dual=False, penalty=l2, tol=0.0014765328156670092;, score=0.923 total time=   9.4s
[CV 2/3; 16/50] START C=0.043530935042477695, class_weight=balanced, dual=False, penalty=l2, tol=0.0014765328156670092
[CV 2/3; 16/50] END C=0.043530935042477695, class_weight=balanced, dual=False, penalty=l2, tol=0.0014765328156670092;, score=0.983 total time=   8.7s
[CV 3/3; 16/50] START C=0.043530935042477695, class_weight=balanced, dual=False, penalty=l2, tol=0.0014765328156670092
[CV 3/3; 16/50] END C=0.043530935042477695, class_weight=balanced, dual=False, penalty=l2, tol=0.0014765328156670092;, score=0.967 total time=   9.2s
[CV 1/3; 17/50] START C=0.02815970619651485, class_weight=balanced, dual=False, penalty=l2, tol=0.0582000892505476
[CV 1/3; 17/50] END C=0.02815970619651485, class_weight=balanced, dual=False, penalty=l2, tol=0.0582000892505476;, score=0.934 total time=   0.9s
[CV 2/3; 17/50] START C=0.02815970619651485, class_weight=balanced, dual=False, penalty=l2, tol=0.0582000892505476
[CV 2/3; 17/50] END C=0.02815970619651485, class_weight=balanced, dual=False, penalty=l2, tol=0.0582000892505476;, score=0.982 total time=   1.4s
[CV 3/3; 17/50] START C=0.02815970619651485, class_weight=balanced, dual=False, penalty=l2, tol=0.0582000892505476
[CV 3/3; 17/50] END C=0.02815970619651485, class_weight=balanced, dual=False, penalty=l2, tol=0.0582000892505476;, score=0.963 total time=   1.1s
[CV 1/3; 18/50] START C=0.4720653500056923, class_weight=balanced, dual=True, penalty=l2, tol=0.005555115629155375
[CV 1/3; 18/50] END C=0.4720653500056923, class_weight=balanced, dual=True, penalty=l2, tol=0.005555115629155375;, score=0.921 total time=   1.4s
[CV 2/3; 18/50] START C=0.4720653500056923, class_weight=balanced, dual=True, penalty=l2, tol=0.005555115629155375
[CV 2/3; 18/50] END C=0.4720653500056923, class_weight=balanced, dual=True, penalty=l2, tol=0.005555115629155375;, score=0.974 total time=   3.3s
[CV 3/3; 18/50] START C=0.4720653500056923, class_weight=balanced, dual=True, penalty=l2, tol=0.005555115629155375
[CV 3/3; 18/50] END C=0.4720653500056923, class_weight=balanced, dual=True, penalty=l2, tol=0.005555115629155375;, score=0.960 total time=   2.5s
[CV 1/3; 19/50] START C=1.3240710272406953, class_weight=None, dual=True, penalty=l2, tol=0.05495899544682988
[CV 1/3; 19/50] END C=1.3240710272406953, class_weight=None, dual=True, penalty=l2, tol=0.05495899544682988;, score=0.922 total time=   1.5s
[CV 2/3; 19/50] START C=1.3240710272406953, class_weight=None, dual=True, penalty=l2, tol=0.05495899544682988
[CV 2/3; 19/50] END C=1.3240710272406953, class_weight=None, dual=True, penalty=l2, tol=0.05495899544682988;, score=0.981 total time=   3.8s
[CV 3/3; 19/50] START C=1.3240710272406953, class_weight=None, dual=True, penalty=l2, tol=0.05495899544682988
[CV 3/3; 19/50] END C=1.3240710272406953, class_weight=None, dual=True, penalty=l2, tol=0.05495899544682988;, score=0.959 total time=   3.0s
[CV 1/3; 20/50] START C=0.004012060296805565, class_weight=None, dual=False, penalty=l2, tol=0.0010674656122210261
[CV 1/3; 20/50] END C=0.004012060296805565, class_weight=None, dual=False, penalty=l2, tol=0.0010674656122210261;, score=0.933 total time=   1.1s
[CV 2/3; 20/50] START C=0.004012060296805565, class_weight=None, dual=False, penalty=l2, tol=0.0010674656122210261
[CV 2/3; 20/50] END C=0.004012060296805565, class_weight=None, dual=False, penalty=l2, tol=0.0010674656122210261;, score=0.982 total time=   1.1s
[CV 3/3; 20/50] START C=0.004012060296805565, class_weight=None, dual=False, penalty=l2, tol=0.0010674656122210261
[CV 3/3; 20/50] END C=0.004012060296805565, class_weight=None, dual=False, penalty=l2, tol=0.0010674656122210261;, score=0.964 total time=   1.1s
[CV 1/3; 21/50] START C=0.42588156080021533, class_weight=None, dual=False, penalty=l2, tol=0.00991457887668963
[CV 1/3; 21/50] END C=0.42588156080021533, class_weight=None, dual=False, penalty=l2, tol=0.00991457887668963;, score=0.927 total time=   0.9s
[CV 2/3; 21/50] START C=0.42588156080021533, class_weight=None, dual=False, penalty=l2, tol=0.00991457887668963
[CV 2/3; 21/50] END C=0.42588156080021533, class_weight=None, dual=False, penalty=l2, tol=0.00991457887668963;, score=0.982 total time=   1.0s
[CV 3/3; 21/50] START C=0.42588156080021533, class_weight=None, dual=False, penalty=l2, tol=0.00991457887668963
[CV 3/3; 21/50] END C=0.42588156080021533, class_weight=None, dual=False, penalty=l2, tol=0.00991457887668963;, score=0.965 total time=   0.9s
[CV 1/3; 22/50] START C=0.11807253332807406, class_weight=balanced, dual=False, penalty=l2, tol=0.09918190628411366
[CV 1/3; 22/50] END C=0.11807253332807406, class_weight=balanced, dual=False, penalty=l2, tol=0.09918190628411366;, score=0.935 total time=   0.8s
[CV 2/3; 22/50] START C=0.11807253332807406, class_weight=balanced, dual=False, penalty=l2, tol=0.09918190628411366
[CV 2/3; 22/50] END C=0.11807253332807406, class_weight=balanced, dual=False, penalty=l2, tol=0.09918190628411366;, score=0.981 total time=   1.1s
[CV 3/3; 22/50] START C=0.11807253332807406, class_weight=balanced, dual=False, penalty=l2, tol=0.09918190628411366
[CV 3/3; 22/50] END C=0.11807253332807406, class_weight=balanced, dual=False, penalty=l2, tol=0.09918190628411366;, score=0.964 total time=   0.9s
[CV 1/3; 23/50] START C=0.04446570742942174, class_weight=balanced, dual=True, penalty=l2, tol=0.0023844164426053784
[CV 1/3; 23/50] END C=0.04446570742942174, class_weight=balanced, dual=True, penalty=l2, tol=0.0023844164426053784;, score=0.922 total time=   1.2s
[CV 2/3; 23/50] START C=0.04446570742942174, class_weight=balanced, dual=True, penalty=l2, tol=0.0023844164426053784
[CV 2/3; 23/50] END C=0.04446570742942174, class_weight=balanced, dual=True, penalty=l2, tol=0.0023844164426053784;, score=0.982 total time=   2.2s
[CV 3/3; 23/50] START C=0.04446570742942174, class_weight=balanced, dual=True, penalty=l2, tol=0.0023844164426053784
[CV 3/3; 23/50] END C=0.04446570742942174, class_weight=balanced, dual=True, penalty=l2, tol=0.0023844164426053784;, score=0.963 total time=   1.9s
[CV 1/3; 24/50] START C=0.10879661814088723, class_weight=None, dual=False, penalty=l2, tol=0.010455797240240296
[CV 1/3; 24/50] END C=0.10879661814088723, class_weight=None, dual=False, penalty=l2, tol=0.010455797240240296;, score=0.927 total time=   0.9s
[CV 2/3; 24/50] START C=0.10879661814088723, class_weight=None, dual=False, penalty=l2, tol=0.010455797240240296
[CV 2/3; 24/50] END C=0.10879661814088723, class_weight=None, dual=False, penalty=l2, tol=0.010455797240240296;, score=0.982 total time=   1.0s
[CV 3/3; 24/50] START C=0.10879661814088723, class_weight=None, dual=False, penalty=l2, tol=0.010455797240240296
[CV 3/3; 24/50] END C=0.10879661814088723, class_weight=None, dual=False, penalty=l2, tol=0.010455797240240296;, score=0.965 total time=   0.9s
[CV 1/3; 25/50] START C=0.4565447945307245, class_weight=balanced, dual=False, penalty=l2, tol=0.01105925830595341
[CV 1/3; 25/50] END C=0.4565447945307245, class_weight=balanced, dual=False, penalty=l2, tol=0.01105925830595341;, score=0.926 total time=   2.6s
[CV 2/3; 25/50] START C=0.4565447945307245, class_weight=balanced, dual=False, penalty=l2, tol=0.01105925830595341
[CV 2/3; 25/50] END C=0.4565447945307245, class_weight=balanced, dual=False, penalty=l2, tol=0.01105925830595341;, score=0.983 total time=   4.8s
[CV 3/3; 25/50] START C=0.4565447945307245, class_weight=balanced, dual=False, penalty=l2, tol=0.01105925830595341
[CV 3/3; 25/50] END C=0.4565447945307245, class_weight=balanced, dual=False, penalty=l2, tol=0.01105925830595341;, score=0.967 total time=   4.3s
[CV 1/3; 26/50] START C=0.08634934067879706, class_weight=balanced, dual=False, penalty=l2, tol=0.010011232360519538
[CV 1/3; 26/50] END C=0.08634934067879706, class_weight=balanced, dual=False, penalty=l2, tol=0.010011232360519538;, score=0.925 total time=   2.5s
[CV 2/3; 26/50] START C=0.08634934067879706, class_weight=balanced, dual=False, penalty=l2, tol=0.010011232360519538
[CV 2/3; 26/50] END C=0.08634934067879706, class_weight=balanced, dual=False, penalty=l2, tol=0.010011232360519538;, score=0.983 total time=   4.9s
[CV 3/3; 26/50] START C=0.08634934067879706, class_weight=balanced, dual=False, penalty=l2, tol=0.010011232360519538
[CV 3/3; 26/50] END C=0.08634934067879706, class_weight=balanced, dual=False, penalty=l2, tol=0.010011232360519538;, score=0.967 total time=   3.8s
[CV 1/3; 27/50] START C=0.0588060995697123, class_weight=balanced, dual=False, penalty=l2, tol=0.026727192207301836
[CV 1/3; 27/50] END C=0.0588060995697123, class_weight=balanced, dual=False, penalty=l2, tol=0.026727192207301836;, score=0.933 total time=   1.3s
[CV 2/3; 27/50] START C=0.0588060995697123, class_weight=balanced, dual=False, penalty=l2, tol=0.026727192207301836
[CV 2/3; 27/50] END C=0.0588060995697123, class_weight=balanced, dual=False, penalty=l2, tol=0.026727192207301836;, score=0.983 total time=   4.1s
[CV 3/3; 27/50] START C=0.0588060995697123, class_weight=balanced, dual=False, penalty=l2, tol=0.026727192207301836
[CV 3/3; 27/50] END C=0.0588060995697123, class_weight=balanced, dual=False, penalty=l2, tol=0.026727192207301836;, score=0.965 total time=   1.6s
[CV 1/3; 28/50] START C=1.7309690241070206, class_weight=balanced, dual=False, penalty=l2, tol=0.08173306815369562
[CV 1/3; 28/50] END C=1.7309690241070206, class_weight=balanced, dual=False, penalty=l2, tol=0.08173306815369562;, score=0.934 total time=   0.8s
[CV 2/3; 28/50] START C=1.7309690241070206, class_weight=balanced, dual=False, penalty=l2, tol=0.08173306815369562
[CV 2/3; 28/50] END C=1.7309690241070206, class_weight=balanced, dual=False, penalty=l2, tol=0.08173306815369562;, score=0.982 total time=   1.3s
[CV 3/3; 28/50] START C=1.7309690241070206, class_weight=balanced, dual=False, penalty=l2, tol=0.08173306815369562
[CV 3/3; 28/50] END C=1.7309690241070206, class_weight=balanced, dual=False, penalty=l2, tol=0.08173306815369562;, score=0.963 total time=   1.0s
[CV 1/3; 29/50] START C=0.0017684599439626678, class_weight=None, dual=False, penalty=l2, tol=0.0017659125923509835
[CV 1/3; 29/50] END C=0.0017684599439626678, class_weight=None, dual=False, penalty=l2, tol=0.0017659125923509835;, score=0.935 total time=   0.9s
[CV 2/3; 29/50] START C=0.0017684599439626678, class_weight=None, dual=False, penalty=l2, tol=0.0017659125923509835
[CV 2/3; 29/50] END C=0.0017684599439626678, class_weight=None, dual=False, penalty=l2, tol=0.0017659125923509835;, score=0.982 total time=   0.9s
[CV 3/3; 29/50] START C=0.0017684599439626678, class_weight=None, dual=False, penalty=l2, tol=0.0017659125923509835
[CV 3/3; 29/50] END C=0.0017684599439626678, class_weight=None, dual=False, penalty=l2, tol=0.0017659125923509835;, score=0.964 total time=   0.9s
[CV 1/3; 30/50] START C=0.7867385039166283, class_weight=None, dual=True, penalty=l2, tol=0.0011062740233972305
[CV 1/3; 30/50] END C=0.7867385039166283, class_weight=None, dual=True, penalty=l2, tol=0.0011062740233972305;, score=0.927 total time=   1.6s
[CV 2/3; 30/50] START C=0.7867385039166283, class_weight=None, dual=True, penalty=l2, tol=0.0011062740233972305
[CV 2/3; 30/50] END C=0.7867385039166283, class_weight=None, dual=True, penalty=l2, tol=0.0011062740233972305;, score=0.979 total time=   3.6s
[CV 3/3; 30/50] START C=0.7867385039166283, class_weight=None, dual=True, penalty=l2, tol=0.0011062740233972305
[CV 3/3; 30/50] END C=0.7867385039166283, class_weight=None, dual=True, penalty=l2, tol=0.0011062740233972305;, score=0.960 total time=   2.8s
[CV 1/3; 31/50] START C=0.16780497239152656, class_weight=None, dual=False, penalty=l2, tol=0.017655821244158775
[CV 1/3; 31/50] END C=0.16780497239152656, class_weight=None, dual=False, penalty=l2, tol=0.017655821244158775;, score=0.930 total time=   0.8s
[CV 2/3; 31/50] START C=0.16780497239152656, class_weight=None, dual=False, penalty=l2, tol=0.017655821244158775
[CV 2/3; 31/50] END C=0.16780497239152656, class_weight=None, dual=False, penalty=l2, tol=0.017655821244158775;, score=0.982 total time=   0.9s
[CV 3/3; 31/50] START C=0.16780497239152656, class_weight=None, dual=False, penalty=l2, tol=0.017655821244158775
[CV 3/3; 31/50] END C=0.16780497239152656, class_weight=None, dual=False, penalty=l2, tol=0.017655821244158775;, score=0.965 total time=   0.8s
[CV 1/3; 32/50] START C=0.4805903632932722, class_weight=None, dual=True, penalty=l2, tol=0.02636854366763283
[CV 1/3; 32/50] END C=0.4805903632932722, class_weight=None, dual=True, penalty=l2, tol=0.02636854366763283;, score=0.922 total time=   1.5s
[CV 2/3; 32/50] START C=0.4805903632932722, class_weight=None, dual=True, penalty=l2, tol=0.02636854366763283
[CV 2/3; 32/50] END C=0.4805903632932722, class_weight=None, dual=True, penalty=l2, tol=0.02636854366763283;, score=0.981 total time=   3.4s
[CV 3/3; 32/50] START C=0.4805903632932722, class_weight=None, dual=True, penalty=l2, tol=0.02636854366763283
[CV 3/3; 32/50] END C=0.4805903632932722, class_weight=None, dual=True, penalty=l2, tol=0.02636854366763283;, score=0.957 total time=   2.7s
[CV 1/3; 33/50] START C=0.004317049170918766, class_weight=None, dual=True, penalty=l2, tol=0.004390838781674284
[CV 1/3; 33/50] END C=0.004317049170918766, class_weight=None, dual=True, penalty=l2, tol=0.004390838781674284;, score=0.932 total time=   1.2s
[CV 2/3; 33/50] START C=0.004317049170918766, class_weight=None, dual=True, penalty=l2, tol=0.004390838781674284
[CV 2/3; 33/50] END C=0.004317049170918766, class_weight=None, dual=True, penalty=l2, tol=0.004390838781674284;, score=0.982 total time=   1.8s
[CV 3/3; 33/50] START C=0.004317049170918766, class_weight=None, dual=True, penalty=l2, tol=0.004390838781674284
[CV 3/3; 33/50] END C=0.004317049170918766, class_weight=None, dual=True, penalty=l2, tol=0.004390838781674284;, score=0.964 total time=   1.6s
[CV 1/3; 34/50] START C=0.003602351932055802, class_weight=balanced, dual=False, penalty=l2, tol=0.015616279893398812
[CV 1/3; 34/50] END C=0.003602351932055802, class_weight=balanced, dual=False, penalty=l2, tol=0.015616279893398812;, score=0.934 total time=   1.4s
[CV 2/3; 34/50] START C=0.003602351932055802, class_weight=balanced, dual=False, penalty=l2, tol=0.015616279893398812
[CV 2/3; 34/50] END C=0.003602351932055802, class_weight=balanced, dual=False, penalty=l2, tol=0.015616279893398812;, score=0.982 total time=   3.5s
[CV 3/3; 34/50] START C=0.003602351932055802, class_weight=balanced, dual=False, penalty=l2, tol=0.015616279893398812
[CV 3/3; 34/50] END C=0.003602351932055802, class_weight=balanced, dual=False, penalty=l2, tol=0.015616279893398812;, score=0.966 total time=   2.0s
[CV 1/3; 35/50] START C=0.0037416619789474347, class_weight=None, dual=True, penalty=l2, tol=0.005930697612692196
[CV 1/3; 35/50] END C=0.0037416619789474347, class_weight=None, dual=True, penalty=l2, tol=0.005930697612692196;, score=0.932 total time=   1.2s
[CV 2/3; 35/50] START C=0.0037416619789474347, class_weight=None, dual=True, penalty=l2, tol=0.005930697612692196
[CV 2/3; 35/50] END C=0.0037416619789474347, class_weight=None, dual=True, penalty=l2, tol=0.005930697612692196;, score=0.982 total time=   1.8s
[CV 3/3; 35/50] START C=0.0037416619789474347, class_weight=None, dual=True, penalty=l2, tol=0.005930697612692196
[CV 3/3; 35/50] END C=0.0037416619789474347, class_weight=None, dual=True, penalty=l2, tol=0.005930697612692196;, score=0.963 total time=   1.6s
[CV 1/3; 36/50] START C=0.0024631198803032753, class_weight=balanced, dual=False, penalty=l2, tol=0.0145254624026771
[CV 1/3; 36/50] END C=0.0024631198803032753, class_weight=balanced, dual=False, penalty=l2, tol=0.0145254624026771;, score=0.932 total time=   1.4s
[CV 2/3; 36/50] START C=0.0024631198803032753, class_weight=balanced, dual=False, penalty=l2, tol=0.0145254624026771
[CV 2/3; 36/50] END C=0.0024631198803032753, class_weight=balanced, dual=False, penalty=l2, tol=0.0145254624026771;, score=0.983 total time=   3.4s
[CV 3/3; 36/50] START C=0.0024631198803032753, class_weight=balanced, dual=False, penalty=l2, tol=0.0145254624026771
[CV 3/3; 36/50] END C=0.0024631198803032753, class_weight=balanced, dual=False, penalty=l2, tol=0.0145254624026771;, score=0.967 total time=   1.5s
[CV 1/3; 37/50] START C=0.0023810214851491987, class_weight=balanced, dual=False, penalty=l2, tol=0.09122026503129191
[CV 1/3; 37/50] END C=0.0023810214851491987, class_weight=balanced, dual=False, penalty=l2, tol=0.09122026503129191;, score=0.938 total time=   0.8s
[CV 2/3; 37/50] START C=0.0023810214851491987, class_weight=balanced, dual=False, penalty=l2, tol=0.09122026503129191
[CV 2/3; 37/50] END C=0.0023810214851491987, class_weight=balanced, dual=False, penalty=l2, tol=0.09122026503129191;, score=0.981 total time=   1.1s
[CV 3/3; 37/50] START C=0.0023810214851491987, class_weight=balanced, dual=False, penalty=l2, tol=0.09122026503129191
[CV 3/3; 37/50] END C=0.0023810214851491987, class_weight=balanced, dual=False, penalty=l2, tol=0.09122026503129191;, score=0.961 total time=   0.9s
[CV 1/3; 38/50] START C=0.002008360705616894, class_weight=None, dual=True, penalty=l2, tol=0.001444764195480543
[CV 1/3; 38/50] END C=0.002008360705616894, class_weight=None, dual=True, penalty=l2, tol=0.001444764195480543;, score=0.934 total time=   1.1s
[CV 2/3; 38/50] START C=0.002008360705616894, class_weight=None, dual=True, penalty=l2, tol=0.001444764195480543
[CV 2/3; 38/50] END C=0.002008360705616894, class_weight=None, dual=True, penalty=l2, tol=0.001444764195480543;, score=0.982 total time=   1.7s
[CV 3/3; 38/50] START C=0.002008360705616894, class_weight=None, dual=True, penalty=l2, tol=0.001444764195480543
[CV 3/3; 38/50] END C=0.002008360705616894, class_weight=None, dual=True, penalty=l2, tol=0.001444764195480543;, score=0.962 total time=   1.5s
[CV 1/3; 39/50] START C=0.07435405022154257, class_weight=None, dual=False, penalty=l2, tol=0.0038604624148118488
[CV 1/3; 39/50] END C=0.07435405022154257, class_weight=None, dual=False, penalty=l2, tol=0.0038604624148118488;, score=0.928 total time=   1.0s
[CV 2/3; 39/50] START C=0.07435405022154257, class_weight=None, dual=False, penalty=l2, tol=0.0038604624148118488
[CV 2/3; 39/50] END C=0.07435405022154257, class_weight=None, dual=False, penalty=l2, tol=0.0038604624148118488;, score=0.982 total time=   1.3s
[CV 3/3; 39/50] START C=0.07435405022154257, class_weight=None, dual=False, penalty=l2, tol=0.0038604624148118488
[CV 3/3; 39/50] END C=0.07435405022154257, class_weight=None, dual=False, penalty=l2, tol=0.0038604624148118488;, score=0.965 total time=   1.0s
[CV 1/3; 40/50] START C=0.0029924438702118826, class_weight=balanced, dual=True, penalty=l2, tol=0.002024571699514551
[CV 1/3; 40/50] END C=0.0029924438702118826, class_weight=balanced, dual=True, penalty=l2, tol=0.002024571699514551;, score=0.928 total time=   1.2s
[CV 2/3; 40/50] START C=0.0029924438702118826, class_weight=balanced, dual=True, penalty=l2, tol=0.002024571699514551
[CV 2/3; 40/50] END C=0.0029924438702118826, class_weight=balanced, dual=True, penalty=l2, tol=0.002024571699514551;, score=0.983 total time=   1.9s
[CV 3/3; 40/50] START C=0.0029924438702118826, class_weight=balanced, dual=True, penalty=l2, tol=0.002024571699514551
[CV 3/3; 40/50] END C=0.0029924438702118826, class_weight=balanced, dual=True, penalty=l2, tol=0.002024571699514551;, score=0.965 total time=   1.6s
[CV 1/3; 41/50] START C=0.001987865511923017, class_weight=balanced, dual=True, penalty=l2, tol=0.06603856542118988
[CV 1/3; 41/50] END C=0.001987865511923017, class_weight=balanced, dual=True, penalty=l2, tol=0.06603856542118988;, score=0.930 total time=   0.8s
[CV 2/3; 41/50] START C=0.001987865511923017, class_weight=balanced, dual=True, penalty=l2, tol=0.06603856542118988
[CV 2/3; 41/50] END C=0.001987865511923017, class_weight=balanced, dual=True, penalty=l2, tol=0.06603856542118988;, score=0.983 total time=   1.6s
[CV 3/3; 41/50] START C=0.001987865511923017, class_weight=balanced, dual=True, penalty=l2, tol=0.06603856542118988
[CV 3/3; 41/50] END C=0.001987865511923017, class_weight=balanced, dual=True, penalty=l2, tol=0.06603856542118988;, score=0.965 total time=   1.2s
[CV 1/3; 42/50] START C=0.0020887248801548094, class_weight=balanced, dual=False, penalty=l2, tol=0.00415246396660419
[CV 1/3; 42/50] END C=0.0020887248801548094, class_weight=balanced, dual=False, penalty=l2, tol=0.00415246396660419;, score=0.930 total time=   1.8s
[CV 2/3; 42/50] START C=0.0020887248801548094, class_weight=balanced, dual=False, penalty=l2, tol=0.00415246396660419
[CV 2/3; 42/50] END C=0.0020887248801548094, class_weight=balanced, dual=False, penalty=l2, tol=0.00415246396660419;, score=0.983 total time=   4.0s
[CV 3/3; 42/50] START C=0.0020887248801548094, class_weight=balanced, dual=False, penalty=l2, tol=0.00415246396660419
[CV 3/3; 42/50] END C=0.0020887248801548094, class_weight=balanced, dual=False, penalty=l2, tol=0.00415246396660419;, score=0.968 total time=   2.9s
[CV 1/3; 43/50] START C=0.1643022392036837, class_weight=None, dual=False, penalty=l2, tol=0.040305862784383875
[CV 1/3; 43/50] END C=0.1643022392036837, class_weight=None, dual=False, penalty=l2, tol=0.040305862784383875;, score=0.936 total time=   0.8s
[CV 2/3; 43/50] START C=0.1643022392036837, class_weight=None, dual=False, penalty=l2, tol=0.040305862784383875
[CV 2/3; 43/50] END C=0.1643022392036837, class_weight=None, dual=False, penalty=l2, tol=0.040305862784383875;, score=0.982 total time=   0.8s
[CV 3/3; 43/50] START C=0.1643022392036837, class_weight=None, dual=False, penalty=l2, tol=0.040305862784383875
[CV 3/3; 43/50] END C=0.1643022392036837, class_weight=None, dual=False, penalty=l2, tol=0.040305862784383875;, score=0.962 total time=   0.8s
[CV 1/3; 44/50] START C=0.45233617734588716, class_weight=balanced, dual=True, penalty=l2, tol=0.0053072049402842075
[CV 1/3; 44/50] END C=0.45233617734588716, class_weight=balanced, dual=True, penalty=l2, tol=0.0053072049402842075;, score=0.924 total time=   1.5s
[CV 2/3; 44/50] START C=0.45233617734588716, class_weight=balanced, dual=True, penalty=l2, tol=0.0053072049402842075
[CV 2/3; 44/50] END C=0.45233617734588716, class_weight=balanced, dual=True, penalty=l2, tol=0.0053072049402842075;, score=0.983 total time=   3.2s
[CV 3/3; 44/50] START C=0.45233617734588716, class_weight=balanced, dual=True, penalty=l2, tol=0.0053072049402842075
[CV 3/3; 44/50] END C=0.45233617734588716, class_weight=balanced, dual=True, penalty=l2, tol=0.0053072049402842075;, score=0.960 total time=   2.4s
[CV 1/3; 45/50] START C=0.004250718794258055, class_weight=balanced, dual=True, penalty=l2, tol=0.019394459386265224
[CV 1/3; 45/50] END C=0.004250718794258055, class_weight=balanced, dual=True, penalty=l2, tol=0.019394459386265224;, score=0.926 total time=   1.1s
[CV 2/3; 45/50] START C=0.004250718794258055, class_weight=balanced, dual=True, penalty=l2, tol=0.019394459386265224
[CV 2/3; 45/50] END C=0.004250718794258055, class_weight=balanced, dual=True, penalty=l2, tol=0.019394459386265224;, score=0.983 total time=   1.9s
[CV 3/3; 45/50] START C=0.004250718794258055, class_weight=balanced, dual=True, penalty=l2, tol=0.019394459386265224
[CV 3/3; 45/50] END C=0.004250718794258055, class_weight=balanced, dual=True, penalty=l2, tol=0.019394459386265224;, score=0.965 total time=   1.6s
[CV 1/3; 46/50] START C=0.28963689967394907, class_weight=None, dual=False, penalty=l2, tol=0.0012763724782088731
[CV 1/3; 46/50] END C=0.28963689967394907, class_weight=None, dual=False, penalty=l2, tol=0.0012763724782088731;, score=0.928 total time=   1.4s
[CV 2/3; 46/50] START C=0.28963689967394907, class_weight=None, dual=False, penalty=l2, tol=0.0012763724782088731
[CV 2/3; 46/50] END C=0.28963689967394907, class_weight=None, dual=False, penalty=l2, tol=0.0012763724782088731;, score=0.981 total time=   2.0s
[CV 3/3; 46/50] START C=0.28963689967394907, class_weight=None, dual=False, penalty=l2, tol=0.0012763724782088731
[CV 3/3; 46/50] END C=0.28963689967394907, class_weight=None, dual=False, penalty=l2, tol=0.0012763724782088731;, score=0.964 total time=   1.7s
[CV 1/3; 47/50] START C=0.00873449559598293, class_weight=balanced, dual=False, penalty=l2, tol=0.041841178301577214
[CV 1/3; 47/50] END C=0.00873449559598293, class_weight=balanced, dual=False, penalty=l2, tol=0.041841178301577214;, score=0.935 total time=   1.0s
[CV 2/3; 47/50] START C=0.00873449559598293, class_weight=balanced, dual=False, penalty=l2, tol=0.041841178301577214
[CV 2/3; 47/50] END C=0.00873449559598293, class_weight=balanced, dual=False, penalty=l2, tol=0.041841178301577214;, score=0.983 total time=   1.8s
[CV 3/3; 47/50] START C=0.00873449559598293, class_weight=balanced, dual=False, penalty=l2, tol=0.041841178301577214
[CV 3/3; 47/50] END C=0.00873449559598293, class_weight=balanced, dual=False, penalty=l2, tol=0.041841178301577214;, score=0.964 total time=   1.2s
[CV 1/3; 48/50] START C=0.005636851483341284, class_weight=None, dual=True, penalty=l2, tol=0.015028650731260109
[CV 1/3; 48/50] END C=0.005636851483341284, class_weight=None, dual=True, penalty=l2, tol=0.015028650731260109;, score=0.931 total time=   1.2s
[CV 2/3; 48/50] START C=0.005636851483341284, class_weight=None, dual=True, penalty=l2, tol=0.015028650731260109
[CV 2/3; 48/50] END C=0.005636851483341284, class_weight=None, dual=True, penalty=l2, tol=0.015028650731260109;, score=0.981 total time=   1.9s
[CV 3/3; 48/50] START C=0.005636851483341284, class_weight=None, dual=True, penalty=l2, tol=0.015028650731260109
[CV 3/3; 48/50] END C=0.005636851483341284, class_weight=None, dual=True, penalty=l2, tol=0.015028650731260109;, score=0.964 total time=   1.6s
[CV 1/3; 49/50] START C=0.27680920596290365, class_weight=balanced, dual=False, penalty=l2, tol=0.08659978164359236
[CV 1/3; 49/50] END C=0.27680920596290365, class_weight=balanced, dual=False, penalty=l2, tol=0.08659978164359236;, score=0.934 total time=   0.8s
[CV 2/3; 49/50] START C=0.27680920596290365, class_weight=balanced, dual=False, penalty=l2, tol=0.08659978164359236
[CV 2/3; 49/50] END C=0.27680920596290365, class_weight=balanced, dual=False, penalty=l2, tol=0.08659978164359236;, score=0.982 total time=   1.2s
[CV 3/3; 49/50] START C=0.27680920596290365, class_weight=balanced, dual=False, penalty=l2, tol=0.08659978164359236
[CV 3/3; 49/50] END C=0.27680920596290365, class_weight=balanced, dual=False, penalty=l2, tol=0.08659978164359236;, score=0.963 total time=   1.0s
[CV 1/3; 50/50] START C=0.2073316179510147, class_weight=balanced, dual=True, penalty=l2, tol=0.0018428378455114334
[CV 1/3; 50/50] END C=0.2073316179510147, class_weight=balanced, dual=True, penalty=l2, tol=0.0018428378455114334;, score=0.924 total time=   1.3s
[CV 2/3; 50/50] START C=0.2073316179510147, class_weight=balanced, dual=True, penalty=l2, tol=0.0018428378455114334
[CV 2/3; 50/50] END C=0.2073316179510147, class_weight=balanced, dual=True, penalty=l2, tol=0.0018428378455114334;, score=0.983 total time=   2.8s
[CV 3/3; 50/50] START C=0.2073316179510147, class_weight=balanced, dual=True, penalty=l2, tol=0.0018428378455114334
[CV 3/3; 50/50] END C=0.2073316179510147, class_weight=balanced, dual=True, penalty=l2, tol=0.0018428378455114334;, score=0.962 total time=   2.3s

--- TUNING FINISHED ---
Beste Parameter: {'C': np.float64(0.003602351932055802), 'class_weight': 'balanced', 'dual': False, 'penalty': 'l2', 'tol': np.float64(0.015616279893398812)}
Bester CV-Score: 0.9610

--- EVALUATION AUF DEN TESTDATEN ---
Test Accuracy: 0.8912

Macro F1: 0.8715446229166459

--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.8912

                     precision    recall  f1-score   support

             B cell       1.00      0.96      0.98       120
     CD14+ monocyte       0.98      0.99      0.99      2575
        CD4+ T cell       0.93      0.99      0.96      3910
   Cytotoxic T cell       0.82      0.62      0.71      1824
     Dendritic cell       1.00      0.60      0.75         5
      Megakaryocyte       1.00      1.00      1.00         7
Natural killer cell       0.56      0.67      0.61       791
        Plasma cell       1.00      0.96      0.98        49

           accuracy                           0.89      9281
          macro avg       0.91      0.85      0.87      9281
       weighted avg       0.89      0.89      0.89      9281

Random dropout accuracy score 0.8881
Total samples: 9281
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.8879
Feature importance dropout (0.5% features dropped) accuracy score 0.8667
Feature importance dropout (1.0% features dropped) accuracy score 0.8577
Feature importance dropout (2.0% features dropped) accuracy score 0.8317
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8597

                     precision    recall  f1-score   support

             B cell       1.00      0.97      0.98      3959
     CD14+ monocyte       0.77      1.00      0.87      3135
        CD4+ T cell       0.95      0.95      0.95     13664
   Cytotoxic T cell       0.67      0.67      0.67      4839
     Dendritic cell       0.99      0.63      0.77       529
      Megakaryocyte       0.97      0.77      0.86        86
Natural killer cell       0.61      0.47      0.53      2751
        Plasma cell       1.00      1.00      1.00        23

           accuracy                           0.86     28986
          macro avg       0.87      0.81      0.83     28986
       weighted avg       0.86      0.86      0.86     28986

Random dropout accuracy score 0.8480
Total samples: 28986
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.8537
Feature importance dropout (0.5% features dropped) accuracy score 0.8313
Feature importance dropout (1.0% features dropped) accuracy score 0.8071
Feature importance dropout (2.0% features dropped) accuracy score 0.7749
=== JOB_STATISTICS ===
=== current date     : Sun Jun 28 23:47:15 CEST 2026
= Job-ID             : 11997760 on woody
= Job-Name           : conditional_autoencoder_linsvc
= Job-Command        : /home/hpc/iwbn/iwbn133h/submit_conditional_autoencoder_linsvc_v1.sh
= Initial workdir    : /home/hpc/iwbn/iwbn133h
= Queue/Partition    : work
= Slurm account      : iwbn with QOS=normal
= Features           : icx
= Requested resources:  for 17:00:00
= Elapsed runtime    : 01:30:26
= Total RAM usage    : 20.8 GiB of requested  GiB (%)   
= Node list          : w2215
= Subm/Elig/Start/End: 2026-06-28T22:16:47 / 2026-06-28T22:16:47 / 2026-06-28T22:16:48 / 2026-06-28T23:47:14
======================
=== Quota infos ======
    Path                 Used     SoftQ    HardQ    Gracetime  Filec    FileQ    FiHaQ    FileGrace    
    /home/woody           982.1M  1000.0G  1500.0G        N/A  29,019    5,000K   7,500K        N/A    
    /home/hpc              86.2G   104.9G   209.7G        N/A     139K     500K   1,000K        N/A    
    /home/vault             0.0K  1048.6G  2097.2G        N/A       1      200K     400K        N/A    
