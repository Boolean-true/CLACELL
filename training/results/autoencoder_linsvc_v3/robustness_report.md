--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9078 +- 0.0086

                               precision          recall        f1-score         support

                  B cell 0.9941 +- 0.0057 0.9825 +- 0.0061 0.9883 +- 0.0043    120.0 +- 0.0
          CD14+ monocyte 0.9962 +- 0.0025 0.9983 +- 0.0005 0.9972 +- 0.0012   2575.0 +- 0.0
             CD4+ T cell 0.8855 +- 0.0226 0.9949 +- 0.0016 0.9369 +- 0.0121   3910.0 +- 0.0
        Cytotoxic T cell 0.9051 +- 0.0168 0.6201 +- 0.0542 0.7344 +- 0.0356   1824.0 +- 0.0
          Dendritic cell 0.975 +- 0.0791  0.52 +- 0.1033 0.6702 +- 0.0887      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.7565 +- 0.0621 0.8321 +- 0.0394 0.7907 +- 0.039    791.0 +- 0.0
             Plasma cell 0.9678 +- 0.026 0.9653 +- 0.0216 0.9663 +- 0.0195     49.0 +- 0.0

                accuracy                                 0.9078 +- 0.0086   9281.0 +- 0.0
               macro avg 0.935 +- 0.0133 0.8642 +- 0.0149 0.8855 +- 0.0145   9281.0 +- 0.0
            weighted avg 0.911 +- 0.0067 0.9078 +- 0.0086 0.9021 +- 0.0103   9281.0 +- 0.0

Random dropout accuracy score 0.8968 +- 0.0106
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9049 +- 0.008
Feature importance dropout (0.5% features dropped) accuracy score 0.8835 +- 0.0083
Feature importance dropout (1.0% features dropped) accuracy score 0.8564 +- 0.0128
Feature importance dropout (2.0% features dropped) accuracy score 0.8139 +- 0.0126
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8673 +- 0.0065

                               precision          recall        f1-score         support

                  B cell 0.999 +- 0.0004 0.9889 +- 0.0092 0.9939 +- 0.0046   3959.0 +- 0.0
          CD14+ monocyte 0.8792 +- 0.0296 0.9989 +- 0.0008 0.935 +- 0.0167   3135.0 +- 0.0
             CD4+ T cell 0.9347 +- 0.0149 0.9835 +- 0.007 0.9583 +- 0.0058  13664.0 +- 0.0
        Cytotoxic T cell 0.6178 +- 0.013 0.7929 +- 0.0496 0.6935 +- 0.0147   4839.0 +- 0.0
          Dendritic cell 0.9849 +- 0.0044 0.6106 +- 0.0877 0.7504 +- 0.0715    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.6593 +- 0.0347 0.7942 +- 0.0249     86.0 +- 0.0
     Natural killer cell 0.8683 +- 0.024 0.1514 +- 0.073 0.2509 +- 0.1008   2751.0 +- 0.0
             Plasma cell 0.6747 +- 0.1007      1.0 +- 0.0 0.8021 +- 0.0681     23.0 +- 0.0

                accuracy                                 0.8673 +- 0.0065  28986.0 +- 0.0
               macro avg 0.8698 +- 0.0135 0.7732 +- 0.0173 0.7723 +- 0.0185  28986.0 +- 0.0
            weighted avg 0.8792 +- 0.0075 0.8673 +- 0.0065 0.8449 +- 0.0104  28986.0 +- 0.0

Random dropout accuracy score 0.8597 +- 0.0084
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8662 +- 0.0067
Feature importance dropout (0.5% features dropped) accuracy score 0.8532 +- 0.009
Feature importance dropout (1.0% features dropped) accuracy score 0.835 +- 0.0124
Feature importance dropout (2.0% features dropped) accuracy score 0.777 +- 0.0221
