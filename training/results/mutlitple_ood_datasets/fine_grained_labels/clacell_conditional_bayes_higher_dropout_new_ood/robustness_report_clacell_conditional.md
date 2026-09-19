# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8337 +- 0.0113

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9927 +- 0.0011 0.9961 +- 0.0007 0.9944 +- 0.0005   3456.0 +- 0.0
          CD16+ Monocyte 0.9594 +- 0.0136 0.9458 +- 0.0121 0.9525 +- 0.0104    192.0 +- 0.0
    CD1C+ dendritic cell 0.924 +- 0.0353 0.8852 +- 0.0146 0.9038 +- 0.0189    108.0 +- 0.0
       CD4 Memory T cell 0.912 +- 0.0122 0.6606 +- 0.0621 0.7648 +- 0.044   2890.0 +- 0.0
        CD4 Naive T cell 0.7503 +- 0.0178 0.9404 +- 0.0064 0.8346 +- 0.0116   3439.0 +- 0.0
       CD8 Memory T cell 0.2477 +- 0.0292 0.5945 +- 0.0206 0.3489 +- 0.0303    818.0 +- 0.0
        CD8 Naive T cell 0.8943 +- 0.014 0.8694 +- 0.0079 0.8816 +- 0.0074   2063.0 +- 0.0
      Gamma-delta T cell 0.9385 +- 0.0069 0.7006 +- 0.0391 0.8018 +- 0.0275   2545.0 +- 0.0
                    MAIT 0.7023 +- 0.0363 0.8321 +- 0.009 0.7612 +- 0.0203    975.0 +- 0.0
           Memory B cell 0.8738 +- 0.006 0.9271 +- 0.0097 0.8996 +- 0.004    897.0 +- 0.0
                 NK cell 0.9674 +- 0.006 0.751 +- 0.0167 0.8455 +- 0.0108   2582.0 +- 0.0
            Naive B cell  0.97 +- 0.0032 0.9451 +- 0.0041 0.9574 +- 0.0016   2232.0 +- 0.0
             Plasma cell 0.9895 +- 0.0147 0.9839 +- 0.0178 0.9865 +- 0.0088     56.0 +- 0.0
Plasmacytoid dendritic cell 0.9926 +- 0.0119 0.6719 +- 0.0341 0.8008 +- 0.0225     57.0 +- 0.0
       T regulatory cell 0.3779 +- 0.1984 0.014 +- 0.0088 0.0267 +- 0.0166    136.0 +- 0.0

                accuracy                                 0.8337 +- 0.0113  22446.0 +- 0.0
               macro avg 0.8328 +- 0.015 0.7812 +- 0.0079 0.784 +- 0.0069  22446.0 +- 0.0
            weighted avg 0.8759 +- 0.0044 0.8337 +- 0.0113 0.8427 +- 0.0099  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8186 +- 0.0107
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8335 +- 0.0113
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8203 +- 0.011
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8185 +- 0.0109
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7795 +- 0.0114


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.7713 +- 0.0063
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.784 +- 0.0069
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.7753 +- 0.0071
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.7731 +- 0.0067
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.7459 +- 0.0071



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.7258 +- 0.0022

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9925 +- 0.0031 0.9774 +- 0.0025 0.9849 +- 0.0024    775.0 +- 0.0
          CD16+ Monocyte  0.921 +- 0.012 0.9702 +- 0.0156 0.9449 +- 0.0096    114.0 +- 0.0
    CD1C+ dendritic cell 0.8819 +- 0.0193 0.9699 +- 0.0156 0.9237 +- 0.0163     73.0 +- 0.0
       CD4 Memory T cell 0.704 +- 0.0456  0.0473 +- 0.01 0.0884 +- 0.0176   1098.0 +- 0.0
        CD4 Naive T cell 0.778 +- 0.0105 0.979 +- 0.0033 0.8669 +- 0.0055   3173.0 +- 0.0
       CD8 Memory T cell 0.0462 +- 0.0116 0.0279 +- 0.0087 0.0347 +- 0.0101    823.0 +- 0.0
        CD8 Naive T cell 0.9428 +- 0.0038 0.8926 +- 0.0163 0.9169 +- 0.008   1349.0 +- 0.0
      Gamma-delta T cell 0.1093 +- 0.004 0.3037 +- 0.0147 0.1607 +- 0.0063    325.0 +- 0.0
                    MAIT 0.3612 +- 0.0199 0.9869 +- 0.0066 0.5286 +- 0.0212    191.0 +- 0.0
           Memory B cell 0.9641 +- 0.005 0.7076 +- 0.0335 0.8158 +- 0.0224    353.0 +- 0.0
                 NK cell 0.984 +- 0.0033 0.8719 +- 0.0125 0.9245 +- 0.0073    876.0 +- 0.0
            Naive B cell 0.8312 +- 0.0166 0.9848 +- 0.0024 0.9014 +- 0.0096    513.0 +- 0.0
             Plasma cell 0.9986 +- 0.0045 0.9757 +- 0.0136 0.987 +- 0.0067     70.0 +- 0.0
