# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8498 +- 0.0

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0   3129.0 +- 0.0
             CD4+ T cell   0.7003 +- 0.0   0.9805 +- 0.0    0.817 +- 0.0   6465.0 +- 0.0
             CD8+ T cell   0.9482 +- 0.0   0.5057 +- 0.0   0.6596 +- 0.0   6401.0 +- 0.0
          Dendritic cell   0.9855 +- 0.0   0.8242 +- 0.0   0.8977 +- 0.0    165.0 +- 0.0
                Monocyte   0.9945 +- 0.0   0.9995 +- 0.0    0.997 +- 0.0   3648.0 +- 0.0
                 NK cell   0.8463 +- 0.0   0.9806 +- 0.0   0.9085 +- 0.0   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0   0.9821 +- 0.0    0.991 +- 0.0     56.0 +- 0.0

                accuracy                                   0.8498 +- 0.0  22446.0 +- 0.0
               macro avg    0.925 +- 0.0   0.8961 +- 0.0   0.8958 +- 0.0  22446.0 +- 0.0
            weighted avg   0.8802 +- 0.0   0.8498 +- 0.0   0.8384 +- 0.0  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8502 +- 0.0008
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8497 +- 0.0
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8499 +- 0.0
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8503 +- 0.0
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8444 +- 0.0


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8947 +- 0.0008
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8958 +- 0.0
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8966 +- 0.0
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.897 +- 0.0
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8908 +- 0.0



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.7776 +- 0.0

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9977 +- 0.0   0.9988 +- 0.0   0.9983 +- 0.0    866.0 +- 0.0
             CD4+ T cell   0.7606 +- 0.0   0.9345 +- 0.0   0.8386 +- 0.0   4474.0 +- 0.0
             CD8+ T cell   0.7459 +- 0.0   0.2906 +- 0.0   0.4182 +- 0.0   2688.0 +- 0.0
          Dendritic cell   0.9407 +- 0.0    0.925 +- 0.0   0.9328 +- 0.0    120.0 +- 0.0
                Monocyte   0.9899 +- 0.0   0.9921 +- 0.0    0.991 +- 0.0    889.0 +- 0.0
                 NK cell   0.5857 +- 0.0   0.9989 +- 0.0   0.7384 +- 0.0    876.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0

                accuracy                                   0.7776 +- 0.0   9983.0 +- 0.0
               macro avg    0.858 +- 0.0    0.873 +- 0.0   0.8422 +- 0.0   9983.0 +- 0.0
            weighted avg    0.786 +- 0.0   0.7776 +- 0.0   0.7462 +- 0.0   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.778 +- 0.0021
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.7777 +- 0.0
Feature importance dropout (0.5% features dropped) Accuracy score: 0.7711 +- 0.0
Feature importance dropout (1.0% features dropped) Accuracy score: 0.7724 +- 0.0
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7631 +- 0.0


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8427 +- 0.0019
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8425 +- 0.0
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8376 +- 0.0
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8391 +- 0.0
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8314 +- 0.0


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8563 +- 0.0

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9949 +- 0.0      1.0 +- 0.0   0.9974 +- 0.0    968.0 +- 0.0
             CD4+ T cell   0.8482 +- 0.0   0.9012 +- 0.0   0.8739 +- 0.0   4371.0 +- 0.0
             CD8+ T cell   0.7333 +- 0.0   0.5381 +- 0.0   0.6207 +- 0.0   2141.0 +- 0.0
          Dendritic cell   0.9787 +- 0.0   0.9452 +- 0.0   0.9617 +- 0.0    146.0 +- 0.0
                Monocyte   0.9953 +- 0.0   0.9982 +- 0.0   0.9968 +- 0.0   1703.0 +- 0.0
                 NK cell   0.6793 +- 0.0      1.0 +- 0.0    0.809 +- 0.0    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0    0.875 +- 0.0   0.9333 +- 0.0     40.0 +- 0.0

                accuracy                                   0.8563 +- 0.0   9998.0 +- 0.0
               macro avg   0.8899 +- 0.0    0.894 +- 0.0   0.8847 +- 0.0   9998.0 +- 0.0
            weighted avg   0.8547 +- 0.0   0.8563 +- 0.0     0.85 +- 0.0   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8564 +- 0.0016
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8558 +- 0.0
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8541 +- 0.0
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8549 +- 0.0
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8492 +- 0.0


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8839 +- 0.0016
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8845 +- 0.0
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8837 +- 0.0
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.885 +- 0.0
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8795 +- 0.0


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.9163 +- 0.0

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0    764.0 +- 0.0
             CD4+ T cell   0.9476 +- 0.0   0.9227 +- 0.0    0.935 +- 0.0   4116.0 +- 0.0
             CD8+ T cell   0.7541 +- 0.0   0.6651 +- 0.0   0.7068 +- 0.0   1457.0 +- 0.0
          Dendritic cell   0.9795 +- 0.0   0.8563 +- 0.0   0.9137 +- 0.0    167.0 +- 0.0
                Monocyte   0.9901 +- 0.0   0.9988 +- 0.0   0.9944 +- 0.0   2413.0 +- 0.0
                 NK cell   0.7848 +- 0.0   0.9962 +- 0.0    0.878 +- 0.0   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                   0.9163 +- 0.0   9997.0 +- 0.0
               macro avg   0.9223 +- 0.0   0.9199 +- 0.0   0.9183 +- 0.0   9997.0 +- 0.0
            weighted avg   0.9175 +- 0.0   0.9163 +- 0.0    0.915 +- 0.0   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9165 +- 0.0021
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.916 +- 0.0
Feature importance dropout (0.5% features dropped) Accuracy score: 0.916 +- 0.0
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9169 +- 0.0
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9123 +- 0.0


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9184 +- 0.0023
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9181 +- 0.0
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.918 +- 0.0
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9191 +- 0.0
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9142 +- 0.0


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.8236 +- 0.0

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0    895.0 +- 0.0
             CD4+ T cell    0.693 +- 0.0   0.9382 +- 0.0   0.7972 +- 0.0   2315.0 +- 0.0
             CD8+ T cell   0.8227 +- 0.0   0.3206 +- 0.0   0.4614 +- 0.0   2127.0 +- 0.0
          Dendritic cell      1.0 +- 0.0   0.5897 +- 0.0   0.7419 +- 0.0    156.0 +- 0.0
                Monocyte   0.9721 +- 0.0      1.0 +- 0.0   0.9859 +- 0.0   2614.0 +- 0.0
                 NK cell   0.7297 +- 0.0   0.9802 +- 0.0   0.8366 +- 0.0   1363.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     46.0 +- 0.0

                accuracy                                   0.8236 +- 0.0   9516.0 +- 0.0
               macro avg   0.8882 +- 0.0   0.8327 +- 0.0   0.8319 +- 0.0   9516.0 +- 0.0
            weighted avg   0.8393 +- 0.0   0.8236 +- 0.0   0.7988 +- 0.0   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8249 +- 0.002
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8237 +- 0.0
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8129 +- 0.0
Feature importance dropout (1.0% features dropped) Accuracy score: 0.815 +- 0.0
Feature importance dropout (2.0% features dropped) Accuracy score: 0.819 +- 0.0


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8315 +- 0.0024
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.832 +- 0.0
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8219 +- 0.0
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8243 +- 0.0
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.826 +- 0.0


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



