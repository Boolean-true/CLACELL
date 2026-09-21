# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9289 +- 0.0008

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   1.0 +- 0.0001      1.0 +- 0.0   1.0 +- 0.0001   3129.0 +- 0.0
             CD4+ T cell 0.8988 +- 0.0031 0.9615 +- 0.0011 0.9291 +- 0.0015   6465.0 +- 0.0
             CD8+ T cell 0.8687 +- 0.0013 0.8915 +- 0.0035 0.8799 +- 0.0015   6401.0 +- 0.0
          Dendritic cell 0.9406 +- 0.0033 0.8248 +- 0.0067 0.8789 +- 0.0038    165.0 +- 0.0
                Monocyte 0.997 +- 0.0003 0.9976 +- 0.0001 0.9973 +- 0.0001   3648.0 +- 0.0
                 NK cell 0.9928 +- 0.0012 0.762 +- 0.0038 0.8622 +- 0.0028   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9768 +- 0.0086 0.9882 +- 0.0044     56.0 +- 0.0

                accuracy                                 0.9289 +- 0.0008  22446.0 +- 0.0
               macro avg 0.9568 +- 0.0006 0.9163 +- 0.0017 0.9337 +- 0.0011  22446.0 +- 0.0
            weighted avg 0.9316 +- 0.0007 0.9289 +- 0.0008 0.9281 +- 0.0008  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9224 +- 0.0056
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9289 +- 0.0008
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9183 +- 0.0016
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9166 +- 0.0014
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8752 +- 0.0013


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9286 +- 0.0033
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9337 +- 0.0011
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9283 +- 0.0012
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9267 +- 0.0018
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9031 +- 0.0018



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.9196 +- 0.0028

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9977 +- 0.0   0.9988 +- 0.0   0.9983 +- 0.0    866.0 +- 0.0
             CD4+ T cell 0.9523 +- 0.0025 0.8749 +- 0.0055 0.912 +- 0.0035   4474.0 +- 0.0
             CD8+ T cell 0.8112 +- 0.0066 0.9233 +- 0.0041 0.8636 +- 0.0045   2688.0 +- 0.0
          Dendritic cell 0.8972 +- 0.0032 0.9892 +- 0.004 0.9409 +- 0.0013    120.0 +- 0.0
                Monocyte 0.9982 +- 0.0008 0.9847 +- 0.0006 0.9914 +- 0.0004    889.0 +- 0.0
                 NK cell 0.988 +- 0.0028 0.9789 +- 0.0039 0.9834 +- 0.0025    876.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0

                accuracy                                 0.9196 +- 0.0028   9983.0 +- 0.0
               macro avg 0.9472 +- 0.0012 0.9602 +- 0.0011 0.9526 +- 0.0011   9983.0 +- 0.0
            weighted avg 0.9251 +- 0.0024 0.9196 +- 0.0028 0.9206 +- 0.0027   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.915 +- 0.0052
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9196 +- 0.0029
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9004 +- 0.0055
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9001 +- 0.0054
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8092 +- 0.0021


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.948 +- 0.0024
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9525 +- 0.0011
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9436 +- 0.0024
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9439 +- 0.0024
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.897 +- 0.0013


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8633 +- 0.0021

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9969 +- 0.0      1.0 +- 0.0   0.9985 +- 0.0    968.0 +- 0.0
             CD4+ T cell 0.9769 +- 0.0009 0.7118 +- 0.0052 0.8235 +- 0.0035   4371.0 +- 0.0
             CD8+ T cell 0.6179 +- 0.004 0.9624 +- 0.0013 0.7526 +- 0.0029   2141.0 +- 0.0
          Dendritic cell 0.9578 +- 0.0031   0.9795 +- 0.0 0.9685 +- 0.0016    146.0 +- 0.0
                Monocyte   0.9982 +- 0.0 0.9963 +- 0.0003 0.9973 +- 0.0001   1703.0 +- 0.0
                 NK cell 0.9889 +- 0.0022 0.9774 +- 0.0025 0.9831 +- 0.0015    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0    0.925 +- 0.0    0.961 +- 0.0     40.0 +- 0.0

                accuracy                                 0.8633 +- 0.0021   9998.0 +- 0.0
               macro avg 0.9338 +- 0.0007 0.936 +- 0.0007 0.9264 +- 0.0009   9998.0 +- 0.0
            weighted avg 0.9062 +- 0.0009 0.8633 +- 0.0021 0.8676 +- 0.0021   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8707 +- 0.0045
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8632 +- 0.0022
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8598 +- 0.0024
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8599 +- 0.0025
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8171 +- 0.0028


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9262 +- 0.002
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9263 +- 0.0009
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9245 +- 0.0012
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9247 +- 0.0012
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9022 +- 0.0015


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.9366 +- 0.0028

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0    764.0 +- 0.0
             CD4+ T cell 0.991 +- 0.0006 0.8625 +- 0.0071 0.9223 +- 0.0038   4116.0 +- 0.0
             CD8+ T cell 0.7131 +- 0.0103 0.9737 +- 0.0015 0.8232 +- 0.0065   1457.0 +- 0.0
          Dendritic cell 0.8968 +- 0.0044 0.9778 +- 0.0029 0.9356 +- 0.0023    167.0 +- 0.0
                Monocyte 0.9982 +- 0.0003 0.9918 +- 0.0004 0.995 +- 0.0002   2413.0 +- 0.0
                 NK cell 0.9931 +- 0.0017 0.9941 +- 0.0012 0.9936 +- 0.001   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                 0.9366 +- 0.0028   9997.0 +- 0.0
               macro avg 0.9417 +- 0.0015 0.9714 +- 0.0008 0.9528 +- 0.0014   9997.0 +- 0.0
            weighted avg 0.9516 +- 0.0013 0.9366 +- 0.0028 0.9393 +- 0.0025   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9404 +- 0.0027
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9365 +- 0.0028
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9345 +- 0.0028
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9342 +- 0.0028
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9283 +- 0.002


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.954 +- 0.0015
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9528 +- 0.0015
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9513 +- 0.0014
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.951 +- 0.0015
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9458 +- 0.001


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.9483 +- 0.0017

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9989 +- 0.0      1.0 +- 0.0   0.9994 +- 0.0    895.0 +- 0.0
             CD4+ T cell 0.9858 +- 0.0018 0.8827 +- 0.0047 0.9314 +- 0.0024   2315.0 +- 0.0
             CD8+ T cell 0.8293 +- 0.0062 0.9854 +- 0.0026 0.9006 +- 0.0031   2127.0 +- 0.0
          Dendritic cell 0.981 +- 0.0034 0.891 +- 0.0043 0.9338 +- 0.0028    156.0 +- 0.0
                Monocyte 0.991 +- 0.0003 0.9986 +- 0.0002 0.9948 +- 0.0002   2614.0 +- 0.0
                 NK cell 0.997 +- 0.0022 0.8762 +- 0.0127 0.9327 +- 0.0066   1363.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     46.0 +- 0.0

                accuracy                                 0.9483 +- 0.0017   9516.0 +- 0.0
               macro avg 0.969 +- 0.0009 0.9477 +- 0.0017 0.9561 +- 0.0014   9516.0 +- 0.0
            weighted avg 0.9551 +- 0.0011 0.9483 +- 0.0017 0.9489 +- 0.0017   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9293 +- 0.0086
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9483 +- 0.0017
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9348 +- 0.0029
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9305 +- 0.0031
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9291 +- 0.0026


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9396 +- 0.0067
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9561 +- 0.0014
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9479 +- 0.0019
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9444 +- 0.0022
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9432 +- 0.0021


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



