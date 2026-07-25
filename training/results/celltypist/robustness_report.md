--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.8108 +- 0.0128

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0 0.9575 +- 0.0323 0.978 +- 0.0169    120.0 +- 0.0
          CD14+ monocyte 0.9933 +- 0.0071 0.9995 +- 0.0004 0.9964 +- 0.0036   2575.0 +- 0.0
             CD4+ T cell 0.711 +- 0.0267 0.9991 +- 0.0005 0.8305 +- 0.018   3910.0 +- 0.0
        Cytotoxic T cell 0.996 +- 0.0044 0.0852 +- 0.0367 0.1551 +- 0.0615   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0      0.2 +- 0.0   0.3333 +- 0.0      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.7429 +- 0.1313 0.8467 +- 0.0847      7.0 +- 0.0
     Natural killer cell 0.8474 +- 0.0787 0.9202 +- 0.0702 0.8769 +- 0.0243    791.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.8306 +- 0.0334 0.9071 +- 0.0199     49.0 +- 0.0

                accuracy                                 0.8108 +- 0.0128   9281.0 +- 0.0
               macro avg 0.9435 +- 0.0062 0.7169 +- 0.0239 0.7405 +- 0.0149   9281.0 +- 0.0
            weighted avg 0.8626 +- 0.0055 0.8108 +- 0.0128 0.7498 +- 0.0188   9281.0 +- 0.0

Random dropout accuracy score 0.7928 +- 0.0166
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8085 +- 0.012
Feature importance dropout (0.5% features dropped) accuracy score 0.7841 +- 0.0185
Feature importance dropout (1.0% features dropped) accuracy score 0.7666 +- 0.0229
Feature importance dropout (2.0% features dropped) accuracy score 0.73 +- 0.0217
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.7747 +- 0.0527

                               precision          recall        f1-score         support

                  B cell 0.9997 +- 0.0004 0.6862 +- 0.1562  0.8046 +- 0.11   3959.0 +- 0.0
          CD14+ monocyte 0.6267 +- 0.1486   1.0 +- 0.0001 0.7608 +- 0.1186   3135.0 +- 0.0
             CD4+ T cell 0.7902 +- 0.0455 0.9994 +- 0.0001 0.8819 +- 0.0289  13664.0 +- 0.0
        Cytotoxic T cell 0.7703 +- 0.0182 0.2714 +- 0.0881 0.3935 +- 0.0946   4839.0 +- 0.0
          Dendritic cell      1.0 +- 0.0 0.0766 +- 0.0476 0.139 +- 0.0822    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.4593 +- 0.0377 0.6287 +- 0.0344     86.0 +- 0.0
     Natural killer cell 0.8609 +- 0.0318 0.5619 +- 0.1992 0.6566 +- 0.1474   2751.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.3435 +- 0.0993   0.504 +- 0.11     23.0 +- 0.0

                accuracy                                 0.7747 +- 0.0527  28986.0 +- 0.0
               macro avg 0.881 +- 0.0156 0.5498 +- 0.0664 0.5961 +- 0.0747  28986.0 +- 0.0
            weighted avg 0.8092 +- 0.0247 0.7747 +- 0.0527 0.7407 +- 0.0615  28986.0 +- 0.0

Random dropout accuracy score 0.7184 +- 0.0652
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.7656 +- 0.0553
Feature importance dropout (0.5% features dropped) accuracy score 0.6665 +- 0.059
Feature importance dropout (1.0% features dropped) accuracy score 0.6313 +- 0.0457
Feature importance dropout (2.0% features dropped) accuracy score 0.5883 +- 0.0117
