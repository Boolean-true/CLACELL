--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9187 +- 0.0163

                               precision          recall        f1-score         support

                  B cell 0.9992 +- 0.0027 0.9883 +- 0.0058 0.9937 +- 0.0036    120.0 +- 0.0
          CD14+ monocyte 0.9933 +- 0.0027 0.9998 +- 0.0003 0.9966 +- 0.0014   2575.0 +- 0.0
             CD4+ T cell 0.8854 +- 0.0324 0.9974 +- 0.0014 0.9378 +- 0.0177   3910.0 +- 0.0
        Cytotoxic T cell 0.9461 +- 0.0253 0.6371 +- 0.1032 0.7561 +- 0.0657   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0  0.48 +- 0.1033 0.6429 +- 0.0922      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.8255 +- 0.052 0.9024 +- 0.0623 0.8592 +- 0.0235    791.0 +- 0.0
             Plasma cell 0.9979 +- 0.0066 0.9755 +- 0.0086 0.9866 +- 0.007     49.0 +- 0.0

                accuracy                                 0.9187 +- 0.0163   9281.0 +- 0.0
               macro avg 0.9559 +- 0.0068 0.8726 +- 0.0172 0.8966 +- 0.0159   9281.0 +- 0.0
            weighted avg 0.9244 +- 0.0126 0.9187 +- 0.0163 0.9126 +- 0.0196   9281.0 +- 0.0

10% Random Dropout accuracy: N/A
50% Random Dropout accuracy: N/A
90% Random Dropout accuracy: N/A
92.5% Random Dropout accuracy: N/A
95% Random Dropout accuracy: N/A
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9112 +- 0.0176
Feature importance dropout (0.5% features dropped) accuracy score 0.8691 +- 0.0205
Feature importance dropout (1.0% features dropped) accuracy score 0.792 +- 0.0085
Feature importance dropout (2.0% features dropped) accuracy score 0.7258 +- 0.0106
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.864 +- 0.0024

                               precision          recall        f1-score         support

                  B cell 0.9991 +- 0.0002 0.9946 +- 0.0111 0.9968 +- 0.0057   3959.0 +- 0.0
          CD14+ monocyte 0.8446 +- 0.0151 0.9996 +- 0.0002 0.9155 +- 0.0088   3135.0 +- 0.0
             CD4+ T cell 0.9425 +- 0.018 0.9903 +- 0.0046 0.9657 +- 0.0079  13664.0 +- 0.0
        Cytotoxic T cell 0.6127 +- 0.0098 0.8152 +- 0.0574 0.6985 +- 0.0184   4839.0 +- 0.0
          Dendritic cell 0.985 +- 0.0042 0.3425 +- 0.1138 0.4988 +- 0.1243    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.6186 +- 0.0218 0.7642 +- 0.0167     86.0 +- 0.0
     Natural killer cell  0.92 +- 0.0417 0.0869 +- 0.0684 0.1514 +- 0.1038   2751.0 +- 0.0
             Plasma cell 0.9958 +- 0.0132      1.0 +- 0.0 0.9979 +- 0.0067     23.0 +- 0.0

                accuracy                                 0.864 +- 0.0024  28986.0 +- 0.0
               macro avg 0.9125 +- 0.0069 0.731 +- 0.0121 0.7486 +- 0.0203  28986.0 +- 0.0
            weighted avg 0.8834 +- 0.0102 0.864 +- 0.0024 0.8335 +- 0.0054  28986.0 +- 0.0

10% Random Dropout accuracy: N/A
50% Random Dropout accuracy: N/A
90% Random Dropout accuracy: N/A
92.5% Random Dropout accuracy: N/A
95% Random Dropout accuracy: N/A
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8616 +- 0.0031
Feature importance dropout (0.5% features dropped) accuracy score 0.838 +- 0.0078
Feature importance dropout (1.0% features dropped) accuracy score 0.721 +- 0.0262
Feature importance dropout (2.0% features dropped) accuracy score 0.584 +- 0.0034
