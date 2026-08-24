--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.7805 +- 0.0008

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9908 +- 0.0005 0.9975 +- 0.0005 0.9941 +- 0.0004   3458.0 +- 0.0
          CD16+ Monocyte 0.9821 +- 0.004 0.8973 +- 0.0081 0.9377 +- 0.0055    183.0 +- 0.0
    CD1C+ dendritic cell 0.9569 +- 0.0124   0.8966 +- 0.0 0.9257 +- 0.0058    116.0 +- 0.0
       CD4 Memory T cell 0.0036 +- 0.0006 0.023 +- 0.0043 0.0062 +- 0.0011    248.0 +- 0.0
        CD4 Naive T cell 0.6686 +- 0.0045 0.9076 +- 0.0024  0.77 +- 0.0035   3251.0 +- 0.0
       CD8 Memory T cell 0.7626 +- 0.0041 0.8719 +- 0.0025 0.8136 +- 0.0021   4026.0 +- 0.0
        CD8 Naive T cell 0.8811 +- 0.0026 0.9026 +- 0.0048 0.8917 +- 0.0024   1908.0 +- 0.0
      Gamma-delta T cell 0.8575 +- 0.0111 0.6571 +- 0.0087 0.7441 +- 0.0092    119.0 +- 0.0
                    MAIT 0.8512 +- 0.0042 0.8597 +- 0.0036 0.8554 +- 0.0034    519.0 +- 0.0
           Memory B cell 0.894 +- 0.0015 0.9364 +- 0.0031 0.9147 +- 0.0021    946.0 +- 0.0
                 NK cell 0.9489 +- 0.0016 0.3753 +- 0.0024 0.5378 +- 0.0025   5399.0 +- 0.0
            Naive B cell 0.972 +- 0.0012 0.9592 +- 0.0007 0.9655 +- 0.0008   2182.0 +- 0.0
             Plasma cell      1.0 +- 0.0    0.963 +- 0.0   0.9811 +- 0.0     54.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0   0.9688 +- 0.0   0.9841 +- 0.0     32.0 +- 0.0
       T regulatory cell 0.0331 +- 0.0006      0.5 +- 0.0 0.0621 +- 0.0011     10.0 +- 0.0

                accuracy                                 0.7805 +- 0.0008  22451.0 +- 0.0
               macro avg 0.7868 +- 0.0015 0.7811 +- 0.0009 0.7589 +- 0.0011  22451.0 +- 0.0
            weighted avg 0.8624 +- 0.0015 0.7805 +- 0.0008 0.788 +- 0.0009  22451.0 +- 0.0

10% Random Dropout accuracy: 0.7721 +- 0.0031
50% Random Dropout accuracy: 0.6798 +- 0.0108
90% Random Dropout accuracy: 0.2608 +- 0.0214
92.5% Random Dropout accuracy: 0.2204 +- 0.0244
95% Random Dropout accuracy: 0.1936 +- 0.0172
Total samples: 22451.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.7805 +- 0.0008
Feature importance dropout (0.5% features dropped) accuracy score 0.7804 +- 0.0008
Feature importance dropout (1.0% features dropped) accuracy score 0.7776 +- 0.0008
Feature importance dropout (2.0% features dropped) accuracy score 0.7688 +- 0.0012
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.7132 +- 0.0019

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9562 +- 0.0028 0.9962 +- 0.0002 0.9758 +- 0.0014  12317.0 +- 0.0
          CD16+ Monocyte   0.9981 +- 0.0 0.841 +- 0.0088 0.9128 +- 0.0052   1903.0 +- 0.0
    CD1C+ dendritic cell 0.9502 +- 0.0028 0.8517 +- 0.0043 0.8982 +- 0.0018   1079.0 +- 0.0
       CD4 Memory T cell   0.1 +- 0.3162      0.0 +- 0.0   0.0 +- 0.0001  14241.0 +- 0.0
        CD4 Naive T cell 0.7769 +- 0.0132 0.9339 +- 0.0067 0.8481 +- 0.0053  17151.0 +- 0.0
       CD8 Memory T cell 0.3035 +- 0.0073 0.9478 +- 0.0043 0.4597 +- 0.0079   6650.0 +- 0.0
        CD8 Naive T cell 0.9407 +- 0.0025 0.8607 +- 0.0049 0.8989 +- 0.0031   6516.0 +- 0.0
      Gamma-delta T cell 0.0136 +- 0.002 0.0036 +- 0.0005 0.0057 +- 0.0008   2271.0 +- 0.0
                    MAIT 0.7616 +- 0.0046 0.9393 +- 0.0041 0.8412 +- 0.0023   2889.0 +- 0.0
           Memory B cell 0.9221 +- 0.0029 0.7251 +- 0.0094 0.8118 +- 0.0053   1395.0 +- 0.0
                 NK cell 0.8777 +- 0.0025 0.8449 +- 0.0039 0.861 +- 0.0019   5959.0 +- 0.0
            Naive B cell 0.8962 +- 0.0031 0.9876 +- 0.0007 0.9397 +- 0.0014   3385.0 +- 0.0
             Plasma cell 0.9997 +- 0.0005 0.9831 +- 0.0009 0.9913 +- 0.0003    930.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.987 +- 0.0018 0.9934 +- 0.0009    584.0 +- 0.0
       T regulatory cell 0.9737 +- 0.0231 0.0121 +- 0.0024 0.0238 +- 0.0047   1731.0 +- 0.0

                accuracy                                 0.7132 +- 0.0019  79001.0 +- 0.0
               macro avg 0.7647 +- 0.0207 0.7276 +- 0.0021 0.6974 +- 0.0013  79001.0 +- 0.0
            weighted avg 0.6655 +- 0.057 0.7132 +- 0.0019 0.6533 +- 0.0008  79001.0 +- 0.0

10% Random Dropout accuracy: 0.704 +- 0.0025
50% Random Dropout accuracy: 0.6064 +- 0.0127
90% Random Dropout accuracy: 0.2846 +- 0.0209
92.5% Random Dropout accuracy: 0.2578 +- 0.0156
95% Random Dropout accuracy: 0.2366 +- 0.0085
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.7132 +- 0.0019
Feature importance dropout (0.5% features dropped) accuracy score 0.715 +- 0.0016
Feature importance dropout (1.0% features dropped) accuracy score 0.7066 +- 0.0023
Feature importance dropout (2.0% features dropped) accuracy score 0.6992 +- 0.0026
