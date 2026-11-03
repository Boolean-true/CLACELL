# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8665 +- 0.0046

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9423 +- 0.0028 0.5607 +- 0.0106 0.703 +- 0.0082   2907.0 +- 0.0
        Endothelial cell 0.9884 +- 0.0016 0.8564 +- 0.0168 0.9176 +- 0.0093   1106.0 +- 0.0
         Epithelial cell 0.9608 +- 0.0014 0.8948 +- 0.0095 0.9266 +- 0.0055  14999.0 +- 0.0
            Myeloid cell 0.9838 +- 0.0009 0.8853 +- 0.0098 0.9319 +- 0.0055   8013.0 +- 0.0
     Natural killer cell 0.6947 +- 0.011 0.2516 +- 0.013 0.3692 +- 0.0135   1687.0 +- 0.0
             Plasma cell 0.8722 +- 0.0094 0.5439 +- 0.0226 0.6698 +- 0.0194    906.0 +- 0.0
                Rejected      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0
            Stromal cell 0.9811 +- 0.0021 0.9027 +- 0.0072 0.9403 +- 0.0037   4047.0 +- 0.0
                  T cell 0.7941 +- 0.002 0.9725 +- 0.0017 0.8743 +- 0.0009  14212.0 +- 0.0

                accuracy                                 0.8665 +- 0.0046  47877.0 +- 0.0
               macro avg 0.8019 +- 0.0015 0.652 +- 0.0028 0.7036 +- 0.0027  47877.0 +- 0.0
            weighted avg 0.9054 +- 0.0008 0.8665 +- 0.0046 0.8749 +- 0.0027  47877.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8577 +- 0.0051
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8665 +- 0.0045
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8628 +- 0.0045
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8646 +- 0.0047
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8634 +- 0.0046


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6942 +- 0.0043
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.7036 +- 0.0027
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.693 +- 0.0026
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6996 +- 0.0032
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6974 +- 0.0034



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



