# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8628 +- 0.0004

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9937 +- 0.0003 0.9957 +- 0.0002 0.9947 +- 0.0002   3456.0 +- 0.0
          CD16+ Monocyte 0.9785 +- 0.0016 0.9703 +- 0.0025 0.9744 +- 0.0017    192.0 +- 0.0
    CD1C+ dendritic cell 0.9259 +- 0.0082 0.8778 +- 0.0073 0.9011 +- 0.0018    108.0 +- 0.0
       CD4 Memory T cell 0.924 +- 0.0011 0.809 +- 0.0036 0.8627 +- 0.0022   2890.0 +- 0.0
        CD4 Naive T cell 0.8656 +- 0.0022 0.9073 +- 0.0017 0.886 +- 0.0012   3439.0 +- 0.0
       CD8 Memory T cell 0.3061 +- 0.0011 0.7476 +- 0.0031 0.4343 +- 0.0014    818.0 +- 0.0
        CD8 Naive T cell 0.8857 +- 0.0018 0.8587 +- 0.0016 0.872 +- 0.0011   2063.0 +- 0.0
      Gamma-delta T cell 0.9445 +- 0.0012 0.7103 +- 0.003 0.8109 +- 0.0019   2545.0 +- 0.0
                    MAIT 0.7439 +- 0.0028 0.8662 +- 0.0027 0.8004 +- 0.0015    975.0 +- 0.0
           Memory B cell 0.8728 +- 0.003 0.9417 +- 0.0013 0.9059 +- 0.0019    897.0 +- 0.0
                 NK cell 0.9709 +- 0.001 0.8043 +- 0.0014 0.8798 +- 0.0008   2582.0 +- 0.0
            Naive B cell 0.9768 +- 0.0005 0.9433 +- 0.0017 0.9598 +- 0.001   2232.0 +- 0.0
             Plasma cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     56.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.6544 +- 0.0085 0.7911 +- 0.0062     57.0 +- 0.0
       T regulatory cell 0.2026 +- 0.0102 0.2279 +- 0.013 0.2145 +- 0.0113    136.0 +- 0.0

                accuracy                                 0.8628 +- 0.0004  22446.0 +- 0.0
               macro avg 0.8394 +- 0.001 0.821 +- 0.0008 0.8192 +- 0.0008  22446.0 +- 0.0
            weighted avg 0.8993 +- 0.0004 0.8628 +- 0.0004 0.874 +- 0.0004  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8434 +- 0.0067
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8625 +- 0.0004
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8474 +- 0.0005
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8479 +- 0.0007
Feature importance dropout (2.0% features dropped) Accuracy score: 0.7967 +- 0.0006


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8018 +- 0.0048
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.819 +- 0.0008
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8078 +- 0.001
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8055 +- 0.0007
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.7611 +- 0.001



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.7171 +- 0.0007

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9912 +- 0.0006 0.9782 +- 0.0004 0.9847 +- 0.0003    775.0 +- 0.0
          CD16+ Monocyte 0.9413 +- 0.0002 0.9851 +- 0.0042 0.9627 +- 0.0021    114.0 +- 0.0
    CD1C+ dendritic cell 0.8729 +- 0.0036   0.9315 +- 0.0 0.9013 +- 0.0019     73.0 +- 0.0
       CD4 Memory T cell 0.6702 +- 0.0263 0.0228 +- 0.0019 0.044 +- 0.0036   1098.0 +- 0.0
        CD4 Naive T cell 0.8204 +- 0.0044 0.9524 +- 0.0025 0.8815 +- 0.0016   3173.0 +- 0.0
       CD8 Memory T cell 0.0136 +- 0.0013 0.0092 +- 0.001 0.011 +- 0.0012    823.0 +- 0.0
        CD8 Naive T cell 0.954 +- 0.0019 0.8863 +- 0.0034 0.9189 +- 0.0015   1349.0 +- 0.0
      Gamma-delta T cell 0.1007 +- 0.0018 0.252 +- 0.0051 0.1439 +- 0.0027    325.0 +- 0.0
                    MAIT 0.2746 +- 0.0033   0.9948 +- 0.0 0.4303 +- 0.004    191.0 +- 0.0
           Memory B cell 0.9543 +- 0.002 0.7269 +- 0.0072 0.8252 +- 0.0041    353.0 +- 0.0
                 NK cell 0.9797 +- 0.0017 0.9348 +- 0.0023 0.9567 +- 0.001    876.0 +- 0.0
            Naive B cell 0.841 +- 0.0034 0.9838 +- 0.0013 0.9068 +- 0.0016    513.0 +- 0.0
             Plasma cell 0.9849 +- 0.0001 0.9329 +- 0.0069 0.9582 +- 0.0037     70.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0   0.9787 +- 0.0   0.9892 +- 0.0     47.0 +- 0.0
       T regulatory cell 0.0446 +- 0.0027 0.0365 +- 0.0034 0.0401 +- 0.0031    203.0 +- 0.0

                accuracy                                 0.7171 +- 0.0007   9983.0 +- 0.0
               macro avg 0.6962 +- 0.0019 0.7071 +- 0.0009 0.6636 +- 0.0007   9983.0 +- 0.0
            weighted avg 0.7426 +- 0.0022 0.7171 +- 0.0007 0.6889 +- 0.0007   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7018 +- 0.0106
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.7171 +- 0.0007
Feature importance dropout (0.5% features dropped) Accuracy score: 0.7025 +- 0.0007
Feature importance dropout (1.0% features dropped) Accuracy score: 0.7018 +- 0.0007
Feature importance dropout (2.0% features dropped) Accuracy score: 0.62 +- 0.0007


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.655 +- 0.0059
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6641 +- 0.0006
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6591 +- 0.0008
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6582 +- 0.0007
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6164 +- 0.0008


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.6593 +- 0.0007

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9939 +- 0.0004 0.9964 +- 0.0003 0.9952 +- 0.0003   1466.0 +- 0.0
          CD16+ Monocyte 0.9902 +- 0.002 0.9827 +- 0.0013 0.9864 +- 0.0011    237.0 +- 0.0
    CD1C+ dendritic cell  0.954 +- 0.005 0.9489 +- 0.0045 0.9515 +- 0.0039     94.0 +- 0.0
       CD4 Memory T cell 0.7643 +- 0.0121 0.0245 +- 0.0007 0.0475 +- 0.0014   1916.0 +- 0.0
        CD4 Naive T cell   0.8 +- 0.0036 0.9428 +- 0.0022 0.8655 +- 0.0014   2232.0 +- 0.0
       CD8 Memory T cell 0.0132 +- 0.0007 0.0206 +- 0.0012 0.0161 +- 0.0008    786.0 +- 0.0
        CD8 Naive T cell 0.9167 +- 0.0022 0.9133 +- 0.0021 0.915 +- 0.0014    686.0 +- 0.0
      Gamma-delta T cell 0.1865 +- 0.0012 0.409 +- 0.0042 0.2562 +- 0.0019    354.0 +- 0.0
                    MAIT 0.3539 +- 0.0012 0.9651 +- 0.0026 0.5179 +- 0.0013    315.0 +- 0.0
           Memory B cell 0.9741 +- 0.0013 0.7711 +- 0.0051 0.8608 +- 0.0034    474.0 +- 0.0
                 NK cell 0.9901 +- 0.0005 0.9711 +- 0.0013 0.9805 +- 0.0007    629.0 +- 0.0
            Naive B cell 0.8181 +- 0.0033   0.9879 +- 0.0  0.895 +- 0.002    494.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9075 +- 0.0121 0.9515 +- 0.0066     40.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0 0.975 +- 0.0093 0.9873 +- 0.0048     52.0 +- 0.0
       T regulatory cell 0.0507 +- 0.0029 0.0655 +- 0.0031 0.0571 +- 0.003    223.0 +- 0.0

                accuracy                                 0.6593 +- 0.0007   9998.0 +- 0.0
               macro avg 0.7204 +- 0.0009 0.7254 +- 0.001 0.6856 +- 0.0007   9998.0 +- 0.0
            weighted avg 0.7442 +- 0.0027 0.6593 +- 0.0007 0.627 +- 0.0005   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6537 +- 0.0035
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6597 +- 0.0007
Feature importance dropout (0.5% features dropped) Accuracy score: 0.656 +- 0.0005
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6564 +- 0.0004
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6231 +- 0.0007


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6771 +- 0.0022
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6863 +- 0.0007
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.685 +- 0.0005
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6836 +- 0.0006
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6515 +- 0.0014


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.661 +- 0.0008

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9889 +- 0.0007 0.9942 +- 0.0002 0.9915 +- 0.0003   2024.0 +- 0.0
          CD16+ Monocyte 0.9926 +- 0.0011 0.9668 +- 0.0041 0.9796 +- 0.0021    389.0 +- 0.0
    CD1C+ dendritic cell 0.9218 +- 0.0041 0.9098 +- 0.0026 0.9157 +- 0.0028    123.0 +- 0.0
       CD4 Memory T cell 0.8537 +- 0.0085 0.127 +- 0.0038 0.2211 +- 0.0057   2300.0 +- 0.0
        CD4 Naive T cell 0.608 +- 0.0068 0.9512 +- 0.0027 0.7418 +- 0.0044   1554.0 +- 0.0
       CD8 Memory T cell 0.0165 +- 0.0006 0.0189 +- 0.0009 0.0176 +- 0.0007    814.0 +- 0.0
        CD8 Naive T cell 0.7159 +- 0.0067 0.9011 +- 0.0068 0.7978 +- 0.0046    180.0 +- 0.0
      Gamma-delta T cell 0.1286 +- 0.0015 0.4022 +- 0.0056 0.1948 +- 0.0024    225.0 +- 0.0
                    MAIT 0.3236 +- 0.0019   0.9874 +- 0.0 0.4874 +- 0.0021    238.0 +- 0.0
           Memory B cell    0.986 +- 0.0 0.7783 +- 0.0018 0.8699 +- 0.0011    272.0 +- 0.0
                 NK cell 0.9675 +- 0.0012 0.9936 +- 0.0006 0.9804 +- 0.0005   1040.0 +- 0.0
            Naive B cell 0.8886 +- 0.0008   0.9939 +- 0.0 0.9383 +- 0.0004    492.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.995 +- 0.0105 0.9975 +- 0.0053     40.0 +- 0.0
