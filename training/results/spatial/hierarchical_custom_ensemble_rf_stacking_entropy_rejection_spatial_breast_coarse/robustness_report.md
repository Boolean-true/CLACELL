# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.7871 +- 0.0023

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9698 +- 0.0029 0.3844 +- 0.014 0.5504 +- 0.0141   3032.0 +- 0.0
        Endothelial cell 0.9853 +- 0.0007 0.8985 +- 0.0026 0.9399 +- 0.0013   1352.0 +- 0.0
         Epithelial cell  0.967 +- 0.002 0.896 +- 0.0031 0.9302 +- 0.0013  13395.0 +- 0.0
            Myeloid cell 0.9933 +- 0.0006 0.8897 +- 0.0014 0.9386 +- 0.0008   7844.0 +- 0.0
     Natural killer cell 0.7062 +- 0.0131 0.2067 +- 0.0164 0.3194 +- 0.0188   1768.0 +- 0.0
             Plasma cell 0.9807 +- 0.0037 0.636 +- 0.0119 0.7715 +- 0.0079    989.0 +- 0.0
                Rejected      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0
            Stromal cell 0.9878 +- 0.0006 0.9534 +- 0.0018 0.9703 +- 0.001   3657.0 +- 0.0
                  T cell 0.8954 +- 0.0017 0.7462 +- 0.0062 0.814 +- 0.0033  15281.0 +- 0.0

                accuracy                                 0.7871 +- 0.0023  47318.0 +- 0.0
               macro avg 0.8317 +- 0.0014 0.6234 +- 0.0023 0.6927 +- 0.0027  47318.0 +- 0.0
            weighted avg 0.9411 +- 0.0005 0.7871 +- 0.0023 0.847 +- 0.0018  47318.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7677 +- 0.0026
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.7865 +- 0.0023
Feature importance dropout (0.5% features dropped) Accuracy score: 0.7818 +- 0.0021
Feature importance dropout (1.0% features dropped) Accuracy score: 0.7801 +- 0.0022
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7752 +- 0.0021


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6765 +- 0.0031
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6926 +- 0.0027
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.676 +- 0.003
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6705 +- 0.0029
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6676 +- 0.0027



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



