# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.817 +- 0.0008

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9934 +- 0.0004 0.9964 +- 0.0004 0.9949 +- 0.0003   3456.0 +- 0.0
          CD16+ Monocyte 0.9806 +- 0.0071 0.9415 +- 0.0055 0.9606 +- 0.0038    193.0 +- 0.0
    CD1C+ dendritic cell 0.9156 +- 0.0064 0.8935 +- 0.0065 0.9044 +- 0.0045    108.0 +- 0.0
       CD4 Memory T cell 0.7874 +- 0.0022 0.9644 +- 0.0023 0.8669 +- 0.0016   2888.0 +- 0.0
        CD4 Naive T cell 0.8634 +- 0.0017 0.9597 +- 0.0014 0.909 +- 0.0013   3439.0 +- 0.0
       CD8 Memory T cell 0.1553 +- 0.0029 0.5172 +- 0.0105 0.2389 +- 0.0045    818.0 +- 0.0
        CD8 Naive T cell 0.9334 +- 0.0028 0.6481 +- 0.005 0.765 +- 0.0037   2047.0 +- 0.0
      Gamma-delta T cell 0.9303 +- 0.0043 0.3518 +- 0.0041 0.5105 +- 0.0046   2544.0 +- 0.0
                    MAIT  0.82 +- 0.0045 0.9182 +- 0.0045 0.8663 +- 0.003    974.0 +- 0.0
           Memory B cell 0.9561 +- 0.0023 0.9158 +- 0.0038 0.9355 +- 0.0021    897.0 +- 0.0
                 NK cell 0.9919 +- 0.0011 0.7166 +- 0.0015 0.8321 +- 0.0013   2580.0 +- 0.0
            Naive B cell 0.9667 +- 0.0015 0.9836 +- 0.001 0.9751 +- 0.0008   2227.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9589 +- 0.0121 0.979 +- 0.0064     56.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.6491 +- 0.0143 0.7872 +- 0.0105     57.0 +- 0.0
       T regulatory cell 0.7432 +- 0.0474 0.1382 +- 0.0285 0.232 +- 0.0419    136.0 +- 0.0

                accuracy                                 0.817 +- 0.0008  22420.0 +- 0.0
               macro avg 0.8692 +- 0.0031 0.7702 +- 0.0025 0.7838 +- 0.0028  22420.0 +- 0.0
            weighted avg 0.8899 +- 0.0009 0.817 +- 0.0008 0.8271 +- 0.0009  22420.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.8077 +- 0.0028
50% Random Dropout Accuracy: 0.6971 +- 0.0133
90% Random Dropout Accuracy: 0.15 +- 0.0155
92.5% Random Dropout Accuracy: 0.1432 +- 0.0085
95% Random Dropout Accuracy: 0.1319 +- 0.0038
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.813 +- 0.0009
Feature importance dropout (0.5% features dropped) Accuracy score 0.8059 +- 0.0009
Feature importance dropout (1.0% features dropped) Accuracy score 0.7927 +- 0.0019
Feature importance dropout (2.0% features dropped) Accuracy score 0.7292 +- 0.0022


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.7686 +- 0.0036
50% Random Dropout Macro_F1: 0.6105 +- 0.0173
90% Random Dropout Macro_F1: 0.0298 +- 0.0089
92.5% Random Dropout Macro_F1: 0.0237 +- 0.0048
95% Random Dropout Macro_F1: 0.0173 +- 0.0024
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.7761 +- 0.0023
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.7669 +- 0.0022
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.7453 +- 0.0022
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.6815 +- 0.003



## Out of data distribution 

### Dataset Similarity + Accuracy 

Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.5864 +- 0.005

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9759 +- 0.0032 0.9962 +- 0.0009 0.9859 +- 0.0013  12317.0 +- 0.0
          CD16+ Monocyte 0.9825 +- 0.0036 0.9697 +- 0.0056 0.9761 +- 0.0017   1903.0 +- 0.0
    CD1C+ dendritic cell 0.9804 +- 0.0071 0.7855 +- 0.0318 0.8718 +- 0.0176   1079.0 +- 0.0
       CD4 Memory T cell 0.365 +- 0.0041 0.9513 +- 0.0071 0.5275 +- 0.0045  14241.0 +- 0.0
        CD4 Naive T cell 0.8467 +- 0.319 0.0003 +- 0.0003 0.0005 +- 0.0006  17151.0 +- 0.0
       CD8 Memory T cell 0.4097 +- 0.009 0.5545 +- 0.029 0.4711 +- 0.0148   6650.0 +- 0.0
        CD8 Naive T cell 0.9622 +- 0.0074 0.4814 +- 0.059 0.6395 +- 0.053   6516.0 +- 0.0
      Gamma-delta T cell 0.0117 +- 0.0047 0.0069 +- 0.0031 0.0086 +- 0.0037   2271.0 +- 0.0
                    MAIT 0.9186 +- 0.0194 0.0779 +- 0.0327  0.142 +- 0.055   2889.0 +- 0.0
           Memory B cell 0.9627 +- 0.0088 0.2205 +- 0.0385 0.3573 +- 0.0496   1395.0 +- 0.0
                 NK cell 0.8647 +- 0.0257  0.934 +- 0.007 0.8978 +- 0.0128   5959.0 +- 0.0
            Naive B cell 0.7548 +- 0.0092 0.9974 +- 0.0011 0.8593 +- 0.0056   3385.0 +- 0.0
             Plasma cell 0.9992 +- 0.0005 0.9909 +- 0.0008 0.995 +- 0.0003    930.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.9899 +- 0.001 0.9949 +- 0.0005    584.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   1731.0 +- 0.0

                accuracy                                 0.5864 +- 0.005  79001.0 +- 0.0
               macro avg 0.7356 +- 0.0205 0.5971 +- 0.0062 0.5818 +- 0.0068  79001.0 +- 0.0
            weighted avg 0.7203 +- 0.069 0.5864 +- 0.005 0.5121 +- 0.0055  79001.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.5773 +- 0.0074
50% Random Dropout Accuracy: 0.4667 +- 0.0252
90% Random Dropout Accuracy: 0.1844 +- 0.0053
92.5% Random Dropout Accuracy: 0.1838 +- 0.0034
95% Random Dropout Accuracy: 0.1817 +- 0.0022
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.5868 +- 0.0049
Feature importance dropout (0.5% features dropped) Accuracy score 0.5783 +- 0.0075
Feature importance dropout (1.0% features dropped) Accuracy score 0.55 +- 0.01
Feature importance dropout (2.0% features dropped) Accuracy score 0.4558 +- 0.0079


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.5609 +- 0.0108
50% Random Dropout Macro_F1: 0.363 +- 0.0285
90% Random Dropout Macro_F1: 0.0255 +- 0.0048
92.5% Random Dropout Macro_F1: 0.0234 +- 0.0026
95% Random Dropout Macro_F1: 0.0221 +- 0.0024
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.583 +- 0.0066
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.5524 +- 0.0087
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.5084 +- 0.0127
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.3719 +- 0.0116


