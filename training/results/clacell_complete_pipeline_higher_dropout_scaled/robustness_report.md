--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.8059 +- 0.0073

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0 0.155 +- 0.0264 0.2676 +- 0.0394    120.0 +- 0.0
          CD14+ monocyte 0.9946 +- 0.0012 0.9996 +- 0.0004 0.9971 +- 0.0006   2575.0 +- 0.0
             CD4+ T cell 0.7275 +- 0.0149 0.9969 +- 0.0008 0.8411 +- 0.0097   3910.0 +- 0.0
        Cytotoxic T cell 0.9889 +- 0.0044 0.119 +- 0.0369 0.2107 +- 0.0587   1824.0 +- 0.0
          Dendritic cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.8714 +- 0.2177 0.9137 +- 0.1692      7.0 +- 0.0
     Natural killer cell 0.7048 +- 0.0423 0.9631 +- 0.0095 0.8132 +- 0.0279    791.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.0959 +- 0.0237 0.1743 +- 0.0386     49.0 +- 0.0

                accuracy                                 0.8059 +- 0.0073   9281.0 +- 0.0
               macro avg 0.802 +- 0.0041 0.5251 +- 0.0241 0.5272 +- 0.0177   9281.0 +- 0.0
            weighted avg 0.8558 +- 0.0046 0.8059 +- 0.0073 0.7468 +- 0.0141   9281.0 +- 0.0

10% Random Dropout accuracy: 0.8084 +- 0.0078
50% Random Dropout accuracy: 0.7902 +- 0.0234
90% Random Dropout accuracy: 0.4176 +- 0.2034
92.5% Random Dropout accuracy: 0.3027 +- 0.2217
95% Random Dropout accuracy: 0.217 +- 0.1755
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8058 +- 0.0066
Feature importance dropout (0.5% features dropped) accuracy score 0.7819 +- 0.0032
Feature importance dropout (1.0% features dropped) accuracy score 0.7586 +- 0.0051
Feature importance dropout (2.0% features dropped) accuracy score 0.7603 +- 0.0084
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8692 +- 0.0033

                               precision          recall        f1-score         support

                  B cell 0.9989 +- 0.0001 0.9774 +- 0.0062 0.988 +- 0.0032   3959.0 +- 0.0
          CD14+ monocyte 0.9489 +- 0.0029 0.9981 +- 0.0004 0.9729 +- 0.0015   3135.0 +- 0.0
             CD4+ T cell 0.9343 +- 0.007 0.9915 +- 0.0017  0.962 +- 0.003  13664.0 +- 0.0
        Cytotoxic T cell 0.6017 +- 0.0052 0.8208 +- 0.0195 0.6943 +- 0.0095   4839.0 +- 0.0
          Dendritic cell 0.9807 +- 0.0022 0.7577 +- 0.0188 0.8547 +- 0.0118    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.5558 +- 0.0049 0.7145 +- 0.0041     86.0 +- 0.0
     Natural killer cell 0.9155 +- 0.0148 0.0746 +- 0.0154 0.1375 +- 0.0262   2751.0 +- 0.0
             Plasma cell 0.7349 +- 0.058      1.0 +- 0.0 0.846 +- 0.0408     23.0 +- 0.0

                accuracy                                 0.8692 +- 0.0033  28986.0 +- 0.0
               macro avg 0.8894 +- 0.0078 0.772 +- 0.0043 0.7712 +- 0.0051  28986.0 +- 0.0
            weighted avg 0.8883 +- 0.004 0.8692 +- 0.0033 0.841 +- 0.0042  28986.0 +- 0.0

10% Random Dropout accuracy: 0.8599 +- 0.0088
50% Random Dropout accuracy: 0.7851 +- 0.0222
90% Random Dropout accuracy: 0.3122 +- 0.1402
92.5% Random Dropout accuracy: 0.2867 +- 0.1409
95% Random Dropout accuracy: 0.2101 +- 0.1575
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8703 +- 0.0034
Feature importance dropout (0.5% features dropped) accuracy score 0.7521 +- 0.0152
Feature importance dropout (1.0% features dropped) accuracy score 0.716 +- 0.0153
Feature importance dropout (2.0% features dropped) accuracy score 0.6729 +- 0.0124
