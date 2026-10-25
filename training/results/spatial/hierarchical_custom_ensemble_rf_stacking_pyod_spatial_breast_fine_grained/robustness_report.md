# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.0073 +- 0.0038

### Classification Report 

                               precision          recall        f1-score         support

                   B_ACB      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    832.0 +- 0.0
                  B_Cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    697.0 +- 0.0
                   B_GCB      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    451.0 +- 0.0
                  B_IFIT      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    673.0 +- 0.0
                 B_Naive      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    379.0 +- 0.0
            CAFs (CA12+)      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      6.0 +- 0.0
         CAFs (COL11A1+)      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    343.0 +- 0.0
             CAFs (DPT+) 0.1467 +- 0.3108 0.0012 +- 0.0026 0.0023 +- 0.0052    511.0 +- 0.0
            CAFs (LAMP5) 0.4733 +- 0.214 0.0036 +- 0.0019 0.0072 +- 0.0038   1072.0 +- 0.0
            CAFs (PI16+) 0.1333 +- 0.2194 0.0003 +- 0.0005 0.0006 +- 0.001    952.0 +- 0.0
               CD4_Naive      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   3062.0 +- 0.0
                 CD4_Tem      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   1396.0 +- 0.0
                 CD4_Tfh      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    953.0 +- 0.0
                  CD4_Th      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      3.0 +- 0.0
                CD4_Treg      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   2219.0 +- 0.0
                 CD8_Isg      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   1561.0 +- 0.0
                 CD8_Tem      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   3705.0 +- 0.0
                 CD8_Tex      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   1683.0 +- 0.0
             Endo Arter. 0.8912 +- 0.099 0.0553 +- 0.0366 0.1022 +- 0.0646    141.0 +- 0.0
             Endo Capil.   0.1 +- 0.3162 0.0006 +- 0.0019 0.0012 +- 0.0037    169.0 +- 0.0
               Endo Imm. 0.1413 +- 0.1649 0.0049 +- 0.0064 0.0094 +- 0.0124    553.0 +- 0.0
             Endo Lymph.   0.2 +- 0.4216 0.0125 +- 0.0281 0.0234 +- 0.0523     48.0 +- 0.0
               Endo Ven.  0.15 +- 0.1995 0.0009 +- 0.0012 0.0018 +- 0.0023    441.0 +- 0.0
         Epithelial cell 0.9682 +- 0.0247 0.021 +- 0.0145 0.0408 +- 0.0273  13395.0 +- 0.0
                Mac/Mono      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    629.0 +- 0.0
               Mac_Anti. 0.0929 +- 0.2936 0.0012 +- 0.0039 0.0025 +- 0.0078   1041.0 +- 0.0
                  Mac_ES      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0     43.0 +- 0.0
                 Mac_IFN      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    743.0 +- 0.0
                  Mac_LA      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    543.0 +- 0.0
             Mac_RTM_IFN      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    884.0 +- 0.0
              Mac_RTM_LA      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    351.0 +- 0.0
              Mac_RTM_MT      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    192.0 +- 0.0
                    Mast      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    139.0 +- 0.0
           Myofibroblast   0.2 +- 0.4216 0.0018 +- 0.004 0.0035 +- 0.0079    168.0 +- 0.0
                      NK      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   1082.0 +- 0.0
                NK_Cyto.    0.3 +- 0.483 0.0012 +- 0.0019 0.0024 +- 0.0038    253.0 +- 0.0
                  NK_rNK      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    433.0 +- 0.0
               PCs (ECM) 0.2956 +- 0.1878 0.0068 +- 0.0064 0.0133 +- 0.0123    264.0 +- 0.0
              Plasma_IgG 0.922 +- 0.0829 0.0421 +- 0.0505 0.0767 +- 0.0872    989.0 +- 0.0
          Prolif Stromal 0.1833 +- 0.2415 0.0211 +- 0.0272 0.0377 +- 0.0486     19.0 +- 0.0
                Rejected      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0
               T_Prolif.    0.3 +- 0.483 0.0006 +- 0.001 0.0011 +- 0.002    699.0 +- 0.0
                    VSMC   0.1 +- 0.3162 0.0003 +- 0.001 0.0006 +- 0.002    322.0 +- 0.0
                    cDC1      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    142.0 +- 0.0
                    cDC2  0.15 +- 0.3187 0.0001 +- 0.0002 0.0002 +- 0.0004   2582.0 +- 0.0
                     mDC   0.1 +- 0.3162 0.0003 +- 0.0009 0.0006 +- 0.0018    354.0 +- 0.0
                     pDC      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    201.0 +- 0.0

                accuracy                                 0.0073 +- 0.0038  47318.0 +- 0.0
               macro avg 0.1244 +- 0.0275 0.0037 +- 0.0019 0.007 +- 0.0034  47318.0 +- 0.0
            weighted avg 0.3347 +- 0.0245 0.0073 +- 0.0038 0.014 +- 0.0072  47318.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.0042 +- 0.0019
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.0073 +- 0.0038
Feature importance dropout (0.5% features dropped) Accuracy score: 0.0073 +- 0.0039
Feature importance dropout (1.0% features dropped) Accuracy score: 0.0071 +- 0.0039
Feature importance dropout (2.0% features dropped) Accuracy score: 0.0067 +- 0.0037


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.0056 +- 0.0034
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.007 +- 0.0034
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.0068 +- 0.0035
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.0066 +- 0.0034
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.0063 +- 0.0037



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



