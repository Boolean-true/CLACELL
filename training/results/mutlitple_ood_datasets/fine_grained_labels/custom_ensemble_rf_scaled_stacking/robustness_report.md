# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8522 +- 0.0031

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9947 +- 0.0005 0.9965 +- 0.0003 0.9956 +- 0.0003   3456.0 +- 0.0
          CD16+ Monocyte 0.9787 +- 0.0035 0.9557 +- 0.0056 0.9671 +- 0.0036    192.0 +- 0.0
    CD1C+ dendritic cell 0.9229 +- 0.0071 0.9083 +- 0.0081 0.9155 +- 0.0064    108.0 +- 0.0
       CD4 Memory T cell 0.9488 +- 0.0058 0.9807 +- 0.0027 0.9644 +- 0.0022   2890.0 +- 0.0
        CD4 Naive T cell 0.9543 +- 0.0032 0.9329 +- 0.0028 0.9435 +- 0.0017   3439.0 +- 0.0
       CD8 Memory T cell 0.2154 +- 0.004 0.8891 +- 0.0089 0.3467 +- 0.0055    818.0 +- 0.0
        CD8 Naive T cell 0.9552 +- 0.0027 0.8787 +- 0.0092 0.9153 +- 0.0046   2063.0 +- 0.0
      Gamma-delta T cell 0.9421 +- 0.0032 0.2764 +- 0.0022 0.4274 +- 0.0027   2545.0 +- 0.0
                    MAIT 0.8976 +- 0.0033 0.9083 +- 0.0039 0.9029 +- 0.003    975.0 +- 0.0
           Memory B cell 0.9751 +- 0.0054 0.942 +- 0.0049 0.9583 +- 0.0037    897.0 +- 0.0
                 NK cell 0.988 +- 0.0033 0.8071 +- 0.019 0.8883 +- 0.0107   2582.0 +- 0.0
            Naive B cell 0.977 +- 0.0019 0.9903 +- 0.0021 0.9836 +- 0.0015   2232.0 +- 0.0
             Plasma cell      1.0 +- 0.0  0.95 +- 0.0075 0.9743 +- 0.0039     56.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.6544 +- 0.0085 0.7911 +- 0.0062     57.0 +- 0.0
       T regulatory cell 0.7283 +- 0.2019 0.0169 +- 0.0036 0.033 +- 0.0067    136.0 +- 0.0

                accuracy                                 0.8522 +- 0.0031  22446.0 +- 0.0
               macro avg 0.8985 +- 0.0137 0.8058 +- 0.0023 0.8005 +- 0.0016  22446.0 +- 0.0
            weighted avg 0.935 +- 0.0021 0.8522 +- 0.0031 0.8621 +- 0.0023  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8396 +- 0.0053
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8522 +- 0.0031
Feature importance dropout (0.5% features dropped) Accuracy score: 0.845 +- 0.0039
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8422 +- 0.0041
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7858 +- 0.0036


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.7896 +- 0.0037
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8005 +- 0.0016
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.7956 +- 0.0022
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.7939 +- 0.0026
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.7453 +- 0.0036



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.7284 +- 0.001

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.997 +- 0.0009 0.975 +- 0.0012 0.9858 +- 0.0009    775.0 +- 0.0
          CD16+ Monocyte 0.9504 +- 0.0059 0.9904 +- 0.0028 0.9699 +- 0.0034    114.0 +- 0.0
    CD1C+ dendritic cell 0.8419 +- 0.0054 0.9849 +- 0.0043 0.9078 +- 0.0043     73.0 +- 0.0
       CD4 Memory T cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   1098.0 +- 0.0
        CD4 Naive T cell 0.8491 +- 0.0089 0.9519 +- 0.0049 0.8975 +- 0.0031   3173.0 +- 0.0
       CD8 Memory T cell 0.0421 +- 0.0034 0.0536 +- 0.0049 0.0471 +- 0.0039    823.0 +- 0.0
        CD8 Naive T cell 0.9612 +- 0.0019 0.8947 +- 0.0104 0.9268 +- 0.0051   1349.0 +- 0.0
      Gamma-delta T cell 0.1188 +- 0.0038 0.2782 +- 0.0112 0.1665 +- 0.0057    325.0 +- 0.0
                    MAIT 0.3423 +- 0.0056 0.9848 +- 0.0017 0.508 +- 0.0061    191.0 +- 0.0
           Memory B cell 0.9639 +- 0.0023 0.8765 +- 0.0085 0.9181 +- 0.0054    353.0 +- 0.0
                 NK cell 0.9879 +- 0.0038 0.9756 +- 0.0048 0.9817 +- 0.0017    876.0 +- 0.0
            Naive B cell 0.922 +- 0.0051 0.9813 +- 0.0014 0.9507 +- 0.0032    513.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.983 +- 0.0135 0.9914 +- 0.0069     47.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    203.0 +- 0.0

                accuracy                                 0.7284 +- 0.001   9983.0 +- 0.0
               macro avg 0.6641 +- 0.0011 0.7267 +- 0.0009 0.682 +- 0.0009   9983.0 +- 0.0
            weighted avg 0.6878 +- 0.0027 0.7284 +- 0.001 0.7028 +- 0.0017   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.716 +- 0.0077
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.7284 +- 0.001
Feature importance dropout (0.5% features dropped) Accuracy score: 0.7127 +- 0.0026
Feature importance dropout (1.0% features dropped) Accuracy score: 0.7123 +- 0.0027
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6169 +- 0.0026


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6746 +- 0.0034
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.682 +- 0.0009
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.677 +- 0.0008
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6766 +- 0.0008
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6212 +- 0.0028


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.6578 +- 0.0025

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9954 +- 0.0003 0.9945 +- 0.0003 0.995 +- 0.0002   1466.0 +- 0.0
          CD16+ Monocyte 0.9827 +- 0.0023 0.9797 +- 0.0018 0.9812 +- 0.0012    237.0 +- 0.0
    CD1C+ dendritic cell 0.9302 +- 0.003   0.9787 +- 0.0 0.9539 +- 0.0016     94.0 +- 0.0
       CD4 Memory T cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   1916.0 +- 0.0
        CD4 Naive T cell 0.8889 +- 0.0055 0.9194 +- 0.0107 0.9039 +- 0.0029   2232.0 +- 0.0
       CD8 Memory T cell 0.0222 +- 0.0016 0.0562 +- 0.0045 0.0318 +- 0.0023    786.0 +- 0.0
        CD8 Naive T cell 0.9513 +- 0.0031 0.923 +- 0.0058 0.937 +- 0.0033    686.0 +- 0.0
      Gamma-delta T cell 0.2047 +- 0.0047  0.424 +- 0.015 0.2761 +- 0.0074    354.0 +- 0.0
                    MAIT 0.3718 +- 0.0048 0.9771 +- 0.0029 0.5386 +- 0.005    315.0 +- 0.0
           Memory B cell 0.9657 +- 0.0029 0.9078 +- 0.0079 0.9358 +- 0.0046    474.0 +- 0.0
                 NK cell 0.9899 +- 0.0013 0.9685 +- 0.005 0.9791 +- 0.0028    629.0 +- 0.0
            Naive B cell 0.917 +- 0.0065 0.9751 +- 0.0027 0.9452 +- 0.0038    494.0 +- 0.0
             Plasma cell 0.9974 +- 0.0083    0.925 +- 0.0 0.9598 +- 0.0039     40.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0   0.9423 +- 0.0   0.9703 +- 0.0     52.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    223.0 +- 0.0

                accuracy                                 0.6578 +- 0.0025   9998.0 +- 0.0
               macro avg 0.6811 +- 0.0008 0.7314 +- 0.0016 0.6938 +- 0.001   9998.0 +- 0.0
            weighted avg 0.625 +- 0.0011 0.6578 +- 0.0025 0.635 +- 0.0009   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.655 +- 0.0038
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6579 +- 0.0024
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6545 +- 0.0019
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6554 +- 0.0019
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6078 +- 0.0029


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6887 +- 0.0035
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6939 +- 0.001
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6923 +- 0.0006
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6937 +- 0.0007
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6527 +- 0.0037


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.6407 +- 0.0009

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9957 +- 0.0007 0.9902 +- 0.0006 0.9929 +- 0.0003   2024.0 +- 0.0
          CD16+ Monocyte 0.9958 +- 0.0013 0.9789 +- 0.0032 0.9873 +- 0.0017    389.0 +- 0.0
    CD1C+ dendritic cell 0.8578 +- 0.0074   0.9756 +- 0.0 0.9129 +- 0.0042    123.0 +- 0.0
       CD4 Memory T cell   0.1 +- 0.3162   0.0 +- 0.0001 0.0001 +- 0.0003   2300.0 +- 0.0
        CD4 Naive T cell 0.6404 +- 0.0181 0.9707 +- 0.0057 0.7716 +- 0.0115   1554.0 +- 0.0
       CD8 Memory T cell 0.0305 +- 0.0022 0.064 +- 0.0057 0.0413 +- 0.0031    814.0 +- 0.0
        CD8 Naive T cell 0.8766 +- 0.0065 0.9039 +- 0.0105  0.89 +- 0.0065    180.0 +- 0.0
      Gamma-delta T cell 0.1323 +- 0.0072 0.3991 +- 0.0256 0.1987 +- 0.0112    225.0 +- 0.0
                    MAIT 0.3649 +- 0.0047 0.9819 +- 0.0035 0.5321 +- 0.005    238.0 +- 0.0
           Memory B cell 0.9843 +- 0.0001 0.9239 +- 0.0072 0.9531 +- 0.0039    272.0 +- 0.0
                 NK cell 0.9863 +- 0.0058 0.9902 +- 0.0031 0.9882 +- 0.0027   1040.0 +- 0.0
            Naive B cell 0.9593 +- 0.0037   0.9919 +- 0.0 0.9753 +- 0.0019    492.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     44.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    262.0 +- 0.0

                accuracy                                 0.6407 +- 0.0009   9997.0 +- 0.0
               macro avg 0.6616 +- 0.0204 0.7447 +- 0.0012 0.6829 +- 0.0012   9997.0 +- 0.0
            weighted avg 0.5884 +- 0.0713 0.6407 +- 0.0009 0.5923 +- 0.0019   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6403 +- 0.0014
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6407 +- 0.0009
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6405 +- 0.001
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6396 +- 0.0009
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6284 +- 0.0006


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6778 +- 0.004
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6829 +- 0.0012
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6816 +- 0.0015
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6807 +- 0.0013
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6379 +- 0.0044


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.803 +- 0.0034

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9803 +- 0.0007 0.9929 +- 0.0007 0.9866 +- 0.0004   2125.0 +- 0.0
          CD16+ Monocyte 0.9767 +- 0.0031 0.9587 +- 0.0033 0.9676 +- 0.0016    489.0 +- 0.0
    CD1C+ dendritic cell 0.9626 +- 0.0054 0.8324 +- 0.0067 0.8927 +- 0.0043    105.0 +- 0.0
       CD4 Memory T cell 0.1624 +- 0.0499 0.0098 +- 0.004 0.0185 +- 0.0073    754.0 +- 0.0
        CD4 Naive T cell 0.9045 +- 0.0041 0.8893 +- 0.0131 0.8968 +- 0.006   1396.0 +- 0.0
       CD8 Memory T cell 0.1447 +- 0.0074 0.6346 +- 0.0435 0.2357 +- 0.0127    312.0 +- 0.0
        CD8 Naive T cell 0.963 +- 0.0131 0.9888 +- 0.0005 0.9757 +- 0.0069   1105.0 +- 0.0
      Gamma-delta T cell 0.1603 +- 0.0491 0.0268 +- 0.0138 0.0455 +- 0.0217    493.0 +- 0.0
                    MAIT 0.4086 +- 0.0047 0.9834 +- 0.0076 0.5773 +- 0.005    217.0 +- 0.0
           Memory B cell 0.9437 +- 0.0047 0.9549 +- 0.0073 0.9492 +- 0.0029    277.0 +- 0.0
                 NK cell 0.974 +- 0.0079 0.913 +- 0.0127 0.9424 +- 0.007   1363.0 +- 0.0
            Naive B cell 0.9797 +- 0.0032 0.9761 +- 0.0024 0.9779 +- 0.0013    618.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     46.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     51.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    165.0 +- 0.0

                accuracy                                 0.803 +- 0.0034   9516.0 +- 0.0
               macro avg 0.704 +- 0.0059 0.744 +- 0.0029 0.6977 +- 0.0019   9516.0 +- 0.0
            weighted avg 0.8003 +- 0.0057 0.803 +- 0.0034 0.7858 +- 0.0023   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7961 +- 0.0039
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.803 +- 0.0033
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8012 +- 0.0032
Feature importance dropout (1.0% features dropped) Accuracy score: 0.7973 +- 0.0039
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7923 +- 0.0036


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6929 +- 0.0024
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6978 +- 0.0019
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6968 +- 0.0021
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6944 +- 0.0025
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6929 +- 0.0023


