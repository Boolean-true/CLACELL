# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8522 +- 0.0021

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9029 +- 0.0078 0.6329 +- 0.0145 0.7441 +- 0.0102   3032.0 +- 0.0
        Endothelial cell 0.9778 +- 0.0018 0.8938 +- 0.0079 0.9339 +- 0.0043   1352.0 +- 0.0
         Epithelial cell 0.9168 +- 0.005 0.8826 +- 0.0082 0.8993 +- 0.0048  13395.0 +- 0.0
            Myeloid cell 0.9826 +- 0.001 0.8737 +- 0.0086 0.9249 +- 0.0049   7844.0 +- 0.0
     Natural killer cell   0.7 +- 0.0083 0.2215 +- 0.0127 0.3363 +- 0.0146   1768.0 +- 0.0
             Plasma cell 0.9204 +- 0.0089 0.4616 +- 0.0233 0.6145 +- 0.0215    989.0 +- 0.0
                Rejected      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0
            Stromal cell 0.9843 +- 0.0009 0.9148 +- 0.0075 0.9483 +- 0.0041   3657.0 +- 0.0
                  T cell 0.8148 +- 0.0017 0.9377 +- 0.0038 0.8719 +- 0.001  15281.0 +- 0.0

                accuracy                                 0.8522 +- 0.0021  47318.0 +- 0.0
               macro avg   0.8 +- 0.0015 0.6465 +- 0.002 0.697 +- 0.0018  47318.0 +- 0.0
            weighted avg 0.8928 +- 0.0012 0.8522 +- 0.0021 0.8625 +- 0.0012  47318.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8466 +- 0.003
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8522 +- 0.0021
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8486 +- 0.0023
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8508 +- 0.0019
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8493 +- 0.002


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6895 +- 0.0031
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.697 +- 0.0018
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6853 +- 0.002
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.694 +- 0.0027
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6922 +- 0.0027



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



