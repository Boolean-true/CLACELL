# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8667 +- 0.0015

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9932 +- 0.0004 0.9957 +- 0.0003 0.9944 +- 0.0003   3456.0 +- 0.0
          CD16+ Monocyte 0.9778 +- 0.0022 0.9646 +- 0.0022 0.9712 +- 0.0017    192.0 +- 0.0
    CD1C+ dendritic cell 0.9286 +- 0.0042 0.8787 +- 0.0068 0.9029 +- 0.0036    108.0 +- 0.0
       CD4 Memory T cell 0.9123 +- 0.0026 0.8029 +- 0.0037 0.8541 +- 0.003   2890.0 +- 0.0
        CD4 Naive T cell 0.8268 +- 0.002 0.9216 +- 0.0024 0.8717 +- 0.0018   3439.0 +- 0.0
       CD8 Memory T cell 0.319 +- 0.0082 0.6033 +- 0.0063 0.4172 +- 0.0068    818.0 +- 0.0
        CD8 Naive T cell 0.9157 +- 0.006 0.8465 +- 0.0017 0.8797 +- 0.0028   2063.0 +- 0.0
      Gamma-delta T cell 0.9438 +- 0.0033 0.7459 +- 0.006 0.8333 +- 0.0048   2545.0 +- 0.0
                    MAIT 0.721 +- 0.0067 0.8886 +- 0.0052 0.796 +- 0.0029    975.0 +- 0.0
           Memory B cell 0.8695 +- 0.0027 0.9401 +- 0.0027 0.9034 +- 0.0024    897.0 +- 0.0
                 NK cell 0.9675 +- 0.0011 0.8389 +- 0.0036 0.8986 +- 0.0021   2582.0 +- 0.0
            Naive B cell 0.9757 +- 0.0009 0.9418 +- 0.0016 0.9585 +- 0.0011   2232.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9875 +- 0.0086 0.9937 +- 0.0044     56.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.6754 +- 0.0189 0.8061 +- 0.0135     57.0 +- 0.0
       T regulatory cell 0.1814 +- 0.0037  0.25 +- 0.0078 0.2102 +- 0.005    136.0 +- 0.0

                accuracy                                 0.8667 +- 0.0015  22446.0 +- 0.0
               macro avg 0.8355 +- 0.0007 0.8188 +- 0.0032 0.8194 +- 0.0021  22446.0 +- 0.0
            weighted avg 0.8932 +- 0.0005 0.8667 +- 0.0015 0.875 +- 0.0011  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8511 +- 0.0061
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8667 +- 0.0015
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8511 +- 0.0013
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8521 +- 0.0014
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8015 +- 0.0014


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8049 +- 0.0038
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8195 +- 0.0021
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.808 +- 0.0019
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8067 +- 0.002
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.7616 +- 0.0018



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.7182 +- 0.0019

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9918 +- 0.0009 0.9791 +- 0.0012 0.9854 +- 0.0007    775.0 +- 0.0
          CD16+ Monocyte 0.9424 +- 0.0024 0.9895 +- 0.0037 0.9653 +- 0.0014    114.0 +- 0.0
    CD1C+ dendritic cell 0.8796 +- 0.0079 0.9301 +- 0.0043 0.9041 +- 0.0054     73.0 +- 0.0
       CD4 Memory T cell 0.6979 +- 0.0376 0.0311 +- 0.0013 0.0596 +- 0.0025   1098.0 +- 0.0
        CD4 Naive T cell 0.8255 +- 0.0074 0.9482 +- 0.0052 0.8826 +- 0.002   3173.0 +- 0.0
       CD8 Memory T cell 0.0066 +- 0.002 0.0036 +- 0.0013 0.0047 +- 0.0016    823.0 +- 0.0
        CD8 Naive T cell 0.9511 +- 0.003 0.8907 +- 0.0044 0.9199 +- 0.0014   1349.0 +- 0.0
      Gamma-delta T cell 0.099 +- 0.0036 0.2514 +- 0.0098 0.1421 +- 0.0053    325.0 +- 0.0
                    MAIT 0.2612 +- 0.0032 0.9942 +- 0.0017 0.4137 +- 0.0039    191.0 +- 0.0
           Memory B cell 0.9553 +- 0.0022 0.7263 +- 0.0061 0.8252 +- 0.0036    353.0 +- 0.0
                 NK cell 0.9728 +- 0.004 0.9424 +- 0.0044 0.9573 +- 0.0013    876.0 +- 0.0
            Naive B cell 0.8414 +- 0.003 0.9844 +- 0.0013 0.9073 +- 0.0015    513.0 +- 0.0
             Plasma cell 0.985 +- 0.0002  0.94 +- 0.0148 0.9619 +- 0.0078     70.0 +- 0.0
