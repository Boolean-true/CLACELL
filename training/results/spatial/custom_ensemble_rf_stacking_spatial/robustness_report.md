# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9866 +- 0.0003

### Classification Report 

                               precision          recall        f1-score         support

                  B.cell 0.7642 +- 0.0062 0.881 +- 0.0056 0.8185 +- 0.0043    416.0 +- 0.0
          Dendritic.cell 0.9661 +- 0.0023   0.9511 +- 0.0 0.9586 +- 0.0011    225.0 +- 0.0
        Endothelial.cell 0.9875 +- 0.0003 0.9968 +- 0.0012 0.9921 +- 0.0005    962.0 +- 0.0
              Fibroblast 0.9976 +- 0.0003 0.987 +- 0.0005 0.9923 +- 0.0002  13573.0 +- 0.0
               Mast.cell 0.9078 +- 0.0159 0.7846 +- 0.0192 0.8415 +- 0.0117     65.0 +- 0.0
                Monocyte 0.9814 +- 0.0009 0.9938 +- 0.0002 0.9876 +- 0.0005  18682.0 +- 0.0
     Ovarian.cancer.cell 0.9931 +- 0.0004 0.9972 +- 0.0002 0.9952 +- 0.0001  18678.0 +- 0.0
             Plasma.cell 0.0333 +- 0.0377 0.0025 +- 0.0026 0.0046 +- 0.0049    200.0 +- 0.0
                  T.cell 0.9836 +- 0.0005 0.9804 +- 0.0011 0.982 +- 0.0005  13521.0 +- 0.0

                accuracy                                 0.9866 +- 0.0003  66322.0 +- 0.0
               macro avg 0.8461 +- 0.0045 0.8416 +- 0.0024 0.8414 +- 0.0016  66322.0 +- 0.0
            weighted avg 0.9842 +- 0.0004 0.9866 +- 0.0003 0.9853 +- 0.0003  66322.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9841 +- 0.0005
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9866 +- 0.0003
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9866 +- 0.0003
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9866 +- 0.0003
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9848 +- 0.0006


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8315 +- 0.0032
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8414 +- 0.0016
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8413 +- 0.0016
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8407 +- 0.0018
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8395 +- 0.002



## Out of data distribution 

### OOD Dataset: All 

Baseline accuracy score: N/A

### Classification Report 

                               precision          recall        f1-score         support

                  B.cell             N/A             N/A             N/A             N/A
          Dendritic.cell             N/A             N/A             N/A             N/A
        Endothelial.cell             N/A             N/A             N/A             N/A
              Fibroblast             N/A             N/A             N/A             N/A
               Mast.cell             N/A             N/A             N/A             N/A
                Monocyte             N/A             N/A             N/A             N/A
     Ovarian.cancer.cell             N/A             N/A             N/A             N/A
             Plasma.cell             N/A             N/A             N/A             N/A
                  T.cell             N/A             N/A             N/A             N/A

                accuracy                                             N/A             N/A
               macro avg             N/A             N/A             N/A             N/A
            weighted avg             N/A             N/A             N/A             N/A

### Further Robustness Evaluation with metric: Accuracy 



### Further Robustness Evaluation with metric: Macro_F1 



