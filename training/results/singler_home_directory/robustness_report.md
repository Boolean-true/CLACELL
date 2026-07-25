--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9717 +- 0.0

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0    120.0 +- 0.0
          CD14+ monocyte      1.0 +- 0.0   0.9984 +- 0.0   0.9992 +- 0.0   2575.0 +- 0.0
             CD4+ T cell   0.9941 +- 0.0   0.9829 +- 0.0   0.9884 +- 0.0   3910.0 +- 0.0
        Cytotoxic T cell   0.9402 +- 0.0   0.9391 +- 0.0   0.9397 +- 0.0   1824.0 +- 0.0
          Dendritic cell      0.5 +- 0.0      0.4 +- 0.0   0.4444 +- 0.0      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell   0.8468 +- 0.0   0.9014 +- 0.0   0.8732 +- 0.0    791.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     49.0 +- 0.0

                accuracy                                   0.9717 +- 0.0   9281.0 +- 0.0
               macro avg   0.9101 +- 0.0   0.9027 +- 0.0   0.9056 +- 0.0   9281.0 +- 0.0
            weighted avg   0.9724 +- 0.0   0.9717 +- 0.0   0.9719 +- 0.0   9281.0 +- 0.0

Random dropout accuracy score 0.9679 +- 0.0014
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9619 +- 0.0
Feature importance dropout (0.5% features dropped) accuracy score 0.939 +- 0.0
Feature importance dropout (1.0% features dropped) accuracy score 0.9112 +- 0.0
Feature importance dropout (2.0% features dropped) accuracy score 0.8702 +- 0.0
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.7762 +- 0.0

                               precision          recall        f1-score         support

                  B cell   0.9992 +- 0.0   0.9997 +- 0.0   0.9995 +- 0.0   3959.0 +- 0.0
          CD14+ monocyte   0.9346 +- 0.0   0.9984 +- 0.0   0.9655 +- 0.0   3135.0 +- 0.0
             CD4+ T cell   0.9973 +- 0.0   0.7431 +- 0.0   0.8517 +- 0.0  13664.0 +- 0.0
        Cytotoxic T cell   0.4363 +- 0.0   0.9944 +- 0.0   0.6065 +- 0.0   4839.0 +- 0.0
          Dendritic cell   0.9422 +- 0.0   0.6163 +- 0.0   0.7451 +- 0.0    529.0 +- 0.0
           Megakaryocyte   0.9559 +- 0.0   0.7558 +- 0.0   0.8442 +- 0.0     86.0 +- 0.0
     Natural killer cell      1.0 +- 0.0   0.0109 +- 0.0   0.0216 +- 0.0   2751.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     23.0 +- 0.0

                accuracy                                   0.7762 +- 0.0  28986.0 +- 0.0
               macro avg   0.9082 +- 0.0   0.7648 +- 0.0   0.7543 +- 0.0  28986.0 +- 0.0
            weighted avg   0.8963 +- 0.0   0.7762 +- 0.0   0.7626 +- 0.0  28986.0 +- 0.0

Random dropout accuracy score 0.7695 +- 0.0065
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.779 +- 0.0
Feature importance dropout (0.5% features dropped) accuracy score 0.7942 +- 0.0
Feature importance dropout (1.0% features dropped) accuracy score 0.7974 +- 0.0
Feature importance dropout (2.0% features dropped) accuracy score 0.8015 +- 0.0
