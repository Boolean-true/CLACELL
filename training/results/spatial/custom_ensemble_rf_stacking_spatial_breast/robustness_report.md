# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.4018 +- 0.0013

### Classification Report 

                               precision          recall        f1-score         support

                   B_ACB 0.3316 +- 0.0155 0.0474 +- 0.0122 0.0824 +- 0.019    832.0 +- 0.0
                  B_Cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    697.0 +- 0.0
                   B_GCB      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    451.0 +- 0.0
                  B_IFIT 0.2543 +- 0.0062 0.3171 +- 0.0187 0.2819 +- 0.0074    673.0 +- 0.0
                 B_Naive 0.3316 +- 0.0055 0.2335 +- 0.0203 0.2735 +- 0.0132    379.0 +- 0.0
            CAFs (CA12+)      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      6.0 +- 0.0
         CAFs (COL11A1+) 0.7403 +- 0.0076 0.4752 +- 0.0115 0.5788 +- 0.0087    343.0 +- 0.0
             CAFs (DPT+) 0.8256 +- 0.0066 0.5982 +- 0.0091 0.6937 +- 0.0063    511.0 +- 0.0
            CAFs (LAMP5) 0.659 +- 0.0055 0.7687 +- 0.0074 0.7096 +- 0.0043   1072.0 +- 0.0
            CAFs (PI16+) 0.5346 +- 0.0063 0.5909 +- 0.0125 0.5613 +- 0.0081    952.0 +- 0.0
               CD4_Naive      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   3062.0 +- 0.0
                 CD4_Tem      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   1396.0 +- 0.0
                 CD4_Tfh 0.3055 +- 0.0023 0.7678 +- 0.0106 0.437 +- 0.0012    953.0 +- 0.0
                  CD4_Th      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      3.0 +- 0.0
                CD4_Treg  0.5299 +- 0.01 0.2571 +- 0.0137 0.3461 +- 0.0136   2219.0 +- 0.0
                 CD8_Isg 0.0966 +- 0.0009 0.6779 +- 0.0081 0.1691 +- 0.0014   1561.0 +- 0.0
                 CD8_Tem 0.1816 +- 0.002 0.1587 +- 0.0042 0.1693 +- 0.0031   3705.0 +- 0.0
                 CD8_Tex 0.1458 +- 0.0231 0.0526 +- 0.007 0.0771 +- 0.0099   1683.0 +- 0.0
             Endo Arter. 0.7444 +- 0.0164 0.5532 +- 0.0167 0.6346 +- 0.0152    141.0 +- 0.0
             Endo Capil. 0.3586 +- 0.0094 0.3059 +- 0.0105 0.3301 +- 0.0086    169.0 +- 0.0
               Endo Imm. 0.6967 +- 0.007 0.6969 +- 0.0093 0.6968 +- 0.0061    553.0 +- 0.0
             Endo Lymph.      1.0 +- 0.0 0.0333 +- 0.0146 0.0642 +- 0.0271     48.0 +- 0.0
               Endo Ven. 0.5902 +- 0.0061 0.6755 +- 0.0066 0.6299 +- 0.0046    441.0 +- 0.0
                Mac/Mono 0.5209 +- 0.0138 0.2638 +- 0.0089 0.3501 +- 0.0097    629.0 +- 0.0
               Mac_Anti. 0.901 +- 0.0049 0.7513 +- 0.0058 0.8193 +- 0.0042   1041.0 +- 0.0
                  Mac_ES 0.5635 +- 0.0698    0.093 +- 0.0 0.1594 +- 0.0029     43.0 +- 0.0
                 Mac_IFN 0.4535 +- 0.0056 0.5976 +- 0.0065 0.5156 +- 0.005    743.0 +- 0.0
                  Mac_LA 0.4242 +- 0.0072 0.1983 +- 0.008 0.2702 +- 0.0084    543.0 +- 0.0
             Mac_RTM_IFN 0.5333 +- 0.0075 0.4788 +- 0.0075 0.5046 +- 0.0058    884.0 +- 0.0
              Mac_RTM_LA 0.2625 +- 0.008 0.461 +- 0.0137 0.3345 +- 0.0098    351.0 +- 0.0
              Mac_RTM_MT 0.3478 +- 0.0137 0.3406 +- 0.0165 0.3441 +- 0.0146    192.0 +- 0.0
                    Mast 0.9051 +- 0.0057 0.5763 +- 0.0093 0.7041 +- 0.0078    139.0 +- 0.0
           Myofibroblast 0.1376 +- 0.1338 0.0036 +- 0.0031 0.0069 +- 0.006    168.0 +- 0.0
                      NK 0.374 +- 0.0105 0.1103 +- 0.0105 0.1701 +- 0.0132   1082.0 +- 0.0
                NK_Cyto. 0.7575 +- 0.0674 0.0881 +- 0.0347 0.1549 +- 0.0535    253.0 +- 0.0
                  NK_rNK      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    433.0 +- 0.0
               PCs (ECM) 0.6426 +- 0.0047 0.792 +- 0.0045 0.7095 +- 0.0033    264.0 +- 0.0
              Plasma_IgG 0.8711 +- 0.0053 0.8118 +- 0.0036 0.8404 +- 0.0025    989.0 +- 0.0
          Prolif Stromal 0.8217 +- 0.2097 0.1053 +- 0.0555 0.182 +- 0.0856     19.0 +- 0.0
               T_Prolif. 0.6612 +- 0.0145 0.6464 +- 0.005 0.6536 +- 0.0077    699.0 +- 0.0
                    VSMC 0.6296 +- 0.0049 0.7991 +- 0.0062 0.7043 +- 0.0047    322.0 +- 0.0
                    cDC1 0.7542 +- 0.0208 0.4035 +- 0.0235 0.5254 +- 0.0213    142.0 +- 0.0
                    cDC2 0.7066 +- 0.0027 0.7201 +- 0.0047 0.7133 +- 0.0026   2582.0 +- 0.0
                   epi_0 0.3767 +- 0.0057 0.3939 +- 0.0099 0.3851 +- 0.0074   3407.0 +- 0.0
                   epi_1 0.4971 +- 0.0042 0.7004 +- 0.0073 0.5815 +- 0.0046   3647.0 +- 0.0
                  epi_13 0.5734 +- 0.0178 0.7798 +- 0.0081 0.6607 +- 0.011    243.0 +- 0.0
                  epi_14      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      2.0 +- 0.0
                  epi_15      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      5.0 +- 0.0
                  epi_18 0.9809 +- 0.0078 0.3354 +- 0.0344 0.499 +- 0.0375    243.0 +- 0.0
                   epi_2 0.5298 +- 0.0112 0.743 +- 0.0046 0.6184 +- 0.0068   3184.0 +- 0.0
                  epi_20      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      5.0 +- 0.0
                   epi_3    0.3 +- 0.483 0.0001 +- 0.0002 0.0002 +- 0.0004   2629.0 +- 0.0
                   epi_4      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      4.0 +- 0.0
                   epi_5      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0     13.0 +- 0.0
                   epi_6      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      1.0 +- 0.0
             epi_low_ent      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0     12.0 +- 0.0
                     mDC 0.7864 +- 0.0101 0.6904 +- 0.0126 0.7352 +- 0.0097    354.0 +- 0.0
                     pDC 0.8401 +- 0.0217 0.8463 +- 0.006 0.843 +- 0.0123    201.0 +- 0.0

                accuracy                                 0.4018 +- 0.0013  47318.0 +- 0.0
               macro avg  0.422 +- 0.012 0.3438 +- 0.0019  0.34 +- 0.0025  47318.0 +- 0.0
            weighted avg 0.4043 +- 0.0273 0.4018 +- 0.0013 0.3704 +- 0.0015  47318.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.3809 +- 0.0042
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.4018 +- 0.0013
Feature importance dropout (0.5% features dropped) Accuracy score: 0.3975 +- 0.0013
Feature importance dropout (1.0% features dropped) Accuracy score: 0.3927 +- 0.0011
Feature importance dropout (2.0% features dropped) Accuracy score: 0.3782 +- 0.0014


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.318 +- 0.0056
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.34 +- 0.0025
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.3328 +- 0.0026
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.328 +- 0.0025
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.3115 +- 0.0024



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
                   epi_0             N/A             N/A             N/A             N/A
                   epi_1             N/A             N/A             N/A             N/A
                  epi_13             N/A             N/A             N/A             N/A
                  epi_14             N/A             N/A             N/A             N/A
                  epi_15             N/A             N/A             N/A             N/A
                  epi_18             N/A             N/A             N/A             N/A
                   epi_2             N/A             N/A             N/A             N/A
                  epi_20             N/A             N/A             N/A             N/A
                   epi_3             N/A             N/A             N/A             N/A
                   epi_4             N/A             N/A             N/A             N/A
                   epi_5             N/A             N/A             N/A             N/A
                   epi_6             N/A             N/A             N/A             N/A
             epi_low_ent             N/A             N/A             N/A             N/A
                     mDC             N/A             N/A             N/A             N/A
                     pDC             N/A             N/A             N/A             N/A

                accuracy                                             N/A             N/A
               macro avg             N/A             N/A             N/A             N/A
            weighted avg             N/A             N/A             N/A             N/A

### Further Robustness Evaluation with metric: Accuracy 



### Further Robustness Evaluation with metric: Macro_F1 



