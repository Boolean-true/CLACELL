# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9106 +- 0.0011

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9996 +- 0.0002   1.0 +- 0.0001 0.9998 +- 0.0001   3129.0 +- 0.0
             CD4+ T cell 0.8933 +- 0.0035 0.9095 +- 0.0015 0.9013 +- 0.002   6465.0 +- 0.0
             CD8+ T cell 0.8183 +- 0.0012 0.8901 +- 0.0041 0.8527 +- 0.0021   6401.0 +- 0.0
          Dendritic cell 0.9319 +- 0.0029 0.8127 +- 0.0067 0.8682 +- 0.0044    165.0 +- 0.0
                Monocyte 0.9967 +- 0.0003 0.9971 +- 0.0003 0.9969 +- 0.0002   3648.0 +- 0.0
                 NK cell 0.9918 +- 0.0011 0.7385 +- 0.0035 0.8466 +- 0.0024   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9786 +- 0.0075 0.9892 +- 0.0039     56.0 +- 0.0

                accuracy                                 0.9106 +- 0.0011  22446.0 +- 0.0
               macro avg 0.9474 +- 0.0005 0.9038 +- 0.0013 0.9221 +- 0.0009  22446.0 +- 0.0
            weighted avg 0.9154 +- 0.0011 0.9106 +- 0.0011 0.9104 +- 0.001  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9033 +- 0.0041
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9106 +- 0.001
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8984 +- 0.0025
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8994 +- 0.0025
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8934 +- 0.0017


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9123 +- 0.0059
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9221 +- 0.0009
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9119 +- 0.0011
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.911 +- 0.0012
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8959 +- 0.0012



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.8742 +- 0.0048

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9965 +- 0.0   0.9988 +- 0.0   0.9977 +- 0.0    866.0 +- 0.0
             CD4+ T cell 0.9511 +- 0.0059 0.7965 +- 0.0073 0.8669 +- 0.0053   4474.0 +- 0.0
             CD8+ T cell 0.705 +- 0.0084 0.9302 +- 0.0084 0.802 +- 0.0069   2688.0 +- 0.0
          Dendritic cell 0.9285 +- 0.0053 0.9308 +- 0.004 0.9297 +- 0.003    120.0 +- 0.0
                Monocyte 0.9904 +- 0.0008 0.9903 +- 0.0008 0.9904 +- 0.0004    889.0 +- 0.0
                 NK cell 0.9941 +- 0.0017 0.843 +- 0.0123 0.9123 +- 0.0068    876.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0

                accuracy                                 0.8742 +- 0.0048   9983.0 +- 0.0
               macro avg 0.9359 +- 0.0017 0.923 +- 0.0031 0.9253 +- 0.0026   9983.0 +- 0.0
            weighted avg  0.896 +- 0.004 0.8742 +- 0.0048 0.8773 +- 0.0046   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8661 +- 0.0089
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8728 +- 0.0049
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8578 +- 0.0049
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8517 +- 0.0052
Feature importance dropout (2.0% features dropped) Accuracy score: 0.846 +- 0.0031


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9112 +- 0.0063
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9248 +- 0.0026
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9135 +- 0.0029
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9031 +- 0.0042
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9006 +- 0.0037


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8325 +- 0.0054

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9959 +- 0.0      1.0 +- 0.0   0.9979 +- 0.0    968.0 +- 0.0
             CD4+ T cell 0.9716 +- 0.0026 0.6509 +- 0.0116 0.7795 +- 0.0087   4371.0 +- 0.0
             CD8+ T cell 0.5665 +- 0.0084 0.9603 +- 0.0034 0.7126 +- 0.0069   2141.0 +- 0.0
          Dendritic cell 0.9654 +- 0.0002 0.9562 +- 0.0048 0.9608 +- 0.0025    146.0 +- 0.0
                Monocyte 0.9962 +- 0.0004   0.9971 +- 0.0 0.9967 +- 0.0002   1703.0 +- 0.0
                 NK cell 0.9964 +- 0.0012 0.9238 +- 0.0063 0.9587 +- 0.0031    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0      0.9 +- 0.0   0.9474 +- 0.0     40.0 +- 0.0

                accuracy                                 0.8325 +- 0.0054   9998.0 +- 0.0
               macro avg 0.9274 +- 0.0013 0.9126 +- 0.0023 0.9077 +- 0.0024   9998.0 +- 0.0
            weighted avg 0.893 +- 0.0025 0.8325 +- 0.0054 0.8379 +- 0.0054   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8303 +- 0.0075
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8304 +- 0.0056
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8252 +- 0.0053
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8231 +- 0.0053
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8277 +- 0.0038


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8988 +- 0.0033
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9068 +- 0.0025
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.902 +- 0.0025
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8949 +- 0.0029
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8972 +- 0.0023


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.8597 +- 0.0058

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0    764.0 +- 0.0
             CD4+ T cell 0.9854 +- 0.001 0.6861 +- 0.0135 0.8089 +- 0.0094   4116.0 +- 0.0
             CD8+ T cell 0.5131 +- 0.0106 0.9668 +- 0.0023 0.6704 +- 0.009   1457.0 +- 0.0
          Dendritic cell 0.9575 +- 0.0003 0.9455 +- 0.0077 0.9515 +- 0.0041    167.0 +- 0.0
                Monocyte 0.9962 +- 0.0005   0.9967 +- 0.0 0.9965 +- 0.0003   2413.0 +- 0.0
                 NK cell 0.9927 +- 0.0009 0.9562 +- 0.0036 0.9741 +- 0.002   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                 0.8597 +- 0.0058   9997.0 +- 0.0
               macro avg 0.9207 +- 0.0016 0.9359 +- 0.003 0.9145 +- 0.0031   9997.0 +- 0.0
            weighted avg 0.9207 +- 0.0017 0.8597 +- 0.0058 0.8689 +- 0.0054   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8641 +- 0.0061
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8562 +- 0.0058
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8537 +- 0.0058
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8501 +- 0.0059
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8629 +- 0.006


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9113 +- 0.0043
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9129 +- 0.0032
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.911 +- 0.0032
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9062 +- 0.0045
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9124 +- 0.0042


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.9159 +- 0.0049

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9978 +- 0.0      1.0 +- 0.0   0.9989 +- 0.0    895.0 +- 0.0
             CD4+ T cell 0.9467 +- 0.0081 0.8808 +- 0.008 0.9125 +- 0.0039   2315.0 +- 0.0
             CD8+ T cell 0.7594 +- 0.0139 0.9409 +- 0.0095 0.8404 +- 0.0083   2127.0 +- 0.0
          Dendritic cell      1.0 +- 0.0 0.841 +- 0.0041 0.9136 +- 0.0024    156.0 +- 0.0
                Monocyte 0.9873 +- 0.0005   0.9996 +- 0.0 0.9934 +- 0.0002   2614.0 +- 0.0
                 NK cell 0.9865 +- 0.0026 0.7262 +- 0.0249 0.8363 +- 0.0161   1363.0 +- 0.0
             Plasma cell 0.9647 +- 0.0193      1.0 +- 0.0  0.9819 +- 0.01     46.0 +- 0.0

                accuracy                                 0.9159 +- 0.0049   9516.0 +- 0.0
               macro avg 0.9489 +- 0.0033 0.9126 +- 0.0044 0.9253 +- 0.004   9516.0 +- 0.0
            weighted avg 0.9275 +- 0.0033 0.9159 +- 0.0049 0.9162 +- 0.005   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9064 +- 0.0106
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9154 +- 0.0048
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9045 +- 0.0046
Feature importance dropout (1.0% features dropped) Accuracy score: 0.884 +- 0.0052
Feature importance dropout (2.0% features dropped) Accuracy score: 0.886 +- 0.0052


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9164 +- 0.0086
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9251 +- 0.004
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9187 +- 0.0031
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8994 +- 0.0046
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8985 +- 0.0056


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



