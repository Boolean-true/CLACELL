--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.8475 +- 0.0017

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9921 +- 0.0004 0.9982 +- 0.0004 0.9952 +- 0.0002   3456.0 +- 0.0
          CD16+ Monocyte 0.9822 +- 0.0066 0.9409 +- 0.0044 0.9611 +- 0.0037    193.0 +- 0.0
    CD1C+ dendritic cell 0.9588 +- 0.0001 0.862 +- 0.0029 0.9078 +- 0.0017    108.0 +- 0.0
       CD4 Memory T cell 0.9311 +- 0.0025 0.7318 +- 0.0179 0.8193 +- 0.0106   2888.0 +- 0.0
        CD4 Naive T cell 0.7757 +- 0.0079 0.9186 +- 0.0031 0.8411 +- 0.0054   3439.0 +- 0.0
       CD8 Memory T cell 0.0025 +- 0.0003  0.58 +- 0.0632 0.0051 +- 0.0006      5.0 +- 0.0
        CD8 Naive T cell 0.8836 +- 0.0046 0.8411 +- 0.0072 0.8619 +- 0.0056   2047.0 +- 0.0
      Gamma-delta T cell 0.9611 +- 0.002 0.6877 +- 0.0108 0.8017 +- 0.0075   2544.0 +- 0.0
                    MAIT 0.7415 +- 0.0075 0.847 +- 0.0065 0.7908 +- 0.0062    974.0 +- 0.0
           Memory B cell 0.8872 +- 0.0026 0.938 +- 0.0036 0.9119 +- 0.002    897.0 +- 0.0
                 NK cell 0.9786 +- 0.001 0.7669 +- 0.0034 0.8599 +- 0.002   2580.0 +- 0.0
            Naive B cell 0.9744 +- 0.0014 0.952 +- 0.0013 0.9631 +- 0.0008   2227.0 +- 0.0
             Plasma cell      1.0 +- 0.0   0.9643 +- 0.0   0.9818 +- 0.0     56.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.7509 +- 0.0138 0.8577 +- 0.0091     57.0 +- 0.0
       T regulatory cell 0.6374 +- 0.0096 0.7047 +- 0.0046 0.6693 +- 0.0058    949.0 +- 0.0

                accuracy                                 0.8475 +- 0.0017  22420.0 +- 0.0
               macro avg 0.8471 +- 0.0017 0.8323 +- 0.0044 0.8152 +- 0.0013  22420.0 +- 0.0
            weighted avg 0.9038 +- 0.0019 0.8475 +- 0.0017 0.8687 +- 0.0019  22420.0 +- 0.0

10% Random Dropout accuracy: 0.8376 +- 0.0028
50% Random Dropout accuracy: 0.762 +- 0.0064
90% Random Dropout accuracy: 0.4439 +- 0.0213
92.5% Random Dropout accuracy: 0.3943 +- 0.0235
95% Random Dropout accuracy: 0.3335 +- 0.0238
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8449 +- 0.0016
Feature importance dropout (0.5% features dropped) accuracy score 0.832 +- 0.0022
Feature importance dropout (1.0% features dropped) accuracy score 0.8286 +- 0.0024
Feature importance dropout (2.0% features dropped) accuracy score 0.8081 +- 0.0025
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.6319 +- 0.0059

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9059 +- 0.0096 0.9997 +- 0.0001 0.9504 +- 0.0053  12317.0 +- 0.0
          CD16+ Monocyte 0.9942 +- 0.0019 0.6826 +- 0.0517 0.8084 +- 0.0357   1903.0 +- 0.0
    CD1C+ dendritic cell  0.996 +- 0.001 0.5487 +- 0.0471 0.7064 +- 0.0404   1079.0 +- 0.0
       CD4 Memory T cell 0.4478 +- 0.0103 0.7907 +- 0.0202 0.5716 +- 0.0071  14241.0 +- 0.0
        CD4 Naive T cell 0.862 +- 0.0145 0.3612 +- 0.0446 0.5072 +- 0.0457  17151.0 +- 0.0
       CD8 Memory T cell 0.2431 +- 0.0309 0.1582 +- 0.0311 0.1914 +- 0.0321   6650.0 +- 0.0
        CD8 Naive T cell 0.9222 +- 0.0046 0.7508 +- 0.0255 0.8275 +- 0.015   6516.0 +- 0.0
      Gamma-delta T cell 0.0763 +- 0.0063 0.1484 +- 0.0221 0.1006 +- 0.0106   2271.0 +- 0.0
                    MAIT 0.4454 +- 0.0127 0.9653 +- 0.0058 0.6094 +- 0.011   2889.0 +- 0.0
           Memory B cell 0.951 +- 0.0016  0.508 +- 0.014 0.6621 +- 0.0119   1395.0 +- 0.0
                 NK cell 0.9761 +- 0.0046 0.5947 +- 0.0279 0.7387 +- 0.0212   5959.0 +- 0.0
            Naive B cell 0.8269 +- 0.0046 0.9926 +- 0.0003 0.9022 +- 0.0026   3385.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9874 +- 0.0007 0.9937 +- 0.0004    930.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0    0.988 +- 0.0    0.994 +- 0.0    584.0 +- 0.0
       T regulatory cell 0.089 +- 0.0025 0.0481 +- 0.0089 0.062 +- 0.0081   1731.0 +- 0.0

                accuracy                                 0.6319 +- 0.0059  79001.0 +- 0.0
               macro avg 0.7157 +- 0.0017 0.635 +- 0.0062 0.6417 +- 0.0049  79001.0 +- 0.0
            weighted avg 0.7086 +- 0.0041 0.6319 +- 0.0059 0.6265 +- 0.0089  79001.0 +- 0.0

10% Random Dropout accuracy: 0.6282 +- 0.0067
50% Random Dropout accuracy: 0.6023 +- 0.0104
90% Random Dropout accuracy: 0.4431 +- 0.0102
92.5% Random Dropout accuracy: 0.4173 +- 0.0136
95% Random Dropout accuracy: 0.3544 +- 0.0196
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.6324 +- 0.0059
Feature importance dropout (0.5% features dropped) accuracy score 0.6331 +- 0.0063
Feature importance dropout (1.0% features dropped) accuracy score 0.6181 +- 0.006
Feature importance dropout (2.0% features dropped) accuracy score 0.5939 +- 0.0059
