--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.885 +- 0.0125

                               precision          recall        f1-score         support

                  B cell 0.9755 +- 0.0153 0.9817 +- 0.0175 0.9784 +- 0.0092    120.0 +- 0.0
          CD14+ monocyte 0.9985 +- 0.0007 0.9977 +- 0.0006 0.9981 +- 0.0006   2575.0 +- 0.0
             CD4+ T cell 0.8444 +- 0.0248 0.9949 +- 0.001 0.9133 +- 0.0141   3910.0 +- 0.0
        Cytotoxic T cell 0.9292 +- 0.0253 0.4768 +- 0.066 0.6277 +- 0.0571   1824.0 +- 0.0
          Dendritic cell 0.9333 +- 0.1405  0.32 +- 0.1033 0.4619 +- 0.114      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.7276 +- 0.0431 0.907 +- 0.0353 0.8064 +- 0.0276    791.0 +- 0.0
             Plasma cell 0.9785 +- 0.0219 0.8327 +- 0.1201 0.8951 +- 0.0803     49.0 +- 0.0

                accuracy                                 0.885 +- 0.0125   9281.0 +- 0.0
               macro avg 0.9234 +- 0.017 0.8138 +- 0.028 0.8351 +- 0.0261   9281.0 +- 0.0
            weighted avg 0.8964 +- 0.0108 0.885 +- 0.0125 0.8721 +- 0.0166   9281.0 +- 0.0

Random dropout accuracy score 0.8695 +- 0.0147
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8819 +- 0.012
Feature importance dropout (0.5% features dropped) accuracy score 0.8603 +- 0.0121
Feature importance dropout (1.0% features dropped) accuracy score 0.8413 +- 0.0125
Feature importance dropout (2.0% features dropped) accuracy score 0.8088 +- 0.0105
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8504 +- 0.0126

                               precision          recall        f1-score         support

                  B cell 0.9988 +- 0.0004 0.9874 +- 0.0112 0.9931 +- 0.0057   3959.0 +- 0.0
          CD14+ monocyte 0.8992 +- 0.0199 0.9984 +- 0.0015 0.9461 +- 0.011   3135.0 +- 0.0
             CD4+ T cell 0.8793 +- 0.0204 0.9936 +- 0.0047 0.9328 +- 0.0104  13664.0 +- 0.0
        Cytotoxic T cell 0.5976 +- 0.0313 0.6108 +- 0.0668 0.6026 +- 0.0423   4839.0 +- 0.0
          Dendritic cell 0.9906 +- 0.0053 0.5989 +- 0.142 0.7364 +- 0.1297    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.6279 +- 0.0155 0.7713 +- 0.0116     86.0 +- 0.0
     Natural killer cell 0.8737 +- 0.0427 0.2509 +- 0.0974 0.3795 +- 0.1201   2751.0 +- 0.0
             Plasma cell 0.7067 +- 0.1436 0.7261 +- 0.2617 0.6871 +- 0.2014     23.0 +- 0.0

                accuracy                                 0.8504 +- 0.0126  28986.0 +- 0.0
               macro avg 0.8682 +- 0.0213 0.7242 +- 0.052 0.7561 +- 0.0436  28986.0 +- 0.0
            weighted avg 0.8525 +- 0.0157 0.8504 +- 0.0126 0.8306 +- 0.017  28986.0 +- 0.0

Random dropout accuracy score 0.8388 +- 0.0143
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8495 +- 0.013
Feature importance dropout (0.5% features dropped) accuracy score 0.8292 +- 0.0157
Feature importance dropout (1.0% features dropped) accuracy score 0.8087 +- 0.0181
Feature importance dropout (2.0% features dropped) accuracy score 0.7331 +- 0.0318
