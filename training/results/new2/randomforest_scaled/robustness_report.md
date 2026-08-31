# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8278 +- 0.003

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9648 +- 0.0022 0.9991 +- 0.0003 0.9817 +- 0.0011   3456.0 +- 0.0
          CD16+ Monocyte 0.9875 +- 0.003 0.7399 +- 0.0181 0.8459 +- 0.0122    193.0 +- 0.0
    CD1C+ dendritic cell 0.9898 +- 0.0132 0.3287 +- 0.0551 0.491 +- 0.0621    108.0 +- 0.0
       CD4 Memory T cell 0.7927 +- 0.0071 0.6215 +- 0.0187 0.6967 +- 0.0133   2888.0 +- 0.0
        CD4 Naive T cell 0.7335 +- 0.0092 0.9778 +- 0.0012 0.8382 +- 0.0057   3439.0 +- 0.0
       CD8 Memory T cell 0.2369 +- 0.0091 0.4733 +- 0.0261 0.3157 +- 0.0127    818.0 +- 0.0
        CD8 Naive T cell 0.9782 +- 0.0037 0.6058 +- 0.0187 0.748 +- 0.0135   2047.0 +- 0.0
      Gamma-delta T cell 0.9591 +- 0.0033 0.8279 +- 0.0159 0.8886 +- 0.0104   2544.0 +- 0.0
                    MAIT 0.6648 +- 0.0179 0.9252 +- 0.0067 0.7735 +- 0.0117    974.0 +- 0.0
           Memory B cell 0.9147 +- 0.0074 0.8606 +- 0.0173 0.8868 +- 0.0097    897.0 +- 0.0
                 NK cell 0.9898 +- 0.0013 0.8229 +- 0.0094 0.8987 +- 0.0056   2580.0 +- 0.0
            Naive B cell 0.9444 +- 0.0065 0.9713 +- 0.0026 0.9576 +- 0.0032   2227.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.8518 +- 0.0189 0.9199 +- 0.011     56.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.4404 +- 0.0587 0.6093 +- 0.0573     57.0 +- 0.0
       T regulatory cell 0.935 +- 0.1055 0.0287 +- 0.0073 0.0556 +- 0.0138    136.0 +- 0.0

                accuracy                                 0.8278 +- 0.003  22420.0 +- 0.0
               macro avg 0.8728 +- 0.0082 0.6983 +- 0.005 0.7271 +- 0.0051  22420.0 +- 0.0
            weighted avg 0.8673 +- 0.0024 0.8278 +- 0.003 0.8317 +- 0.003  22420.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.812 +- 0.0056
50% Random Dropout Accuracy: 0.6786 +- 0.0098
90% Random Dropout Accuracy: 0.1584 +- 0.0164
92.5% Random Dropout Accuracy: 0.1415 +- 0.0107
95% Random Dropout Accuracy: 0.1357 +- 0.0086
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.8218 +- 0.004
Feature importance dropout (0.5% features dropped) Accuracy score 0.7818 +- 0.0044
Feature importance dropout (1.0% features dropped) Accuracy score 0.7691 +- 0.0049
Feature importance dropout (2.0% features dropped) Accuracy score 0.6647 +- 0.0082


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.694 +- 0.0068
50% Random Dropout Macro_F1: 0.4484 +- 0.0118
90% Random Dropout Macro_F1: 0.0314 +- 0.0073
92.5% Random Dropout Macro_F1: 0.0216 +- 0.0046
95% Random Dropout Macro_F1: 0.0186 +- 0.0039
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.7222 +- 0.0053
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.6559 +- 0.0076
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.6217 +- 0.0095
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.5223 +- 0.0085



## Out of data distribution 

### Dataset Similarity + Accuracy 

Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.5876 +- 0.0071

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9743 +- 0.0025 0.9968 +- 0.0008 0.9854 +- 0.001  12317.0 +- 0.0
          CD16+ Monocyte 0.9858 +- 0.0037 0.9624 +- 0.0084 0.9739 +- 0.0031   1903.0 +- 0.0
    CD1C+ dendritic cell 0.9806 +- 0.0064 0.7826 +- 0.0292 0.8701 +- 0.0154   1079.0 +- 0.0
       CD4 Memory T cell 0.3658 +- 0.0076 0.9503 +- 0.0087 0.5282 +- 0.0073  14241.0 +- 0.0
        CD4 Naive T cell 0.8773 +- 0.3096 0.0008 +- 0.0013 0.0017 +- 0.0026  17151.0 +- 0.0
       CD8 Memory T cell 0.4131 +- 0.0149 0.5674 +- 0.0531 0.4777 +- 0.0282   6650.0 +- 0.0
        CD8 Naive T cell 0.9543 +- 0.0149 0.4925 +- 0.1104 0.6417 +- 0.1017   6516.0 +- 0.0
      Gamma-delta T cell 0.0109 +- 0.0058 0.0059 +- 0.005 0.0074 +- 0.0052   2271.0 +- 0.0
                    MAIT 0.8979 +- 0.0246 0.0699 +- 0.0448 0.1265 +- 0.0714   2889.0 +- 0.0
           Memory B cell  0.964 +- 0.007 0.2035 +- 0.048 0.3335 +- 0.0683   1395.0 +- 0.0
                 NK cell 0.8558 +- 0.0339 0.9335 +- 0.0121 0.8925 +- 0.0153   5959.0 +- 0.0
            Naive B cell 0.7511 +- 0.011 0.9981 +- 0.0007 0.8571 +- 0.007   3385.0 +- 0.0
             Plasma cell 0.9992 +- 0.0005 0.9908 +- 0.001 0.995 +- 0.0004    930.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.9887 +- 0.0012 0.9943 +- 0.0006    584.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   1731.0 +- 0.0

                accuracy                                 0.5876 +- 0.0071  79001.0 +- 0.0
               macro avg 0.7353 +- 0.0189 0.5962 +- 0.0072 0.579 +- 0.0089  79001.0 +- 0.0
            weighted avg 0.725 +- 0.0656 0.5876 +- 0.0071 0.5115 +- 0.0091  79001.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.578 +- 0.0083
50% Random Dropout Accuracy: 0.4778 +- 0.0156
90% Random Dropout Accuracy: 0.1858 +- 0.0033
92.5% Random Dropout Accuracy: 0.1827 +- 0.0024
95% Random Dropout Accuracy: 0.1803 +- 0.0001
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.5881 +- 0.0071
Feature importance dropout (0.5% features dropped) Accuracy score 0.5792 +- 0.0094
Feature importance dropout (1.0% features dropped) Accuracy score 0.555 +- 0.0111
Feature importance dropout (2.0% features dropped) Accuracy score 0.4571 +- 0.006


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.5587 +- 0.0097
50% Random Dropout Macro_F1: 0.3689 +- 0.017
90% Random Dropout Macro_F1: 0.0275 +- 0.0043
92.5% Random Dropout Macro_F1: 0.0229 +- 0.0022
95% Random Dropout Macro_F1: 0.0204 +- 0.0001
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.5804 +- 0.0089
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.5532 +- 0.011
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.5124 +- 0.0162
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.3777 +- 0.0115


