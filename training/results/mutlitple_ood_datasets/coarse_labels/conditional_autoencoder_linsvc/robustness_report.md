# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.7706 +- 0.056

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0 0.9993 +- 0.0011 0.9996 +- 0.0006   3129.0 +- 0.0
             CD4+ T cell 0.9802 +- 0.0047 0.4419 +- 0.1371 0.5971 +- 0.1395   6465.0 +- 0.0
             CD8+ T cell 0.5635 +- 0.0624 0.9904 +- 0.004 0.7163 +- 0.0498   6401.0 +- 0.0
          Dendritic cell 0.8505 +- 0.1038 0.8248 +- 0.0539 0.8313 +- 0.0362    165.0 +- 0.0
                Monocyte 0.9953 +- 0.0035 0.9847 +- 0.0228 0.9899 +- 0.0119   3648.0 +- 0.0
                 NK cell 0.9975 +- 0.0028 0.4672 +- 0.2096 0.6089 +- 0.211   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.7018 +- 0.2345 0.8004 +- 0.1996     56.0 +- 0.0

                accuracy                                 0.7706 +- 0.056  22446.0 +- 0.0
               macro avg 0.9124 +- 0.0146 0.7729 +- 0.0783 0.7919 +- 0.0748  22446.0 +- 0.0
            weighted avg 0.8677 +- 0.0172 0.7706 +- 0.056 0.7547 +- 0.0705  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7586 +- 0.0546
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.7704 +- 0.056
Feature importance dropout (0.5% features dropped) Accuracy score: 0.7607 +- 0.0569
Feature importance dropout (1.0% features dropped) Accuracy score: 0.7433 +- 0.0581
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7274 +- 0.0559


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.7654 +- 0.0751
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.7919 +- 0.0748
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.7658 +- 0.0859
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.7414 +- 0.0907
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.7181 +- 0.0913



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.6982 +- 0.0664

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9978 +- 0.0009   0.9988 +- 0.0 0.9983 +- 0.0004    866.0 +- 0.0
             CD4+ T cell 0.9911 +- 0.0026 0.4455 +- 0.122 0.6059 +- 0.1143   4474.0 +- 0.0
             CD8+ T cell 0.4904 +- 0.0642 0.9919 +- 0.0037 0.654 +- 0.0558   2688.0 +- 0.0
          Dendritic cell 0.8766 +- 0.0658 0.9558 +- 0.0408 0.9124 +- 0.0347    120.0 +- 0.0
                Monocyte 0.8946 +- 0.1162 0.9642 +- 0.0599 0.923 +- 0.0719    889.0 +- 0.0
                 NK cell 0.9989 +- 0.002 0.4795 +- 0.2461 0.6112 +- 0.2442    876.0 +- 0.0
             Plasma cell 0.9892 +- 0.0075 0.7743 +- 0.2521 0.8413 +- 0.2066     70.0 +- 0.0

                accuracy                                 0.6982 +- 0.0664   9983.0 +- 0.0
               macro avg 0.8912 +- 0.0146 0.8014 +- 0.0778 0.7923 +- 0.0716   9983.0 +- 0.0
            weighted avg 0.8476 +- 0.0174 0.6982 +- 0.0664 0.6869 +- 0.0771   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6725 +- 0.0663
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6975 +- 0.0662
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6891 +- 0.0658
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6839 +- 0.0651
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6395 +- 0.0656


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.7594 +- 0.0792
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.7917 +- 0.0715
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.7763 +- 0.075
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.7358 +- 0.0846
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.7104 +- 0.0873


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.6527 +- 0.0549

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9956 +- 0.0007 0.9999 +- 0.0003 0.9977 +- 0.0004    968.0 +- 0.0
             CD4+ T cell 0.9945 +- 0.0022   0.293 +- 0.11 0.4423 +- 0.1345   4371.0 +- 0.0
             CD8+ T cell 0.3906 +- 0.0432 0.9957 +- 0.0023 0.5598 +- 0.0439   2141.0 +- 0.0
          Dendritic cell 0.9467 +- 0.034  0.95 +- 0.0364 0.9474 +- 0.016    146.0 +- 0.0
                Monocyte 0.9658 +- 0.057 0.988 +- 0.0215 0.9757 +- 0.0318   1703.0 +- 0.0
                 NK cell 0.9996 +- 0.0013 0.4679 +- 0.2904 0.5838 +- 0.3013    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.735 +- 0.2109 0.8272 +- 0.1846     40.0 +- 0.0

                accuracy                                 0.6527 +- 0.0549   9998.0 +- 0.0
               macro avg 0.899 +- 0.0066 0.7756 +- 0.0746 0.762 +- 0.0761   9998.0 +- 0.0
            weighted avg 0.8601 +- 0.009 0.6527 +- 0.0549 0.6299 +- 0.0731   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6374 +- 0.0544
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6523 +- 0.0547
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6477 +- 0.0542
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6438 +- 0.0535
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6088 +- 0.0495


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.7359 +- 0.0777
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.7618 +- 0.0761
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.7505 +- 0.0768
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.7002 +- 0.0888
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6771 +- 0.0889


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.6838 +- 0.0643

