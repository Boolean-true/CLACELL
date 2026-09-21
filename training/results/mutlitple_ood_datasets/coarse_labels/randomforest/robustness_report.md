# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9284 +- 0.002

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9995 +- 0.0002      1.0 +- 0.0 0.9997 +- 0.0001   3129.0 +- 0.0
             CD4+ T cell 0.8864 +- 0.0053 0.9654 +- 0.0013 0.9242 +- 0.0031   6465.0 +- 0.0
             CD8+ T cell 0.8798 +- 0.0022 0.8753 +- 0.0069 0.8775 +- 0.0039   6401.0 +- 0.0
          Dendritic cell 0.9665 +- 0.0049 0.7848 +- 0.0059 0.8662 +- 0.003    165.0 +- 0.0
                Monocyte 0.9954 +- 0.0003 0.9988 +- 0.0002 0.9971 +- 0.0001   3648.0 +- 0.0
                 NK cell 0.9911 +- 0.0012  0.79 +- 0.0049 0.8792 +- 0.003   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9571 +- 0.0151 0.978 +- 0.0079     56.0 +- 0.0

                accuracy                                 0.9284 +- 0.002  22446.0 +- 0.0
               macro avg 0.9598 +- 0.0008 0.9102 +- 0.0026 0.9317 +- 0.0017  22446.0 +- 0.0
            weighted avg 0.9309 +- 0.0019 0.9284 +- 0.002 0.9278 +- 0.002  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9227 +- 0.0056
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9284 +- 0.002
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9164 +- 0.0025
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9151 +- 0.0022
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8772 +- 0.002


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9273 +- 0.0036
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9317 +- 0.0017
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9249 +- 0.0022
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9224 +- 0.0012
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9013 +- 0.0022



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.9206 +- 0.002

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9976 +- 0.0004   0.9988 +- 0.0 0.9982 +- 0.0002    866.0 +- 0.0
             CD4+ T cell 0.9473 +- 0.0036 0.8821 +- 0.0071 0.9135 +- 0.0027   4474.0 +- 0.0
             CD8+ T cell 0.8197 +- 0.0083 0.9127 +- 0.0068 0.8637 +- 0.0028   2688.0 +- 0.0
          Dendritic cell 0.9271 +- 0.0087 0.9533 +- 0.007  0.94 +- 0.0051    120.0 +- 0.0
                Monocyte 0.9933 +- 0.0006 0.9899 +- 0.0013 0.9916 +- 0.0008    889.0 +- 0.0
                 NK cell 0.9828 +- 0.0028 0.9854 +- 0.0034 0.9841 +- 0.001    876.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0

                accuracy                                 0.9206 +- 0.002   9983.0 +- 0.0
               macro avg 0.9505 +- 0.0014 0.9562 +- 0.0013 0.9528 +- 0.0012   9983.0 +- 0.0
            weighted avg 0.9246 +- 0.0014 0.9206 +- 0.002 0.9214 +- 0.0019   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9136 +- 0.0087
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9206 +- 0.0021
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8971 +- 0.0042
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8969 +- 0.0042
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8122 +- 0.0028


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9459 +- 0.0049
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9528 +- 0.0012
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9421 +- 0.002
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9422 +- 0.002
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8982 +- 0.0012


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8661 +- 0.0028

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9969 +- 0.0      1.0 +- 0.0   0.9985 +- 0.0    968.0 +- 0.0
             CD4+ T cell 0.9758 +- 0.0011 0.7197 +- 0.0063 0.8284 +- 0.0042   4371.0 +- 0.0
             CD8+ T cell 0.6242 +- 0.0053 0.9595 +- 0.0018 0.7564 +- 0.004   2141.0 +- 0.0
          Dendritic cell 0.9685 +- 0.0036 0.9466 +- 0.0054 0.9574 +- 0.0033    146.0 +- 0.0
                Monocyte 0.9954 +- 0.0005 0.9974 +- 0.0003 0.9964 +- 0.0003   1703.0 +- 0.0
                 NK cell 0.9861 +- 0.0028 0.9819 +- 0.0017 0.984 +- 0.0015    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0    0.925 +- 0.0    0.961 +- 0.0     40.0 +- 0.0

                accuracy                                 0.8661 +- 0.0028   9998.0 +- 0.0
               macro avg 0.9353 +- 0.001 0.9329 +- 0.0015 0.926 +- 0.0015   9998.0 +- 0.0
            weighted avg 0.9065 +- 0.0014 0.8661 +- 0.0028 0.8702 +- 0.0027   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8759 +- 0.0062
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8661 +- 0.0028
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8613 +- 0.003
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8615 +- 0.0031
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8197 +- 0.0028


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9274 +- 0.0032
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.926 +- 0.0015
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9237 +- 0.0015
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9236 +- 0.0015
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9018 +- 0.0014


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.9403 +- 0.0022

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0    764.0 +- 0.0
             CD4+ T cell 0.9904 +- 0.0004  0.871 +- 0.006 0.9269 +- 0.0033   4116.0 +- 0.0
             CD8+ T cell 0.7255 +- 0.0086 0.9703 +- 0.0018 0.8302 +- 0.0053   1457.0 +- 0.0
          Dendritic cell 0.9558 +- 0.003 0.9449 +- 0.0062 0.9503 +- 0.0042    167.0 +- 0.0
                Monocyte 0.996 +- 0.0005 0.9966 +- 0.0002 0.9963 +- 0.0003   2413.0 +- 0.0
                 NK cell 0.9907 +- 0.002 0.9957 +- 0.0019 0.9932 +- 0.0012   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                 0.9403 +- 0.0022   9997.0 +- 0.0
               macro avg 0.9512 +- 0.0009 0.9683 +- 0.0008 0.9567 +- 0.001   9997.0 +- 0.0
            weighted avg 0.9534 +- 0.0011 0.9403 +- 0.0022 0.9427 +- 0.002   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9443 +- 0.0026
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9402 +- 0.0021
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9381 +- 0.002
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9381 +- 0.0021
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9326 +- 0.0025


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9564 +- 0.0019
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9566 +- 0.0009
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9551 +- 0.0009
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9549 +- 0.001
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9505 +- 0.0014


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.95 +- 0.0025

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9989 +- 0.0      1.0 +- 0.0   0.9994 +- 0.0    895.0 +- 0.0
             CD4+ T cell 0.9842 +- 0.002 0.8833 +- 0.0049 0.931 +- 0.0025   2315.0 +- 0.0
             CD8+ T cell 0.8396 +- 0.0081 0.9803 +- 0.0034 0.9045 +- 0.0046   2127.0 +- 0.0
          Dendritic cell 0.9977 +- 0.0051 0.8359 +- 0.0101 0.9096 +- 0.0064    156.0 +- 0.0
                Monocyte 0.9877 +- 0.0007 0.9995 +- 0.0003 0.9936 +- 0.0004   2614.0 +- 0.0
                 NK cell 0.9913 +- 0.004 0.8995 +- 0.0134 0.9431 +- 0.0066   1363.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     46.0 +- 0.0

                accuracy                                  0.95 +- 0.0025   9516.0 +- 0.0
               macro avg 0.9713 +- 0.0012 0.9426 +- 0.0028 0.9545 +- 0.0022   9516.0 +- 0.0
            weighted avg 0.9555 +- 0.0019  0.95 +- 0.0025 0.9504 +- 0.0024   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9393 +- 0.0056
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.95 +- 0.0025
Feature importance dropout (0.5% features dropped) Accuracy score: 0.933 +- 0.0045
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9305 +- 0.0049
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9285 +- 0.0055


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9426 +- 0.0047
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9545 +- 0.0022
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9441 +- 0.0032
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.942 +- 0.0036
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9401 +- 0.0038


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



