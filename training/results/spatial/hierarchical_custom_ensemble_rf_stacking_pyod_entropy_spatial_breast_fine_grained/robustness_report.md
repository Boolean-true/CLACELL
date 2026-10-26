# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.4395 +- 0.0105

### Classification Report 

                               precision          recall        f1-score         support

                   B_ACB 0.3741 +- 0.0155 0.2978 +- 0.0573 0.3291 +- 0.0387    832.0 +- 0.0
                  B_Cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    697.0 +- 0.0
                   B_GCB      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    451.0 +- 0.0
                  B_IFIT 0.3903 +- 0.0203 0.2611 +- 0.0119 0.3124 +- 0.0078    673.0 +- 0.0
                 B_Naive 0.5842 +- 0.1678 0.0533 +- 0.0553 0.0866 +- 0.0807    379.0 +- 0.0
            CAFs (CA12+)      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      6.0 +- 0.0
         CAFs (COL11A1+) 0.9259 +- 0.0155 0.1236 +- 0.016 0.2178 +- 0.0244    343.0 +- 0.0
             CAFs (DPT+) 0.9522 +- 0.0076 0.4031 +- 0.0221 0.5661 +- 0.0207    511.0 +- 0.0
            CAFs (LAMP5) 0.7797 +- 0.0167 0.4641 +- 0.0319 0.581 +- 0.0213   1072.0 +- 0.0
            CAFs (PI16+) 0.7538 +- 0.015 0.2861 +- 0.045 0.4128 +- 0.0436    952.0 +- 0.0
               CD4_Naive 0.5538 +- 0.0348 0.1986 +- 0.0491 0.2876 +- 0.0449   3062.0 +- 0.0
                 CD4_Tem 0.2152 +- 0.0402 0.041 +- 0.0274 0.0631 +- 0.0322   1396.0 +- 0.0
                 CD4_Tfh  0.424 +- 0.025 0.3443 +- 0.1471 0.3626 +- 0.0689    953.0 +- 0.0
                  CD4_Th      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      3.0 +- 0.0
                CD4_Treg 0.7245 +- 0.0454 0.4169 +- 0.0272 0.5275 +- 0.011   2219.0 +- 0.0
                 CD8_Isg 0.2628 +- 0.0189 0.3238 +- 0.0347 0.2899 +- 0.0248   1561.0 +- 0.0
                 CD8_Tem 0.4097 +- 0.0075 0.3639 +- 0.0209 0.3851 +- 0.0123   3705.0 +- 0.0
                 CD8_Tex 0.6312 +- 0.0258 0.1838 +- 0.0131 0.2844 +- 0.0158   1683.0 +- 0.0
             Endo Arter.  0.94 +- 0.0279 0.2957 +- 0.0164 0.4496 +- 0.019    141.0 +- 0.0
             Endo Capil. 0.5861 +- 0.079 0.0515 +- 0.0122 0.0945 +- 0.0215    169.0 +- 0.0
               Endo Imm. 0.8445 +- 0.0104 0.3278 +- 0.0103 0.4722 +- 0.0113    553.0 +- 0.0
             Endo Lymph.      1.0 +- 0.0 0.0583 +- 0.0237 0.1094 +- 0.0419     48.0 +- 0.0
               Endo Ven. 0.802 +- 0.0096 0.2939 +- 0.0106  0.43 +- 0.0119    441.0 +- 0.0
         Epithelial cell 0.9727 +- 0.0017 0.8984 +- 0.0032 0.934 +- 0.0015  13395.0 +- 0.0
                Mac/Mono 0.8935 +- 0.0211 0.0682 +- 0.0048 0.1267 +- 0.0084    629.0 +- 0.0
               Mac_Anti. 0.9791 +- 0.0021 0.6212 +- 0.0037 0.7601 +- 0.0029   1041.0 +- 0.0
                  Mac_ES      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0     43.0 +- 0.0
                 Mac_IFN 0.6788 +- 0.0121 0.1938 +- 0.0107 0.3014 +- 0.013    743.0 +- 0.0
                  Mac_LA 0.6328 +- 0.0727 0.0099 +- 0.001 0.0196 +- 0.0019    543.0 +- 0.0
             Mac_RTM_IFN 0.7381 +- 0.2019 0.0035 +- 0.001  0.007 +- 0.002    884.0 +- 0.0
              Mac_RTM_LA 0.5112 +- 0.1174 0.0063 +- 0.0022 0.0124 +- 0.0044    351.0 +- 0.0
              Mac_RTM_MT  0.15 +- 0.3375 0.001 +- 0.0022 0.0021 +- 0.0044    192.0 +- 0.0
                    Mast      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    139.0 +- 0.0
           Myofibroblast      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    168.0 +- 0.0
                      NK 0.7145 +- 0.0565 0.0457 +- 0.0118 0.0855 +- 0.0203   1082.0 +- 0.0
                NK_Cyto. 0.6132 +- 0.1061 0.0225 +- 0.0136 0.0431 +- 0.0249    253.0 +- 0.0
                  NK_rNK  0.05 +- 0.1581 0.0002 +- 0.0007 0.0005 +- 0.0015    433.0 +- 0.0
               PCs (ECM) 0.8047 +- 0.0141 0.561 +- 0.0285 0.6607 +- 0.0194    264.0 +- 0.0
              Plasma_IgG 0.9777 +- 0.0022 0.6152 +- 0.0143 0.7551 +- 0.0109    989.0 +- 0.0
          Prolif Stromal      1.0 +- 0.0   0.1053 +- 0.0   0.1905 +- 0.0     19.0 +- 0.0
                Rejected      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0
               T_Prolif. 0.8333 +- 0.0219 0.5721 +- 0.0127 0.6781 +- 0.0066    699.0 +- 0.0
                    VSMC 0.8727 +- 0.0239 0.4422 +- 0.0308 0.586 +- 0.0232    322.0 +- 0.0
                    cDC1 0.896 +- 0.0315 0.1563 +- 0.0148 0.2659 +- 0.0216    142.0 +- 0.0
                    cDC2 0.8843 +- 0.007 0.1741 +- 0.005 0.2909 +- 0.0067   2582.0 +- 0.0
                     mDC 0.9515 +- 0.0136 0.2311 +- 0.015 0.3716 +- 0.019    354.0 +- 0.0
                     pDC      1.0 +- 0.0 0.4925 +- 0.0174 0.6598 +- 0.0156    201.0 +- 0.0

                accuracy                                 0.4395 +- 0.0105  47318.0 +- 0.0
               macro avg 0.581 +- 0.0116  0.213 +- 0.007 0.2769 +- 0.0053  47318.0 +- 0.0
            weighted avg 0.7086 +- 0.0079 0.4395 +- 0.0105 0.4997 +- 0.0071  47318.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.418 +- 0.0092
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.4378 +- 0.0106
Feature importance dropout (0.5% features dropped) Accuracy score: 0.4339 +- 0.0105
Feature importance dropout (1.0% features dropped) Accuracy score: 0.4312 +- 0.01
Feature importance dropout (2.0% features dropped) Accuracy score: 0.4268 +- 0.01


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.2449 +- 0.0057
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.2762 +- 0.0054
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.2673 +- 0.0045
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.2657 +- 0.0044
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.2602 +- 0.0045



