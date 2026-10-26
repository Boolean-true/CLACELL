# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.4882 +- 0.01

### Classification Report 

                               precision          recall        f1-score         support

                   B_ACB 0.3256 +- 0.0099 0.4278 +- 0.0338 0.3694 +- 0.0174    832.0 +- 0.0
                  B_Cell  0.05 +- 0.1581 0.0001 +- 0.0005 0.0003 +- 0.0009    697.0 +- 0.0
                   B_GCB      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    451.0 +- 0.0
                  B_IFIT 0.3669 +- 0.0133 0.4192 +- 0.0175 0.3909 +- 0.0079    673.0 +- 0.0
                 B_Naive 0.5835 +- 0.2632 0.0182 +- 0.0114 0.035 +- 0.0212    379.0 +- 0.0
            CAFs (CA12+)      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      6.0 +- 0.0
         CAFs (COL11A1+) 0.7465 +- 0.0117 0.4152 +- 0.0148 0.5334 +- 0.0126    343.0 +- 0.0
             CAFs (DPT+) 0.8331 +- 0.0137 0.4479 +- 0.0179 0.5824 +- 0.0159    511.0 +- 0.0
            CAFs (LAMP5) 0.713 +- 0.0136 0.6038 +- 0.0178 0.6538 +- 0.0145   1072.0 +- 0.0
            CAFs (PI16+) 0.5654 +- 0.0134 0.4935 +- 0.0289 0.5268 +- 0.0214    952.0 +- 0.0
               CD4_Naive 0.4867 +- 0.0399 0.2917 +- 0.0622 0.3581 +- 0.0387   3062.0 +- 0.0
                 CD4_Tem  0.168 +- 0.007 0.0837 +- 0.0299 0.109 +- 0.0272   1396.0 +- 0.0
                 CD4_Tfh 0.2868 +- 0.0814 0.2018 +- 0.1786 0.212 +- 0.1632    953.0 +- 0.0
                  CD4_Th      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      3.0 +- 0.0
                CD4_Treg 0.5373 +- 0.0247 0.4543 +- 0.0745 0.4907 +- 0.0537   2219.0 +- 0.0
                 CD8_Isg 0.2188 +- 0.0194 0.5084 +- 0.0376 0.3044 +- 0.0126   1561.0 +- 0.0
                 CD8_Tem 0.3495 +- 0.013  0.53 +- 0.0227 0.4207 +- 0.0046   3705.0 +- 0.0
                 CD8_Tex 0.4269 +- 0.0814 0.1958 +- 0.0654 0.2673 +- 0.0777   1683.0 +- 0.0
             Endo Arter. 0.8279 +- 0.0192 0.3936 +- 0.0393 0.5324 +- 0.034    141.0 +- 0.0
             Endo Capil. 0.504 +- 0.0177 0.3852 +- 0.0232 0.4364 +- 0.019    169.0 +- 0.0
               Endo Imm. 0.7167 +- 0.0133 0.4888 +- 0.0133 0.581 +- 0.0096    553.0 +- 0.0
             Endo Lymph. 0.9289 +- 0.0783 0.1271 +- 0.0373 0.2217 +- 0.0575     48.0 +- 0.0
               Endo Ven. 0.6116 +- 0.012 0.4805 +- 0.0239 0.538 +- 0.0181    441.0 +- 0.0
         Epithelial cell 0.9109 +- 0.0058 0.8043 +- 0.0245 0.8541 +- 0.0159  13395.0 +- 0.0
                Mac/Mono 0.5348 +- 0.0104 0.3068 +- 0.007 0.3899 +- 0.0067    629.0 +- 0.0
               Mac_Anti. 0.8952 +- 0.0122 0.3048 +- 0.0291 0.4541 +- 0.0324   1041.0 +- 0.0
                  Mac_ES 0.6108 +- 0.1852 0.0744 +- 0.0183 0.1317 +- 0.0319     43.0 +- 0.0
                 Mac_IFN 0.439 +- 0.0078 0.4829 +- 0.0127 0.4598 +- 0.007    743.0 +- 0.0
                  Mac_LA 0.4258 +- 0.0129 0.1604 +- 0.009 0.233 +- 0.0109    543.0 +- 0.0
             Mac_RTM_IFN 0.5424 +- 0.0083 0.407 +- 0.0113  0.465 +- 0.009    884.0 +- 0.0
              Mac_RTM_LA 0.2621 +- 0.0088 0.4057 +- 0.0205 0.3183 +- 0.0114    351.0 +- 0.0
              Mac_RTM_MT 0.3553 +- 0.0189 0.2719 +- 0.0249 0.3078 +- 0.0221    192.0 +- 0.0
                    Mast      1.0 +- 0.0 0.0137 +- 0.0053 0.0269 +- 0.0103    139.0 +- 0.0
           Myofibroblast 0.7394 +- 0.0732 0.0792 +- 0.0097 0.1428 +- 0.0163    168.0 +- 0.0
                      NK 0.5171 +- 0.0169 0.1736 +- 0.0132 0.2597 +- 0.0151   1082.0 +- 0.0
                NK_Cyto. 0.5817 +- 0.0574 0.1407 +- 0.0193 0.226 +- 0.0264    253.0 +- 0.0
                  NK_rNK 0.2329 +- 0.0347 0.0145 +- 0.0058 0.0272 +- 0.0104    433.0 +- 0.0
               PCs (ECM) 0.6462 +- 0.0258 0.5398 +- 0.0315 0.588 +- 0.0273    264.0 +- 0.0
              Plasma_IgG 0.9117 +- 0.0103 0.3785 +- 0.0322 0.5342 +- 0.0319    989.0 +- 0.0
          Prolif Stromal 0.6917 +- 0.1282 0.1579 +- 0.0656 0.2498 +- 0.0851     19.0 +- 0.0
                Rejected      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0
               T_Prolif. 0.7131 +- 0.0243 0.4456 +- 0.1409 0.5383 +- 0.1132    699.0 +- 0.0
                    VSMC 0.6162 +- 0.0279 0.3537 +- 0.0242 0.4491 +- 0.0245    322.0 +- 0.0
                    cDC1 0.7914 +- 0.0196 0.4113 +- 0.0253 0.5409 +- 0.0237    142.0 +- 0.0
                    cDC2 0.7309 +- 0.0081 0.5423 +- 0.0125 0.6225 +- 0.0094   2582.0 +- 0.0
                     mDC 0.5984 +- 0.0287 0.1316 +- 0.0074 0.2158 +- 0.0114    354.0 +- 0.0
                     pDC 0.9065 +- 0.0268    0.4 +- 0.027 0.5544 +- 0.0252    201.0 +- 0.0

                accuracy                                  0.4882 +- 0.01  47318.0 +- 0.0
               macro avg 0.5298 +- 0.0076 0.2972 +- 0.0028 0.3437 +- 0.0028  47318.0 +- 0.0
            weighted avg 0.6162 +- 0.0064  0.4882 +- 0.01 0.5216 +- 0.0063  47318.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.4793 +- 0.0096
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.4882 +- 0.0092
Feature importance dropout (0.5% features dropped) Accuracy score: 0.4843 +- 0.0097
Feature importance dropout (1.0% features dropped) Accuracy score: 0.4885 +- 0.0085
Feature importance dropout (2.0% features dropped) Accuracy score: 0.4848 +- 0.0086


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.3265 +- 0.0018
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.3436 +- 0.0027
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.3344 +- 0.0037
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.3365 +- 0.0039
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.3309 +- 0.0032



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



