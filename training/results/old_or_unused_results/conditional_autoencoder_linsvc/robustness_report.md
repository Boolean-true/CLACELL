--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.8978 +- 0.0083

                               precision          recall        f1-score         support

                  B cell 0.9974 +- 0.0058  0.96 +- 0.0156 0.9783 +- 0.0094    120.0 +- 0.0
          CD14+ monocyte 0.981 +- 0.0049 0.9972 +- 0.0006 0.989 +- 0.0025   2575.0 +- 0.0
             CD4+ T cell 0.8975 +- 0.0175 0.9935 +- 0.0018  0.943 +- 0.009   3910.0 +- 0.0
        Cytotoxic T cell 0.8822 +- 0.0283 0.6002 +- 0.0683 0.7114 +- 0.0377   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0  0.44 +- 0.0843 0.6071 +- 0.0753      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.6723 +- 0.0275 0.777 +- 0.0696 0.7188 +- 0.0321    791.0 +- 0.0
             Plasma cell 0.9979 +- 0.0067 0.951 +- 0.0143 0.9738 +- 0.009     49.0 +- 0.0

                accuracy                                 0.8978 +- 0.0083   9281.0 +- 0.0
               macro avg 0.9285 +- 0.004 0.8399 +- 0.0124 0.8652 +- 0.011   9281.0 +- 0.0
            weighted avg 0.9004 +- 0.0057 0.8978 +- 0.0083 0.8916 +- 0.0099   9281.0 +- 0.0

Random dropout accuracy score 0.8878 +- 0.0087
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8942 +- 0.0087
Feature importance dropout (0.5% features dropped) accuracy score 0.8723 +- 0.0093
Feature importance dropout (1.0% features dropped) accuracy score 0.8474 +- 0.0115
Feature importance dropout (2.0% features dropped) accuracy score 0.8083 +- 0.0152
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8441 +- 0.0166

                               precision          recall        f1-score         support

                  B cell 0.999 +- 0.0005 0.9738 +- 0.0241 0.9861 +- 0.0125   3959.0 +- 0.0
          CD14+ monocyte 0.6972 +- 0.0843 0.9984 +- 0.0009 0.8183 +- 0.0619   3135.0 +- 0.0
             CD4+ T cell 0.9297 +- 0.0163 0.9557 +- 0.0281 0.9421 +- 0.0103  13664.0 +- 0.0
        Cytotoxic T cell 0.6496 +- 0.0126 0.6551 +- 0.072 0.6505 +- 0.0404   4839.0 +- 0.0
          Dendritic cell 0.9868 +- 0.0041 0.5206 +- 0.0818 0.6778 +- 0.0772    529.0 +- 0.0
           Megakaryocyte 0.9786 +- 0.0128 0.7395 +- 0.0191 0.8423 +- 0.0129     86.0 +- 0.0
     Natural killer cell 0.7079 +- 0.0463 0.3237 +- 0.0553 0.4409 +- 0.0503   2751.0 +- 0.0
             Plasma cell 0.9494 +- 0.0561 0.9783 +- 0.0307 0.9622 +- 0.0246     23.0 +- 0.0

                accuracy                                 0.8441 +- 0.0166  28986.0 +- 0.0
               macro avg 0.8623 +- 0.0071 0.7681 +- 0.019  0.79 +- 0.0186  28986.0 +- 0.0
            weighted avg 0.8474 +- 0.0101 0.8441 +- 0.0166 0.8334 +- 0.0151  28986.0 +- 0.0

Random dropout accuracy score 0.8161 +- 0.0245
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8382 +- 0.0192
Feature importance dropout (0.5% features dropped) accuracy score 0.8106 +- 0.0276
Feature importance dropout (1.0% features dropped) accuracy score 0.7681 +- 0.0418
Feature importance dropout (2.0% features dropped) accuracy score 0.6956 +- 0.062
