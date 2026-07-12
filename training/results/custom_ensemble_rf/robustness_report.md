--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.8671 +- 0.0021

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0   0.9917 +- 0.0   0.9958 +- 0.0    120.0 +- 0.0
          CD14+ monocyte 0.9986 +- 0.0002   1.0 +- 0.0001 0.9993 +- 0.0001   2575.0 +- 0.0
             CD4+ T cell 0.9145 +- 0.0031 0.9957 +- 0.0005 0.9533 +- 0.0017   3910.0 +- 0.0
        Cytotoxic T cell 0.9981 +- 0.0007 0.3437 +- 0.0107 0.5112 +- 0.0118   1824.0 +- 0.0
          Dendritic cell   0.9 +- 0.3162  0.18 +- 0.0632   0.3 +- 0.1054      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.4763 +- 0.0052 0.9946 +- 0.0006 0.6442 +- 0.0047    791.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.7898 +- 0.0099 0.8825 +- 0.0062     49.0 +- 0.0

                accuracy                                 0.8671 +- 0.0021   9281.0 +- 0.0
               macro avg 0.9109 +- 0.0395 0.7869 +- 0.0086 0.7858 +- 0.0136   9281.0 +- 0.0
            weighted avg 0.9185 +- 0.0013 0.8671 +- 0.0021 0.8527 +- 0.003   9281.0 +- 0.0

Random dropout accuracy score 0.8518 +- 0.0037
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8562 +- 0.0025
Feature importance dropout (0.5% features dropped) accuracy score 0.8257 +- 0.0019
Feature importance dropout (1.0% features dropped) accuracy score 0.8126 +- 0.0012
Feature importance dropout (2.0% features dropped) accuracy score 0.7898 +- 0.0013
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8825 +- 0.0017

                               precision          recall        f1-score         support

                  B cell 0.9991 +- 0.0001 0.9792 +- 0.0028 0.9891 +- 0.0014   3959.0 +- 0.0
          CD14+ monocyte 0.8481 +- 0.0005      1.0 +- 0.0 0.9178 +- 0.0003   3135.0 +- 0.0
             CD4+ T cell 0.8717 +- 0.0016   0.9988 +- 0.0 0.9309 +- 0.0009  13664.0 +- 0.0
        Cytotoxic T cell  0.8895 +- 0.01 0.5018 +- 0.0072 0.6416 +- 0.006   4839.0 +- 0.0
          Dendritic cell 0.9789 +- 0.0446 0.011 +- 0.0032 0.0217 +- 0.0062    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.5779 +- 0.0056 0.7325 +- 0.0045     86.0 +- 0.0
     Natural killer cell 0.8211 +- 0.0055 0.8807 +- 0.0121 0.8498 +- 0.0055   2751.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.6783 +- 0.0225 0.8081 +- 0.016     23.0 +- 0.0

                accuracy                                 0.8825 +- 0.0017  28986.0 +- 0.0
               macro avg 0.926 +- 0.0054 0.7035 +- 0.0035 0.7364 +- 0.0029  28986.0 +- 0.0
            weighted avg 0.8871 +- 0.0021 0.8825 +- 0.0017 0.8642 +- 0.002  28986.0 +- 0.0

Random dropout accuracy score 0.8666 +- 0.0015
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8785 +- 0.0017
Feature importance dropout (0.5% features dropped) accuracy score 0.8511 +- 0.0025
Feature importance dropout (1.0% features dropped) accuracy score 0.8064 +- 0.0031
Feature importance dropout (2.0% features dropped) accuracy score 0.6486 +- 0.0045
