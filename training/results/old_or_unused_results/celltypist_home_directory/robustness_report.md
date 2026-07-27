--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.8019 +- 0.0166

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0 0.9458 +- 0.0264  0.972 +- 0.014    120.0 +- 0.0
          CD14+ monocyte 0.9936 +- 0.0067 0.9991 +- 0.001 0.9963 +- 0.0031   2575.0 +- 0.0
             CD4+ T cell 0.6959 +- 0.0308 0.9991 +- 0.0007  0.82 +- 0.0212   3910.0 +- 0.0
        Cytotoxic T cell 0.9947 +- 0.006 0.076 +- 0.0257 0.1402 +- 0.0438   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0      0.2 +- 0.0   0.3333 +- 0.0      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.7714 +- 0.1205 0.866 +- 0.0818      7.0 +- 0.0
     Natural killer cell 0.8832 +- 0.0839 0.841 +- 0.1531 0.8472 +- 0.0671    791.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.8163 +- 0.0319 0.8986 +- 0.0195     49.0 +- 0.0

                accuracy                                 0.8019 +- 0.0166   9281.0 +- 0.0
               macro avg 0.9459 +- 0.0073 0.7061 +- 0.0203 0.7342 +- 0.0135   9281.0 +- 0.0
            weighted avg 0.8591 +- 0.0055 0.8019 +- 0.0166 0.7398 +- 0.0194   9281.0 +- 0.0

Random dropout accuracy score 0.7815 +- 0.0217
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.7993 +- 0.0168
Feature importance dropout (0.5% features dropped) accuracy score 0.7675 +- 0.0282
Feature importance dropout (1.0% features dropped) accuracy score 0.7485 +- 0.0314
Feature importance dropout (2.0% features dropped) accuracy score 0.7169 +- 0.0211
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.7604 +- 0.0341

                               precision          recall        f1-score         support

                  B cell 0.9998 +- 0.0002 0.6479 +- 0.0841 0.7835 +- 0.0601   3959.0 +- 0.0
          CD14+ monocyte 0.6707 +- 0.1331 0.9996 +- 0.0006 0.796 +- 0.0943   3135.0 +- 0.0
             CD4+ T cell 0.7541 +- 0.0728 0.9994 +- 0.0001 0.8578 +- 0.0477  13664.0 +- 0.0
        Cytotoxic T cell 0.7534 +- 0.0322 0.2693 +- 0.0629 0.3927 +- 0.0692   4839.0 +- 0.0
          Dendritic cell 0.9992 +- 0.0025 0.0958 +- 0.0666 0.1691 +- 0.1056    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0   0.45 +- 0.057 0.6187 +- 0.0549     86.0 +- 0.0
     Natural killer cell  0.8775 +- 0.03 0.4677 +- 0.1947 0.5843 +- 0.1678   2751.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.3043 +- 0.0458 0.465 +- 0.0542     23.0 +- 0.0

                accuracy                                 0.7604 +- 0.0341  28986.0 +- 0.0
               macro avg 0.8818 +- 0.0108 0.5293 +- 0.0351 0.5834 +- 0.0337  28986.0 +- 0.0
            weighted avg 0.7956 +- 0.0226 0.7604 +- 0.0341 0.7238 +- 0.0454  28986.0 +- 0.0

Random dropout accuracy score 0.6962 +- 0.0338
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.7487 +- 0.0361
Feature importance dropout (0.5% features dropped) accuracy score 0.6393 +- 0.0324
Feature importance dropout (1.0% features dropped) accuracy score 0.606 +- 0.0217
Feature importance dropout (2.0% features dropped) accuracy score 0.5777 +- 0.0105
