# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.896 +- 0.003

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9967 +- 0.0012 0.9997 +- 0.0003 0.9982 +- 0.0006   3129.0 +- 0.0
             CD4+ T cell 0.8645 +- 0.0057 0.8912 +- 0.0076 0.8776 +- 0.0046   6465.0 +- 0.0
             CD8+ T cell 0.8039 +- 0.0089 0.8528 +- 0.0066 0.8276 +- 0.0048   6401.0 +- 0.0
          Dendritic cell 0.958 +- 0.0097 0.7715 +- 0.0095 0.8546 +- 0.0066    165.0 +- 0.0
                Monocyte 0.9938 +- 0.0011 0.9981 +- 0.0004 0.996 +- 0.0007   3648.0 +- 0.0
                 NK cell 0.9705 +- 0.0069 0.7543 +- 0.0189 0.8488 +- 0.0128   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.8429 +- 0.0436 0.9142 +- 0.0257     56.0 +- 0.0

                accuracy                                  0.896 +- 0.003  22446.0 +- 0.0
               macro avg 0.9411 +- 0.0023 0.8729 +- 0.0044 0.9024 +- 0.0024  22446.0 +- 0.0
            weighted avg 0.8999 +- 0.0027  0.896 +- 0.003  0.896 +- 0.003  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8892 +- 0.0026
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8959 +- 0.003
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8874 +- 0.0031
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8868 +- 0.0031
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8714 +- 0.003


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8949 +- 0.0032
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9024 +- 0.0024
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8952 +- 0.002
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8873 +- 0.004
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8743 +- 0.0038



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.8717 +- 0.0051

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9703 +- 0.0077 0.999 +- 0.0004 0.9844 +- 0.004    866.0 +- 0.0
             CD4+ T cell 0.9081 +- 0.0134 0.8264 +- 0.0107 0.8652 +- 0.0057   4474.0 +- 0.0
             CD8+ T cell 0.7321 +- 0.0097 0.8499 +- 0.0241 0.7864 +- 0.0105   2688.0 +- 0.0
          Dendritic cell 0.9169 +- 0.0117 0.9817 +- 0.0035 0.9481 +- 0.0066    120.0 +- 0.0
                Monocyte 0.9973 +- 0.0011 0.988 +- 0.0018 0.9926 +- 0.001    889.0 +- 0.0
                 NK cell 0.9658 +- 0.009 0.9305 +- 0.0235 0.9476 +- 0.0102    876.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.6286 +- 0.1003 0.7678 +- 0.0739     70.0 +- 0.0

                accuracy                                 0.8717 +- 0.0051   9983.0 +- 0.0
               macro avg 0.9272 +- 0.0027 0.8863 +- 0.015 0.8989 +- 0.0111   9983.0 +- 0.0
            weighted avg 0.8799 +- 0.006 0.8717 +- 0.0051 0.8732 +- 0.0051   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8633 +- 0.0072
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8709 +- 0.0052
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8546 +- 0.0057
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8516 +- 0.0056
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8226 +- 0.0055


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.889 +- 0.0084
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8986 +- 0.0112
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8901 +- 0.0111
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8471 +- 0.01
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8338 +- 0.0109


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8494 +- 0.0048

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9922 +- 0.0019      1.0 +- 0.0 0.9961 +- 0.001    968.0 +- 0.0
             CD4+ T cell  0.941 +- 0.009 0.7124 +- 0.0102 0.8108 +- 0.0073   4371.0 +- 0.0
             CD8+ T cell 0.6016 +- 0.0082 0.9033 +- 0.0153 0.7221 +- 0.0089   2141.0 +- 0.0
          Dendritic cell 0.9523 +- 0.0076 0.9829 +- 0.0048 0.9673 +- 0.0038    146.0 +- 0.0
                Monocyte 0.9985 +- 0.0006 0.9958 +- 0.0007 0.9971 +- 0.0004   1703.0 +- 0.0
                 NK cell 0.9811 +- 0.0065 0.9617 +- 0.0133 0.9712 +- 0.005    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0  0.81 +- 0.0474 0.8944 +- 0.0287     40.0 +- 0.0

                accuracy                                 0.8494 +- 0.0048   9998.0 +- 0.0
               macro avg 0.9238 +- 0.0022 0.9094 +- 0.0067 0.9084 +- 0.004   9998.0 +- 0.0
            weighted avg  0.886 +- 0.005 0.8494 +- 0.0048 0.8542 +- 0.0047   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8466 +- 0.0051
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8483 +- 0.0047
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8429 +- 0.0053
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8416 +- 0.005
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8266 +- 0.0054


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.903 +- 0.0034
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9078 +- 0.0043
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9049 +- 0.0039
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8749 +- 0.0099
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8678 +- 0.0099


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.8677 +- 0.0086

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9949 +- 0.0019      1.0 +- 0.0 0.9975 +- 0.0009    764.0 +- 0.0
             CD4+ T cell 0.9742 +- 0.0031 0.7138 +- 0.0227 0.8237 +- 0.0147   4116.0 +- 0.0
             CD8+ T cell 0.5305 +- 0.0179 0.9325 +- 0.0114 0.6761 +- 0.014   1457.0 +- 0.0
          Dendritic cell 0.9457 +- 0.0122 0.9665 +- 0.0058 0.9559 +- 0.0067    167.0 +- 0.0
                Monocyte 0.9976 +- 0.0004 0.9958 +- 0.0009 0.9967 +- 0.0005   2413.0 +- 0.0
                 NK cell 0.9796 +- 0.009 0.974 +- 0.0103 0.9768 +- 0.005   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9025 +- 0.0362 0.9484 +- 0.0201     40.0 +- 0.0

                accuracy                                 0.8677 +- 0.0086   9997.0 +- 0.0
               macro avg 0.9175 +- 0.0033 0.9264 +- 0.0059 0.9107 +- 0.0055   9997.0 +- 0.0
            weighted avg  0.917 +- 0.003 0.8677 +- 0.0086 0.8759 +- 0.008   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8651 +- 0.009
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8654 +- 0.0084
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8626 +- 0.0087
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8615 +- 0.0087
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8547 +- 0.0096


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9055 +- 0.0051
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9096 +- 0.0053
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9076 +- 0.0053
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8915 +- 0.0111
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8874 +- 0.0121


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.8611 +- 0.0102

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9578 +- 0.0037      1.0 +- 0.0 0.9785 +- 0.0019    895.0 +- 0.0
             CD4+ T cell 0.7017 +- 0.0137 0.9531 +- 0.0055 0.8082 +- 0.0086   2315.0 +- 0.0
             CD8+ T cell 0.7944 +- 0.037 0.5595 +- 0.0291 0.6561 +- 0.027   2127.0 +- 0.0
          Dendritic cell 0.9925 +- 0.0069 0.8404 +- 0.0143  0.91 +- 0.0072    156.0 +- 0.0
                Monocyte 0.9889 +- 0.0009 0.9987 +- 0.0004 0.9938 +- 0.0004   2614.0 +- 0.0
                 NK cell 0.9975 +- 0.0025 0.8434 +- 0.0471 0.9134 +- 0.0281   1363.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.2478 +- 0.0895 0.3896 +- 0.1179     46.0 +- 0.0

                accuracy                                 0.8611 +- 0.0102   9516.0 +- 0.0
               macro avg 0.919 +- 0.0068 0.7776 +- 0.0168 0.8071 +- 0.0209   9516.0 +- 0.0
            weighted avg   0.874 +- 0.01 0.8611 +- 0.0102 0.8559 +- 0.0109   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8578 +- 0.0118
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8608 +- 0.0101
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8542 +- 0.0101
Feature importance dropout (1.0% features dropped) Accuracy score: 0.849 +- 0.0126
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8493 +- 0.0125


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8043 +- 0.0186
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8069 +- 0.0209
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8022 +- 0.0214
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.7979 +- 0.0225
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.7756 +- 0.0224


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



