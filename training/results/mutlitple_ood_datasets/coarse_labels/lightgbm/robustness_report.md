# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9387 +- 0.0012

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9997 +- 0.0001 0.9999 +- 0.0002 0.9998 +- 0.0001   3129.0 +- 0.0
             CD4+ T cell 0.9535 +- 0.003 0.9426 +- 0.002 0.948 +- 0.0013   6465.0 +- 0.0
             CD8+ T cell 0.8533 +- 0.0025 0.9562 +- 0.0031 0.9018 +- 0.002   6401.0 +- 0.0
          Dendritic cell 0.9366 +- 0.0078 0.8036 +- 0.0118 0.8649 +- 0.0059    165.0 +- 0.0
                Monocyte 0.9966 +- 0.0003 0.9973 +- 0.0003 0.9969 +- 0.0001   3648.0 +- 0.0
                 NK cell 0.9975 +- 0.0005 0.7368 +- 0.0068 0.8476 +- 0.0045   2582.0 +- 0.0
             Plasma cell 0.9982 +- 0.0057 0.9536 +- 0.0359  0.975 +- 0.019     56.0 +- 0.0

                accuracy                                 0.9387 +- 0.0012  22446.0 +- 0.0
               macro avg 0.9622 +- 0.0016 0.9128 +- 0.0065 0.9334 +- 0.0033  22446.0 +- 0.0
            weighted avg 0.9434 +- 0.0011 0.9387 +- 0.0012 0.9379 +- 0.0013  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9267 +- 0.0049
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9387 +- 0.0012
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9341 +- 0.0015
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9325 +- 0.0015
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8721 +- 0.0016


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9167 +- 0.0083
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9334 +- 0.0033
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9302 +- 0.0032
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9289 +- 0.0039
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8925 +- 0.0057



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.8992 +- 0.0023

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9962 +- 0.0008   0.9988 +- 0.0 0.9975 +- 0.0004    866.0 +- 0.0
             CD4+ T cell 0.9365 +- 0.0022 0.8503 +- 0.0067 0.8913 +- 0.0031   4474.0 +- 0.0
             CD8+ T cell 0.7706 +- 0.0069 0.9013 +- 0.0039 0.8308 +- 0.0032   2688.0 +- 0.0
          Dendritic cell 0.9162 +- 0.008 0.9458 +- 0.0143 0.9307 +- 0.0054    120.0 +- 0.0
                Monocyte 0.9938 +- 0.0013 0.9883 +- 0.0013 0.991 +- 0.0006    889.0 +- 0.0
                 NK cell 0.9919 +- 0.0006 0.941 +- 0.0065 0.9658 +- 0.0034    876.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0

                accuracy                                 0.8992 +- 0.0023   9983.0 +- 0.0
               macro avg 0.9415 +- 0.0013 0.9424 +- 0.0019 0.9408 +- 0.0011   9983.0 +- 0.0
            weighted avg 0.907 +- 0.0015 0.8992 +- 0.0023 0.9007 +- 0.0022   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8844 +- 0.0066
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.899 +- 0.0023
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8761 +- 0.0025
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8754 +- 0.0027
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7865 +- 0.0037


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9231 +- 0.0068
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9407 +- 0.0011
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9295 +- 0.001
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9287 +- 0.0013
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8826 +- 0.0016


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8294 +- 0.0022

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.996 +- 0.0003 0.9987 +- 0.0009 0.9973 +- 0.0005    968.0 +- 0.0
             CD4+ T cell 0.966 +- 0.0014 0.6444 +- 0.0053 0.7731 +- 0.0036   4371.0 +- 0.0
             CD8+ T cell 0.5628 +- 0.0035 0.952 +- 0.0021 0.7074 +- 0.0025   2141.0 +- 0.0
          Dendritic cell 0.9616 +- 0.0046 0.9425 +- 0.0074 0.9519 +- 0.0036    146.0 +- 0.0
                Monocyte 0.9947 +- 0.0005 0.9968 +- 0.0004 0.9957 +- 0.0002   1703.0 +- 0.0
                 NK cell 0.9935 +- 0.0012 0.9523 +- 0.0033 0.9725 +- 0.0015    629.0 +- 0.0
             Plasma cell 0.9784 +- 0.0114 0.9025 +- 0.0079 0.9389 +- 0.0062     40.0 +- 0.0

                accuracy                                 0.8294 +- 0.0022   9998.0 +- 0.0
               macro avg 0.9219 +- 0.0017 0.9127 +- 0.0022 0.9053 +- 0.0016   9998.0 +- 0.0
            weighted avg 0.8891 +- 0.0008 0.8294 +- 0.0022 0.8345 +- 0.0022   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8418 +- 0.0094
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8293 +- 0.0021
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8242 +- 0.0025
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8242 +- 0.0025
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7801 +- 0.0033


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9011 +- 0.0084
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9053 +- 0.0015
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9025 +- 0.0017
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9027 +- 0.0012
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8799 +- 0.0015


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.9272 +- 0.0053

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9999 +- 0.0004      1.0 +- 0.0 0.9999 +- 0.0002    764.0 +- 0.0
             CD4+ T cell 0.9882 +- 0.0008 0.8469 +- 0.0135 0.9121 +- 0.0077   4116.0 +- 0.0
             CD8+ T cell 0.6805 +- 0.0185 0.9693 +- 0.0026 0.7995 +- 0.0121   1457.0 +- 0.0
          Dendritic cell 0.9304 +- 0.0095 0.9677 +- 0.0076 0.9486 +- 0.0061    167.0 +- 0.0
                Monocyte 0.9977 +- 0.0004 0.9946 +- 0.0007 0.9961 +- 0.0004   2413.0 +- 0.0
                 NK cell 0.9959 +- 0.0005 0.9667 +- 0.0059 0.9811 +- 0.003   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9975 +- 0.0079 0.9987 +- 0.004     40.0 +- 0.0

                accuracy                                 0.9272 +- 0.0053   9997.0 +- 0.0
               macro avg 0.9418 +- 0.0019 0.9632 +- 0.0029 0.948 +- 0.0027   9997.0 +- 0.0
            weighted avg 0.9464 +- 0.0024 0.9272 +- 0.0053 0.9308 +- 0.0048   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9287 +- 0.0077
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9269 +- 0.0053
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9251 +- 0.0054
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9245 +- 0.0055
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9237 +- 0.0053


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9327 +- 0.0137
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9479 +- 0.0027
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9462 +- 0.0029
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9451 +- 0.0032
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9427 +- 0.0034


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.8773 +- 0.0139

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9985 +- 0.0005      1.0 +- 0.0 0.9993 +- 0.0003    895.0 +- 0.0
             CD4+ T cell 0.9818 +- 0.004 0.8163 +- 0.008 0.8914 +- 0.0056   2315.0 +- 0.0
             CD8+ T cell 0.6568 +- 0.0264 0.9849 +- 0.0036 0.7878 +- 0.0197   2127.0 +- 0.0
          Dendritic cell 0.9794 +- 0.0096 0.8519 +- 0.0088 0.9112 +- 0.0066    156.0 +- 0.0
                Monocyte 0.9888 +- 0.0008 0.9985 +- 0.0005 0.9937 +- 0.0004   2614.0 +- 0.0
                 NK cell      1.0 +- 0.0 0.4986 +- 0.0917 0.6609 +- 0.0828   1363.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     46.0 +- 0.0

                accuracy                                 0.8773 +- 0.0139   9516.0 +- 0.0
               macro avg 0.9436 +- 0.0052 0.8786 +- 0.0134 0.892 +- 0.0151   9516.0 +- 0.0
            weighted avg 0.9153 +- 0.0067 0.8773 +- 0.0139 0.8743 +- 0.0166   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8572 +- 0.0103
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8773 +- 0.0139
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8666 +- 0.0137
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8629 +- 0.0126
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8582 +- 0.0132


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8565 +- 0.0138
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.892 +- 0.0151
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8864 +- 0.015
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8824 +- 0.0141
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8795 +- 0.0144


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



