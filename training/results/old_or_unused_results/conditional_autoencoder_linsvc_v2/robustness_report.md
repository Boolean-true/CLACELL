--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9043 +- 0.0147

                               precision          recall        f1-score         support

                  B cell 0.9908 +- 0.0073 0.9808 +- 0.0125 0.9857 +- 0.0078    120.0 +- 0.0
          CD14+ monocyte 0.9973 +- 0.0011 0.9983 +- 0.0004 0.9978 +- 0.0005   2575.0 +- 0.0
             CD4+ T cell 0.9044 +- 0.0288 0.9948 +- 0.0019 0.9472 +- 0.015   3910.0 +- 0.0
        Cytotoxic T cell 0.8489 +- 0.0287 0.6586 +- 0.1018 0.737 +- 0.0583   1824.0 +- 0.0
          Dendritic cell  0.9167 +- 0.18   0.4 +- 0.0943 0.5456 +- 0.1071      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.7038 +- 0.0612 0.7043 +- 0.0831 0.6988 +- 0.0388    791.0 +- 0.0
             Plasma cell 0.9562 +- 0.0201 0.9694 +- 0.0173 0.9625 +- 0.0107     49.0 +- 0.0

                accuracy                                 0.9043 +- 0.0147   9281.0 +- 0.0
               macro avg 0.9148 +- 0.0247 0.8383 +- 0.0145 0.8593 +- 0.0169   9281.0 +- 0.0
            weighted avg 0.9036 +- 0.0135 0.9043 +- 0.0147 0.8991 +- 0.0164   9281.0 +- 0.0

Random dropout accuracy score 0.8919 +- 0.0153
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9013 +- 0.0148
Feature importance dropout (0.5% features dropped) accuracy score 0.8791 +- 0.0162
Feature importance dropout (1.0% features dropped) accuracy score 0.852 +- 0.0195
Feature importance dropout (2.0% features dropped) accuracy score 0.8075 +- 0.0213
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8683 +- 0.0078

                               precision          recall        f1-score         support

                  B cell 0.9988 +- 0.0004 0.9922 +- 0.0058 0.9955 +- 0.0029   3959.0 +- 0.0
          CD14+ monocyte 0.867 +- 0.0365 0.9985 +- 0.0013 0.9277 +- 0.0215   3135.0 +- 0.0
             CD4+ T cell 0.9294 +- 0.0104 0.982 +- 0.0085 0.9549 +- 0.0052  13664.0 +- 0.0
        Cytotoxic T cell 0.6344 +- 0.0191 0.7488 +- 0.0468 0.6858 +- 0.0187   4839.0 +- 0.0
          Dendritic cell 0.9853 +- 0.0032 0.624 +- 0.0556 0.7628 +- 0.042    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.643 +- 0.0325 0.7823 +- 0.0241     86.0 +- 0.0
     Natural killer cell 0.782 +- 0.0493 0.2408 +- 0.0904 0.3586 +- 0.1012   2751.0 +- 0.0
             Plasma cell 0.7596 +- 0.1561 0.9739 +- 0.0367 0.8453 +- 0.097     23.0 +- 0.0

                accuracy                                 0.8683 +- 0.0078  28986.0 +- 0.0
               macro avg 0.8696 +- 0.0203 0.7754 +- 0.0159 0.7891 +- 0.0196  28986.0 +- 0.0
            weighted avg  0.87 +- 0.0086 0.8683 +- 0.0078 0.8519 +- 0.0118  28986.0 +- 0.0

Random dropout accuracy score 0.8607 +- 0.0094
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8674 +- 0.0078
Feature importance dropout (0.5% features dropped) accuracy score 0.8532 +- 0.0088
Feature importance dropout (1.0% features dropped) accuracy score 0.8345 +- 0.0127
Feature importance dropout (2.0% features dropped) accuracy score 0.7776 +- 0.0216
