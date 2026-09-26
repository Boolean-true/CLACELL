# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8701 +- 0.0022

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9897 +- 0.0002 0.997 +- 0.0001 0.9934 +- 0.0001   3456.0 +- 0.0
          CD16+ Monocyte 0.9765 +- 0.0027 0.9531 +- 0.0025 0.9647 +- 0.0018    192.0 +- 0.0
    CD1C+ dendritic cell 0.9395 +- 0.0002 0.862 +- 0.0029 0.8991 +- 0.0017    108.0 +- 0.0
       CD4 Memory T cell 0.9549 +- 0.0013 0.9139 +- 0.0061 0.9339 +- 0.003   2890.0 +- 0.0
        CD4 Naive T cell 0.9079 +- 0.0022 0.9397 +- 0.0013 0.9236 +- 0.001   3439.0 +- 0.0
       CD8 Memory T cell 0.2656 +- 0.0054 0.8649 +- 0.0038 0.4063 +- 0.0065    818.0 +- 0.0
        CD8 Naive T cell 0.9407 +- 0.0056 0.8733 +- 0.0023 0.9057 +- 0.0023   2063.0 +- 0.0
      Gamma-delta T cell 0.9746 +- 0.0007 0.6008 +- 0.0099 0.7433 +- 0.0077   2545.0 +- 0.0
                    MAIT 0.8454 +- 0.0022 0.8499 +- 0.0029 0.8476 +- 0.0017    975.0 +- 0.0
           Memory B cell 0.9001 +- 0.0015 0.9649 +- 0.0012 0.9313 +- 0.0012    897.0 +- 0.0
                 NK cell 0.9869 +- 0.004 0.7655 +- 0.0075 0.8622 +- 0.0042   2582.0 +- 0.0
            Naive B cell 0.985 +- 0.0005 0.9561 +- 0.0007 0.9703 +- 0.0005   2232.0 +- 0.0
             Plasma cell      1.0 +- 0.0   0.9464 +- 0.0   0.9725 +- 0.0     56.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.6579 +- 0.0092 0.7936 +- 0.0067     57.0 +- 0.0
       T regulatory cell      1.0 +- 0.0   0.0147 +- 0.0    0.029 +- 0.0    136.0 +- 0.0

                accuracy                                 0.8701 +- 0.0022  22446.0 +- 0.0
               macro avg 0.9111 +- 0.0007 0.8107 +- 0.0016 0.8118 +- 0.0014  22446.0 +- 0.0
            weighted avg 0.9292 +- 0.0007 0.8701 +- 0.0022 0.8839 +- 0.0017  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8378 +- 0.0088
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8701 +- 0.0022
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8563 +- 0.0022
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8558 +- 0.002
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7755 +- 0.0042


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.7859 +- 0.0067
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8119 +- 0.0014
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8024 +- 0.0012
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.7995 +- 0.0013
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.7221 +- 0.0033



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.7162 +- 0.001

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9859 +- 0.0011 0.9844 +- 0.0007 0.9851 +- 0.0006    775.0 +- 0.0
          CD16+ Monocyte 0.9558 +- 0.0034 0.9868 +- 0.0046 0.9711 +- 0.0029    114.0 +- 0.0
    CD1C+ dendritic cell 0.8898 +- 0.0036 0.874 +- 0.0058 0.8818 +- 0.0025     73.0 +- 0.0
       CD4 Memory T cell      1.0 +- 0.0 0.001 +- 0.0003 0.002 +- 0.0006   1098.0 +- 0.0
        CD4 Naive T cell 0.8031 +- 0.0051 0.9716 +- 0.0014 0.8793 +- 0.0025   3173.0 +- 0.0
       CD8 Memory T cell 0.0634 +- 0.0029 0.0685 +- 0.0043 0.0658 +- 0.0033    823.0 +- 0.0
        CD8 Naive T cell 0.967 +- 0.0008 0.8717 +- 0.0053 0.9169 +- 0.0027   1349.0 +- 0.0
      Gamma-delta T cell 0.0983 +- 0.0021 0.2391 +- 0.0065 0.1393 +- 0.0032    325.0 +- 0.0
                    MAIT 0.3487 +- 0.0051 0.9958 +- 0.0022 0.5165 +- 0.0057    191.0 +- 0.0
           Memory B cell 0.9657 +- 0.0002 0.7178 +- 0.0038 0.8235 +- 0.0026    353.0 +- 0.0
                 NK cell 0.9965 +- 0.0029 0.8582 +- 0.0122 0.9221 +- 0.0061    876.0 +- 0.0
            Naive B cell 0.8372 +- 0.0019   0.9883 +- 0.0 0.9065 +- 0.0011    513.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0   0.9787 +- 0.0   0.9892 +- 0.0     47.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    203.0 +- 0.0

                accuracy                                 0.7162 +- 0.001   9983.0 +- 0.0
               macro avg 0.7265 +- 0.0005 0.7005 +- 0.0009 0.6652 +- 0.0005   9983.0 +- 0.0
            weighted avg 0.7812 +- 0.0017 0.7162 +- 0.001 0.6856 +- 0.0009   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6962 +- 0.0062
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.7161 +- 0.001
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6958 +- 0.0015
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6942 +- 0.0015
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6039 +- 0.0035


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6485 +- 0.0041
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6652 +- 0.0005
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6578 +- 0.0007
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6522 +- 0.0008
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.5981 +- 0.0023


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.6625 +- 0.0008

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9919 +- 0.001 0.9965 +- 0.0002 0.9942 +- 0.0004   1466.0 +- 0.0
          CD16+ Monocyte 0.983 +- 0.0001 0.9776 +- 0.0035 0.9803 +- 0.0018    237.0 +- 0.0
    CD1C+ dendritic cell 0.9552 +- 0.003 0.9298 +- 0.0103 0.9423 +- 0.0048     94.0 +- 0.0
       CD4 Memory T cell   0.7 +- 0.4216 0.0004 +- 0.0002 0.0008 +- 0.0004   1916.0 +- 0.0
        CD4 Naive T cell 0.8145 +- 0.0028 0.9652 +- 0.0012 0.8835 +- 0.0013   2232.0 +- 0.0
       CD8 Memory T cell 0.0552 +- 0.0014 0.127 +- 0.0038 0.0769 +- 0.002    786.0 +- 0.0
        CD8 Naive T cell 0.9598 +- 0.0021 0.9143 +- 0.0026 0.9365 +- 0.0019    686.0 +- 0.0
      Gamma-delta T cell 0.1707 +- 0.0011 0.3415 +- 0.0051 0.2276 +- 0.002    354.0 +- 0.0
                    MAIT 0.4178 +- 0.0067 0.9698 +- 0.0017 0.584 +- 0.0063    315.0 +- 0.0
           Memory B cell 0.977 +- 0.0013 0.7789 +- 0.0067 0.8668 +- 0.0044    474.0 +- 0.0
                 NK cell 0.9965 +- 0.0005 0.9399 +- 0.0083 0.9673 +- 0.0044    629.0 +- 0.0
            Naive B cell 0.823 +- 0.0044 0.9864 +- 0.001 0.8973 +- 0.0028    494.0 +- 0.0
             Plasma cell      1.0 +- 0.0     0.95 +- 0.0   0.9744 +- 0.0     40.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0   0.9423 +- 0.0   0.9703 +- 0.0     52.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    223.0 +- 0.0

                accuracy                                 0.6625 +- 0.0008   9998.0 +- 0.0
               macro avg 0.723 +- 0.0278 0.7213 +- 0.0013 0.6868 +- 0.001   9998.0 +- 0.0
            weighted avg 0.742 +- 0.0804 0.6625 +- 0.0008 0.6273 +- 0.0008   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6567 +- 0.0048
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6626 +- 0.0008
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6578 +- 0.0008
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6578 +- 0.001
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6155 +- 0.0014


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.678 +- 0.0047
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6871 +- 0.001
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6844 +- 0.001
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6797 +- 0.0016
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.639 +- 0.0017


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.6422 +- 0.0011

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9892 +- 0.0004 0.9949 +- 0.0002 0.9921 +- 0.0002   2024.0 +- 0.0
          CD16+ Monocyte 0.9896 +- 0.0017 0.974 +- 0.0023 0.9817 +- 0.0013    389.0 +- 0.0
    CD1C+ dendritic cell 0.9459 +- 0.004 0.8959 +- 0.0051 0.9202 +- 0.0037    123.0 +- 0.0
       CD4 Memory T cell 0.9251 +- 0.0216 0.0152 +- 0.0029 0.0299 +- 0.0056   2300.0 +- 0.0
        CD4 Naive T cell 0.5948 +- 0.0117 0.981 +- 0.0012 0.7405 +- 0.0087   1554.0 +- 0.0
       CD8 Memory T cell 0.0533 +- 0.0037 0.1012 +- 0.0054 0.0698 +- 0.0043    814.0 +- 0.0
        CD8 Naive T cell 0.9081 +- 0.0075 0.8722 +- 0.0045 0.8898 +- 0.0055    180.0 +- 0.0
      Gamma-delta T cell 0.1256 +- 0.0029 0.3818 +- 0.0108 0.189 +- 0.0046    225.0 +- 0.0
                    MAIT 0.3973 +- 0.009 0.9739 +- 0.0027 0.5643 +- 0.0089    238.0 +- 0.0
           Memory B cell 0.9901 +- 0.0019 0.8085 +- 0.0059 0.8901 +- 0.0035    272.0 +- 0.0
                 NK cell 0.9857 +- 0.0037 0.9684 +- 0.0058 0.977 +- 0.0028   1040.0 +- 0.0
            Naive B cell 0.902 +- 0.0028 0.9955 +- 0.0009 0.9465 +- 0.0016    492.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0
