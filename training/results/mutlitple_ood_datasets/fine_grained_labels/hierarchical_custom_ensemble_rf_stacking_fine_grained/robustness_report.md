# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8329 +- 0.0024

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9938 +- 0.0004 0.9967 +- 0.0003 0.9952 +- 0.0002   3456.0 +- 0.0
          CD16+ Monocyte 0.9817 +- 0.0037 0.949 +- 0.0033 0.965 +- 0.0021    192.0 +- 0.0
    CD1C+ dendritic cell 0.9241 +- 0.0059 0.9019 +- 0.0048 0.9128 +- 0.0039    108.0 +- 0.0
       CD4 Memory T cell 0.8729 +- 0.0124 0.9826 +- 0.0022 0.9245 +- 0.0064   2890.0 +- 0.0
        CD4 Naive T cell 0.9214 +- 0.0023 0.9505 +- 0.0018 0.9357 +- 0.001   3439.0 +- 0.0
       CD8 Memory T cell 0.1863 +- 0.0017 0.7364 +- 0.0068 0.2974 +- 0.0026    818.0 +- 0.0
        CD8 Naive T cell 0.9484 +- 0.0035 0.749 +- 0.0226 0.8368 +- 0.0138   2063.0 +- 0.0
      Gamma-delta T cell 0.9374 +- 0.0025 0.2689 +- 0.0017 0.4179 +- 0.002   2545.0 +- 0.0
                    MAIT 0.9133 +- 0.0036 0.9058 +- 0.0042 0.9095 +- 0.0029    975.0 +- 0.0
           Memory B cell 0.969 +- 0.0104 0.9119 +- 0.0019 0.9396 +- 0.005    897.0 +- 0.0
                 NK cell 0.9948 +- 0.0015 0.7776 +- 0.0081 0.8729 +- 0.0051   2582.0 +- 0.0
            Naive B cell 0.9654 +- 0.0007 0.9883 +- 0.0042 0.9767 +- 0.0021   2232.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9607 +- 0.0075 0.9799 +- 0.0039     56.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.6649 +- 0.0055 0.7987 +- 0.004     57.0 +- 0.0
       T regulatory cell 0.2731 +- 0.0203 0.1772 +- 0.0122 0.2149 +- 0.0149    136.0 +- 0.0

                accuracy                                 0.8329 +- 0.0024  22446.0 +- 0.0
               macro avg 0.8588 +- 0.0022 0.7948 +- 0.0023 0.7985 +- 0.0023  22446.0 +- 0.0
            weighted avg 0.9152 +- 0.0015 0.8329 +- 0.0024 0.8438 +- 0.0025  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8211 +- 0.0047
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8329 +- 0.0024
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8229 +- 0.0031
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8218 +- 0.0031
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7687 +- 0.0019


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.7869 +- 0.004
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.7985 +- 0.0023
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.792 +- 0.0027
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.7892 +- 0.0029
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.7381 +- 0.0023



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.7392 +- 0.0017

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9964 +- 0.0016 0.9741 +- 0.0014 0.9851 +- 0.0006    775.0 +- 0.0
          CD16+ Monocyte 0.9449 +- 0.0065 0.9921 +- 0.005 0.9679 +- 0.0022    114.0 +- 0.0
    CD1C+ dendritic cell 0.8408 +- 0.0048 0.9767 +- 0.0092 0.9037 +- 0.0042     73.0 +- 0.0
       CD4 Memory T cell   0.1 +- 0.3162 0.0001 +- 0.0003 0.0002 +- 0.0006   1098.0 +- 0.0
        CD4 Naive T cell 0.8066 +- 0.005 0.9708 +- 0.0026 0.8811 +- 0.0022   3173.0 +- 0.0
       CD8 Memory T cell  0.13 +- 0.0063 0.0804 +- 0.005 0.0993 +- 0.0051    823.0 +- 0.0
        CD8 Naive T cell 0.9557 +- 0.0032 0.9072 +- 0.0102 0.9308 +- 0.0042   1349.0 +- 0.0
      Gamma-delta T cell 0.1168 +- 0.0043 0.2702 +- 0.0114 0.1631 +- 0.0063    325.0 +- 0.0
                    MAIT 0.3548 +- 0.0031   0.9843 +- 0.0 0.5216 +- 0.0034    191.0 +- 0.0
           Memory B cell 0.9633 +- 0.0015 0.834 +- 0.0102 0.894 +- 0.0062    353.0 +- 0.0
                 NK cell 0.9887 +- 0.0041 0.9682 +- 0.0067 0.9783 +- 0.0035    876.0 +- 0.0
            Naive B cell 0.8974 +- 0.0058 0.9821 +- 0.0008 0.9378 +- 0.0033    513.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     47.0 +- 0.0
       T regulatory cell 0.1138 +- 0.0145 0.1616 +- 0.019 0.1334 +- 0.0156    203.0 +- 0.0

                accuracy                                 0.7392 +- 0.0017   9983.0 +- 0.0
               macro avg 0.6797 +- 0.0205 0.7382 +- 0.0015 0.6916 +- 0.0011   9983.0 +- 0.0
            weighted avg 0.693 +- 0.0351 0.7392 +- 0.0017 0.7034 +- 0.0014   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7266 +- 0.0054
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.7392 +- 0.0017
Feature importance dropout (0.5% features dropped) Accuracy score: 0.7227 +- 0.0053
Feature importance dropout (1.0% features dropped) Accuracy score: 0.7231 +- 0.0053
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6269 +- 0.0023


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6865 +- 0.0035
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6916 +- 0.0011
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6863 +- 0.0024
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6879 +- 0.002
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6316 +- 0.0027


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.6732 +- 0.0006

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.996 +- 0.0003 0.9951 +- 0.0005 0.9956 +- 0.0003   1466.0 +- 0.0
          CD16+ Monocyte 0.9852 +- 0.0041 0.9797 +- 0.0018 0.9824 +- 0.002    237.0 +- 0.0
    CD1C+ dendritic cell 0.9321 +- 0.0046   0.9787 +- 0.0 0.9549 +- 0.0024     94.0 +- 0.0
       CD4 Memory T cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   1916.0 +- 0.0
        CD4 Naive T cell 0.8172 +- 0.0045 0.9593 +- 0.0018 0.8826 +- 0.0021   2232.0 +- 0.0
       CD8 Memory T cell 0.0642 +- 0.0049 0.0944 +- 0.0082 0.0764 +- 0.0061    786.0 +- 0.0
        CD8 Naive T cell 0.9368 +- 0.0059 0.9224 +- 0.0062 0.9296 +- 0.0024    686.0 +- 0.0
      Gamma-delta T cell 0.2169 +- 0.0038 0.4506 +- 0.0112 0.2928 +- 0.0057    354.0 +- 0.0
                    MAIT 0.3965 +- 0.0054 0.9841 +- 0.003 0.5652 +- 0.0052    315.0 +- 0.0
           Memory B cell  0.972 +- 0.002 0.8726 +- 0.0051 0.9196 +- 0.0032    474.0 +- 0.0
                 NK cell 0.9909 +- 0.0016 0.9692 +- 0.004 0.9799 +- 0.0022    629.0 +- 0.0
            Naive B cell 0.8893 +- 0.004 0.982 +- 0.0018 0.9333 +- 0.0025    494.0 +- 0.0
             Plasma cell      1.0 +- 0.0    0.925 +- 0.0    0.961 +- 0.0     40.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0   0.9615 +- 0.0   0.9804 +- 0.0     52.0 +- 0.0
       T regulatory cell 0.0622 +- 0.0052 0.1556 +- 0.0122 0.0888 +- 0.0072    223.0 +- 0.0

                accuracy                                 0.6732 +- 0.0006   9998.0 +- 0.0
               macro avg  0.684 +- 0.001 0.7487 +- 0.0011 0.7028 +- 0.001   9998.0 +- 0.0
            weighted avg 0.6131 +- 0.0013 0.6732 +- 0.0006 0.6355 +- 0.001   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6708 +- 0.0037
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6732 +- 0.0006
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6701 +- 0.0016
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6718 +- 0.0015
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6261 +- 0.0023


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6984 +- 0.0042
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.7028 +- 0.0011
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.7013 +- 0.0016
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.7038 +- 0.0015
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6583 +- 0.0036


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.6528 +- 0.0011

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9963 +- 0.001 0.9912 +- 0.0008 0.9937 +- 0.0007   2024.0 +- 0.0
          CD16+ Monocyte 0.9953 +- 0.0011 0.9823 +- 0.0048 0.9887 +- 0.0026    389.0 +- 0.0
    CD1C+ dendritic cell 0.8686 +- 0.0087 0.9724 +- 0.0042 0.9175 +- 0.0052    123.0 +- 0.0
       CD4 Memory T cell 0.882 +- 0.0894 0.0021 +- 0.0007 0.0042 +- 0.0014   2300.0 +- 0.0
        CD4 Naive T cell 0.4785 +- 0.0052 0.9903 +- 0.0006 0.6452 +- 0.0047   1554.0 +- 0.0
       CD8 Memory T cell   0.184 +- 0.02 0.1305 +- 0.0153 0.1525 +- 0.0168    814.0 +- 0.0
        CD8 Naive T cell 0.8864 +- 0.0161 0.8817 +- 0.0111 0.8839 +- 0.008    180.0 +- 0.0
      Gamma-delta T cell 0.1186 +- 0.0099 0.3267 +- 0.0349 0.174 +- 0.0155    225.0 +- 0.0
                    MAIT 0.375 +- 0.0055 0.9807 +- 0.0053 0.5425 +- 0.0059    238.0 +- 0.0
           Memory B cell 0.9839 +- 0.0001   0.9 +- 0.0064 0.9401 +- 0.0036    272.0 +- 0.0
                 NK cell 0.9944 +- 0.0016 0.9862 +- 0.0032 0.9903 +- 0.0013   1040.0 +- 0.0
            Naive B cell 0.9472 +- 0.0032   0.9919 +- 0.0 0.969 +- 0.0017    492.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     44.0 +- 0.0
       T regulatory cell 0.1667 +- 0.0123 0.2294 +- 0.0151 0.1926 +- 0.008    262.0 +- 0.0

                accuracy                                 0.6528 +- 0.0011   9997.0 +- 0.0
               macro avg 0.7251 +- 0.0069 0.7577 +- 0.0021 0.693 +- 0.0017   9997.0 +- 0.0
            weighted avg 0.7606 +- 0.0215 0.6528 +- 0.0011 0.5871 +- 0.0012   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6503 +- 0.0018
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6528 +- 0.0011
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6509 +- 0.0012
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6502 +- 0.0013
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6377 +- 0.0011


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6875 +- 0.0038
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6929 +- 0.0016
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6889 +- 0.0021
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6888 +- 0.002
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6444 +- 0.0019


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.8189 +- 0.0036

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9772 +- 0.001 0.9945 +- 0.0007 0.9858 +- 0.0006   2125.0 +- 0.0
          CD16+ Monocyte 0.9807 +- 0.0028 0.9468 +- 0.0041 0.9635 +- 0.0024    489.0 +- 0.0
    CD1C+ dendritic cell 0.9647 +- 0.0045 0.8333 +- 0.005 0.8942 +- 0.0035    105.0 +- 0.0
       CD4 Memory T cell 0.5025 +- 0.0264 0.1438 +- 0.0199 0.2229 +- 0.0249    754.0 +- 0.0
        CD4 Naive T cell 0.8092 +- 0.0036 0.9303 +- 0.0102 0.8655 +- 0.0049   1396.0 +- 0.0
       CD8 Memory T cell 0.2632 +- 0.0095 0.8971 +- 0.0199 0.4069 +- 0.0121    312.0 +- 0.0
        CD8 Naive T cell 0.9953 +- 0.0009 0.9744 +- 0.0032 0.9847 +- 0.0018   1105.0 +- 0.0
      Gamma-delta T cell 0.3257 +- 0.0468 0.0181 +- 0.0081 0.034 +- 0.0146    493.0 +- 0.0
                    MAIT 0.5216 +- 0.0139 0.9737 +- 0.0107 0.6792 +- 0.0111    217.0 +- 0.0
           Memory B cell 0.9694 +- 0.0011 0.9022 +- 0.0077 0.9345 +- 0.0041    277.0 +- 0.0
                 NK cell 0.9973 +- 0.003 0.8505 +- 0.0271 0.9178 +- 0.016   1363.0 +- 0.0
            Naive B cell 0.9575 +- 0.0032 0.9888 +- 0.0005 0.9729 +- 0.0016    618.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     46.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.9824 +- 0.0062 0.9911 +- 0.0031     51.0 +- 0.0
       T regulatory cell 0.1228 +- 0.0101 0.1764 +- 0.0247 0.1446 +- 0.0151    165.0 +- 0.0

                accuracy                                 0.8189 +- 0.0036   9516.0 +- 0.0
               macro avg 0.7591 +- 0.0031 0.7741 +- 0.0027 0.7332 +- 0.0022   9516.0 +- 0.0
            weighted avg 0.8363 +- 0.0023 0.8189 +- 0.0036 0.8036 +- 0.0021   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8002 +- 0.0126
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8189 +- 0.0036
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8076 +- 0.0062
Feature importance dropout (1.0% features dropped) Accuracy score: 0.801 +- 0.0066
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8009 +- 0.0067


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.718 +- 0.007
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.7331 +- 0.0022
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.7271 +- 0.0034
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.7241 +- 0.0034
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.7224 +- 0.0035


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



