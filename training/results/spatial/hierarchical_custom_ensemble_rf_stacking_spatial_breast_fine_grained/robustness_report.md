# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.6135 +- 0.0035

### Classification Report 

                               precision          recall        f1-score         support

                   B_ACB 0.3292 +- 0.0087 0.5004 +- 0.0476 0.3966 +- 0.0209    832.0 +- 0.0
                  B_Cell   0.1 +- 0.3162 0.0001 +- 0.0005 0.0003 +- 0.0009    697.0 +- 0.0
                   B_GCB      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    451.0 +- 0.0
                  B_IFIT 0.3691 +- 0.0101 0.4704 +- 0.0126 0.4136 +- 0.0098    673.0 +- 0.0
                 B_Naive 0.641 +- 0.1486 0.1018 +- 0.0981 0.1463 +- 0.0981    379.0 +- 0.0
            CAFs (CA12+)      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      6.0 +- 0.0
         CAFs (COL11A1+) 0.743 +- 0.0101 0.5207 +- 0.0095 0.6122 +- 0.0077    343.0 +- 0.0
             CAFs (DPT+) 0.8368 +- 0.0093 0.6002 +- 0.0083 0.6989 +- 0.0051    511.0 +- 0.0
            CAFs (LAMP5) 0.6974 +- 0.0076 0.7825 +- 0.0041 0.7375 +- 0.0046   1072.0 +- 0.0
            CAFs (PI16+) 0.5753 +- 0.0056 0.6672 +- 0.0127 0.6178 +- 0.0083    952.0 +- 0.0
               CD4_Naive 0.4785 +- 0.0391 0.2952 +- 0.0741 0.3564 +- 0.0492   3062.0 +- 0.0
                 CD4_Tem 0.1663 +- 0.0093 0.0878 +- 0.0305 0.112 +- 0.0279   1396.0 +- 0.0
                 CD4_Tfh  0.374 +- 0.011 0.6749 +- 0.1061 0.4777 +- 0.0224    953.0 +- 0.0
                  CD4_Th      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      3.0 +- 0.0
                CD4_Treg 0.5699 +- 0.0082 0.5761 +- 0.0099 0.5728 +- 0.0032   2219.0 +- 0.0
                 CD8_Isg 0.2229 +- 0.0222 0.5016 +- 0.0373 0.3069 +- 0.0154   1561.0 +- 0.0
                 CD8_Tem 0.347 +- 0.0146 0.5425 +- 0.0294 0.4224 +- 0.0034   3705.0 +- 0.0
                 CD8_Tex 0.4629 +- 0.039 0.2532 +- 0.0316 0.3272 +- 0.0357   1683.0 +- 0.0
             Endo Arter. 0.8343 +- 0.0128 0.6348 +- 0.0117 0.7209 +- 0.0092    141.0 +- 0.0
             Endo Capil. 0.5067 +- 0.0176 0.4432 +- 0.0226 0.4727 +- 0.019    169.0 +- 0.0
               Endo Imm. 0.6957 +- 0.0067 0.692 +- 0.0098 0.6938 +- 0.0075    553.0 +- 0.0
             Endo Lymph.  0.9215 +- 0.03 0.2208 +- 0.0314 0.3553 +- 0.0415     48.0 +- 0.0
               Endo Ven. 0.6196 +- 0.0082 0.6798 +- 0.0081 0.6483 +- 0.0077    441.0 +- 0.0
         Epithelial cell 0.9196 +- 0.004 0.9453 +- 0.0014 0.9323 +- 0.0015  13395.0 +- 0.0
                Mac/Mono 0.5265 +- 0.0091 0.3518 +- 0.0068 0.4217 +- 0.0053    629.0 +- 0.0
               Mac_Anti. 0.8914 +- 0.0054 0.7919 +- 0.0035 0.8387 +- 0.0026   1041.0 +- 0.0
                  Mac_ES 0.4861 +- 0.0946 0.0837 +- 0.012 0.1426 +- 0.0206     43.0 +- 0.0
                 Mac_IFN 0.4521 +- 0.007 0.6455 +- 0.0064 0.5318 +- 0.006    743.0 +- 0.0
                  Mac_LA 0.427 +- 0.0069 0.1939 +- 0.0058 0.2667 +- 0.0065    543.0 +- 0.0
             Mac_RTM_IFN 0.5351 +- 0.0056 0.5032 +- 0.0099 0.5186 +- 0.006    884.0 +- 0.0
              Mac_RTM_LA 0.2517 +- 0.0046 0.4969 +- 0.0062 0.3342 +- 0.0052    351.0 +- 0.0
              Mac_RTM_MT 0.3689 +- 0.0057 0.3594 +- 0.0089 0.364 +- 0.0054    192.0 +- 0.0
                    Mast 0.8064 +- 0.1122 0.0259 +- 0.007 0.0501 +- 0.013    139.0 +- 0.0
           Myofibroblast 0.7136 +- 0.0618 0.103 +- 0.0116 0.1798 +- 0.0187    168.0 +- 0.0
                      NK 0.5281 +- 0.0183 0.2216 +- 0.0181 0.3116 +- 0.0173   1082.0 +- 0.0
                NK_Cyto. 0.5751 +- 0.0256 0.1791 +- 0.0128 0.2728 +- 0.0153    253.0 +- 0.0
                  NK_rNK 0.3128 +- 0.0619 0.0254 +- 0.0056 0.0467 +- 0.0096    433.0 +- 0.0
               PCs (ECM) 0.6472 +- 0.0087 0.8064 +- 0.0065 0.7181 +- 0.0072    264.0 +- 0.0
              Plasma_IgG 0.9419 +- 0.0056 0.7706 +- 0.011 0.8476 +- 0.0056    989.0 +- 0.0
          Prolif Stromal 0.7228 +- 0.0602 0.3526 +- 0.0254 0.4735 +- 0.0325     19.0 +- 0.0
               T_Prolif. 0.7341 +- 0.0313 0.6954 +- 0.0066 0.7139 +- 0.0137    699.0 +- 0.0
                    VSMC 0.6729 +- 0.0088 0.7245 +- 0.0132 0.6977 +- 0.0095    322.0 +- 0.0
                    cDC1 0.7565 +- 0.0202 0.5493 +- 0.0185 0.6361 +- 0.0123    142.0 +- 0.0
                    cDC2 0.7262 +- 0.0043 0.7135 +- 0.0042 0.7198 +- 0.0027   2582.0 +- 0.0
                     mDC 0.8078 +- 0.0072 0.5969 +- 0.0196 0.6863 +- 0.0129    354.0 +- 0.0
                     pDC 0.9206 +- 0.0175 0.702 +- 0.0127 0.7965 +- 0.0122    201.0 +- 0.0

                accuracy                                 0.6135 +- 0.0035  47318.0 +- 0.0
               macro avg 0.5482 +- 0.0088 0.4366 +- 0.004 0.4476 +- 0.0038  47318.0 +- 0.0
            weighted avg 0.6262 +- 0.0067 0.6135 +- 0.0035 0.6011 +- 0.0042  47318.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.6015 +- 0.0044
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.6121 +- 0.0036
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6058 +- 0.0034
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6036 +- 0.003
Feature importance dropout (2.0% features dropped) Accuracy score: 0.5981 +- 0.0026


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.4256 +- 0.0034
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.4471 +- 0.0039
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.4335 +- 0.0028
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.4316 +- 0.003
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.4243 +- 0.0028



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