Plasmacytoid dendritic cell   0.9778 +- 0.0      1.0 +- 0.0   0.9888 +- 0.0     44.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    262.0 +- 0.0

                accuracy                                 0.6422 +- 0.0011   9997.0 +- 0.0
               macro avg 0.719 +- 0.0019 0.7308 +- 0.001 0.6787 +- 0.0009   9997.0 +- 0.0
            weighted avg 0.7709 +- 0.0056 0.6422 +- 0.0011 0.5926 +- 0.0013   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6366 +- 0.004
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6421 +- 0.0011
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6394 +- 0.0012
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6377 +- 0.0013
Feature importance dropout (2.0% features dropped) Accuracy score: 0.628 +- 0.0021


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.668 +- 0.006
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6789 +- 0.0009
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6741 +- 0.0012
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.673 +- 0.0013
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6373 +- 0.002


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.7239 +- 0.0075

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9729 +- 0.0009 0.9942 +- 0.0012 0.9834 +- 0.0004   2125.0 +- 0.0
          CD16+ Monocyte 0.9714 +- 0.0043 0.9495 +- 0.0037 0.9603 +- 0.0012    489.0 +- 0.0
    CD1C+ dendritic cell      1.0 +- 0.0 0.7581 +- 0.0049 0.8624 +- 0.0032    105.0 +- 0.0
       CD4 Memory T cell 0.6039 +- 0.0387 0.0389 +- 0.0053 0.073 +- 0.0095    754.0 +- 0.0
        CD4 Naive T cell 0.862 +- 0.0047 0.887 +- 0.0129 0.8742 +- 0.0052   1396.0 +- 0.0
       CD8 Memory T cell 0.116 +- 0.0056 0.8234 +- 0.0148 0.2034 +- 0.0088    312.0 +- 0.0
        CD8 Naive T cell 0.9917 +- 0.0011 0.8462 +- 0.0059 0.9132 +- 0.0036   1105.0 +- 0.0
      Gamma-delta T cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    493.0 +- 0.0
                    MAIT 0.5562 +- 0.0115 0.5576 +- 0.0234 0.5565 +- 0.0104    217.0 +- 0.0
           Memory B cell 0.9858 +- 0.0044 0.2971 +- 0.0126 0.4564 +- 0.0146    277.0 +- 0.0
                 NK cell 0.9769 +- 0.0078 0.6326 +- 0.0387 0.7674 +- 0.0282   1363.0 +- 0.0
            Naive B cell 0.7581 +- 0.0028 0.9981 +- 0.0007 0.8617 +- 0.0016    618.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.8587 +- 0.0494 0.9233 +- 0.0281     46.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     51.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    165.0 +- 0.0

                accuracy                                 0.7239 +- 0.0075   9516.0 +- 0.0
               macro avg 0.7197 +- 0.0027 0.6428 +- 0.0051 0.629 +- 0.0031   9516.0 +- 0.0
            weighted avg 0.8122 +- 0.0026 0.7239 +- 0.0075 0.7269 +- 0.005   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7018 +- 0.0086
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.7239 +- 0.0075
Feature importance dropout (0.5% features dropped) Accuracy score: 0.7095 +- 0.007
Feature importance dropout (1.0% features dropped) Accuracy score: 0.691 +- 0.0073
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6759 +- 0.0077


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6033 +- 0.0069
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6291 +- 0.0031
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6193 +- 0.0026
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.613 +- 0.0028
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.5912 +- 0.0035


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



