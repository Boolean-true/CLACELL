# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9097 +- 0.0007

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9994 +- 0.0001      1.0 +- 0.0 0.9997 +- 0.0001   3129.0 +- 0.0
             CD4+ T cell 0.8875 +- 0.0009 0.9124 +- 0.0024 0.8997 +- 0.0011   6465.0 +- 0.0
             CD8+ T cell 0.8199 +- 0.0021 0.8832 +- 0.0013 0.8504 +- 0.0012   6401.0 +- 0.0
          Dendritic cell 0.9371 +- 0.0052 0.8121 +- 0.004 0.8701 +- 0.0026    165.0 +- 0.0
                Monocyte 0.997 +- 0.0002 0.9975 +- 0.0003 0.9972 +- 0.0002   3648.0 +- 0.0
                 NK cell 0.9924 +- 0.0011 0.7411 +- 0.0035 0.8485 +- 0.0024   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0  0.95 +- 0.0075 0.9743 +- 0.0039     56.0 +- 0.0

                accuracy                                 0.9097 +- 0.0007  22446.0 +- 0.0
               macro avg 0.9476 +- 0.0009 0.8995 +- 0.0014   0.92 +- 0.001  22446.0 +- 0.0
            weighted avg 0.9143 +- 0.0006 0.9097 +- 0.0007 0.9095 +- 0.0007  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9013 +- 0.0035
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9098 +- 0.0008
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8952 +- 0.0009
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8959 +- 0.0008
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8921 +- 0.001


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9106 +- 0.0043
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.92 +- 0.001
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9088 +- 0.0009
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9094 +- 0.0008
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9037 +- 0.0028



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.87 +- 0.0034

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9967 +- 0.0004   0.9988 +- 0.0 0.9978 +- 0.0002    866.0 +- 0.0
             CD4+ T cell 0.9537 +- 0.005 0.7867 +- 0.0106 0.8621 +- 0.0047   4474.0 +- 0.0
             CD8+ T cell 0.6954 +- 0.0087  0.935 +- 0.008 0.7975 +- 0.0035   2688.0 +- 0.0
          Dendritic cell 0.9251 +- 0.0081 0.935 +- 0.0066   0.93 +- 0.004    120.0 +- 0.0
                Monocyte 0.9905 +- 0.0013  0.99 +- 0.0011 0.9903 +- 0.0006    889.0 +- 0.0
                 NK cell 0.9955 +- 0.0007 0.8296 +- 0.0094 0.905 +- 0.0056    876.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0

                accuracy                                  0.87 +- 0.0034   9983.0 +- 0.0
               macro avg 0.9346 +- 0.0011 0.9209 +- 0.002 0.923 +- 0.0017   9983.0 +- 0.0
            weighted avg 0.8947 +- 0.0013  0.87 +- 0.0034 0.8733 +- 0.0032   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8637 +- 0.0092
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8695 +- 0.0034
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8526 +- 0.0035
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8456 +- 0.0038
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8449 +- 0.0026


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9137 +- 0.0051
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9228 +- 0.0017
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9101 +- 0.0023
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9013 +- 0.003
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9025 +- 0.0027


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8287 +- 0.0036

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9959 +- 0.0      1.0 +- 0.0   0.9979 +- 0.0    968.0 +- 0.0
             CD4+ T cell 0.9705 +- 0.002 0.645 +- 0.0079 0.775 +- 0.0058   4371.0 +- 0.0
             CD8+ T cell 0.561 +- 0.0057 0.9592 +- 0.0027 0.7079 +- 0.0046   2141.0 +- 0.0
          Dendritic cell 0.965 +- 0.0004 0.9432 +- 0.0121 0.9539 +- 0.0064    146.0 +- 0.0
                Monocyte 0.9949 +- 0.0012   0.9971 +- 0.0 0.996 +- 0.0006   1703.0 +- 0.0
                 NK cell 0.9969 +- 0.0007 0.9102 +- 0.0057 0.9515 +- 0.0031    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0      0.9 +- 0.0   0.9474 +- 0.0     40.0 +- 0.0

                accuracy                                 0.8287 +- 0.0036   9998.0 +- 0.0
               macro avg 0.9263 +- 0.0008 0.9078 +- 0.002 0.9042 +- 0.0017   9998.0 +- 0.0
            weighted avg 0.8911 +- 0.0015 0.8287 +- 0.0036 0.8343 +- 0.0036   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8342 +- 0.0055
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8273 +- 0.0036
Feature importance dropout (0.5% features dropped) Accuracy score: 0.821 +- 0.0036
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8193 +- 0.0037
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8274 +- 0.0031


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9021 +- 0.0037
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9036 +- 0.0018
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8982 +- 0.0019
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8939 +- 0.0019
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8986 +- 0.0017


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.861 +- 0.0088

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0    764.0 +- 0.0
             CD4+ T cell 0.9849 +- 0.0015 0.6897 +- 0.0216 0.8111 +- 0.0145   4116.0 +- 0.0
             CD8+ T cell 0.5161 +- 0.0167 0.9663 +- 0.0045 0.6727 +- 0.0133   1457.0 +- 0.0
          Dendritic cell 0.9613 +- 0.0025 0.9353 +- 0.0146 0.9481 +- 0.007    167.0 +- 0.0
                Monocyte 0.9955 +- 0.001 0.997 +- 0.0002 0.9963 +- 0.0005   2413.0 +- 0.0
                 NK cell 0.9942 +- 0.0019 0.9569 +- 0.005 0.9752 +- 0.0026   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                 0.861 +- 0.0088   9997.0 +- 0.0
               macro avg 0.9217 +- 0.0023 0.935 +- 0.0042 0.9148 +- 0.0047   9997.0 +- 0.0
            weighted avg 0.9209 +- 0.0022 0.861 +- 0.0088 0.8702 +- 0.0081   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.863 +- 0.0084
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8585 +- 0.009
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8552 +- 0.0092
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8511 +- 0.0093
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8657 +- 0.0101


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9093 +- 0.0049
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9135 +- 0.0048
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9112 +- 0.0049
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9073 +- 0.005
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9142 +- 0.0052


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.9187 +- 0.0034

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9989 +- 0.0      1.0 +- 0.0   0.9994 +- 0.0    895.0 +- 0.0
             CD4+ T cell 0.9613 +- 0.005 0.847 +- 0.0099 0.9005 +- 0.0037   2315.0 +- 0.0
             CD8+ T cell 0.7583 +- 0.011 0.9599 +- 0.006 0.8472 +- 0.005   2127.0 +- 0.0
          Dendritic cell 0.9992 +- 0.0024 0.8455 +- 0.0077 0.916 +- 0.0046    156.0 +- 0.0
                Monocyte 0.9886 +- 0.0004 0.9996 +- 0.0001 0.9941 +- 0.0002   2614.0 +- 0.0
                 NK cell 0.9917 +- 0.0032 0.7731 +- 0.0197 0.8687 +- 0.0118   1363.0 +- 0.0
             Plasma cell 0.9407 +- 0.0062      1.0 +- 0.0 0.9695 +- 0.0033     46.0 +- 0.0

                accuracy                                 0.9187 +- 0.0034   9516.0 +- 0.0
               macro avg 0.9484 +- 0.0012 0.9179 +- 0.0034 0.9279 +- 0.0028   9516.0 +- 0.0
            weighted avg 0.9318 +- 0.0015 0.9187 +- 0.0034 0.9196 +- 0.0033   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9136 +- 0.0097
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9182 +- 0.0034
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9077 +- 0.0027
Feature importance dropout (1.0% features dropped) Accuracy score: 0.887 +- 0.0035
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8884 +- 0.0038


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9222 +- 0.01
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9276 +- 0.0028
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9216 +- 0.0021
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9037 +- 0.0033
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9048 +- 0.0037


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



