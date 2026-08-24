--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.6866 +- 0.0

                               precision          recall        f1-score         support

          CD14+ Monocyte   0.9974 +- 0.0   0.9847 +- 0.0    0.991 +- 0.0   3458.0 +- 0.0
          CD16+ Monocyte   0.9275 +- 0.0   0.9781 +- 0.0   0.9521 +- 0.0    183.0 +- 0.0
    CD1C+ dendritic cell   0.7115 +- 0.0   0.9569 +- 0.0   0.8162 +- 0.0    116.0 +- 0.0
       CD4 Memory T cell   0.0076 +- 0.0   0.0161 +- 0.0   0.0103 +- 0.0    248.0 +- 0.0
        CD4 Naive T cell   0.4237 +- 0.0   0.5986 +- 0.0   0.4962 +- 0.0   3251.0 +- 0.0
       CD8 Memory T cell   0.9176 +- 0.0   0.5452 +- 0.0    0.684 +- 0.0   4026.0 +- 0.0
        CD8 Naive T cell   0.5505 +- 0.0   0.8742 +- 0.0   0.6756 +- 0.0   1908.0 +- 0.0
      Gamma-delta T cell    0.307 +- 0.0   0.5546 +- 0.0   0.3952 +- 0.0    119.0 +- 0.0
                    MAIT   0.6267 +- 0.0   0.9865 +- 0.0   0.7665 +- 0.0    519.0 +- 0.0
           Memory B cell   0.9112 +- 0.0   0.9006 +- 0.0   0.9059 +- 0.0    946.0 +- 0.0
                 NK cell   0.8392 +- 0.0   0.4225 +- 0.0    0.562 +- 0.0   5399.0 +- 0.0
            Naive B cell   0.9567 +- 0.0   0.9624 +- 0.0   0.9596 +- 0.0   2182.0 +- 0.0
             Plasma cell   0.9464 +- 0.0   0.9815 +- 0.0   0.9636 +- 0.0     54.0 +- 0.0
Plasmacytoid dendritic cell   0.9412 +- 0.0      1.0 +- 0.0   0.9697 +- 0.0     32.0 +- 0.0
       T regulatory cell   0.0085 +- 0.0      1.0 +- 0.0   0.0169 +- 0.0     10.0 +- 0.0

                accuracy                                   0.6866 +- 0.0  22451.0 +- 0.0
               macro avg   0.6715 +- 0.0   0.7841 +- 0.0   0.6776 +- 0.0  22451.0 +- 0.0
            weighted avg   0.7906 +- 0.0   0.6866 +- 0.0   0.7068 +- 0.0  22451.0 +- 0.0

10% Random Dropout accuracy: 0.6816 +- 0.0048
50% Random Dropout accuracy: 0.6473 +- 0.0076
90% Random Dropout accuracy: 0.4645 +- 0.0121
92.5% Random Dropout accuracy: 0.4212 +- 0.0182
95% Random Dropout accuracy: 0.3594 +- 0.016
Total samples: 22451.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.6866 +- 0.0
Feature importance dropout (0.5% features dropped) accuracy score 0.6838 +- 0.0
Feature importance dropout (1.0% features dropped) accuracy score 0.679 +- 0.0
Feature importance dropout (2.0% features dropped) accuracy score 0.67 +- 0.0
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.6906 +- 0.0

                               precision          recall        f1-score         support

          CD14+ Monocyte   0.9926 +- 0.0   0.9845 +- 0.0   0.9885 +- 0.0  12317.0 +- 0.0
          CD16+ Monocyte   0.9798 +- 0.0   0.9685 +- 0.0   0.9741 +- 0.0   1903.0 +- 0.0
    CD1C+ dendritic cell   0.8416 +- 0.0    0.975 +- 0.0   0.9034 +- 0.0   1079.0 +- 0.0
       CD4 Memory T cell   0.2381 +- 0.0   0.0007 +- 0.0   0.0014 +- 0.0  14241.0 +- 0.0
        CD4 Naive T cell   0.6133 +- 0.0   0.7997 +- 0.0   0.6942 +- 0.0  17151.0 +- 0.0
       CD8 Memory T cell   0.4417 +- 0.0   0.6208 +- 0.0   0.5161 +- 0.0   6650.0 +- 0.0
        CD8 Naive T cell   0.6613 +- 0.0   0.9817 +- 0.0   0.7902 +- 0.0   6516.0 +- 0.0
      Gamma-delta T cell   0.0168 +- 0.0   0.0026 +- 0.0   0.0046 +- 0.0   2271.0 +- 0.0
                    MAIT   0.4957 +- 0.0   0.9941 +- 0.0   0.6615 +- 0.0   2889.0 +- 0.0
           Memory B cell   0.9534 +- 0.0   0.7771 +- 0.0   0.8562 +- 0.0   1395.0 +- 0.0
                 NK cell   0.7033 +- 0.0   0.9451 +- 0.0   0.8065 +- 0.0   5959.0 +- 0.0
            Naive B cell   0.9141 +- 0.0   0.9876 +- 0.0   0.9494 +- 0.0   3385.0 +- 0.0
             Plasma cell   0.9924 +- 0.0   0.9871 +- 0.0   0.9898 +- 0.0    930.0 +- 0.0
Plasmacytoid dendritic cell   0.9915 +- 0.0   0.9983 +- 0.0   0.9949 +- 0.0    584.0 +- 0.0
       T regulatory cell   0.4815 +- 0.0   0.4899 +- 0.0   0.4857 +- 0.0   1731.0 +- 0.0

                accuracy                                   0.6906 +- 0.0  79001.0 +- 0.0
               macro avg   0.6878 +- 0.0   0.7675 +- 0.0   0.7078 +- 0.0  79001.0 +- 0.0
            weighted avg   0.6148 +- 0.0   0.6906 +- 0.0   0.6201 +- 0.0  79001.0 +- 0.0

10% Random Dropout accuracy: 0.6841 +- 0.0027
50% Random Dropout accuracy: 0.6481 +- 0.0074
90% Random Dropout accuracy: 0.4167 +- 0.0145
92.5% Random Dropout accuracy: 0.3687 +- 0.0203
95% Random Dropout accuracy: 0.3175 +- 0.0136
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.6906 +- 0.0
Feature importance dropout (0.5% features dropped) accuracy score 0.6897 +- 0.0
Feature importance dropout (1.0% features dropped) accuracy score 0.6875 +- 0.0
Feature importance dropout (2.0% features dropped) accuracy score 0.6872 +- 0.0
