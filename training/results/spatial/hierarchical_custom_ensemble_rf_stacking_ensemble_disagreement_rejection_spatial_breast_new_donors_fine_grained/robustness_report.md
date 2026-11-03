# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.5685 +- 0.0042

### Classification Report 

                               precision          recall        f1-score         support

                   B_ACB 0.3339 +- 0.0103 0.3953 +- 0.0555 0.3609 +- 0.0286    769.0 +- 0.0
                  B_Cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    675.0 +- 0.0
                   B_GCB      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    438.0 +- 0.0
                  B_IFIT 0.398 +- 0.0121 0.4042 +- 0.0175 0.4007 +- 0.0084    674.0 +- 0.0
                 B_Naive 0.4945 +- 0.3692 0.0279 +- 0.0276 0.0515 +- 0.0504    351.0 +- 0.0
            CAFs (CA12+)      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      6.0 +- 0.0
         CAFs (COL11A1+) 0.6175 +- 0.013 0.4985 +- 0.0212 0.5515 +- 0.0164    340.0 +- 0.0
             CAFs (DPT+) 0.852 +- 0.0076 0.5297 +- 0.0108 0.6532 +- 0.0076    556.0 +- 0.0
            CAFs (LAMP5) 0.7383 +- 0.0096 0.7185 +- 0.0091 0.7282 +- 0.0079   1110.0 +- 0.0
            CAFs (PI16+) 0.6492 +- 0.0101 0.6142 +- 0.0189 0.6311 +- 0.0123    948.0 +- 0.0
               CD4_Naive 0.5504 +- 0.0137 0.1433 +- 0.0158 0.2269 +- 0.0199   2672.0 +- 0.0
                 CD4_Tem 0.1474 +- 0.019 0.0327 +- 0.0078 0.0532 +- 0.0112   1472.0 +- 0.0
                 CD4_Tfh 0.3819 +- 0.0177 0.6979 +- 0.0275 0.493 +- 0.0107    947.0 +- 0.0
                  CD4_Th      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      7.0 +- 0.0
                CD4_Treg 0.4198 +- 0.0124 0.6716 +- 0.0289 0.5166 +- 0.017   2074.0 +- 0.0
                 CD8_Isg 0.1844 +- 0.007  0.518 +- 0.016 0.2719 +- 0.0079   1566.0 +- 0.0
                 CD8_Tem 0.294 +- 0.0052 0.4574 +- 0.0202 0.3577 +- 0.0061   2978.0 +- 0.0
                 CD8_Tex 0.4556 +- 0.0215 0.3309 +- 0.0341   0.383 +- 0.03   1792.0 +- 0.0
             Endo Arter. 0.8762 +- 0.0342 0.4448 +- 0.0383 0.5892 +- 0.0354    125.0 +- 0.0
             Endo Capil. 0.397 +- 0.0171 0.3236 +- 0.0218 0.3564 +- 0.0187    127.0 +- 0.0
               Endo Imm. 0.6516 +- 0.0137 0.4829 +- 0.019 0.5546 +- 0.0166    427.0 +- 0.0
             Endo Lymph.  0.51 +- 0.1432 0.2667 +- 0.0777 0.3473 +- 0.0948      9.0 +- 0.0
               Endo Ven. 0.6488 +- 0.0162 0.5481 +- 0.0302 0.5936 +- 0.018    418.0 +- 0.0
         Epithelial cell 0.9608 +- 0.0014 0.8948 +- 0.0095 0.9266 +- 0.0055  14999.0 +- 0.0
                Mac/Mono 0.4606 +- 0.0075 0.3527 +- 0.0104 0.3994 +- 0.0074    628.0 +- 0.0
               Mac_Anti. 0.8823 +- 0.0076 0.628 +- 0.0269 0.7335 +- 0.0187   1060.0 +- 0.0
                  Mac_ES      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0     59.0 +- 0.0
                 Mac_IFN 0.4532 +- 0.0082 0.596 +- 0.0191 0.5148 +- 0.0118    748.0 +- 0.0
                  Mac_LA 0.3989 +- 0.0162 0.1938 +- 0.0074 0.2608 +- 0.0089    562.0 +- 0.0
             Mac_RTM_IFN 0.4652 +- 0.0078 0.545 +- 0.0147 0.5019 +- 0.0096    901.0 +- 0.0
              Mac_RTM_LA 0.2413 +- 0.0089 0.3562 +- 0.0145 0.2876 +- 0.0096    333.0 +- 0.0
              Mac_RTM_MT 0.4142 +- 0.0311 0.2005 +- 0.0198 0.2698 +- 0.0224    216.0 +- 0.0
                    Mast 0.7148 +- 0.1886 0.0169 +- 0.0058 0.033 +- 0.0113    201.0 +- 0.0
           Myofibroblast 0.5093 +- 0.022 0.2428 +- 0.0151 0.3286 +- 0.0158    250.0 +- 0.0
                      NK 0.4645 +- 0.0193 0.2178 +- 0.0177 0.2959 +- 0.0151   1007.0 +- 0.0
                NK_Cyto. 0.6955 +- 0.0574 0.1414 +- 0.0297 0.2333 +- 0.041    263.0 +- 0.0
                  NK_rNK 0.2871 +- 0.0827 0.0221 +- 0.0084 0.0409 +- 0.0151    417.0 +- 0.0
               PCs (ECM) 0.6547 +- 0.0106 0.6853 +- 0.0172 0.6695 +- 0.0092    259.0 +- 0.0
              Plasma_IgG 0.8722 +- 0.0094 0.5439 +- 0.0226 0.6698 +- 0.0194    906.0 +- 0.0
          Prolif Stromal 0.7752 +- 0.0649   0.3 +- 0.0434 0.4309 +- 0.0488     17.0 +- 0.0
                Rejected      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0
               T_Prolif. 0.6581 +- 0.0128 0.5205 +- 0.0274 0.581 +- 0.0203    704.0 +- 0.0
                    VSMC 0.8041 +- 0.0148 0.4781 +- 0.0145 0.5995 +- 0.0131    561.0 +- 0.0
                    cDC1 0.8172 +- 0.0282 0.4309 +- 0.0238 0.5637 +- 0.0207    139.0 +- 0.0
                    cDC2 0.7426 +- 0.004 0.6228 +- 0.0126 0.6774 +- 0.0071   2606.0 +- 0.0
                     mDC   0.59 +- 0.031 0.1461 +- 0.0223 0.2338 +- 0.0305    356.0 +- 0.0
                     pDC 0.9237 +- 0.0231 0.5461 +- 0.0251 0.6862 +- 0.0239    204.0 +- 0.0

                accuracy                                 0.5685 +- 0.0042  47877.0 +- 0.0
               macro avg 0.4976 +- 0.0127 0.3572 +- 0.004 0.3842 +- 0.0038  47877.0 +- 0.0
            weighted avg  0.639 +- 0.004 0.5685 +- 0.0042 0.5777 +- 0.003  47877.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.5571 +- 0.0035
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.5684 +- 0.0041
Feature importance dropout (0.5% features dropped) Accuracy score: 0.5645 +- 0.0034
Feature importance dropout (1.0% features dropped) Accuracy score: 0.5676 +- 0.0039
Feature importance dropout (2.0% features dropped) Accuracy score: 0.5635 +- 0.0042


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.3642 +- 0.0037
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.3842 +- 0.0039
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.3749 +- 0.0034
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.3758 +- 0.0034
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.3708 +- 0.0037



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



