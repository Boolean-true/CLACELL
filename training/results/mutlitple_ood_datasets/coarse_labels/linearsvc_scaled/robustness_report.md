# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9266 +- 0.0004

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9998 +- 0.0002      1.0 +- 0.0 0.9999 +- 0.0001   3129.0 +- 0.0
             CD4+ T cell 0.9122 +- 0.0007 0.9136 +- 0.0022 0.9129 +- 0.0012   6465.0 +- 0.0
             CD8+ T cell 0.8502 +- 0.0009 0.9081 +- 0.0009 0.8782 +- 0.0004   6401.0 +- 0.0
          Dendritic cell 0.9181 +- 0.0022 0.8897 +- 0.0114 0.9036 +- 0.0065    165.0 +- 0.0
                Monocyte 0.9975 +- 0.0001 0.9964 +- 0.0003 0.9969 +- 0.0001   3648.0 +- 0.0
                 NK cell 0.985 +- 0.0004 0.8183 +- 0.0028 0.8939 +- 0.0015   2582.0 +- 0.0
             Plasma cell 0.9823 +- 0.0002 0.9911 +- 0.0094 0.9866 +- 0.0047     56.0 +- 0.0

                accuracy                                 0.9266 +- 0.0004  22446.0 +- 0.0
               macro avg 0.9493 +- 0.0005 0.931 +- 0.0028 0.9389 +- 0.0016  22446.0 +- 0.0
            weighted avg 0.9292 +- 0.0004 0.9266 +- 0.0004 0.9267 +- 0.0003  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9186 +- 0.0043
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9267 +- 0.0004
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9162 +- 0.0004
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9173 +- 0.0005
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8828 +- 0.0004


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.931 +- 0.0031
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9389 +- 0.0016
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9321 +- 0.0015
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9312 +- 0.0013
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.913 +- 0.001



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.8988 +- 0.0032

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9927 +- 0.002   0.9988 +- 0.0 0.9957 +- 0.001    866.0 +- 0.0
             CD4+ T cell 0.9598 +- 0.0035 0.8264 +- 0.0101 0.8881 +- 0.0044   4474.0 +- 0.0
             CD8+ T cell 0.7585 +- 0.0091 0.9327 +- 0.0058 0.8365 +- 0.0035   2688.0 +- 0.0
          Dendritic cell 0.9128 +- 0.0002 0.9592 +- 0.0026 0.9354 +- 0.0014    120.0 +- 0.0
                Monocyte 0.9838 +- 0.003   0.9876 +- 0.0 0.9857 +- 0.0015    889.0 +- 0.0
                 NK cell 0.9729 +- 0.0008 0.9614 +- 0.0026 0.9671 +- 0.0016    876.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0

                accuracy                                 0.8988 +- 0.0032   9983.0 +- 0.0
               macro avg 0.938 +- 0.0012 0.9482 +- 0.0008 0.941 +- 0.0013   9983.0 +- 0.0
            weighted avg 0.9113 +- 0.0014 0.8988 +- 0.0032 0.9004 +- 0.0031   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.888 +- 0.0102
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8984 +- 0.0032
Feature importance dropout (0.5% features dropped) Accuracy score: 0.89 +- 0.0019
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8887 +- 0.002
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8129 +- 0.001


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9311 +- 0.0068
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9408 +- 0.0014
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9364 +- 0.001
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9349 +- 0.0011
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8974 +- 0.001


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8268 +- 0.0032

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9959 +- 0.0      1.0 +- 0.0   0.9979 +- 0.0    968.0 +- 0.0
             CD4+ T cell 0.9791 +- 0.0012 0.6268 +- 0.0079 0.7643 +- 0.0057   4371.0 +- 0.0
             CD8+ T cell 0.557 +- 0.0048 0.9702 +- 0.0017 0.7077 +- 0.0036   2141.0 +- 0.0
          Dendritic cell 0.9442 +- 0.0032 0.9856 +- 0.0022 0.9645 +- 0.0017    146.0 +- 0.0
                Monocyte 0.9981 +- 0.0004 0.9956 +- 0.0003 0.9969 +- 0.0002   1703.0 +- 0.0
                 NK cell 0.9918 +- 0.0011 0.9636 +- 0.0027 0.9775 +- 0.0013    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0      0.9 +- 0.0   0.9474 +- 0.0     40.0 +- 0.0

                accuracy                                 0.8268 +- 0.0032   9998.0 +- 0.0
               macro avg 0.9237 +- 0.0008 0.9203 +- 0.0012 0.908 +- 0.0015   9998.0 +- 0.0
            weighted avg 0.894 +- 0.0009 0.8268 +- 0.0032 0.8315 +- 0.0033   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8273 +- 0.0069
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8258 +- 0.0033
Feature importance dropout (0.5% features dropped) Accuracy score: 0.824 +- 0.0032
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8235 +- 0.0032
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8095 +- 0.0026


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9052 +- 0.0025
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9076 +- 0.0015
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9064 +- 0.0013
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9058 +- 0.0015
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.899 +- 0.0013


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.902 +- 0.006

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9987 +- 0.0      1.0 +- 0.0   0.9993 +- 0.0    764.0 +- 0.0
             CD4+ T cell 0.9877 +- 0.0011 0.7819 +- 0.0157 0.8728 +- 0.0094   4116.0 +- 0.0
             CD8+ T cell  0.609 +- 0.016 0.958 +- 0.0032 0.7445 +- 0.0112   1457.0 +- 0.0
          Dendritic cell 0.9207 +- 0.0024 0.9731 +- 0.0032 0.9461 +- 0.0016    167.0 +- 0.0
                Monocyte 0.9974 +- 0.0005 0.9947 +- 0.0003 0.996 +- 0.0002   2413.0 +- 0.0
                 NK cell 0.9803 +- 0.0008 0.9962 +- 0.0007 0.9882 +- 0.0003   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                  0.902 +- 0.006   9997.0 +- 0.0
               macro avg 0.9277 +- 0.002 0.9577 +- 0.0021 0.9353 +- 0.003   9997.0 +- 0.0
            weighted avg 0.9339 +- 0.0019  0.902 +- 0.006 0.9073 +- 0.0055   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9085 +- 0.0069
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9003 +- 0.0063
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8991 +- 0.0064
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8985 +- 0.0066
Feature importance dropout (2.0% features dropped) Accuracy score: 0.905 +- 0.0057


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9346 +- 0.0043
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9344 +- 0.0031
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9335 +- 0.0031
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.933 +- 0.0032
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9357 +- 0.0029


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.9429 +- 0.0015

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9989 +- 0.0      1.0 +- 0.0   0.9994 +- 0.0    895.0 +- 0.0
             CD4+ T cell 0.9731 +- 0.0079 0.8685 +- 0.0094 0.9178 +- 0.0021   2315.0 +- 0.0
             CD8+ T cell 0.8368 +- 0.0067 0.9563 +- 0.0102 0.8925 +- 0.003   2127.0 +- 0.0
          Dendritic cell 0.9709 +- 0.0069 0.8756 +- 0.0062 0.9208 +- 0.004    156.0 +- 0.0
                Monocyte 0.9883 +- 0.0004 0.9985 +- 0.0002 0.9934 +- 0.0002   2614.0 +- 0.0
                 NK cell 0.9616 +- 0.0036 0.9102 +- 0.0064 0.9352 +- 0.0042   1363.0 +- 0.0
             Plasma cell 0.9128 +- 0.0093      1.0 +- 0.0 0.9544 +- 0.0051     46.0 +- 0.0

                accuracy                                 0.9429 +- 0.0015   9516.0 +- 0.0
               macro avg 0.9489 +- 0.003 0.9442 +- 0.002 0.9448 +- 0.0019   9516.0 +- 0.0
            weighted avg 0.9473 +- 0.0018 0.9429 +- 0.0015 0.9433 +- 0.0014   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9317 +- 0.0069
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9426 +- 0.0015
Feature importance dropout (0.5% features dropped) Accuracy score: 0.933 +- 0.0029
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9284 +- 0.0031
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9303 +- 0.0026


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9351 +- 0.006
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9448 +- 0.002
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9382 +- 0.003
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9344 +- 0.0032
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9364 +- 0.0029


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



