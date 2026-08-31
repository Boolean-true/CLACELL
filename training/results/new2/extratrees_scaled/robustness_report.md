# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8492 +- 0.0024

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9676 +- 0.0017 0.9999 +- 0.0001 0.9835 +- 0.0009   3456.0 +- 0.0
          CD16+ Monocyte      1.0 +- 0.0 0.786 +- 0.0115 0.8801 +- 0.0072    193.0 +- 0.0
    CD1C+ dendritic cell      1.0 +- 0.0 0.3407 +- 0.0543  0.506 +- 0.063    108.0 +- 0.0
       CD4 Memory T cell 0.8538 +- 0.0076 0.8822 +- 0.0126 0.8677 +- 0.0079   2888.0 +- 0.0
        CD4 Naive T cell 0.793 +- 0.0062 0.9806 +- 0.0012 0.8769 +- 0.0035   3439.0 +- 0.0
       CD8 Memory T cell 0.2214 +- 0.0095 0.4392 +- 0.0138 0.2944 +- 0.0112    818.0 +- 0.0
        CD8 Naive T cell 0.973 +- 0.0031 0.7161 +- 0.0195 0.8248 +- 0.0124   2047.0 +- 0.0
      Gamma-delta T cell 0.9723 +- 0.0022 0.7199 +- 0.0158 0.8272 +- 0.0109   2544.0 +- 0.0
                    MAIT 0.7255 +- 0.006 0.9393 +- 0.0031 0.8187 +- 0.0044    974.0 +- 0.0
           Memory B cell 0.9245 +- 0.0024 0.8158 +- 0.009 0.8667 +- 0.0053    897.0 +- 0.0
                 NK cell 0.9907 +- 0.0011 0.7462 +- 0.0084 0.8512 +- 0.0051   2580.0 +- 0.0
            Naive B cell 0.9287 +- 0.0032 0.9736 +- 0.001 0.9506 +- 0.0017   2227.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.8321 +- 0.0282 0.9081 +- 0.0171     56.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.5491 +- 0.0144 0.7088 +- 0.0121     57.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    136.0 +- 0.0

                accuracy                                 0.8492 +- 0.0024  22420.0 +- 0.0
               macro avg 0.8234 +- 0.001 0.7147 +- 0.0041 0.7443 +- 0.0046  22420.0 +- 0.0
            weighted avg 0.8812 +- 0.0018 0.8492 +- 0.0024 0.8545 +- 0.0024  22420.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.8236 +- 0.008
50% Random Dropout Accuracy: 0.6407 +- 0.0217
90% Random Dropout Accuracy: 0.1577 +- 0.0051
92.5% Random Dropout Accuracy: 0.1546 +- 0.0034
95% Random Dropout Accuracy: 0.1537 +- 0.0011
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.8359 +- 0.0035
Feature importance dropout (0.5% features dropped) Accuracy score 0.799 +- 0.003
Feature importance dropout (1.0% features dropped) Accuracy score 0.7663 +- 0.0033
Feature importance dropout (2.0% features dropped) Accuracy score 0.6709 +- 0.0058


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.6961 +- 0.0084
50% Random Dropout Macro_F1: 0.3991 +- 0.0248
90% Random Dropout Macro_F1: 0.0205 +- 0.0026
92.5% Random Dropout Macro_F1: 0.0185 +- 0.002
95% Random Dropout Macro_F1: 0.0181 +- 0.001
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.7371 +- 0.005
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.6809 +- 0.0071
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.6287 +- 0.0097
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.5249 +- 0.0147



## Out of data distribution 

### Dataset Similarity + Accuracy 

Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.679 +- 0.0064

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9059 +- 0.0054 0.9997 +- 0.0001 0.9505 +- 0.003  12317.0 +- 0.0
          CD16+ Monocyte 0.9979 +- 0.0005 0.8304 +- 0.0271 0.9063 +- 0.016   1903.0 +- 0.0
    CD1C+ dendritic cell 0.9992 +- 0.0024 0.1617 +- 0.0585 0.2745 +- 0.0851   1079.0 +- 0.0
       CD4 Memory T cell 0.7162 +- 0.0255 0.2423 +- 0.0601 0.3576 +- 0.0617  14241.0 +- 0.0
        CD4 Naive T cell 0.5763 +- 0.0124 0.9405 +- 0.0189 0.7144 +- 0.0054  17151.0 +- 0.0
       CD8 Memory T cell 0.3393 +- 0.0294 0.1385 +- 0.0299 0.1953 +- 0.0314   6650.0 +- 0.0
        CD8 Naive T cell 0.8712 +- 0.0174 0.8362 +- 0.015 0.8531 +- 0.0048   6516.0 +- 0.0
      Gamma-delta T cell 0.0148 +- 0.0048 0.0244 +- 0.0096 0.0184 +- 0.0064   2271.0 +- 0.0
                    MAIT 0.6652 +- 0.0294 0.7883 +- 0.0577 0.7195 +- 0.0169   2889.0 +- 0.0
           Memory B cell 0.9417 +- 0.0043 0.4023 +- 0.0182 0.5636 +- 0.0181   1395.0 +- 0.0
                 NK cell 0.6976 +- 0.0299 0.986 +- 0.0035 0.8167 +- 0.0198   5959.0 +- 0.0
            Naive B cell 0.7984 +- 0.0049 0.9951 +- 0.0004 0.8859 +- 0.0029   3385.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9743 +- 0.0043 0.987 +- 0.0022    930.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.9856 +- 0.0014 0.9928 +- 0.0007    584.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   1731.0 +- 0.0

                accuracy                                 0.679 +- 0.0064  79001.0 +- 0.0
               macro avg 0.7016 +- 0.0029 0.6204 +- 0.0044 0.6157 +- 0.0077  79001.0 +- 0.0
            weighted avg 0.6809 +- 0.0037 0.679 +- 0.0064 0.6354 +- 0.0124  79001.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.656 +- 0.0082
50% Random Dropout Accuracy: 0.5407 +- 0.0079
90% Random Dropout Accuracy: 0.2224 +- 0.01
92.5% Random Dropout Accuracy: 0.2178 +- 0.0013
95% Random Dropout Accuracy: 0.2174 +- 0.0011
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.6797 +- 0.0067
Feature importance dropout (0.5% features dropped) Accuracy score 0.6602 +- 0.0069
Feature importance dropout (1.0% features dropped) Accuracy score 0.6446 +- 0.0072
Feature importance dropout (2.0% features dropped) Accuracy score 0.5249 +- 0.0041


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.5803 +- 0.0096
50% Random Dropout Macro_F1: 0.3715 +- 0.014
90% Random Dropout Macro_F1: 0.0284 +- 0.0069
92.5% Random Dropout Macro_F1: 0.0249 +- 0.002
95% Random Dropout Macro_F1: 0.0242 +- 0.0012
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.6183 +- 0.0081
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.5777 +- 0.0066
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.5548 +- 0.0075
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.382 +- 0.0181


