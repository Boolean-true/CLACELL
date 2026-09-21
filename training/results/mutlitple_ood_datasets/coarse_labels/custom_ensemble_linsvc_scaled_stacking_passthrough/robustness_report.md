# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8825 +- 0.0021

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0   0.9997 +- 0.0   0.9998 +- 0.0   3129.0 +- 0.0
             CD4+ T cell 0.9066 +- 0.0034 0.7651 +- 0.0115 0.8298 +- 0.0055   6465.0 +- 0.0
             CD8+ T cell 0.7396 +- 0.006 0.9153 +- 0.0042 0.8181 +- 0.0022   6401.0 +- 0.0
          Dendritic cell 0.9479 +- 0.0028 0.8594 +- 0.0056 0.9015 +- 0.0039    165.0 +- 0.0
                Monocyte   0.9967 +- 0.0 0.9979 +- 0.0001 0.9973 +- 0.0001   3648.0 +- 0.0
                 NK cell 0.9783 +- 0.0007 0.7886 +- 0.002 0.8733 +- 0.0013   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     56.0 +- 0.0

                accuracy                                 0.8825 +- 0.0021  22446.0 +- 0.0
               macro avg 0.9384 +- 0.0006 0.9037 +- 0.0006 0.9171 +- 0.0007  22446.0 +- 0.0
            weighted avg 0.8954 +- 0.0009 0.8825 +- 0.0021 0.8833 +- 0.0021  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8775 +- 0.0036
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.882 +- 0.0021
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8744 +- 0.0021
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8739 +- 0.0024
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8484 +- 0.0018


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9133 +- 0.002
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9169 +- 0.0007
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9123 +- 0.0008
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9113 +- 0.0008
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8982 +- 0.0007



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.854 +- 0.0099

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9965 +- 0.0   0.9988 +- 0.0   0.9977 +- 0.0    866.0 +- 0.0
             CD4+ T cell 0.9584 +- 0.0033 0.7308 +- 0.0252 0.829 +- 0.0151   4474.0 +- 0.0
             CD8+ T cell 0.6706 +- 0.0191 0.924 +- 0.0063 0.777 +- 0.0108   2688.0 +- 0.0
          Dendritic cell     0.92 +- 0.0   0.9583 +- 0.0   0.9388 +- 0.0    120.0 +- 0.0
                Monocyte   0.9955 +- 0.0   0.9888 +- 0.0   0.9921 +- 0.0    889.0 +- 0.0
                 NK cell 0.9193 +- 0.0027 0.965 +- 0.0017 0.9416 +- 0.0014    876.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0

                accuracy                                 0.854 +- 0.0099   9983.0 +- 0.0
               macro avg 0.9208 +- 0.0025 0.9339 +- 0.0029 0.9221 +- 0.0038   9983.0 +- 0.0
            weighted avg 0.8838 +- 0.004 0.854 +- 0.0099 0.8564 +- 0.0098   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.854 +- 0.0088
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8527 +- 0.01
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8418 +- 0.0085
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8415 +- 0.0087
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7876 +- 0.0085


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9184 +- 0.0029
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9213 +- 0.0039
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9159 +- 0.0032
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9147 +- 0.0034
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8874 +- 0.0028


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.7602 +- 0.0094

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9959 +- 0.0      1.0 +- 0.0   0.9979 +- 0.0    968.0 +- 0.0
             CD4+ T cell 0.9784 +- 0.0009 0.4721 +- 0.0223 0.6366 +- 0.0203   4371.0 +- 0.0
             CD8+ T cell 0.4727 +- 0.0101 0.971 +- 0.0017 0.6358 +- 0.0088   2141.0 +- 0.0
          Dendritic cell 0.9731 +- 0.0021 0.9658 +- 0.0032 0.9694 +- 0.0011    146.0 +- 0.0
                Monocyte 0.9971 +- 0.0003 0.9977 +- 0.0002 0.9974 +- 0.0001   1703.0 +- 0.0
                 NK cell 0.9717 +- 0.0014 0.9763 +- 0.0012  0.974 +- 0.001    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0      0.9 +- 0.0   0.9474 +- 0.0     40.0 +- 0.0

                accuracy                                 0.7602 +- 0.0094   9998.0 +- 0.0
               macro avg 0.9127 +- 0.0013 0.8976 +- 0.0028 0.8798 +- 0.004   9998.0 +- 0.0
            weighted avg 0.8746 +- 0.002 0.7602 +- 0.0094 0.7602 +- 0.0107   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7767 +- 0.0175
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.759 +- 0.0093
Feature importance dropout (0.5% features dropped) Accuracy score: 0.7565 +- 0.0089
Feature importance dropout (1.0% features dropped) Accuracy score: 0.7565 +- 0.0091
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7486 +- 0.01


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8858 +- 0.0073
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8792 +- 0.0039
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8784 +- 0.0038
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8779 +- 0.0033
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8742 +- 0.0036


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.8559 +- 0.0121

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0    764.0 +- 0.0
             CD4+ T cell 0.9871 +- 0.0012 0.6758 +- 0.0306 0.8019 +- 0.0213   4116.0 +- 0.0
             CD8+ T cell 0.508 +- 0.0227 0.9446 +- 0.0036 0.6604 +- 0.0184   1457.0 +- 0.0
          Dendritic cell 0.9452 +- 0.0032 0.9395 +- 0.0019 0.9423 +- 0.0012    167.0 +- 0.0
                Monocyte 0.9958 +- 0.0001 0.9959 +- 0.0001   0.9959 +- 0.0   2413.0 +- 0.0
                 NK cell 0.9564 +- 0.0015 0.9945 +- 0.0005 0.9751 +- 0.0008   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0

                accuracy                                 0.8559 +- 0.0121   9997.0 +- 0.0
               macro avg 0.9132 +- 0.0028 0.9358 +- 0.004 0.9108 +- 0.0056   9997.0 +- 0.0
            weighted avg 0.9165 +- 0.0028 0.8559 +- 0.0121 0.8644 +- 0.0114   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8654 +- 0.0166
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8541 +- 0.0127
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8528 +- 0.0125
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8529 +- 0.0125
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8685 +- 0.0102


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9131 +- 0.0079
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9099 +- 0.0059
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9093 +- 0.0057
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9095 +- 0.0057
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.9132 +- 0.0047


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.8713 +- 0.002