Plasmacytoid dendritic cell 0.9917 +- 0.0144 0.9936 +- 0.0103 0.9926 +- 0.0087     47.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    203.0 +- 0.0

                accuracy                                 0.7258 +- 0.0022   9983.0 +- 0.0
               macro avg 0.7004 +- 0.0044 0.7126 +- 0.0031 0.6714 +- 0.0033   9983.0 +- 0.0
            weighted avg 0.7352 +- 0.0068 0.7258 +- 0.0022 0.6893 +- 0.0037   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7121 +- 0.0049
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.7259 +- 0.0023
Feature importance dropout (0.5% features dropped) Accuracy score: 0.7103 +- 0.0033
Feature importance dropout (1.0% features dropped) Accuracy score: 0.7089 +- 0.003
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6723 +- 0.0042


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6632 +- 0.0045
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6716 +- 0.0035
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.666 +- 0.0039
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6633 +- 0.0048
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6476 +- 0.005


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.6674 +- 0.0015

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9927 +- 0.0015 0.9945 +- 0.001 0.9936 +- 0.0005   1466.0 +- 0.0
          CD16+ Monocyte 0.9847 +- 0.0039 0.9785 +- 0.0081 0.9816 +- 0.0032    237.0 +- 0.0
    CD1C+ dendritic cell 0.9305 +- 0.0146 0.9362 +- 0.0159 0.9332 +- 0.0099     94.0 +- 0.0
       CD4 Memory T cell 0.7622 +- 0.0474 0.0336 +- 0.0107 0.0642 +- 0.0196   1916.0 +- 0.0
        CD4 Naive T cell 0.684 +- 0.0148 0.9835 +- 0.0026 0.8067 +- 0.0097   2232.0 +- 0.0
       CD8 Memory T cell 0.0525 +- 0.0084 0.0663 +- 0.0129 0.0585 +- 0.0102    786.0 +- 0.0
        CD8 Naive T cell 0.9126 +- 0.0064 0.8915 +- 0.012 0.9019 +- 0.0075    686.0 +- 0.0
      Gamma-delta T cell 0.1683 +- 0.0069 0.3678 +- 0.0213 0.2309 +- 0.0106    354.0 +- 0.0
                    MAIT 0.3812 +- 0.0125 0.981 +- 0.0076 0.5489 +- 0.0125    315.0 +- 0.0
           Memory B cell 0.9706 +- 0.0048 0.7648 +- 0.0246 0.8553 +- 0.0145    474.0 +- 0.0
                 NK cell 0.9882 +- 0.0045 0.9472 +- 0.0136 0.9672 +- 0.0071    629.0 +- 0.0
            Naive B cell 0.8134 +- 0.0157 0.9828 +- 0.0038  0.89 +- 0.0085    494.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9425 +- 0.0121 0.9704 +- 0.0064     40.0 +- 0.0
Plasmacytoid dendritic cell 0.9961 +- 0.0082 0.9731 +- 0.0226 0.9843 +- 0.0125     52.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    223.0 +- 0.0

                accuracy                                 0.6674 +- 0.0015   9998.0 +- 0.0
               macro avg 0.7091 +- 0.0041 0.7229 +- 0.0029 0.6791 +- 0.0031   9998.0 +- 0.0
            weighted avg 0.7187 +- 0.0097 0.6674 +- 0.0015 0.6165 +- 0.0051   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6604 +- 0.0033
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6674 +- 0.0016
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6627 +- 0.0012
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6624 +- 0.0013
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6462 +- 0.0015


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6734 +- 0.0029
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6792 +- 0.0031
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6773 +- 0.0028
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6759 +- 0.0035
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6661 +- 0.0031


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.6575 +- 0.0043

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9941 +- 0.0006 0.9933 +- 0.0009 0.9937 +- 0.0005   2024.0 +- 0.0
          CD16+ Monocyte 0.9879 +- 0.006 0.9859 +- 0.0025 0.9869 +- 0.003    389.0 +- 0.0
    CD1C+ dendritic cell 0.931 +- 0.0128 0.9415 +- 0.0107 0.9361 +- 0.0083    123.0 +- 0.0
       CD4 Memory T cell 0.7774 +- 0.0278 0.0897 +- 0.0212 0.1601 +- 0.0345   2300.0 +- 0.0
        CD4 Naive T cell 0.5763 +- 0.0147 0.972 +- 0.0076 0.7235 +- 0.0101   1554.0 +- 0.0
       CD8 Memory T cell 0.0455 +- 0.0073 0.0639 +- 0.0128 0.0531 +- 0.0094    814.0 +- 0.0
        CD8 Naive T cell 0.7714 +- 0.0211 0.8906 +- 0.0162 0.8266 +- 0.0164    180.0 +- 0.0
      Gamma-delta T cell 0.1289 +- 0.0079 0.4364 +- 0.0322 0.199 +- 0.0127    225.0 +- 0.0
                    MAIT  0.39 +- 0.0166 0.9794 +- 0.0085 0.5576 +- 0.0168    238.0 +- 0.0
           Memory B cell 0.9883 +- 0.0028 0.8357 +- 0.0288 0.9053 +- 0.017    272.0 +- 0.0
                 NK cell 0.9827 +- 0.0044 0.9636 +- 0.0068 0.973 +- 0.0043   1040.0 +- 0.0
            Naive B cell 0.9151 +- 0.0133 0.9949 +- 0.0014 0.9533 +- 0.0072    492.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9975 +- 0.0079 0.9987 +- 0.004     40.0 +- 0.0
