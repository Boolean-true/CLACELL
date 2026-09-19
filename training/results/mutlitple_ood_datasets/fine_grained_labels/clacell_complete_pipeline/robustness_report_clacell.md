# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8645 +- 0.0028

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9908 +- 0.0007 0.9974 +- 0.0002 0.9941 +- 0.0004   3456.0 +- 0.0
          CD16+ Monocyte 0.9841 +- 0.0001 0.9661 +- 0.0037 0.975 +- 0.0019    192.0 +- 0.0
    CD1C+ dendritic cell 0.941 +- 0.0063 0.8852 +- 0.0065 0.9122 +- 0.0052    108.0 +- 0.0
       CD4 Memory T cell 0.955 +- 0.0014  0.871 +- 0.012 0.911 +- 0.0064   2890.0 +- 0.0
        CD4 Naive T cell 0.8504 +- 0.0061 0.9576 +- 0.0013 0.9008 +- 0.0037   3439.0 +- 0.0
       CD8 Memory T cell 0.2617 +- 0.004 0.7435 +- 0.0045 0.3871 +- 0.0045    818.0 +- 0.0
        CD8 Naive T cell 0.9254 +- 0.0035 0.8559 +- 0.0088 0.8893 +- 0.0061   2063.0 +- 0.0
      Gamma-delta T cell 0.9643 +- 0.0015 0.6257 +- 0.0103 0.7589 +- 0.0078   2545.0 +- 0.0
                    MAIT 0.7942 +- 0.0043 0.8714 +- 0.0044 0.831 +- 0.0026    975.0 +- 0.0
           Memory B cell 0.8992 +- 0.0033 0.963 +- 0.0031  0.93 +- 0.0022    897.0 +- 0.0
                 NK cell 0.9882 +- 0.0011 0.7539 +- 0.0029 0.8553 +- 0.002   2582.0 +- 0.0
            Naive B cell 0.9847 +- 0.0013 0.9561 +- 0.0017 0.9702 +- 0.001   2232.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9679 +- 0.0075 0.9837 +- 0.0039     56.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0   0.6842 +- 0.0   0.8125 +- 0.0     57.0 +- 0.0
       T regulatory cell 0.5703 +- 0.0342 0.1007 +- 0.007 0.1711 +- 0.0103    136.0 +- 0.0

                accuracy                                 0.8645 +- 0.0028  22446.0 +- 0.0
               macro avg 0.874 +- 0.0029 0.8133 +- 0.0018 0.8188 +- 0.0017  22446.0 +- 0.0
            weighted avg 0.9132 +- 0.0015 0.8645 +- 0.0028 0.8767 +- 0.0025  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8399 +- 0.0069
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8644 +- 0.0029
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8489 +- 0.0021
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8493 +- 0.0019
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8052 +- 0.0048


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.7964 +- 0.004
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8188 +- 0.0017
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.808 +- 0.001
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8057 +- 0.0008
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.7653 +- 0.0049



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.7175 +- 0.002

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9875 +- 0.0015 0.9819 +- 0.0009 0.9847 +- 0.0008    775.0 +- 0.0
          CD16+ Monocyte 0.9475 +- 0.0081 0.9807 +- 0.0055 0.9638 +- 0.0035    114.0 +- 0.0
    CD1C+ dendritic cell 0.8706 +- 0.0034 0.9123 +- 0.0071 0.891 +- 0.0035     73.0 +- 0.0
       CD4 Memory T cell   0.1 +- 0.3162 0.0002 +- 0.0006 0.0004 +- 0.0011   1098.0 +- 0.0
        CD4 Naive T cell 0.7877 +- 0.0099 0.9759 +- 0.0028 0.8717 +- 0.0052   3173.0 +- 0.0
       CD8 Memory T cell 0.032 +- 0.0027 0.0254 +- 0.0023 0.0283 +- 0.0023    823.0 +- 0.0
        CD8 Naive T cell 0.9625 +- 0.0009 0.8624 +- 0.0144 0.9097 +- 0.0082   1349.0 +- 0.0
      Gamma-delta T cell  0.09 +- 0.0036 0.2274 +- 0.0116 0.1289 +- 0.0055    325.0 +- 0.0
                    MAIT 0.3027 +- 0.011 0.9958 +- 0.0022 0.4642 +- 0.0128    191.0 +- 0.0
           Memory B cell 0.9637 +- 0.0015 0.781 +- 0.0082 0.8628 +- 0.0048    353.0 +- 0.0
                 NK cell 0.9942 +- 0.0017 0.895 +- 0.0122 0.9419 +- 0.0064    876.0 +- 0.0
            Naive B cell 0.8689 +- 0.0043 0.9856 +- 0.001 0.9236 +- 0.0022    513.0 +- 0.0
             Plasma cell   0.9855 +- 0.0   0.9714 +- 0.0   0.9784 +- 0.0     70.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.9596 +- 0.0067 0.9794 +- 0.0035     47.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    203.0 +- 0.0

                accuracy                                 0.7175 +- 0.002   9983.0 +- 0.0
               macro avg 0.6595 +- 0.021 0.7036 +- 0.0014 0.6619 +- 0.0011   9983.0 +- 0.0
            weighted avg 0.6742 +- 0.0349 0.7175 +- 0.002 0.6815 +- 0.0019   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7068 +- 0.0025
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.7175 +- 0.002
Feature importance dropout (0.5% features dropped) Accuracy score: 0.7024 +- 0.0025
Feature importance dropout (1.0% features dropped) Accuracy score: 0.7011 +- 0.0026
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6804 +- 0.0035


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6559 +- 0.0021
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.662 +- 0.0011
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.658 +- 0.0013
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6581 +- 0.0015
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6495 +- 0.0018


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.6662 +- 0.0008

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9921 +- 0.0007 0.995 +- 0.0006 0.9935 +- 0.0002   1466.0 +- 0.0
          CD16+ Monocyte 0.9801 +- 0.002 0.9755 +- 0.0018 0.9778 +- 0.0011    237.0 +- 0.0
    CD1C+ dendritic cell 0.9389 +- 0.0047 0.9309 +- 0.0056 0.9348 +- 0.0023     94.0 +- 0.0
       CD4 Memory T cell   0.15 +- 0.254 0.0004 +- 0.0007 0.0007 +- 0.0014   1916.0 +- 0.0
        CD4 Naive T cell 0.7361 +- 0.0053 0.983 +- 0.0017 0.8418 +- 0.0032   2232.0 +- 0.0
       CD8 Memory T cell 0.0577 +- 0.0048 0.101 +- 0.0104 0.0734 +- 0.0066    786.0 +- 0.0
        CD8 Naive T cell 0.9305 +- 0.0021 0.9061 +- 0.0112 0.9181 +- 0.0061    686.0 +- 0.0
      Gamma-delta T cell 0.1636 +- 0.003 0.3251 +- 0.0062 0.2177 +- 0.0038    354.0 +- 0.0
                    MAIT 0.3933 +- 0.0131 0.986 +- 0.0031 0.5622 +- 0.0132    315.0 +- 0.0
           Memory B cell 0.9739 +- 0.0008 0.7947 +- 0.0055 0.8752 +- 0.0035    474.0 +- 0.0
                 NK cell 0.9893 +- 0.0008 0.9703 +- 0.0023 0.9797 +- 0.001    629.0 +- 0.0
            Naive B cell 0.8332 +- 0.0038 0.9836 +- 0.0006 0.9022 +- 0.0023    494.0 +- 0.0
             Plasma cell      1.0 +- 0.0     0.95 +- 0.0   0.9744 +- 0.0     40.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0   0.9615 +- 0.0   0.9804 +- 0.0     52.0 +- 0.0
       T regulatory cell 0.1043 +- 0.0913 0.0027 +- 0.0023 0.0052 +- 0.0045    223.0 +- 0.0

                accuracy                                 0.6662 +- 0.0008   9998.0 +- 0.0
               macro avg 0.6829 +- 0.0208 0.7244 +- 0.0008 0.6825 +- 0.0011   9998.0 +- 0.0
            weighted avg 0.6183 +- 0.0505 0.6662 +- 0.0008 0.6167 +- 0.0012   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6608 +- 0.0025
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6662 +- 0.0008
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6637 +- 0.0009
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6646 +- 0.0012
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6589 +- 0.0017


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6753 +- 0.003
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6826 +- 0.001
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6833 +- 0.0015
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6839 +- 0.0021
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6806 +- 0.0024


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.6509 +- 0.003

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9901 +- 0.0004 0.9944 +- 0.0005 0.9923 +- 0.0002   2024.0 +- 0.0
          CD16+ Monocyte 0.9878 +- 0.0017 0.9756 +- 0.0014 0.9816 +- 0.001    389.0 +- 0.0
    CD1C+ dendritic cell 0.9408 +- 0.0022 0.9171 +- 0.0051 0.9288 +- 0.0022    123.0 +- 0.0
       CD4 Memory T cell 0.903 +- 0.0102 0.0473 +- 0.0146 0.0895 +- 0.026   2300.0 +- 0.0
        CD4 Naive T cell 0.5882 +- 0.022 0.9837 +- 0.0027 0.7359 +- 0.0166   1554.0 +- 0.0
       CD8 Memory T cell 0.0399 +- 0.0027 0.0629 +- 0.0053 0.0488 +- 0.0033    814.0 +- 0.0
        CD8 Naive T cell 0.8426 +- 0.0157 0.8794 +- 0.0105 0.8606 +- 0.0122    180.0 +- 0.0
      Gamma-delta T cell 0.1261 +- 0.0072 0.3973 +- 0.0303 0.1914 +- 0.0118    225.0 +- 0.0
                    MAIT 0.3555 +- 0.0117      1.0 +- 0.0 0.5244 +- 0.0126    238.0 +- 0.0
           Memory B cell 0.9892 +- 0.0022  0.843 +- 0.009 0.9103 +- 0.0047    272.0 +- 0.0
                 NK cell 0.9893 +- 0.0029 0.9858 +- 0.002 0.9875 +- 0.0011   1040.0 +- 0.0
            Naive B cell 0.9181 +- 0.0042 0.9949 +- 0.0011 0.9549 +- 0.002    492.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     40.0 +- 0.0
