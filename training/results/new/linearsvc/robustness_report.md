--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.7808 +- 0.0002

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9943 +- 0.0003 0.9963 +- 0.0001 0.9953 +- 0.0002   3458.0 +- 0.0
          CD16+ Monocyte 0.9473 +- 0.0022   0.9617 +- 0.0 0.9544 +- 0.0011    183.0 +- 0.0
    CD1C+ dendritic cell    0.955 +- 0.0   0.9138 +- 0.0   0.9339 +- 0.0    116.0 +- 0.0
       CD4 Memory T cell 0.0047 +- 0.0002 0.0419 +- 0.0021 0.0084 +- 0.0004    248.0 +- 0.0
        CD4 Naive T cell 0.7277 +- 0.0003 0.9022 +- 0.0004 0.8056 +- 0.0002   3251.0 +- 0.0
       CD8 Memory T cell 0.8678 +- 0.0004 0.8007 +- 0.0001 0.8329 +- 0.0002   4026.0 +- 0.0
        CD8 Naive T cell 0.8397 +- 0.0003 0.9568 +- 0.0004 0.8944 +- 0.0001   1908.0 +- 0.0
      Gamma-delta T cell 0.7232 +- 0.0029   0.7311 +- 0.0 0.7271 +- 0.0015    119.0 +- 0.0
                    MAIT 0.7737 +- 0.0011   0.9711 +- 0.0 0.8612 +- 0.0007    519.0 +- 0.0
           Memory B cell 0.8934 +- 0.0004   0.9545 +- 0.0 0.9229 +- 0.0002    946.0 +- 0.0
                 NK cell 0.948 +- 0.0002 0.396 +- 0.0004 0.5587 +- 0.0004   5399.0 +- 0.0
            Naive B cell   0.9794 +- 0.0   0.9565 +- 0.0   0.9678 +- 0.0   2182.0 +- 0.0
             Plasma cell   0.9286 +- 0.0    0.963 +- 0.0   0.9455 +- 0.0     54.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0   0.9688 +- 0.0   0.9841 +- 0.0     32.0 +- 0.0
       T regulatory cell   0.0304 +- 0.0      0.9 +- 0.0 0.0588 +- 0.0001     10.0 +- 0.0

                accuracy                                 0.7808 +- 0.0002  22451.0 +- 0.0
               macro avg 0.7742 +- 0.0002 0.8276 +- 0.0002 0.7634 +- 0.0001  22451.0 +- 0.0
            weighted avg 0.8844 +- 0.0001 0.7808 +- 0.0002 0.8028 +- 0.0001  22451.0 +- 0.0

10% Random Dropout accuracy: 0.7737 +- 0.0027
50% Random Dropout accuracy: 0.6889 +- 0.0116
90% Random Dropout accuracy: 0.4106 +- 0.0253
92.5% Random Dropout accuracy: 0.3695 +- 0.0225
95% Random Dropout accuracy: 0.3117 +- 0.0272
Total samples: 22451.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.7808 +- 0.0002
Feature importance dropout (0.5% features dropped) accuracy score 0.7797 +- 0.0003
Feature importance dropout (1.0% features dropped) accuracy score 0.7775 +- 0.0005
Feature importance dropout (2.0% features dropped) accuracy score 0.7602 +- 0.0004
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.7265 +- 0.0004

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9607 +- 0.0007   0.9964 +- 0.0 0.9782 +- 0.0004  12317.0 +- 0.0
          CD16+ Monocyte 0.9144 +- 0.0017 0.9115 +- 0.0016 0.913 +- 0.0013   1903.0 +- 0.0
    CD1C+ dendritic cell 0.9333 +- 0.0004 0.8781 +- 0.0013 0.9049 +- 0.0006   1079.0 +- 0.0
       CD4 Memory T cell 0.7138 +- 0.0058 0.1401 +- 0.002 0.2341 +- 0.0026  14241.0 +- 0.0
        CD4 Naive T cell 0.8634 +- 0.003 0.8452 +- 0.0047 0.8542 +- 0.0009  17151.0 +- 0.0
       CD8 Memory T cell 0.3319 +- 0.0009  0.749 +- 0.003 0.4599 +- 0.0003   6650.0 +- 0.0
        CD8 Naive T cell 0.8281 +- 0.0014 0.9768 +- 0.0005 0.8963 +- 0.0007   6516.0 +- 0.0
      Gamma-delta T cell 0.0531 +- 0.0005 0.0196 +- 0.0002 0.0286 +- 0.0003   2271.0 +- 0.0
                    MAIT 0.5315 +- 0.0024   0.9924 +- 0.0 0.6923 +- 0.002   2889.0 +- 0.0
           Memory B cell 0.661 +- 0.0034 0.8133 +- 0.0008 0.7293 +- 0.002   1395.0 +- 0.0
                 NK cell 0.794 +- 0.0015 0.882 +- 0.0003 0.8357 +- 0.0008   5959.0 +- 0.0
            Naive B cell 0.9247 +- 0.0008 0.9813 +- 0.0003 0.9522 +- 0.0005   3385.0 +- 0.0
             Plasma cell 0.943 +- 0.0013   0.9882 +- 0.0 0.9651 +- 0.0007    930.0 +- 0.0
Plasmacytoid dendritic cell 0.9911 +- 0.0007   0.9966 +- 0.0 0.9939 +- 0.0004    584.0 +- 0.0
       T regulatory cell 0.3669 +- 0.0049 0.278 +- 0.0011 0.3163 +- 0.0012   1731.0 +- 0.0

                accuracy                                 0.7265 +- 0.0004  79001.0 +- 0.0
               macro avg 0.7207 +- 0.0006 0.7632 +- 0.0002 0.7169 +- 0.0003  79001.0 +- 0.0
            weighted avg 0.7555 +- 0.0005 0.7265 +- 0.0004 0.6956 +- 0.0002  79001.0 +- 0.0

10% Random Dropout accuracy: 0.717 +- 0.0031
50% Random Dropout accuracy: 0.6523 +- 0.009
90% Random Dropout accuracy: 0.4197 +- 0.0169
92.5% Random Dropout accuracy: 0.3902 +- 0.0167
95% Random Dropout accuracy: 0.35 +- 0.0232
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.7265 +- 0.0004
Feature importance dropout (0.5% features dropped) accuracy score 0.7283 +- 0.0003
Feature importance dropout (1.0% features dropped) accuracy score 0.7332 +- 0.0004
Feature importance dropout (2.0% features dropped) accuracy score 0.726 +- 0.0001
