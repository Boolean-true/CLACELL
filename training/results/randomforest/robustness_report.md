--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.8838 +- 0.0041

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0 0.9883 +- 0.0058 0.9941 +- 0.003    120.0 +- 0.0
          CD14+ monocyte 0.9985 +- 0.0002      1.0 +- 0.0 0.9993 +- 0.0001   2575.0 +- 0.0
             CD4+ T cell 0.9341 +- 0.0024 0.9962 +- 0.0003 0.9641 +- 0.0013   3910.0 +- 0.0
        Cytotoxic T cell 0.9978 +- 0.001 0.4265 +- 0.0206 0.5973 +- 0.0202   1824.0 +- 0.0
          Dendritic cell    0.7 +- 0.483  0.14 +- 0.0966 0.2333 +- 0.161      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.4968 +- 0.0124 0.9943 +- 0.0011 0.6625 +- 0.011    791.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.8531 +- 0.0129 0.9207 +- 0.0075     49.0 +- 0.0

                accuracy                                 0.8838 +- 0.0041   9281.0 +- 0.0
               macro avg 0.8909 +- 0.0606 0.7998 +- 0.0127 0.7964 +- 0.0209   9281.0 +- 0.0
            weighted avg 0.9283 +- 0.0014 0.8838 +- 0.0041 0.8759 +- 0.0049   9281.0 +- 0.0

Random dropout accuracy score 0.8717 +- 0.0065
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8448 +- 0.0014
Feature importance dropout (0.5% features dropped) accuracy score 0.8191 +- 0.0025
Feature importance dropout (1.0% features dropped) accuracy score 0.7946 +- 0.002
Feature importance dropout (2.0% features dropped) accuracy score 0.7155 +- 0.0045
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8972 +- 0.0048

                               precision          recall        f1-score         support

                  B cell 0.9988 +- 0.0002 0.9994 +- 0.0002 0.9991 +- 0.0001   3959.0 +- 0.0
          CD14+ monocyte 0.8694 +- 0.003   1.0 +- 0.0001 0.9301 +- 0.0017   3135.0 +- 0.0
             CD4+ T cell 0.9152 +- 0.0036 0.9975 +- 0.0003 0.9546 +- 0.0019  13664.0 +- 0.0
        Cytotoxic T cell 0.7706 +- 0.0263 0.6972 +- 0.0157 0.7316 +- 0.0108   4839.0 +- 0.0
          Dendritic cell 0.9873 +- 0.0044 0.1788 +- 0.0233 0.3022 +- 0.0343    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0   0.5698 +- 0.0   0.7259 +- 0.0     86.0 +- 0.0
     Natural killer cell  0.885 +- 0.011 0.6355 +- 0.0603 0.738 +- 0.0392   2751.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.8739 +- 0.0321 0.9324 +- 0.0183     23.0 +- 0.0

                accuracy                                 0.8972 +- 0.0048  28986.0 +- 0.0
               macro avg 0.9283 +- 0.0024 0.744 +- 0.0095 0.7892 +- 0.0089  28986.0 +- 0.0
            weighted avg 0.8963 +- 0.0041 0.8972 +- 0.0048 0.8876 +- 0.0056  28986.0 +- 0.0

Random dropout accuracy score 0.886 +- 0.0052
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8906 +- 0.0039
Feature importance dropout (0.5% features dropped) accuracy score 0.8548 +- 0.0033
Feature importance dropout (1.0% features dropped) accuracy score 0.7175 +- 0.0153
Feature importance dropout (2.0% features dropped) accuracy score 0.5789 +- 0.0009
