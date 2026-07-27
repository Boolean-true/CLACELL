--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9248 +- 0.0137

                               precision          recall        f1-score         support

                  B cell 0.9715 +- 0.0155 0.9875 +- 0.0148 0.9793 +- 0.0114    120.0 +- 0.0
          CD14+ monocyte 0.997 +- 0.0018 0.9987 +- 0.0007 0.9978 +- 0.0007   2575.0 +- 0.0
             CD4+ T cell 0.9548 +- 0.0157 0.9861 +- 0.0029 0.9701 +- 0.0075   3910.0 +- 0.0
        Cytotoxic T cell 0.8949 +- 0.0339  0.74 +- 0.0811 0.8072 +- 0.0458   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0  0.34 +- 0.0966    0.5 +- 0.115      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.6624 +- 0.0874 0.803 +- 0.0677 0.7218 +- 0.0592    791.0 +- 0.0
             Plasma cell 0.9909 +- 0.0118 0.8939 +- 0.0559 0.9391 +- 0.0329     49.0 +- 0.0

                accuracy                                 0.9248 +- 0.0137   9281.0 +- 0.0
               macro avg 0.9339 +- 0.0118 0.8437 +- 0.0162 0.8644 +- 0.0206   9281.0 +- 0.0
            weighted avg 0.9303 +- 0.0092 0.9248 +- 0.0137 0.9243 +- 0.0135   9281.0 +- 0.0

Random dropout accuracy score 0.9138 +- 0.0184
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9208 +- 0.0153
Feature importance dropout (0.5% features dropped) accuracy score 0.8992 +- 0.022
Feature importance dropout (1.0% features dropped) accuracy score 0.8805 +- 0.0286
Feature importance dropout (2.0% features dropped) accuracy score 0.8508 +- 0.0329
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.883 +- 0.012

                               precision          recall        f1-score         support

                  B cell 0.9988 +- 0.0003 0.9747 +- 0.0195 0.9865 +- 0.0101   3959.0 +- 0.0
          CD14+ monocyte 0.9055 +- 0.0162 0.9974 +- 0.0039 0.9492 +- 0.0087   3135.0 +- 0.0
             CD4+ T cell 0.9226 +- 0.0202 0.9839 +- 0.008 0.9521 +- 0.0085  13664.0 +- 0.0
        Cytotoxic T cell 0.7192 +- 0.0585 0.6692 +- 0.0859 0.6879 +- 0.0416   4839.0 +- 0.0
          Dendritic cell 0.9958 +- 0.0029 0.6905 +- 0.0676 0.8138 +- 0.0475    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.6174 +- 0.0193 0.7633 +- 0.0146     86.0 +- 0.0
     Natural killer cell 0.7189 +- 0.1039 0.5406 +- 0.1482 0.6066 +- 0.1105   2751.0 +- 0.0
             Plasma cell 0.7543 +- 0.0874   0.9217 +- 0.1 0.824 +- 0.0614     23.0 +- 0.0

                accuracy                                  0.883 +- 0.012  28986.0 +- 0.0
               macro avg 0.8769 +- 0.0158 0.7994 +- 0.0222 0.8229 +- 0.0173  28986.0 +- 0.0
            weighted avg 0.8793 +- 0.0145  0.883 +- 0.012 0.8764 +- 0.0135  28986.0 +- 0.0

Random dropout accuracy score 0.8753 +- 0.0146
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8801 +- 0.0125
Feature importance dropout (0.5% features dropped) accuracy score 0.8561 +- 0.0182
Feature importance dropout (1.0% features dropped) accuracy score 0.8305 +- 0.0257
Feature importance dropout (2.0% features dropped) accuracy score 0.7567 +- 0.0373
