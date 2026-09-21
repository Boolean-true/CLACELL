# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9021 +- 0.002

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9997 +- 0.0002 0.9988 +- 0.0009 0.9992 +- 0.0005   3129.0 +- 0.0
             CD4+ T cell 0.8829 +- 0.0076 0.8782 +- 0.0092 0.8805 +- 0.0037   6465.0 +- 0.0
             CD8+ T cell 0.8064 +- 0.0079 0.8773 +- 0.0089 0.8403 +- 0.0025   6401.0 +- 0.0
          Dendritic cell 0.8652 +- 0.0307 0.8333 +- 0.0216 0.8486 +- 0.019    165.0 +- 0.0
                Monocyte 0.9965 +- 0.0017 0.9948 +- 0.0014 0.9956 +- 0.0011   3648.0 +- 0.0
                 NK cell 0.9718 +- 0.0038 0.7781 +- 0.0124 0.8642 +- 0.0082   2582.0 +- 0.0
             Plasma cell 0.9965 +- 0.0074 0.9875 +- 0.0147 0.9919 +- 0.0067     56.0 +- 0.0

                accuracy                                 0.9021 +- 0.002  22446.0 +- 0.0
               macro avg 0.9313 +- 0.0045 0.9069 +- 0.0044 0.9172 +- 0.0033  22446.0 +- 0.0
            weighted avg 0.9062 +- 0.0017 0.9021 +- 0.002 0.9025 +- 0.0019  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8974 +- 0.0027
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.902 +- 0.0021
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8946 +- 0.002
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8954 +- 0.0019
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8791 +- 0.0026


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9121 +- 0.0038
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9171 +- 0.0033
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9124 +- 0.0034
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9117 +- 0.0036
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9017 +- 0.0055



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.8967 +- 0.0039

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9962 +- 0.0017   0.9988 +- 0.0 0.9975 +- 0.0009    866.0 +- 0.0
             CD4+ T cell 0.9217 +- 0.0097 0.8698 +- 0.0105 0.8949 +- 0.0051   4474.0 +- 0.0
             CD8+ T cell 0.7816 +- 0.0112 0.8659 +- 0.0171 0.8215 +- 0.0072   2688.0 +- 0.0
          Dendritic cell 0.9077 +- 0.016  0.98 +- 0.0098 0.9424 +- 0.0085    120.0 +- 0.0
                Monocyte 0.9957 +- 0.0031 0.9885 +- 0.0017 0.9921 +- 0.0013    889.0 +- 0.0
                 NK cell 0.9647 +- 0.0044 0.9177 +- 0.0134 0.9406 +- 0.0076    876.0 +- 0.0
             Plasma cell 0.9941 +- 0.0076    0.96 +- 0.02 0.9767 +- 0.0109     70.0 +- 0.0

                accuracy                                 0.8967 +- 0.0039   9983.0 +- 0.0
               macro avg 0.9374 +- 0.0032 0.9401 +- 0.0022 0.9379 +- 0.0021   9983.0 +- 0.0
            weighted avg 0.9011 +- 0.004 0.8967 +- 0.0039 0.8978 +- 0.0038   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8928 +- 0.0057
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.896 +- 0.0039
Feature importance dropout (0.5% features dropped) Accuracy score: 0.878 +- 0.0045
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8766 +- 0.0045
Feature importance dropout (2.0% features dropped) Accuracy score: 0.842 +- 0.0036


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9332 +- 0.0035
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9376 +- 0.002
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9283 +- 0.0019
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9189 +- 0.007
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9021 +- 0.0073


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8757 +- 0.006

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9961 +- 0.0008      1.0 +- 0.0 0.998 +- 0.0004    968.0 +- 0.0
             CD4+ T cell 0.952 +- 0.0052 0.7647 +- 0.0158 0.848 +- 0.0086   4371.0 +- 0.0
             CD8+ T cell 0.6523 +- 0.014 0.9166 +- 0.011 0.7621 +- 0.008   2141.0 +- 0.0
          Dendritic cell 0.9499 +- 0.006 0.9726 +- 0.0171 0.961 +- 0.0083    146.0 +- 0.0
                Monocyte 0.9965 +- 0.0023 0.9958 +- 0.0005 0.9961 +- 0.001   1703.0 +- 0.0
                 NK cell 0.9856 +- 0.0064 0.9669 +- 0.0069 0.9762 +- 0.0035    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.905 +- 0.0197  0.95 +- 0.0108     40.0 +- 0.0

                accuracy                                 0.8757 +- 0.006   9998.0 +- 0.0
               macro avg 0.9332 +- 0.0021 0.9317 +- 0.0058 0.9274 +- 0.0044   9998.0 +- 0.0
            weighted avg 0.9019 +- 0.0031 0.8757 +- 0.006 0.8795 +- 0.0057   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8756 +- 0.0064
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8748 +- 0.0063
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8675 +- 0.0061
Feature importance dropout (1.0% features dropped) Accuracy score: 0.867 +- 0.006
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8486 +- 0.0064


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9249 +- 0.0033
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.927 +- 0.0045
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9227 +- 0.0044
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9163 +- 0.0024
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.907 +- 0.003


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.9031 +- 0.0076

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9991 +- 0.0006 0.9996 +- 0.0009 0.9993 +- 0.0006    764.0 +- 0.0
             CD4+ T cell 0.9809 +- 0.0028 0.7943 +- 0.0195 0.8777 +- 0.0113   4116.0 +- 0.0
             CD8+ T cell 0.6144 +- 0.0223 0.9423 +- 0.0082 0.7435 +- 0.0149   1457.0 +- 0.0
          Dendritic cell 0.9395 +- 0.0195 0.9551 +- 0.0256 0.9468 +- 0.0099    167.0 +- 0.0
                Monocyte 0.9965 +- 0.0019 0.9957 +- 0.0014 0.9961 +- 0.0007   2413.0 +- 0.0
                 NK cell 0.9799 +- 0.0021 0.9804 +- 0.0054 0.9801 +- 0.0028   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                 0.9031 +- 0.0076   9997.0 +- 0.0
               macro avg  0.93 +- 0.0034 0.9525 +- 0.0046 0.9348 +- 0.0039   9997.0 +- 0.0
            weighted avg 0.9319 +- 0.0029 0.9031 +- 0.0076 0.9083 +- 0.0069   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.905 +- 0.0084
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9009 +- 0.0078
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8988 +- 0.0081
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8982 +- 0.0083
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8906 +- 0.0093


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9332 +- 0.0048
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9337 +- 0.004
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9322 +- 0.0042
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9276 +- 0.0046
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.923 +- 0.0051


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.9116 +- 0.0118

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9975 +- 0.0013 0.9971 +- 0.003 0.9973 +- 0.0019    895.0 +- 0.0
             CD4+ T cell 0.8464 +- 0.0266 0.931 +- 0.0122 0.8865 +- 0.0156   2315.0 +- 0.0
             CD8+ T cell 0.8306 +- 0.0189 0.7997 +- 0.0434 0.8144 +- 0.0269   2127.0 +- 0.0
          Dendritic cell 0.9626 +- 0.0691 0.8077 +- 0.0569 0.8769 +- 0.0532    156.0 +- 0.0
                Monocyte 0.9813 +- 0.0114 0.999 +- 0.0005  0.99 +- 0.0059   2614.0 +- 0.0
                 NK cell 0.9674 +- 0.0212 0.8406 +- 0.0206 0.8994 +- 0.0162   1363.0 +- 0.0
             Plasma cell  0.9079 +- 0.04 0.9283 +- 0.0447 0.9172 +- 0.0318     46.0 +- 0.0

                accuracy                                 0.9116 +- 0.0118   9516.0 +- 0.0
               macro avg 0.9277 +- 0.0176 0.9005 +- 0.0198 0.9117 +- 0.0178   9516.0 +- 0.0
            weighted avg 0.9137 +- 0.0118 0.9116 +- 0.0118 0.9111 +- 0.0122   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9033 +- 0.0154
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9114 +- 0.0119
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8905 +- 0.0142
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8857 +- 0.0145
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8905 +- 0.0146


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8989 +- 0.0207
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9116 +- 0.0178
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.898 +- 0.0195
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8939 +- 0.0199
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8898 +- 0.0233


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



