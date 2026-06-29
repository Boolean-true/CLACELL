### Starting TaskPrologue of job 11997670 on w2517 at Sun Jun 28 19:58:58 CEST 2026
#   SLURM_JOB_NODELIST=w2517
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
Epoch [1/150], Loss: 0.9429
Epoch [10/150], Loss: 0.9062
Epoch [20/150], Loss: 0.8993
Epoch [30/150], Loss: 0.8967
Epoch [40/150], Loss: 0.8928
Epoch [50/150], Loss: 0.8907
Early Stopping after [51/150] Epochs!

Extract robust features...
Starte automatische Hyperparametersuche auf dem Latent Space...

--- EVALUATION AUF DEN TESTDATEN ---
Test Accuracy: 0.9000

Macro F1: 0.8589205665347999

--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9000

                     precision    recall  f1-score   support

             B cell       0.99      0.97      0.98       120
     CD14+ monocyte       0.99      1.00      0.99      2575
        CD4+ T cell       0.92      0.99      0.96      3910
   Cytotoxic T cell       0.88      0.60      0.72      1824
     Dendritic cell       1.00      0.40      0.57         5
      Megakaryocyte       1.00      1.00      1.00         7
Natural killer cell       0.59      0.80      0.68       791
        Plasma cell       1.00      0.94      0.97        49

           accuracy                           0.90      9281
          macro avg       0.92      0.84      0.86      9281
       weighted avg       0.91      0.90      0.90      9281

Random dropout accuracy score 0.8989
Total samples: 9281
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.8979
Feature importance dropout (0.5% features dropped) accuracy score 0.8799
Feature importance dropout (1.0% features dropped) accuracy score 0.8544
Feature importance dropout (2.0% features dropped) accuracy score 0.8269
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8674

                     precision    recall  f1-score   support

             B cell       1.00      0.96      0.98      3959
     CD14+ monocyte       0.76      1.00      0.86      3135
        CD4+ T cell       0.94      0.97      0.95     13664
   Cytotoxic T cell       0.69      0.69      0.69      4839
     Dendritic cell       1.00      0.45      0.62       529
      Megakaryocyte       0.98      0.71      0.82        86
Natural killer cell       0.72      0.47      0.57      2751
        Plasma cell       1.00      0.96      0.98        23

           accuracy                           0.87     28986
          macro avg       0.89      0.78      0.81     28986
       weighted avg       0.87      0.87      0.86     28986

Random dropout accuracy score 0.8489
Total samples: 28986
Number of inconsistent predictions: 0
Feature importance dropout (0.1% features dropped) accuracy score 0.8641
Feature importance dropout (0.5% features dropped) accuracy score 0.8369
Feature importance dropout (1.0% features dropped) accuracy score 0.7950
Feature importance dropout (2.0% features dropped) accuracy score 0.7294
=== JOB_STATISTICS ===
=== current date     : Sun Jun 28 21:01:06 CEST 2026
= Job-ID             : 11997670 on woody
= Job-Name           : conditional_autoencoder_lr
= Job-Command        : /home/hpc/iwbn/iwbn133h/submit_conditional_autoencoder_lr_v1.sh
= Initial workdir    : /home/hpc/iwbn/iwbn133h
= Queue/Partition    : work
= Slurm account      : iwbn with QOS=normal
= Features           : icx
= Requested resources:  for 17:00:00
= Elapsed runtime    : 01:02:10
= Total RAM usage    : 20.7 GiB of requested  GiB (%)   
= Node list          : w2517
= Subm/Elig/Start/End: 2026-06-28T19:58:55 / 2026-06-28T19:58:55 / 2026-06-28T19:58:56 / 2026-06-28T21:01:06
======================
=== Quota infos ======
    Path                 Used     SoftQ    HardQ    Gracetime  Filec    FileQ    FiHaQ    FileGrace    
    /home/woody           982.1M  1000.0G  1500.0G        N/A  29,019    5,000K   7,500K        N/A    
    /home/hpc              86.2G   104.9G   209.7G        N/A     139K     500K   1,000K        N/A    
    /home/vault             0.0K  1048.6G  2097.2G        N/A       1      200K     400K        N/A    
