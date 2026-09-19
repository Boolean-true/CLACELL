# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8631 +- 0.0013

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9934 +- 0.0004 0.9972 +- 0.0001 0.9953 +- 0.0002   3456.0 +- 0.0
          CD16+ Monocyte 0.9859 +- 0.0028 0.9464 +- 0.0055 0.9657 +- 0.003    192.0 +- 0.0
    CD1C+ dendritic cell 0.9317 +- 0.0004 0.8843 +- 0.0049 0.9074 +- 0.0027    108.0 +- 0.0
       CD4 Memory T cell 0.9072 +- 0.0041 0.9937 +- 0.001 0.9485 +- 0.0019   2890.0 +- 0.0
        CD4 Naive T cell 0.9025 +- 0.0021 0.9628 +- 0.0013 0.9317 +- 0.0014   3439.0 +- 0.0
       CD8 Memory T cell 0.2114 +- 0.0041 0.6248 +- 0.0113 0.3159 +- 0.006    818.0 +- 0.0
        CD8 Naive T cell 0.9481 +- 0.0019 0.8438 +- 0.006 0.8929 +- 0.0029   2063.0 +- 0.0
      Gamma-delta T cell 0.9586 +- 0.0018 0.4738 +- 0.0079 0.6342 +- 0.0074   2545.0 +- 0.0
                    MAIT 0.8102 +- 0.0039 0.9412 +- 0.0027 0.8708 +- 0.0031    975.0 +- 0.0
           Memory B cell 0.9422 +- 0.0038 0.9476 +- 0.0027 0.9449 +- 0.0024    897.0 +- 0.0
                 NK cell 0.9912 +- 0.0011 0.7533 +- 0.0023 0.856 +- 0.0014   2582.0 +- 0.0
            Naive B cell 0.9789 +- 0.0011 0.9766 +- 0.0016 0.9778 +- 0.001   2232.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     56.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.6737 +- 0.0091 0.805 +- 0.0065     57.0 +- 0.0
       T regulatory cell 0.8816 +- 0.0222 0.1632 +- 0.0097 0.2753 +- 0.0137    136.0 +- 0.0

                accuracy                                 0.8631 +- 0.0013  22446.0 +- 0.0
               macro avg 0.8962 +- 0.0019 0.8122 +- 0.0012 0.8214 +- 0.0013  22446.0 +- 0.0
            weighted avg 0.9191 +- 0.0008 0.8631 +- 0.0013 0.8737 +- 0.0013  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8634 +- 0.0055
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8631 +- 0.0013
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8554 +- 0.0012
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8546 +- 0.0012
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7973 +- 0.0023


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8137 +- 0.0046
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8214 +- 0.0013
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8155 +- 0.0011
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.814 +- 0.0016
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.7635 +- 0.0025



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.7426 +- 0.0005

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9911 +- 0.0005 0.979 +- 0.0009 0.985 +- 0.0005    775.0 +- 0.0
          CD16+ Monocyte 0.9582 +- 0.0026 0.9842 +- 0.0037 0.971 +- 0.0021    114.0 +- 0.0
    CD1C+ dendritic cell 0.8582 +- 0.0055   0.9452 +- 0.0 0.8996 +- 0.003     73.0 +- 0.0
       CD4 Memory T cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   1098.0 +- 0.0
        CD4 Naive T cell 0.7772 +- 0.0034 0.9797 +- 0.0011 0.8668 +- 0.002   3173.0 +- 0.0
       CD8 Memory T cell 0.0008 +- 0.0013 0.0004 +- 0.0006 0.0005 +- 0.0008    823.0 +- 0.0
        CD8 Naive T cell 0.9347 +- 0.0022 0.9526 +- 0.003 0.9436 +- 0.0011   1349.0 +- 0.0
      Gamma-delta T cell 0.1152 +- 0.0018 0.2698 +- 0.0048 0.1615 +- 0.0026    325.0 +- 0.0
                    MAIT 0.3056 +- 0.0025   0.9843 +- 0.0 0.4663 +- 0.0029    191.0 +- 0.0
           Memory B cell 0.9642 +- 0.0016 0.8841 +- 0.0052 0.9224 +- 0.0032    353.0 +- 0.0
                 NK cell 0.9706 +- 0.0022 0.9973 +- 0.0006 0.9837 +- 0.0012    876.0 +- 0.0
            Naive B cell 0.9266 +- 0.0032 0.9813 +- 0.001 0.9531 +- 0.0019    513.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     47.0 +- 0.0
       T regulatory cell 0.025 +- 0.0791 0.0005 +- 0.0016 0.001 +- 0.0031    203.0 +- 0.0

                accuracy                                 0.7426 +- 0.0005   9983.0 +- 0.0
               macro avg 0.6542 +- 0.0055 0.7287 +- 0.0007 0.6755 +- 0.0008   9983.0 +- 0.0
            weighted avg 0.6562 +- 0.002 0.7426 +- 0.0005 0.6909 +- 0.0009   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7356 +- 0.0041
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.7426 +- 0.0005
Feature importance dropout (0.5% features dropped) Accuracy score: 0.7352 +- 0.0011
Feature importance dropout (1.0% features dropped) Accuracy score: 0.7354 +- 0.0009
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6565 +- 0.0062


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6691 +- 0.0037
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6755 +- 0.0008
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6737 +- 0.0007
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6728 +- 0.0006
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6365 +- 0.004


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.6729 +- 0.0005

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9939 +- 0.0002 0.9962 +- 0.0004 0.9951 +- 0.0002   1466.0 +- 0.0
          CD16+ Monocyte   0.9872 +- 0.0   0.9789 +- 0.0   0.9831 +- 0.0    237.0 +- 0.0
    CD1C+ dendritic cell 0.9414 +- 0.0051   0.9574 +- 0.0 0.9494 +- 0.0026     94.0 +- 0.0
       CD4 Memory T cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   1916.0 +- 0.0
        CD4 Naive T cell  0.744 +- 0.003 0.9793 +- 0.0014 0.8455 +- 0.002   2232.0 +- 0.0
       CD8 Memory T cell 0.002 +- 0.0004 0.0028 +- 0.0005 0.0023 +- 0.0004    786.0 +- 0.0
        CD8 Naive T cell 0.9138 +- 0.0051 0.9652 +- 0.0014 0.9388 +- 0.0026    686.0 +- 0.0
      Gamma-delta T cell 0.2058 +- 0.0029 0.4393 +- 0.0067 0.2803 +- 0.004    354.0 +- 0.0
                    MAIT 0.3296 +- 0.0018 0.9876 +- 0.0018 0.4943 +- 0.0021    315.0 +- 0.0
           Memory B cell 0.9636 +- 0.0021 0.9171 +- 0.0053 0.9398 +- 0.003    474.0 +- 0.0
                 NK cell 0.986 +- 0.0011 0.9946 +- 0.0013 0.9903 +- 0.0007    629.0 +- 0.0
            Naive B cell 0.9244 +- 0.0045 0.9729 +- 0.002 0.948 +- 0.0025    494.0 +- 0.0
             Plasma cell      1.0 +- 0.0    0.925 +- 0.0    0.961 +- 0.0     40.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.9442 +- 0.0061 0.9713 +- 0.0032     52.0 +- 0.0
       T regulatory cell 0.0454 +- 0.0282 0.0063 +- 0.0043 0.011 +- 0.0074    223.0 +- 0.0

                accuracy                                 0.6729 +- 0.0005   9998.0 +- 0.0
               macro avg 0.6692 +- 0.0018 0.7378 +- 0.0007 0.6873 +- 0.0006   9998.0 +- 0.0
            weighted avg 0.5882 +- 0.0005 0.6729 +- 0.0005 0.6198 +- 0.0004   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6703 +- 0.0021
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6729 +- 0.0005
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6714 +- 0.0005
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6717 +- 0.0003
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6462 +- 0.0024


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6821 +- 0.0018
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6873 +- 0.0006
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6871 +- 0.0007
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6875 +- 0.0005
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6694 +- 0.0024


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.6419 +- 0.0007

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9918 +- 0.0008 0.9941 +- 0.0004 0.9929 +- 0.0005   2024.0 +- 0.0
          CD16+ Monocyte   0.9973 +- 0.0 0.9663 +- 0.0041 0.9816 +- 0.0021    389.0 +- 0.0
    CD1C+ dendritic cell 0.9049 +- 0.0049 0.9585 +- 0.0026 0.9309 +- 0.0032    123.0 +- 0.0
       CD4 Memory T cell  0.88 +- 0.1333 0.0014 +- 0.0005 0.0028 +- 0.001   2300.0 +- 0.0
        CD4 Naive T cell 0.4413 +- 0.005 0.9929 +- 0.0009 0.611 +- 0.0047   1554.0 +- 0.0
       CD8 Memory T cell 0.0008 +- 0.0013 0.0004 +- 0.0006 0.0005 +- 0.0008    814.0 +- 0.0
        CD8 Naive T cell 0.7139 +- 0.0074 0.9478 +- 0.0047 0.8143 +- 0.0051    180.0 +- 0.0
      Gamma-delta T cell 0.1339 +- 0.0074 0.4124 +- 0.026 0.2022 +- 0.0116    225.0 +- 0.0
                    MAIT 0.3096 +- 0.0028   0.9874 +- 0.0 0.4714 +- 0.0033    238.0 +- 0.0
           Memory B cell 0.9844 +- 0.0001 0.9298 +- 0.0032 0.9563 +- 0.0017    272.0 +- 0.0
                 NK cell 0.9555 +- 0.0042      1.0 +- 0.0 0.9773 +- 0.0022   1040.0 +- 0.0
            Naive B cell 0.9623 +- 0.0017   0.9919 +- 0.0 0.9769 +- 0.0009    492.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     44.0 +- 0.0
       T regulatory cell  0.95 +- 0.1581 0.0057 +- 0.002 0.0114 +- 0.004    262.0 +- 0.0

                accuracy                                 0.6419 +- 0.0007   9997.0 +- 0.0
               macro avg 0.7484 +- 0.0113 0.7459 +- 0.002 0.662 +- 0.0013   9997.0 +- 0.0
            weighted avg 0.752 +- 0.0295 0.6419 +- 0.0007 0.5612 +- 0.0013   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6401 +- 0.0012
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6419 +- 0.0007
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6415 +- 0.0007
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6412 +- 0.0007
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6334 +- 0.001


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6581 +- 0.0023
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.662 +- 0.0013
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6641 +- 0.0013
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6641 +- 0.0012
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6425 +- 0.0031


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.8305 +- 0.0017

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9763 +- 0.0008 0.9957 +- 0.0006 0.9859 +- 0.0004   2125.0 +- 0.0
          CD16+ Monocyte 0.9831 +- 0.0024 0.9505 +- 0.0029 0.9665 +- 0.002    489.0 +- 0.0
    CD1C+ dendritic cell 0.986 +- 0.0047 0.8038 +- 0.0092 0.8856 +- 0.0053    105.0 +- 0.0
       CD4 Memory T cell 0.7706 +- 0.0568 0.104 +- 0.0172 0.1828 +- 0.0267    754.0 +- 0.0
        CD4 Naive T cell 0.7886 +- 0.003 0.9804 +- 0.0036 0.8741 +- 0.0017   1396.0 +- 0.0
       CD8 Memory T cell 0.0339 +- 0.0103 0.0474 +- 0.0153 0.0395 +- 0.0123    312.0 +- 0.0
        CD8 Naive T cell 0.9914 +- 0.0009  0.99 +- 0.0006 0.9907 +- 0.0005   1105.0 +- 0.0
      Gamma-delta T cell 0.4163 +- 0.0114 0.4178 +- 0.023 0.417 +- 0.0168    493.0 +- 0.0
                    MAIT 0.3694 +- 0.003   0.9954 +- 0.0 0.5389 +- 0.0032    217.0 +- 0.0
           Memory B cell 0.9404 +- 0.0034 0.9625 +- 0.0025 0.9513 +- 0.0025    277.0 +- 0.0
                 NK cell 0.9638 +- 0.004 0.9495 +- 0.0015 0.9566 +- 0.0019   1363.0 +- 0.0
            Naive B cell 0.983 +- 0.0011 0.9743 +- 0.0016 0.9786 +- 0.0012    618.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     46.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     51.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    165.0 +- 0.0

                accuracy                                 0.8305 +- 0.0017   9516.0 +- 0.0
               macro avg 0.7469 +- 0.0046 0.7448 +- 0.0017 0.7178 +- 0.0023   9516.0 +- 0.0
            weighted avg 0.8418 +- 0.0053 0.8305 +- 0.0017 0.811 +- 0.0026   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8206 +- 0.002
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8305 +- 0.0017
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8284 +- 0.0018
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8265 +- 0.0015
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8251 +- 0.0014


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.7021 +- 0.0043
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.7178 +- 0.0023
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.7167 +- 0.0022
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.7154 +- 0.0018
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.7138 +- 0.0015


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



