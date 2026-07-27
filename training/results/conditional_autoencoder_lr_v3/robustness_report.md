--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9139 +- 0.0084

                               precision          recall        f1-score         support

                  B cell  0.99 +- 0.0075 0.9858 +- 0.0056 0.9879 +- 0.0036    120.0 +- 0.0
          CD14+ monocyte 0.9976 +- 0.0006 0.9982 +- 0.0008 0.9979 +- 0.0004   2575.0 +- 0.0
             CD4+ T cell 0.9204 +- 0.0147 0.9941 +- 0.0007 0.9558 +- 0.008   3910.0 +- 0.0
        Cytotoxic T cell 0.8527 +- 0.0146 0.7035 +- 0.0505  0.77 +- 0.0302   1824.0 +- 0.0
          Dendritic cell  0.95 +- 0.1581      0.4 +- 0.0 0.5587 +- 0.0402      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.7145 +- 0.0517 0.7182 +- 0.0371 0.7148 +- 0.0281    791.0 +- 0.0
             Plasma cell 0.9813 +- 0.0202 0.9347 +- 0.0211 0.9571 +- 0.0105     49.0 +- 0.0

                accuracy                                 0.9139 +- 0.0084   9281.0 +- 0.0
               macro avg 0.9258 +- 0.0179 0.8418 +- 0.0066 0.8678 +- 0.0056   9281.0 +- 0.0
            weighted avg 0.9123 +- 0.0078 0.9139 +- 0.0084 0.9107 +- 0.0092   9281.0 +- 0.0

Random dropout accuracy score 0.9036 +- 0.0096
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9118 +- 0.0093
Feature importance dropout (0.5% features dropped) accuracy score 0.8932 +- 0.0104
Feature importance dropout (1.0% features dropped) accuracy score 0.87 +- 0.0108
Feature importance dropout (2.0% features dropped) accuracy score 0.827 +- 0.0122
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.871 +- 0.0032

                               precision          recall        f1-score         support

                  B cell 0.9992 +- 0.0002 0.9893 +- 0.004 0.9942 +- 0.0021   3959.0 +- 0.0
          CD14+ monocyte 0.8934 +- 0.0201 0.9995 +- 0.0003 0.9434 +- 0.0112   3135.0 +- 0.0
             CD4+ T cell 0.9313 +- 0.0117 0.9876 +- 0.0047 0.9586 +- 0.0047  13664.0 +- 0.0
        Cytotoxic T cell 0.6278 +- 0.016 0.7639 +- 0.0489 0.688 +- 0.0155   4839.0 +- 0.0
          Dendritic cell 0.9898 +- 0.0024 0.6437 +- 0.0387 0.7795 +- 0.0291    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.6256 +- 0.0273 0.7694 +- 0.0209     86.0 +- 0.0
     Natural killer cell 0.8047 +- 0.0358 0.2142 +- 0.0771 0.3312 +- 0.0845   2751.0 +- 0.0
             Plasma cell 0.7477 +- 0.128 0.9652 +- 0.0572 0.8342 +- 0.0667     23.0 +- 0.0

                accuracy                                 0.871 +- 0.0032  28986.0 +- 0.0
               macro avg 0.8743 +- 0.0171 0.7736 +- 0.0096 0.7873 +- 0.0123  28986.0 +- 0.0
            weighted avg 0.8749 +- 0.0059 0.871 +- 0.0032 0.8532 +- 0.0053  28986.0 +- 0.0

Random dropout accuracy score 0.8618 +- 0.0056
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8703 +- 0.0032
Feature importance dropout (0.5% features dropped) accuracy score 0.8553 +- 0.0058
Feature importance dropout (1.0% features dropped) accuracy score 0.8374 +- 0.0085
Feature importance dropout (2.0% features dropped) accuracy score 0.7627 +- 0.0235
