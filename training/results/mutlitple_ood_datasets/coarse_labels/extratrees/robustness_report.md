# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9188 +- 0.0011

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9998 +- 0.0002      1.0 +- 0.0 0.9999 +- 0.0001   3129.0 +- 0.0
             CD4+ T cell 0.8875 +- 0.003 0.966 +- 0.0007 0.9251 +- 0.0016   6465.0 +- 0.0
             CD8+ T cell 0.8486 +- 0.0008 0.8786 +- 0.0037 0.8633 +- 0.002   6401.0 +- 0.0
          Dendritic cell 0.9968 +- 0.0056 0.7491 +- 0.0077 0.8553 +- 0.0048    165.0 +- 0.0
                Monocyte 0.9941 +- 0.0004 0.9999 +- 0.0002 0.997 +- 0.0002   3648.0 +- 0.0
                 NK cell 0.9973 +- 0.0006 0.6969 +- 0.0013 0.8204 +- 0.0009   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9804 +- 0.0132  0.99 +- 0.0067     56.0 +- 0.0

                accuracy                                 0.9188 +- 0.0011  22446.0 +- 0.0
               macro avg 0.9606 +- 0.0011 0.8958 +- 0.0023 0.9216 +- 0.0013  22446.0 +- 0.0
            weighted avg 0.9231 +- 0.001 0.9188 +- 0.0011 0.9172 +- 0.0011  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9101 +- 0.0056
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9188 +- 0.001
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9056 +- 0.0015
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9046 +- 0.0016
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8651 +- 0.0016


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9102 +- 0.0046
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9216 +- 0.0013
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.914 +- 0.0015
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.912 +- 0.0013
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8836 +- 0.0015



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.9174 +- 0.0033

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9968 +- 0.0005   0.9988 +- 0.0 0.9978 +- 0.0002    866.0 +- 0.0
             CD4+ T cell 0.9402 +- 0.0052 0.8846 +- 0.0038 0.9116 +- 0.0038   4474.0 +- 0.0
             CD8+ T cell 0.8164 +- 0.0053 0.9046 +- 0.0085 0.8582 +- 0.0061   2688.0 +- 0.0
          Dendritic cell 0.9464 +- 0.0023 0.8967 +- 0.0125 0.9208 +- 0.0064    120.0 +- 0.0
                Monocyte 0.9871 +- 0.0017 0.9931 +- 0.0004 0.9901 +- 0.0008    889.0 +- 0.0
                 NK cell 0.9942 +- 0.0014 0.9654 +- 0.0026 0.9796 +- 0.001    876.0 +- 0.0
             Plasma cell 0.9855 +- 0.0001  0.97 +- 0.0045 0.9777 +- 0.0023     70.0 +- 0.0

                accuracy                                 0.9174 +- 0.0033   9983.0 +- 0.0
               macro avg 0.9524 +- 0.0013 0.9447 +- 0.0025 0.948 +- 0.0019   9983.0 +- 0.0
            weighted avg 0.9211 +- 0.0034 0.9174 +- 0.0033 0.9182 +- 0.0033   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9035 +- 0.0067
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9173 +- 0.0034
Feature importance dropout (0.5% features dropped) Accuracy score: 0.887 +- 0.0045
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8863 +- 0.0046
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8094 +- 0.0016


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9335 +- 0.004
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9479 +- 0.0019
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9332 +- 0.0022
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9326 +- 0.0023
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8919 +- 0.0013


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8642 +- 0.0021

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9961 +- 0.0004      1.0 +- 0.0 0.998 +- 0.0002    968.0 +- 0.0
             CD4+ T cell 0.9779 +- 0.0013  0.715 +- 0.005 0.826 +- 0.0034   4371.0 +- 0.0
             CD8+ T cell 0.6204 +- 0.004 0.9652 +- 0.002 0.7553 +- 0.003   2141.0 +- 0.0
          Dendritic cell 0.9767 +- 0.0044 0.9185 +- 0.0051 0.9467 +- 0.0027    146.0 +- 0.0
                Monocyte 0.993 +- 0.0004 0.9981 +- 0.0004 0.9956 +- 0.0002   1703.0 +- 0.0
                 NK cell 0.9938 +- 0.0007 0.9701 +- 0.0034 0.9818 +- 0.0018    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.905 +- 0.0105 0.9501 +- 0.0058     40.0 +- 0.0

                accuracy                                 0.8642 +- 0.0021   9998.0 +- 0.0
               macro avg 0.9369 +- 0.0006 0.9246 +- 0.0016 0.9219 +- 0.0012   9998.0 +- 0.0
            weighted avg 0.9068 +- 0.001 0.8642 +- 0.0021 0.8685 +- 0.0021   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8688 +- 0.0057
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8641 +- 0.0022
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8589 +- 0.0021
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8587 +- 0.0021
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8233 +- 0.0041


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9171 +- 0.0054
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9219 +- 0.0012
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9189 +- 0.0011
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9183 +- 0.0006
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9002 +- 0.0021


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.9347 +- 0.0034

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0    764.0 +- 0.0
             CD4+ T cell 0.9895 +- 0.0007 0.8595 +- 0.0082 0.9199 +- 0.0046   4116.0 +- 0.0
             CD8+ T cell 0.706 +- 0.0119 0.9727 +- 0.0019 0.8181 +- 0.0079   1457.0 +- 0.0
          Dendritic cell  0.974 +- 0.006 0.8976 +- 0.0044 0.9342 +- 0.0042    167.0 +- 0.0
                Monocyte 0.9929 +- 0.0003 0.9979 +- 0.0004 0.9954 +- 0.0003   2413.0 +- 0.0
                 NK cell 0.9967 +- 0.0005 0.9881 +- 0.0024 0.9924 +- 0.0012   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                 0.9347 +- 0.0034   9997.0 +- 0.0
               macro avg 0.9513 +- 0.0022 0.9594 +- 0.0014 0.9514 +- 0.0021   9997.0 +- 0.0
            weighted avg 0.9504 +- 0.0018 0.9347 +- 0.0034 0.9375 +- 0.0031   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9346 +- 0.0045
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9346 +- 0.0035
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9309 +- 0.0031
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9305 +- 0.0032
Feature importance dropout (2.0% features dropped) Accuracy score: 0.925 +- 0.0032


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9429 +- 0.0041
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9514 +- 0.0021
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9485 +- 0.0019
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.948 +- 0.0019
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9429 +- 0.0019


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.9287 +- 0.0041

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9989 +- 0.0      1.0 +- 0.0   0.9994 +- 0.0    895.0 +- 0.0
             CD4+ T cell 0.9864 +- 0.0027 0.8623 +- 0.0058 0.9202 +- 0.0036   2315.0 +- 0.0
             CD8+ T cell 0.7767 +- 0.0106 0.9876 +- 0.0027 0.8695 +- 0.0069   2127.0 +- 0.0
          Dendritic cell      1.0 +- 0.0 0.7487 +- 0.0131 0.8562 +- 0.0086    156.0 +- 0.0
                Monocyte 0.983 +- 0.0007   0.9996 +- 0.0 0.9912 +- 0.0004   2614.0 +- 0.0
                 NK cell 0.9999 +- 0.0003   0.785 +- 0.02 0.8794 +- 0.0126   1363.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     46.0 +- 0.0

                accuracy                                 0.9287 +- 0.0041   9516.0 +- 0.0
               macro avg 0.9635 +- 0.0017 0.9119 +- 0.0047 0.9309 +- 0.0039   9516.0 +- 0.0
            weighted avg 0.942 +- 0.0027 0.9287 +- 0.0041 0.9293 +- 0.0041   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9145 +- 0.0073
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9286 +- 0.0041
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9166 +- 0.0053
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9084 +- 0.0057
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9059 +- 0.0065


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.908 +- 0.0052
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9308 +- 0.0039
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9237 +- 0.0045
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9165 +- 0.005
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9131 +- 0.0056


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



