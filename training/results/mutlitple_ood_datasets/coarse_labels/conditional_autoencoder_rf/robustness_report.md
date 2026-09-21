# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8903 +- 0.0021

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9954 +- 0.0034 0.9991 +- 0.0006 0.9972 +- 0.0018   3129.0 +- 0.0
             CD4+ T cell 0.8522 +- 0.0054 0.875 +- 0.0091 0.8634 +- 0.0038   6465.0 +- 0.0
             CD8+ T cell 0.797 +- 0.0067 0.8385 +- 0.0084 0.8172 +- 0.0036   6401.0 +- 0.0
          Dendritic cell 0.9549 +- 0.0075 0.7812 +- 0.0097 0.8593 +- 0.005    165.0 +- 0.0
                Monocyte 0.9933 +- 0.0013 0.9981 +- 0.0006 0.9957 +- 0.0006   3648.0 +- 0.0
                 NK cell 0.9672 +- 0.0069 0.7806 +- 0.0184 0.8638 +- 0.0102   2582.0 +- 0.0
             Plasma cell 0.9939 +- 0.0139 0.8411 +- 0.0501 0.9103 +- 0.0295     56.0 +- 0.0

                accuracy                                 0.8903 +- 0.0021  22446.0 +- 0.0
               macro avg 0.9363 +- 0.0027 0.8734 +- 0.0077 0.901 +- 0.0045  22446.0 +- 0.0
            weighted avg 0.8937 +- 0.002 0.8903 +- 0.0021 0.8905 +- 0.0021  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8847 +- 0.0031
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8902 +- 0.0021
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8827 +- 0.0024
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8819 +- 0.0023
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8668 +- 0.0027


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8934 +- 0.0049
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.901 +- 0.0045
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8944 +- 0.0046
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8844 +- 0.006
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8706 +- 0.0076



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.8751 +- 0.0073

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9703 +- 0.006 0.9992 +- 0.0006 0.9845 +- 0.0033    866.0 +- 0.0
             CD4+ T cell 0.8952 +- 0.0131 0.8521 +- 0.0114 0.873 +- 0.0084   4474.0 +- 0.0
             CD8+ T cell 0.7512 +- 0.0128 0.8238 +- 0.0244 0.7857 +- 0.0139   2688.0 +- 0.0
          Dendritic cell 0.919 +- 0.0167 0.9792 +- 0.0081 0.948 +- 0.0075    120.0 +- 0.0
                Monocyte 0.998 +- 0.0014 0.9883 +- 0.0027 0.9931 +- 0.0013    889.0 +- 0.0
                 NK cell 0.9671 +- 0.0081 0.9178 +- 0.0252 0.9416 +- 0.0109    876.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.6257 +- 0.0808 0.7671 +- 0.0595     70.0 +- 0.0

                accuracy                                 0.8751 +- 0.0073   9983.0 +- 0.0
               macro avg 0.9287 +- 0.0044 0.8837 +- 0.0129 0.899 +- 0.0106   9983.0 +- 0.0
            weighted avg 0.8794 +- 0.0079 0.8751 +- 0.0073 0.876 +- 0.0074   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8664 +- 0.0079
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8742 +- 0.0074
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8579 +- 0.0081
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8549 +- 0.0078
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8258 +- 0.0074


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.889 +- 0.0131
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8987 +- 0.0106
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8896 +- 0.0105
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8486 +- 0.0089
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8345 +- 0.0091


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.8597 +- 0.0065

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9916 +- 0.0018 0.9998 +- 0.0004 0.9957 +- 0.0011    968.0 +- 0.0
             CD4+ T cell 0.9296 +- 0.0085 0.7504 +- 0.0129 0.8304 +- 0.0092   4371.0 +- 0.0
             CD8+ T cell 0.6266 +- 0.0125 0.8759 +- 0.0163 0.7305 +- 0.0117   2141.0 +- 0.0
          Dendritic cell 0.949 +- 0.0079 0.9801 +- 0.0082 0.9643 +- 0.0064    146.0 +- 0.0
                Monocyte 0.9983 +- 0.0007 0.9955 +- 0.0007 0.9969 +- 0.0006   1703.0 +- 0.0
                 NK cell 0.9726 +- 0.0119 0.9566 +- 0.0148 0.9644 +- 0.007    629.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.7975 +- 0.0399 0.8869 +- 0.0247     40.0 +- 0.0

                accuracy                                 0.8597 +- 0.0065   9998.0 +- 0.0
               macro avg 0.9239 +- 0.0031  0.908 +- 0.008 0.9099 +- 0.0055   9998.0 +- 0.0
            weighted avg 0.8857 +- 0.0057 0.8597 +- 0.0065 0.864 +- 0.0063   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8568 +- 0.0072
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8588 +- 0.0067
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8527 +- 0.0073
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8513 +- 0.0071
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8367 +- 0.0071


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9 +- 0.0077
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9095 +- 0.0055
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9061 +- 0.0057
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8718 +- 0.007
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8639 +- 0.0066


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.8784 +- 0.0068

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9947 +- 0.0011      1.0 +- 0.0 0.9973 +- 0.0006    764.0 +- 0.0
             CD4+ T cell 0.9718 +- 0.0047 0.7453 +- 0.0176 0.8435 +- 0.0116   4116.0 +- 0.0
             CD8+ T cell 0.5545 +- 0.0156 0.9211 +- 0.0148 0.6921 +- 0.0128   1457.0 +- 0.0
          Dendritic cell 0.9413 +- 0.0141 0.9647 +- 0.0082 0.9527 +- 0.0058    167.0 +- 0.0
                Monocyte 0.9976 +- 0.0006 0.9955 +- 0.0011 0.9965 +- 0.0004   2413.0 +- 0.0
                 NK cell 0.9748 +- 0.0118 0.9698 +- 0.0119 0.9722 +- 0.0059   1040.0 +- 0.0
             Plasma cell      1.0 +- 0.0  0.895 +- 0.023 0.9445 +- 0.0129     40.0 +- 0.0

                accuracy                                 0.8784 +- 0.0068   9997.0 +- 0.0
               macro avg 0.9192 +- 0.0035 0.9273 +- 0.0035 0.9141 +- 0.0029   9997.0 +- 0.0
            weighted avg 0.9188 +- 0.0035 0.8784 +- 0.0068 0.8857 +- 0.0063   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8764 +- 0.0077
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8762 +- 0.0071
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8734 +- 0.007
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8722 +- 0.0068
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8656 +- 0.0077


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.9085 +- 0.0044
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.9131 +- 0.0029
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.9111 +- 0.0029
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8911 +- 0.0081
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8874 +- 0.0084


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.8603 +- 0.0084

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.954 +- 0.0033      1.0 +- 0.0 0.9764 +- 0.0017    895.0 +- 0.0
             CD4+ T cell 0.703 +- 0.0125 0.9569 +- 0.0089 0.8104 +- 0.0078   2315.0 +- 0.0
             CD8+ T cell 0.7937 +- 0.0302 0.5574 +- 0.0274 0.6544 +- 0.023   2127.0 +- 0.0
          Dendritic cell 0.9925 +- 0.007 0.8372 +- 0.0187 0.9081 +- 0.009    156.0 +- 0.0
                Monocyte 0.9885 +- 0.0015 0.9989 +- 0.0006 0.9937 +- 0.0006   2614.0 +- 0.0
                 NK cell 0.9932 +- 0.0047 0.8367 +- 0.0402 0.9077 +- 0.0231   1363.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.1935 +- 0.0565 0.3208 +- 0.0794     46.0 +- 0.0

                accuracy                                 0.8603 +- 0.0084   9516.0 +- 0.0
               macro avg 0.9179 +- 0.0052 0.7687 +- 0.0121 0.796 +- 0.0147   9516.0 +- 0.0
            weighted avg 0.8731 +- 0.008 0.8603 +- 0.0084 0.8547 +- 0.009   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8568 +- 0.0095
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8602 +- 0.0085
Feature importance dropout (0.5% features dropped) Accuracy score: 0.854 +- 0.0078
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8496 +- 0.0087
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8499 +- 0.0088


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.7935 +- 0.0137
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.7959 +- 0.0148
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.7916 +- 0.0144
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.7879 +- 0.0148
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.7718 +- 0.0114


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



