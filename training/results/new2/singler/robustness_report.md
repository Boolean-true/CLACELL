# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8554 +- 0.0

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte   0.9974 +- 0.0   0.9905 +- 0.0   0.9939 +- 0.0   3456.0 +- 0.0
          CD16+ Monocyte    0.974 +- 0.0   0.9689 +- 0.0   0.9714 +- 0.0    193.0 +- 0.0
    CD1C+ dendritic cell    0.782 +- 0.0    0.963 +- 0.0   0.8631 +- 0.0    108.0 +- 0.0
       CD4 Memory T cell   0.9567 +- 0.0   0.7427 +- 0.0   0.8363 +- 0.0   2888.0 +- 0.0
        CD4 Naive T cell   0.8391 +- 0.0   0.8369 +- 0.0    0.838 +- 0.0   3439.0 +- 0.0
       CD8 Memory T cell   0.0084 +- 0.0   0.0049 +- 0.0   0.0062 +- 0.0    818.0 +- 0.0
        CD8 Naive T cell   0.8257 +- 0.0   0.9468 +- 0.0   0.8821 +- 0.0   2047.0 +- 0.0
      Gamma-delta T cell   0.9678 +- 0.0   0.7685 +- 0.0   0.8567 +- 0.0   2544.0 +- 0.0
                    MAIT   0.7363 +- 0.0    0.886 +- 0.0   0.8043 +- 0.0    974.0 +- 0.0
           Memory B cell   0.8974 +- 0.0   0.9454 +- 0.0   0.9207 +- 0.0    897.0 +- 0.0
                 NK cell   0.9673 +- 0.0   0.9744 +- 0.0   0.9708 +- 0.0   2580.0 +- 0.0
            Naive B cell   0.9775 +- 0.0   0.9564 +- 0.0   0.9669 +- 0.0   2227.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     56.0 +- 0.0
Plasmacytoid dendritic cell     0.98 +- 0.0   0.8596 +- 0.0   0.9159 +- 0.0     57.0 +- 0.0
       T regulatory cell   0.0732 +- 0.0   0.6176 +- 0.0   0.1308 +- 0.0    136.0 +- 0.0

                accuracy                                   0.8554 +- 0.0  22420.0 +- 0.0
               macro avg   0.7989 +- 0.0   0.8308 +- 0.0   0.7971 +- 0.0  22420.0 +- 0.0
            weighted avg   0.8851 +- 0.0   0.8554 +- 0.0   0.8651 +- 0.0  22420.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.8471 +- 0.0017
50% Random Dropout Accuracy: 0.7933 +- 0.0077
90% Random Dropout Accuracy: 0.5388 +- 0.0144
92.5% Random Dropout Accuracy: 0.4814 +- 0.0129
95% Random Dropout Accuracy: 0.4115 +- 0.0171
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.8522 +- 0.0
Feature importance dropout (0.5% features dropped) Accuracy score 0.8448 +- 0.0
Feature importance dropout (1.0% features dropped) Accuracy score 0.8377 +- 0.0
Feature importance dropout (2.0% features dropped) Accuracy score 0.8088 +- 0.0


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.7888 +- 0.0017
50% Random Dropout Macro_F1: 0.7413 +- 0.0065
90% Random Dropout Macro_F1: 0.4455 +- 0.0151
92.5% Random Dropout Macro_F1: 0.3781 +- 0.0126
95% Random Dropout Macro_F1: 0.3134 +- 0.0136
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.7949 +- 0.0
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.788 +- 0.0
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.7827 +- 0.0
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.7666 +- 0.0



## Out of data distribution 

### Dataset Similarity + Accuracy 

Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.6672 +- 0.0

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte   0.9729 +- 0.0   0.9956 +- 0.0   0.9841 +- 0.0  12317.0 +- 0.0
          CD16+ Monocyte   0.9901 +- 0.0   0.8954 +- 0.0   0.9404 +- 0.0   1903.0 +- 0.0
    CD1C+ dendritic cell   0.9392 +- 0.0   0.8869 +- 0.0   0.9123 +- 0.0   1079.0 +- 0.0
       CD4 Memory T cell   0.4827 +- 0.0   0.5377 +- 0.0   0.5087 +- 0.0  14241.0 +- 0.0
        CD4 Naive T cell   0.9126 +- 0.0   0.4754 +- 0.0   0.6252 +- 0.0  17151.0 +- 0.0
       CD8 Memory T cell   0.1528 +- 0.0   0.0311 +- 0.0   0.0517 +- 0.0   6650.0 +- 0.0
        CD8 Naive T cell   0.8103 +- 0.0   0.9672 +- 0.0   0.8818 +- 0.0   6516.0 +- 0.0
      Gamma-delta T cell   0.0948 +- 0.0   0.2281 +- 0.0   0.1339 +- 0.0   2271.0 +- 0.0
                    MAIT   0.3252 +- 0.0   0.9695 +- 0.0    0.487 +- 0.0   2889.0 +- 0.0
           Memory B cell   0.9461 +- 0.0   0.6918 +- 0.0   0.7992 +- 0.0   1395.0 +- 0.0
                 NK cell   0.8394 +- 0.0   0.9982 +- 0.0   0.9119 +- 0.0   5959.0 +- 0.0
            Naive B cell   0.8846 +- 0.0   0.9897 +- 0.0   0.9342 +- 0.0   3385.0 +- 0.0
             Plasma cell   0.9956 +- 0.0   0.9785 +- 0.0    0.987 +- 0.0    930.0 +- 0.0
Plasmacytoid dendritic cell   0.9983 +- 0.0   0.9966 +- 0.0   0.9974 +- 0.0    584.0 +- 0.0
       T regulatory cell    0.174 +- 0.0    0.227 +- 0.0    0.197 +- 0.0   1731.0 +- 0.0

                accuracy                                   0.6672 +- 0.0  79001.0 +- 0.0
               macro avg   0.7012 +- 0.0   0.7246 +- 0.0   0.6901 +- 0.0  79001.0 +- 0.0
            weighted avg   0.7086 +- 0.0   0.6672 +- 0.0    0.661 +- 0.0  79001.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.6598 +- 0.0032
50% Random Dropout Accuracy: 0.614 +- 0.0107
90% Random Dropout Accuracy: 0.4207 +- 0.0178
92.5% Random Dropout Accuracy: 0.3781 +- 0.0117
95% Random Dropout Accuracy: 0.3182 +- 0.015
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.6679 +- 0.0
Feature importance dropout (0.5% features dropped) Accuracy score 0.6762 +- 0.0
Feature importance dropout (1.0% features dropped) Accuracy score 0.6725 +- 0.0
Feature importance dropout (2.0% features dropped) Accuracy score 0.6793 +- 0.0


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.6847 +- 0.0014
50% Random Dropout Macro_F1: 0.6437 +- 0.0097
90% Random Dropout Macro_F1: 0.3838 +- 0.0173
92.5% Random Dropout Macro_F1: 0.3401 +- 0.0071
95% Random Dropout Macro_F1: 0.2696 +- 0.0123
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.6914 +- 0.0
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.69 +- 0.0
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.6827 +- 0.0
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.6815 +- 0.0


