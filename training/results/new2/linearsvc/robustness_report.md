# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8789 +- 0.0013

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.994 +- 0.0004 0.9957 +- 0.0002 0.9949 +- 0.0003   3456.0 +- 0.0
          CD16+ Monocyte 0.9634 +- 0.0039 0.9803 +- 0.0022 0.9718 +- 0.0024    193.0 +- 0.0
    CD1C+ dendritic cell 0.9211 +- 0.0037 0.8972 +- 0.0092 0.909 +- 0.0037    108.0 +- 0.0
       CD4 Memory T cell 0.9294 +- 0.0014 0.8028 +- 0.0031 0.8615 +- 0.0021   2888.0 +- 0.0
        CD4 Naive T cell 0.8669 +- 0.0019 0.925 +- 0.0016 0.895 +- 0.0017   3439.0 +- 0.0
       CD8 Memory T cell 0.3089 +- 0.0033 0.5775 +- 0.0063 0.4025 +- 0.0028    818.0 +- 0.0
        CD8 Naive T cell 0.8977 +- 0.0018 0.9266 +- 0.0014 0.9119 +- 0.0006   2047.0 +- 0.0
      Gamma-delta T cell 0.9647 +- 0.0014 0.818 +- 0.0044 0.8853 +- 0.0024   2544.0 +- 0.0
                    MAIT 0.7499 +- 0.0029 0.9009 +- 0.0035 0.8185 +- 0.0027    974.0 +- 0.0
           Memory B cell 0.893 +- 0.0015 0.9551 +- 0.0021 0.923 +- 0.0016    897.0 +- 0.0
                 NK cell 0.9864 +- 0.0003 0.7839 +- 0.0017 0.8736 +- 0.001   2580.0 +- 0.0
            Naive B cell 0.9798 +- 0.0011 0.9538 +- 0.0007 0.9666 +- 0.0008   2227.0 +- 0.0
             Plasma cell 0.8425 +- 0.0092 0.9929 +- 0.0092 0.9115 +- 0.0074     56.0 +- 0.0
Plasmacytoid dendritic cell 0.9642 +- 0.0002 0.9456 +- 0.0055 0.9548 +- 0.0029     57.0 +- 0.0
       T regulatory cell 0.1698 +- 0.0098 0.2787 +- 0.0157 0.211 +- 0.0111    136.0 +- 0.0

                accuracy                                 0.8789 +- 0.0013  22420.0 +- 0.0
               macro avg 0.8288 +- 0.0011 0.8489 +- 0.0022 0.8327 +- 0.0016  22420.0 +- 0.0
            weighted avg 0.9061 +- 0.0007 0.8789 +- 0.0013 0.8878 +- 0.0011  22420.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.8558 +- 0.008
50% Random Dropout Accuracy: 0.7148 +- 0.011
90% Random Dropout Accuracy: 0.3228 +- 0.0437
92.5% Random Dropout Accuracy: 0.2809 +- 0.0257
95% Random Dropout Accuracy: 0.2395 +- 0.0224
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.8736 +- 0.0014
Feature importance dropout (0.5% features dropped) Accuracy score 0.8447 +- 0.0017
Feature importance dropout (1.0% features dropped) Accuracy score 0.8412 +- 0.0013
Feature importance dropout (2.0% features dropped) Accuracy score 0.6878 +- 0.0025


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.8049 +- 0.0049
50% Random Dropout Macro_F1: 0.586 +- 0.0158
90% Random Dropout Macro_F1: 0.1796 +- 0.0291
92.5% Random Dropout Macro_F1: 0.1456 +- 0.0168
95% Random Dropout Macro_F1: 0.1116 +- 0.0122
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.8277 +- 0.0016
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.7964 +- 0.0018
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.7934 +- 0.0015
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.6393 +- 0.0069



## Out of data distribution 

### Dataset Similarity + Accuracy 

Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.5814 +- 0.0106

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.8922 +- 0.0459 0.9881 +- 0.0014 0.9371 +- 0.0246  12317.0 +- 0.0
          CD16+ Monocyte 0.3811 +- 0.064 0.9893 +- 0.0008 0.5474 +- 0.0676   1903.0 +- 0.0
    CD1C+ dendritic cell 0.3324 +- 0.0367 0.9239 +- 0.0151 0.488 +- 0.0413   1079.0 +- 0.0
       CD4 Memory T cell  0.46 +- 0.0092 0.5342 +- 0.0487 0.493 +- 0.0166  14241.0 +- 0.0
        CD4 Naive T cell 0.9592 +- 0.0027 0.1283 +- 0.0112 0.2261 +- 0.0174  17151.0 +- 0.0
       CD8 Memory T cell 0.0164 +- 0.0115 0.0004 +- 0.0003 0.0008 +- 0.0005   6650.0 +- 0.0
        CD8 Naive T cell 0.6978 +- 0.0603 0.9684 +- 0.0113 0.8094 +- 0.0363   6516.0 +- 0.0
      Gamma-delta T cell 0.1017 +- 0.0135 0.269 +- 0.0536 0.1475 +- 0.0224   2271.0 +- 0.0
                    MAIT 0.5586 +- 0.0558 0.9212 +- 0.0422 0.6924 +- 0.0308   2889.0 +- 0.0
           Memory B cell 0.8441 +- 0.0472 0.4999 +- 0.0291 0.6264 +- 0.0171   1395.0 +- 0.0
                 NK cell 0.7553 +- 0.069 0.9935 +- 0.0031 0.8565 +- 0.0441   5959.0 +- 0.0
            Naive B cell 0.7133 +- 0.0361 0.9921 +- 0.001 0.8295 +- 0.0244   3385.0 +- 0.0
             Plasma cell 0.2691 +- 0.0529 0.9915 +- 0.0009 0.4207 +- 0.0664    930.0 +- 0.0
Plasmacytoid dendritic cell 0.6676 +- 0.0435 0.9836 +- 0.0031 0.7946 +- 0.0314    584.0 +- 0.0
       T regulatory cell 0.0618 +- 0.0101 0.0083 +- 0.0023 0.0145 +- 0.0037   1731.0 +- 0.0

                accuracy                                 0.5814 +- 0.0106  79001.0 +- 0.0
               macro avg 0.514 +- 0.0136 0.6794 +- 0.0111 0.5256 +- 0.0179  79001.0 +- 0.0
            weighted avg 0.6382 +- 0.0076 0.5814 +- 0.0106 0.5227 +- 0.0095  79001.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.57 +- 0.0158
50% Random Dropout Accuracy: 0.4749 +- 0.0179
90% Random Dropout Accuracy: 0.2734 +- 0.0267
92.5% Random Dropout Accuracy: 0.2572 +- 0.0279
95% Random Dropout Accuracy: 0.2366 +- 0.0354
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.5812 +- 0.0102
Feature importance dropout (0.5% features dropped) Accuracy score 0.583 +- 0.0137
Feature importance dropout (1.0% features dropped) Accuracy score 0.577 +- 0.0145
Feature importance dropout (2.0% features dropped) Accuracy score 0.5257 +- 0.0136


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.5089 +- 0.0226
50% Random Dropout Macro_F1: 0.3808 +- 0.0244
90% Random Dropout Macro_F1: 0.1634 +- 0.0151
92.5% Random Dropout Macro_F1: 0.1415 +- 0.0173
95% Random Dropout Macro_F1: 0.1243 +- 0.0147
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.5259 +- 0.0176
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.5173 +- 0.0249
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.498 +- 0.0262
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.4093 +- 0.0241


