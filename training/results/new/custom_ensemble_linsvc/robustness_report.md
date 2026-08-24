--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.7848 +- 0.0008

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9911 +- 0.0002 0.9988 +- 0.0003 0.9949 +- 0.0002   3458.0 +- 0.0
          CD16+ Monocyte 0.9877 +- 0.0018 0.9186 +- 0.0017 0.9519 +- 0.0013    183.0 +- 0.0
    CD1C+ dendritic cell 0.9862 +- 0.0067 0.8612 +- 0.0027 0.9195 +- 0.003    116.0 +- 0.0
       CD4 Memory T cell 0.0033 +- 0.0004 0.0137 +- 0.0021 0.0053 +- 0.0007    248.0 +- 0.0
        CD4 Naive T cell 0.6224 +- 0.0047 0.9111 +- 0.0015 0.7396 +- 0.0034   3251.0 +- 0.0
       CD8 Memory T cell 0.7315 +- 0.0035 0.8941 +- 0.0014 0.8046 +- 0.0025   4026.0 +- 0.0
        CD8 Naive T cell 0.8783 +- 0.0023 0.8939 +- 0.0027 0.886 +- 0.0022   1908.0 +- 0.0
      Gamma-delta T cell  0.86 +- 0.0108 0.6958 +- 0.0077 0.7692 +- 0.0055    119.0 +- 0.0
                    MAIT 0.8589 +- 0.0071 0.878 +- 0.0027 0.8683 +- 0.0032    519.0 +- 0.0
           Memory B cell 0.899 +- 0.0019 0.9291 +- 0.0042 0.9138 +- 0.0021    946.0 +- 0.0
                 NK cell 0.9684 +- 0.0017 0.3755 +- 0.0028 0.5412 +- 0.003   5399.0 +- 0.0
            Naive B cell 0.969 +- 0.0018 0.9598 +- 0.001 0.9643 +- 0.0008   2182.0 +- 0.0
             Plasma cell   0.9811 +- 0.0    0.963 +- 0.0    0.972 +- 0.0     54.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0   0.9688 +- 0.0   0.9841 +- 0.0     32.0 +- 0.0
       T regulatory cell 0.0459 +- 0.004  0.47 +- 0.0483 0.0836 +- 0.0073     10.0 +- 0.0

                accuracy                                 0.7848 +- 0.0008  22451.0 +- 0.0
               macro avg 0.7855 +- 0.0012 0.7821 +- 0.0035 0.7599 +- 0.001  22451.0 +- 0.0
            weighted avg 0.8549 +- 0.001 0.7848 +- 0.0008 0.7828 +- 0.001  22451.0 +- 0.0

10% Random Dropout accuracy: 0.7761 +- 0.0027
50% Random Dropout accuracy: 0.7045 +- 0.0118
90% Random Dropout accuracy: 0.4193 +- 0.0263
92.5% Random Dropout accuracy: 0.3785 +- 0.0215
95% Random Dropout accuracy: 0.3157 +- 0.0175
Total samples: 22451.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.7848 +- 0.0008
Feature importance dropout (0.5% features dropped) accuracy score 0.7846 +- 0.0006
Feature importance dropout (1.0% features dropped) accuracy score 0.7795 +- 0.0011
Feature importance dropout (2.0% features dropped) accuracy score 0.7677 +- 0.0011
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.716 +- 0.0012

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9522 +- 0.0015 0.9983 +- 0.0002 0.9747 +- 0.0007  12317.0 +- 0.0
          CD16+ Monocyte 0.9957 +- 0.0008 0.8208 +- 0.0062 0.8998 +- 0.0038   1903.0 +- 0.0
    CD1C+ dendritic cell 0.9762 +- 0.0025 0.8221 +- 0.0045 0.8925 +- 0.0017   1079.0 +- 0.0
       CD4 Memory T cell 0.6098 +- 0.0392 0.0087 +- 0.0031 0.0172 +- 0.006  14241.0 +- 0.0
        CD4 Naive T cell 0.8012 +- 0.0098 0.9141 +- 0.0032 0.8539 +- 0.0045  17151.0 +- 0.0
       CD8 Memory T cell 0.3006 +- 0.0058 0.9179 +- 0.0076 0.4528 +- 0.0058   6650.0 +- 0.0
        CD8 Naive T cell 0.8898 +- 0.0075 0.9273 +- 0.0057 0.9082 +- 0.0032   6516.0 +- 0.0
      Gamma-delta T cell 0.0162 +- 0.0017 0.0044 +- 0.0005 0.0069 +- 0.0008   2271.0 +- 0.0
                    MAIT 0.6915 +- 0.0069 0.9641 +- 0.0038 0.8053 +- 0.0036   2889.0 +- 0.0
           Memory B cell 0.9305 +- 0.0032 0.7434 +- 0.0076 0.8264 +- 0.0057   1395.0 +- 0.0
                 NK cell 0.9025 +- 0.006 0.8615 +- 0.0037 0.8815 +- 0.0018   5959.0 +- 0.0
            Naive B cell 0.9022 +- 0.0026 0.9862 +- 0.0004 0.9423 +- 0.0014   3385.0 +- 0.0
             Plasma cell   0.9989 +- 0.0 0.9881 +- 0.0003 0.9935 +- 0.0002    930.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.9908 +- 0.0014 0.9954 +- 0.0007    584.0 +- 0.0
       T regulatory cell 0.7839 +- 0.0165 0.0396 +- 0.0067 0.0753 +- 0.0121   1731.0 +- 0.0

                accuracy                                 0.716 +- 0.0012  79001.0 +- 0.0
               macro avg 0.7834 +- 0.0013 0.7325 +- 0.001 0.7017 +- 0.0008  79001.0 +- 0.0
            weighted avg 0.7536 +- 0.0047 0.716 +- 0.0012 0.6591 +- 0.0009  79001.0 +- 0.0

10% Random Dropout accuracy: 0.71 +- 0.0023
50% Random Dropout accuracy: 0.6481 +- 0.0051
90% Random Dropout accuracy: 0.418 +- 0.0154
92.5% Random Dropout accuracy: 0.3807 +- 0.0203
95% Random Dropout accuracy: 0.3292 +- 0.0177
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.716 +- 0.0012
Feature importance dropout (0.5% features dropped) accuracy score 0.7174 +- 0.0013
Feature importance dropout (1.0% features dropped) accuracy score 0.7104 +- 0.0017
Feature importance dropout (2.0% features dropped) accuracy score 0.7034 +- 0.0018
