# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8416 +- 0.0016

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9936 +- 0.0004 0.9978 +- 0.0004 0.9957 +- 0.0003   3456.0 +- 0.0
          CD16+ Monocyte 0.9867 +- 0.0044 0.9606 +- 0.0027 0.9735 +- 0.0019    193.0 +- 0.0
    CD1C+ dendritic cell 0.9515 +- 0.0076 0.8713 +- 0.0029 0.9096 +- 0.0037    108.0 +- 0.0
       CD4 Memory T cell 0.9331 +- 0.0032 0.7195 +- 0.016 0.8124 +- 0.0097   2888.0 +- 0.0
        CD4 Naive T cell 0.7841 +- 0.0063 0.938 +- 0.0025 0.8542 +- 0.0035   3439.0 +- 0.0
       CD8 Memory T cell 0.2216 +- 0.0041 0.6236 +- 0.0059 0.327 +- 0.0047    818.0 +- 0.0
        CD8 Naive T cell 0.8986 +- 0.0046 0.8494 +- 0.0085 0.8733 +- 0.0061   2047.0 +- 0.0
      Gamma-delta T cell 0.9686 +- 0.0017 0.6972 +- 0.012 0.8107 +- 0.0086   2544.0 +- 0.0
                    MAIT 0.7736 +- 0.0062 0.839 +- 0.0058 0.805 +- 0.0034    974.0 +- 0.0
           Memory B cell 0.8928 +- 0.0026 0.9478 +- 0.0028 0.9195 +- 0.0023    897.0 +- 0.0
                 NK cell 0.9753 +- 0.0017 0.7455 +- 0.006 0.845 +- 0.0043   2580.0 +- 0.0
            Naive B cell 0.9789 +- 0.0012 0.9539 +- 0.0012 0.9662 +- 0.001   2227.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9804 +- 0.0056 0.9901 +- 0.0029     56.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.7105 +- 0.0223 0.8306 +- 0.0154     57.0 +- 0.0
       T regulatory cell 0.6915 +- 0.0939 0.0316 +- 0.0036 0.0604 +- 0.0066    136.0 +- 0.0

                accuracy                                 0.8416 +- 0.0016  22420.0 +- 0.0
               macro avg  0.87 +- 0.0061 0.7911 +- 0.0017 0.7982 +- 0.0014  22420.0 +- 0.0
            weighted avg 0.8948 +- 0.001 0.8416 +- 0.0016 0.8555 +- 0.0013  22420.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.8256 +- 0.005
50% Random Dropout Accuracy: 0.7234 +- 0.0191
90% Random Dropout Accuracy: 0.3302 +- 0.0277
92.5% Random Dropout Accuracy: 0.2689 +- 0.0326
95% Random Dropout Accuracy: 0.224 +- 0.0299
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.8398 +- 0.0017
Feature importance dropout (0.5% features dropped) Accuracy score 0.8187 +- 0.0023
Feature importance dropout (1.0% features dropped) Accuracy score 0.8135 +- 0.0032
Feature importance dropout (2.0% features dropped) Accuracy score 0.7662 +- 0.0042


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.7836 +- 0.0029
50% Random Dropout Macro_F1: 0.6618 +- 0.016
90% Random Dropout Macro_F1: 0.1347 +- 0.0209
92.5% Random Dropout Macro_F1: 0.0904 +- 0.0166
95% Random Dropout Macro_F1: 0.0623 +- 0.0187
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.7971 +- 0.0013
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.7835 +- 0.0015
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.7739 +- 0.0024
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.7196 +- 0.004



## Out of data distribution 

### Dataset Similarity + Accuracy 

Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.6946 +- 0.0092

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.8604 +- 0.0276 0.9997 +- 0.0002 0.9246 +- 0.0159  12317.0 +- 0.0
          CD16+ Monocyte 0.9885 +- 0.0039 0.6868 +- 0.0886 0.8075 +- 0.0591   1903.0 +- 0.0
    CD1C+ dendritic cell 0.9946 +- 0.0045 0.6296 +- 0.0666 0.7691 +- 0.0463   1079.0 +- 0.0
       CD4 Memory T cell 0.5988 +- 0.0546 0.5598 +- 0.0885 0.5706 +- 0.0312  14241.0 +- 0.0
        CD4 Naive T cell 0.7166 +- 0.0423 0.7654 +- 0.0897 0.7351 +- 0.0208  17151.0 +- 0.0
       CD8 Memory T cell  0.1269 +- 0.01 0.0408 +- 0.0111 0.0613 +- 0.0131   6650.0 +- 0.0
        CD8 Naive T cell 0.9457 +- 0.0036 0.7194 +- 0.0222 0.817 +- 0.0135   6516.0 +- 0.0
      Gamma-delta T cell 0.088 +- 0.0087 0.2123 +- 0.0275 0.1244 +- 0.0134   2271.0 +- 0.0
                    MAIT 0.5035 +- 0.0264 0.9667 +- 0.0053 0.6617 +- 0.0219   2889.0 +- 0.0
           Memory B cell 0.9506 +- 0.0051 0.5176 +- 0.0204  0.67 +- 0.0164   1395.0 +- 0.0
                 NK cell 0.9352 +- 0.0075 0.9515 +- 0.0142 0.9432 +- 0.0054   5959.0 +- 0.0
            Naive B cell 0.8038 +- 0.0169 0.9926 +- 0.0008 0.8882 +- 0.0105   3385.0 +- 0.0
             Plasma cell 0.9983 +- 0.0015   0.99 +- 0.001 0.9941 +- 0.0005    930.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0   0.98 +- 0.003 0.9899 +- 0.0015    584.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   1731.0 +- 0.0

                accuracy                                 0.6946 +- 0.0092  79001.0 +- 0.0
               macro avg 0.7007 +- 0.0029 0.6675 +- 0.0123 0.6638 +- 0.0089  79001.0 +- 0.0
            weighted avg 0.6856 +- 0.0048 0.6946 +- 0.0092 0.6769 +- 0.0081  79001.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.6815 +- 0.0095
50% Random Dropout Accuracy: 0.5747 +- 0.0138
90% Random Dropout Accuracy: 0.3512 +- 0.025
92.5% Random Dropout Accuracy: 0.316 +- 0.0304
95% Random Dropout Accuracy: 0.2809 +- 0.0289
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.6953 +- 0.0092
Feature importance dropout (0.5% features dropped) Accuracy score 0.6944 +- 0.0095
Feature importance dropout (1.0% features dropped) Accuracy score 0.682 +- 0.0094
Feature importance dropout (2.0% features dropped) Accuracy score 0.6526 +- 0.0086


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.645 +- 0.013
50% Random Dropout Macro_F1: 0.4833 +- 0.0219
90% Random Dropout Macro_F1: 0.1146 +- 0.0181
92.5% Random Dropout Macro_F1: 0.0928 +- 0.0148
95% Random Dropout Macro_F1: 0.0634 +- 0.0169
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.6654 +- 0.0086
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.6608 +- 0.0103
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.627 +- 0.0123
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.4909 +- 0.0117


