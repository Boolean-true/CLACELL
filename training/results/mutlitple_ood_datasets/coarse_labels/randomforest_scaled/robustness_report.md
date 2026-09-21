# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9287 +- 0.0013

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9995 +- 0.0003      1.0 +- 0.0 0.9997 +- 0.0001   3129.0 +- 0.0
             CD4+ T cell 0.8866 +- 0.004 0.9663 +- 0.0013 0.9247 +- 0.0022   6465.0 +- 0.0
             CD8+ T cell 0.8806 +- 0.0013 0.8753 +- 0.005 0.8779 +- 0.0027   6401.0 +- 0.0
          Dendritic cell 0.9653 +- 0.0083 0.7903 +- 0.0071 0.869 +- 0.0061    165.0 +- 0.0
                Monocyte 0.9956 +- 0.0002 0.9987 +- 0.0003 0.9971 +- 0.0002   3648.0 +- 0.0
                 NK cell 0.9908 +- 0.0012 0.7897 +- 0.0033 0.8789 +- 0.0022   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9571 +- 0.0173  0.978 +- 0.009     56.0 +- 0.0

                accuracy                                 0.9287 +- 0.0013  22446.0 +- 0.0
               macro avg 0.9598 +- 0.0011 0.9111 +- 0.0028 0.9322 +- 0.0018  22446.0 +- 0.0
            weighted avg 0.9312 +- 0.0012 0.9287 +- 0.0013 0.9281 +- 0.0013  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9195 +- 0.0049
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9287 +- 0.0013
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9163 +- 0.0017
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9153 +- 0.0012
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8779 +- 0.001


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9251 +- 0.003
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9322 +- 0.0018
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.925 +- 0.0018
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.922 +- 0.0017
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9014 +- 0.0023



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.922 +- 0.0024

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9977 +- 0.0   0.9988 +- 0.0   0.9983 +- 0.0    866.0 +- 0.0
             CD4+ T cell 0.9474 +- 0.0027 0.8852 +- 0.0055 0.9152 +- 0.003   4474.0 +- 0.0
             CD8+ T cell 0.8238 +- 0.0068 0.9122 +- 0.0049 0.8657 +- 0.0038   2688.0 +- 0.0
          Dendritic cell 0.9246 +- 0.0054 0.9608 +- 0.0069 0.9424 +- 0.0053    120.0 +- 0.0
                Monocyte 0.9941 +- 0.0013 0.9894 +- 0.0008 0.9918 +- 0.0007    889.0 +- 0.0
                 NK cell 0.9819 +- 0.0031 0.9866 +- 0.0034 0.9843 +- 0.002    876.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0

                accuracy                                 0.922 +- 0.0024   9983.0 +- 0.0
               macro avg 0.9507 +- 0.0013 0.9578 +- 0.0012 0.9537 +- 0.0013   9983.0 +- 0.0
            weighted avg 0.9256 +- 0.002 0.922 +- 0.0024 0.9227 +- 0.0023   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9067 +- 0.008
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9219 +- 0.0025
Feature importance dropout (0.5% features dropped) Accuracy score: 0.898 +- 0.0047
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8979 +- 0.0048
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8118 +- 0.0021


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9435 +- 0.0039
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9537 +- 0.0013
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9428 +- 0.0022
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9428 +- 0.0021
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8984 +- 0.0013


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8664 +- 0.0023

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9969 +- 0.0      1.0 +- 0.0   0.9985 +- 0.0    968.0 +- 0.0
             CD4+ T cell 0.9751 +- 0.0008 0.7212 +- 0.0058 0.8291 +- 0.0036   4371.0 +- 0.0
             CD8+ T cell 0.625 +- 0.0046 0.9582 +- 0.0013 0.7565 +- 0.0031   2141.0 +- 0.0
          Dendritic cell 0.9699 +- 0.0045 0.9473 +- 0.0056 0.9584 +- 0.0037    146.0 +- 0.0
                Monocyte 0.9955 +- 0.0005 0.9975 +- 0.0004 0.9965 +- 0.0003   1703.0 +- 0.0
                 NK cell 0.9859 +- 0.0022 0.9804 +- 0.0032 0.9832 +- 0.0021    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0    0.925 +- 0.0    0.961 +- 0.0     40.0 +- 0.0

                accuracy                                 0.8664 +- 0.0023   9998.0 +- 0.0
               macro avg 0.9355 +- 0.0013 0.9328 +- 0.0011 0.9262 +- 0.0013   9998.0 +- 0.0
            weighted avg 0.9064 +- 0.0009 0.8664 +- 0.0023 0.8706 +- 0.0023   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.874 +- 0.0029
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8664 +- 0.0024
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8615 +- 0.0023
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8615 +- 0.0023
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8222 +- 0.0035


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9254 +- 0.0016
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9262 +- 0.0013
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9238 +- 0.0013
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9239 +- 0.0013
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9032 +- 0.0018


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.9422 +- 0.0029

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0    764.0 +- 0.0
             CD4+ T cell 0.9907 +- 0.0006 0.8752 +- 0.0079 0.9293 +- 0.0043   4116.0 +- 0.0
             CD8+ T cell 0.7324 +- 0.0117 0.9706 +- 0.0028 0.8348 +- 0.0068   1457.0 +- 0.0
          Dendritic cell 0.9559 +- 0.0048 0.9479 +- 0.0049 0.9519 +- 0.004    167.0 +- 0.0
                Monocyte 0.9961 +- 0.0004 0.9966 +- 0.0003 0.9964 +- 0.0003   2413.0 +- 0.0
                 NK cell 0.9904 +- 0.0018 0.9961 +- 0.0012 0.9932 +- 0.0014   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                 0.9422 +- 0.0029   9997.0 +- 0.0
               macro avg 0.9522 +- 0.0017 0.9695 +- 0.0014 0.9579 +- 0.0018   9997.0 +- 0.0
            weighted avg 0.9545 +- 0.0015 0.9422 +- 0.0029 0.9444 +- 0.0027   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9452 +- 0.0027
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.942 +- 0.0029
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9397 +- 0.0031
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9396 +- 0.0032
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9333 +- 0.0023


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9564 +- 0.0026
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9579 +- 0.0018
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9563 +- 0.002
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9559 +- 0.002
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9509 +- 0.0016


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.9511 +- 0.0011

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9989 +- 0.0      1.0 +- 0.0   0.9994 +- 0.0    895.0 +- 0.0
             CD4+ T cell 0.9832 +- 0.0023 0.8854 +- 0.0045 0.9317 +- 0.0028   2315.0 +- 0.0
             CD8+ T cell 0.8433 +- 0.0039 0.9797 +- 0.0032 0.9064 +- 0.0023   2127.0 +- 0.0
          Dendritic cell 0.9985 +- 0.0032 0.841 +- 0.0084  0.913 +- 0.005    156.0 +- 0.0
                Monocyte 0.9881 +- 0.0006 0.9995 +- 0.0002 0.9938 +- 0.0003   2614.0 +- 0.0
                 NK cell 0.9919 +- 0.0029 0.9041 +- 0.0042 0.946 +- 0.0028   1363.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     46.0 +- 0.0

                accuracy                                 0.9511 +- 0.0011   9516.0 +- 0.0
               macro avg 0.972 +- 0.0006 0.9443 +- 0.001 0.9558 +- 0.0007   9516.0 +- 0.0
            weighted avg 0.9563 +- 0.001 0.9511 +- 0.0011 0.9515 +- 0.0011   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.94 +- 0.0059
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9512 +- 0.0011
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9328 +- 0.0019
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9302 +- 0.002
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9285 +- 0.0017


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9437 +- 0.0046
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9558 +- 0.0007
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9445 +- 0.0014
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9424 +- 0.0014
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9407 +- 0.0015


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



