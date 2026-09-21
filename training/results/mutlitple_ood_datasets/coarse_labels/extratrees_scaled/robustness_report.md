# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.919 +- 0.0015

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9998 +- 0.0002      1.0 +- 0.0 0.9999 +- 0.0001   3129.0 +- 0.0
             CD4+ T cell 0.8878 +- 0.004 0.9663 +- 0.0011 0.9254 +- 0.0022   6465.0 +- 0.0
             CD8+ T cell 0.8487 +- 0.0015 0.879 +- 0.0049 0.8636 +- 0.0029   6401.0 +- 0.0
          Dendritic cell 0.9952 +- 0.0041 0.7521 +- 0.0053 0.8567 +- 0.0036    165.0 +- 0.0
                Monocyte 0.9942 +- 0.0003 0.9998 +- 0.0001 0.997 +- 0.0001   3648.0 +- 0.0
                 NK cell 0.9978 +- 0.0006 0.6966 +- 0.0018 0.8204 +- 0.0012   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9804 +- 0.0101 0.9901 +- 0.0052     56.0 +- 0.0

                accuracy                                 0.919 +- 0.0015  22446.0 +- 0.0
               macro avg 0.9605 +- 0.0007 0.8963 +- 0.0016 0.9219 +- 0.001  22446.0 +- 0.0
            weighted avg 0.9233 +- 0.0014 0.919 +- 0.0015 0.9174 +- 0.0015  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9085 +- 0.0042
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.919 +- 0.0015
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9061 +- 0.0019
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9052 +- 0.0019
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8654 +- 0.0016


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.906 +- 0.0017
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9219 +- 0.001
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9144 +- 0.0011
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9122 +- 0.0011
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8833 +- 0.002



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.9178 +- 0.0017

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9969 +- 0.0006   0.9988 +- 0.0 0.9979 +- 0.0003    866.0 +- 0.0
             CD4+ T cell 0.9423 +- 0.0049 0.8833 +- 0.0054 0.9118 +- 0.002   4474.0 +- 0.0
             CD8+ T cell 0.8159 +- 0.006 0.9078 +- 0.0087 0.8593 +- 0.0032   2688.0 +- 0.0
          Dendritic cell 0.9455 +- 0.0053 0.8967 +- 0.0131 0.9204 +- 0.0075    120.0 +- 0.0
                Monocyte 0.9869 +- 0.0018 0.993 +- 0.0007   0.99 +- 0.001    889.0 +- 0.0
                 NK cell 0.9933 +- 0.0013 0.9672 +- 0.0037 0.9801 +- 0.0016    876.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0

                accuracy                                 0.9178 +- 0.0017   9983.0 +- 0.0
               macro avg 0.9523 +- 0.0008 0.9455 +- 0.002 0.9483 +- 0.0012   9983.0 +- 0.0
            weighted avg 0.9218 +- 0.0018 0.9178 +- 0.0017 0.9187 +- 0.0017   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9048 +- 0.0064
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9177 +- 0.0017
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8881 +- 0.0045
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8874 +- 0.0046
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8083 +- 0.0019


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9348 +- 0.0053
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9482 +- 0.0012
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9338 +- 0.0028
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9331 +- 0.0028
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8919 +- 0.0014


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8644 +- 0.0021

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9963 +- 0.0005      1.0 +- 0.0 0.9981 +- 0.0003    968.0 +- 0.0
             CD4+ T cell 0.9781 +- 0.0005 0.7152 +- 0.005 0.8262 +- 0.0032   4371.0 +- 0.0
             CD8+ T cell 0.6206 +- 0.0038 0.9653 +- 0.0011 0.7555 +- 0.0027   2141.0 +- 0.0
          Dendritic cell 0.9761 +- 0.0047 0.9219 +- 0.0066 0.9482 +- 0.003    146.0 +- 0.0
                Monocyte 0.9933 +- 0.0006 0.9981 +- 0.0004 0.9957 +- 0.0002   1703.0 +- 0.0
                 NK cell 0.9933 +- 0.0012 0.9706 +- 0.0038 0.9818 +- 0.0019    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0  0.91 +- 0.0129 0.9528 +- 0.0071     40.0 +- 0.0

                accuracy                                 0.8644 +- 0.0021   9998.0 +- 0.0
               macro avg 0.9368 +- 0.001 0.9259 +- 0.0027 0.9226 +- 0.0019   9998.0 +- 0.0
            weighted avg 0.9069 +- 0.0008 0.8644 +- 0.0021 0.8687 +- 0.002   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8679 +- 0.0067
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8644 +- 0.0019
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8594 +- 0.0022
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8592 +- 0.0023
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8222 +- 0.0032


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9162 +- 0.0036
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9227 +- 0.0018
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9197 +- 0.0017
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9183 +- 0.002
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8994 +- 0.0019


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.933 +- 0.0038

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0    764.0 +- 0.0
             CD4+ T cell 0.9907 +- 0.0009 0.8544 +- 0.0097 0.9175 +- 0.0053   4116.0 +- 0.0
             CD8+ T cell 0.6993 +- 0.0135 0.9759 +- 0.0025 0.8147 +- 0.0084   1457.0 +- 0.0
          Dendritic cell 0.974 +- 0.0067 0.897 +- 0.0068 0.9339 +- 0.0042    167.0 +- 0.0
                Monocyte 0.9929 +- 0.0005 0.9979 +- 0.0004 0.9954 +- 0.0003   2413.0 +- 0.0
                 NK cell 0.9972 +- 0.0006 0.9873 +- 0.0021 0.9922 +- 0.0012   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                 0.933 +- 0.0038   9997.0 +- 0.0
               macro avg 0.9506 +- 0.0021 0.9589 +- 0.0016 0.9505 +- 0.0021   9997.0 +- 0.0
            weighted avg 0.9499 +- 0.0017 0.933 +- 0.0038 0.936 +- 0.0034   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9349 +- 0.0031
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9329 +- 0.0038
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9296 +- 0.0038
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9292 +- 0.0039
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9224 +- 0.0039


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9441 +- 0.0033
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9505 +- 0.0022
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9479 +- 0.0022
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9475 +- 0.0023
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9414 +- 0.0018


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.928 +- 0.0046

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9989 +- 0.0      1.0 +- 0.0   0.9994 +- 0.0    895.0 +- 0.0
             CD4+ T cell 0.9872 +- 0.0019 0.8617 +- 0.0045 0.9202 +- 0.0029   2315.0 +- 0.0
             CD8+ T cell 0.7744 +- 0.0119 0.9883 +- 0.0018 0.8683 +- 0.008   2127.0 +- 0.0
          Dendritic cell      1.0 +- 0.0 0.7474 +- 0.0125 0.8554 +- 0.0082    156.0 +- 0.0
                Monocyte 0.983 +- 0.0007   0.9996 +- 0.0 0.9912 +- 0.0004   2614.0 +- 0.0
                 NK cell 0.9999 +- 0.0003  0.78 +- 0.0301 0.8761 +- 0.019   1363.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     46.0 +- 0.0

                accuracy                                 0.928 +- 0.0046   9516.0 +- 0.0
               macro avg 0.9633 +- 0.0019 0.911 +- 0.0047 0.9301 +- 0.0041   9516.0 +- 0.0
            weighted avg 0.9417 +- 0.003 0.928 +- 0.0046 0.9286 +- 0.0047   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9079 +- 0.0107
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9279 +- 0.0046
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9152 +- 0.0057
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9055 +- 0.0077
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9029 +- 0.0073


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9029 +- 0.0099
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.93 +- 0.0041
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9225 +- 0.0047
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9138 +- 0.0065
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9109 +- 0.006


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



