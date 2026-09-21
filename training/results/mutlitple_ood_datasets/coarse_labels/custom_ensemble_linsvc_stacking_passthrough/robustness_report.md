# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8847 +- 0.0029

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0   0.9997 +- 0.0   0.9998 +- 0.0   3129.0 +- 0.0
             CD4+ T cell 0.9046 +- 0.0035 0.7829 +- 0.0158 0.8393 +- 0.0077   6465.0 +- 0.0
             CD8+ T cell 0.7451 +- 0.0082 0.9131 +- 0.0049 0.8205 +- 0.0031   6401.0 +- 0.0
          Dendritic cell 0.9616 +- 0.0035  0.82 +- 0.0029 0.8852 +- 0.0024    165.0 +- 0.0
                Monocyte 0.9964 +- 0.0003 0.9985 +- 0.0001 0.9975 +- 0.0001   3648.0 +- 0.0
                 NK cell 0.9831 +- 0.0011 0.7706 +- 0.0034 0.864 +- 0.0021   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     56.0 +- 0.0

                accuracy                                 0.8847 +- 0.0029  22446.0 +- 0.0
               macro avg 0.9415 +- 0.0007 0.8978 +- 0.0011 0.9152 +- 0.0012  22446.0 +- 0.0
            weighted avg 0.897 +- 0.0014 0.8847 +- 0.0029 0.8856 +- 0.0029  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8796 +- 0.0024
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8844 +- 0.003
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8755 +- 0.0027
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8755 +- 0.0032
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8499 +- 0.0027


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9092 +- 0.0028
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.915 +- 0.0012
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.908 +- 0.0012
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9071 +- 0.0016
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8972 +- 0.0013



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.8711 +- 0.0067

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9973 +- 0.0006   0.9988 +- 0.0 0.9981 +- 0.0003    866.0 +- 0.0
             CD4+ T cell 0.9563 +- 0.0023 0.7667 +- 0.0174 0.851 +- 0.0099   4474.0 +- 0.0
             CD8+ T cell 0.7001 +- 0.0143  0.93 +- 0.0044 0.7987 +- 0.0078   2688.0 +- 0.0
          Dendritic cell 0.9069 +- 0.003   0.9583 +- 0.0 0.9319 +- 0.0016    120.0 +- 0.0
                Monocyte 0.9922 +- 0.0008 0.9867 +- 0.0005 0.9895 +- 0.0004    889.0 +- 0.0
                 NK cell 0.9601 +- 0.0014 0.9603 +- 0.0014 0.9602 +- 0.0008    876.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0

                accuracy                                 0.8711 +- 0.0067   9983.0 +- 0.0
               macro avg 0.9284 +- 0.0019 0.9389 +- 0.0019 0.9297 +- 0.0026   9983.0 +- 0.0
            weighted avg  0.894 +- 0.003 0.8711 +- 0.0067 0.8734 +- 0.0066   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8715 +- 0.0117
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8702 +- 0.007
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8584 +- 0.0063
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8583 +- 0.0066
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8039 +- 0.0058


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9275 +- 0.005
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9291 +- 0.0027
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9238 +- 0.0024
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9233 +- 0.0026
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8964 +- 0.0019


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.7701 +- 0.0063

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9959 +- 0.0 0.9993 +- 0.0005 0.9976 +- 0.0002    968.0 +- 0.0
             CD4+ T cell 0.9761 +- 0.0014 0.4959 +- 0.0154 0.6575 +- 0.0133   4371.0 +- 0.0
             CD8+ T cell 0.4837 +- 0.007 0.9688 +- 0.0024 0.6452 +- 0.0058   2141.0 +- 0.0
          Dendritic cell   0.9786 +- 0.0   0.9384 +- 0.0    0.958 +- 0.0    146.0 +- 0.0
                Monocyte   0.9947 +- 0.0   0.9982 +- 0.0   0.9965 +- 0.0   1703.0 +- 0.0
                 NK cell 0.9784 +- 0.0013 0.9814 +- 0.0008 0.9799 +- 0.0006    629.0 +- 0.0
             Plasma cell 0.9811 +- 0.0131      0.9 +- 0.0 0.9388 +- 0.0059     40.0 +- 0.0

                accuracy                                 0.7701 +- 0.0063   9998.0 +- 0.0
               macro avg 0.9126 +- 0.002 0.8974 +- 0.002 0.8819 +- 0.0029   9998.0 +- 0.0
            weighted avg 0.8759 +- 0.001 0.7701 +- 0.0063 0.7713 +- 0.0071   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7808 +- 0.0094
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.7699 +- 0.0063
Feature importance dropout (0.5% features dropped) Accuracy score: 0.7673 +- 0.0061
Feature importance dropout (1.0% features dropped) Accuracy score: 0.7667 +- 0.0061
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7591 +- 0.007


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8838 +- 0.0035
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8818 +- 0.0029
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8808 +- 0.0028
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8814 +- 0.0027
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8775 +- 0.0029


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.8717 +- 0.0075

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0    764.0 +- 0.0
             CD4+ T cell 0.9875 +- 0.0008 0.7115 +- 0.0189 0.8269 +- 0.0124   4116.0 +- 0.0
             CD8+ T cell 0.5381 +- 0.0159 0.9549 +- 0.0028 0.6882 +- 0.0123   1457.0 +- 0.0
          Dendritic cell   0.9623 +- 0.0   0.9162 +- 0.0   0.9387 +- 0.0    167.0 +- 0.0
                Monocyte   0.9942 +- 0.0   0.9971 +- 0.0   0.9957 +- 0.0   2413.0 +- 0.0
                 NK cell 0.972 +- 0.0011 0.9915 +- 0.0014 0.9817 +- 0.0008   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                 0.8717 +- 0.0075   9997.0 +- 0.0
               macro avg 0.922 +- 0.0021 0.9387 +- 0.0025 0.9187 +- 0.0036   9997.0 +- 0.0
            weighted avg 0.9226 +- 0.002 0.8717 +- 0.0075 0.8793 +- 0.007   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.88 +- 0.0072
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8702 +- 0.0075
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8685 +- 0.0076
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8679 +- 0.0077
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8829 +- 0.0062


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9202 +- 0.0033
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.918 +- 0.0036
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9169 +- 0.0035
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9165 +- 0.0036
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9216 +- 0.003


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.9007 +- 0.0043

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9989 +- 0.0      1.0 +- 0.0   0.9994 +- 0.0    895.0 +- 0.0
             CD4+ T cell 0.8977 +- 0.0033   0.8 +- 0.0203 0.8459 +- 0.0109   2315.0 +- 0.0
             CD8+ T cell 0.7683 +- 0.0147 0.8258 +- 0.0047 0.7959 +- 0.007   2127.0 +- 0.0
          Dendritic cell   0.9925 +- 0.0 0.8455 +- 0.002 0.9131 +- 0.0012    156.0 +- 0.0
                Monocyte 0.987 +- 0.0002   0.9996 +- 0.0 0.9933 +- 0.0001   2614.0 +- 0.0
                 NK cell 0.8845 +- 0.0025 0.9364 +- 0.0022 0.9097 +- 0.0008   1363.0 +- 0.0
             Plasma cell 0.9915 +- 0.011      1.0 +- 0.0 0.9957 +- 0.0056     46.0 +- 0.0

                accuracy                                 0.9007 +- 0.0043   9516.0 +- 0.0
               macro avg 0.9315 +- 0.0025 0.9153 +- 0.0024 0.9219 +- 0.0026   9516.0 +- 0.0
            weighted avg 0.9029 +- 0.0034 0.9007 +- 0.0043 0.9006 +- 0.0042   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8902 +- 0.0086
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9001 +- 0.0044
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8777 +- 0.004
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8756 +- 0.0038
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8761 +- 0.0045


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.912 +- 0.006
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9211 +- 0.0027
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9067 +- 0.0023
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9054 +- 0.0022
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9054 +- 0.0025


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



