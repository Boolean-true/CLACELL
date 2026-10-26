# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.7987 +- 0.0024

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9682 +- 0.0024 0.4284 +- 0.0045 0.594 +- 0.0045   3032.0 +- 0.0
        Endothelial cell  0.986 +- 0.001 0.8882 +- 0.0032 0.9345 +- 0.0017   1352.0 +- 0.0
         Epithelial cell 0.9727 +- 0.0017 0.8984 +- 0.0032 0.934 +- 0.0015  13395.0 +- 0.0
            Myeloid cell 0.9949 +- 0.0007 0.8869 +- 0.0028 0.9378 +- 0.0014   7844.0 +- 0.0
     Natural killer cell 0.7478 +- 0.0333 0.0696 +- 0.0114 0.1271 +- 0.019   1768.0 +- 0.0
             Plasma cell 0.9777 +- 0.0022 0.6152 +- 0.0143 0.7551 +- 0.0109    989.0 +- 0.0
                Rejected      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0
            Stromal cell 0.9916 +- 0.0006 0.9474 +- 0.0022 0.969 +- 0.0012   3657.0 +- 0.0
                  T cell 0.9025 +- 0.0024 0.7924 +- 0.0075 0.8438 +- 0.0036  15281.0 +- 0.0

                accuracy                                 0.7987 +- 0.0024  47318.0 +- 0.0
               macro avg 0.8379 +- 0.0036 0.614 +- 0.0026 0.6773 +- 0.0029  47318.0 +- 0.0
            weighted avg 0.9469 +- 0.0017 0.7987 +- 0.0024 0.8526 +- 0.0014  47318.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7857 +- 0.0029
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.7985 +- 0.0024
Feature importance dropout (0.5% features dropped) Accuracy score: 0.7956 +- 0.0022
Feature importance dropout (1.0% features dropped) Accuracy score: 0.795 +- 0.0021
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7917 +- 0.0024


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6618 +- 0.0045
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6772 +- 0.0029
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6644 +- 0.0018
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6608 +- 0.0018
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6585 +- 0.002



## Out of data distribution 

### OOD Dataset: All 

Baseline accuracy score: N/A

### Classification Report 

                               precision          recall        f1-score         support

                  B cell             N/A             N/A             N/A             N/A
        Endothelial cell             N/A             N/A             N/A             N/A
         Epithelial cell             N/A             N/A             N/A             N/A
            Myeloid cell             N/A             N/A             N/A             N/A
     Natural killer cell             N/A             N/A             N/A             N/A
             Plasma cell             N/A             N/A             N/A             N/A
                Rejected             N/A             N/A             N/A             N/A
            Stromal cell             N/A             N/A             N/A             N/A
                  T cell             N/A             N/A             N/A             N/A

                accuracy                                             N/A             N/A
               macro avg             N/A             N/A             N/A             N/A
            weighted avg             N/A             N/A             N/A             N/A

### Further Robustness Evaluation with metric: Accuracy 



### Further Robustness Evaluation with metric: Macro_F1 



