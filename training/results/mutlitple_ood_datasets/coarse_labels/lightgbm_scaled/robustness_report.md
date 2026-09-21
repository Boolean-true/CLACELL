# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9394 +- 0.001

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9998 +- 0.0002 0.9999 +- 0.0001 0.9999 +- 0.0001   3129.0 +- 0.0
             CD4+ T cell 0.9541 +- 0.0014 0.944 +- 0.0022 0.949 +- 0.0011   6465.0 +- 0.0
             CD8+ T cell 0.8549 +- 0.0027 0.9566 +- 0.0018 0.9029 +- 0.0015   6401.0 +- 0.0
          Dendritic cell 0.9381 +- 0.0093 0.8061 +- 0.0099 0.867 +- 0.0046    165.0 +- 0.0
                Monocyte 0.9966 +- 0.0004 0.9973 +- 0.0004 0.997 +- 0.0002   3648.0 +- 0.0
                 NK cell 0.997 +- 0.0009 0.7383 +- 0.0053 0.8483 +- 0.0033   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9482 +- 0.0472 0.9729 +- 0.0257     56.0 +- 0.0

                accuracy                                 0.9394 +- 0.001  22446.0 +- 0.0
               macro avg 0.9629 +- 0.0014 0.9129 +- 0.0076 0.9338 +- 0.0039  22446.0 +- 0.0
            weighted avg 0.944 +- 0.0008 0.9394 +- 0.001 0.9386 +- 0.001  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9233 +- 0.006
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9394 +- 0.001
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9347 +- 0.0011
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9331 +- 0.001
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8722 +- 0.0023


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9131 +- 0.0083
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9338 +- 0.0039
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.931 +- 0.0039
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9297 +- 0.0039
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8932 +- 0.0049



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.9003 +- 0.0022

