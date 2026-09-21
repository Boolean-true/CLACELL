# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8947 +- 0.0012

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9999 +- 0.0001 0.9993 +- 0.0004 0.9996 +- 0.0002   3129.0 +- 0.0
             CD4+ T cell 0.8986 +- 0.0044 0.8601 +- 0.0062 0.8789 +- 0.0021   6465.0 +- 0.0
             CD8+ T cell 0.7741 +- 0.0041 0.9003 +- 0.0052 0.8324 +- 0.0017   6401.0 +- 0.0
          Dendritic cell 0.9569 +- 0.0022 0.7945 +- 0.0067 0.8682 +- 0.0042    165.0 +- 0.0
                Monocyte 0.9962 +- 0.0003 0.9977 +- 0.0004 0.9969 +- 0.0003   3648.0 +- 0.0
                 NK cell 0.9818 +- 0.0022 0.6999 +- 0.0051 0.8172 +- 0.0031   2582.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9839 +- 0.0132 0.9919 +- 0.0067     56.0 +- 0.0

                accuracy                                 0.8947 +- 0.0012  22446.0 +- 0.0
               macro avg 0.9439 +- 0.0005 0.8908 +- 0.0028 0.9122 +- 0.0017  22446.0 +- 0.0
            weighted avg 0.9033 +- 0.001 0.8947 +- 0.0012 0.8948 +- 0.0012  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8878 +- 0.0023
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8943 +- 0.0013
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8877 +- 0.0015
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8862 +- 0.0015
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8716 +- 0.0019


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9047 +- 0.0029
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.912 +- 0.0017
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9068 +- 0.0017
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9046 +- 0.0019
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8892 +- 0.0029



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.8926 +- 0.002

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9968 +- 0.0005   0.9988 +- 0.0 0.9978 +- 0.0002    866.0 +- 0.0
             CD4+ T cell 0.9448 +- 0.0053 0.8567 +- 0.0043 0.8986 +- 0.0017   4474.0 +- 0.0
             CD8+ T cell 0.7491 +- 0.004 0.9124 +- 0.0084 0.8227 +- 0.0035   2688.0 +- 0.0
          Dendritic cell 0.9179 +- 0.0051 0.9783 +- 0.0043 0.9472 +- 0.0035    120.0 +- 0.0
                Monocyte 0.9982 +- 0.0006 0.9881 +- 0.0006 0.9931 +- 0.0004    889.0 +- 0.0
                 NK cell 0.9831 +- 0.0018 0.7962 +- 0.014 0.8798 +- 0.0083    876.0 +- 0.0
             Plasma cell      1.0 +- 0.0   0.96 +- 0.006 0.9796 +- 0.0031     70.0 +- 0.0

                accuracy                                 0.8926 +- 0.002   9983.0 +- 0.0
               macro avg 0.9414 +- 0.0012 0.9272 +- 0.0025 0.9312 +- 0.0018   9983.0 +- 0.0
            weighted avg 0.9048 +- 0.0023 0.8926 +- 0.002 0.8947 +- 0.002   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8856 +- 0.0041
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8904 +- 0.002
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8718 +- 0.003
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8701 +- 0.003
Feature importance dropout (2.0% features dropped) Accuracy score: 0.83 +- 0.0038


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9244 +- 0.0041
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9304 +- 0.0018
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9177 +- 0.0025
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9096 +- 0.0033
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8907 +- 0.0044


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8722 +- 0.0032

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9957 +- 0.0004 0.9997 +- 0.0005 0.9977 +- 0.0003    968.0 +- 0.0
             CD4+ T cell 0.964 +- 0.0032 0.7605 +- 0.0074 0.8502 +- 0.0043   4371.0 +- 0.0
             CD8+ T cell 0.6395 +- 0.0066 0.9397 +- 0.0058 0.7611 +- 0.0046   2141.0 +- 0.0
          Dendritic cell  0.954 +- 0.002 0.9801 +- 0.0039 0.9669 +- 0.0022    146.0 +- 0.0
                Monocyte 0.9983 +- 0.0003 0.9959 +- 0.0002 0.9971 +- 0.0002   1703.0 +- 0.0
                 NK cell 0.9907 +- 0.0023 0.8609 +- 0.0144 0.9212 +- 0.008    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.895 +- 0.0105 0.9446 +- 0.0059     40.0 +- 0.0

                accuracy                                 0.8722 +- 0.0032   9998.0 +- 0.0
               macro avg 0.9346 +- 0.0012 0.9188 +- 0.0035 0.9198 +- 0.0026   9998.0 +- 0.0
            weighted avg 0.9051 +- 0.0019 0.8722 +- 0.0032 0.877 +- 0.0031   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8668 +- 0.0025
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8698 +- 0.0034
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8623 +- 0.0035
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8613 +- 0.0036
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8411 +- 0.0034


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9112 +- 0.0035
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9188 +- 0.0027
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9122 +- 0.003
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.904 +- 0.0028
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.893 +- 0.0029


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.8806 +- 0.0044

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9987 +- 0.0011      1.0 +- 0.0 0.9993 +- 0.0005    764.0 +- 0.0
             CD4+ T cell 0.9873 +- 0.0015 0.7523 +- 0.0097 0.8539 +- 0.006   4116.0 +- 0.0
             CD8+ T cell 0.5553 +- 0.0095 0.969 +- 0.0028 0.706 +- 0.0075   1457.0 +- 0.0
          Dendritic cell 0.9546 +- 0.0039 0.9569 +- 0.0062 0.9557 +- 0.0032    167.0 +- 0.0
                Monocyte 0.997 +- 0.0004 0.9964 +- 0.0003 0.9967 +- 0.0002   2413.0 +- 0.0
                 NK cell 0.993 +- 0.0015 0.8924 +- 0.0083  0.94 +- 0.0047   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.975 +- 0.0204 0.9872 +- 0.0105     40.0 +- 0.0

                accuracy                                 0.8806 +- 0.0044   9997.0 +- 0.0
               macro avg 0.9266 +- 0.0014 0.9346 +- 0.0043 0.9198 +- 0.0035   9997.0 +- 0.0
            weighted avg 0.9277 +- 0.0013 0.8806 +- 0.0044 0.8891 +- 0.004   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8784 +- 0.0057
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8769 +- 0.0044
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8719 +- 0.0049
Feature importance dropout (1.0% features dropped) Accuracy score: 0.87 +- 0.0045
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8586 +- 0.005


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9149 +- 0.0049
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9181 +- 0.0035
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9136 +- 0.0039
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.9014 +- 0.0033
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8936 +- 0.0041


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.894 +- 0.0055

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9968 +- 0.0008      1.0 +- 0.0 0.9984 +- 0.0004    895.0 +- 0.0
             CD4+ T cell 0.853 +- 0.0115 0.9604 +- 0.0039 0.9035 +- 0.0067   2315.0 +- 0.0
             CD8+ T cell 0.7496 +- 0.0145 0.8215 +- 0.0158 0.7838 +- 0.0114   2127.0 +- 0.0
          Dendritic cell      1.0 +- 0.0 0.8154 +- 0.0127 0.8983 +- 0.0077    156.0 +- 0.0
                Monocyte 0.9875 +- 0.0008 0.9995 +- 0.0002 0.9935 +- 0.0005   2614.0 +- 0.0
                 NK cell 0.9962 +- 0.0026 0.6287 +- 0.0324 0.7704 +- 0.0245   1363.0 +- 0.0
             Plasma cell 0.9722 +- 0.0141 0.9783 +- 0.0145 0.9751 +- 0.0073     46.0 +- 0.0

                accuracy                                 0.894 +- 0.0055   9516.0 +- 0.0
               macro avg 0.9365 +- 0.0035 0.8862 +- 0.0051 0.9033 +- 0.005   9516.0 +- 0.0
            weighted avg 0.9038 +- 0.0043 0.894 +- 0.0055 0.8916 +- 0.006   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8859 +- 0.0075
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8938 +- 0.0055
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8702 +- 0.0058
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8607 +- 0.006
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8617 +- 0.0058


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8923 +- 0.007
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9032 +- 0.005
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8888 +- 0.005
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8793 +- 0.0054
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8748 +- 0.0055


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



