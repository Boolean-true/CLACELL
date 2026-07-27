--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9295 +- 0.0108

                               precision          recall        f1-score         support

                  B cell 0.9659 +- 0.0095 0.9883 +- 0.0098 0.9769 +- 0.0065    120.0 +- 0.0
          CD14+ monocyte 0.9962 +- 0.0013 0.9985 +- 0.001 0.9973 +- 0.0007   2575.0 +- 0.0
             CD4+ T cell 0.9668 +- 0.0134 0.9836 +- 0.0034 0.975 +- 0.0057   3910.0 +- 0.0
        Cytotoxic T cell 0.8754 +- 0.0311 0.794 +- 0.0799 0.8296 +- 0.0387   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0  0.36 +- 0.0843 0.5238 +- 0.1004      5.0 +- 0.0
           Megakaryocyte 0.975 +- 0.0527      1.0 +- 0.0 0.9867 +- 0.0281      7.0 +- 0.0
     Natural killer cell 0.6753 +- 0.0623 0.7465 +- 0.0763 0.7045 +- 0.0353    791.0 +- 0.0
             Plasma cell 0.9916 +- 0.0145 0.8959 +- 0.0378 0.9407 +- 0.017     49.0 +- 0.0

                accuracy                                 0.9295 +- 0.0108   9281.0 +- 0.0
               macro avg 0.9308 +- 0.0112 0.8459 +- 0.017 0.8668 +- 0.0182   9281.0 +- 0.0
            weighted avg 0.9323 +- 0.007 0.9295 +- 0.0108 0.9292 +- 0.0109   9281.0 +- 0.0

Random dropout accuracy score 0.9258 +- 0.0135
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.927 +- 0.0123
Feature importance dropout (0.5% features dropped) accuracy score 0.9144 +- 0.0152
Feature importance dropout (1.0% features dropped) accuracy score 0.9044 +- 0.0192
Feature importance dropout (2.0% features dropped) accuracy score 0.8794 +- 0.0234
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8815 +- 0.0109

                               precision          recall        f1-score         support

                  B cell 0.9988 +- 0.0008 0.9786 +- 0.0144 0.9886 +- 0.0075   3959.0 +- 0.0
          CD14+ monocyte 0.9127 +- 0.0112 0.9989 +- 0.0006 0.9538 +- 0.0061   3135.0 +- 0.0
             CD4+ T cell 0.9332 +- 0.0162 0.9839 +- 0.008 0.9578 +- 0.0058  13664.0 +- 0.0
        Cytotoxic T cell 0.6738 +- 0.054 0.7455 +- 0.0652 0.7039 +- 0.0243   4839.0 +- 0.0
          Dendritic cell 0.9922 +- 0.0034 0.7193 +- 0.0309 0.8336 +- 0.0208    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.6256 +- 0.0244 0.7694 +- 0.0184     86.0 +- 0.0
     Natural killer cell 0.7476 +- 0.054 0.3778 +- 0.1735 0.4805 +- 0.1637   2751.0 +- 0.0
             Plasma cell  0.78 +- 0.1611  0.9043 +- 0.17 0.8129 +- 0.1075     23.0 +- 0.0

                accuracy                                 0.8815 +- 0.0109  28986.0 +- 0.0
               macro avg  0.8798 +- 0.02 0.7917 +- 0.024 0.8126 +- 0.0158  28986.0 +- 0.0
            weighted avg 0.8802 +- 0.0103 0.8815 +- 0.0109 0.8709 +- 0.0166  28986.0 +- 0.0

Random dropout accuracy score 0.8751 +- 0.0116
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8795 +- 0.0108
Feature importance dropout (0.5% features dropped) accuracy score 0.8572 +- 0.0138
Feature importance dropout (1.0% features dropped) accuracy score 0.8367 +- 0.0212
Feature importance dropout (2.0% features dropped) accuracy score 0.7601 +- 0.0347