## Out of data distribution 

### OOD Dataset: All 

Baseline accuracy score: N/A

### Classification Report 

                               precision          recall        f1-score         support

                   B_ACB             N/A             N/A             N/A             N/A
                  B_Cell             N/A             N/A             N/A             N/A
                   B_GCB             N/A             N/A             N/A             N/A
                  B_IFIT             N/A             N/A             N/A             N/A
                 B_Naive             N/A             N/A             N/A             N/A
            CAFs (CA12+)             N/A             N/A             N/A             N/A
         CAFs (COL11A1+)             N/A             N/A             N/A             N/A
             CAFs (DPT+)             N/A             N/A             N/A             N/A
            CAFs (LAMP5)             N/A             N/A             N/A             N/A
            CAFs (PI16+)             N/A             N/A             N/A             N/A
               CD4_Naive             N/A             N/A             N/A             N/A
                 CD4_Tem             N/A             N/A             N/A             N/A
                 CD4_Tfh             N/A             N/A             N/A             N/A
                  CD4_Th             N/A             N/A             N/A             N/A
                CD4_Treg             N/A             N/A             N/A             N/A
                 CD8_Isg             N/A             N/A             N/A             N/A
                 CD8_Tem             N/A             N/A             N/A             N/A
                 CD8_Tex             N/A             N/A             N/A             N/A
             Endo Arter.             N/A             N/A             N/A             N/A
             Endo Capil.             N/A             N/A             N/A             N/A
               Endo Imm.             N/A             N/A             N/A             N/A
             Endo Lymph.             N/A             N/A             N/A             N/A
               Endo Ven.             N/A             N/A             N/A             N/A
         Epithelial cell             N/A             N/A             N/A             N/A
                Mac/Mono             N/A             N/A             N/A             N/A
               Mac_Anti.             N/A             N/A             N/A             N/A
                  Mac_ES             N/A             N/A             N/A             N/A
                 Mac_IFN             N/A             N/A             N/A             N/A
                  Mac_LA             N/A             N/A             N/A             N/A
             Mac_RTM_IFN             N/A             N/A             N/A             N/A
              Mac_RTM_LA             N/A             N/A             N/A             N/A
              Mac_RTM_MT             N/A             N/A             N/A             N/A
                    Mast             N/A             N/A             N/A             N/A
           Myofibroblast             N/A             N/A             N/A             N/A
                      NK             N/A             N/A             N/A             N/A
                NK_Cyto.             N/A             N/A             N/A             N/A
                  NK_rNK             N/A             N/A             N/A             N/A
               PCs (ECM)             N/A             N/A             N/A             N/A
              Plasma_IgG             N/A             N/A             N/A             N/A
          Prolif Stromal             N/A             N/A             N/A             N/A
                Rejected             N/A             N/A             N/A             N/A
               T_Prolif.             N/A             N/A             N/A             N/A
                    VSMC             N/A             N/A             N/A             N/A
                    cDC1             N/A             N/A             N/A             N/A
                    cDC2             N/A             N/A             N/A             N/A
                     mDC             N/A             N/A             N/A             N/A
                     pDC             N/A             N/A             N/A             N/A

                accuracy                                             N/A             N/A
               macro avg             N/A             N/A             N/A             N/A
            weighted avg             N/A             N/A             N/A             N/A

### Further Robustness Evaluation with metric: Accuracy 



### Further Robustness Evaluation with metric: Macro_F1 



