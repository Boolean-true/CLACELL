--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9339 +- 0.0051

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0   0.9917 +- 0.0   0.9958 +- 0.0    120.0 +- 0.0
          CD14+ monocyte 0.9965 +- 0.0021 0.9996 +- 0.0002 0.9981 +- 0.0011   2575.0 +- 0.0
             CD4+ T cell 0.9069 +- 0.005 0.9949 +- 0.0006 0.9489 +- 0.0029   3910.0 +- 0.0
        Cytotoxic T cell 0.9243 +- 0.0076 0.7372 +- 0.0288 0.8199 +- 0.0179   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0  0.54 +- 0.0966 0.6964 +- 0.0863      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.8793 +- 0.0288 0.8613 +- 0.0177 0.8697 +- 0.0107    791.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9939 +- 0.0099 0.9969 +- 0.005     49.0 +- 0.0

                accuracy                                 0.9339 +- 0.0051   9281.0 +- 0.0
               macro avg 0.9634 +- 0.004 0.8898 +- 0.0103 0.9157 +- 0.0097   9281.0 +- 0.0
            weighted avg 0.9347 +- 0.0045 0.9339 +- 0.0051 0.9312 +- 0.0058   9281.0 +- 0.0

10% Random Dropout accuracy: 0.9301 +- 0.0062
50% Random Dropout accuracy: 0.8955 +- 0.0188
90% Random Dropout accuracy: 0.6843 +- 0.0377
92.5% Random Dropout accuracy: 0.6327 +- 0.0493
95% Random Dropout accuracy: 0.5482 +- 0.0568
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9332 +- 0.006
Feature importance dropout (0.5% features dropped) accuracy score 0.8868 +- 0.0043
Feature importance dropout (1.0% features dropped) accuracy score 0.8563 +- 0.0065
Feature importance dropout (2.0% features dropped) accuracy score 0.8196 +- 0.0097
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.871 +- 0.001

                               precision          recall        f1-score         support

                  B cell 0.9989 +- 0.0002 0.9984 +- 0.0013 0.9987 +- 0.0007   3959.0 +- 0.0
          CD14+ monocyte 0.8992 +- 0.008 0.9992 +- 0.0004 0.9465 +- 0.0044   3135.0 +- 0.0
             CD4+ T cell 0.9604 +- 0.0023 0.9772 +- 0.0036 0.9687 +- 0.0012  13664.0 +- 0.0
        Cytotoxic T cell 0.6023 +- 0.0025 0.8803 +- 0.0073 0.7153 +- 0.0029   4839.0 +- 0.0
          Dendritic cell 0.9871 +- 0.0018 0.6183 +- 0.0413 0.7596 +- 0.0292    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.5791 +- 0.0049 0.7334 +- 0.0039     86.0 +- 0.0
     Natural killer cell 0.9035 +- 0.0131 0.0542 +- 0.0132 0.102 +- 0.0233   2751.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     23.0 +- 0.0

                accuracy                                  0.871 +- 0.001  28986.0 +- 0.0
               macro avg 0.9189 +- 0.0019 0.7634 +- 0.0057 0.778 +- 0.0055  28986.0 +- 0.0
            weighted avg 0.8945 +- 0.002  0.871 +- 0.001 0.8414 +- 0.0024  28986.0 +- 0.0

10% Random Dropout accuracy: 0.8678 +- 0.0011
50% Random Dropout accuracy: 0.8131 +- 0.0208
90% Random Dropout accuracy: 0.4639 +- 0.0682
92.5% Random Dropout accuracy: 0.399 +- 0.0742
95% Random Dropout accuracy: 0.3158 +- 0.0557
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8701 +- 0.0009
Feature importance dropout (0.5% features dropped) accuracy score 0.8543 +- 0.0022
Feature importance dropout (1.0% features dropped) accuracy score 0.8426 +- 0.0038
Feature importance dropout (2.0% features dropped) accuracy score 0.778 +- 0.0184
