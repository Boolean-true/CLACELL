# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.932 +- 0.0023

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0   3129.0 +- 0.0
             CD4+ T cell 0.8994 +- 0.0074 0.9591 +- 0.0024 0.9283 +- 0.0032   6465.0 +- 0.0
             CD8+ T cell 0.8777 +- 0.0029 0.8925 +- 0.0093 0.885 +- 0.0045   6401.0 +- 0.0
          Dendritic cell 0.9417 +- 0.0045 0.8218 +- 0.0042 0.8777 +- 0.0026    165.0 +- 0.0
                Monocyte 0.997 +- 0.0003 0.9977 +- 0.0002 0.9973 +- 0.0001   3648.0 +- 0.0
                 NK cell 0.9921 +- 0.0011 0.7933 +- 0.0075 0.8816 +- 0.0047   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9589 +- 0.0121 0.979 +- 0.0063     56.0 +- 0.0

                accuracy                                 0.932 +- 0.0023  22446.0 +- 0.0
               macro avg 0.9583 +- 0.0016 0.9176 +- 0.0017 0.9356 +- 0.0014  22446.0 +- 0.0
            weighted avg 0.9343 +- 0.0022 0.932 +- 0.0023 0.9315 +- 0.0023  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9174 +- 0.0044
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.932 +- 0.0023
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9191 +- 0.0025
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9179 +- 0.0028
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8738 +- 0.0024


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9247 +- 0.0036
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9355 +- 0.0014
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9291 +- 0.0016
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9277 +- 0.0017
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9029 +- 0.0015



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.9189 +- 0.0046

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9977 +- 0.0   0.9988 +- 0.0   0.9983 +- 0.0    866.0 +- 0.0
             CD4+ T cell 0.9403 +- 0.0053 0.8947 +- 0.0099 0.9169 +- 0.0057   4474.0 +- 0.0
             CD8+ T cell 0.8236 +- 0.0118 0.8981 +- 0.0094 0.8592 +- 0.0077   2688.0 +- 0.0
          Dendritic cell 0.9006 +- 0.004 0.9892 +- 0.004 0.9428 +- 0.0033    120.0 +- 0.0
                Monocyte 0.9985 +- 0.0005 0.9853 +- 0.0006 0.9918 +- 0.0005    889.0 +- 0.0
                 NK cell 0.9767 +- 0.0026 0.9466 +- 0.0088 0.9614 +- 0.0043    876.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0

                accuracy                                 0.9189 +- 0.0046   9983.0 +- 0.0
               macro avg 0.9461 +- 0.0023 0.9549 +- 0.0021 0.9498 +- 0.0021   9983.0 +- 0.0
            weighted avg 0.9221 +- 0.0042 0.9189 +- 0.0046 0.9197 +- 0.0045   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9039 +- 0.0096
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9189 +- 0.0047
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8906 +- 0.0093
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8904 +- 0.0094
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8052 +- 0.0028


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9379 +- 0.0061
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9498 +- 0.0021
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9366 +- 0.0044
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9374 +- 0.0044
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.891 +- 0.0011


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8552 +- 0.0036

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9969 +- 0.0      1.0 +- 0.0   0.9985 +- 0.0    968.0 +- 0.0
             CD4+ T cell 0.976 +- 0.0014 0.6972 +- 0.0084 0.8133 +- 0.0058   4371.0 +- 0.0
             CD8+ T cell 0.6037 +- 0.0064 0.9592 +- 0.0031 0.741 +- 0.0049   2141.0 +- 0.0
          Dendritic cell 0.9596 +- 0.0001 0.9774 +- 0.0033 0.9684 +- 0.0017    146.0 +- 0.0
                Monocyte 0.9981 +- 0.0003   0.9965 +- 0.0 0.9973 +- 0.0001   1703.0 +- 0.0
                 NK cell 0.9796 +- 0.0046 0.9606 +- 0.0049  0.97 +- 0.0029    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0    0.925 +- 0.0    0.961 +- 0.0     40.0 +- 0.0

                accuracy                                 0.8552 +- 0.0036   9998.0 +- 0.0
               macro avg 0.9306 +- 0.0013 0.9308 +- 0.0013 0.9214 +- 0.0016   9998.0 +- 0.0
            weighted avg 0.9022 +- 0.0017 0.8552 +- 0.0036 0.8598 +- 0.0036   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8658 +- 0.0041
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8551 +- 0.0037
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8506 +- 0.0037
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8504 +- 0.0038
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8071 +- 0.0037


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9209 +- 0.003
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9213 +- 0.0016
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9189 +- 0.0015
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9189 +- 0.0016
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8952 +- 0.0019


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.9465 +- 0.0033

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0    764.0 +- 0.0
             CD4+ T cell 0.9898 +- 0.0007 0.8959 +- 0.0085 0.9405 +- 0.0047   4116.0 +- 0.0
             CD8+ T cell 0.7571 +- 0.0137 0.9563 +- 0.0032 0.8451 +- 0.0086   1457.0 +- 0.0
          Dendritic cell 0.9023 +- 0.0039 0.9784 +- 0.0031 0.9388 +- 0.0018    167.0 +- 0.0
                Monocyte 0.9983 +- 0.0002 0.9923 +- 0.0003 0.9953 +- 0.0002   2413.0 +- 0.0
                 NK cell 0.974 +- 0.0036 0.9806 +- 0.0023 0.9773 +- 0.002   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                 0.9465 +- 0.0033   9997.0 +- 0.0
               macro avg 0.9459 +- 0.0019 0.9719 +- 0.0011 0.9567 +- 0.0017   9997.0 +- 0.0
            weighted avg 0.9556 +- 0.0021 0.9465 +- 0.0033 0.9484 +- 0.0031   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9459 +- 0.0062
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9464 +- 0.0034
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9446 +- 0.0037
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9447 +- 0.0036
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9382 +- 0.0026


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9529 +- 0.006
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9567 +- 0.0017
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9552 +- 0.002
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9553 +- 0.002
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9495 +- 0.0015


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.9426 +- 0.0028

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9989 +- 0.0      1.0 +- 0.0   0.9994 +- 0.0    895.0 +- 0.0
             CD4+ T cell 0.9895 +- 0.0023 0.8571 +- 0.0081 0.9186 +- 0.0041   2315.0 +- 0.0
             CD8+ T cell 0.8151 +- 0.0095 0.9792 +- 0.0056 0.8896 +- 0.0047   2127.0 +- 0.0
          Dendritic cell 0.9844 +- 0.0029 0.8878 +- 0.0054 0.9336 +- 0.0033    156.0 +- 0.0
                Monocyte 0.9909 +- 0.0004 0.9988 +- 0.0002 0.9948 +- 0.0002   2614.0 +- 0.0
                 NK cell  0.98 +- 0.0081 0.8895 +- 0.0249 0.9323 +- 0.0113   1363.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     46.0 +- 0.0

                accuracy                                 0.9426 +- 0.0028   9516.0 +- 0.0
               macro avg 0.9655 +- 0.0015 0.9446 +- 0.003 0.9526 +- 0.0023   9516.0 +- 0.0
            weighted avg 0.9504 +- 0.0019 0.9426 +- 0.0028 0.9433 +- 0.0027   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.924 +- 0.0143
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9426 +- 0.0028
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9338 +- 0.0047
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9323 +- 0.0052
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9299 +- 0.0055


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9355 +- 0.0113
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9526 +- 0.0023
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9473 +- 0.0035
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9461 +- 0.004
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9441 +- 0.0044


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