Plasmacytoid dendritic cell   0.9778 +- 0.0      1.0 +- 0.0   0.9888 +- 0.0     44.0 +- 0.0
       T regulatory cell 0.0962 +- 0.0069 0.0656 +- 0.0064 0.078 +- 0.0067    262.0 +- 0.0

                accuracy                                 0.661 +- 0.0008   9997.0 +- 0.0
               macro avg 0.6977 +- 0.0009 0.739 +- 0.0011  0.68 +- 0.0009   9997.0 +- 0.0
            weighted avg 0.748 +- 0.0013 0.661 +- 0.0008 0.6303 +- 0.0017   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6587 +- 0.0028
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6603 +- 0.0008
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6602 +- 0.0008
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6591 +- 0.0008
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6554 +- 0.001


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.674 +- 0.0031
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6804 +- 0.0008
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.68 +- 0.0006
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6791 +- 0.0006
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6566 +- 0.0016


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.7267 +- 0.0044

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9648 +- 0.0006 0.9963 +- 0.0001 0.9803 +- 0.0003   2125.0 +- 0.0
          CD16+ Monocyte 0.9826 +- 0.0007 0.9102 +- 0.0028 0.945 +- 0.0015    489.0 +- 0.0
    CD1C+ dendritic cell      1.0 +- 0.0  0.761 +- 0.003 0.8642 +- 0.002    105.0 +- 0.0
       CD4 Memory T cell 0.3917 +- 0.0049 0.4345 +- 0.0056 0.4119 +- 0.0031    754.0 +- 0.0
        CD4 Naive T cell 0.8497 +- 0.0032 0.6742 +- 0.0144 0.7517 +- 0.0083   1396.0 +- 0.0
       CD8 Memory T cell 0.1326 +- 0.0016 0.5862 +- 0.0197 0.2163 +- 0.0032    312.0 +- 0.0
        CD8 Naive T cell 0.9341 +- 0.0052 0.8613 +- 0.003 0.8962 +- 0.0024   1105.0 +- 0.0
      Gamma-delta T cell 0.2343 +- 0.016 0.0647 +- 0.0091 0.1013 +- 0.0126    493.0 +- 0.0
                    MAIT 0.4031 +- 0.0079 0.3364 +- 0.0081 0.3667 +- 0.007    217.0 +- 0.0
           Memory B cell 0.9112 +- 0.0082 0.1996 +- 0.0246 0.3269 +- 0.0328    277.0 +- 0.0
                 NK cell 0.9005 +- 0.0023 0.7326 +- 0.0161 0.8079 +- 0.0104   1363.0 +- 0.0
            Naive B cell 0.7359 +- 0.0067 0.9927 +- 0.0016 0.8452 +- 0.0039    618.0 +- 0.0
             Plasma cell 0.9759 +- 0.0065 0.9652 +- 0.0183 0.9704 +- 0.0093     46.0 +- 0.0
Plasmacytoid dendritic cell      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0     51.0 +- 0.0
       T regulatory cell 0.0664 +- 0.0035   0.0121 +- 0.0 0.0205 +- 0.0002    165.0 +- 0.0

                accuracy                                 0.7267 +- 0.0044   9516.0 +- 0.0
               macro avg 0.6989 +- 0.0016 0.6351 +- 0.0032 0.6336 +- 0.0044   9516.0 +- 0.0
            weighted avg 0.7813 +- 0.002 0.7267 +- 0.0044 0.7352 +- 0.0046   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.7288 +- 0.0079
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.7265 +- 0.0045
Feature importance dropout (0.5% features dropped) Accuracy score: 0.7133 +- 0.0049
Feature importance dropout (1.0% features dropped) Accuracy score: 0.7009 +- 0.0053
Feature importance dropout (2.0% features dropped) Accuracy score: 0.6885 +- 0.0042


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.6316 +- 0.0078
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.6339 +- 0.0048
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.6262 +- 0.0053
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.6219 +- 0.0058
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.6085 +- 0.0049


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



