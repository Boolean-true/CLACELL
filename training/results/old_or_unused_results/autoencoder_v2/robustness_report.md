--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.8863 +- 0.0176

                               precision          recall        f1-score         support

                  B cell 0.9818 +- 0.0085 0.9842 +- 0.0121 0.9829 +- 0.0083    120.0 +- 0.0
          CD14+ monocyte 0.9979 +- 0.0014 0.998 +- 0.0007 0.998 +- 0.0008   2575.0 +- 0.0
             CD4+ T cell 0.8628 +- 0.0239 0.9953 +- 0.0009 0.9242 +- 0.0134   3910.0 +- 0.0
        Cytotoxic T cell 0.9386 +- 0.021 0.4814 +- 0.1027 0.6297 +- 0.0869   1824.0 +- 0.0
          Dendritic cell 0.9667 +- 0.1054  0.42 +- 0.0632 0.5821 +- 0.0631      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.6757 +- 0.0891 0.9042 +- 0.0433 0.7683 +- 0.0468    791.0 +- 0.0
             Plasma cell 0.9934 +- 0.0106 0.8898 +- 0.0595 0.9377 +- 0.0335     49.0 +- 0.0

                accuracy                                 0.8863 +- 0.0176   9281.0 +- 0.0
               macro avg 0.9271 +- 0.014 0.8341 +- 0.0195 0.8529 +- 0.0219   9281.0 +- 0.0
            weighted avg 0.9017 +- 0.0105 0.8863 +- 0.0176 0.8742 +- 0.0231   9281.0 +- 0.0

Random dropout accuracy score 0.869 +- 0.0181
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8822 +- 0.0183
Feature importance dropout (0.5% features dropped) accuracy score 0.8596 +- 0.019
Feature importance dropout (1.0% features dropped) accuracy score 0.8307 +- 0.0146
Feature importance dropout (2.0% features dropped) accuracy score 0.791 +- 0.0104
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8508 +- 0.0117

                               precision          recall        f1-score         support

                  B cell 0.9992 +- 0.0003 0.9723 +- 0.0188 0.9855 +- 0.0097   3959.0 +- 0.0
          CD14+ monocyte 0.879 +- 0.0319 0.9983 +- 0.0012 0.9346 +- 0.0181   3135.0 +- 0.0
             CD4+ T cell  0.88 +- 0.0168 0.9931 +- 0.0074 0.933 +- 0.0091  13664.0 +- 0.0
        Cytotoxic T cell 0.6151 +- 0.0241 0.6207 +- 0.0584 0.6165 +- 0.0342   4839.0 +- 0.0
          Dendritic cell 0.9871 +- 0.0033 0.4996 +- 0.1255 0.6548 +- 0.1146    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.6349 +- 0.0281 0.7764 +- 0.0207     86.0 +- 0.0
     Natural killer cell 0.8448 +- 0.0513 0.2807 +- 0.0917 0.4138 +- 0.1148   2751.0 +- 0.0
             Plasma cell 0.8638 +- 0.1366 0.7957 +- 0.1834 0.813 +- 0.1287     23.0 +- 0.0

                accuracy                                 0.8508 +- 0.0117  28986.0 +- 0.0
               macro avg 0.8836 +- 0.0241 0.7244 +- 0.0365 0.7659 +- 0.0331  28986.0 +- 0.0
            weighted avg 0.8509 +- 0.0134 0.8508 +- 0.0117 0.8326 +- 0.0157  28986.0 +- 0.0

Random dropout accuracy score 0.8355 +- 0.0128
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.849 +- 0.0118
Feature importance dropout (0.5% features dropped) accuracy score 0.8237 +- 0.015
Feature importance dropout (1.0% features dropped) accuracy score 0.7935 +- 0.0169
Feature importance dropout (2.0% features dropped) accuracy score 0.7052 +- 0.025
