--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9259 +- 0.0131

                               precision          recall        f1-score         support

                  B cell 0.9707 +- 0.0182 0.9833 +- 0.0079 0.9769 +- 0.0091    120.0 +- 0.0
          CD14+ monocyte 0.9965 +- 0.0013 0.9981 +- 0.0007 0.9973 +- 0.0006   2575.0 +- 0.0
             CD4+ T cell 0.9599 +- 0.0276 0.9838 +- 0.0049 0.9714 +- 0.0125   3910.0 +- 0.0
        Cytotoxic T cell 0.8779 +- 0.0477 0.7752 +- 0.1043 0.8172 +- 0.0507   1824.0 +- 0.0
          Dendritic cell   0.9 +- 0.3162  0.36 +- 0.1265 0.5143 +- 0.1807      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.6723 +- 0.0761 0.7475 +- 0.1224 0.7003 +- 0.0676    791.0 +- 0.0
             Plasma cell 0.9802 +- 0.0193 0.9041 +- 0.0334 0.9403 +- 0.0226     49.0 +- 0.0

                accuracy                                 0.9259 +- 0.0131   9281.0 +- 0.0
               macro avg 0.9197 +- 0.0409 0.844 +- 0.0216 0.8647 +- 0.0258   9281.0 +- 0.0
            weighted avg 0.9297 +- 0.0098 0.9259 +- 0.0131 0.9249 +- 0.0142   9281.0 +- 0.0

10% Random Dropout accuracy: 0.9191 +- 0.0162
50% Random Dropout accuracy: 0.8285 +- 0.0377
90% Random Dropout accuracy: 0.5156 +- 0.1033
92.5% Random Dropout accuracy: 0.4838 +- 0.098
95% Random Dropout accuracy: 0.4562 +- 0.0797
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9221 +- 0.0144
Feature importance dropout (0.5% features dropped) accuracy score 0.9064 +- 0.0206
Feature importance dropout (1.0% features dropped) accuracy score 0.8922 +- 0.0233
Feature importance dropout (2.0% features dropped) accuracy score 0.8654 +- 0.0245
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8751 +- 0.0091

                               precision          recall        f1-score         support

                  B cell 0.9989 +- 0.0004 0.9724 +- 0.0123 0.9855 +- 0.0063   3959.0 +- 0.0
          CD14+ monocyte 0.9054 +- 0.0215 0.999 +- 0.0007 0.9498 +- 0.0121   3135.0 +- 0.0
             CD4+ T cell 0.9209 +- 0.0273 0.9861 +- 0.0075 0.9521 +- 0.012  13664.0 +- 0.0
        Cytotoxic T cell 0.675 +- 0.0608 0.6956 +- 0.1232 0.6741 +- 0.0502   4839.0 +- 0.0
          Dendritic cell 0.994 +- 0.0022 0.7197 +- 0.0662 0.8333 +- 0.0454    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.6314 +- 0.0251 0.7738 +- 0.0191     86.0 +- 0.0
     Natural killer cell 0.7355 +- 0.0588 0.3965 +- 0.2031 0.4904 +- 0.1589   2751.0 +- 0.0
             Plasma cell 0.7499 +- 0.1279 0.8217 +- 0.1594 0.7741 +- 0.1213     23.0 +- 0.0

                accuracy                                 0.8751 +- 0.0091  28986.0 +- 0.0
               macro avg 0.8724 +- 0.0228 0.7778 +- 0.0249 0.8041 +- 0.0233  28986.0 +- 0.0
            weighted avg 0.8727 +- 0.0109 0.8751 +- 0.0091 0.8633 +- 0.0124  28986.0 +- 0.0

10% Random Dropout accuracy: 0.866 +- 0.0135
50% Random Dropout accuracy: 0.7099 +- 0.0439
90% Random Dropout accuracy: 0.4944 +- 0.0383
92.5% Random Dropout accuracy: 0.487 +- 0.031
95% Random Dropout accuracy: 0.4807 +- 0.0241
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8723 +- 0.0097
Feature importance dropout (0.5% features dropped) accuracy score 0.8446 +- 0.0168
Feature importance dropout (1.0% features dropped) accuracy score 0.8189 +- 0.0225
Feature importance dropout (2.0% features dropped) accuracy score 0.7321 +- 0.0288
