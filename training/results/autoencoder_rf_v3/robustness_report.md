--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.861 +- 0.0194

                               precision          recall        f1-score         support

                  B cell 0.9857 +- 0.0079 0.9767 +- 0.0129 0.9811 +- 0.0082    120.0 +- 0.0
          CD14+ monocyte 0.9956 +- 0.0011 0.9983 +- 0.0007 0.997 +- 0.0007   2575.0 +- 0.0
             CD4+ T cell 0.8283 +- 0.0456 0.9928 +- 0.0016 0.9025 +- 0.0268   3910.0 +- 0.0
        Cytotoxic T cell 0.9281 +- 0.0373  0.3618 +- 0.11 0.5111 +- 0.108   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0  0.38 +- 0.0632 0.5476 +- 0.0753      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.6567 +- 0.102 0.8977 +- 0.0739 0.7497 +- 0.0436    791.0 +- 0.0
             Plasma cell 0.9774 +- 0.0186 0.8714 +- 0.0397 0.9209 +- 0.0247     49.0 +- 0.0

                accuracy                                 0.861 +- 0.0194   9281.0 +- 0.0
               macro avg 0.9215 +- 0.0081  0.8098 +- 0.02 0.8262 +- 0.0227   9281.0 +- 0.0
            weighted avg 0.8827 +- 0.0171 0.861 +- 0.0194 0.8398 +- 0.0294   9281.0 +- 0.0

Random dropout accuracy score 0.8478 +- 0.0169
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8568 +- 0.0187
Feature importance dropout (0.5% features dropped) accuracy score 0.8355 +- 0.0149
Feature importance dropout (1.0% features dropped) accuracy score 0.8215 +- 0.0124
Feature importance dropout (2.0% features dropped) accuracy score 0.7968 +- 0.0096
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8457 +- 0.0147

                               precision          recall        f1-score         support

                  B cell 0.9988 +- 0.0004 0.9509 +- 0.0136 0.9742 +- 0.0071   3959.0 +- 0.0
          CD14+ monocyte 0.8912 +- 0.0263 0.9986 +- 0.001 0.9416 +- 0.0144   3135.0 +- 0.0
             CD4+ T cell 0.8478 +- 0.0184 0.997 +- 0.0014 0.9163 +- 0.0107  13664.0 +- 0.0
        Cytotoxic T cell 0.6422 +- 0.0467 0.5001 +- 0.0799 0.5583 +- 0.0546   4839.0 +- 0.0
          Dendritic cell 0.9932 +- 0.0028 0.6293 +- 0.081 0.7676 +- 0.063    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.5907 +- 0.0204 0.7425 +- 0.0161     86.0 +- 0.0
     Natural killer cell 0.8328 +- 0.0356 0.4273 +- 0.153 0.5452 +- 0.1502   2751.0 +- 0.0
             Plasma cell 0.7586 +- 0.1464  0.6783 +- 0.13 0.7012 +- 0.0931     23.0 +- 0.0

                accuracy                                 0.8457 +- 0.0147  28986.0 +- 0.0
               macro avg 0.8706 +- 0.0194 0.7215 +- 0.0288 0.7684 +- 0.0279  28986.0 +- 0.0
            weighted avg 0.8404 +- 0.0144 0.8457 +- 0.0147 0.8286 +- 0.0201  28986.0 +- 0.0

Random dropout accuracy score 0.8243 +- 0.0168
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8423 +- 0.0138
Feature importance dropout (0.5% features dropped) accuracy score 0.7969 +- 0.0176
Feature importance dropout (1.0% features dropped) accuracy score 0.7619 +- 0.0191
Feature importance dropout (2.0% features dropped) accuracy score 0.6743 +- 0.0214
