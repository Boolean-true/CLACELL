--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9042 +- 0.0096

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0  0.99 +- 0.0035 0.995 +- 0.0018    120.0 +- 0.0
          CD14+ monocyte 0.9926 +- 0.0042 0.9988 +- 0.0004 0.9957 +- 0.0022   2575.0 +- 0.0
             CD4+ T cell 0.8542 +- 0.0097 0.9964 +- 0.0005 0.9198 +- 0.0056   3910.0 +- 0.0
        Cytotoxic T cell 0.9732 +- 0.0059 0.5433 +- 0.0471 0.6962 +- 0.0403   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0  0.52 +- 0.1033 0.6786 +- 0.0922      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.8104 +- 0.0268 0.956 +- 0.0071 0.877 +- 0.0176    791.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9857 +- 0.0255 0.9927 +- 0.0133     49.0 +- 0.0

                accuracy                                 0.9042 +- 0.0096   9281.0 +- 0.0
               macro avg 0.9538 +- 0.0053 0.8738 +- 0.0129 0.8944 +- 0.011   9281.0 +- 0.0
            weighted avg 0.9151 +- 0.0077 0.9042 +- 0.0096 0.8946 +- 0.0121   9281.0 +- 0.0

Random dropout accuracy score 0.8961 +- 0.0086
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.902 +- 0.0083
Feature importance dropout (0.5% features dropped) accuracy score 0.8455 +- 0.0096
Feature importance dropout (1.0% features dropped) accuracy score 0.8224 +- 0.0106
Feature importance dropout (2.0% features dropped) accuracy score 0.7926 +- 0.0146
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8684 +- 0.0068

                               precision          recall        f1-score         support

                  B cell 0.9992 +- 0.0001 0.9979 +- 0.0009 0.9985 +- 0.0005   3959.0 +- 0.0
          CD14+ monocyte 0.8535 +- 0.0232 0.9993 +- 0.0002 0.9205 +- 0.0136   3135.0 +- 0.0
             CD4+ T cell 0.9345 +- 0.0082 0.988 +- 0.0028 0.9605 +- 0.0034  13664.0 +- 0.0
        Cytotoxic T cell 0.6245 +- 0.0172 0.7739 +- 0.0366 0.6905 +- 0.0122   4839.0 +- 0.0
          Dendritic cell 0.987 +- 0.0016 0.5718 +- 0.1627 0.7075 +- 0.178    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.5907 +- 0.0049 0.7427 +- 0.0039     86.0 +- 0.0
     Natural killer cell 0.8956 +- 0.0326 0.1691 +- 0.0698 0.2778 +- 0.0948   2751.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9957 +- 0.0137 0.9978 +- 0.007     23.0 +- 0.0

                accuracy                                 0.8684 +- 0.0068  28986.0 +- 0.0
               macro avg 0.9118 +- 0.0042 0.7608 +- 0.0282 0.787 +- 0.0337  28986.0 +- 0.0
            weighted avg 0.8804 +- 0.0058 0.8684 +- 0.0068 0.8463 +- 0.0123  28986.0 +- 0.0

Random dropout accuracy score 0.8611 +- 0.0093
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8674 +- 0.0069
Feature importance dropout (0.5% features dropped) accuracy score 0.8392 +- 0.0104
Feature importance dropout (1.0% features dropped) accuracy score 0.817 +- 0.02
Feature importance dropout (2.0% features dropped) accuracy score 0.7233 +- 0.065
