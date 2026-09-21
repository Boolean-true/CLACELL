# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9076 +- 0.0013

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9996 +- 0.0003      1.0 +- 0.0 0.9998 +- 0.0001   3129.0 +- 0.0
             CD4+ T cell 0.8406 +- 0.0033 0.9684 +- 0.0008   0.9 +- 0.0017   6465.0 +- 0.0
             CD8+ T cell 0.8636 +- 0.0012 0.8101 +- 0.0048 0.836 +- 0.0028   6401.0 +- 0.0
          Dendritic cell 0.9684 +- 0.0034 0.7976 +- 0.0031 0.8747 +- 0.0023    165.0 +- 0.0
                Monocyte 0.9959 +- 0.0001 0.9988 +- 0.0001 0.9973 +- 0.0001   3648.0 +- 0.0
                 NK cell 0.9765 +- 0.001 0.7622 +- 0.0023 0.8562 +- 0.0015   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9589 +- 0.0169 0.979 +- 0.0088     56.0 +- 0.0

                accuracy                                 0.9076 +- 0.0013  22446.0 +- 0.0
               macro avg 0.9492 +- 0.0009 0.8994 +- 0.0023 0.9204 +- 0.0013  22446.0 +- 0.0
            weighted avg 0.9115 +- 0.0011 0.9076 +- 0.0013 0.9064 +- 0.0013  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9033 +- 0.0016
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9076 +- 0.0013
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8956 +- 0.0012
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8948 +- 0.001
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8842 +- 0.0005


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9153 +- 0.001
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9204 +- 0.0013
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9139 +- 0.0012
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9109 +- 0.0014
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9042 +- 0.0012



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.8972 +- 0.0019

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9975 +- 0.0005   0.9988 +- 0.0 0.9982 +- 0.0002    866.0 +- 0.0
             CD4+ T cell 0.9286 +- 0.0038  0.85 +- 0.0031 0.8876 +- 0.0022   4474.0 +- 0.0
             CD8+ T cell 0.7721 +- 0.0034 0.886 +- 0.0064 0.8251 +- 0.0035   2688.0 +- 0.0
          Dendritic cell 0.9271 +- 0.0003 0.9533 +- 0.0043  0.94 +- 0.0022    120.0 +- 0.0
                Monocyte 0.9948 +- 0.0006   0.9899 +- 0.0 0.9923 +- 0.0003    889.0 +- 0.0
                 NK cell 0.9835 +- 0.0015 0.964 +- 0.0018 0.9737 +- 0.0014    876.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0

                accuracy                                 0.8972 +- 0.0019   9983.0 +- 0.0
               macro avg 0.9413 +- 0.0007 0.9448 +- 0.0011 0.9422 +- 0.0008   9983.0 +- 0.0
            weighted avg 0.9035 +- 0.002 0.8972 +- 0.0019 0.8985 +- 0.0019   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8855 +- 0.0046
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8971 +- 0.0019
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8726 +- 0.0018
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8717 +- 0.0018
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8483 +- 0.0036


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9326 +- 0.0029
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9422 +- 0.0009
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9294 +- 0.0009
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9287 +- 0.001
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9179 +- 0.0017


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8782 +- 0.0014

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9969 +- 0.0      1.0 +- 0.0   0.9985 +- 0.0    968.0 +- 0.0
             CD4+ T cell 0.9618 +- 0.002 0.761 +- 0.0034 0.8497 +- 0.0019   4371.0 +- 0.0
             CD8+ T cell 0.6534 +- 0.003 0.9331 +- 0.0037 0.7686 +- 0.0022   2141.0 +- 0.0
          Dendritic cell 0.9719 +- 0.0001 0.9493 +- 0.0035 0.9605 +- 0.0019    146.0 +- 0.0
                Monocyte 0.9957 +- 0.0003   0.9977 +- 0.0 0.9967 +- 0.0002   1703.0 +- 0.0
                 NK cell 0.9825 +- 0.0014 0.9757 +- 0.0029 0.9791 +- 0.0017    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0    0.925 +- 0.0    0.961 +- 0.0     40.0 +- 0.0

                accuracy                                 0.8782 +- 0.0014   9998.0 +- 0.0
               macro avg 0.9375 +- 0.0006 0.9345 +- 0.001 0.9306 +- 0.0008   9998.0 +- 0.0
            weighted avg 0.9065 +- 0.0011 0.8782 +- 0.0014 0.882 +- 0.0013   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8778 +- 0.0023
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8782 +- 0.0014
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8692 +- 0.0015
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8693 +- 0.0014
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8544 +- 0.0011


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9277 +- 0.0015
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9306 +- 0.0008
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9261 +- 0.0009
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9262 +- 0.0009
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9191 +- 0.0005


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.9116 +- 0.0017

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0    764.0 +- 0.0
             CD4+ T cell 0.9842 +- 0.0006 0.8081 +- 0.0041 0.8875 +- 0.0025   4116.0 +- 0.0
             CD8+ T cell 0.6337 +- 0.005 0.959 +- 0.0012 0.7631 +- 0.0038   1457.0 +- 0.0
          Dendritic cell 0.9583 +- 0.0032 0.9503 +- 0.004 0.9543 +- 0.0019    167.0 +- 0.0
                Monocyte 0.9963 +- 0.0004 0.9967 +- 0.0002 0.9965 +- 0.0002   2413.0 +- 0.0
                 NK cell 0.9931 +- 0.0007 0.9828 +- 0.001 0.9879 +- 0.0007   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                 0.9116 +- 0.0017   9997.0 +- 0.0
               macro avg 0.938 +- 0.0009 0.9567 +- 0.0006 0.9413 +- 0.0008   9997.0 +- 0.0
            weighted avg 0.9378 +- 0.0008 0.9116 +- 0.0017 0.9163 +- 0.0016   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9126 +- 0.0029
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9113 +- 0.0017
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9084 +- 0.0015
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9077 +- 0.0017
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9023 +- 0.0016


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.939 +- 0.0018
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9412 +- 0.0008
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.939 +- 0.0007
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9381 +- 0.0008
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9351 +- 0.001


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.9188 +- 0.0027

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9988 +- 0.0004      1.0 +- 0.0 0.9994 +- 0.0002    895.0 +- 0.0
             CD4+ T cell 0.8655 +- 0.0075 0.9173 +- 0.002 0.8906 +- 0.0035   2315.0 +- 0.0
             CD8+ T cell 0.8164 +- 0.0053 0.8436 +- 0.0106 0.8297 +- 0.0065   2127.0 +- 0.0
          Dendritic cell 0.997 +- 0.0039 0.8359 +- 0.0062 0.9093 +- 0.0039    156.0 +- 0.0
                Monocyte 0.9876 +- 0.0004 0.9995 +- 0.0002 0.9935 +- 0.0002   2614.0 +- 0.0
                 NK cell 0.9963 +- 0.0013 0.8375 +- 0.0115  0.91 +- 0.0066   1363.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     46.0 +- 0.0

                accuracy                                 0.9188 +- 0.0027   9516.0 +- 0.0
               macro avg 0.9516 +- 0.0017 0.9191 +- 0.0026 0.9332 +- 0.0023   9516.0 +- 0.0
            weighted avg 0.9221 +- 0.0025 0.9188 +- 0.0027 0.9191 +- 0.0027   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9033 +- 0.0054
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9188 +- 0.0027
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8961 +- 0.0021
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8872 +- 0.0024
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8857 +- 0.0022


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9189 +- 0.0044
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9332 +- 0.0022
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9189 +- 0.0016
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9113 +- 0.0019
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9099 +- 0.0018


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



