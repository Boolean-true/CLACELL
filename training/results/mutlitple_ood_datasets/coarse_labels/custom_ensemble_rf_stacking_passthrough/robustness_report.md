# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9176 +- 0.0008

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0   3129.0 +- 0.0
             CD4+ T cell 0.8895 +- 0.0028 0.9358 +- 0.0018 0.9121 +- 0.0012   6465.0 +- 0.0
             CD8+ T cell 0.8431 +- 0.0013 0.8804 +- 0.0036 0.8614 +- 0.0016   6401.0 +- 0.0
          Dendritic cell 0.9623 +- 0.0033 0.8194 +- 0.0048 0.8851 +- 0.0034    165.0 +- 0.0
                Monocyte 0.9962 +- 0.0002 0.9984 +- 0.0001 0.9973 +- 0.0001   3648.0 +- 0.0
                 NK cell 0.9849 +- 0.0006 0.7552 +- 0.0017 0.8549 +- 0.0011   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0   0.9821 +- 0.0    0.991 +- 0.0     56.0 +- 0.0

                accuracy                                 0.9176 +- 0.0008  22446.0 +- 0.0
               macro avg 0.9537 +- 0.0008 0.9102 +- 0.0008 0.9288 +- 0.0008  22446.0 +- 0.0
            weighted avg 0.9208 +- 0.0008 0.9176 +- 0.0008 0.9171 +- 0.0008  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9097 +- 0.0036
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9175 +- 0.0008
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9081 +- 0.001
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9069 +- 0.0011
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8707 +- 0.0009


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9232 +- 0.0034
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9288 +- 0.0008
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9228 +- 0.0009
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9208 +- 0.0009
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9031 +- 0.0007



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.9037 +- 0.0011

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9977 +- 0.0   0.9988 +- 0.0   0.9983 +- 0.0    866.0 +- 0.0
             CD4+ T cell 0.9534 +- 0.0013 0.8411 +- 0.0034 0.8938 +- 0.0015   4474.0 +- 0.0
             CD8+ T cell 0.7727 +- 0.0033 0.9221 +- 0.0022 0.8408 +- 0.0014   2688.0 +- 0.0
          Dendritic cell 0.9055 +- 0.0048   0.9583 +- 0.0 0.9312 +- 0.0025    120.0 +- 0.0
                Monocyte   0.9943 +- 0.0 0.9876 +- 0.0007 0.991 +- 0.0004    889.0 +- 0.0
                 NK cell 0.9686 +- 0.0016 0.9753 +- 0.001 0.972 +- 0.0009    876.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0

                accuracy                                 0.9037 +- 0.0011   9983.0 +- 0.0
               macro avg 0.9397 +- 0.001 0.9507 +- 0.0003 0.9436 +- 0.0007   9983.0 +- 0.0
            weighted avg 0.9132 +- 0.0007 0.9037 +- 0.0011 0.9051 +- 0.0011   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9007 +- 0.0038
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9032 +- 0.0012
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8883 +- 0.0015
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8875 +- 0.0016
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8083 +- 0.0019


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9406 +- 0.0013
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9434 +- 0.0007
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9365 +- 0.0008
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9357 +- 0.0007
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8961 +- 0.0011


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8377 +- 0.0015

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9959 +- 0.0    0.999 +- 0.0   0.9974 +- 0.0    968.0 +- 0.0
             CD4+ T cell 0.9737 +- 0.0014 0.6551 +- 0.0041 0.7833 +- 0.0027   4371.0 +- 0.0
             CD8+ T cell 0.575 +- 0.0025 0.9583 +- 0.0023 0.7187 +- 0.0017   2141.0 +- 0.0
          Dendritic cell   0.9786 +- 0.0   0.9384 +- 0.0    0.958 +- 0.0    146.0 +- 0.0
                Monocyte   0.9947 +- 0.0   0.9982 +- 0.0   0.9965 +- 0.0   1703.0 +- 0.0
                 NK cell 0.9812 +- 0.0014 0.9854 +- 0.0007 0.9833 +- 0.0007    629.0 +- 0.0
             Plasma cell    0.973 +- 0.0      0.9 +- 0.0   0.9351 +- 0.0     40.0 +- 0.0

                accuracy                                 0.8377 +- 0.0015   9998.0 +- 0.0
               macro avg 0.9246 +- 0.0003 0.9192 +- 0.0004 0.9103 +- 0.0006   9998.0 +- 0.0
            weighted avg 0.8946 +- 0.0006 0.8377 +- 0.0015 0.8422 +- 0.0015   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8441 +- 0.0028
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8369 +- 0.0017
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8329 +- 0.0017
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8334 +- 0.0016
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8118 +- 0.0026


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9106 +- 0.0014
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.91 +- 0.0007
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.908 +- 0.0007
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.91 +- 0.0007
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8975 +- 0.0011


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.9059 +- 0.0034

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0    764.0 +- 0.0
             CD4+ T cell 0.9871 +- 0.0007 0.7944 +- 0.0089 0.8803 +- 0.0053   4116.0 +- 0.0
             CD8+ T cell 0.6199 +- 0.0098 0.9541 +- 0.0021 0.7515 +- 0.0068   1457.0 +- 0.0
          Dendritic cell   0.9623 +- 0.0   0.9162 +- 0.0   0.9387 +- 0.0    167.0 +- 0.0
                Monocyte   0.9942 +- 0.0   0.9971 +- 0.0   0.9957 +- 0.0   2413.0 +- 0.0
                 NK cell 0.9764 +- 0.0014 0.9937 +- 0.001 0.9849 +- 0.0007   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                 0.9059 +- 0.0034   9997.0 +- 0.0
               macro avg 0.9343 +- 0.0013 0.9508 +- 0.001 0.9359 +- 0.0017   9997.0 +- 0.0
            weighted avg 0.9348 +- 0.0013 0.9059 +- 0.0034 0.9109 +- 0.0031   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.915 +- 0.0037
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9039 +- 0.0034
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9019 +- 0.0033
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9022 +- 0.0033
Feature importance dropout (2.0% features dropped) Accuracy score: 0.911 +- 0.0028


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9394 +- 0.002
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9348 +- 0.0017
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9336 +- 0.0016
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9337 +- 0.0016
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9358 +- 0.0014


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.9342 +- 0.0012

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9989 +- 0.0      1.0 +- 0.0   0.9994 +- 0.0    895.0 +- 0.0
             CD4+ T cell 0.9405 +- 0.0035 0.8876 +- 0.004 0.9133 +- 0.0024   2315.0 +- 0.0
             CD8+ T cell 0.8217 +- 0.0049 0.9258 +- 0.0042 0.8706 +- 0.0022   2127.0 +- 0.0
          Dendritic cell      1.0 +- 0.0 0.8417 +- 0.0031 0.914 +- 0.0018    156.0 +- 0.0
                Monocyte 0.9873 +- 0.0002   0.9996 +- 0.0 0.9934 +- 0.0001   2614.0 +- 0.0
                 NK cell 0.9722 +- 0.0021 0.8662 +- 0.0078 0.9161 +- 0.0041   1363.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     46.0 +- 0.0

                accuracy                                 0.9342 +- 0.0012   9516.0 +- 0.0
               macro avg 0.9601 +- 0.0006 0.9316 +- 0.0013 0.9438 +- 0.001   9516.0 +- 0.0
            weighted avg 0.9381 +- 0.001 0.9342 +- 0.0012 0.9347 +- 0.0012   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9208 +- 0.006
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.934 +- 0.0012
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9142 +- 0.0019
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9074 +- 0.0018
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9051 +- 0.0021


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9318 +- 0.0044
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9437 +- 0.001
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9314 +- 0.0012
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9257 +- 0.0013
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9227 +- 0.0014


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



