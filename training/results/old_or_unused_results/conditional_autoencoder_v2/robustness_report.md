--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9067 +- 0.0111

                               precision          recall        f1-score         support

                  B cell 0.9916 +- 0.0078 0.9808 +- 0.0088 0.9862 +- 0.0059    120.0 +- 0.0
          CD14+ monocyte 0.9984 +- 0.001 0.9986 +- 0.0007 0.9985 +- 0.0007   2575.0 +- 0.0
             CD4+ T cell 0.9106 +- 0.0163 0.9955 +- 0.0014 0.9511 +- 0.0087   3910.0 +- 0.0
        Cytotoxic T cell 0.8334 +- 0.0271  0.6828 +- 0.05 0.7498 +- 0.0355   1824.0 +- 0.0
          Dendritic cell 0.9667 +- 0.1054  0.44 +- 0.1578 0.5901 +- 0.1457      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.9857 +- 0.0452 0.9923 +- 0.0243      7.0 +- 0.0
     Natural killer cell 0.7019 +- 0.0492 0.6731 +- 0.0552 0.6866 +- 0.0482    791.0 +- 0.0
             Plasma cell 0.9735 +- 0.0267 0.949 +- 0.0173 0.9608 +- 0.0148     49.0 +- 0.0

                accuracy                                 0.9067 +- 0.0111   9281.0 +- 0.0
               macro avg  0.922 +- 0.021 0.8382 +- 0.0264 0.8644 +- 0.0255   9281.0 +- 0.0
            weighted avg 0.9035 +- 0.0118 0.9067 +- 0.0111 0.9025 +- 0.0123   9281.0 +- 0.0

Random dropout accuracy score 0.8938 +- 0.0125
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9039 +- 0.0111
Feature importance dropout (0.5% features dropped) accuracy score 0.882 +- 0.0095
Feature importance dropout (1.0% features dropped) accuracy score 0.8509 +- 0.0111
Feature importance dropout (2.0% features dropped) accuracy score 0.8037 +- 0.0127
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8646 +- 0.0051

                               precision          recall        f1-score         support

                  B cell 0.9993 +- 0.0002 0.9884 +- 0.0051 0.9938 +- 0.0026   3959.0 +- 0.0
          CD14+ monocyte 0.8634 +- 0.0324 0.9991 +- 0.0005  0.926 +- 0.019   3135.0 +- 0.0
             CD4+ T cell 0.925 +- 0.0077 0.9832 +- 0.007 0.9531 +- 0.0038  13664.0 +- 0.0
        Cytotoxic T cell 0.6259 +- 0.0111 0.7267 +- 0.0372 0.672 +- 0.0158   4839.0 +- 0.0
          Dendritic cell 0.9886 +- 0.0039 0.6359 +- 0.0595 0.7725 +- 0.0438    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0  0.643 +- 0.029 0.7824 +- 0.0221     86.0 +- 0.0
     Natural killer cell 0.7617 +- 0.0562 0.2374 +- 0.0548 0.3573 +- 0.0642   2751.0 +- 0.0
             Plasma cell 0.819 +- 0.1531 0.9609 +- 0.0478 0.8771 +- 0.0973     23.0 +- 0.0

                accuracy                                 0.8646 +- 0.0051  28986.0 +- 0.0
               macro avg 0.8729 +- 0.0232 0.7718 +- 0.0122 0.7918 +- 0.0143  28986.0 +- 0.0
            weighted avg 0.8644 +- 0.0086 0.8646 +- 0.0051 0.8484 +- 0.007  28986.0 +- 0.0

Random dropout accuracy score 0.8532 +- 0.0096
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8628 +- 0.0057
Feature importance dropout (0.5% features dropped) accuracy score 0.8447 +- 0.008
Feature importance dropout (1.0% features dropped) accuracy score 0.8231 +- 0.012
Feature importance dropout (2.0% features dropped) accuracy score 0.7552 +- 0.0283
