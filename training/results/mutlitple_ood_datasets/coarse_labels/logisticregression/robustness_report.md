# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9187 +- 0.0019

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9999 +- 0.0001 0.9995 +- 0.0004 0.9997 +- 0.0002   3129.0 +- 0.0
             CD4+ T cell 0.8838 +- 0.0026 0.9191 +- 0.0013 0.9011 +- 0.0017   6465.0 +- 0.0
             CD8+ T cell 0.8521 +- 0.005 0.8728 +- 0.003 0.8623 +- 0.0033   6401.0 +- 0.0
          Dendritic cell 0.8414 +- 0.0554 0.9206 +- 0.0186 0.878 +- 0.0279    165.0 +- 0.0
                Monocyte 0.9987 +- 0.0011 0.9921 +- 0.0034 0.9953 +- 0.0016   3648.0 +- 0.0
                 NK cell 0.9822 +- 0.0008 0.8278 +- 0.0106 0.8984 +- 0.0061   2582.0 +- 0.0
             Plasma cell 0.9793 +- 0.0176 0.9982 +- 0.0056 0.9886 +- 0.0093     56.0 +- 0.0

                accuracy                                 0.9187 +- 0.0019  22446.0 +- 0.0
               macro avg 0.9339 +- 0.0074 0.9329 +- 0.0038 0.9319 +- 0.0039  22446.0 +- 0.0
            weighted avg 0.9209 +- 0.0017 0.9187 +- 0.0019 0.9188 +- 0.0019  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9122 +- 0.0072
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9187 +- 0.0019
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9079 +- 0.0015
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9092 +- 0.0013
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8791 +- 0.0015


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9212 +- 0.0103
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9319 +- 0.0039
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9249 +- 0.004
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9263 +- 0.004
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9105 +- 0.0037



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.8743 +- 0.0072

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9945 +- 0.0018   0.9988 +- 0.0 0.9967 +- 0.0009    866.0 +- 0.0
             CD4+ T cell 0.9712 +- 0.0013 0.7683 +- 0.0142 0.8578 +- 0.0086   4474.0 +- 0.0
             CD8+ T cell 0.7185 +- 0.009 0.9312 +- 0.0074 0.8111 +- 0.0061   2688.0 +- 0.0
          Dendritic cell 0.7996 +- 0.0616 0.9733 +- 0.0129 0.8767 +- 0.038    120.0 +- 0.0
                Monocyte 0.9232 +- 0.0525 0.9837 +- 0.0052 0.9517 +- 0.0264    889.0 +- 0.0
                 NK cell 0.9356 +- 0.0077 0.9861 +- 0.001 0.9602 +- 0.0042    876.0 +- 0.0
             Plasma cell 0.9771 +- 0.0073   0.9714 +- 0.0 0.9742 +- 0.0036     70.0 +- 0.0

                accuracy                                 0.8743 +- 0.0072   9983.0 +- 0.0
               macro avg 0.9028 +- 0.0145 0.9447 +- 0.0037 0.9183 +- 0.0094   9983.0 +- 0.0
            weighted avg 0.8958 +- 0.0059 0.8743 +- 0.0072 0.8757 +- 0.0076   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8661 +- 0.008
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8737 +- 0.0072
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8697 +- 0.0071
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8699 +- 0.007
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8123 +- 0.0091


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9038 +- 0.0153
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9178 +- 0.0095
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9148 +- 0.0104
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.915 +- 0.0104
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.881 +- 0.0156


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8099 +- 0.0043

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9959 +- 0.0008 0.9996 +- 0.0005 0.9977 +- 0.0004    968.0 +- 0.0
             CD4+ T cell 0.9829 +- 0.0004 0.5874 +- 0.0094 0.7353 +- 0.0073   4371.0 +- 0.0
             CD8+ T cell 0.5372 +- 0.0045 0.9666 +- 0.003 0.6906 +- 0.0039   2141.0 +- 0.0
          Dendritic cell 0.9172 +- 0.0336 0.9733 +- 0.0153 0.9438 +- 0.0137    146.0 +- 0.0
                Monocyte 0.9803 +- 0.0138 0.9934 +- 0.0033 0.9867 +- 0.0066   1703.0 +- 0.0
                 NK cell 0.9675 +- 0.0046 0.9892 +- 0.0022 0.9782 +- 0.0018    629.0 +- 0.0
             Plasma cell 0.9893 +- 0.0138  0.92 +- 0.0105 0.9534 +- 0.0109     40.0 +- 0.0

                accuracy                                 0.8099 +- 0.0043   9998.0 +- 0.0
               macro avg  0.91 +- 0.0041 0.9185 +- 0.003 0.898 +- 0.0027   9998.0 +- 0.0
            weighted avg 0.8864 +- 0.0029 0.8099 +- 0.0043 0.8132 +- 0.0048   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8088 +- 0.0091
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8086 +- 0.0043
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8076 +- 0.0041
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8073 +- 0.0041
Feature importance dropout (2.0% features dropped) Accuracy score: 0.801 +- 0.0047


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8905 +- 0.0089
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8974 +- 0.0027
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8971 +- 0.0027
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8957 +- 0.0027
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8903 +- 0.0031


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.8743 +- 0.0068

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9949 +- 0.004      1.0 +- 0.0 0.9975 +- 0.002    764.0 +- 0.0
             CD4+ T cell 0.9896 +- 0.0002 0.7186 +- 0.0167 0.8325 +- 0.0114   4116.0 +- 0.0
             CD8+ T cell 0.5488 +- 0.013 0.9503 +- 0.0024 0.6957 +- 0.0106   1457.0 +- 0.0
          Dendritic cell   0.89 +- 0.041 0.9653 +- 0.0201 0.9253 +- 0.0167    167.0 +- 0.0
                Monocyte 0.9912 +- 0.0064 0.992 +- 0.0036 0.9916 +- 0.0024   2413.0 +- 0.0
                 NK cell 0.9637 +- 0.002 0.9992 +- 0.0006 0.9811 +- 0.0011   1040.0 +- 0.0
             Plasma cell 0.9854 +- 0.0126      1.0 +- 0.0 0.9926 +- 0.0064     40.0 +- 0.0

                accuracy                                 0.8743 +- 0.0068   9997.0 +- 0.0
               macro avg 0.9091 +- 0.0053 0.9465 +- 0.0049 0.9166 +- 0.0039   9997.0 +- 0.0
            weighted avg 0.9218 +- 0.0028 0.8743 +- 0.0068 0.8812 +- 0.0066   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8741 +- 0.0099
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8727 +- 0.007
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8711 +- 0.007
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8717 +- 0.0069
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8838 +- 0.0079


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9118 +- 0.0077
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9158 +- 0.0039
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9148 +- 0.004
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9155 +- 0.0038
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9192 +- 0.0041


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.918 +- 0.008

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9987 +- 0.0007      1.0 +- 0.0 0.9993 +- 0.0004    895.0 +- 0.0
             CD4+ T cell 0.9901 +- 0.0007 0.7557 +- 0.0263 0.857 +- 0.0165   2315.0 +- 0.0
             CD8+ T cell 0.7639 +- 0.0178 0.949 +- 0.0108 0.8464 +- 0.0135   2127.0 +- 0.0
          Dendritic cell 0.8903 +- 0.0525 0.9013 +- 0.0222 0.8945 +- 0.0228    156.0 +- 0.0
                Monocyte 0.9901 +- 0.002 0.9953 +- 0.0031 0.9927 +- 0.0012   2614.0 +- 0.0
                 NK cell 0.9341 +- 0.0159 0.9425 +- 0.0016 0.9382 +- 0.0083   1363.0 +- 0.0
             Plasma cell 0.9631 +- 0.0283      1.0 +- 0.0 0.981 +- 0.0147     46.0 +- 0.0

                accuracy                                  0.918 +- 0.008   9516.0 +- 0.0
               macro avg 0.9329 +- 0.0118 0.9348 +- 0.0072 0.9299 +- 0.0091   9516.0 +- 0.0
            weighted avg 0.9306 +- 0.0061  0.918 +- 0.008 0.9181 +- 0.0081   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9072 +- 0.0069
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9176 +- 0.0079
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9151 +- 0.0076
Feature importance dropout (1.0% features dropped) Accuracy score: 0.916 +- 0.0072
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9143 +- 0.0076


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9169 +- 0.0093
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9296 +- 0.0091
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.928 +- 0.0089
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9288 +- 0.0086
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9289 +- 0.0077


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



