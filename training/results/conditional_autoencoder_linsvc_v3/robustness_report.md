--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9148 +- 0.0064

                               precision          recall        f1-score         support

                  B cell 0.9941 +- 0.004 0.9892 +- 0.0056 0.9916 +- 0.004    120.0 +- 0.0
          CD14+ monocyte 0.9972 +- 0.0013 0.9985 +- 0.0004 0.9978 +- 0.0007   2575.0 +- 0.0
             CD4+ T cell 0.925 +- 0.0149 0.9934 +- 0.0013 0.9579 +- 0.0076   3910.0 +- 0.0
        Cytotoxic T cell 0.8438 +- 0.0265 0.725 +- 0.0459 0.7786 +- 0.0217   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0  0.48 +- 0.1398 0.6389 +- 0.115      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.7172 +- 0.0502 0.6796 +- 0.0777 0.694 +- 0.0393    791.0 +- 0.0
             Plasma cell 0.9712 +- 0.0171 0.9571 +- 0.0179 0.964 +- 0.0139     49.0 +- 0.0

                accuracy                                 0.9148 +- 0.0064   9281.0 +- 0.0
               macro avg 0.9311 +- 0.0049 0.8529 +- 0.0189 0.8779 +- 0.0162   9281.0 +- 0.0
            weighted avg 0.9126 +- 0.0069 0.9148 +- 0.0064 0.9116 +- 0.0069   9281.0 +- 0.0

Random dropout accuracy score 0.9073 +- 0.0049
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9132 +- 0.0063
Feature importance dropout (0.5% features dropped) accuracy score 0.8954 +- 0.0075
Feature importance dropout (1.0% features dropped) accuracy score 0.8755 +- 0.0091
Feature importance dropout (2.0% features dropped) accuracy score 0.8357 +- 0.0128
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8749 +- 0.007

                               precision          recall        f1-score         support

                  B cell 0.9991 +- 0.0003 0.9949 +- 0.0022 0.997 +- 0.0011   3959.0 +- 0.0
          CD14+ monocyte 0.8909 +- 0.0226 0.9993 +- 0.0004 0.9419 +- 0.0126   3135.0 +- 0.0
             CD4+ T cell 0.9386 +- 0.007 0.9871 +- 0.0036 0.9622 +- 0.0034  13664.0 +- 0.0
        Cytotoxic T cell 0.6354 +- 0.018 0.7792 +- 0.0273 0.6997 +- 0.0152   4839.0 +- 0.0
          Dendritic cell 0.9849 +- 0.0062 0.5964 +- 0.0576 0.7415 +- 0.0456    529.0 +- 0.0
           Megakaryocyte 0.9984 +- 0.0052 0.6616 +- 0.0271 0.7955 +- 0.0189     86.0 +- 0.0
     Natural killer cell 0.7868 +- 0.0427 0.231 +- 0.0675 0.3522 +- 0.0779   2751.0 +- 0.0
             Plasma cell 0.8447 +- 0.1455 0.9826 +- 0.0304 0.9019 +- 0.0918     23.0 +- 0.0

                accuracy                                 0.8749 +- 0.007  28986.0 +- 0.0
               macro avg 0.8848 +- 0.0186   0.779 +- 0.01 0.799 +- 0.0127  28986.0 +- 0.0
            weighted avg 0.8776 +- 0.0079 0.8749 +- 0.007 0.8585 +- 0.0103  28986.0 +- 0.0

Random dropout accuracy score 0.8689 +- 0.0086
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8745 +- 0.0071
Feature importance dropout (0.5% features dropped) accuracy score 0.8634 +- 0.0079
Feature importance dropout (1.0% features dropped) accuracy score 0.8518 +- 0.0108
Feature importance dropout (2.0% features dropped) accuracy score 0.8 +- 0.0247
