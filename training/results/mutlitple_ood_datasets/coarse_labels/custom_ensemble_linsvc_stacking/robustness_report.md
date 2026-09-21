# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.9156 +- 0.0009

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9996 +- 0.0002      1.0 +- 0.0 0.9998 +- 0.0001   3129.0 +- 0.0
             CD4+ T cell 0.8897 +- 0.0015 0.9278 +- 0.001 0.9083 +- 0.0009   6465.0 +- 0.0
             CD8+ T cell 0.8357 +- 0.0018 0.8841 +- 0.0022 0.8592 +- 0.0017   6401.0 +- 0.0
          Dendritic cell 0.9302 +- 0.0131 0.7921 +- 0.0162 0.8556 +- 0.0146    165.0 +- 0.0
                Monocyte 0.9967 +- 0.0002 0.9973 +- 0.0006 0.997 +- 0.0003   3648.0 +- 0.0
                 NK cell 0.9922 +- 0.0014 0.7525 +- 0.005 0.8559 +- 0.0033   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9464 +- 0.0238 0.9723 +- 0.0126     56.0 +- 0.0

                accuracy                                 0.9156 +- 0.0009  22446.0 +- 0.0
               macro avg 0.9492 +- 0.0017   0.9 +- 0.0052 0.9212 +- 0.0035  22446.0 +- 0.0
            weighted avg 0.9194 +- 0.0008 0.9156 +- 0.0009 0.9152 +- 0.0009  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9063 +- 0.0044
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9156 +- 0.0009
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9009 +- 0.0012
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9025 +- 0.0014
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8697 +- 0.0014


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9108 +- 0.0047
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9212 +- 0.0035
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9103 +- 0.0034
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9099 +- 0.0035
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8684 +- 0.0115



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.8981 +- 0.0034

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9964 +- 0.0004   0.9988 +- 0.0 0.9976 +- 0.0002    866.0 +- 0.0
             CD4+ T cell 0.955 +- 0.0036 0.8326 +- 0.0098 0.8896 +- 0.0043   4474.0 +- 0.0
             CD8+ T cell 0.7562 +- 0.0098  0.931 +- 0.006 0.8344 +- 0.0041   2688.0 +- 0.0
          Dendritic cell 0.9249 +- 0.0083 0.9225 +- 0.0088 0.9237 +- 0.0071    120.0 +- 0.0
                Monocyte 0.9884 +- 0.0014 0.9899 +- 0.0012 0.9892 +- 0.001    889.0 +- 0.0
                 NK cell 0.9878 +- 0.0021 0.9303 +- 0.0087 0.9581 +- 0.0045    876.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0

                accuracy                                 0.8981 +- 0.0034   9983.0 +- 0.0
               macro avg 0.942 +- 0.0011 0.9395 +- 0.0018 0.9387 +- 0.0016   9983.0 +- 0.0
            weighted avg 0.9108 +- 0.0015 0.8981 +- 0.0034   0.9 +- 0.0032   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8872 +- 0.0098
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8979 +- 0.0034
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8848 +- 0.0026
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8806 +- 0.0026
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8112 +- 0.0014


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.924 +- 0.0072
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9386 +- 0.0016
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9312 +- 0.0011
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9262 +- 0.0013
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8921 +- 0.0016


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8302 +- 0.0041

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9959 +- 0.0      1.0 +- 0.0   0.9979 +- 0.0    968.0 +- 0.0
             CD4+ T cell 0.9792 +- 0.0014 0.6388 +- 0.0104 0.7731 +- 0.0073   4371.0 +- 0.0
             CD8+ T cell 0.5626 +- 0.0063 0.9709 +- 0.0021 0.7123 +- 0.0046   2141.0 +- 0.0
          Dendritic cell 0.9688 +- 0.0037 0.9356 +- 0.0066 0.9519 +- 0.005    146.0 +- 0.0
                Monocyte 0.9944 +- 0.0007 0.9974 +- 0.0003 0.9959 +- 0.0005   1703.0 +- 0.0
                 NK cell 0.9944 +- 0.0016 0.9396 +- 0.0033 0.9662 +- 0.0019    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0      0.9 +- 0.0   0.9474 +- 0.0     40.0 +- 0.0

                accuracy                                 0.8302 +- 0.0041   9998.0 +- 0.0
               macro avg 0.9279 +- 0.0009 0.9117 +- 0.0016 0.9064 +- 0.0018   9998.0 +- 0.0
            weighted avg 0.8951 +- 0.001 0.8302 +- 0.0041 0.8353 +- 0.0042   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.834 +- 0.0125
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8294 +- 0.0042
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8263 +- 0.0037
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8249 +- 0.0036
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8157 +- 0.0032


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8993 +- 0.0078
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9061 +- 0.0018
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.904 +- 0.0015
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9003 +- 0.0016
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8944 +- 0.0012


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.9097 +- 0.006

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0    764.0 +- 0.0
             CD4+ T cell 0.9866 +- 0.0008 0.8024 +- 0.0148 0.8849 +- 0.0087   4116.0 +- 0.0
             CD8+ T cell 0.6289 +- 0.0169 0.9621 +- 0.0026 0.7605 +- 0.0117   1457.0 +- 0.0
          Dendritic cell 0.9572 +- 0.0004 0.9383 +- 0.0098 0.9477 +- 0.0052    167.0 +- 0.0
                Monocyte 0.9957 +- 0.0007   0.9967 +- 0.0 0.9962 +- 0.0003   2413.0 +- 0.0
                 NK cell 0.989 +- 0.0014 0.9852 +- 0.0029 0.9871 +- 0.0014   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                 0.9097 +- 0.006   9997.0 +- 0.0
               macro avg 0.9368 +- 0.0025 0.955 +- 0.0032 0.9395 +- 0.0037   9997.0 +- 0.0
            weighted avg 0.9375 +- 0.0024 0.9097 +- 0.006 0.9146 +- 0.0055   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9139 +- 0.0064
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9083 +- 0.0061
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9055 +- 0.0062
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9044 +- 0.0063
Feature importance dropout (2.0% features dropped) Accuracy score: 0.915 +- 0.0059


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9342 +- 0.0059
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9387 +- 0.0037
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9368 +- 0.0037
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9357 +- 0.0038
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9383 +- 0.0036


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.9386 +- 0.0031

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9985 +- 0.0005      1.0 +- 0.0 0.9993 +- 0.0003    895.0 +- 0.0
             CD4+ T cell 0.9862 +- 0.003 0.8435 +- 0.0137 0.9092 +- 0.0071   2315.0 +- 0.0
             CD8+ T cell 0.8041 +- 0.0092 0.9818 +- 0.0025 0.8841 +- 0.0052   2127.0 +- 0.0
          Dendritic cell      1.0 +- 0.0 0.8417 +- 0.0074 0.914 +- 0.0044    156.0 +- 0.0
                Monocyte 0.9878 +- 0.0006   0.9996 +- 0.0 0.9937 +- 0.0003   2614.0 +- 0.0
                 NK cell 0.9899 +- 0.002 0.8844 +- 0.0109 0.9342 +- 0.0057   1363.0 +- 0.0
             Plasma cell 0.9667 +- 0.0169      1.0 +- 0.0 0.983 +- 0.0088     46.0 +- 0.0

                accuracy                                 0.9386 +- 0.0031   9516.0 +- 0.0
               macro avg 0.9619 +- 0.003 0.9359 +- 0.0028 0.9453 +- 0.003   9516.0 +- 0.0
            weighted avg 0.9477 +- 0.002 0.9386 +- 0.0031 0.9393 +- 0.0031   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9269 +- 0.0066
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9382 +- 0.0031
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9326 +- 0.0025
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9231 +- 0.0034
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9229 +- 0.0031


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9299 +- 0.0056
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9451 +- 0.003
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9417 +- 0.0027
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9341 +- 0.003
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9323 +- 0.0032


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



