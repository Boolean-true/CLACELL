--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.897 +- 0.0156

                               precision          recall        f1-score         support

                  B cell 0.9868 +- 0.0116 0.985 +- 0.0086 0.9858 +- 0.0076    120.0 +- 0.0
          CD14+ monocyte 0.9972 +- 0.0015 0.9986 +- 0.0006 0.9979 +- 0.0006   2575.0 +- 0.0
             CD4+ T cell 0.8662 +- 0.0278 0.9949 +- 0.0014 0.9259 +- 0.0157   3910.0 +- 0.0
        Cytotoxic T cell 0.909 +- 0.0348 0.5606 +- 0.088 0.6893 +- 0.0645   1824.0 +- 0.0
          Dendritic cell 0.9333 +- 0.1405      0.4 +- 0.0 0.5571 +- 0.0301      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.9571 +- 0.0964 0.9756 +- 0.0555      7.0 +- 0.0
     Natural killer cell 0.7499 +- 0.0696 0.8464 +- 0.0798 0.7891 +- 0.0244    791.0 +- 0.0
             Plasma cell 0.9957 +- 0.009 0.9061 +- 0.0587 0.9478 +- 0.0322     49.0 +- 0.0

                accuracy                                 0.897 +- 0.0156   9281.0 +- 0.0
               macro avg 0.9298 +- 0.0184 0.8311 +- 0.0153 0.8586 +- 0.0133   9281.0 +- 0.0
            weighted avg 0.9034 +- 0.0138 0.897 +- 0.0156 0.8884 +- 0.0192   9281.0 +- 0.0

Random dropout accuracy score 0.8835 +- 0.013
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8944 +- 0.0154
Feature importance dropout (0.5% features dropped) accuracy score 0.8748 +- 0.0171
Feature importance dropout (1.0% features dropped) accuracy score 0.8477 +- 0.0181
Feature importance dropout (2.0% features dropped) accuracy score 0.807 +- 0.0168
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.857 +- 0.0106

                               precision          recall        f1-score         support

                  B cell 0.9992 +- 0.0003  0.98 +- 0.0204 0.9894 +- 0.0106   3959.0 +- 0.0
          CD14+ monocyte  0.89 +- 0.0192 0.9987 +- 0.0011 0.9411 +- 0.0106   3135.0 +- 0.0
             CD4+ T cell 0.9023 +- 0.0226 0.9917 +- 0.0061 0.9447 +- 0.0115  13664.0 +- 0.0
        Cytotoxic T cell 0.6087 +- 0.0163 0.6989 +- 0.0727 0.649 +- 0.0336   4839.0 +- 0.0
          Dendritic cell 0.9859 +- 0.0044 0.4991 +- 0.1176 0.6557 +- 0.1002    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.6372 +- 0.0284 0.7781 +- 0.0214     86.0 +- 0.0
     Natural killer cell 0.8699 +- 0.0476 0.2025 +- 0.0846 0.3193 +- 0.112   2751.0 +- 0.0
             Plasma cell 0.8351 +- 0.1523 0.887 +- 0.0825 0.8561 +- 0.1116     23.0 +- 0.0

                accuracy                                 0.857 +- 0.0106  28986.0 +- 0.0
               macro avg 0.8864 +- 0.0192 0.7369 +- 0.0267 0.7667 +- 0.0273  28986.0 +- 0.0
            weighted avg 0.8639 +- 0.0132 0.857 +- 0.0106 0.8359 +- 0.0128  28986.0 +- 0.0

Random dropout accuracy score 0.8475 +- 0.0145
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8561 +- 0.011
Feature importance dropout (0.5% features dropped) accuracy score 0.8369 +- 0.0165
Feature importance dropout (1.0% features dropped) accuracy score 0.8115 +- 0.0266
Feature importance dropout (2.0% features dropped) accuracy score 0.7234 +- 0.0466
