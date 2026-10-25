# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.4239 +- 0.0169

### Classification Report 

                               precision          recall        f1-score         support

                   B_ACB 0.393 +- 0.0213 0.1258 +- 0.0324 0.1883 +- 0.0323    832.0 +- 0.0
                  B_Cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    697.0 +- 0.0
                   B_GCB      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    451.0 +- 0.0
                  B_IFIT 0.4051 +- 0.0267  0.234 +- 0.013 0.296 +- 0.0108    673.0 +- 0.0
                 B_Naive 0.5589 +- 0.2285 0.1731 +- 0.122 0.2149 +- 0.1347    379.0 +- 0.0
            CAFs (CA12+)      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      6.0 +- 0.0
         CAFs (COL11A1+) 0.9437 +- 0.021 0.1449 +- 0.0078 0.2511 +- 0.0116    343.0 +- 0.0
             CAFs (DPT+) 0.9497 +- 0.006 0.392 +- 0.0191 0.5547 +- 0.0193    511.0 +- 0.0
            CAFs (LAMP5) 0.7839 +- 0.018 0.4364 +- 0.0223 0.5601 +- 0.0135   1072.0 +- 0.0
            CAFs (PI16+) 0.7545 +- 0.0194 0.2317 +- 0.0373 0.353 +- 0.0408    952.0 +- 0.0
               CD4_Naive 0.5877 +- 0.0561 0.1151 +- 0.0566 0.1844 +- 0.0764   3062.0 +- 0.0
                 CD4_Tem 0.3712 +- 0.2503 0.0176 +- 0.0178 0.0303 +- 0.0302   1396.0 +- 0.0
                 CD4_Tfh 0.4438 +- 0.0489 0.4342 +- 0.1777 0.4123 +- 0.0732    953.0 +- 0.0
                  CD4_Th      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      3.0 +- 0.0
                CD4_Treg 0.7615 +- 0.0398 0.411 +- 0.0359 0.5317 +- 0.0214   2219.0 +- 0.0
                 CD8_Isg 0.3803 +- 0.0181 0.2248 +- 0.0784 0.2733 +- 0.0582   1561.0 +- 0.0
                 CD8_Tem 0.4656 +- 0.0214 0.2685 +- 0.0658 0.3346 +- 0.048   3705.0 +- 0.0
                 CD8_Tex 0.5101 +- 0.0263 0.1817 +- 0.0298  0.2661 +- 0.03   1683.0 +- 0.0
             Endo Arter. 0.9397 +- 0.016 0.3085 +- 0.019 0.4642 +- 0.022    141.0 +- 0.0
             Endo Capil. 0.6704 +- 0.0813 0.0598 +- 0.0098 0.1095 +- 0.0167    169.0 +- 0.0
               Endo Imm. 0.8512 +- 0.0113 0.3099 +- 0.0069 0.4544 +- 0.0076    553.0 +- 0.0
             Endo Lymph.      1.0 +- 0.0 0.0938 +- 0.0147 0.1711 +- 0.025     48.0 +- 0.0
               Endo Ven. 0.8105 +- 0.0101 0.2868 +- 0.0089 0.4236 +- 0.0098    441.0 +- 0.0
         Epithelial cell  0.967 +- 0.002 0.896 +- 0.0031 0.9302 +- 0.0013  13395.0 +- 0.0
                Mac/Mono 0.8997 +- 0.0226 0.0591 +- 0.0031 0.111 +- 0.0053    629.0 +- 0.0
               Mac_Anti. 0.9761 +- 0.0018 0.6343 +- 0.0046 0.7689 +- 0.0031   1041.0 +- 0.0
                  Mac_ES      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0     43.0 +- 0.0
                 Mac_IFN 0.7271 +- 0.015 0.2421 +- 0.0359 0.3618 +- 0.0356    743.0 +- 0.0
                  Mac_LA 0.7098 +- 0.0817 0.0099 +- 0.0016 0.0196 +- 0.003    543.0 +- 0.0
             Mac_RTM_IFN   0.9 +- 0.3162 0.0019 +- 0.0009 0.0038 +- 0.0019    884.0 +- 0.0
              Mac_RTM_LA 0.6733 +- 0.2392 0.0037 +- 0.0014 0.0074 +- 0.0027    351.0 +- 0.0
              Mac_RTM_MT      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    192.0 +- 0.0
                    Mast      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    139.0 +- 0.0
           Myofibroblast      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    168.0 +- 0.0
                      NK 0.6775 +- 0.0382 0.1243 +- 0.0175 0.2091 +- 0.0224   1082.0 +- 0.0
                NK_Cyto.  0.675 +- 0.074 0.047 +- 0.0187 0.0871 +- 0.0326    253.0 +- 0.0
                  NK_rNK 0.4079 +- 0.3677 0.003 +- 0.0019 0.0059 +- 0.0037    433.0 +- 0.0
               PCs (ECM) 0.8181 +- 0.0162  0.547 +- 0.028 0.655 +- 0.0158    264.0 +- 0.0
              Plasma_IgG 0.9807 +- 0.0037 0.636 +- 0.0119 0.7715 +- 0.0079    989.0 +- 0.0
          Prolif Stromal 0.7333 +- 0.1405   0.1053 +- 0.0 0.1835 +- 0.0037     19.0 +- 0.0
                Rejected      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0
               T_Prolif. 0.8294 +- 0.0203 0.6147 +- 0.0093 0.7059 +- 0.0056    699.0 +- 0.0
                    VSMC 0.877 +- 0.0183 0.4621 +- 0.0256 0.6047 +- 0.0205    322.0 +- 0.0
                    cDC1 0.9098 +- 0.0252 0.1697 +- 0.0146 0.2858 +- 0.0208    142.0 +- 0.0
                    cDC2 0.8535 +- 0.0056 0.1864 +- 0.0119 0.3058 +- 0.0155   2582.0 +- 0.0
                     mDC 0.9449 +- 0.0115  0.25 +- 0.0116 0.3952 +- 0.0139    354.0 +- 0.0
                     pDC 0.9939 +- 0.0052 0.4861 +- 0.0161 0.6527 +- 0.0145    201.0 +- 0.0

                accuracy                                 0.4239 +- 0.0169  47318.0 +- 0.0
               macro avg 0.5986 +- 0.0182 0.2112 +- 0.0074 0.2795 +- 0.0048  47318.0 +- 0.0
            weighted avg 0.7272 +- 0.0151 0.4239 +- 0.0169 0.4895 +- 0.0134  47318.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.3999 +- 0.0189
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.4221 +- 0.0167
Feature importance dropout (0.5% features dropped) Accuracy score: 0.4166 +- 0.0168
Feature importance dropout (1.0% features dropped) Accuracy score: 0.4134 +- 0.0162
Feature importance dropout (2.0% features dropped) Accuracy score: 0.4071 +- 0.0162


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.2463 +- 0.0075
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.2788 +- 0.0048
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.2669 +- 0.0049
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.2649 +- 0.0047
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.2568 +- 0.0046



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



