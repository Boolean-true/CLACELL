--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.8968 +- 0.0142

                               precision          recall        f1-score         support

                  B cell   0.985 +- 0.01 0.9817 +- 0.0077 0.9833 +- 0.0068    120.0 +- 0.0
          CD14+ monocyte 0.9974 +- 0.0013 0.9979 +- 0.0011 0.9976 +- 0.001   2575.0 +- 0.0
             CD4+ T cell 0.8644 +- 0.0271 0.9962 +- 0.0008 0.9254 +- 0.0153   3910.0 +- 0.0
        Cytotoxic T cell 0.915 +- 0.0208 0.5524 +- 0.0799 0.6855 +- 0.0597   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0  0.52 +- 0.1033 0.6786 +- 0.0922      5.0 +- 0.0
           Megakaryocyte 0.9875 +- 0.0395      1.0 +- 0.0 0.9933 +- 0.0211      7.0 +- 0.0
     Natural killer cell 0.7491 +- 0.0696 0.8561 +- 0.0466 0.7956 +- 0.0298    791.0 +- 0.0
             Plasma cell 0.9653 +- 0.0209 0.951 +- 0.0172 0.9579 +- 0.0112     49.0 +- 0.0

                accuracy                                 0.8968 +- 0.0142   9281.0 +- 0.0
               macro avg 0.933 +- 0.0115 0.8569 +- 0.017 0.8772 +- 0.0157   9281.0 +- 0.0
            weighted avg 0.9037 +- 0.0113 0.8968 +- 0.0142 0.8881 +- 0.0175   9281.0 +- 0.0

Random dropout accuracy score 0.8822 +- 0.014
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.893 +- 0.0143
Feature importance dropout (0.5% features dropped) accuracy score 0.8696 +- 0.0147
Feature importance dropout (1.0% features dropped) accuracy score 0.838 +- 0.0134
Feature importance dropout (2.0% features dropped) accuracy score 0.7996 +- 0.0081
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8634 +- 0.0098

                               precision          recall        f1-score         support

                  B cell 0.9989 +- 0.0005 0.9918 +- 0.0029 0.9953 +- 0.0014   3959.0 +- 0.0
          CD14+ monocyte 0.8894 +- 0.036 0.9976 +- 0.0042  0.94 +- 0.0202   3135.0 +- 0.0
             CD4+ T cell 0.9162 +- 0.0149 0.9876 +- 0.0071 0.9505 +- 0.0081  13664.0 +- 0.0
        Cytotoxic T cell 0.6161 +- 0.0204 0.7324 +- 0.0424 0.6687 +- 0.0242   4839.0 +- 0.0
          Dendritic cell 0.9868 +- 0.0062 0.6418 +- 0.0726 0.7756 +- 0.0522    529.0 +- 0.0
           Megakaryocyte 0.995 +- 0.0158 0.6372 +- 0.0204 0.7766 +- 0.0138     86.0 +- 0.0
     Natural killer cell 0.8475 +- 0.0414 0.1883 +- 0.073 0.3013 +- 0.0927   2751.0 +- 0.0
             Plasma cell 0.8201 +- 0.1809 0.9957 +- 0.0137 0.8889 +- 0.1104     23.0 +- 0.0

                accuracy                                 0.8634 +- 0.0098  28986.0 +- 0.0
               macro avg 0.8837 +- 0.0206 0.7715 +- 0.0149 0.7871 +- 0.019  28986.0 +- 0.0
            weighted avg 0.8694 +- 0.0084 0.8634 +- 0.0098 0.8431 +- 0.0139  28986.0 +- 0.0

Random dropout accuracy score 0.8539 +- 0.0118
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8624 +- 0.0097
Feature importance dropout (0.5% features dropped) accuracy score 0.8468 +- 0.0101
Feature importance dropout (1.0% features dropped) accuracy score 0.8238 +- 0.0143
Feature importance dropout (2.0% features dropped) accuracy score 0.767 +- 0.0231
