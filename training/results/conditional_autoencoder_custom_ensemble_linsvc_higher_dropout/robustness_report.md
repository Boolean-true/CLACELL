--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9074 +- 0.0064

                               precision          recall        f1-score         support

                  B cell 0.9916 +- 0.004 0.9833 +- 0.0056 0.9874 +- 0.004    120.0 +- 0.0
          CD14+ monocyte 0.9975 +- 0.0008 0.9984 +- 0.0004 0.9979 +- 0.0005   2575.0 +- 0.0
             CD4+ T cell 0.9104 +- 0.0111 0.9952 +- 0.0011 0.9509 +- 0.0061   3910.0 +- 0.0
        Cytotoxic T cell 0.8323 +- 0.0271 0.6941 +- 0.047 0.7556 +- 0.0237   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0  0.42 +- 0.0632 0.5893 +- 0.0565      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.718 +- 0.0481 0.6576 +- 0.0752 0.6827 +- 0.0358    791.0 +- 0.0
             Plasma cell 0.981 +- 0.0154 0.9327 +- 0.0168 0.956 +- 0.0083     49.0 +- 0.0

                accuracy                                 0.9074 +- 0.0064   9281.0 +- 0.0
               macro avg 0.9288 +- 0.0061 0.8352 +- 0.0076 0.865 +- 0.0078   9281.0 +- 0.0
            weighted avg 0.9043 +- 0.0067 0.9074 +- 0.0064  0.903 +- 0.007   9281.0 +- 0.0

10% Random Dropout accuracy: 0.897 +- 0.0058
50% Random Dropout accuracy: 0.8084 +- 0.0182
90% Random Dropout accuracy: 0.6301 +- 0.0502
92.5% Random Dropout accuracy: 0.5641 +- 0.0752
95% Random Dropout accuracy: 0.4808 +- 0.0758
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9049 +- 0.0068
Feature importance dropout (0.5% features dropped) accuracy score 0.8848 +- 0.0065
Feature importance dropout (1.0% features dropped) accuracy score 0.861 +- 0.0063
Feature importance dropout (2.0% features dropped) accuracy score 0.8208 +- 0.0103
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8702 +- 0.0071

                               precision          recall        f1-score         support

                  B cell 0.9992 +- 0.0004 0.9923 +- 0.0026 0.9957 +- 0.0012   3959.0 +- 0.0
          CD14+ monocyte 0.8864 +- 0.0325 0.999 +- 0.0009 0.9391 +- 0.019   3135.0 +- 0.0
             CD4+ T cell  0.93 +- 0.0159 0.9868 +- 0.008 0.9575 +- 0.0079  13664.0 +- 0.0
        Cytotoxic T cell 0.6311 +- 0.0238 0.7641 +- 0.0606 0.6896 +- 0.0209   4839.0 +- 0.0
          Dendritic cell 0.9871 +- 0.0067 0.5378 +- 0.0618 0.6944 +- 0.0531    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.6244 +- 0.0285 0.7684 +- 0.0216     86.0 +- 0.0
     Natural killer cell 0.8087 +- 0.0459 0.2263 +- 0.1019 0.343 +- 0.1269   2751.0 +- 0.0
             Plasma cell 0.7785 +- 0.142 0.9783 +- 0.0307 0.8603 +- 0.089     23.0 +- 0.0

                accuracy                                 0.8702 +- 0.0071  28986.0 +- 0.0
               macro avg 0.8776 +- 0.0184 0.7636 +- 0.0089 0.781 +- 0.0176  28986.0 +- 0.0
            weighted avg 0.8745 +- 0.0098 0.8702 +- 0.0071  0.8522 +- 0.01  28986.0 +- 0.0

10% Random Dropout accuracy: 0.8637 +- 0.0069
50% Random Dropout accuracy: 0.7523 +- 0.026
90% Random Dropout accuracy: 0.4701 +- 0.1041
92.5% Random Dropout accuracy: 0.443 +- 0.1231
95% Random Dropout accuracy: 0.4147 +- 0.1415
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8697 +- 0.0072
Feature importance dropout (0.5% features dropped) accuracy score 0.8566 +- 0.0072
Feature importance dropout (1.0% features dropped) accuracy score 0.8402 +- 0.0096
Feature importance dropout (2.0% features dropped) accuracy score 0.7764 +- 0.0214
