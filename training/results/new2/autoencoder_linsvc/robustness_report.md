# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8386 +- 0.006

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9938 +- 0.0008 0.9821 +- 0.0089 0.9879 +- 0.0046   3456.0 +- 0.0
          CD16+ Monocyte 0.9365 +- 0.0209 0.9456 +- 0.011 0.9408 +- 0.0075    193.0 +- 0.0
    CD1C+ dendritic cell 0.6746 +- 0.1362 0.8787 +- 0.0211 0.7554 +- 0.0842    108.0 +- 0.0
       CD4 Memory T cell 0.9143 +- 0.0158 0.6624 +- 0.0243 0.7678 +- 0.0139   2888.0 +- 0.0
        CD4 Naive T cell 0.7662 +- 0.0274 0.907 +- 0.0188 0.8301 +- 0.0108   3439.0 +- 0.0
       CD8 Memory T cell 0.2363 +- 0.0358 0.4204 +- 0.0681 0.302 +- 0.0443    818.0 +- 0.0
        CD8 Naive T cell 0.8487 +- 0.0369 0.8912 +- 0.0532 0.8674 +- 0.0149   2047.0 +- 0.0
      Gamma-delta T cell 0.9415 +- 0.0177 0.7386 +- 0.0524 0.8264 +- 0.0284   2544.0 +- 0.0
                    MAIT 0.6735 +- 0.073 0.8319 +- 0.0526 0.7396 +- 0.0336    974.0 +- 0.0
           Memory B cell 0.8872 +- 0.0114 0.9047 +- 0.0201 0.8956 +- 0.0064    897.0 +- 0.0
                 NK cell 0.9537 +- 0.0184 0.8435 +- 0.0355 0.8945 +- 0.0117   2580.0 +- 0.0
            Naive B cell 0.9611 +- 0.0074 0.9533 +- 0.006 0.9572 +- 0.002   2227.0 +- 0.0
             Plasma cell 0.9824 +- 0.0141 0.9875 +- 0.0147 0.9849 +- 0.0111     56.0 +- 0.0
Plasmacytoid dendritic cell 0.9657 +- 0.0121 0.6895 +- 0.031 0.8042 +- 0.0214     57.0 +- 0.0
       T regulatory cell 0.2609 +- 0.0683 0.2574 +- 0.0737 0.2464 +- 0.0325    136.0 +- 0.0

                accuracy                                 0.8386 +- 0.006  22420.0 +- 0.0
               macro avg 0.7998 +- 0.009 0.7929 +- 0.0086 0.7867 +- 0.0092  22420.0 +- 0.0
            weighted avg 0.8692 +- 0.0045 0.8386 +- 0.006 0.8462 +- 0.0057  22420.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.8251 +- 0.0066
50% Random Dropout Accuracy: 0.6937 +- 0.0202
90% Random Dropout Accuracy: 0.2806 +- 0.044
92.5% Random Dropout Accuracy: 0.2258 +- 0.0396
95% Random Dropout Accuracy: 0.1906 +- 0.0295
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.8366 +- 0.006
Feature importance dropout (0.5% features dropped) Accuracy score 0.824 +- 0.0057
Feature importance dropout (1.0% features dropped) Accuracy score 0.8094 +- 0.0069
Feature importance dropout (2.0% features dropped) Accuracy score 0.7622 +- 0.0109


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.7768 +- 0.0096
50% Random Dropout Macro_F1: 0.6226 +- 0.0235
90% Random Dropout Macro_F1: 0.1154 +- 0.0245
92.5% Random Dropout Macro_F1: 0.0758 +- 0.0202
95% Random Dropout Macro_F1: 0.0487 +- 0.0165
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.7844 +- 0.01
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.7757 +- 0.0097
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.7642 +- 0.0089
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.7275 +- 0.0094



## Out of data distribution 

### Dataset Similarity + Accuracy 

Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.6834 +- 0.0159

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.8468 +- 0.0198 0.9999 +- 0.0001 0.9169 +- 0.0116  12317.0 +- 0.0
          CD16+ Monocyte 0.9991 +- 0.001 0.3995 +- 0.1446 0.5571 +- 0.1468   1903.0 +- 0.0
    CD1C+ dendritic cell 0.8976 +- 0.3154 0.1421 +- 0.0995 0.2368 +- 0.1519   1079.0 +- 0.0
       CD4 Memory T cell 0.7049 +- 0.0513 0.3911 +- 0.1239 0.4875 +- 0.093  14241.0 +- 0.0
        CD4 Naive T cell 0.648 +- 0.0422 0.9058 +- 0.043 0.7535 +- 0.016  17151.0 +- 0.0
       CD8 Memory T cell 0.1746 +- 0.0587 0.0612 +- 0.0264 0.0893 +- 0.0346   6650.0 +- 0.0
        CD8 Naive T cell 0.8926 +- 0.0292 0.793 +- 0.0805 0.8363 +- 0.0399   6516.0 +- 0.0
      Gamma-delta T cell 0.077 +- 0.0204 0.1953 +- 0.0717 0.1101 +- 0.0321   2271.0 +- 0.0
                    MAIT 0.6717 +- 0.0643 0.8681 +- 0.0825 0.7513 +- 0.0121   2889.0 +- 0.0
           Memory B cell 0.9689 +- 0.0113 0.2657 +- 0.0971 0.4081 +- 0.119   1395.0 +- 0.0
                 NK cell 0.8066 +- 0.0675 0.989 +- 0.0064 0.8869 +- 0.0402   5959.0 +- 0.0
            Naive B cell 0.7545 +- 0.0364 0.9975 +- 0.0014 0.8586 +- 0.0236   3385.0 +- 0.0
             Plasma cell 0.9811 +- 0.0177 0.9848 +- 0.0054 0.9828 +- 0.0077    930.0 +- 0.0
Plasmacytoid dendritic cell 0.9947 +- 0.0074 0.9795 +- 0.0162 0.9869 +- 0.0075    584.0 +- 0.0
       T regulatory cell 0.0591 +- 0.1575 0.0001 +- 0.0002 0.0002 +- 0.0005   1731.0 +- 0.0

                accuracy                                 0.6834 +- 0.0159  79001.0 +- 0.0
               macro avg 0.6985 +- 0.0261 0.5982 +- 0.0184 0.5908 +- 0.0212  79001.0 +- 0.0
            weighted avg 0.6817 +- 0.0125 0.6834 +- 0.0159 0.648 +- 0.0203  79001.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.6604 +- 0.0188
50% Random Dropout Accuracy: 0.5509 +- 0.0147
90% Random Dropout Accuracy: 0.2852 +- 0.0438
92.5% Random Dropout Accuracy: 0.2523 +- 0.0306
95% Random Dropout Accuracy: 0.2334 +- 0.0152
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.6839 +- 0.0159
Feature importance dropout (0.5% features dropped) Accuracy score 0.6788 +- 0.0165
Feature importance dropout (1.0% features dropped) Accuracy score 0.6713 +- 0.0173
Feature importance dropout (2.0% features dropped) Accuracy score 0.6361 +- 0.0176


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.5616 +- 0.0239
50% Random Dropout Macro_F1: 0.3978 +- 0.031
90% Random Dropout Macro_F1: 0.0863 +- 0.0256
92.5% Random Dropout Macro_F1: 0.0589 +- 0.0173
95% Random Dropout Macro_F1: 0.0408 +- 0.0122
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.5928 +- 0.0218
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.5796 +- 0.0231
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.5687 +- 0.0237
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.5095 +- 0.023


