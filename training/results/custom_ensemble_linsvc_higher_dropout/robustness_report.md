--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9331 +- 0.006

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0   0.9917 +- 0.0   0.9958 +- 0.0    120.0 +- 0.0
          CD14+ monocyte 0.9948 +- 0.002   0.9996 +- 0.0 0.9972 +- 0.001   2575.0 +- 0.0
             CD4+ T cell 0.9064 +- 0.005 0.995 +- 0.0002 0.9486 +- 0.0028   3910.0 +- 0.0
        Cytotoxic T cell 0.9273 +- 0.0049 0.7294 +- 0.0359 0.816 +- 0.0222   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0      0.6 +- 0.0     0.75 +- 0.0      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.8746 +- 0.0376 0.8692 +- 0.0142 0.8712 +- 0.0138    791.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.998 +- 0.0065 0.999 +- 0.0033     49.0 +- 0.0

                accuracy                                 0.9331 +- 0.006   9281.0 +- 0.0
               macro avg 0.9629 +- 0.0049 0.8979 +- 0.0037 0.9222 +- 0.0053   9281.0 +- 0.0
            weighted avg 0.9341 +- 0.0047 0.9331 +- 0.006 0.9302 +- 0.0069   9281.0 +- 0.0

10% Random Dropout accuracy: 0.9269 +- 0.0064
50% Random Dropout accuracy: 0.8919 +- 0.0086
90% Random Dropout accuracy: 0.6875 +- 0.0422
92.5% Random Dropout accuracy: 0.6003 +- 0.0394
95% Random Dropout accuracy: 0.5035 +- 0.0501
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9335 +- 0.0062
Feature importance dropout (0.5% features dropped) accuracy score 0.8829 +- 0.0038
Feature importance dropout (1.0% features dropped) accuracy score 0.8608 +- 0.0018
Feature importance dropout (2.0% features dropped) accuracy score 0.8237 +- 0.0045
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8689 +- 0.0018

                               precision          recall        f1-score         support

                  B cell 0.9989 +- 0.0002 0.9966 +- 0.0015 0.9978 +- 0.0008   3959.0 +- 0.0
          CD14+ monocyte 0.8761 +- 0.0152 0.9993 +- 0.0001 0.9336 +- 0.0087   3135.0 +- 0.0
             CD4+ T cell 0.9576 +- 0.0017 0.9772 +- 0.0032 0.9673 +- 0.0016  13664.0 +- 0.0
        Cytotoxic T cell 0.6052 +- 0.0018 0.8657 +- 0.0078 0.7123 +- 0.0023   4839.0 +- 0.0
          Dendritic cell 0.9877 +- 0.0006 0.6064 +- 0.0341 0.751 +- 0.0253    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.5779 +- 0.0056 0.7325 +- 0.0045     86.0 +- 0.0
     Natural killer cell 0.881 +- 0.0064 0.0629 +- 0.0162 0.117 +- 0.0275   2751.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     23.0 +- 0.0

                accuracy                                 0.8689 +- 0.0018  28986.0 +- 0.0
               macro avg 0.9133 +- 0.0025 0.7608 +- 0.0055 0.7764 +- 0.0062  28986.0 +- 0.0
            weighted avg 0.889 +- 0.0025 0.8689 +- 0.0018 0.8399 +- 0.003  28986.0 +- 0.0

10% Random Dropout accuracy: 0.8637 +- 0.0026
50% Random Dropout accuracy: 0.7938 +- 0.0186
90% Random Dropout accuracy: 0.4075 +- 0.0495
92.5% Random Dropout accuracy: 0.3685 +- 0.0401
95% Random Dropout accuracy: 0.2907 +- 0.0468
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8684 +- 0.0018
Feature importance dropout (0.5% features dropped) accuracy score 0.8485 +- 0.0025
Feature importance dropout (1.0% features dropped) accuracy score 0.8382 +- 0.0021
Feature importance dropout (2.0% features dropped) accuracy score 0.7683 +- 0.0086
