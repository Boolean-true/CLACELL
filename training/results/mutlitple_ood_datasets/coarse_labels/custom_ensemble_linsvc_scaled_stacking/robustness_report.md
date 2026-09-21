# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9154 +- 0.0009

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9997 +- 0.0002      1.0 +- 0.0 0.9998 +- 0.0001   3129.0 +- 0.0
             CD4+ T cell 0.8924 +- 0.0039 0.926 +- 0.0017 0.9089 +- 0.0017   6465.0 +- 0.0
             CD8+ T cell 0.8333 +- 0.0014 0.887 +- 0.0049 0.8593 +- 0.002   6401.0 +- 0.0
          Dendritic cell 0.9205 +- 0.0088 0.7855 +- 0.0087 0.8476 +- 0.0086    165.0 +- 0.0
                Monocyte 0.9964 +- 0.0002 0.9969 +- 0.0004 0.9966 +- 0.0001   3648.0 +- 0.0
                 NK cell 0.9921 +- 0.001 0.7487 +- 0.0041 0.8534 +- 0.0027   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9768 +- 0.0086 0.9882 +- 0.0044     56.0 +- 0.0

                accuracy                                 0.9154 +- 0.0009  22446.0 +- 0.0
               macro avg 0.9478 +- 0.0011 0.903 +- 0.0013 0.922 +- 0.0012  22446.0 +- 0.0
            weighted avg 0.9193 +- 0.001 0.9154 +- 0.0009 0.915 +- 0.0009  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9048 +- 0.0043
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9154 +- 0.0009
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9029 +- 0.0015
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9042 +- 0.0013
Feature importance dropout (2.0% features dropped) Accuracy score: 0.868 +- 0.001


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9086 +- 0.0073
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.922 +- 0.0012
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9132 +- 0.0011
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9111 +- 0.0015
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8389 +- 0.0097



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.8973 +- 0.0043

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9965 +- 0.0   0.9988 +- 0.0   0.9977 +- 0.0    866.0 +- 0.0
             CD4+ T cell 0.9545 +- 0.0048 0.8312 +- 0.013 0.8885 +- 0.0056   4474.0 +- 0.0
             CD8+ T cell 0.7552 +- 0.0138 0.9296 +- 0.0099 0.8332 +- 0.0048   2688.0 +- 0.0
          Dendritic cell 0.9251 +- 0.0033 0.9058 +- 0.004 0.9154 +- 0.0024    120.0 +- 0.0
                Monocyte 0.9872 +- 0.0006 0.9901 +- 0.0005 0.9887 +- 0.0004    889.0 +- 0.0
                 NK cell 0.9858 +- 0.0071 0.9342 +- 0.0129 0.9592 +- 0.0039    876.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0

                accuracy                                 0.8973 +- 0.0043   9983.0 +- 0.0
               macro avg 0.9414 +- 0.0006 0.9373 +- 0.0024 0.9373 +- 0.0019   9983.0 +- 0.0
            weighted avg  0.91 +- 0.0017 0.8973 +- 0.0043 0.8992 +- 0.004   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.891 +- 0.0091
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8969 +- 0.0043
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8851 +- 0.0029
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8809 +- 0.0039
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8096 +- 0.0027


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9221 +- 0.0104
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9372 +- 0.0019
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9306 +- 0.0017
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9164 +- 0.005
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8808 +- 0.0045


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8297 +- 0.0041

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9959 +- 0.0      1.0 +- 0.0   0.9979 +- 0.0    968.0 +- 0.0
             CD4+ T cell 0.9772 +- 0.0018   0.638 +- 0.01 0.772 +- 0.0069   4371.0 +- 0.0
             CD8+ T cell 0.5618 +- 0.0063 0.9682 +- 0.0028 0.711 +- 0.0045   2141.0 +- 0.0
          Dendritic cell 0.9669 +- 0.0031 0.9384 +- 0.0085 0.9524 +- 0.0035    146.0 +- 0.0
                Monocyte 0.9947 +- 0.0007 0.9972 +- 0.0003 0.996 +- 0.0003   1703.0 +- 0.0
                 NK cell 0.995 +- 0.0017 0.9444 +- 0.0055 0.969 +- 0.0026    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0      0.9 +- 0.0   0.9474 +- 0.0     40.0 +- 0.0

                accuracy                                 0.8297 +- 0.0041   9998.0 +- 0.0
               macro avg 0.9274 +- 0.0008 0.9123 +- 0.0026 0.9065 +- 0.0023   9998.0 +- 0.0
            weighted avg 0.8941 +- 0.001 0.8297 +- 0.0041 0.8347 +- 0.0041   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8332 +- 0.008
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8286 +- 0.0043
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8258 +- 0.0044
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8242 +- 0.0045
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8135 +- 0.0036


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8971 +- 0.0077
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9061 +- 0.0023
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.904 +- 0.0026
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8902 +- 0.0051
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8834 +- 0.0044


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.9023 +- 0.0093

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9993 +- 0.0007      1.0 +- 0.0 0.9997 +- 0.0003    764.0 +- 0.0
             CD4+ T cell 0.9871 +- 0.0017 0.7836 +- 0.0238 0.8735 +- 0.0144   4116.0 +- 0.0
             CD8+ T cell 0.6088 +- 0.0245 0.9618 +- 0.0071 0.7453 +- 0.0169   1457.0 +- 0.0
          Dendritic cell 0.9571 +- 0.0017 0.9491 +- 0.0127 0.9531 +- 0.0065    167.0 +- 0.0
                Monocyte 0.9965 +- 0.0009 0.9966 +- 0.0001 0.9966 +- 0.0004   2413.0 +- 0.0
                 NK cell 0.9865 +- 0.0046 0.9866 +- 0.0027 0.9865 +- 0.0013   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                 0.9023 +- 0.0093   9997.0 +- 0.0
               macro avg 0.9336 +- 0.0031 0.954 +- 0.0042 0.9364 +- 0.0051   9997.0 +- 0.0
            weighted avg 0.9346 +- 0.0029 0.9023 +- 0.0093 0.9077 +- 0.0085   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9049 +- 0.0127
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9004 +- 0.0093
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8982 +- 0.0093
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8969 +- 0.0095
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9062 +- 0.0091


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.93 +- 0.0072
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9354 +- 0.0051
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9339 +- 0.0051
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9286 +- 0.0062
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9304 +- 0.006


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.9391 +- 0.0029

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9978 +- 0.0      1.0 +- 0.0   0.9989 +- 0.0    895.0 +- 0.0
             CD4+ T cell 0.9663 +- 0.0075 0.8778 +- 0.0109 0.9199 +- 0.0032   2315.0 +- 0.0
             CD8+ T cell 0.8234 +- 0.0135 0.9541 +- 0.0111 0.8838 +- 0.0044   2127.0 +- 0.0
          Dendritic cell 0.9985 +- 0.0032 0.8288 +- 0.0113 0.9057 +- 0.0064    156.0 +- 0.0
                Monocyte 0.9861 +- 0.0008   0.9996 +- 0.0 0.9928 +- 0.0004   2614.0 +- 0.0
                 NK cell 0.9741 +- 0.0062 0.8742 +- 0.0215  0.9213 +- 0.01   1363.0 +- 0.0
             Plasma cell 0.9747 +- 0.0131      1.0 +- 0.0 0.9872 +- 0.0067     46.0 +- 0.0

                accuracy                                 0.9391 +- 0.0029   9516.0 +- 0.0
               macro avg 0.9601 +- 0.0019 0.9335 +- 0.004 0.9442 +- 0.0034   9516.0 +- 0.0
            weighted avg 0.9444 +- 0.0016 0.9391 +- 0.0029 0.9396 +- 0.0028   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9284 +- 0.0079
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9387 +- 0.0029
Feature importance dropout (0.5% features dropped) Accuracy score: 0.927 +- 0.0039
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9181 +- 0.0058
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9192 +- 0.0053


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.934 +- 0.0063
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.944 +- 0.0034
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.937 +- 0.0026
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9304 +- 0.0051
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9265 +- 0.005


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



