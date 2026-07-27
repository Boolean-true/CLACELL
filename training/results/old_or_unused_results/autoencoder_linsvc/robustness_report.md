--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.89 +- 0.0141

                               precision          recall        f1-score         support

                  B cell 0.9777 +- 0.0389 0.9875 +- 0.0059 0.9822 +- 0.0201    120.0 +- 0.0
          CD14+ monocyte 0.998 +- 0.0009 0.9981 +- 0.0005 0.9981 +- 0.0006   2575.0 +- 0.0
             CD4+ T cell 0.8427 +- 0.0212 0.9951 +- 0.0012 0.9125 +- 0.0121   3910.0 +- 0.0
        Cytotoxic T cell 0.9026 +- 0.0391 0.5292 +- 0.0763 0.6638 +- 0.0606   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0  0.44 +- 0.0843 0.6071 +- 0.0753      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.7998 +- 0.0651 0.8373 +- 0.0691 0.8138 +- 0.0328    791.0 +- 0.0
             Plasma cell 0.9697 +- 0.0167 0.898 +- 0.0897 0.9299 +- 0.0536     49.0 +- 0.0

                accuracy                                  0.89 +- 0.0141   9281.0 +- 0.0
               macro avg 0.9363 +- 0.0081 0.8356 +- 0.0223 0.8634 +- 0.0192   9281.0 +- 0.0
            weighted avg 0.8965 +- 0.0125  0.89 +- 0.0141 0.8798 +- 0.0175   9281.0 +- 0.0

Random dropout accuracy score 0.8721 +- 0.0156
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8868 +- 0.0139
Feature importance dropout (0.5% features dropped) accuracy score 0.8609 +- 0.0138
Feature importance dropout (1.0% features dropped) accuracy score 0.8343 +- 0.0129
Feature importance dropout (2.0% features dropped) accuracy score 0.7969 +- 0.0133
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8524 +- 0.0188

                               precision          recall        f1-score         support

                  B cell 0.9987 +- 0.0009 0.993 +- 0.0057 0.9958 +- 0.0028   3959.0 +- 0.0
          CD14+ monocyte 0.8675 +- 0.0378 0.9991 +- 0.0003 0.9283 +- 0.0217   3135.0 +- 0.0
             CD4+ T cell 0.8909 +- 0.0313 0.9854 +- 0.0114 0.9354 +- 0.0161  13664.0 +- 0.0
        Cytotoxic T cell 0.6096 +- 0.0387 0.6542 +- 0.0886 0.6291 +- 0.057   4839.0 +- 0.0
          Dendritic cell 0.9857 +- 0.0143 0.5983 +- 0.1755 0.728 +- 0.1785    529.0 +- 0.0
           Megakaryocyte 0.9983 +- 0.0055 0.6581 +- 0.0191 0.7931 +- 0.0139     86.0 +- 0.0
     Natural killer cell 0.8863 +- 0.0317 0.2249 +- 0.1054 0.3475 +- 0.1328   2751.0 +- 0.0
             Plasma cell 0.6719 +- 0.0689 0.9522 +- 0.0596 0.7854 +- 0.0526     23.0 +- 0.0

                accuracy                                 0.8524 +- 0.0188  28986.0 +- 0.0
               macro avg 0.8636 +- 0.017 0.7582 +- 0.0403 0.7678 +- 0.0426  28986.0 +- 0.0
            weighted avg 0.8575 +- 0.0201 0.8524 +- 0.0188 0.8316 +- 0.026  28986.0 +- 0.0

Random dropout accuracy score 0.8405 +- 0.0212
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8512 +- 0.0192
Feature importance dropout (0.5% features dropped) accuracy score 0.8328 +- 0.0198
Feature importance dropout (1.0% features dropped) accuracy score 0.8106 +- 0.0216
Feature importance dropout (2.0% features dropped) accuracy score 0.7509 +- 0.0291
