# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9201 +- 0.0014

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9994 +- 0.0003      1.0 +- 0.0 0.9997 +- 0.0002   3129.0 +- 0.0
             CD4+ T cell 0.8638 +- 0.0027 0.9688 +- 0.0008 0.9133 +- 0.0015   6465.0 +- 0.0
             CD8+ T cell 0.8762 +- 0.0024 0.8463 +- 0.0035 0.861 +- 0.0027   6401.0 +- 0.0
          Dendritic cell 0.9667 +- 0.0039 0.7909 +- 0.0043  0.87 +- 0.0036    165.0 +- 0.0
                Monocyte 0.9955 +- 0.0002 0.9988 +- 0.0001 0.9971 +- 0.0002   3648.0 +- 0.0
                 NK cell 0.9916 +- 0.0005 0.7812 +- 0.0047 0.8739 +- 0.0031   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9446 +- 0.0132 0.9715 +- 0.007     56.0 +- 0.0

                accuracy                                 0.9201 +- 0.0014  22446.0 +- 0.0
               macro avg 0.9562 +- 0.0005 0.9044 +- 0.002 0.9266 +- 0.0012  22446.0 +- 0.0
            weighted avg 0.9234 +- 0.0013 0.9201 +- 0.0014 0.9193 +- 0.0015  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.914 +- 0.006
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9201 +- 0.0014
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9037 +- 0.0009
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9035 +- 0.0009
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8838 +- 0.0012


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9211 +- 0.0041
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9266 +- 0.0012
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9179 +- 0.0011
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9165 +- 0.0013
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9043 +- 0.001



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.912 +- 0.002

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9977 +- 0.0   0.9988 +- 0.0   0.9983 +- 0.0    866.0 +- 0.0
             CD4+ T cell 0.9259 +- 0.0025 0.8838 +- 0.0049 0.9043 +- 0.0024   4474.0 +- 0.0
             CD8+ T cell 0.8157 +- 0.0061 0.8784 +- 0.0047 0.8459 +- 0.0032   2688.0 +- 0.0
          Dendritic cell 0.9272 +- 0.0005 0.9558 +- 0.0069 0.9413 +- 0.0036    120.0 +- 0.0
                Monocyte 0.9936 +- 0.0005   0.9899 +- 0.0 0.9917 +- 0.0003    889.0 +- 0.0
                 NK cell 0.988 +- 0.0017 0.9841 +- 0.0033 0.986 +- 0.0013    876.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0

                accuracy                                  0.912 +- 0.002   9983.0 +- 0.0
               macro avg 0.9477 +- 0.0008 0.9518 +- 0.0015 0.9494 +- 0.001   9983.0 +- 0.0
            weighted avg 0.9144 +- 0.0017  0.912 +- 0.002 0.9127 +- 0.0019   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8984 +- 0.0074
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9119 +- 0.0021
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8674 +- 0.0045
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8672 +- 0.0046
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8232 +- 0.0019


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.939 +- 0.0042
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9494 +- 0.0011
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9285 +- 0.0021
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9283 +- 0.0022
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.905 +- 0.0009


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8613 +- 0.001

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9969 +- 0.0      1.0 +- 0.0   0.9985 +- 0.0    968.0 +- 0.0
             CD4+ T cell 0.9686 +- 0.0007 0.7138 +- 0.0027 0.8219 +- 0.0017   4371.0 +- 0.0
             CD8+ T cell 0.6167 +- 0.002 0.9497 +- 0.0012 0.7478 +- 0.0014   2141.0 +- 0.0
          Dendritic cell 0.9712 +- 0.0021 0.9479 +- 0.0048 0.9594 +- 0.0024    146.0 +- 0.0
                Monocyte 0.9955 +- 0.0004 0.9976 +- 0.0002 0.9966 +- 0.0002   1703.0 +- 0.0
                 NK cell 0.9894 +- 0.0011 0.9789 +- 0.0017 0.9841 +- 0.0009    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0    0.925 +- 0.0    0.961 +- 0.0     40.0 +- 0.0

                accuracy                                 0.8613 +- 0.001   9998.0 +- 0.0
               macro avg 0.9341 +- 0.0003 0.9304 +- 0.0006 0.9242 +- 0.0004   9998.0 +- 0.0
            weighted avg 0.9021 +- 0.0005 0.8613 +- 0.001 0.8657 +- 0.001   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8663 +- 0.0058
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8612 +- 0.001
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8495 +- 0.0009
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8495 +- 0.0009
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8277 +- 0.0022


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9229 +- 0.0036
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9242 +- 0.0004
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9182 +- 0.0005
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9184 +- 0.0005
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9068 +- 0.0012


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.9413 +- 0.002

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0    764.0 +- 0.0
             CD4+ T cell 0.9884 +- 0.0005 0.8742 +- 0.0056 0.9278 +- 0.0031   4116.0 +- 0.0
             CD8+ T cell 0.7301 +- 0.0083 0.9663 +- 0.0021 0.8317 +- 0.0048   1457.0 +- 0.0
          Dendritic cell 0.9566 +- 0.0025 0.9509 +- 0.0038 0.9538 +- 0.0029    167.0 +- 0.0
                Monocyte 0.9963 +- 0.0003 0.9966 +- 0.0002 0.9964 +- 0.0002   2413.0 +- 0.0
                 NK cell 0.9923 +- 0.0017 0.9962 +- 0.0005 0.9943 +- 0.001   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                 0.9413 +- 0.002   9997.0 +- 0.0
               macro avg 0.952 +- 0.0009 0.9692 +- 0.0006 0.9577 +- 0.0009   9997.0 +- 0.0
            weighted avg 0.9535 +- 0.0009 0.9413 +- 0.002 0.9435 +- 0.0018   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9443 +- 0.0027
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9411 +- 0.002
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9366 +- 0.0019
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9364 +- 0.002
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9351 +- 0.0019


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9572 +- 0.0018
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9576 +- 0.0009
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9545 +- 0.0009
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.954 +- 0.001
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9528 +- 0.001


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.947 +- 0.001

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9989 +- 0.0      1.0 +- 0.0   0.9994 +- 0.0    895.0 +- 0.0
             CD4+ T cell 0.9719 +- 0.0026 0.8777 +- 0.0022 0.9224 +- 0.0013   2315.0 +- 0.0
             CD8+ T cell 0.8348 +- 0.0028 0.9718 +- 0.003 0.8981 +- 0.0021   2127.0 +- 0.0
          Dendritic cell 0.9947 +- 0.005 0.8391 +- 0.0056 0.9103 +- 0.0029    156.0 +- 0.0
                Monocyte 0.988 +- 0.0004 0.9993 +- 0.0003 0.9936 +- 0.0002   2614.0 +- 0.0
                 NK cell 0.9973 +- 0.0012 0.9012 +- 0.0044 0.9468 +- 0.0021   1363.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     46.0 +- 0.0

                accuracy                                  0.947 +- 0.001   9516.0 +- 0.0
               macro avg 0.9694 +- 0.0009 0.9413 +- 0.0012 0.9529 +- 0.0009   9516.0 +- 0.0
            weighted avg 0.9524 +- 0.001  0.947 +- 0.001 0.9474 +- 0.001   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9378 +- 0.0071
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9469 +- 0.001
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9121 +- 0.0029
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9086 +- 0.0027
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9072 +- 0.0018


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9427 +- 0.0073
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9529 +- 0.0009
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9315 +- 0.0019
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9287 +- 0.0018
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.927 +- 0.0013


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



