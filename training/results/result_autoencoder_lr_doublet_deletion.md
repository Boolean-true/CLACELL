### Starting TaskPrologue of job 11997669 on w2333 at Sun Jun 28 19:58:51 CEST 2026
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
Start DAE Training...
Epoch [1/150], Loss: 0.9532
Epoch [10/150], Loss: 0.9071
Epoch [20/150], Loss: 0.8926
Epoch [30/150], Loss: 0.8844
Epoch [40/150], Loss: 0.8794
Epoch [50/150], Loss: 0.8760
Epoch [60/150], Loss: 0.8733
Epoch [70/150], Loss: 0.8710
Epoch [80/150], Loss: 0.8692
Epoch [90/150], Loss: 0.8677
Epoch [100/150], Loss: 0.8663

Extract robust features...
Starte automatische Hyperparametersuche auf dem Latent Space...

--- EVALUATION AUF DEN TESTDATEN ---
Test Accuracy: 0.9184

Macro F1: 0.8821535367054697

--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9184

                     precision    recall  f1-score   support

             B cell       0.98      1.00      0.99       120
     CD14+ monocyte       1.00      1.00      1.00      2575
        CD4+ T cell       0.90      0.99      0.94      3910
   Cytotoxic T cell       0.94      0.65      0.77      1824
     Dendritic cell       1.00      0.40      0.57         5
      Megakaryocyte       1.00      1.00      1.00         7
Natural killer cell       0.76      0.91      0.83       791
        Plasma cell       1.00      0.92      0.96        49

           accuracy                           0.92      9281
          macro avg       0.95      0.86      0.88      9281
       weighted avg       0.92      0.92      0.91      9281

Random dropout accuracy score 0.9038
Total samples: 9281
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.9153
Feature importance dropout (0.5% features dropped) accuracy score 0.8957
Feature importance dropout (1.0% features dropped) accuracy score 0.8765
Feature importance dropout (2.0% features dropped) accuracy score 0.8345
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8653

                     precision    recall  f1-score   support

             B cell       1.00      0.99      1.00      3959
     CD14+ monocyte       0.89      1.00      0.94      3135
        CD4+ T cell       0.90      0.99      0.95     13664
   Cytotoxic T cell       0.63      0.69      0.66      4839
     Dendritic cell       0.98      0.59      0.74       529
      Megakaryocyte       1.00      0.62      0.76        86
Natural killer cell       0.91      0.27      0.41      2751
        Plasma cell       0.88      0.91      0.89        23

           accuracy                           0.87     28986
          macro avg       0.90      0.76      0.79     28986
       weighted avg       0.87      0.87      0.85     28986

Random dropout accuracy score 0.8585
Total samples: 28986
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.8647
Feature importance dropout (0.5% features dropped) accuracy score 0.8501
Feature importance dropout (1.0% features dropped) accuracy score 0.8358
Feature importance dropout (2.0% features dropped) accuracy score 0.7553
=== JOB_STATISTICS ===
=== current date     : Sun Jun 28 21:58:32 CEST 2026
= Job-ID             : 11997669 on woody
= Job-Name           : autoencoder_lr
= Job-Command        : /home/hpc/iwbn/iwbn133h/submit_autoencoder_lr_v1.sh
= Initial workdir    : /home/hpc/iwbn/iwbn133h
= Queue/Partition    : work
= Slurm account      : iwbn with QOS=normal
= Features           : icx
= Requested resources:  for 17:00:00
= Elapsed runtime    : 01:59:44
= Total RAM usage    : 18.9 GiB of requested  GiB (%)   
= Node list          : w2333
= Subm/Elig/Start/End: 2026-06-28T19:58:47 / 2026-06-28T19:58:47 / 2026-06-28T19:58:48 / 2026-06-28T21:58:32
======================
=== Quota infos ======
    Path                 Used     SoftQ    HardQ    Gracetime  Filec    FileQ    FiHaQ    FileGrace    
    /home/woody           982.1M  1000.0G  1500.0G        N/A  29,019    5,000K   7,500K        N/A    
    /home/hpc              86.2G   104.9G   209.7G        N/A     139K     500K   1,000K        N/A    
    /home/vault             0.0K  1048.6G  2097.2G        N/A       1      200K     400K        N/A    