### Classification Report 

                               precision          recall        f1-score         support

                  B cell  0.996 +- 0.001   0.9988 +- 0.0 0.9974 +- 0.0005    866.0 +- 0.0
             CD4+ T cell 0.9367 +- 0.0019 0.8525 +- 0.0074 0.8926 +- 0.0034   4474.0 +- 0.0
             CD8+ T cell 0.7732 +- 0.0069 0.9013 +- 0.0036 0.8324 +- 0.0029   2688.0 +- 0.0
          Dendritic cell 0.917 +- 0.0066 0.9475 +- 0.0079 0.932 +- 0.0029    120.0 +- 0.0
                Monocyte 0.9941 +- 0.0017 0.9884 +- 0.0011 0.9913 +- 0.0006    889.0 +- 0.0
                 NK cell 0.9917 +- 0.0007 0.9422 +- 0.0088 0.9663 +- 0.0046    876.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0

                accuracy                                 0.9003 +- 0.0022   9983.0 +- 0.0
               macro avg 0.942 +- 0.0007 0.9432 +- 0.0016 0.9415 +- 0.0008   9983.0 +- 0.0
            weighted avg 0.9079 +- 0.0014 0.9003 +- 0.0022 0.9018 +- 0.0021   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8823 +- 0.0098
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9002 +- 0.0022
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8774 +- 0.0025
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8767 +- 0.0027
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7888 +- 0.0035


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9137 +- 0.0152
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9415 +- 0.0009
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9303 +- 0.0012
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9295 +- 0.0013
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8839 +- 0.0011


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8294 +- 0.002

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9959 +- 0.0 0.999 +- 0.0005 0.9974 +- 0.0002    968.0 +- 0.0
             CD4+ T cell 0.9656 +- 0.0015 0.6449 +- 0.0044 0.7733 +- 0.0033   4371.0 +- 0.0
             CD8+ T cell 0.5629 +- 0.0032 0.9513 +- 0.0019 0.7073 +- 0.0027   2141.0 +- 0.0
          Dendritic cell 0.9604 +- 0.0053 0.9445 +- 0.0051 0.9523 +- 0.0014    146.0 +- 0.0
                Monocyte 0.995 +- 0.0006 0.9967 +- 0.0005 0.9958 +- 0.0002   1703.0 +- 0.0
                 NK cell 0.993 +- 0.0007 0.952 +- 0.0016 0.9721 +- 0.0009    629.0 +- 0.0
             Plasma cell 0.9865 +- 0.0142      0.9 +- 0.0 0.9412 +- 0.0065     40.0 +- 0.0

                accuracy                                 0.8294 +- 0.002   9998.0 +- 0.0
               macro avg 0.9227 +- 0.0016 0.9126 +- 0.0009 0.9056 +- 0.0009   9998.0 +- 0.0
            weighted avg 0.889 +- 0.0011 0.8294 +- 0.002 0.8345 +- 0.002   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8414 +- 0.0136
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8294 +- 0.002
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8245 +- 0.0021
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8244 +- 0.0021
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7808 +- 0.0023


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8961 +- 0.0123
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9056 +- 0.0009
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9031 +- 0.0013
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9034 +- 0.0007
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8808 +- 0.001


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.9277 +- 0.0053

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0    764.0 +- 0.0
             CD4+ T cell 0.9879 +- 0.0007 0.8476 +- 0.0141 0.9124 +- 0.008   4116.0 +- 0.0
             CD8+ T cell 0.6825 +- 0.0184 0.9688 +- 0.0023 0.8007 +- 0.0118   1457.0 +- 0.0
          Dendritic cell 0.9274 +- 0.006 0.9707 +- 0.0072 0.9485 +- 0.0037    167.0 +- 0.0
                Monocyte 0.9978 +- 0.0005 0.9943 +- 0.0005 0.9961 +- 0.0003   2413.0 +- 0.0
                 NK cell 0.9961 +- 0.0007 0.9698 +- 0.0045 0.9828 +- 0.0025   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.995 +- 0.0158 0.9974 +- 0.0081     40.0 +- 0.0

                accuracy                                 0.9277 +- 0.0053   9997.0 +- 0.0
               macro avg 0.9417 +- 0.0021 0.9638 +- 0.0036 0.9483 +- 0.0032   9997.0 +- 0.0
            weighted avg 0.9466 +- 0.0025 0.9277 +- 0.0053 0.9313 +- 0.0048   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9286 +- 0.0037
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9274 +- 0.0054
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9255 +- 0.0054
Feature importance dropout (1.0% features dropped) Accuracy score: 0.925 +- 0.0056
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9259 +- 0.0057


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9308 +- 0.0091
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9481 +- 0.0033
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9464 +- 0.0035
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9454 +- 0.0041
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9437 +- 0.0043


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.8754 +- 0.0169

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9985 +- 0.0005      1.0 +- 0.0 0.9993 +- 0.0003    895.0 +- 0.0
             CD4+ T cell 0.982 +- 0.0016 0.8149 +- 0.0063 0.8907 +- 0.0035   2315.0 +- 0.0
             CD8+ T cell 0.6534 +- 0.032 0.985 +- 0.0017 0.7852 +- 0.0232   2127.0 +- 0.0
          Dendritic cell 0.9823 +- 0.007  0.85 +- 0.0033 0.9113 +- 0.0034    156.0 +- 0.0
                Monocyte 0.9888 +- 0.0005 0.9987 +- 0.0004 0.9937 +- 0.0002   2614.0 +- 0.0
                 NK cell      1.0 +- 0.0 0.4873 +- 0.1159 0.6476 +- 0.1097   1363.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     46.0 +- 0.0

                accuracy                                 0.8754 +- 0.0169   9516.0 +- 0.0
               macro avg 0.9436 +- 0.0051 0.8766 +- 0.0168 0.8897 +- 0.0193   9516.0 +- 0.0
            weighted avg 0.9147 +- 0.0073 0.8754 +- 0.0169 0.8717 +- 0.0211   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.856 +- 0.0212
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8753 +- 0.0169
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8653 +- 0.0151
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8608 +- 0.0142
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8564 +- 0.0144


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8595 +- 0.0201
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8897 +- 0.0193
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8845 +- 0.018
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8796 +- 0.0174
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8771 +- 0.0172


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



