# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9193 +- 0.0016

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9999 +- 0.0002      1.0 +- 0.0   1.0 +- 0.0001   3129.0 +- 0.0
             CD4+ T cell 0.8862 +- 0.0025 0.9159 +- 0.0029 0.9008 +- 0.0024   6465.0 +- 0.0
             CD8+ T cell 0.8503 +- 0.0031 0.8758 +- 0.0026 0.8629 +- 0.0028   6401.0 +- 0.0
          Dendritic cell  0.9036 +- 0.01 0.9073 +- 0.0128 0.9053 +- 0.0061    165.0 +- 0.0
                Monocyte 0.9983 +- 0.0003 0.9955 +- 0.0006 0.9969 +- 0.0003   3648.0 +- 0.0
                 NK cell 0.9813 +- 0.0023 0.8291 +- 0.004 0.8988 +- 0.0024   2582.0 +- 0.0
             Plasma cell 0.9982 +- 0.0055      1.0 +- 0.0 0.9991 +- 0.0028     56.0 +- 0.0

                accuracy                                 0.9193 +- 0.0016  22446.0 +- 0.0
               macro avg 0.9454 +- 0.0018 0.932 +- 0.0019 0.9377 +- 0.0012  22446.0 +- 0.0
            weighted avg 0.9214 +- 0.0016 0.9193 +- 0.0016 0.9195 +- 0.0016  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9127 +- 0.0035
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9193 +- 0.0016
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9094 +- 0.0013
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9104 +- 0.0013
Feature importance dropout (2.0% features dropped) Accuracy score: 0.879 +- 0.0017


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.931 +- 0.0019
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9377 +- 0.0012
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9317 +- 0.001
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9324 +- 0.0011
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9168 +- 0.0019



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.8706 +- 0.0039

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9963 +- 0.0007   0.9988 +- 0.0 0.9976 +- 0.0004    866.0 +- 0.0
             CD4+ T cell 0.9704 +- 0.0007 0.7536 +- 0.0107 0.8483 +- 0.0067   4474.0 +- 0.0
             CD8+ T cell 0.6955 +- 0.0086 0.9401 +- 0.0043 0.7995 +- 0.0044   2688.0 +- 0.0
          Dendritic cell 0.9064 +- 0.0005 0.9683 +- 0.0053 0.9363 +- 0.0027    120.0 +- 0.0
                Monocyte 0.9963 +- 0.0008   0.9876 +- 0.0 0.9919 +- 0.0004    889.0 +- 0.0
                 NK cell 0.9335 +- 0.0087 0.9878 +- 0.0027 0.9599 +- 0.0038    876.0 +- 0.0
             Plasma cell 0.973 +- 0.0122   0.9714 +- 0.0 0.9722 +- 0.0061     70.0 +- 0.0

                accuracy                                 0.8706 +- 0.0039   9983.0 +- 0.0
               macro avg 0.9245 +- 0.0017 0.944 +- 0.0014 0.9294 +- 0.0013   9983.0 +- 0.0
            weighted avg 0.897 +- 0.0016 0.8706 +- 0.0039 0.8726 +- 0.0039   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8597 +- 0.006
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8694 +- 0.0042
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8668 +- 0.004
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8667 +- 0.0045
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8174 +- 0.0022


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9214 +- 0.0047
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9288 +- 0.0014
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9279 +- 0.001
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9279 +- 0.0015
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9035 +- 0.0027


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8042 +- 0.0023

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9962 +- 0.0005 0.9998 +- 0.0004 0.998 +- 0.0002    968.0 +- 0.0
             CD4+ T cell 0.9832 +- 0.0012 0.5718 +- 0.0051 0.723 +- 0.0041   4371.0 +- 0.0
             CD8+ T cell  0.525 +- 0.003 0.9706 +- 0.0013 0.6814 +- 0.0026   2141.0 +- 0.0
          Dendritic cell 0.9461 +- 0.0103 0.9842 +- 0.0046 0.9648 +- 0.0051    146.0 +- 0.0
                Monocyte 0.9986 +- 0.0004 0.9952 +- 0.001 0.9969 +- 0.0005   1703.0 +- 0.0
                 NK cell  0.968 +- 0.004 0.9866 +- 0.0032 0.9772 +- 0.0015    629.0 +- 0.0
             Plasma cell 0.9947 +- 0.0111 0.9075 +- 0.0121 0.949 +- 0.0043     40.0 +- 0.0

                accuracy                                 0.8042 +- 0.0023   9998.0 +- 0.0
               macro avg 0.916 +- 0.0027 0.9165 +- 0.0027 0.8986 +- 0.002   9998.0 +- 0.0
            weighted avg 0.8875 +- 0.0009 0.8042 +- 0.0023 0.8078 +- 0.0024   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.802 +- 0.0054
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8029 +- 0.0022
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8025 +- 0.0023
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8021 +- 0.0023
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7934 +- 0.0026


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8964 +- 0.0028
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8981 +- 0.0019
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8985 +- 0.002
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8978 +- 0.0017
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8928 +- 0.0016


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.8615 +- 0.0049

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9999 +- 0.0004      1.0 +- 0.0 0.9999 +- 0.0002    764.0 +- 0.0
             CD4+ T cell 0.9907 +- 0.0005 0.6868 +- 0.0127 0.8112 +- 0.0088   4116.0 +- 0.0
             CD8+ T cell 0.5171 +- 0.0096 0.9469 +- 0.0043 0.6688 +- 0.0073   1457.0 +- 0.0
          Dendritic cell 0.9228 +- 0.0043 0.9725 +- 0.0031 0.9469 +- 0.0022    167.0 +- 0.0
                Monocyte 0.9981 +- 0.0002 0.9945 +- 0.0003 0.9963 +- 0.0002   2413.0 +- 0.0
                 NK cell 0.9534 +- 0.006 0.9992 +- 0.001 0.9758 +- 0.0028   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                 0.8615 +- 0.0049   9997.0 +- 0.0
               macro avg 0.9117 +- 0.0015 0.9428 +- 0.0017 0.9141 +- 0.0022   9997.0 +- 0.0
            weighted avg 0.9192 +- 0.0012 0.8615 +- 0.0049 0.8697 +- 0.0046   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8568 +- 0.0077
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8592 +- 0.0047
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8583 +- 0.0046
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8586 +- 0.0047
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8668 +- 0.0035


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9093 +- 0.0036
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9131 +- 0.0021
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.913 +- 0.002
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9135 +- 0.0021
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9157 +- 0.0012


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.9097 +- 0.005

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9988 +- 0.0004 0.9998 +- 0.0007 0.9993 +- 0.0004    895.0 +- 0.0
             CD4+ T cell 0.9779 +- 0.0087 0.782 +- 0.0209  0.8688 +- 0.01   2315.0 +- 0.0
             CD8+ T cell 0.7791 +- 0.0117 0.8797 +- 0.0183 0.8262 +- 0.0081   2127.0 +- 0.0
          Dendritic cell 0.9724 +- 0.0098 0.8756 +- 0.0069 0.9214 +- 0.0034    156.0 +- 0.0
                Monocyte 0.9888 +- 0.0009 0.9982 +- 0.0004 0.9935 +- 0.0003   2614.0 +- 0.0
                 NK cell 0.8376 +- 0.0226 0.9453 +- 0.0057 0.8881 +- 0.0135   1363.0 +- 0.0
             Plasma cell 0.9726 +- 0.0098      1.0 +- 0.0 0.9861 +- 0.0051     46.0 +- 0.0

                accuracy                                 0.9097 +- 0.005   9516.0 +- 0.0
               macro avg 0.9325 +- 0.0039 0.9258 +- 0.0033 0.9262 +- 0.0037   9516.0 +- 0.0
            weighted avg 0.9182 +- 0.0045 0.9097 +- 0.005   0.91 +- 0.005   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9017 +- 0.0065
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9091 +- 0.0051
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9022 +- 0.0057
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9042 +- 0.0063
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9025 +- 0.0059


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9185 +- 0.0055
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9257 +- 0.0037
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9212 +- 0.0043
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9224 +- 0.005
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9219 +- 0.0051


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



