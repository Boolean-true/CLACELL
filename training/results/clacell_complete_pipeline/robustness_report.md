--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9362 +- 0.003

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0   0.9917 +- 0.0   0.9958 +- 0.0    120.0 +- 0.0
          CD14+ monocyte 0.9963 +- 0.0013 0.9997 +- 0.0002 0.998 +- 0.0007   2575.0 +- 0.0
             CD4+ T cell 0.9088 +- 0.0054 0.995 +- 0.0003   0.95 +- 0.003   3910.0 +- 0.0
        Cytotoxic T cell 0.9287 +- 0.0048 0.7452 +- 0.0163 0.8268 +- 0.0102   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0  0.56 +- 0.0843 0.7143 +- 0.0753      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.8865 +- 0.009  0.8679 +- 0.01 0.877 +- 0.0028    791.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     49.0 +- 0.0

                accuracy                                 0.9362 +- 0.003   9281.0 +- 0.0
               macro avg 0.965 +- 0.0013 0.8949 +- 0.0104 0.9202 +- 0.0091   9281.0 +- 0.0
            weighted avg 0.9369 +- 0.0028 0.9362 +- 0.003 0.9336 +- 0.0033   9281.0 +- 0.0

Random dropout accuracy score 0.9293 +- 0.0053
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9363 +- 0.0028
Feature importance dropout (0.5% features dropped) accuracy score 0.8919 +- 0.0045
Feature importance dropout (1.0% features dropped) accuracy score 0.8625 +- 0.0064
Feature importance dropout (2.0% features dropped) accuracy score 0.8253 +- 0.0081
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8705 +- 0.0017

                               precision          recall        f1-score         support

                  B cell    0.999 +- 0.0 0.9978 +- 0.0014 0.9984 +- 0.0007   3959.0 +- 0.0
          CD14+ monocyte 0.8912 +- 0.0143   0.9994 +- 0.0 0.9421 +- 0.0081   3135.0 +- 0.0
             CD4+ T cell 0.9611 +- 0.0024 0.9765 +- 0.0018 0.9687 +- 0.0013  13664.0 +- 0.0
        Cytotoxic T cell 0.6031 +- 0.002 0.8809 +- 0.0086 0.716 +- 0.0029   4839.0 +- 0.0
          Dendritic cell 0.9877 +- 0.0003 0.6059 +- 0.0137 0.7509 +- 0.0105    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.5802 +- 0.0037 0.7344 +- 0.003     86.0 +- 0.0
     Natural killer cell 0.9039 +- 0.019 0.0546 +- 0.0065 0.1028 +- 0.0116   2751.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     23.0 +- 0.0

                accuracy                                 0.8705 +- 0.0017  28986.0 +- 0.0
               macro avg 0.9182 +- 0.0024 0.7619 +- 0.0026 0.7767 +- 0.0024  28986.0 +- 0.0
            weighted avg 0.8941 +- 0.0023 0.8705 +- 0.0017 0.8409 +- 0.0019  28986.0 +- 0.0

Random dropout accuracy score 0.867 +- 0.0023
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8699 +- 0.0021
Feature importance dropout (0.5% features dropped) accuracy score 0.8555 +- 0.0031
Feature importance dropout (1.0% features dropped) accuracy score 0.8451 +- 0.0037
Feature importance dropout (2.0% features dropped) accuracy score 0.7881 +- 0.0158
