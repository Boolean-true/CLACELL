# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8216 +- 0.0016

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9849 +- 0.0003 0.9995 +- 0.0001 0.9922 +- 0.0002   3456.0 +- 0.0
          CD16+ Monocyte      1.0 +- 0.0 0.8549 +- 0.0049 0.9218 +- 0.0028    193.0 +- 0.0
    CD1C+ dendritic cell 0.9815 +- 0.0059 0.7843 +- 0.0107 0.8718 +- 0.0076    108.0 +- 0.0
       CD4 Memory T cell 0.8077 +- 0.0075 0.9786 +- 0.0022 0.8849 +- 0.0044   2888.0 +- 0.0
        CD4 Naive T cell 0.8512 +- 0.0029 0.9699 +- 0.001 0.9067 +- 0.0017   3439.0 +- 0.0
       CD8 Memory T cell 0.1447 +- 0.0066 0.4645 +- 0.0275 0.2207 +- 0.0108    818.0 +- 0.0
        CD8 Naive T cell 0.956 +- 0.0034 0.6982 +- 0.0123 0.8069 +- 0.0085   2047.0 +- 0.0
      Gamma-delta T cell 0.9605 +- 0.003 0.3719 +- 0.0077 0.5361 +- 0.0079   2544.0 +- 0.0
                    MAIT 0.8319 +- 0.0061 0.9317 +- 0.0049 0.879 +- 0.0044    974.0 +- 0.0
           Memory B cell 0.9355 +- 0.0034 0.9038 +- 0.0072 0.9194 +- 0.0036    897.0 +- 0.0
                 NK cell 0.9922 +- 0.0009 0.7052 +- 0.0014 0.8244 +- 0.001   2580.0 +- 0.0
            Naive B cell 0.9617 +- 0.0028 0.9754 +- 0.0015 0.9685 +- 0.0013   2227.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9339 +- 0.0121 0.9658 +- 0.0065     56.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.6386 +- 0.0148 0.7794 +- 0.011     57.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    136.0 +- 0.0

                accuracy                                 0.8216 +- 0.0016  22420.0 +- 0.0
               macro avg 0.8272 +- 0.0014 0.7474 +- 0.002 0.7652 +- 0.0015  22420.0 +- 0.0
            weighted avg 0.8896 +- 0.0016 0.8216 +- 0.0016 0.8311 +- 0.0017  22420.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.8086 +- 0.0047
50% Random Dropout Accuracy: 0.6868 +- 0.016
90% Random Dropout Accuracy: 0.1577 +- 0.0053
92.5% Random Dropout Accuracy: 0.1553 +- 0.0022
95% Random Dropout Accuracy: 0.1534 +- 0.0
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.8136 +- 0.0016
Feature importance dropout (0.5% features dropped) Accuracy score 0.7993 +- 0.0018
Feature importance dropout (1.0% features dropped) Accuracy score 0.7788 +- 0.0014
Feature importance dropout (2.0% features dropped) Accuracy score 0.7014 +- 0.0039


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.7477 +- 0.0045
50% Random Dropout Macro_F1: 0.5267 +- 0.0136
90% Random Dropout Macro_F1: 0.0214 +- 0.0046
92.5% Random Dropout Macro_F1: 0.0195 +- 0.0021
95% Random Dropout Macro_F1: 0.0177 +- 0.0
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.7606 +- 0.0016
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.7427 +- 0.0028
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.7196 +- 0.003
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.6162 +- 0.0092



## Out of data distribution 

### Dataset Similarity + Accuracy 

Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.6824 +- 0.0047

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9063 +- 0.0049   0.9997 +- 0.0 0.9507 +- 0.0027  12317.0 +- 0.0
          CD16+ Monocyte 0.9979 +- 0.0003 0.8212 +- 0.0325  0.9007 +- 0.02   1903.0 +- 0.0
    CD1C+ dendritic cell 0.9979 +- 0.0027 0.1867 +- 0.0339 0.3133 +- 0.0481   1079.0 +- 0.0
       CD4 Memory T cell 0.7011 +- 0.0203 0.2679 +- 0.0353 0.3862 +- 0.0346  14241.0 +- 0.0
        CD4 Naive T cell 0.5816 +- 0.0073 0.9348 +- 0.0116 0.717 +- 0.0043  17151.0 +- 0.0
       CD8 Memory T cell 0.3521 +- 0.029 0.1451 +- 0.0195 0.2051 +- 0.0234   6650.0 +- 0.0
        CD8 Naive T cell 0.8751 +- 0.0136 0.8277 +- 0.0194 0.8505 +- 0.0055   6516.0 +- 0.0
      Gamma-delta T cell 0.017 +- 0.0055 0.0269 +- 0.0097 0.0208 +- 0.007   2271.0 +- 0.0
                    MAIT 0.6497 +- 0.035 0.7845 +- 0.0381 0.7093 +- 0.0127   2889.0 +- 0.0
           Memory B cell 0.9438 +- 0.0049 0.4132 +- 0.0251 0.5743 +- 0.024   1395.0 +- 0.0
                 NK cell 0.7034 +- 0.0157 0.9857 +- 0.0033 0.8208 +- 0.0097   5959.0 +- 0.0
            Naive B cell 0.8013 +- 0.0062 0.995 +- 0.0007 0.8877 +- 0.0036   3385.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9754 +- 0.0039 0.9875 +- 0.002    930.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.986 +- 0.0011 0.9929 +- 0.0005    584.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   1731.0 +- 0.0

                accuracy                                 0.6824 +- 0.0047  79001.0 +- 0.0
               macro avg 0.7018 +- 0.0043 0.6233 +- 0.0044 0.6211 +- 0.006  79001.0 +- 0.0
            weighted avg 0.6809 +- 0.0046 0.6824 +- 0.0047 0.6425 +- 0.0082  79001.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.6555 +- 0.0075
50% Random Dropout Accuracy: 0.5343 +- 0.01
90% Random Dropout Accuracy: 0.2204 +- 0.0035
92.5% Random Dropout Accuracy: 0.2181 +- 0.002
95% Random Dropout Accuracy: 0.2171 +- 0.0
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.6833 +- 0.0047
Feature importance dropout (0.5% features dropped) Accuracy score 0.6628 +- 0.0048
Feature importance dropout (1.0% features dropped) Accuracy score 0.6457 +- 0.0054
Feature importance dropout (2.0% features dropped) Accuracy score 0.5231 +- 0.0089


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.5808 +- 0.0107
50% Random Dropout Macro_F1: 0.3597 +- 0.0135
90% Random Dropout Macro_F1: 0.0273 +- 0.003
92.5% Random Dropout Macro_F1: 0.025 +- 0.0018
95% Random Dropout Macro_F1: 0.0238 +- 0.0
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.6246 +- 0.006
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.5768 +- 0.0102
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.5504 +- 0.0117
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.3719 +- 0.018


