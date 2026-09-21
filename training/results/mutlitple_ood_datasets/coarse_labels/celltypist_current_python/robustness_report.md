# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8986 +- 0.0037

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9996 +- 0.0002      1.0 +- 0.0 0.9998 +- 0.0001   3129.0 +- 0.0
             CD4+ T cell 0.8983 +- 0.0085 0.8755 +- 0.013 0.8867 +- 0.0055   6465.0 +- 0.0
             CD8+ T cell 0.7839 +- 0.0084   0.898 +- 0.01 0.837 +- 0.0057   6401.0 +- 0.0
          Dendritic cell 0.9464 +- 0.0053 0.7794 +- 0.0096 0.8547 +- 0.0044    165.0 +- 0.0
                Monocyte 0.9949 +- 0.0004 0.998 +- 0.0002 0.9965 +- 0.0002   3648.0 +- 0.0
                 NK cell 0.9884 +- 0.0011 0.7017 +- 0.0196 0.8206 +- 0.013   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9393 +- 0.0125 0.9687 +- 0.0067     56.0 +- 0.0

                accuracy                                 0.8986 +- 0.0037  22446.0 +- 0.0
               macro avg 0.9445 +- 0.0018 0.8846 +- 0.0044 0.9091 +- 0.0032  22446.0 +- 0.0
            weighted avg 0.9065 +- 0.0032 0.8986 +- 0.0037 0.8985 +- 0.0037  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8797 +- 0.0058
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8984 +- 0.0037
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8855 +- 0.0041
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8857 +- 0.0037
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8506 +- 0.0044


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8782 +- 0.0062
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.909 +- 0.0031
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8959 +- 0.004
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8923 +- 0.0029
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8597 +- 0.006



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.8624 +- 0.0114

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9956 +- 0.0009   0.9988 +- 0.0 0.9972 +- 0.0005    866.0 +- 0.0
             CD4+ T cell 0.9644 +- 0.0064 0.7607 +- 0.0314 0.8501 +- 0.0179   4474.0 +- 0.0
             CD8+ T cell 0.6789 +- 0.0219  0.95 +- 0.0103 0.7916 +- 0.0122   2688.0 +- 0.0
          Dendritic cell 0.9262 +- 0.0049 0.8992 +- 0.0178 0.9124 +- 0.0084    120.0 +- 0.0
                Monocyte 0.9838 +- 0.0026 0.9903 +- 0.0008 0.9871 +- 0.0012    889.0 +- 0.0
                 NK cell 0.9897 +- 0.0025 0.8346 +- 0.0151 0.9055 +- 0.0081    876.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9686 +- 0.006 0.984 +- 0.0031     70.0 +- 0.0

                accuracy                                 0.8624 +- 0.0114   9983.0 +- 0.0
               macro avg 0.9341 +- 0.0026 0.9146 +- 0.0037 0.9183 +- 0.004   9983.0 +- 0.0
            weighted avg 0.894 +- 0.0038 0.8624 +- 0.0114 0.8659 +- 0.0111   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8445 +- 0.0119
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8609 +- 0.0115
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8481 +- 0.0095
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8419 +- 0.0091
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7904 +- 0.0076


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8619 +- 0.0122
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9177 +- 0.0041
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9077 +- 0.0034
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8524 +- 0.0103
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8213 +- 0.0131


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.7667 +- 0.0196

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9949 +- 0.0      1.0 +- 0.0   0.9974 +- 0.0    968.0 +- 0.0
             CD4+ T cell 0.9822 +- 0.0033 0.4949 +- 0.0477 0.6569 +- 0.0422   4371.0 +- 0.0
             CD8+ T cell 0.4812 +- 0.021 0.9799 +- 0.005 0.6451 +- 0.018   2141.0 +- 0.0
          Dendritic cell 0.955 +- 0.0046 0.9596 +- 0.0022 0.9573 +- 0.0023    146.0 +- 0.0
                Monocyte 0.9958 +- 0.0007 0.9961 +- 0.0004 0.996 +- 0.0004   1703.0 +- 0.0
                 NK cell 0.9942 +- 0.0019 0.8989 +- 0.0072 0.9441 +- 0.0041    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.865 +- 0.0129 0.9276 +- 0.0074     40.0 +- 0.0

                accuracy                                 0.7667 +- 0.0196   9998.0 +- 0.0
               macro avg 0.9148 +- 0.0027 0.8849 +- 0.0061 0.8749 +- 0.0084   9998.0 +- 0.0
            weighted avg 0.8789 +- 0.0033 0.7667 +- 0.0196 0.7686 +- 0.0222   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7703 +- 0.0216
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.7656 +- 0.0196
Feature importance dropout (0.5% features dropped) Accuracy score: 0.763 +- 0.0192
Feature importance dropout (1.0% features dropped) Accuracy score: 0.761 +- 0.0188
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7551 +- 0.0184


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8483 +- 0.0109
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8744 +- 0.0085
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8715 +- 0.0082
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8131 +- 0.0106
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8086 +- 0.0102


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.8542 +- 0.0113

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.999 +- 0.0006      1.0 +- 0.0 0.9995 +- 0.0003    764.0 +- 0.0
             CD4+ T cell 0.9888 +- 0.0022  0.6831 +- 0.03 0.8076 +- 0.0209   4116.0 +- 0.0
             CD8+ T cell 0.5057 +- 0.0197 0.9679 +- 0.0051 0.6641 +- 0.0165   1457.0 +- 0.0
          Dendritic cell  0.964 +- 0.003 0.8814 +- 0.0176 0.9208 +- 0.0093    167.0 +- 0.0
                Monocyte 0.991 +- 0.0012 0.9973 +- 0.0002 0.9942 +- 0.0005   2413.0 +- 0.0
                 NK cell 0.9851 +- 0.0026 0.9247 +- 0.0135 0.9539 +- 0.007   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0     0.95 +- 0.0   0.9744 +- 0.0     40.0 +- 0.0

                accuracy                                 0.8542 +- 0.0113   9997.0 +- 0.0
               macro avg 0.9191 +- 0.0029 0.9149 +- 0.0044 0.9021 +- 0.0053   9997.0 +- 0.0
            weighted avg 0.9189 +- 0.0025 0.8542 +- 0.0113 0.8642 +- 0.0107   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.849 +- 0.0149
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8519 +- 0.0115
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8473 +- 0.0112
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8435 +- 0.0106
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8502 +- 0.0111


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.863 +- 0.0119
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.901 +- 0.0053
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8972 +- 0.0049
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8526 +- 0.0121
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.85 +- 0.0122


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.8475 +- 0.0163

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9977 +- 0.0004      1.0 +- 0.0 0.9988 +- 0.0002    895.0 +- 0.0
             CD4+ T cell 0.9755 +- 0.0142 0.7332 +- 0.0674 0.8352 +- 0.0382   2315.0 +- 0.0
             CD8+ T cell 0.6104 +- 0.0316 0.9782 +- 0.015 0.751 +- 0.0194   2127.0 +- 0.0
          Dendritic cell      1.0 +- 0.0 0.709 +- 0.0317 0.8293 +- 0.0219    156.0 +- 0.0
                Monocyte 0.9757 +- 0.0018   0.9996 +- 0.0 0.9875 +- 0.0009   2614.0 +- 0.0
                 NK cell 0.9977 +- 0.0018 0.4563 +- 0.0368 0.6254 +- 0.0346   1363.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     46.0 +- 0.0

                accuracy                                 0.8475 +- 0.0163   9516.0 +- 0.0
               macro avg 0.9367 +- 0.0025 0.8395 +- 0.0088 0.861 +- 0.0098   9516.0 +- 0.0
            weighted avg 0.8997 +- 0.0037 0.8475 +- 0.0163 0.8443 +- 0.0165   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8165 +- 0.015
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8468 +- 0.0165
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8401 +- 0.0124
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8237 +- 0.0113
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8191 +- 0.0133


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.7953 +- 0.0151
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8606 +- 0.0099
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8569 +- 0.0076
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.837 +- 0.0073
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.7991 +- 0.0096


### OOD Dataset: All 

Baseline accuracy score: N/A

### Classification Report 

                               precision          recall        f1-score         support

                  B cell             N/A             N/A             N/A             N/A
             CD4+ T cell             N/A             N/A             N/A             N/A
             CD8+ T cell             N/A             N/A             N/A             N/A
          Dendritic cell             N/A             N/A             N/A             N/A
                Monocyte             N/A             N/A             N/A             N/A
                 NK cell             N/A             N/A             N/A             N/A
             Plasma cell             N/A             N/A             N/A             N/A

                accuracy                                             N/A             N/A
               macro avg             N/A             N/A             N/A             N/A
            weighted avg             N/A             N/A             N/A             N/A

### Further Robustness Evaluation with metric: Accuracy 



### Further Robustness Evaluation with metric: Macro_F1 



