# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9016 +- 0.0008

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte  0.99 +- 0.0002 0.9968 +- 0.0001 0.9934 +- 0.0001   3456.0 +- 0.0
          CD16+ Monocyte 0.9543 +- 0.0001 0.9736 +- 0.0016 0.9638 +- 0.0008    193.0 +- 0.0
    CD1C+ dendritic cell      1.0 +- 0.0   0.7593 +- 0.0   0.8632 +- 0.0    108.0 +- 0.0
       CD4 Memory T cell 0.8877 +- 0.0043 0.9348 +- 0.0051 0.9106 +- 0.0009   2888.0 +- 0.0
        CD4 Naive T cell 0.9337 +- 0.0013 0.8991 +- 0.0006 0.9161 +- 0.0007   3439.0 +- 0.0
       CD8 Memory T cell 0.4353 +- 0.0056 0.7023 +- 0.0102 0.5374 +- 0.0063    818.0 +- 0.0
        CD8 Naive T cell 0.9355 +- 0.0008 0.868 +- 0.0018 0.9004 +- 0.0011   2047.0 +- 0.0
      Gamma-delta T cell 0.9428 +- 0.0009 0.8937 +- 0.0025 0.9176 +- 0.0011   2544.0 +- 0.0
                    MAIT 0.6966 +- 0.0103 0.9219 +- 0.002 0.7935 +- 0.0062    974.0 +- 0.0
           Memory B cell 0.8562 +- 0.0013 0.9766 +- 0.0011 0.9125 +- 0.001    897.0 +- 0.0
                 NK cell    0.994 +- 0.0 0.8302 +- 0.002 0.9047 +- 0.0012   2580.0 +- 0.0
            Naive B cell 0.991 +- 0.0004 0.9355 +- 0.0004 0.9624 +- 0.0003   2227.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.8304 +- 0.0126 0.9073 +- 0.0075     56.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.3965 +- 0.0237 0.5675 +- 0.0243     57.0 +- 0.0
       T regulatory cell 0.3673 +- 0.0368 0.1037 +- 0.0182 0.1603 +- 0.0207    136.0 +- 0.0

                accuracy                                 0.9016 +- 0.0008  22420.0 +- 0.0
               macro avg 0.8656 +- 0.0026 0.8015 +- 0.0027 0.814 +- 0.0027  22420.0 +- 0.0
            weighted avg 0.9161 +- 0.0003 0.9016 +- 0.0008 0.9047 +- 0.0006  22420.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.8813 +- 0.0058
50% Random Dropout Accuracy: 0.7501 +- 0.0163
90% Random Dropout Accuracy: 0.3876 +- 0.0221
92.5% Random Dropout Accuracy: 0.3279 +- 0.0265
95% Random Dropout Accuracy: 0.2952 +- 0.0385
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.898 +- 0.0007
Feature importance dropout (0.5% features dropped) Accuracy score 0.875 +- 0.0011
Feature importance dropout (1.0% features dropped) Accuracy score 0.8547 +- 0.001
Feature importance dropout (2.0% features dropped) Accuracy score 0.6376 +- 0.0118


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.7895 +- 0.0064
50% Random Dropout Macro_F1: 0.6126 +- 0.0242
90% Random Dropout Macro_F1: 0.2181 +- 0.0159
92.5% Random Dropout Macro_F1: 0.1771 +- 0.0232
95% Random Dropout Macro_F1: 0.1488 +- 0.0154
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.8128 +- 0.0028
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.7981 +- 0.0026
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.7606 +- 0.0022
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.5045 +- 0.0112



## Out of data distribution 

### Dataset Similarity + Accuracy 

Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.5785 +- 0.0049

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9646 +- 0.0032 0.9817 +- 0.0014 0.9731 +- 0.001  12317.0 +- 0.0
          CD16+ Monocyte  0.6797 +- 0.02 0.9898 +- 0.001 0.8058 +- 0.0138   1903.0 +- 0.0
    CD1C+ dendritic cell 0.7203 +- 0.012 0.9599 +- 0.0028 0.8229 +- 0.0073   1079.0 +- 0.0
       CD4 Memory T cell  0.3964 +- 0.01 0.5513 +- 0.0281 0.4611 +- 0.0166  14241.0 +- 0.0
        CD4 Naive T cell 0.9806 +- 0.0017 0.0524 +- 0.0016 0.0994 +- 0.0029  17151.0 +- 0.0
       CD8 Memory T cell 0.0135 +- 0.0042   0.0003 +- 0.0 0.0006 +- 0.0001   6650.0 +- 0.0
        CD8 Naive T cell 0.6054 +- 0.0088 0.9822 +- 0.001 0.7491 +- 0.0064   6516.0 +- 0.0
      Gamma-delta T cell 0.1176 +- 0.0021 0.337 +- 0.0051 0.1744 +- 0.003   2271.0 +- 0.0
                    MAIT 0.4973 +- 0.0388 0.971 +- 0.0077 0.6567 +- 0.0344   2889.0 +- 0.0
           Memory B cell 0.6781 +- 0.0479 0.6586 +- 0.005 0.6675 +- 0.0219   1395.0 +- 0.0
                 NK cell 0.8598 +- 0.0121 0.9892 +- 0.0034 0.9199 +- 0.0054   5959.0 +- 0.0
            Naive B cell 0.8165 +- 0.0077   0.9891 +- 0.0 0.8945 +- 0.0046   3385.0 +- 0.0
             Plasma cell 0.7408 +- 0.0227 0.9905 +- 0.0005 0.8475 +- 0.0148    930.0 +- 0.0
Plasmacytoid dendritic cell 0.7482 +- 0.0103 0.9894 +- 0.0018 0.852 +- 0.0062    584.0 +- 0.0
       T regulatory cell 0.0718 +- 0.0027 0.1763 +- 0.0222 0.1017 +- 0.0052   1731.0 +- 0.0

                accuracy                                 0.5785 +- 0.0049  79001.0 +- 0.0
               macro avg 0.5927 +- 0.0048 0.7079 +- 0.0014 0.6018 +- 0.0017  79001.0 +- 0.0
            weighted avg 0.6612 +- 0.0011 0.5785 +- 0.0049 0.5159 +- 0.0023  79001.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.5751 +- 0.0088
50% Random Dropout Accuracy: 0.5187 +- 0.0087
90% Random Dropout Accuracy: 0.3051 +- 0.026
92.5% Random Dropout Accuracy: 0.272 +- 0.0224
95% Random Dropout Accuracy: 0.2499 +- 0.0241
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.5771 +- 0.0047
Feature importance dropout (0.5% features dropped) Accuracy score 0.5892 +- 0.004
Feature importance dropout (1.0% features dropped) Accuracy score 0.5843 +- 0.0048
Feature importance dropout (2.0% features dropped) Accuracy score 0.5294 +- 0.0083


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.5912 +- 0.0061
50% Random Dropout Macro_F1: 0.4869 +- 0.0111
90% Random Dropout Macro_F1: 0.2141 +- 0.0109
92.5% Random Dropout Macro_F1: 0.1863 +- 0.0176
95% Random Dropout Macro_F1: 0.1623 +- 0.0163
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.5994 +- 0.0018
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.602 +- 0.0017
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.592 +- 0.0016
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.5066 +- 0.0114


