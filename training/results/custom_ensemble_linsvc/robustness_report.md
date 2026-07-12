--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9331 +- 0.0061

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0   0.9917 +- 0.0   0.9958 +- 0.0    120.0 +- 0.0
          CD14+ monocyte 0.9949 +- 0.0018 0.9995 +- 0.0004 0.9972 +- 0.001   2575.0 +- 0.0
             CD4+ T cell 0.9058 +- 0.0068 0.9951 +- 0.0001 0.9483 +- 0.0038   3910.0 +- 0.0
        Cytotoxic T cell 0.9263 +- 0.0017 0.7302 +- 0.0335 0.8162 +- 0.0216   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0      0.6 +- 0.0     0.75 +- 0.0      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.8778 +- 0.0276 0.8673 +- 0.0083 0.8721 +- 0.0107    791.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     49.0 +- 0.0

                accuracy                                 0.9331 +- 0.0061   9281.0 +- 0.0
               macro avg 0.9631 +- 0.0042 0.898 +- 0.0033 0.9225 +- 0.0046   9281.0 +- 0.0
            weighted avg 0.934 +- 0.0052 0.9331 +- 0.0061 0.9302 +- 0.0069   9281.0 +- 0.0

Random dropout accuracy score 0.9272 +- 0.0093
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9334 +- 0.0064
Feature importance dropout (0.5% features dropped) accuracy score 0.8827 +- 0.0043
Feature importance dropout (1.0% features dropped) accuracy score 0.8604 +- 0.0028
Feature importance dropout (2.0% features dropped) accuracy score 0.8233 +- 0.0036
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8689 +- 0.0017

                               precision          recall        f1-score         support

                  B cell 0.9989 +- 0.0002 0.9966 +- 0.0015 0.9978 +- 0.0009   3959.0 +- 0.0
          CD14+ monocyte 0.8768 +- 0.0163 0.9993 +- 0.0003 0.934 +- 0.0092   3135.0 +- 0.0
             CD4+ T cell 0.9575 +- 0.0014 0.9772 +- 0.0032 0.9672 +- 0.0016  13664.0 +- 0.0
        Cytotoxic T cell 0.605 +- 0.0016 0.8653 +- 0.0073 0.7121 +- 0.0017   4839.0 +- 0.0
          Dendritic cell 0.9872 +- 0.0009 0.6093 +- 0.0426 0.7527 +- 0.0305    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.5779 +- 0.0056 0.7325 +- 0.0045     86.0 +- 0.0
     Natural killer cell 0.8803 +- 0.0072 0.0628 +- 0.0158 0.1168 +- 0.0268   2751.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     23.0 +- 0.0

                accuracy                                 0.8689 +- 0.0017  28986.0 +- 0.0
               macro avg 0.9132 +- 0.0024 0.761 +- 0.0064 0.7766 +- 0.0068  28986.0 +- 0.0
            weighted avg 0.889 +- 0.0024 0.8689 +- 0.0017 0.8399 +- 0.003  28986.0 +- 0.0

Random dropout accuracy score 0.8646 +- 0.0044
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8684 +- 0.0017
Feature importance dropout (0.5% features dropped) accuracy score 0.8485 +- 0.0024
Feature importance dropout (1.0% features dropped) accuracy score 0.8378 +- 0.0024
Feature importance dropout (2.0% features dropped) accuracy score 0.7674 +- 0.0105