### Classification Report 

                               precision          recall        f1-score         support

                  B cell   0.9989 +- 0.0      1.0 +- 0.0   0.9994 +- 0.0    895.0 +- 0.0
             CD4+ T cell 0.8806 +- 0.0042 0.757 +- 0.0134 0.814 +- 0.0061   2315.0 +- 0.0
             CD8+ T cell 0.7312 +- 0.0089 0.7579 +- 0.0069 0.7442 +- 0.0023   2127.0 +- 0.0
          Dendritic cell      1.0 +- 0.0   0.8397 +- 0.0   0.9129 +- 0.0    156.0 +- 0.0
                Monocyte 0.9856 +- 0.0002   0.9996 +- 0.0 0.9926 +- 0.0001   2614.0 +- 0.0
                 NK cell 0.779 +- 0.0025 0.912 +- 0.0029 0.8402 +- 0.0017   1363.0 +- 0.0
             Plasma cell 0.9573 +- 0.0004 0.9739 +- 0.0092 0.9655 +- 0.0047     46.0 +- 0.0

                accuracy                                 0.8713 +- 0.002   9516.0 +- 0.0
               macro avg 0.9046 +- 0.0008 0.8914 +- 0.002 0.8956 +- 0.0016   9516.0 +- 0.0
            weighted avg 0.8749 +- 0.0012 0.8713 +- 0.002 0.871 +- 0.0019   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8577 +- 0.0069
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8703 +- 0.0017
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8481 +- 0.0016
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8462 +- 0.0015
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8445 +- 0.002


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.883 +- 0.0054
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8949 +- 0.0015
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.88 +- 0.0013
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8788 +- 0.0012
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8711 +- 0.0025


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



