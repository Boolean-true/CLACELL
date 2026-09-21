# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9254 +- 0.0009

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9996 +- 0.0001   0.9997 +- 0.0 0.9997 +- 0.0001   3129.0 +- 0.0
             CD4+ T cell 0.9081 +- 0.0013 0.9161 +- 0.0021 0.9121 +- 0.0005   6465.0 +- 0.0
             CD8+ T cell 0.8506 +- 0.0035 0.9038 +- 0.0019 0.8764 +- 0.0012   6401.0 +- 0.0
          Dendritic cell 0.9156 +- 0.0077 0.8473 +- 0.0069 0.8801 +- 0.0026    165.0 +- 0.0
                Monocyte 0.9965 +- 0.0009 0.9967 +- 0.0005 0.9966 +- 0.0005   3648.0 +- 0.0
                 NK cell 0.9858 +- 0.0008 0.815 +- 0.0065 0.8923 +- 0.004   2582.0 +- 0.0
             Plasma cell 0.974 +- 0.0089 0.9982 +- 0.0056 0.9859 +- 0.0045     56.0 +- 0.0

                accuracy                                 0.9254 +- 0.0009  22446.0 +- 0.0
               macro avg 0.9472 +- 0.0008 0.9252 +- 0.0015 0.9347 +- 0.0012  22446.0 +- 0.0
            weighted avg 0.928 +- 0.0007 0.9254 +- 0.0009 0.9255 +- 0.0009  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9164 +- 0.0067
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9254 +- 0.0009
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9145 +- 0.0011
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9167 +- 0.0011
Feature importance dropout (2.0% features dropped) Accuracy score: 0.883 +- 0.0005


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9241 +- 0.0051
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9347 +- 0.0012
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9269 +- 0.0013
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9282 +- 0.0015
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9115 +- 0.0015



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.8959 +- 0.004

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9837 +- 0.0036   0.9988 +- 0.0 0.9912 +- 0.0018    866.0 +- 0.0
             CD4+ T cell 0.963 +- 0.0036 0.823 +- 0.0118 0.8875 +- 0.0054   4474.0 +- 0.0
             CD8+ T cell 0.7587 +- 0.0097 0.9276 +- 0.0053 0.8347 +- 0.0039   2688.0 +- 0.0
          Dendritic cell 0.884 +- 0.0077 0.965 +- 0.0035 0.9227 +- 0.0048    120.0 +- 0.0
                Monocyte 0.9454 +- 0.012   0.9876 +- 0.0 0.966 +- 0.0063    889.0 +- 0.0
                 NK cell 0.977 +- 0.0018 0.9599 +- 0.002 0.9684 +- 0.0013    876.0 +- 0.0
             Plasma cell 0.9419 +- 0.0083   0.9714 +- 0.0 0.9564 +- 0.0043     70.0 +- 0.0

                accuracy                                 0.8959 +- 0.004   9983.0 +- 0.0
               macro avg 0.922 +- 0.0017 0.9476 +- 0.0015 0.9324 +- 0.0018   9983.0 +- 0.0
            weighted avg 0.9084 +- 0.0019 0.8959 +- 0.004 0.8973 +- 0.004   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8884 +- 0.0076
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8956 +- 0.004
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8874 +- 0.0035
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8856 +- 0.0039
Feature importance dropout (2.0% features dropped) Accuracy score: 0.812 +- 0.0017


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9226 +- 0.0048
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.932 +- 0.002
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9265 +- 0.0026
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9246 +- 0.0032
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8872 +- 0.0019


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8238 +- 0.0044

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9944 +- 0.001 0.9999 +- 0.0003 0.9971 +- 0.0005    968.0 +- 0.0
             CD4+ T cell 0.9801 +- 0.0007 0.6203 +- 0.0105 0.7597 +- 0.0077   4371.0 +- 0.0
             CD8+ T cell 0.5534 +- 0.0065 0.9713 +- 0.0011  0.705 +- 0.005   2141.0 +- 0.0
          Dendritic cell 0.9494 +- 0.0042 0.976 +- 0.0058 0.9625 +- 0.002    146.0 +- 0.0
                Monocyte 0.9944 +- 0.0012 0.9957 +- 0.0003 0.995 +- 0.0005   1703.0 +- 0.0
                 NK cell 0.9914 +- 0.0015 0.9582 +- 0.0013 0.9745 +- 0.0009    629.0 +- 0.0
             Plasma cell 0.9973 +- 0.0085 0.905 +- 0.0105 0.9489 +- 0.0075     40.0 +- 0.0

                accuracy                                 0.8238 +- 0.0044   9998.0 +- 0.0
               macro avg 0.9229 +- 0.0016 0.9181 +- 0.0028 0.9061 +- 0.0026   9998.0 +- 0.0
            weighted avg 0.8929 +- 0.0012 0.8238 +- 0.0044 0.8283 +- 0.0045   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8246 +- 0.0079
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.823 +- 0.0044
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8213 +- 0.0042
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8211 +- 0.0042
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8093 +- 0.0038


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.901 +- 0.0061
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9058 +- 0.0025
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9043 +- 0.0025
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9041 +- 0.0018
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8964 +- 0.002


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.9071 +- 0.0085

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9934 +- 0.0025      1.0 +- 0.0 0.9967 +- 0.0013    764.0 +- 0.0
             CD4+ T cell 0.9879 +- 0.0004 0.7942 +- 0.0212 0.8804 +- 0.0129   4116.0 +- 0.0
             CD8+ T cell 0.6246 +- 0.0239 0.9572 +- 0.0024 0.7557 +- 0.0169   1457.0 +- 0.0
          Dendritic cell 0.9274 +- 0.0063 0.9701 +- 0.0049 0.9482 +- 0.0023    167.0 +- 0.0
                Monocyte 0.9959 +- 0.0006 0.9954 +- 0.0006 0.9956 +- 0.0003   2413.0 +- 0.0
                 NK cell 0.9815 +- 0.0009 0.9973 +- 0.0009 0.9894 +- 0.0003   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                 0.9071 +- 0.0085   9997.0 +- 0.0
               macro avg 0.9301 +- 0.0028 0.9592 +- 0.0034 0.938 +- 0.0043   9997.0 +- 0.0
            weighted avg 0.9357 +- 0.0033 0.9071 +- 0.0085 0.9119 +- 0.0078   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.912 +- 0.0084
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.906 +- 0.0086
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9044 +- 0.0087
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9036 +- 0.0088
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9122 +- 0.0079


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9356 +- 0.004
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9374 +- 0.0043
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9364 +- 0.0043
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9358 +- 0.0045
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9384 +- 0.0043


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.9359 +- 0.0024

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9973 +- 0.0006      1.0 +- 0.0 0.9987 +- 0.0003    895.0 +- 0.0
             CD4+ T cell 0.9894 +- 0.001 0.8209 +- 0.0113 0.8973 +- 0.0064   2315.0 +- 0.0
             CD8+ T cell 0.7972 +- 0.0074 0.9843 +- 0.0014 0.8809 +- 0.0044   2127.0 +- 0.0
          Dendritic cell 0.9428 +- 0.006 0.8756 +- 0.0045 0.9079 +- 0.0014    156.0 +- 0.0
                Monocyte 0.9889 +- 0.0003 0.999 +- 0.0002 0.9939 +- 0.0001   2614.0 +- 0.0
                 NK cell 0.9891 +- 0.0023 0.897 +- 0.0035 0.9408 +- 0.0012   1363.0 +- 0.0
             Plasma cell 0.9256 +- 0.0091      1.0 +- 0.0 0.9614 +- 0.0049     46.0 +- 0.0

                accuracy                                 0.9359 +- 0.0024   9516.0 +- 0.0
               macro avg 0.9472 +- 0.0008 0.9396 +- 0.0017 0.9401 +- 0.0013   9516.0 +- 0.0
            weighted avg 0.9459 +- 0.0015 0.9359 +- 0.0024 0.9364 +- 0.0024   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.93 +- 0.0089
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9357 +- 0.0024
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9329 +- 0.0017
Feature importance dropout (1.0% features dropped) Accuracy score: 0.926 +- 0.0021
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9251 +- 0.0023


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9321 +- 0.0064
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9399 +- 0.0014
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9383 +- 0.0011
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9329 +- 0.0013
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9325 +- 0.0013


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



