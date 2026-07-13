--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9249 +- 0.0061

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0   0.9917 +- 0.0   0.9958 +- 0.0    120.0 +- 0.0
          CD14+ monocyte 0.9921 +- 0.0033 0.9995 +- 0.0002 0.9958 +- 0.0017   2575.0 +- 0.0
             CD4+ T cell 0.8931 +- 0.0062 0.9953 +- 0.0005 0.9414 +- 0.0037   3910.0 +- 0.0
        Cytotoxic T cell 0.9084 +- 0.0037 0.7054 +- 0.0308 0.7939 +- 0.0217   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0  0.58 +- 0.0632 0.7321 +- 0.0565      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.8908 +- 0.0237 0.8273 +- 0.0027 0.8577 +- 0.0104    791.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9918 +- 0.0143 0.9959 +- 0.0073     49.0 +- 0.0

                accuracy                                 0.9249 +- 0.0061   9281.0 +- 0.0
               macro avg 0.9605 +- 0.0044  0.8864 +- 0.01 0.9141 +- 0.0091   9281.0 +- 0.0
            weighted avg 0.9254 +- 0.006 0.9249 +- 0.0061 0.9213 +- 0.007   9281.0 +- 0.0

Random dropout accuracy score 0.9188 +- 0.0112
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9251 +- 0.0068
Feature importance dropout (0.5% features dropped) accuracy score 0.8747 +- 0.0034
Feature importance dropout (1.0% features dropped) accuracy score 0.8589 +- 0.0044
Feature importance dropout (2.0% features dropped) accuracy score 0.8155 +- 0.0034
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8627 +- 0.0026

                               precision          recall        f1-score         support

                  B cell 0.9989 +- 0.0002 0.998 +- 0.0011 0.9984 +- 0.0006   3959.0 +- 0.0
          CD14+ monocyte 0.8541 +- 0.0213 0.9993 +- 0.0002 0.9209 +- 0.0124   3135.0 +- 0.0
             CD4+ T cell 0.9506 +- 0.0018 0.9761 +- 0.0032 0.9632 +- 0.0019  13664.0 +- 0.0
        Cytotoxic T cell 0.5992 +- 0.0015 0.8417 +- 0.0096 0.7001 +- 0.003   4839.0 +- 0.0
          Dendritic cell 0.987 +- 0.0004 0.5887 +- 0.0356 0.7369 +- 0.0268    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.5709 +- 0.0037 0.7269 +- 0.003     86.0 +- 0.0
     Natural killer cell 0.8848 +- 0.0123 0.0466 +- 0.0082 0.0883 +- 0.0147   2751.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9913 +- 0.0275 0.9955 +- 0.0144     23.0 +- 0.0

                accuracy                                 0.8627 +- 0.0026  28986.0 +- 0.0
               macro avg 0.9093 +- 0.004 0.7516 +- 0.0023 0.7663 +- 0.0037  28986.0 +- 0.0
            weighted avg 0.8827 +- 0.0038 0.8627 +- 0.0026 0.8317 +- 0.0029  28986.0 +- 0.0

Random dropout accuracy score 0.8575 +- 0.0033
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8619 +- 0.0025
Feature importance dropout (0.5% features dropped) accuracy score 0.8432 +- 0.0029
Feature importance dropout (1.0% features dropped) accuracy score 0.8315 +- 0.0025
Feature importance dropout (2.0% features dropped) accuracy score 0.7586 +- 0.012
