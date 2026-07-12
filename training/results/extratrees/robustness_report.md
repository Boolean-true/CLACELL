--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.8932 +- 0.005

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0 0.9892 +- 0.004 0.9946 +- 0.002    120.0 +- 0.0
          CD14+ monocyte 0.9986 +- 0.0002 0.9998 +- 0.0002 0.9992 +- 0.0001   2575.0 +- 0.0
             CD4+ T cell 0.9204 +- 0.0048 0.9969 +- 0.0003 0.9571 +- 0.0025   3910.0 +- 0.0
        Cytotoxic T cell 0.9981 +- 0.0013 0.4741 +- 0.0252 0.6424 +- 0.0233   1824.0 +- 0.0
          Dendritic cell   0.8 +- 0.4216  0.16 +- 0.0843 0.2667 +- 0.1405      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.5485 +- 0.0178 0.9941 +- 0.0017 0.7068 +- 0.0148    791.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.8204 +- 0.0232 0.9012 +- 0.0141     49.0 +- 0.0

                accuracy                                 0.8932 +- 0.005   9281.0 +- 0.0
               macro avg 0.9082 +- 0.0539 0.8043 +- 0.0133 0.8085 +- 0.0208   9281.0 +- 0.0
            weighted avg 0.9271 +- 0.002 0.8932 +- 0.005 0.8855 +- 0.006   9281.0 +- 0.0

Random dropout accuracy score 0.8691 +- 0.008
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.854 +- 0.0051
Feature importance dropout (0.5% features dropped) accuracy score 0.8195 +- 0.0023
Feature importance dropout (1.0% features dropped) accuracy score 0.7939 +- 0.0018
Feature importance dropout (2.0% features dropped) accuracy score 0.7279 +- 0.0082
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8941 +- 0.0025

                               precision          recall        f1-score         support

                  B cell 0.9989 +- 0.0001 0.9976 +- 0.0009 0.9983 +- 0.0005   3959.0 +- 0.0
          CD14+ monocyte 0.8495 +- 0.001      1.0 +- 0.0 0.9187 +- 0.0006   3135.0 +- 0.0
             CD4+ T cell 0.8914 +- 0.0041 0.9985 +- 0.0001 0.9419 +- 0.0023  13664.0 +- 0.0
        Cytotoxic T cell 0.8727 +- 0.0162 0.5732 +- 0.0172 0.6917 +- 0.0112   4839.0 +- 0.0
          Dendritic cell 0.9852 +- 0.0313 0.021 +- 0.0066 0.041 +- 0.0126    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0   0.5698 +- 0.0   0.7259 +- 0.0     86.0 +- 0.0
     Natural killer cell 0.8408 +- 0.0104 0.8486 +- 0.024 0.8444 +- 0.0093   2751.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.7826 +- 0.0794 0.8761 +- 0.0487     23.0 +- 0.0

                accuracy                                 0.8941 +- 0.0025  28986.0 +- 0.0
               macro avg 0.9298 +- 0.0044 0.7239 +- 0.0122 0.7548 +- 0.0082  28986.0 +- 0.0
            weighted avg 0.8958 +- 0.003 0.8941 +- 0.0025 0.8789 +- 0.0031  28986.0 +- 0.0

Random dropout accuracy score 0.8814 +- 0.0032
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8845 +- 0.0019
Feature importance dropout (0.5% features dropped) accuracy score 0.8497 +- 0.0029
Feature importance dropout (1.0% features dropped) accuracy score 0.734 +- 0.0163
Feature importance dropout (2.0% features dropped) accuracy score 0.584 +- 0.0018
