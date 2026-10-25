# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8936 +- 0.0009

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9026 +- 0.0052 0.6563 +- 0.005 0.7599 +- 0.0022   3032.0 +- 0.0
        Endothelial cell 0.9761 +- 0.0011 0.939 +- 0.0027 0.9572 +- 0.0013   1352.0 +- 0.0
         Epithelial cell 0.9196 +- 0.004 0.9453 +- 0.0014 0.9323 +- 0.0015  13395.0 +- 0.0
            Myeloid cell 0.9817 +- 0.0009  0.93 +- 0.0019 0.9552 +- 0.0008   7844.0 +- 0.0
     Natural killer cell 0.6974 +- 0.0131 0.2248 +- 0.0156 0.3396 +- 0.0175   1768.0 +- 0.0
             Plasma cell 0.9419 +- 0.0056 0.7706 +- 0.011 0.8476 +- 0.0056    989.0 +- 0.0
            Stromal cell 0.9831 +- 0.0007 0.974 +- 0.0006 0.9786 +- 0.0004   3657.0 +- 0.0
                  T cell 0.8147 +- 0.0025 0.9388 +- 0.0036 0.8724 +- 0.001  15281.0 +- 0.0

                accuracy                                 0.8936 +- 0.0009  47318.0 +- 0.0
               macro avg 0.9021 +- 0.0018 0.7974 +- 0.0025 0.8303 +- 0.0024  47318.0 +- 0.0
            weighted avg 0.8936 +- 0.0011 0.8936 +- 0.0009 0.8861 +- 0.0011  47318.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8869 +- 0.0013
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8936 +- 0.0009
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8892 +- 0.001
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8885 +- 0.001
Feature importance dropout (2.0% features dropped) Accuracy score: 0.887 +- 0.0011


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8174 +- 0.0037
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8303 +- 0.0024
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8164 +- 0.0033
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8126 +- 0.0032
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8112 +- 0.0034



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
            Stromal cell             N/A             N/A             N/A             N/A
                  T cell             N/A             N/A             N/A             N/A

                accuracy                                             N/A             N/A
               macro avg             N/A             N/A             N/A             N/A
            weighted avg             N/A             N/A             N/A             N/A

### Further Robustness Evaluation with metric: Accuracy 



### Further Robustness Evaluation with metric: Macro_F1 