Plasmacytoid dendritic cell 0.9957 +- 0.009   0.9787 +- 0.0 0.9871 +- 0.0044     47.0 +- 0.0
       T regulatory cell 0.0535 +- 0.0055 0.0621 +- 0.0093 0.0574 +- 0.007    203.0 +- 0.0

                accuracy                                 0.7182 +- 0.0019   9983.0 +- 0.0
               macro avg 0.6973 +- 0.0026 0.7101 +- 0.0021 0.6649 +- 0.0013   9983.0 +- 0.0
            weighted avg 0.7457 +- 0.0026 0.7182 +- 0.0019 0.6908 +- 0.0007   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7057 +- 0.0053
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.7181 +- 0.002
Feature importance dropout (0.5% features dropped) Accuracy score: 0.7055 +- 0.001
Feature importance dropout (1.0% features dropped) Accuracy score: 0.7048 +- 0.0009
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6253 +- 0.0007


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.657 +- 0.0027
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.665 +- 0.0013
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6608 +- 0.001
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6596 +- 0.0009
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.62 +- 0.0009


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.6644 +- 0.0006

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9921 +- 0.0005 0.9968 +- 0.0006 0.9945 +- 0.0003   1466.0 +- 0.0
          CD16+ Monocyte 0.9864 +- 0.0033 0.9776 +- 0.002 0.982 +- 0.0015    237.0 +- 0.0
    CD1C+ dendritic cell 0.9596 +- 0.0083 0.933 +- 0.0088 0.9461 +- 0.0026     94.0 +- 0.0
       CD4 Memory T cell 0.8283 +- 0.0186 0.0402 +- 0.0022 0.0767 +- 0.0041   1916.0 +- 0.0
        CD4 Naive T cell 0.7786 +- 0.0063 0.952 +- 0.0034 0.8565 +- 0.0025   2232.0 +- 0.0
       CD8 Memory T cell 0.008 +- 0.0007 0.0101 +- 0.0009 0.0089 +- 0.0008    786.0 +- 0.0
        CD8 Naive T cell 0.9068 +- 0.0028 0.9178 +- 0.0045 0.9123 +- 0.0018    686.0 +- 0.0
      Gamma-delta T cell 0.1792 +- 0.0028 0.3918 +- 0.0089 0.2459 +- 0.0043    354.0 +- 0.0
                    MAIT 0.3243 +- 0.0028 0.973 +- 0.0064 0.4864 +- 0.0031    315.0 +- 0.0
           Memory B cell 0.9756 +- 0.0007 0.7684 +- 0.0063 0.8597 +- 0.0038    474.0 +- 0.0
                 NK cell 0.9895 +- 0.0008 0.9776 +- 0.0017 0.9835 +- 0.0011    629.0 +- 0.0
            Naive B cell 0.8163 +- 0.0041   0.9879 +- 0.0 0.8939 +- 0.0024    494.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9225 +- 0.0079 0.9597 +- 0.0043     40.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.9577 +- 0.0152 0.9783 +- 0.0079     52.0 +- 0.0
       T regulatory cell 0.0775 +- 0.0068 0.104 +- 0.0115 0.0888 +- 0.0086    223.0 +- 0.0

                accuracy                                 0.6644 +- 0.0006   9998.0 +- 0.0
               macro avg 0.7215 +- 0.0012 0.7274 +- 0.0018 0.6849 +- 0.001   9998.0 +- 0.0
            weighted avg 0.7496 +- 0.0033 0.6644 +- 0.0006  0.629 +- 0.001   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6604 +- 0.0022
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6648 +- 0.0007
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6619 +- 0.0004
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6623 +- 0.0004
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6295 +- 0.0005


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6785 +- 0.0022
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6855 +- 0.0008
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6846 +- 0.001
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6833 +- 0.0011
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6539 +- 0.0017


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.6762 +- 0.0007

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9891 +- 0.0007 0.9944 +- 0.0003 0.9917 +- 0.0005   2024.0 +- 0.0
          CD16+ Monocyte 0.9924 +- 0.0008 0.9692 +- 0.0032 0.9806 +- 0.0015    389.0 +- 0.0
    CD1C+ dendritic cell 0.9269 +- 0.0083 0.9073 +- 0.0057 0.917 +- 0.0065    123.0 +- 0.0
       CD4 Memory T cell 0.852 +- 0.0084 0.1833 +- 0.0033 0.3016 +- 0.0042   2300.0 +- 0.0
        CD4 Naive T cell 0.6088 +- 0.0132 0.9544 +- 0.0059 0.7433 +- 0.008   1554.0 +- 0.0
       CD8 Memory T cell  0.01 +- 0.0012 0.0082 +- 0.0013 0.009 +- 0.0013    814.0 +- 0.0
        CD8 Naive T cell 0.6932 +- 0.0112 0.9167 +- 0.0079 0.7893 +- 0.006    180.0 +- 0.0
      Gamma-delta T cell 0.1338 +- 0.003 0.4267 +- 0.0134 0.2037 +- 0.005    225.0 +- 0.0
                    MAIT 0.3109 +- 0.0046 0.9866 +- 0.0043 0.4728 +- 0.005    238.0 +- 0.0
           Memory B cell 0.986 +- 0.0001 0.775 +- 0.0045 0.8678 +- 0.0029    272.0 +- 0.0
                 NK cell 0.9603 +- 0.0015 0.9957 +- 0.0005 0.9777 +- 0.0008   1040.0 +- 0.0
            Naive B cell 0.8872 +- 0.002   0.9939 +- 0.0 0.9375 +- 0.0011    492.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0
