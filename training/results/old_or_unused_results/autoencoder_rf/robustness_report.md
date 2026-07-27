--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.8908 +- 0.0169

                               precision          recall        f1-score         support

                  B cell 0.9892 +- 0.0077 0.9883 +- 0.009 0.9887 +- 0.0044    120.0 +- 0.0
          CD14+ monocyte 0.9974 +- 0.0007 0.9991 +- 0.0005 0.9983 +- 0.0005   2575.0 +- 0.0
             CD4+ T cell 0.8836 +- 0.0164 0.9924 +- 0.001 0.9348 +- 0.009   3910.0 +- 0.0
        Cytotoxic T cell 0.9502 +- 0.0062 0.4944 +- 0.092 0.6455 +- 0.0827   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0  0.26 +- 0.0966 0.4048 +- 0.115      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.635 +- 0.0806 0.9368 +- 0.0191 0.7536 +- 0.0524    791.0 +- 0.0
             Plasma cell 0.9848 +- 0.0105 0.9184 +- 0.0236 0.9503 +- 0.0137     49.0 +- 0.0

                accuracy                                 0.8908 +- 0.0169   9281.0 +- 0.0
               macro avg  0.93 +- 0.0093 0.8237 +- 0.0142 0.8345 +- 0.0208   9281.0 +- 0.0
            weighted avg 0.9091 +- 0.0086 0.8908 +- 0.0169 0.8807 +- 0.0214   9281.0 +- 0.0

Random dropout accuracy score 0.8803 +- 0.0159
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8862 +- 0.0166
Feature importance dropout (0.5% features dropped) accuracy score 0.8688 +- 0.0162
Feature importance dropout (1.0% features dropped) accuracy score 0.8582 +- 0.0135
Feature importance dropout (2.0% features dropped) accuracy score 0.8272 +- 0.0131
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8716 +- 0.0059

                               precision          recall        f1-score         support

                  B cell 0.9991 +- 0.0003 0.9918 +- 0.0041 0.9954 +- 0.0021   3959.0 +- 0.0
          CD14+ monocyte 0.9089 +- 0.0198 0.9995 +- 0.0003 0.952 +- 0.0109   3135.0 +- 0.0
             CD4+ T cell 0.891 +- 0.0158 0.9942 +- 0.0028 0.9397 +- 0.0079  13664.0 +- 0.0
        Cytotoxic T cell 0.6835 +- 0.0478 0.5915 +- 0.0906 0.6276 +- 0.0417   4839.0 +- 0.0
          Dendritic cell 0.9955 +- 0.0027 0.6541 +- 0.0636 0.7878 +- 0.0457    529.0 +- 0.0
           Megakaryocyte 0.9981 +- 0.006 0.6163 +- 0.0226 0.7618 +- 0.0177     86.0 +- 0.0
     Natural killer cell 0.8039 +- 0.0459 0.4855 +- 0.1567 0.5881 +- 0.1095   2751.0 +- 0.0
             Plasma cell 0.8128 +- 0.0875  0.9652 +- 0.04  0.88 +- 0.0566     23.0 +- 0.0

                accuracy                                 0.8716 +- 0.0059  28986.0 +- 0.0
               macro avg 0.8866 +- 0.0117 0.7873 +- 0.0145 0.8165 +- 0.018  28986.0 +- 0.0
            weighted avg 0.8669 +- 0.0063 0.8716 +- 0.0059 0.8598 +- 0.0076  28986.0 +- 0.0

Random dropout accuracy score 0.8594 +- 0.0072
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8696 +- 0.0056
Feature importance dropout (0.5% features dropped) accuracy score 0.8491 +- 0.0056
Feature importance dropout (1.0% features dropped) accuracy score 0.8278 +- 0.0094
Feature importance dropout (2.0% features dropped) accuracy score 0.7506 +- 0.0329