Plasmacytoid dendritic cell   0.9778 +- 0.0      1.0 +- 0.0   0.9888 +- 0.0     44.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    262.0 +- 0.0

                accuracy                                 0.6509 +- 0.003   9997.0 +- 0.0
               macro avg 0.7099 +- 0.0022 0.7388 +- 0.0014 0.6797 +- 0.0016   9997.0 +- 0.0
            weighted avg 0.7627 +- 0.0053 0.6509 +- 0.003 0.6046 +- 0.0072   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6445 +- 0.0036
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6505 +- 0.0029
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6524 +- 0.0032
Feature importance dropout (1.0% features dropped) Accuracy score: 0.65 +- 0.0035
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6468 +- 0.0038


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6705 +- 0.0026
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6796 +- 0.0015
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6828 +- 0.0023
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.682 +- 0.0027
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6763 +- 0.0036


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.7686 +- 0.0052

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9784 +- 0.0018 0.9927 +- 0.0022 0.9855 +- 0.0004   2125.0 +- 0.0
          CD16+ Monocyte 0.9638 +- 0.0077 0.9599 +- 0.0068 0.9618 +- 0.0013    489.0 +- 0.0
    CD1C+ dendritic cell 0.9954 +- 0.0097 0.8038 +- 0.008 0.8894 +- 0.005    105.0 +- 0.0
       CD4 Memory T cell 0.8352 +- 0.0293 0.0865 +- 0.0361 0.1544 +- 0.0571    754.0 +- 0.0
        CD4 Naive T cell 0.7618 +- 0.0101 0.9922 +- 0.0052 0.8618 +- 0.0046   1396.0 +- 0.0
       CD8 Memory T cell 0.1099 +- 0.0047 0.5186 +- 0.0242 0.1813 +- 0.0077    312.0 +- 0.0
        CD8 Naive T cell 0.9969 +- 0.0008 0.9207 +- 0.0058 0.9573 +- 0.003   1105.0 +- 0.0
      Gamma-delta T cell 0.0538 +- 0.0123 0.0193 +- 0.0047 0.0284 +- 0.0068    493.0 +- 0.0
                    MAIT 0.5973 +- 0.0092 0.7548 +- 0.0302 0.6666 +- 0.0138    217.0 +- 0.0
           Memory B cell 0.9862 +- 0.0024 0.6697 +- 0.0345 0.7972 +- 0.0238    277.0 +- 0.0
                 NK cell 0.9977 +- 0.001 0.6961 +- 0.0252 0.8198 +- 0.0173   1363.0 +- 0.0
            Naive B cell 0.8709 +- 0.0119 0.9974 +- 0.0008 0.9298 +- 0.0065    618.0 +- 0.0
             Plasma cell 0.9369 +- 0.0059      1.0 +- 0.0 0.9674 +- 0.0032     46.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     51.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    165.0 +- 0.0

                accuracy                                 0.7686 +- 0.0052   9516.0 +- 0.0
               macro avg 0.7389 +- 0.0019 0.6941 +- 0.005  0.68 +- 0.0055   9516.0 +- 0.0
            weighted avg 0.8308 +- 0.002 0.7686 +- 0.0052 0.7628 +- 0.0067   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7511 +- 0.0113
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.7685 +- 0.0052
Feature importance dropout (0.5% features dropped) Accuracy score: 0.759 +- 0.0067
Feature importance dropout (1.0% features dropped) Accuracy score: 0.7373 +- 0.0071
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7305 +- 0.007


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6636 +- 0.0087
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.68 +- 0.0055
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6741 +- 0.0063
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6665 +- 0.0067
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6602 +- 0.0068


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



