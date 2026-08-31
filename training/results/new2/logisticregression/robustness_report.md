# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8686 +- 0.0026

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9958 +- 0.0004 0.9953 +- 0.001 0.9956 +- 0.0006   3456.0 +- 0.0
          CD16+ Monocyte 0.9656 +- 0.0041 0.9736 +- 0.0016 0.9696 +- 0.0023    193.0 +- 0.0
    CD1C+ dendritic cell 0.921 +- 0.0217 0.9222 +- 0.0109 0.9215 +- 0.0117    108.0 +- 0.0
       CD4 Memory T cell 0.9342 +- 0.0021 0.7635 +- 0.014 0.8402 +- 0.0084   2888.0 +- 0.0
        CD4 Naive T cell 0.8565 +- 0.0055 0.9006 +- 0.0046 0.878 +- 0.0038   3439.0 +- 0.0
       CD8 Memory T cell 0.3129 +- 0.0076 0.7035 +- 0.0167 0.4331 +- 0.0086    818.0 +- 0.0
        CD8 Naive T cell 0.8957 +- 0.0036 0.8986 +- 0.0072 0.8971 +- 0.0025   2047.0 +- 0.0
      Gamma-delta T cell 0.9633 +- 0.004 0.7915 +- 0.0047 0.869 +- 0.0034   2544.0 +- 0.0
                    MAIT 0.7512 +- 0.0056 0.9017 +- 0.0035 0.8196 +- 0.0024    974.0 +- 0.0
           Memory B cell 0.8843 +- 0.0041 0.9551 +- 0.0021 0.9183 +- 0.0022    897.0 +- 0.0
                 NK cell 0.9823 +- 0.0019 0.7888 +- 0.0136 0.8749 +- 0.0083   2580.0 +- 0.0
            Naive B cell 0.9813 +- 0.0009 0.9494 +- 0.0023 0.9651 +- 0.0011   2227.0 +- 0.0
             Plasma cell 0.9946 +- 0.0087 0.9679 +- 0.0113 0.981 +- 0.0051     56.0 +- 0.0
Plasmacytoid dendritic cell 0.9547 +- 0.0103 0.7421 +- 0.0614 0.834 +- 0.0385     57.0 +- 0.0
       T regulatory cell 0.1476 +- 0.0103 0.2588 +- 0.0285 0.1875 +- 0.0127    136.0 +- 0.0

                accuracy                                 0.8686 +- 0.0026  22420.0 +- 0.0
               macro avg 0.8361 +- 0.0028 0.8342 +- 0.0034 0.8256 +- 0.002  22420.0 +- 0.0
            weighted avg 0.9048 +- 0.0011 0.8686 +- 0.0026 0.8801 +- 0.002  22420.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.8502 +- 0.0072
50% Random Dropout Accuracy: 0.7358 +- 0.0215
90% Random Dropout Accuracy: 0.3785 +- 0.0416
92.5% Random Dropout Accuracy: 0.3154 +- 0.045
95% Random Dropout Accuracy: 0.2782 +- 0.0261
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.8622 +- 0.0028
Feature importance dropout (0.5% features dropped) Accuracy score 0.8234 +- 0.0033
Feature importance dropout (1.0% features dropped) Accuracy score 0.8189 +- 0.0042
Feature importance dropout (2.0% features dropped) Accuracy score 0.6844 +- 0.0118


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.809 +- 0.0051
50% Random Dropout Macro_F1: 0.6941 +- 0.0279
90% Random Dropout Macro_F1: 0.3025 +- 0.0589
92.5% Random Dropout Macro_F1: 0.2396 +- 0.049
95% Random Dropout Macro_F1: 0.1902 +- 0.0296
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.8214 +- 0.0019
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.7923 +- 0.0033
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.7821 +- 0.009
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.6584 +- 0.0354



## Out of data distribution 

### Dataset Similarity + Accuracy 

Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.5278 +- 0.0183

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9688 +- 0.0104 0.9964 +- 0.0022 0.9824 +- 0.0055  12317.0 +- 0.0
          CD16+ Monocyte  0.952 +- 0.049 0.9626 +- 0.0092 0.9565 +- 0.0224   1903.0 +- 0.0
    CD1C+ dendritic cell 0.9562 +- 0.0334 0.8358 +- 0.0489 0.8903 +- 0.0185   1079.0 +- 0.0
       CD4 Memory T cell 0.3112 +- 0.029 0.3392 +- 0.0961 0.3215 +- 0.0619  14241.0 +- 0.0
        CD4 Naive T cell 0.9649 +- 0.0042 0.051 +- 0.0113 0.0967 +- 0.0206  17151.0 +- 0.0
       CD8 Memory T cell 0.0038 +- 0.001 0.0007 +- 0.0003 0.0012 +- 0.0004   6650.0 +- 0.0
        CD8 Naive T cell 0.6716 +- 0.0147 0.9611 +- 0.0057 0.7906 +- 0.0118   6516.0 +- 0.0
      Gamma-delta T cell 0.102 +- 0.0067 0.3244 +- 0.056 0.155 +- 0.0137   2271.0 +- 0.0
                    MAIT   0.29 +- 0.013 0.9927 +- 0.0056 0.4487 +- 0.0149   2889.0 +- 0.0
           Memory B cell 0.9281 +- 0.0348 0.4272 +- 0.0311 0.5838 +- 0.0214   1395.0 +- 0.0
                 NK cell 0.9805 +- 0.0091 0.8465 +- 0.0408 0.9082 +- 0.0259   5959.0 +- 0.0
            Naive B cell 0.8026 +- 0.0077 0.9943 +- 0.0011 0.8882 +- 0.0042   3385.0 +- 0.0
             Plasma cell 0.9854 +- 0.0329 0.9863 +- 0.0056 0.9856 +- 0.0156    930.0 +- 0.0
Plasmacytoid dendritic cell 0.9058 +- 0.1661 0.989 +- 0.0045 0.9371 +- 0.1024    584.0 +- 0.0
       T regulatory cell 0.0782 +- 0.0035 0.3553 +- 0.1339 0.1255 +- 0.0053   1731.0 +- 0.0

                accuracy                                 0.5278 +- 0.0183  79001.0 +- 0.0
               macro avg 0.6601 +- 0.0201 0.6708 +- 0.0054 0.6048 +- 0.0132  79001.0 +- 0.0
            weighted avg 0.6666 +- 0.0094 0.5278 +- 0.0183 0.4916 +- 0.018  79001.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.5202 +- 0.0196
50% Random Dropout Accuracy: 0.486 +- 0.0277
90% Random Dropout Accuracy: 0.3028 +- 0.036
92.5% Random Dropout Accuracy: 0.2834 +- 0.0365
95% Random Dropout Accuracy: 0.2533 +- 0.044
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.5283 +- 0.0184
Feature importance dropout (0.5% features dropped) Accuracy score 0.5447 +- 0.0174
Feature importance dropout (1.0% features dropped) Accuracy score 0.5374 +- 0.0179
Feature importance dropout (2.0% features dropped) Accuracy score 0.5308 +- 0.0184


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.5959 +- 0.0182
50% Random Dropout Macro_F1: 0.5445 +- 0.0311
90% Random Dropout Macro_F1: 0.2656 +- 0.0472
92.5% Random Dropout Macro_F1: 0.2388 +- 0.0383
95% Random Dropout Macro_F1: 0.1885 +- 0.0274
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.6062 +- 0.0134
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.6075 +- 0.0104
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.5858 +- 0.0128
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.5696 +- 0.0337


