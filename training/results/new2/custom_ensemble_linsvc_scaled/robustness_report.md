# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8458 +- 0.0014

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9939 +- 0.0004 0.9971 +- 0.0003 0.9955 +- 0.0002   3456.0 +- 0.0
          CD16+ Monocyte 0.9892 +- 0.0025 0.9492 +- 0.0068 0.9688 +- 0.0036    193.0 +- 0.0
    CD1C+ dendritic cell 0.9298 +- 0.0074 0.8944 +- 0.0048 0.9118 +- 0.0043    108.0 +- 0.0
       CD4 Memory T cell 0.9369 +- 0.0026 0.7129 +- 0.0174 0.8096 +- 0.0103   2888.0 +- 0.0
        CD4 Naive T cell 0.775 +- 0.0067 0.9411 +- 0.002  0.85 +- 0.0041   3439.0 +- 0.0
       CD8 Memory T cell 0.2334 +- 0.0046 0.617 +- 0.0037 0.3386 +- 0.0049    818.0 +- 0.0
        CD8 Naive T cell 0.9071 +- 0.0045 0.8686 +- 0.0114 0.8874 +- 0.0076   2047.0 +- 0.0
      Gamma-delta T cell 0.967 +- 0.0023 0.7215 +- 0.0123 0.8264 +- 0.0085   2544.0 +- 0.0
                    MAIT 0.7735 +- 0.0083 0.8315 +- 0.0052 0.8014 +- 0.0046    974.0 +- 0.0
           Memory B cell 0.8896 +- 0.0025 0.9506 +- 0.003 0.9191 +- 0.0021    897.0 +- 0.0
                 NK cell 0.972 +- 0.0028 0.7531 +- 0.0063 0.8487 +- 0.0046   2580.0 +- 0.0
            Naive B cell  0.98 +- 0.0012 0.9521 +- 0.0014 0.9659 +- 0.0009   2227.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9946 +- 0.0086 0.9973 +- 0.0044     56.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.6719 +- 0.0118 0.8037 +- 0.0085     57.0 +- 0.0
       T regulatory cell  0.715 +- 0.064 0.0287 +- 0.0023 0.0551 +- 0.0043    136.0 +- 0.0

                accuracy                                 0.8458 +- 0.0014  22420.0 +- 0.0
               macro avg 0.8708 +- 0.0051 0.7923 +- 0.0018 0.7986 +- 0.0016  22420.0 +- 0.0
            weighted avg 0.8946 +- 0.0015 0.8458 +- 0.0014 0.8581 +- 0.0014  22420.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.8343 +- 0.0051
50% Random Dropout Accuracy: 0.7249 +- 0.0227
90% Random Dropout Accuracy: 0.2907 +- 0.0425
92.5% Random Dropout Accuracy: 0.2391 +- 0.0331
95% Random Dropout Accuracy: 0.1935 +- 0.0224
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.8444 +- 0.0015
Feature importance dropout (0.5% features dropped) Accuracy score 0.8298 +- 0.0025
Feature importance dropout (1.0% features dropped) Accuracy score 0.8235 +- 0.0035
Feature importance dropout (2.0% features dropped) Accuracy score 0.7718 +- 0.0075


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.7861 +- 0.0034
50% Random Dropout Macro_F1: 0.6569 +- 0.0224
90% Random Dropout Macro_F1: 0.124 +- 0.0263
92.5% Random Dropout Macro_F1: 0.0881 +- 0.0214
95% Random Dropout Macro_F1: 0.0488 +- 0.0145
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.7974 +- 0.0017
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.7867 +- 0.0021
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.7757 +- 0.0022
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.7189 +- 0.0052



## Out of data distribution 

### Dataset Similarity + Accuracy 

Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.7032 +- 0.0049

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9204 +- 0.012 0.998 +- 0.0006 0.9576 +- 0.0064  12317.0 +- 0.0
          CD16+ Monocyte 0.9966 +- 0.0013 0.7157 +- 0.0552 0.832 +- 0.0369   1903.0 +- 0.0
    CD1C+ dendritic cell 0.9696 +- 0.0074 0.7887 +- 0.0229 0.8696 +- 0.0107   1079.0 +- 0.0
       CD4 Memory T cell 0.5847 +- 0.0296 0.5795 +- 0.0751 0.5781 +- 0.0222  14241.0 +- 0.0
        CD4 Naive T cell 0.7392 +- 0.0311 0.7605 +- 0.0668 0.7468 +- 0.0231  17151.0 +- 0.0
       CD8 Memory T cell 0.0828 +- 0.0084 0.0246 +- 0.0061 0.0376 +- 0.0081   6650.0 +- 0.0
        CD8 Naive T cell 0.9286 +- 0.0039 0.7622 +- 0.0413 0.8366 +- 0.0247   6516.0 +- 0.0
      Gamma-delta T cell 0.0866 +- 0.0065 0.2126 +- 0.0172 0.123 +- 0.0094   2271.0 +- 0.0
                    MAIT 0.4613 +- 0.0246 0.9754 +- 0.0045 0.6259 +- 0.0216   2889.0 +- 0.0
           Memory B cell 0.948 +- 0.0021 0.5852 +- 0.0241 0.7234 +- 0.0188   1395.0 +- 0.0
                 NK cell 0.9305 +- 0.0157  0.95 +- 0.0172 0.9399 +- 0.0028   5959.0 +- 0.0
            Naive B cell 0.8416 +- 0.0086 0.9906 +- 0.0005  0.91 +- 0.0049   3385.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9863 +- 0.002 0.9931 +- 0.001    930.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.9839 +- 0.002 0.9919 +- 0.001    584.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   1731.0 +- 0.0

                accuracy                                 0.7032 +- 0.0049  79001.0 +- 0.0
               macro avg 0.6993 +- 0.0021 0.6875 +- 0.0072 0.6777 +- 0.0049  79001.0 +- 0.0
            weighted avg 0.6917 +- 0.0046 0.7032 +- 0.0049 0.6878 +- 0.0045  79001.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.6929 +- 0.0055
50% Random Dropout Accuracy: 0.6044 +- 0.0175
90% Random Dropout Accuracy: 0.3077 +- 0.0426
92.5% Random Dropout Accuracy: 0.2594 +- 0.0208
95% Random Dropout Accuracy: 0.2431 +- 0.0149
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.7037 +- 0.0049
Feature importance dropout (0.5% features dropped) Accuracy score 0.7027 +- 0.0046
Feature importance dropout (1.0% features dropped) Accuracy score 0.6936 +- 0.0048
Feature importance dropout (2.0% features dropped) Accuracy score 0.6703 +- 0.0052


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.6623 +- 0.0086
50% Random Dropout Macro_F1: 0.5243 +- 0.0219
90% Random Dropout Macro_F1: 0.1091 +- 0.0329
92.5% Random Dropout Macro_F1: 0.0655 +- 0.0169
95% Random Dropout Macro_F1: 0.0456 +- 0.0102
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.6788 +- 0.0048
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.6741 +- 0.0049
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.6509 +- 0.0081
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.5412 +- 0.0112


