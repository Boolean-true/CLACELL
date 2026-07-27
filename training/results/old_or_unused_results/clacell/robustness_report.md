--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9114 +- 0.0112

                               precision          recall        f1-score         support

                  B cell 0.9206 +- 0.0486 0.9358 +- 0.0125 0.9275 +- 0.0246    120.0 +- 0.0
          CD14+ monocyte 0.9944 +- 0.0024 0.9993 +- 0.0007 0.9968 +- 0.0012   2575.0 +- 0.0
             CD4+ T cell 0.8828 +- 0.0194 0.9941 +- 0.0011 0.935 +- 0.0107   3910.0 +- 0.0
        Cytotoxic T cell 0.9797 +- 0.0054 0.6055 +- 0.0584 0.747 +- 0.0432   1824.0 +- 0.0
          Dendritic cell 0.3167 +- 0.3885  0.18 +- 0.1989 0.2253 +- 0.2586      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.751 +- 0.0405 0.9611 +- 0.0093 0.8425 +- 0.0233    791.0 +- 0.0
             Plasma cell    0.7 +- 0.483 0.2816 +- 0.4101 0.3168 +- 0.4272     49.0 +- 0.0

                accuracy                                 0.9114 +- 0.0112   9281.0 +- 0.0
               macro avg 0.8181 +- 0.1012 0.7447 +- 0.0726 0.7489 +- 0.0856   9281.0 +- 0.0
            weighted avg 0.9209 +- 0.0085 0.9114 +- 0.0112 0.9036 +- 0.0136   9281.0 +- 0.0

Random dropout accuracy score 0.894 +- 0.009
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9162 +- 0.0103
Feature importance dropout (0.5% features dropped) accuracy score 0.8181 +- 0.0171
Feature importance dropout (1.0% features dropped) accuracy score 0.7849 +- 0.0226
Feature importance dropout (2.0% features dropped) accuracy score 0.7445 +- 0.0207
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8589 +- 0.0068

                               precision          recall        f1-score         support

                  B cell 0.9975 +- 0.0008 0.9819 +- 0.0129 0.9896 +- 0.0067   3959.0 +- 0.0
          CD14+ monocyte 0.8471 +- 0.0232   1.0 +- 0.0001 0.9171 +- 0.0131   3135.0 +- 0.0
             CD4+ T cell 0.9421 +- 0.0093 0.9854 +- 0.0028 0.9633 +- 0.0039  13664.0 +- 0.0
        Cytotoxic T cell 0.6057 +- 0.0144 0.8441 +- 0.0203 0.7051 +- 0.0113   4839.0 +- 0.0
          Dendritic cell 0.2845 +- 0.4093  0.0563 +- 0.15 0.0792 +- 0.1976    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.5395 +- 0.0166 0.7008 +- 0.014     86.0 +- 0.0
     Natural killer cell 0.9434 +- 0.0262 0.0877 +- 0.057 0.1558 +- 0.0899   2751.0 +- 0.0
             Plasma cell    0.5 +- 0.527   0.3 +- 0.4117 0.3388 +- 0.4333     23.0 +- 0.0

                accuracy                                 0.8589 +- 0.0068  28986.0 +- 0.0
               macro avg 0.765 +- 0.1111 0.5994 +- 0.067 0.6062 +- 0.0757  28986.0 +- 0.0
            weighted avg 0.8712 +- 0.0121 0.8589 +- 0.0068 0.8247 +- 0.0123  28986.0 +- 0.0

Random dropout accuracy score 0.8489 +- 0.0073
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8599 +- 0.0055
Feature importance dropout (0.5% features dropped) accuracy score 0.7072 +- 0.0142
Feature importance dropout (1.0% features dropped) accuracy score 0.6706 +- 0.0277
Feature importance dropout (2.0% features dropped) accuracy score 0.5912 +- 0.014
