--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9156 +- 0.0057

                               precision          recall        f1-score         support

                  B cell 0.995 +- 0.0058 0.9842 +- 0.0061 0.9895 +- 0.0045    120.0 +- 0.0
          CD14+ monocyte 0.9971 +- 0.0014 0.9984 +- 0.0005 0.9977 +- 0.0006   2575.0 +- 0.0
             CD4+ T cell 0.9205 +- 0.0063 0.9936 +- 0.0015 0.9557 +- 0.0034   3910.0 +- 0.0
        Cytotoxic T cell 0.8592 +- 0.0192 0.7116 +- 0.0464 0.7772 +- 0.024   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0  0.46 +- 0.0966 0.625 +- 0.0863      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.7266 +- 0.0608  0.72 +- 0.0524 0.7197 +- 0.0194    791.0 +- 0.0
             Plasma cell 0.9702 +- 0.0208 0.9653 +- 0.0289 0.9672 +- 0.007     49.0 +- 0.0

                accuracy                                 0.9156 +- 0.0057   9281.0 +- 0.0
               macro avg 0.9336 +- 0.0075 0.8541 +- 0.0118 0.879 +- 0.0108   9281.0 +- 0.0
            weighted avg 0.9145 +- 0.0034 0.9156 +- 0.0057 0.9125 +- 0.006   9281.0 +- 0.0

Random dropout accuracy score 0.9058 +- 0.0062
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9132 +- 0.0067
Feature importance dropout (0.5% features dropped) accuracy score 0.8937 +- 0.0081
Feature importance dropout (1.0% features dropped) accuracy score 0.8696 +- 0.0095
Feature importance dropout (2.0% features dropped) accuracy score 0.8262 +- 0.0133
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8725 +- 0.0039

                               precision          recall        f1-score         support

                  B cell 0.9992 +- 0.0003 0.9939 +- 0.0026 0.9965 +- 0.0014   3959.0 +- 0.0
          CD14+ monocyte 0.8872 +- 0.0178 0.9995 +- 0.0002 0.9399 +- 0.0101   3135.0 +- 0.0
             CD4+ T cell 0.9342 +- 0.0054 0.9888 +- 0.0019 0.9607 +- 0.0026  13664.0 +- 0.0
        Cytotoxic T cell 0.6302 +- 0.0152 0.7712 +- 0.0285 0.6931 +- 0.0076   4839.0 +- 0.0
          Dendritic cell 0.9858 +- 0.0045 0.6017 +- 0.061 0.7457 +- 0.0486    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.6593 +- 0.031 0.7943 +- 0.0224     86.0 +- 0.0
     Natural killer cell 0.8168 +- 0.0325 0.2117 +- 0.0672 0.3311 +- 0.0872   2751.0 +- 0.0
             Plasma cell 0.7588 +- 0.1522 0.9913 +- 0.0183 0.8521 +- 0.0945     23.0 +- 0.0

                accuracy                                 0.8725 +- 0.0039  28986.0 +- 0.0
               macro avg 0.8765 +- 0.0157 0.7772 +- 0.0123 0.7892 +- 0.0135  28986.0 +- 0.0
            weighted avg 0.8771 +- 0.0047 0.8725 +- 0.0039 0.8544 +- 0.0076  28986.0 +- 0.0

Random dropout accuracy score 0.8656 +- 0.0048
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8719 +- 0.0037
Feature importance dropout (0.5% features dropped) accuracy score 0.8593 +- 0.0037
Feature importance dropout (1.0% features dropped) accuracy score 0.8431 +- 0.0061
Feature importance dropout (2.0% features dropped) accuracy score 0.7847 +- 0.0152
