# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9145 +- 0.001

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0   0.9997 +- 0.0   0.9998 +- 0.0   3129.0 +- 0.0
             CD4+ T cell 0.8857 +- 0.0027 0.9229 +- 0.0017 0.9039 +- 0.0016   6465.0 +- 0.0
             CD8+ T cell 0.837 +- 0.0014 0.8761 +- 0.0032 0.8561 +- 0.0019   6401.0 +- 0.0
          Dendritic cell 0.9508 +- 0.0027 0.8424 +- 0.0057 0.8933 +- 0.0032    165.0 +- 0.0
                Monocyte 0.9967 +- 0.0001 0.998 +- 0.0001 0.9974 +- 0.0001   3648.0 +- 0.0
                 NK cell 0.9813 +- 0.0005  0.77 +- 0.0017 0.8629 +- 0.0009   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     56.0 +- 0.0

                accuracy                                 0.9145 +- 0.001  22446.0 +- 0.0
               macro avg 0.9502 +- 0.0007 0.9156 +- 0.0011 0.9305 +- 0.0008  22446.0 +- 0.0
            weighted avg 0.9175 +- 0.001 0.9145 +- 0.001 0.9143 +- 0.001  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.908 +- 0.0046
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9143 +- 0.001
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9069 +- 0.0012
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9068 +- 0.0011
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8721 +- 0.0014


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9251 +- 0.0037
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9304 +- 0.0008
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9261 +- 0.0008
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9249 +- 0.0006
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9052 +- 0.0008



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.8967 +- 0.0016

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9965 +- 0.0   0.9988 +- 0.0   0.9977 +- 0.0    866.0 +- 0.0
             CD4+ T cell 0.9467 +- 0.0022 0.8365 +- 0.0032 0.8882 +- 0.002   4474.0 +- 0.0
             CD8+ T cell 0.7629 +- 0.0033 0.9075 +- 0.0035 0.8289 +- 0.0025   2688.0 +- 0.0
          Dendritic cell     0.92 +- 0.0   0.9583 +- 0.0   0.9388 +- 0.0    120.0 +- 0.0
                Monocyte 0.9947 +- 0.0005   0.9888 +- 0.0 0.9917 +- 0.0003    889.0 +- 0.0
                 NK cell 0.9501 +- 0.0031 0.9635 +- 0.0015 0.9568 +- 0.0017    876.0 +- 0.0
             Plasma cell 0.9852 +- 0.0001 0.9486 +- 0.0074 0.9665 +- 0.0039     70.0 +- 0.0

                accuracy                                 0.8967 +- 0.0016   9983.0 +- 0.0
               macro avg 0.9366 +- 0.0009 0.9431 +- 0.0014 0.9384 +- 0.0011   9983.0 +- 0.0
            weighted avg 0.9061 +- 0.0015 0.8967 +- 0.0016 0.8981 +- 0.0016   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8915 +- 0.0093
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8956 +- 0.0017
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8774 +- 0.0029
Feature importance dropout (1.0% features dropped) Accuracy score: 0.877 +- 0.003
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8057 +- 0.0027


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9332 +- 0.0043
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9377 +- 0.0011
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9294 +- 0.0015
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9256 +- 0.0021
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8887 +- 0.0017


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8333 +- 0.0032

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9959 +- 0.0      1.0 +- 0.0   0.9979 +- 0.0    968.0 +- 0.0
             CD4+ T cell 0.9689 +- 0.0009 0.6494 +- 0.0078 0.7776 +- 0.0055   4371.0 +- 0.0
             CD8+ T cell 0.5683 +- 0.0052 0.9502 +- 0.0015 0.7112 +- 0.0039   2141.0 +- 0.0
          Dendritic cell 0.9781 +- 0.0022 0.9486 +- 0.0036 0.9631 +- 0.0025    146.0 +- 0.0
                Monocyte 0.9956 +- 0.0003 0.9982 +- 0.0002 0.9969 +- 0.0002   1703.0 +- 0.0
                 NK cell 0.9755 +- 0.0011 0.9792 +- 0.0016 0.9773 +- 0.0011    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0      0.9 +- 0.0   0.9474 +- 0.0     40.0 +- 0.0

                accuracy                                 0.8333 +- 0.0032   9998.0 +- 0.0
               macro avg 0.926 +- 0.0009 0.9179 +- 0.0011 0.9102 +- 0.0014   9998.0 +- 0.0
            weighted avg 0.8909 +- 0.0011 0.8333 +- 0.0032 0.838 +- 0.0032   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.839 +- 0.008
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8325 +- 0.0031
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8283 +- 0.003
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8282 +- 0.0032
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8091 +- 0.0044


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9097 +- 0.0033
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9099 +- 0.0014
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.908 +- 0.0013
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9061 +- 0.0016
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8947 +- 0.0019


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.9027 +- 0.0046

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0    764.0 +- 0.0
             CD4+ T cell 0.9861 +- 0.0011 0.7882 +- 0.0116  0.876 +- 0.007   4116.0 +- 0.0
             CD8+ T cell 0.612 +- 0.0125 0.9485 +- 0.0024 0.7439 +- 0.0089   1457.0 +- 0.0
          Dendritic cell 0.9492 +- 0.003   0.9401 +- 0.0 0.9446 +- 0.0015    167.0 +- 0.0
                Monocyte   0.9959 +- 0.0 0.9962 +- 0.0001 0.996 +- 0.0001   2413.0 +- 0.0
                 NK cell 0.9709 +- 0.002 0.9939 +- 0.0005 0.9823 +- 0.001   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                 0.9027 +- 0.0046   9997.0 +- 0.0
               macro avg 0.9306 +- 0.0018 0.9524 +- 0.0015 0.9347 +- 0.0023   9997.0 +- 0.0
            weighted avg 0.9328 +- 0.0018 0.9027 +- 0.0046 0.9079 +- 0.0042   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9141 +- 0.0057
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9013 +- 0.0048
Feature importance dropout (0.5% features dropped) Accuracy score: 0.899 +- 0.0048
Feature importance dropout (1.0% features dropped) Accuracy score: 0.899 +- 0.0047
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9093 +- 0.0035


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9386 +- 0.003
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9339 +- 0.0023
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9327 +- 0.0023
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9323 +- 0.0022
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9343 +- 0.002


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.9128 +- 0.002

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9989 +- 0.0      1.0 +- 0.0   0.9994 +- 0.0    895.0 +- 0.0
             CD4+ T cell 0.9285 +- 0.0086 0.8608 +- 0.0064 0.8933 +- 0.0035   2315.0 +- 0.0
             CD8+ T cell 0.8158 +- 0.005 0.8392 +- 0.0106 0.8273 +- 0.0052   2127.0 +- 0.0
          Dendritic cell      1.0 +- 0.0 0.8378 +- 0.0031 0.9118 +- 0.0018    156.0 +- 0.0
                Monocyte 0.9855 +- 0.0004   0.9996 +- 0.0 0.9925 +- 0.0002   2614.0 +- 0.0
                 NK cell 0.8403 +- 0.0028 0.8988 +- 0.0042 0.8685 +- 0.0027   1363.0 +- 0.0
             Plasma cell 0.9782 +- 0.0005 0.9739 +- 0.0225 0.9759 +- 0.0115     46.0 +- 0.0

                accuracy                                 0.9128 +- 0.002   9516.0 +- 0.0
               macro avg 0.9353 +- 0.0014 0.9157 +- 0.0036 0.9241 +- 0.0022   9516.0 +- 0.0
            weighted avg 0.9144 +- 0.0023 0.9128 +- 0.002 0.9129 +- 0.002   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.899 +- 0.0081
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9124 +- 0.0019
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8925 +- 0.0034
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8907 +- 0.0032
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8866 +- 0.0033


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9111 +- 0.0061
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9239 +- 0.0022
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9109 +- 0.003
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9094 +- 0.0027
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9024 +- 0.0025


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



