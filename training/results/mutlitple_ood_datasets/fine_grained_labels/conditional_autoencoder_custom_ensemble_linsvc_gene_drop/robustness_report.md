# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8136 +- 0.0052

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9914 +- 0.0006 0.9974 +- 0.0003 0.9944 +- 0.0003   3456.0 +- 0.0
          CD16+ Monocyte 0.9852 +- 0.0044 0.9328 +- 0.0057 0.9583 +- 0.0032    192.0 +- 0.0
    CD1C+ dendritic cell 0.9478 +- 0.0075 0.8731 +- 0.0088 0.9089 +- 0.0063    108.0 +- 0.0
       CD4 Memory T cell 0.9122 +- 0.0044 0.5853 +- 0.0296 0.7127 +- 0.0223   2890.0 +- 0.0
        CD4 Naive T cell 0.7262 +- 0.0084 0.9405 +- 0.0023 0.8195 +- 0.005   3439.0 +- 0.0
       CD8 Memory T cell 0.2031 +- 0.0075 0.601 +- 0.0135 0.3035 +- 0.0092    818.0 +- 0.0
        CD8 Naive T cell 0.8988 +- 0.0081 0.8685 +- 0.0038 0.8833 +- 0.0041   2063.0 +- 0.0
      Gamma-delta T cell 0.9484 +- 0.0024 0.6265 +- 0.0184 0.7544 +- 0.0135   2545.0 +- 0.0
                    MAIT 0.7274 +- 0.0092 0.8099 +- 0.0047 0.7664 +- 0.0059    975.0 +- 0.0
           Memory B cell 0.8826 +- 0.0025 0.9376 +- 0.0043 0.9092 +- 0.0024    897.0 +- 0.0
                 NK cell 0.963 +- 0.0031 0.7329 +- 0.0084 0.8323 +- 0.0045   2582.0 +- 0.0
            Naive B cell 0.9747 +- 0.0016 0.9488 +- 0.0018 0.9616 +- 0.0013   2232.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9857 +- 0.0075 0.9928 +- 0.0038     56.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.6544 +- 0.0118 0.791 +- 0.0087     57.0 +- 0.0
       T regulatory cell 0.3536 +- 0.0738 0.0301 +- 0.0095 0.055 +- 0.0167    136.0 +- 0.0

                accuracy                                 0.8136 +- 0.0052  22446.0 +- 0.0
               macro avg 0.8343 +- 0.0059 0.7683 +- 0.0037 0.7762 +- 0.0033  22446.0 +- 0.0
            weighted avg 0.8736 +- 0.0027 0.8136 +- 0.0052 0.8266 +- 0.005  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7964 +- 0.0061
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8132 +- 0.0052
Feature importance dropout (0.5% features dropped) Accuracy score: 0.799 +- 0.0044
Feature importance dropout (1.0% features dropped) Accuracy score: 0.796 +- 0.0045
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7459 +- 0.0047


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.762 +- 0.003
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.7761 +- 0.0033
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.7678 +- 0.0026
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.765 +- 0.0027
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.7275 +- 0.0027



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.7274 +- 0.0019

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9951 +- 0.0014 0.9779 +- 0.002 0.9865 +- 0.0008    775.0 +- 0.0
          CD16+ Monocyte 0.9268 +- 0.0069 0.9772 +- 0.0074 0.9513 +- 0.0046    114.0 +- 0.0
    CD1C+ dendritic cell 0.8834 +- 0.0115 0.9849 +- 0.0043 0.9314 +- 0.0058     73.0 +- 0.0
       CD4 Memory T cell 0.7235 +- 0.0242 0.0509 +- 0.0045 0.0951 +- 0.0078   1098.0 +- 0.0
        CD4 Naive T cell 0.7836 +- 0.0051 0.9772 +- 0.0009 0.8698 +- 0.0031   3173.0 +- 0.0
       CD8 Memory T cell 0.069 +- 0.0079 0.0501 +- 0.0076 0.058 +- 0.0078    823.0 +- 0.0
        CD8 Naive T cell 0.9498 +- 0.0022 0.8947 +- 0.0084 0.9214 +- 0.0039   1349.0 +- 0.0
      Gamma-delta T cell 0.1003 +- 0.0048 0.2754 +- 0.0164 0.147 +- 0.0074    325.0 +- 0.0
                    MAIT 0.4015 +- 0.0118 0.9812 +- 0.0056 0.5697 +- 0.0121    191.0 +- 0.0
           Memory B cell 0.9611 +- 0.0024 0.7357 +- 0.0099 0.8334 +- 0.0063    353.0 +- 0.0
                 NK cell 0.9764 +- 0.0015 0.8678 +- 0.0097 0.9189 +- 0.0054    876.0 +- 0.0
            Naive B cell 0.8456 +- 0.0049 0.9852 +- 0.001 0.9101 +- 0.0027    513.0 +- 0.0
             Plasma cell 0.9971 +- 0.0062   0.9571 +- 0.0 0.9767 +- 0.003     70.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.9851 +- 0.0103 0.9925 +- 0.0052     47.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    203.0 +- 0.0

                accuracy                                 0.7274 +- 0.0019   9983.0 +- 0.0
               macro avg 0.7076 +- 0.0033 0.7134 +- 0.0021 0.6774 +- 0.0024   9983.0 +- 0.0
            weighted avg 0.7427 +- 0.0038 0.7274 +- 0.0019 0.6945 +- 0.0021   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7175 +- 0.0024
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.7273 +- 0.0017
Feature importance dropout (0.5% features dropped) Accuracy score: 0.7103 +- 0.0024
Feature importance dropout (1.0% features dropped) Accuracy score: 0.7095 +- 0.0024
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6736 +- 0.0027


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6714 +- 0.0024
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6775 +- 0.0022
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6722 +- 0.0024
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6694 +- 0.0027
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6555 +- 0.0022


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.6702 +- 0.0015

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9943 +- 0.0009 0.9946 +- 0.0004 0.9944 +- 0.0004   1466.0 +- 0.0
          CD16+ Monocyte 0.9886 +- 0.002 0.9835 +- 0.0058 0.986 +- 0.0025    237.0 +- 0.0
    CD1C+ dendritic cell 0.9352 +- 0.0041 0.9511 +- 0.0055 0.943 +- 0.0034     94.0 +- 0.0
       CD4 Memory T cell 0.7926 +- 0.0424 0.0398 +- 0.006 0.0757 +- 0.0108   1916.0 +- 0.0
        CD4 Naive T cell 0.6871 +- 0.0052 0.9828 +- 0.0026 0.8088 +- 0.0029   2232.0 +- 0.0
       CD8 Memory T cell 0.0848 +- 0.0077 0.119 +- 0.0151 0.099 +- 0.0104    786.0 +- 0.0
        CD8 Naive T cell 0.9173 +- 0.0047 0.8806 +- 0.0081 0.8985 +- 0.005    686.0 +- 0.0
      Gamma-delta T cell 0.152 +- 0.0053 0.3042 +- 0.0138 0.2027 +- 0.0074    354.0 +- 0.0
                    MAIT 0.3964 +- 0.0112 0.9841 +- 0.003  0.565 +- 0.011    315.0 +- 0.0
           Memory B cell 0.9717 +- 0.0024 0.7829 +- 0.0121 0.8671 +- 0.0071    474.0 +- 0.0
                 NK cell 0.9783 +- 0.0028 0.9362 +- 0.0072 0.9568 +- 0.0027    629.0 +- 0.0
            Naive B cell 0.8259 +- 0.0081  0.983 +- 0.002 0.8976 +- 0.0043    494.0 +- 0.0
             Plasma cell      1.0 +- 0.0  0.94 +- 0.0129 0.969 +- 0.0069     40.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.9827 +- 0.0061 0.9913 +- 0.0031     52.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    223.0 +- 0.0

                accuracy                                 0.6702 +- 0.0015   9998.0 +- 0.0
               macro avg 0.7149 +- 0.0029 0.7243 +- 0.0016 0.6837 +- 0.0019   9998.0 +- 0.0
            weighted avg 0.7284 +- 0.0073 0.6702 +- 0.0015 0.6222 +- 0.0029   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6624 +- 0.0015
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.67 +- 0.0015
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6655 +- 0.0016
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6656 +- 0.0016
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6492 +- 0.0024


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6773 +- 0.0021
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6837 +- 0.0018
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.682 +- 0.0016
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6776 +- 0.0013
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6669 +- 0.0021


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.6577 +- 0.0025

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9949 +- 0.0011 0.9935 +- 0.0006 0.9942 +- 0.0004   2024.0 +- 0.0
          CD16+ Monocyte 0.9915 +- 0.0021 0.9864 +- 0.003 0.9889 +- 0.002    389.0 +- 0.0
    CD1C+ dendritic cell 0.9227 +- 0.0091 0.9488 +- 0.0086 0.9355 +- 0.0028    123.0 +- 0.0
       CD4 Memory T cell 0.8012 +- 0.0253 0.0846 +- 0.011 0.1528 +- 0.0184   2300.0 +- 0.0
        CD4 Naive T cell 0.6059 +- 0.008 0.973 +- 0.0038 0.7468 +- 0.0053   1554.0 +- 0.0
       CD8 Memory T cell 0.0682 +- 0.0048 0.1195 +- 0.0128 0.0868 +- 0.0072    814.0 +- 0.0
        CD8 Naive T cell 0.8191 +- 0.0088 0.9006 +- 0.0096 0.8579 +- 0.0085    180.0 +- 0.0
      Gamma-delta T cell 0.1133 +- 0.0062 0.3729 +- 0.0229 0.1738 +- 0.0098    225.0 +- 0.0
                    MAIT 0.4433 +- 0.0106 0.9634 +- 0.0053 0.6072 +- 0.0097    238.0 +- 0.0
           Memory B cell 0.9846 +- 0.0021 0.8688 +- 0.0111 0.923 +- 0.0067    272.0 +- 0.0
                 NK cell 0.9787 +- 0.0019 0.9382 +- 0.0063 0.958 +- 0.0035   1040.0 +- 0.0
            Naive B cell 0.932 +- 0.0054 0.9937 +- 0.0006 0.9618 +- 0.0028    492.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9825 +- 0.0121 0.9911 +- 0.0061     40.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     44.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    262.0 +- 0.0

                accuracy                                 0.6577 +- 0.0025   9997.0 +- 0.0
               macro avg 0.7104 +- 0.0017 0.7417 +- 0.0018 0.6919 +- 0.0014   9997.0 +- 0.0
            weighted avg 0.7461 +- 0.0051 0.6577 +- 0.0025 0.6239 +- 0.0041   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6493 +- 0.0037
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6566 +- 0.0026
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6542 +- 0.0032
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6529 +- 0.0032
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6426 +- 0.0028


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6842 +- 0.0028
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6916 +- 0.0016
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6903 +- 0.0019
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6833 +- 0.0031
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6671 +- 0.0022


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.6532 +- 0.0031

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9554 +- 0.0022 0.9977 +- 0.0004 0.9761 +- 0.0011   2125.0 +- 0.0
          CD16+ Monocyte 0.9913 +- 0.0023 0.8808 +- 0.0056 0.9327 +- 0.0027    489.0 +- 0.0
    CD1C+ dendritic cell      1.0 +- 0.0 0.6648 +- 0.031 0.7982 +- 0.0227    105.0 +- 0.0
       CD4 Memory T cell 0.2862 +- 0.0052 0.779 +- 0.0196 0.4186 +- 0.0063    754.0 +- 0.0
        CD4 Naive T cell 0.9143 +- 0.014 0.182 +- 0.0184 0.3033 +- 0.0259   1396.0 +- 0.0
       CD8 Memory T cell 0.142 +- 0.0051 0.716 +- 0.0377 0.2369 +- 0.0088    312.0 +- 0.0
        CD8 Naive T cell 0.9977 +- 0.001 0.7893 +- 0.0174 0.8813 +- 0.0105   1105.0 +- 0.0
      Gamma-delta T cell 0.028 +- 0.0086 0.0049 +- 0.0017 0.0083 +- 0.0028    493.0 +- 0.0
                    MAIT 0.7123 +- 0.0508 0.229 +- 0.0424 0.3451 +- 0.0511    217.0 +- 0.0
           Memory B cell 0.9582 +- 0.0138 0.1433 +- 0.0176  0.249 +- 0.027    277.0 +- 0.0
                 NK cell 0.9915 +- 0.0041 0.6267 +- 0.0181 0.7679 +- 0.0138   1363.0 +- 0.0
            Naive B cell 0.7191 +- 0.0048      1.0 +- 0.0 0.8366 +- 0.0033    618.0 +- 0.0
             Plasma cell 0.9626 +- 0.0176 0.9435 +- 0.0275 0.9527 +- 0.0169     46.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     51.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    165.0 +- 0.0

                accuracy                                 0.6532 +- 0.0031   9516.0 +- 0.0
               macro avg 0.7106 +- 0.0032 0.5971 +- 0.0063 0.5804 +- 0.0055   9516.0 +- 0.0
            weighted avg 0.797 +- 0.0025 0.6532 +- 0.0031 0.6523 +- 0.0042   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6497 +- 0.0095
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6531 +- 0.0031
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6362 +- 0.0049
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6252 +- 0.0049
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6218 +- 0.0046


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.5791 +- 0.0099
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.5804 +- 0.0055
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.5596 +- 0.0052
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.5548 +- 0.0052
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.5443 +- 0.0065


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



