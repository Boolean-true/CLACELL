--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.856 +- 0.0131

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0 0.9758 +- 0.0047 0.9878 +- 0.0024    120.0 +- 0.0
          CD14+ monocyte      1.0 +- 0.0 0.9987 +- 0.0004 0.9994 +- 0.0002   2575.0 +- 0.0
             CD4+ T cell 0.9553 +- 0.0021 0.9895 +- 0.0008 0.9721 +- 0.001   3910.0 +- 0.0
        Cytotoxic T cell 0.9839 +- 0.0016 0.4363 +- 0.0614 0.602 +- 0.0657   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0      0.4 +- 0.0   0.5714 +- 0.0      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.968 +- 0.0083 0.6802 +- 0.0066 0.7989 +- 0.007    791.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.8939 +- 0.0129 0.9439 +- 0.0073     49.0 +- 0.0
                  Reject      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0

                accuracy                                 0.856 +- 0.0131   9281.0 +- 0.0
               macro avg 0.8786 +- 0.0007 0.7083 +- 0.0094 0.7639 +- 0.009   9281.0 +- 0.0
            weighted avg 0.9753 +- 0.0008 0.856 +- 0.0131 0.892 +- 0.0134   9281.0 +- 0.0

10% Random Dropout accuracy: 0.8287 +- 0.011
50% Random Dropout accuracy: 0.5809 +- 0.0317
90% Random Dropout accuracy: 0.0 +- 0.0
92.5% Random Dropout accuracy: 0.0 +- 0.0
95% Random Dropout accuracy: 0.0 +- 0.0
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8552 +- 0.0129
Feature importance dropout (0.5% features dropped) accuracy score 0.8 +- 0.0073
Feature importance dropout (1.0% features dropped) accuracy score 0.7697 +- 0.0011
Feature importance dropout (2.0% features dropped) accuracy score 0.7344 +- 0.0011
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.7729 +- 0.0174

                               precision          recall        f1-score         support

                  B cell 0.9992 +- 0.0001 0.9495 +- 0.0213 0.9736 +- 0.0115   3959.0 +- 0.0
          CD14+ monocyte 0.9425 +- 0.0064 0.9979 +- 0.0014 0.9694 +- 0.0027   3135.0 +- 0.0
             CD4+ T cell 0.979 +- 0.0018 0.9053 +- 0.0207 0.9406 +- 0.0108  13664.0 +- 0.0
        Cytotoxic T cell 0.6717 +- 0.0201 0.5873 +- 0.0307 0.6257 +- 0.0113   4839.0 +- 0.0
          Dendritic cell 0.9914 +- 0.0018 0.4198 +- 0.0369 0.5891 +- 0.0358    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.557 +- 0.0037 0.7155 +- 0.0031     86.0 +- 0.0
     Natural killer cell 0.9234 +- 0.0126 0.0045 +- 0.0006 0.0089 +- 0.0012   2751.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9261 +- 0.0962 0.9589 +- 0.0595     23.0 +- 0.0
                  Reject      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0

                accuracy                                 0.7729 +- 0.0174  28986.0 +- 0.0
               macro avg 0.8341 +- 0.0021 0.5942 +- 0.0156 0.6424 +- 0.0072  28986.0 +- 0.0
            weighted avg 0.9215 +- 0.0037 0.7729 +- 0.0174 0.8002 +- 0.0077  28986.0 +- 0.0

10% Random Dropout accuracy: 0.7051 +- 0.0207
50% Random Dropout accuracy: 0.1316 +- 0.0549
90% Random Dropout accuracy: 0.0 +- 0.0
92.5% Random Dropout accuracy: 0.0 +- 0.0
95% Random Dropout accuracy: 0.0 +- 0.0
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.7673 +- 0.0178
Feature importance dropout (0.5% features dropped) accuracy score 0.7236 +- 0.029
Feature importance dropout (1.0% features dropped) accuracy score 0.6773 +- 0.0275
Feature importance dropout (2.0% features dropped) accuracy score 0.5089 +- 0.0184
