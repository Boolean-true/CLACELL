--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.853 +- 0.0069

                               precision          recall        f1-score         support

                  B cell 0.9991 +- 0.0029 0.9083 +- 0.0291 0.9513 +- 0.0159    120.0 +- 0.0
          CD14+ monocyte 0.9957 +- 0.0009      1.0 +- 0.0 0.9979 +- 0.0004   2575.0 +- 0.0
             CD4+ T cell 0.8688 +- 0.0059 0.9951 +- 0.0005 0.9277 +- 0.0034   3910.0 +- 0.0
        Cytotoxic T cell 0.9768 +- 0.0037 0.2783 +- 0.0339 0.4323 +- 0.0421   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0     0.5 +- 0.17 0.6528 +- 0.1363      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.9714 +- 0.0602 0.9846 +- 0.0324      7.0 +- 0.0
     Natural killer cell 0.5095 +- 0.0179 0.987 +- 0.0019 0.6719 +- 0.0156    791.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9041 +- 0.0216 0.9495 +- 0.012     49.0 +- 0.0

                accuracy                                 0.853 +- 0.0069   9281.0 +- 0.0
               macro avg 0.9187 +- 0.0027   0.818 +- 0.02 0.821 +- 0.0177   9281.0 +- 0.0
            weighted avg 0.8972 +- 0.0037 0.853 +- 0.0069 0.8283 +- 0.0103   9281.0 +- 0.0

Random dropout accuracy score 0.8509 +- 0.0106
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8458 +- 0.0071
Feature importance dropout (0.5% features dropped) accuracy score 0.8048 +- 0.0044
Feature importance dropout (1.0% features dropped) accuracy score 0.7055 +- 0.003
Feature importance dropout (2.0% features dropped) accuracy score 0.6896 +- 0.0122
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8887 +- 0.0026

                               precision          recall        f1-score         support

                  B cell 0.9985 +- 0.0002 0.9958 +- 0.0017 0.9971 +- 0.0009   3959.0 +- 0.0
          CD14+ monocyte 0.9207 +- 0.0035 0.9985 +- 0.0018 0.958 +- 0.0023   3135.0 +- 0.0
             CD4+ T cell 0.9489 +- 0.0025 0.985 +- 0.0025 0.9666 +- 0.0003  13664.0 +- 0.0
        Cytotoxic T cell 0.6684 +- 0.0131 0.7909 +- 0.0126 0.7244 +- 0.004   4839.0 +- 0.0
          Dendritic cell 0.9643 +- 0.0204 0.5866 +- 0.0224 0.7293 +- 0.0205    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.5802 +- 0.0159 0.7342 +- 0.0128     86.0 +- 0.0
     Natural killer cell 0.7671 +- 0.0155 0.3703 +- 0.0389 0.4985 +- 0.0357   2751.0 +- 0.0
             Plasma cell 0.9105 +- 0.0376   0.9565 +- 0.0 0.9326 +- 0.0201     23.0 +- 0.0

                accuracy                                 0.8887 +- 0.0026  28986.0 +- 0.0
               macro avg 0.8973 +- 0.0067 0.783 +- 0.0032 0.8176 +- 0.0033  28986.0 +- 0.0
            weighted avg 0.8889 +- 0.0022 0.8887 +- 0.0026 0.8799 +- 0.0035  28986.0 +- 0.0

Random dropout accuracy score 0.8624 +- 0.0181
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8851 +- 0.0034
Feature importance dropout (0.5% features dropped) accuracy score 0.7665 +- 0.0327
Feature importance dropout (1.0% features dropped) accuracy score 0.5925 +- 0.0057
Feature importance dropout (2.0% features dropped) accuracy score 0.541 +- 0.0184
