--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9209 +- 0.0101

                               precision          recall        f1-score         support

                  B cell 0.9967 +- 0.0104 0.9892 +- 0.004 0.9929 +- 0.0065    120.0 +- 0.0
          CD14+ monocyte 0.9926 +- 0.0017 0.9997 +- 0.0005 0.9961 +- 0.001   2575.0 +- 0.0
             CD4+ T cell 0.8866 +- 0.0071 0.9959 +- 0.0004 0.9381 +- 0.0041   3910.0 +- 0.0
        Cytotoxic T cell 0.9685 +- 0.0144 0.6304 +- 0.0439 0.7632 +- 0.0372   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0  0.62 +- 0.0632 0.7639 +- 0.0439      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.8081 +- 0.0392 0.9493 +- 0.017 0.8728 +- 0.0302    791.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.998 +- 0.0065 0.999 +- 0.0033     49.0 +- 0.0

                accuracy                                 0.9209 +- 0.0101   9281.0 +- 0.0
               macro avg 0.9566 +- 0.0088 0.8978 +- 0.0026 0.9157 +- 0.0047   9281.0 +- 0.0
            weighted avg 0.9276 +- 0.0091 0.9209 +- 0.0101 0.9152 +- 0.0117   9281.0 +- 0.0

Random dropout accuracy score 0.9117 +- 0.0115
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9194 +- 0.0098
Feature importance dropout (0.5% features dropped) accuracy score 0.8391 +- 0.0037
Feature importance dropout (1.0% features dropped) accuracy score 0.7873 +- 0.0052
Feature importance dropout (2.0% features dropped) accuracy score 0.7302 +- 0.01
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8753 +- 0.001

                               precision          recall        f1-score         support

                  B cell 0.9988 +- 0.0003 0.9995 +- 0.0007 0.9991 +- 0.0005   3959.0 +- 0.0
          CD14+ monocyte 0.9045 +- 0.0025 0.9991 +- 0.0008 0.9495 +- 0.0013   3135.0 +- 0.0
             CD4+ T cell 0.9545 +- 0.0007 0.9822 +- 0.0032 0.9681 +- 0.0014  13664.0 +- 0.0
        Cytotoxic T cell 0.6149 +- 0.0028  0.86 +- 0.0032 0.7171 +- 0.0019   4839.0 +- 0.0
          Dendritic cell 0.9863 +- 0.0048 0.6253 +- 0.0424 0.7646 +- 0.0287    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0   0.5814 +- 0.0   0.7353 +- 0.0     86.0 +- 0.0
     Natural killer cell 0.915 +- 0.0081 0.1082 +- 0.021 0.1929 +- 0.032   2751.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     23.0 +- 0.0

                accuracy                                 0.8753 +- 0.001  28986.0 +- 0.0
               macro avg 0.9218 +- 0.0013 0.7695 +- 0.0072 0.7908 +- 0.0075  28986.0 +- 0.0
            weighted avg 0.8955 +- 0.0008 0.8753 +- 0.001 0.8505 +- 0.0031  28986.0 +- 0.0

Random dropout accuracy score 0.8733 +- 0.0017
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8753 +- 0.0006
Feature importance dropout (0.5% features dropped) accuracy score 0.8532 +- 0.0022
Feature importance dropout (1.0% features dropped) accuracy score 0.8239 +- 0.0031
Feature importance dropout (2.0% features dropped) accuracy score 0.7136 +- 0.0182