### Classification Report 

                               precision          recall        f1-score         support

                  B cell      1.0 +- 0.0 0.9997 +- 0.0006 0.9999 +- 0.0003    764.0 +- 0.0
             CD4+ T cell 0.998 +- 0.0009 0.3604 +- 0.1046 0.5214 +- 0.1179   4116.0 +- 0.0
             CD8+ T cell 0.3245 +- 0.0469 0.9973 +- 0.0012 0.4879 +- 0.0531   1457.0 +- 0.0
          Dendritic cell 0.9161 +- 0.0412 0.9407 +- 0.0568 0.9262 +- 0.0217    167.0 +- 0.0
                Monocyte 0.9872 +- 0.0207 0.9845 +- 0.0267 0.9856 +- 0.0163   2413.0 +- 0.0
                 NK cell 0.9993 +- 0.0013 0.5451 +- 0.3055 0.6545 +- 0.2859   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.8825 +- 0.1654 0.9288 +- 0.1109     40.0 +- 0.0

                accuracy                                 0.6838 +- 0.0643   9997.0 +- 0.0
               macro avg 0.8893 +- 0.0059 0.8158 +- 0.0716 0.7863 +- 0.0685   9997.0 +- 0.0
            weighted avg 0.8962 +- 0.0064 0.6838 +- 0.0643 0.6874 +- 0.0738   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6738 +- 0.0689
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.683 +- 0.064
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6755 +- 0.0647
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6682 +- 0.0626
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6363 +- 0.0624


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.7649 +- 0.0817
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.7859 +- 0.0683
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.7742 +- 0.0726
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.7284 +- 0.0908
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.7066 +- 0.0918


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.8047 +- 0.0485

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9998 +- 0.0005 0.9992 +- 0.0012 0.9995 +- 0.0006    895.0 +- 0.0
             CD4+ T cell 0.9968 +- 0.0016 0.5458 +- 0.0802 0.7022 +- 0.0656   2315.0 +- 0.0
             CD8+ T cell 0.5477 +- 0.0651 0.9974 +- 0.0014 0.705 +- 0.0538   2127.0 +- 0.0
          Dendritic cell 0.9806 +- 0.0302 0.8397 +- 0.0686 0.9025 +- 0.0357    156.0 +- 0.0
                Monocyte 0.9822 +- 0.0162 0.9916 +- 0.0138 0.9868 +- 0.0093   2614.0 +- 0.0
                 NK cell 0.9986 +- 0.0022 0.4514 +- 0.2536 0.581 +- 0.2589   1363.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.8804 +- 0.1552 0.9291 +- 0.099     46.0 +- 0.0

                accuracy                                 0.8047 +- 0.0485   9516.0 +- 0.0
               macro avg 0.9294 +- 0.0097 0.8151 +- 0.0606 0.8295 +- 0.0598   9516.0 +- 0.0
            weighted avg 0.8927 +- 0.0148 0.8047 +- 0.0485 0.796 +- 0.0579   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7827 +- 0.047
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8044 +- 0.0486
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8069 +- 0.049
Feature importance dropout (1.0% features dropped) Accuracy score: 0.7914 +- 0.0469
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7658 +- 0.0522


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.7977 +- 0.065
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8292 +- 0.0598
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8323 +- 0.0594
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.814 +- 0.0605
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.7703 +- 0.0806


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



