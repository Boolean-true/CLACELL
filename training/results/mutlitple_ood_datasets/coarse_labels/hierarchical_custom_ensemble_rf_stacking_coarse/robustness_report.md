# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9314 +- 0.0024

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   1.0 +- 0.0001      1.0 +- 0.0   1.0 +- 0.0001   3129.0 +- 0.0
             CD4+ T cell 0.9013 +- 0.0066 0.9605 +- 0.0016  0.93 +- 0.0031   6465.0 +- 0.0
             CD8+ T cell 0.8737 +- 0.003 0.8954 +- 0.0078 0.8844 +- 0.0045   6401.0 +- 0.0
          Dendritic cell 0.9442 +- 0.0044  0.82 +- 0.0041 0.8777 +- 0.0031    165.0 +- 0.0
                Monocyte 0.9968 +- 0.0002 0.9978 +- 0.0002 0.9973 +- 0.0001   3648.0 +- 0.0
                 NK cell 0.9948 +- 0.0015 0.7776 +- 0.0081 0.8729 +- 0.0051   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9607 +- 0.0075 0.9799 +- 0.0039     56.0 +- 0.0

                accuracy                                 0.9314 +- 0.0024  22446.0 +- 0.0
               macro avg 0.9587 +- 0.0016 0.916 +- 0.0022 0.9346 +- 0.0019  22446.0 +- 0.0
            weighted avg 0.934 +- 0.0023 0.9314 +- 0.0024 0.9309 +- 0.0025  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.921 +- 0.0033
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9314 +- 0.0024
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9214 +- 0.0029
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9204 +- 0.0029
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8751 +- 0.0016


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9269 +- 0.0025
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9346 +- 0.0019
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9291 +- 0.002
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.926 +- 0.0025
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9015 +- 0.0014



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.9192 +- 0.0025

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9977 +- 0.0   0.9988 +- 0.0   0.9983 +- 0.0    866.0 +- 0.0
             CD4+ T cell 0.9531 +- 0.0038 0.8752 +- 0.0052 0.9125 +- 0.0028   4474.0 +- 0.0
             CD8+ T cell 0.8092 +- 0.0057 0.9247 +- 0.0063 0.8631 +- 0.0042   2688.0 +- 0.0
          Dendritic cell 0.8976 +- 0.0034 0.9858 +- 0.0056 0.9396 +- 0.0026    120.0 +- 0.0
                Monocyte 0.9979 +- 0.001 0.9848 +- 0.0006 0.9913 +- 0.0005    889.0 +- 0.0
                 NK cell 0.9887 +- 0.0041 0.9682 +- 0.0067 0.9783 +- 0.0035    876.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0

                accuracy                                 0.9192 +- 0.0025   9983.0 +- 0.0
               macro avg 0.9471 +- 0.0015 0.9584 +- 0.0018 0.9516 +- 0.0014   9983.0 +- 0.0
            weighted avg 0.9249 +- 0.0023 0.9192 +- 0.0025 0.9202 +- 0.0025   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9101 +- 0.0118
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9191 +- 0.0025
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9016 +- 0.0056
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9008 +- 0.006
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8075 +- 0.0022


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9455 +- 0.006
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9516 +- 0.0014
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9433 +- 0.0028
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.943 +- 0.003
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8951 +- 0.0021


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8623 +- 0.0019

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9969 +- 0.0      1.0 +- 0.0   0.9985 +- 0.0    968.0 +- 0.0
             CD4+ T cell 0.9769 +- 0.0012 0.7104 +- 0.0054 0.8226 +- 0.0032   4371.0 +- 0.0
             CD8+ T cell 0.6161 +- 0.0038 0.9631 +- 0.002 0.7515 +- 0.0023   2141.0 +- 0.0
          Dendritic cell 0.9596 +- 0.0001 0.9774 +- 0.0033 0.9684 +- 0.0017    146.0 +- 0.0
                Monocyte 0.9981 +- 0.0003   0.9965 +- 0.0 0.9973 +- 0.0001   1703.0 +- 0.0
                 NK cell 0.9909 +- 0.0016 0.9692 +- 0.004 0.9799 +- 0.0022    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0    0.925 +- 0.0    0.961 +- 0.0     40.0 +- 0.0

                accuracy                                 0.8623 +- 0.0019   9998.0 +- 0.0
               macro avg 0.9341 +- 0.0005 0.9345 +- 0.0007 0.9256 +- 0.0008   9998.0 +- 0.0
            weighted avg 0.9059 +- 0.0004 0.8623 +- 0.0019 0.8667 +- 0.0019   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.871 +- 0.0045
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8623 +- 0.0019
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8586 +- 0.0012
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8585 +- 0.0011
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8172 +- 0.0037


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9258 +- 0.0027
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9256 +- 0.0008
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9234 +- 0.0005
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9233 +- 0.0006
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9011 +- 0.0018


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.9363 +- 0.0033

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0    764.0 +- 0.0
             CD4+ T cell 0.9912 +- 0.0007 0.8632 +- 0.0079 0.9227 +- 0.0046   4116.0 +- 0.0
             CD8+ T cell 0.7112 +- 0.0114 0.9749 +- 0.0021 0.8224 +- 0.0078   1457.0 +- 0.0
          Dendritic cell 0.9004 +- 0.0068 0.9796 +- 0.0031 0.9384 +- 0.0039    167.0 +- 0.0
                Monocyte 0.9985 +- 0.0002 0.9921 +- 0.0006 0.9953 +- 0.0003   2413.0 +- 0.0
                 NK cell 0.9944 +- 0.0016 0.9862 +- 0.0032 0.9903 +- 0.0013   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                 0.9363 +- 0.0033   9997.0 +- 0.0
               macro avg 0.9422 +- 0.0022 0.9709 +- 0.0014 0.9527 +- 0.002   9997.0 +- 0.0
            weighted avg 0.9517 +- 0.0018 0.9363 +- 0.0033 0.9391 +- 0.0031   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9383 +- 0.0046
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9363 +- 0.0034
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9343 +- 0.0033
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9337 +- 0.0034
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9274 +- 0.0036


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9522 +- 0.0032
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9527 +- 0.0021
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9512 +- 0.0021
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9505 +- 0.0022
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9448 +- 0.0021


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.9435 +- 0.0036

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9989 +- 0.0      1.0 +- 0.0   0.9994 +- 0.0    895.0 +- 0.0
             CD4+ T cell 0.987 +- 0.0017 0.877 +- 0.0085 0.9287 +- 0.0044   2315.0 +- 0.0
             CD8+ T cell 0.8142 +- 0.0108 0.9871 +- 0.0021 0.8923 +- 0.0066   2127.0 +- 0.0
          Dendritic cell 0.9837 +- 0.0034 0.8878 +- 0.0034 0.9333 +- 0.0027    156.0 +- 0.0
                Monocyte 0.9908 +- 0.0003 0.9986 +- 0.0003 0.9947 +- 0.0002   2614.0 +- 0.0
                 NK cell 0.9973 +- 0.003 0.8505 +- 0.0271 0.9178 +- 0.016   1363.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     46.0 +- 0.0

                accuracy                                 0.9435 +- 0.0036   9516.0 +- 0.0
               macro avg 0.9674 +- 0.0015 0.943 +- 0.0037 0.9523 +- 0.003   9516.0 +- 0.0
            weighted avg 0.952 +- 0.0025 0.9435 +- 0.0036 0.9442 +- 0.0036   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9312 +- 0.0044
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9435 +- 0.0036
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9326 +- 0.0056
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9268 +- 0.0063
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9257 +- 0.0065


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9401 +- 0.0036
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9523 +- 0.003
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9457 +- 0.0043
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9408 +- 0.0049
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9398 +- 0.0052


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