### OOD Dataset: All 

Baseline accuracy score: N/A

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte             N/A             N/A             N/A             N/A
          CD16+ Monocyte             N/A             N/A             N/A             N/A
    CD1C+ dendritic cell             N/A             N/A             N/A             N/A
       CD4 Memory T cell             N/A             N/A             N/A             N/A
        CD4 Naive T cell             N/A             N/A             N/A             N/A
       CD8 Memory T cell             N/A             N/A             N/A             N/A
        CD8 Naive T cell             N/A             N/A             N/A             N/A
      Gamma-delta T cell             N/A             N/A             N/A             N/A
                    MAIT             N/A             N/A             N/A             N/A
           Memory B cell             N/A             N/A             N/A             N/A
                 NK cell             N/A             N/A             N/A             N/A
            Naive B cell             N/A             N/A             N/A             N/A
             Plasma cell             N/A             N/A             N/A             N/A
Plasmacytoid dendritic cell             N/A             N/A             N/A             N/A
       T regulatory cell             N/A             N/A             N/A             N/A

                accuracy                                             N/A             N/A
               macro avg             N/A             N/A             N/A             N/A
            weighted avg             N/A             N/A             N/A             N/A

### Further Robustness Evaluation with metric: Accuracy 



### Further Robustness Evaluation with metric: Macro_F1 



