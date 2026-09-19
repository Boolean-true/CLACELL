# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8314 +- 0.0

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte   0.9991 +- 0.0   0.9829 +- 0.0    0.991 +- 0.0   3456.0 +- 0.0
          CD16+ Monocyte   0.9543 +- 0.0   0.9792 +- 0.0   0.9666 +- 0.0    192.0 +- 0.0
    CD1C+ dendritic cell   0.6543 +- 0.0   0.9815 +- 0.0   0.7852 +- 0.0    108.0 +- 0.0
       CD4 Memory T cell   0.9238 +- 0.0   0.9401 +- 0.0   0.9319 +- 0.0   2890.0 +- 0.0
        CD4 Naive T cell   0.9291 +- 0.0   0.8427 +- 0.0   0.8838 +- 0.0   3439.0 +- 0.0
       CD8 Memory T cell   0.0042 +- 0.0   0.0073 +- 0.0   0.0053 +- 0.0    818.0 +- 0.0
        CD8 Naive T cell   0.8271 +- 0.0   0.8861 +- 0.0   0.8556 +- 0.0   2063.0 +- 0.0
      Gamma-delta T cell   0.9433 +- 0.0   0.4644 +- 0.0   0.6224 +- 0.0   2545.0 +- 0.0
                    MAIT   0.7953 +- 0.0   0.8687 +- 0.0   0.8304 +- 0.0    975.0 +- 0.0
           Memory B cell   0.8951 +- 0.0   0.9509 +- 0.0   0.9222 +- 0.0    897.0 +- 0.0
                 NK cell   0.9476 +- 0.0   0.9028 +- 0.0   0.9246 +- 0.0   2582.0 +- 0.0
            Naive B cell   0.9798 +- 0.0   0.9552 +- 0.0   0.9673 +- 0.0   2232.0 +- 0.0
             Plasma cell   0.9825 +- 0.0      1.0 +- 0.0   0.9912 +- 0.0     56.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0   0.6842 +- 0.0   0.8125 +- 0.0     57.0 +- 0.0
       T regulatory cell   0.0828 +- 0.0   0.5956 +- 0.0   0.1454 +- 0.0    136.0 +- 0.0

                accuracy                                   0.8314 +- 0.0  22446.0 +- 0.0
               macro avg   0.7946 +- 0.0   0.8028 +- 0.0   0.7757 +- 0.0  22446.0 +- 0.0
            weighted avg   0.8918 +- 0.0   0.8314 +- 0.0   0.8503 +- 0.0  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.827 +- 0.0032
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8312 +- 0.0
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8207 +- 0.0
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8197 +- 0.0
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7934 +- 0.0


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.7719 +- 0.0016
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.7757 +- 0.0
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.7707 +- 0.0
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.7696 +- 0.0
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.7495 +- 0.0



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.7335 +- 0.0

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte   0.9973 +- 0.0   0.9613 +- 0.0    0.979 +- 0.0    775.0 +- 0.0
          CD16+ Monocyte   0.9417 +- 0.0   0.9912 +- 0.0   0.9658 +- 0.0    114.0 +- 0.0
    CD1C+ dendritic cell   0.7579 +- 0.0   0.9863 +- 0.0   0.8571 +- 0.0     73.0 +- 0.0
       CD4 Memory T cell   0.6078 +- 0.0   0.0282 +- 0.0    0.054 +- 0.0   1098.0 +- 0.0
        CD4 Naive T cell   0.8998 +- 0.0   0.8944 +- 0.0   0.8971 +- 0.0   3173.0 +- 0.0
       CD8 Memory T cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    823.0 +- 0.0
        CD8 Naive T cell   0.8849 +- 0.0     0.98 +- 0.0     0.93 +- 0.0   1349.0 +- 0.0
      Gamma-delta T cell    0.147 +- 0.0   0.3723 +- 0.0   0.2108 +- 0.0    325.0 +- 0.0
                    MAIT   0.3047 +- 0.0   0.9843 +- 0.0   0.4653 +- 0.0    191.0 +- 0.0
           Memory B cell   0.9628 +- 0.0   0.8074 +- 0.0   0.8783 +- 0.0    353.0 +- 0.0
                 NK cell   0.9666 +- 0.0   0.9897 +- 0.0    0.978 +- 0.0    876.0 +- 0.0
            Naive B cell   0.8827 +- 0.0   0.9825 +- 0.0   0.9299 +- 0.0    513.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     47.0 +- 0.0
       T regulatory cell   0.1222 +- 0.0    0.601 +- 0.0   0.2032 +- 0.0    203.0 +- 0.0

                accuracy                                   0.7335 +- 0.0   9983.0 +- 0.0
               macro avg   0.6974 +- 0.0     0.77 +- 0.0   0.6885 +- 0.0   9983.0 +- 0.0
            weighted avg   0.7551 +- 0.0   0.7335 +- 0.0   0.7062 +- 0.0   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7274 +- 0.0015
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.7334 +- 0.0
Feature importance dropout (0.5% features dropped) Accuracy score: 0.7315 +- 0.0
Feature importance dropout (1.0% features dropped) Accuracy score: 0.731 +- 0.0
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7215 +- 0.0


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.685 +- 0.001
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6883 +- 0.0
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6882 +- 0.0
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6873 +- 0.0
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6838 +- 0.0


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.6712 +- 0.0

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte   0.9986 +- 0.0   0.9789 +- 0.0   0.9886 +- 0.0   1466.0 +- 0.0
          CD16+ Monocyte   0.9791 +- 0.0   0.9873 +- 0.0   0.9832 +- 0.0    237.0 +- 0.0
    CD1C+ dendritic cell   0.7642 +- 0.0      1.0 +- 0.0   0.8664 +- 0.0     94.0 +- 0.0
       CD4 Memory T cell   0.5652 +- 0.0   0.0136 +- 0.0   0.0265 +- 0.0   1916.0 +- 0.0
        CD4 Naive T cell   0.8689 +- 0.0   0.9059 +- 0.0    0.887 +- 0.0   2232.0 +- 0.0
       CD8 Memory T cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    786.0 +- 0.0
        CD8 Naive T cell   0.8835 +- 0.0    0.984 +- 0.0    0.931 +- 0.0    686.0 +- 0.0
      Gamma-delta T cell   0.2301 +- 0.0   0.4972 +- 0.0   0.3146 +- 0.0    354.0 +- 0.0
                    MAIT   0.3373 +- 0.0   0.9841 +- 0.0   0.5024 +- 0.0    315.0 +- 0.0
           Memory B cell   0.9665 +- 0.0   0.7911 +- 0.0   0.8701 +- 0.0    474.0 +- 0.0
                 NK cell   0.9751 +- 0.0   0.9968 +- 0.0   0.9858 +- 0.0    629.0 +- 0.0
            Naive B cell   0.8308 +- 0.0   0.9838 +- 0.0   0.9008 +- 0.0    494.0 +- 0.0
             Plasma cell      1.0 +- 0.0    0.875 +- 0.0   0.9333 +- 0.0     40.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0   0.9615 +- 0.0   0.9804 +- 0.0     52.0 +- 0.0
       T regulatory cell    0.099 +- 0.0   0.7444 +- 0.0   0.1748 +- 0.0    223.0 +- 0.0

                accuracy                                   0.6712 +- 0.0   9998.0 +- 0.0
               macro avg   0.6999 +- 0.0   0.7802 +- 0.0   0.6897 +- 0.0   9998.0 +- 0.0
            weighted avg   0.7181 +- 0.0   0.6712 +- 0.0   0.6309 +- 0.0   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6658 +- 0.0009
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.671 +- 0.0
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6704 +- 0.0
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6695 +- 0.0
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6663 +- 0.0


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6868 +- 0.0013
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6894 +- 0.0
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.69 +- 0.0
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6893 +- 0.0
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6864 +- 0.0


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.658 +- 0.0

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte    0.999 +- 0.0   0.9822 +- 0.0   0.9905 +- 0.0   2024.0 +- 0.0
          CD16+ Monocyte   0.9773 +- 0.0   0.9949 +- 0.0    0.986 +- 0.0    389.0 +- 0.0
    CD1C+ dendritic cell   0.8067 +- 0.0   0.9837 +- 0.0   0.8864 +- 0.0    123.0 +- 0.0
       CD4 Memory T cell   0.7603 +- 0.0     0.04 +- 0.0    0.076 +- 0.0   2300.0 +- 0.0
        CD4 Naive T cell   0.7391 +- 0.0   0.8951 +- 0.0   0.8097 +- 0.0   1554.0 +- 0.0
       CD8 Memory T cell      0.4 +- 0.0   0.0025 +- 0.0   0.0049 +- 0.0    814.0 +- 0.0
        CD8 Naive T cell   0.7783 +- 0.0   0.9556 +- 0.0   0.8579 +- 0.0    180.0 +- 0.0
      Gamma-delta T cell   0.1769 +- 0.0      0.6 +- 0.0   0.2733 +- 0.0    225.0 +- 0.0
                    MAIT   0.3528 +- 0.0   0.9916 +- 0.0   0.5204 +- 0.0    238.0 +- 0.0
           Memory B cell   0.9872 +- 0.0   0.8493 +- 0.0    0.913 +- 0.0    272.0 +- 0.0
                 NK cell   0.9728 +- 0.0   0.9962 +- 0.0   0.9843 +- 0.0   1040.0 +- 0.0
            Naive B cell   0.9226 +- 0.0   0.9939 +- 0.0   0.9569 +- 0.0    492.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     44.0 +- 0.0
       T regulatory cell   0.1134 +- 0.0   0.8168 +- 0.0   0.1992 +- 0.0    262.0 +- 0.0

                accuracy                                    0.658 +- 0.0   9997.0 +- 0.0
               macro avg   0.7324 +- 0.0   0.8068 +- 0.0   0.6972 +- 0.0   9997.0 +- 0.0
            weighted avg   0.7838 +- 0.0    0.658 +- 0.0   0.6155 +- 0.0   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6552 +- 0.0015
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6579 +- 0.0
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6579 +- 0.0
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6581 +- 0.0
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6575 +- 0.0


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6921 +- 0.0015
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6968 +- 0.0
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6972 +- 0.0
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.698 +- 0.0
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6909 +- 0.0


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.7883 +- 0.0

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte   0.9768 +- 0.0   0.9915 +- 0.0   0.9841 +- 0.0   2125.0 +- 0.0
          CD16+ Monocyte   0.9649 +- 0.0   0.9571 +- 0.0    0.961 +- 0.0    489.0 +- 0.0
    CD1C+ dendritic cell   0.9651 +- 0.0   0.7905 +- 0.0   0.8691 +- 0.0    105.0 +- 0.0
       CD4 Memory T cell   0.3259 +- 0.0   0.3103 +- 0.0   0.3179 +- 0.0    754.0 +- 0.0
        CD4 Naive T cell   0.9391 +- 0.0   0.5745 +- 0.0   0.7129 +- 0.0   1396.0 +- 0.0
       CD8 Memory T cell   0.1277 +- 0.0   0.0192 +- 0.0   0.0334 +- 0.0    312.0 +- 0.0
        CD8 Naive T cell    0.914 +- 0.0    0.981 +- 0.0   0.9463 +- 0.0   1105.0 +- 0.0
      Gamma-delta T cell   0.3099 +- 0.0    0.286 +- 0.0   0.2975 +- 0.0    493.0 +- 0.0
                    MAIT   0.4921 +- 0.0      1.0 +- 0.0   0.6596 +- 0.0    217.0 +- 0.0
           Memory B cell   0.9912 +- 0.0   0.8159 +- 0.0    0.895 +- 0.0    277.0 +- 0.0
                 NK cell   0.8411 +- 0.0    0.967 +- 0.0   0.8997 +- 0.0   1363.0 +- 0.0
            Naive B cell   0.9237 +- 0.0   0.9984 +- 0.0   0.9596 +- 0.0    618.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     46.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0   0.9804 +- 0.0   0.9901 +- 0.0     51.0 +- 0.0
       T regulatory cell   0.1932 +- 0.0   0.6182 +- 0.0   0.2944 +- 0.0    165.0 +- 0.0

                accuracy                                   0.7883 +- 0.0   9516.0 +- 0.0
               macro avg    0.731 +- 0.0   0.7527 +- 0.0   0.7214 +- 0.0   9516.0 +- 0.0
            weighted avg   0.8024 +- 0.0   0.7883 +- 0.0   0.7824 +- 0.0   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7836 +- 0.0034
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.7886 +- 0.0
Feature importance dropout (0.5% features dropped) Accuracy score: 0.7875 +- 0.0
Feature importance dropout (1.0% features dropped) Accuracy score: 0.7871 +- 0.0
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7827 +- 0.0


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.7169 +- 0.0019
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.7216 +- 0.0
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.7219 +- 0.0
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.7225 +- 0.0
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.7189 +- 0.0


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