Plasmacytoid dendritic cell 0.9801 +- 0.0124      1.0 +- 0.0 0.9899 +- 0.0063     44.0 +- 0.0
       T regulatory cell   0.1 +- 0.3162 0.0004 +- 0.0012 0.0008 +- 0.0024    262.0 +- 0.0

                accuracy                                 0.6575 +- 0.0043   9997.0 +- 0.0
               macro avg 0.7046 +- 0.0227 0.743 +- 0.0036 0.6838 +- 0.0039   9997.0 +- 0.0
            weighted avg 0.7345 +- 0.0121 0.6575 +- 0.0043 0.6185 +- 0.009   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6495 +- 0.0031
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6572 +- 0.0045
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6555 +- 0.0044
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6542 +- 0.0043
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6453 +- 0.0036


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6748 +- 0.0042
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6839 +- 0.004
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.683 +- 0.0039
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6813 +- 0.0042
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6693 +- 0.0042


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.6878 +- 0.0199

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9447 +- 0.0093 0.9979 +- 0.0011 0.9705 +- 0.0046   2125.0 +- 0.0
          CD16+ Monocyte 0.9896 +- 0.0041 0.8509 +- 0.0329 0.9147 +- 0.0183    489.0 +- 0.0
    CD1C+ dendritic cell 0.9854 +- 0.0414 0.621 +- 0.0457 0.7605 +- 0.0371    105.0 +- 0.0
       CD4 Memory T cell 0.3157 +- 0.0281 0.5956 +- 0.0558 0.411 +- 0.0249    754.0 +- 0.0
        CD4 Naive T cell 0.8358 +- 0.0267 0.4155 +- 0.0783 0.5504 +- 0.0627   1396.0 +- 0.0
       CD8 Memory T cell 0.1277 +- 0.0102 0.5878 +- 0.0657 0.2094 +- 0.0153    312.0 +- 0.0
        CD8 Naive T cell 0.9866 +- 0.0071 0.8403 +- 0.0316 0.9072 +- 0.0165   1105.0 +- 0.0
      Gamma-delta T cell 0.1092 +- 0.0677 0.0363 +- 0.0309 0.054 +- 0.0429    493.0 +- 0.0
                    MAIT 0.6134 +- 0.0365 0.4194 +- 0.1238 0.4889 +- 0.0873    217.0 +- 0.0
           Memory B cell 0.9623 +- 0.0409 0.1773 +- 0.0409 0.2976 +- 0.0582    277.0 +- 0.0
                 NK cell 0.9547 +- 0.0192 0.6852 +- 0.0749 0.7954 +- 0.0496   1363.0 +- 0.0
            Naive B cell 0.7316 +- 0.0106 0.9998 +- 0.0005 0.8449 +- 0.0071    618.0 +- 0.0
             Plasma cell 0.8475 +- 0.0582 0.9087 +- 0.0531 0.8757 +- 0.0431     46.0 +- 0.0
Plasmacytoid dendritic cell 0.9943 +- 0.0128 0.9961 +- 0.0083 0.9951 +- 0.0069     51.0 +- 0.0
       T regulatory cell  0.15 +- 0.3375 0.0012 +- 0.0026 0.0024 +- 0.0051    165.0 +- 0.0

                accuracy                                 0.6878 +- 0.0199   9516.0 +- 0.0
               macro avg 0.7032 +- 0.0189 0.6089 +- 0.0116 0.6052 +- 0.0107   9516.0 +- 0.0
            weighted avg  0.783 +- 0.006 0.6878 +- 0.0199 0.6987 +- 0.0172   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6861 +- 0.0207
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6878 +- 0.0198
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6742 +- 0.0196
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6615 +- 0.0203
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6537 +- 0.0195


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.5981 +- 0.0099
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6052 +- 0.0106
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.5887 +- 0.0104
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.5825 +- 0.0108
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.5701 +- 0.0101


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



