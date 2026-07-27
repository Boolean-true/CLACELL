--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.915 +- 0.0051

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0   0.9917 +- 0.0   0.9958 +- 0.0    120.0 +- 0.0
          CD14+ monocyte 0.9914 +- 0.0022 0.9997 +- 0.0005 0.9955 +- 0.0012   2575.0 +- 0.0
             CD4+ T cell 0.8709 +- 0.0033 0.9956 +- 0.0007 0.929 +- 0.0022   3910.0 +- 0.0
        Cytotoxic T cell 0.9513 +- 0.0045 0.6138 +- 0.0234  0.746 +- 0.019   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0      0.6 +- 0.0     0.75 +- 0.0      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.8471 +- 0.0261 0.9198 +- 0.0033 0.8818 +- 0.0149    791.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     49.0 +- 0.0

                accuracy                                 0.915 +- 0.0051   9281.0 +- 0.0
               macro avg 0.9576 +- 0.0041 0.8901 +- 0.0032 0.9123 +- 0.0045   9281.0 +- 0.0
            weighted avg 0.9206 +- 0.0044 0.915 +- 0.0051 0.9087 +- 0.0059   9281.0 +- 0.0

Random dropout accuracy score 0.9093 +- 0.0054
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9139 +- 0.0046
Feature importance dropout (0.5% features dropped) accuracy score 0.8555 +- 0.0015
Feature importance dropout (1.0% features dropped) accuracy score 0.8379 +- 0.0007
Feature importance dropout (2.0% features dropped) accuracy score 0.8081 +- 0.0067
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.869 +- 0.0029

                               precision          recall        f1-score         support

                  B cell 0.9991 +- 0.0003 0.9961 +- 0.0022 0.9976 +- 0.001   3959.0 +- 0.0
          CD14+ monocyte  0.8775 +- 0.02 0.9989 +- 0.0004 0.9342 +- 0.0111   3135.0 +- 0.0
             CD4+ T cell 0.9463 +- 0.0019 0.9835 +- 0.0012 0.9646 +- 0.001  13664.0 +- 0.0
        Cytotoxic T cell 0.6098 +- 0.0022  0.8238 +- 0.01 0.7008 +- 0.0042   4839.0 +- 0.0
          Dendritic cell 0.9852 +- 0.0031 0.6875 +- 0.0349 0.8094 +- 0.0222    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.5942 +- 0.0066 0.7454 +- 0.0052     86.0 +- 0.0
     Natural killer cell 0.8765 +- 0.0144 0.0917 +- 0.0124 0.1658 +- 0.0202   2751.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     23.0 +- 0.0

                accuracy                                 0.869 +- 0.0029  28986.0 +- 0.0
               macro avg 0.9118 +- 0.0042 0.772 +- 0.0061 0.7897 +- 0.0058  28986.0 +- 0.0
            weighted avg 0.8842 +- 0.0043 0.869 +- 0.0029 0.8425 +- 0.0038  28986.0 +- 0.0

Random dropout accuracy score 0.8642 +- 0.0051
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8688 +- 0.0031
Feature importance dropout (0.5% features dropped) accuracy score 0.8465 +- 0.0054
Feature importance dropout (1.0% features dropped) accuracy score 0.8343 +- 0.0069
Feature importance dropout (2.0% features dropped) accuracy score 0.7554 +- 0.0239
