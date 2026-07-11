--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9141 +- 0.0139

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0 0.9875 +- 0.0044 0.9937 +- 0.0022    120.0 +- 0.0
          CD14+ monocyte 0.9949 +- 0.0029 0.9997 +- 0.0006 0.9973 +- 0.0016   2575.0 +- 0.0
             CD4+ T cell 0.8691 +- 0.0156 0.9965 +- 0.0003 0.9284 +- 0.0089   3910.0 +- 0.0
        Cytotoxic T cell 0.9794 +- 0.0037 0.5871 +- 0.0702 0.7319 +- 0.0576   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0  0.52 +- 0.1033 0.6786 +- 0.0922      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.8177 +- 0.0413 0.9694 +- 0.0024 0.8866 +- 0.0246    791.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9735 +- 0.0138 0.9865 +- 0.0072     49.0 +- 0.0

                accuracy                                 0.9141 +- 0.0139   9281.0 +- 0.0
               macro avg 0.9576 +- 0.0073 0.8792 +- 0.0151 0.9004 +- 0.0147   9281.0 +- 0.0
            weighted avg 0.9238 +- 0.0107 0.9141 +- 0.0139 0.9064 +- 0.0172   9281.0 +- 0.0

Random dropout accuracy score 0.907 +- 0.0157
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9107 +- 0.0126
Feature importance dropout (0.5% features dropped) accuracy score 0.8357 +- 0.0131
Feature importance dropout (1.0% features dropped) accuracy score 0.7789 +- 0.0143
Feature importance dropout (2.0% features dropped) accuracy score 0.7153 +- 0.0382
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8764 +- 0.003

                               precision          recall        f1-score         support

                  B cell 0.9989 +- 0.0003 0.9994 +- 0.0002 0.9992 +- 0.0002   3959.0 +- 0.0
          CD14+ monocyte 0.9038 +- 0.0077   0.9994 +- 0.0 0.9492 +- 0.0042   3135.0 +- 0.0
             CD4+ T cell 0.9487 +- 0.0025 0.9874 +- 0.0005 0.9676 +- 0.0013  13664.0 +- 0.0
        Cytotoxic T cell 0.6215 +- 0.0099 0.8392 +- 0.0146 0.714 +- 0.0027   4839.0 +- 0.0
          Dendritic cell 0.9873 +- 0.0021 0.5994 +- 0.0724 0.7435 +- 0.0629    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.5826 +- 0.0066 0.7362 +- 0.0053     86.0 +- 0.0
     Natural killer cell 0.925 +- 0.0288 0.1348 +- 0.0429 0.2325 +- 0.0639   2751.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     23.0 +- 0.0

                accuracy                                 0.8764 +- 0.003  28986.0 +- 0.0
               macro avg 0.9231 +- 0.0033 0.7678 +- 0.0125 0.7928 +- 0.0152  28986.0 +- 0.0
            weighted avg 0.8947 +- 0.0029 0.8764 +- 0.003 0.8531 +- 0.0067  28986.0 +- 0.0

Random dropout accuracy score 0.8725 +- 0.0029
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8765 +- 0.0033
Feature importance dropout (0.5% features dropped) accuracy score 0.8465 +- 0.0064
Feature importance dropout (1.0% features dropped) accuracy score 0.7982 +- 0.0305
Feature importance dropout (2.0% features dropped) accuracy score 0.6718 +- 0.0689
