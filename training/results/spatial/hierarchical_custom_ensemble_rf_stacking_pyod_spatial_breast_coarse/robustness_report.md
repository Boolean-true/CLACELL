# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.0091 +- 0.0037

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.442 +- 0.4698 0.0025 +- 0.0035  0.005 +- 0.007   3032.0 +- 0.0
        Endothelial cell 0.8365 +- 0.1152 0.0271 +- 0.0236 0.0518 +- 0.0443   1352.0 +- 0.0
         Epithelial cell 0.9682 +- 0.0247 0.021 +- 0.0145 0.0408 +- 0.0273  13395.0 +- 0.0
            Myeloid cell 0.4204 +- 0.2561 0.0011 +- 0.0015 0.0022 +- 0.003   7844.0 +- 0.0
     Natural killer cell 0.3738 +- 0.4247 0.0007 +- 0.0008 0.0014 +- 0.0017   1768.0 +- 0.0
             Plasma cell 0.922 +- 0.0829 0.0421 +- 0.0505 0.0767 +- 0.0872    989.0 +- 0.0
                Rejected      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0
            Stromal cell 0.7403 +- 0.0919 0.0138 +- 0.0081 0.0271 +- 0.0157   3657.0 +- 0.0
                  T cell  0.25 +- 0.4249      0.0 +- 0.0 0.0001 +- 0.0001  15281.0 +- 0.0

                accuracy                                 0.0091 +- 0.0037  47318.0 +- 0.0
               macro avg 0.5504 +- 0.0658 0.012 +- 0.0052 0.0228 +- 0.009  47318.0 +- 0.0
            weighted avg 0.5672 +- 0.1476 0.0091 +- 0.0037 0.0175 +- 0.0071  47318.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.0056 +- 0.0022
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.009 +- 0.0037
Feature importance dropout (0.5% features dropped) Accuracy score: 0.009 +- 0.0037
Feature importance dropout (1.0% features dropped) Accuracy score: 0.0088 +- 0.0037
Feature importance dropout (2.0% features dropped) Accuracy score: 0.0084 +- 0.0036


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.0157 +- 0.0082
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.0227 +- 0.009
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.0216 +- 0.0084
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.0204 +- 0.0065
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.019 +- 0.0064



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



