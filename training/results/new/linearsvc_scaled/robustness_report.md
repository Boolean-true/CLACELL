--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.7379 +- 0.0014

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9825 +- 0.0023 0.9987 +- 0.0002 0.9905 +- 0.0011   3458.0 +- 0.0
          CD16+ Monocyte 0.9707 +- 0.0064 0.918 +- 0.0182 0.9435 +- 0.0073    183.0 +- 0.0
    CD1C+ dendritic cell      1.0 +- 0.0 0.6345 +- 0.0321 0.7759 +- 0.0243    116.0 +- 0.0
       CD4 Memory T cell   0.0016 +- 0.0   0.0242 +- 0.0    0.003 +- 0.0    248.0 +- 0.0
        CD4 Naive T cell 0.9004 +- 0.0029 0.7863 +- 0.0069 0.8394 +- 0.0028   3251.0 +- 0.0
       CD8 Memory T cell 0.7616 +- 0.0058 0.7792 +- 0.0042 0.7703 +- 0.0021   4026.0 +- 0.0
        CD8 Naive T cell 0.9101 +- 0.001 0.8654 +- 0.0041 0.8871 +- 0.0018   1908.0 +- 0.0
      Gamma-delta T cell 0.9419 +- 0.0082 0.5311 +- 0.0095 0.6792 +- 0.0083    119.0 +- 0.0
                    MAIT 0.6991 +- 0.0067 0.9713 +- 0.0014 0.813 +- 0.0041    519.0 +- 0.0
           Memory B cell 0.9228 +- 0.0023 0.9039 +- 0.0031 0.9133 +- 0.0012    946.0 +- 0.0
                 NK cell 0.9745 +- 0.0006 0.3559 +- 0.0012 0.5214 +- 0.0012   5399.0 +- 0.0
            Naive B cell 0.9582 +- 0.0012 0.9645 +- 0.0014 0.9614 +- 0.0006   2182.0 +- 0.0
             Plasma cell 0.9654 +- 0.0097 0.8778 +- 0.0096 0.9195 +- 0.008     54.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.6906 +- 0.0698 0.8152 +- 0.049     32.0 +- 0.0
       T regulatory cell 0.0237 +- 0.003  0.34 +- 0.0516 0.0444 +- 0.0057     10.0 +- 0.0

                accuracy                                 0.7379 +- 0.0014  22451.0 +- 0.0
               macro avg 0.8008 +- 0.0013 0.7094 +- 0.0101 0.7251 +- 0.0054  22451.0 +- 0.0
            weighted avg   0.9 +- 0.0007 0.7379 +- 0.0014 0.7825 +- 0.0013  22451.0 +- 0.0

10% Random Dropout accuracy: 0.7298 +- 0.0077
50% Random Dropout accuracy: 0.6525 +- 0.0178
90% Random Dropout accuracy: 0.2828 +- 0.0346
92.5% Random Dropout accuracy: 0.2369 +- 0.0401
95% Random Dropout accuracy: 0.1885 +- 0.0206
Total samples: 22451.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.7379 +- 0.0014
Feature importance dropout (0.5% features dropped) accuracy score 0.7379 +- 0.001
Feature importance dropout (1.0% features dropped) accuracy score 0.7433 +- 0.0019
Feature importance dropout (2.0% features dropped) accuracy score 0.7272 +- 0.0015
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.7159 +- 0.0013

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.8205 +- 0.0274 0.9949 +- 0.0002 0.8991 +- 0.0163  12317.0 +- 0.0
          CD16+ Monocyte 0.9749 +- 0.0044 0.9148 +- 0.0053 0.9439 +- 0.0016   1903.0 +- 0.0
    CD1C+ dendritic cell 0.9144 +- 0.0041 0.9041 +- 0.0032 0.9092 +- 0.0009   1079.0 +- 0.0
       CD4 Memory T cell 0.7519 +- 0.0171 0.0062 +- 0.0005 0.0122 +- 0.0011  14241.0 +- 0.0
        CD4 Naive T cell 0.7967 +- 0.0221 0.9244 +- 0.0104 0.8555 +- 0.0086  17151.0 +- 0.0
       CD8 Memory T cell 0.3383 +- 0.0076 0.804 +- 0.0158  0.476 +- 0.005   6650.0 +- 0.0
        CD8 Naive T cell 0.9168 +- 0.0047 0.9384 +- 0.0048 0.9275 +- 0.0026   6516.0 +- 0.0
      Gamma-delta T cell 0.0547 +- 0.0048 0.0187 +- 0.0024 0.0279 +- 0.0033   2271.0 +- 0.0
                    MAIT 0.6457 +- 0.0139 0.9835 +- 0.0021 0.7795 +- 0.0098   2889.0 +- 0.0
           Memory B cell 0.8085 +- 0.0194 0.773 +- 0.0022 0.7902 +- 0.0089   1395.0 +- 0.0
                 NK cell 0.785 +- 0.0085 0.8791 +- 0.0005 0.8294 +- 0.0046   5959.0 +- 0.0
            Naive B cell 0.8897 +- 0.003   0.9843 +- 0.0 0.9346 +- 0.0017   3385.0 +- 0.0
             Plasma cell 0.9725 +- 0.0128   0.9882 +- 0.0 0.9803 +- 0.0065    930.0 +- 0.0
Plasmacytoid dendritic cell 0.9858 +- 0.0096 0.9952 +- 0.0007 0.9905 +- 0.0048    584.0 +- 0.0
       T regulatory cell  0.7126 +- 0.03 0.0856 +- 0.0083 0.1526 +- 0.0125   1731.0 +- 0.0

                accuracy                                 0.7159 +- 0.0013  79001.0 +- 0.0
               macro avg 0.7579 +- 0.0056 0.7463 +- 0.0012 0.7006 +- 0.0012  79001.0 +- 0.0
            weighted avg 0.7476 +- 0.004 0.7159 +- 0.0013 0.6479 +- 0.001  79001.0 +- 0.0

10% Random Dropout accuracy: 0.7078 +- 0.0032
50% Random Dropout accuracy: 0.6348 +- 0.0155
90% Random Dropout accuracy: 0.3117 +- 0.0418
92.5% Random Dropout accuracy: 0.2819 +- 0.0328
95% Random Dropout accuracy: 0.2443 +- 0.0157
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.7159 +- 0.0013
Feature importance dropout (0.5% features dropped) accuracy score 0.7175 +- 0.0006
Feature importance dropout (1.0% features dropped) accuracy score 0.7171 +- 0.0014
Feature importance dropout (2.0% features dropped) accuracy score 0.7108 +- 0.0017
