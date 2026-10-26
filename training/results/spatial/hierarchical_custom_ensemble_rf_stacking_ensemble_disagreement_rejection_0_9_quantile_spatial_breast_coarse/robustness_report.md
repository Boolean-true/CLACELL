# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8044 +- 0.0054

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.8995 +- 0.0045 0.5822 +- 0.0178 0.7067 +- 0.0127   3032.0 +- 0.0
        Endothelial cell 0.9755 +- 0.0026 0.8225 +- 0.0154 0.8924 +- 0.009   1352.0 +- 0.0
         Epithelial cell 0.9109 +- 0.0058 0.8043 +- 0.0245 0.8541 +- 0.0159  13395.0 +- 0.0
            Myeloid cell 0.982 +- 0.0012 0.8055 +- 0.0109 0.885 +- 0.0068   7844.0 +- 0.0
     Natural killer cell 0.6906 +- 0.0133 0.2116 +- 0.0061 0.3239 +- 0.0079   1768.0 +- 0.0
             Plasma cell 0.9117 +- 0.0103 0.3785 +- 0.0322 0.5342 +- 0.0319    989.0 +- 0.0
                Rejected      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0
            Stromal cell 0.9841 +- 0.0013 0.8596 +- 0.0093 0.9176 +- 0.0051   3657.0 +- 0.0
                  T cell 0.8149 +- 0.002 0.9295 +- 0.004 0.8684 +- 0.0016  15281.0 +- 0.0

                accuracy                                 0.8044 +- 0.0054  47318.0 +- 0.0
               macro avg 0.7966 +- 0.0019 0.5993 +- 0.0037 0.6647 +- 0.0034  47318.0 +- 0.0
            weighted avg 0.8902 +- 0.0012 0.8044 +- 0.0054 0.8339 +- 0.0035  47318.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7997 +- 0.0051
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8044 +- 0.0053
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8025 +- 0.0056
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8046 +- 0.0061
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8043 +- 0.0065


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6588 +- 0.0036
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6647 +- 0.0034
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6547 +- 0.0037
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6634 +- 0.0047
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6627 +- 0.0048



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