Plasmacytoid dendritic cell 0.9844 +- 0.0107      1.0 +- 0.0 0.9921 +- 0.0054     44.0 +- 0.0
       T regulatory cell 0.1439 +- 0.0054 0.1237 +- 0.0108 0.1329 +- 0.0083    262.0 +- 0.0

                accuracy                                 0.6762 +- 0.0007   9997.0 +- 0.0
               macro avg 0.6986 +- 0.0011 0.749 +- 0.0007 0.6878 +- 0.0006   9997.0 +- 0.0
            weighted avg 0.7472 +- 0.0016 0.6762 +- 0.0007 0.6493 +- 0.0018   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6721 +- 0.005
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6755 +- 0.0005
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6757 +- 0.0007
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6753 +- 0.0007
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6721 +- 0.001


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6805 +- 0.0024
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6883 +- 0.0007
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6885 +- 0.0008
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6884 +- 0.0008
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6678 +- 0.0019


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.7583 +- 0.0071

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.964 +- 0.0005   0.9962 +- 0.0 0.9798 +- 0.0002   2125.0 +- 0.0
          CD16+ Monocyte   0.9823 +- 0.0 0.9104 +- 0.0023 0.945 +- 0.0013    489.0 +- 0.0
    CD1C+ dendritic cell      1.0 +- 0.0 0.7514 +- 0.003 0.8581 +- 0.002    105.0 +- 0.0
       CD4 Memory T cell 0.4119 +- 0.0096 0.5357 +- 0.0084 0.4656 +- 0.0065    754.0 +- 0.0
        CD4 Naive T cell  0.851 +- 0.004 0.6616 +- 0.0219 0.7442 +- 0.0131   1396.0 +- 0.0
       CD8 Memory T cell 0.1781 +- 0.0033 0.4321 +- 0.0431 0.2518 +- 0.009    312.0 +- 0.0
        CD8 Naive T cell  0.937 +- 0.006 0.8562 +- 0.0048 0.8947 +- 0.0035   1105.0 +- 0.0
      Gamma-delta T cell 0.2671 +- 0.0629 0.1126 +- 0.0397 0.1578 +- 0.0508    493.0 +- 0.0
                    MAIT 0.3772 +- 0.0089 0.5774 +- 0.0229 0.4562 +- 0.0115    217.0 +- 0.0
           Memory B cell 0.9253 +- 0.0113 0.2354 +- 0.0419 0.3735 +- 0.0534    277.0 +- 0.0
                 NK cell 0.8724 +- 0.0061 0.8867 +- 0.0166 0.8794 +- 0.0092   1363.0 +- 0.0
            Naive B cell 0.7427 +- 0.0107 0.9906 +- 0.0033 0.8489 +- 0.0062    618.0 +- 0.0
             Plasma cell 0.9805 +- 0.0158 0.9674 +- 0.0154 0.9737 +- 0.0077     46.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     51.0 +- 0.0
       T regulatory cell 0.0852 +- 0.0074 0.023 +- 0.0026 0.0362 +- 0.0037    165.0 +- 0.0

                accuracy                                 0.7583 +- 0.0071   9516.0 +- 0.0
               macro avg 0.705 +- 0.0045 0.6625 +- 0.0065 0.6577 +- 0.0089   9516.0 +- 0.0
            weighted avg 0.783 +- 0.0051 0.7583 +- 0.0071 0.7563 +- 0.0081   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7536 +- 0.0114
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.7581 +- 0.0068
Feature importance dropout (0.5% features dropped) Accuracy score: 0.7436 +- 0.0067
Feature importance dropout (1.0% features dropped) Accuracy score: 0.737 +- 0.0074
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7245 +- 0.0075


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6547 +- 0.0101
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6578 +- 0.0084
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6498 +- 0.0086
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6481 +- 0.0091
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6352 +- 0.0107


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



