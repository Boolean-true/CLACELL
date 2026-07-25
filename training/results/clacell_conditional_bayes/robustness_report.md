--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9105 +- 0.0079

                               precision          recall        f1-score         support

                  B cell 0.9908 +- 0.0026 0.985 +- 0.0066 0.9879 +- 0.0037    120.0 +- 0.0
          CD14+ monocyte 0.9967 +- 0.0016 0.9984 +- 0.0006 0.9976 +- 0.001   2575.0 +- 0.0
             CD4+ T cell 0.9104 +- 0.0123 0.9946 +- 0.001 0.9506 +- 0.0064   3910.0 +- 0.0
        Cytotoxic T cell 0.8473 +- 0.0249 0.6923 +- 0.0428 0.7611 +- 0.027   1824.0 +- 0.0
          Dendritic cell 0.975 +- 0.0791   0.5 +- 0.1054 0.6524 +- 0.0889      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.7321 +- 0.0585 0.6996 +- 0.0627 0.7131 +- 0.0433    791.0 +- 0.0
             Plasma cell 0.971 +- 0.0141 0.9531 +- 0.0168 0.9619 +- 0.0129     49.0 +- 0.0

                accuracy                                 0.9105 +- 0.0079   9281.0 +- 0.0
               macro avg 0.9279 +- 0.0157 0.8529 +- 0.0152 0.8781 +- 0.0147   9281.0 +- 0.0
            weighted avg 0.9082 +- 0.0083 0.9105 +- 0.0079 0.9066 +- 0.0086   9281.0 +- 0.0

Random dropout accuracy score 0.8993 +- 0.0088
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9084 +- 0.0078
Feature importance dropout (0.5% features dropped) accuracy score 0.8887 +- 0.009
Feature importance dropout (1.0% features dropped) accuracy score 0.8631 +- 0.0099
Feature importance dropout (2.0% features dropped) accuracy score 0.819 +- 0.0089
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8688 +- 0.0057

                               precision          recall        f1-score         support

                  B cell 0.999 +- 0.0002 0.9937 +- 0.0022 0.9963 +- 0.0011   3959.0 +- 0.0
          CD14+ monocyte 0.8862 +- 0.0229 0.9995 +- 0.0002 0.9393 +- 0.013   3135.0 +- 0.0
             CD4+ T cell 0.9304 +- 0.0114 0.9869 +- 0.0077 0.9577 +- 0.0043  13664.0 +- 0.0
        Cytotoxic T cell 0.6226 +- 0.0134 0.7662 +- 0.0501 0.6862 +- 0.0206   4839.0 +- 0.0
          Dendritic cell 0.9882 +- 0.008 0.5879 +- 0.042 0.7363 +- 0.0329    529.0 +- 0.0
           Megakaryocyte 0.9982 +- 0.0057 0.6547 +- 0.0165 0.7906 +- 0.0131     86.0 +- 0.0
     Natural killer cell 0.8347 +- 0.0503 0.1943 +- 0.0706 0.3079 +- 0.0917   2751.0 +- 0.0
             Plasma cell 0.7482 +- 0.1391 0.9783 +- 0.0307 0.842 +- 0.0892     23.0 +- 0.0

                accuracy                                 0.8688 +- 0.0057  28986.0 +- 0.0
               macro avg 0.8759 +- 0.0217 0.7702 +- 0.0112 0.7821 +- 0.0218  28986.0 +- 0.0
            weighted avg 0.8756 +- 0.0089 0.8688 +- 0.0057 0.8494 +- 0.0091  28986.0 +- 0.0

Random dropout accuracy score 0.862 +- 0.0074
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8681 +- 0.0059
Feature importance dropout (0.5% features dropped) accuracy score 0.857 +- 0.0057
Feature importance dropout (1.0% features dropped) accuracy score 0.8419 +- 0.0084
Feature importance dropout (2.0% features dropped) accuracy score 0.7855 +- 0.0265
