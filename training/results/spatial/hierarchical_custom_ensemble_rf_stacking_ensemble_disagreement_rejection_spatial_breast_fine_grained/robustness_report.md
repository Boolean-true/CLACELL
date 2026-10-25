# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.5429 +- 0.0048

### Classification Report 

                               precision          recall        f1-score         support

                   B_ACB 0.3228 +- 0.0095 0.4511 +- 0.0587 0.3753 +- 0.0262    832.0 +- 0.0
                  B_Cell 0.2667 +- 0.4389 0.0006 +- 0.001 0.0011 +- 0.002    697.0 +- 0.0
                   B_GCB      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    451.0 +- 0.0
                  B_IFIT 0.3725 +- 0.0092 0.4611 +- 0.0184 0.4118 +- 0.0078    673.0 +- 0.0
                 B_Naive 0.6417 +- 0.0992 0.0393 +- 0.0297 0.0713 +- 0.0478    379.0 +- 0.0
            CAFs (CA12+)      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      6.0 +- 0.0
         CAFs (COL11A1+) 0.7499 +- 0.0159 0.4743 +- 0.0239 0.5809 +- 0.0218    343.0 +- 0.0
             CAFs (DPT+) 0.8361 +- 0.0086 0.5249 +- 0.0195 0.6447 +- 0.0152    511.0 +- 0.0
            CAFs (LAMP5) 0.7107 +- 0.0101 0.6933 +- 0.0122 0.7018 +- 0.0091   1072.0 +- 0.0
            CAFs (PI16+) 0.5706 +- 0.0107 0.5755 +- 0.0133 0.573 +- 0.0114    952.0 +- 0.0
               CD4_Naive 0.4779 +- 0.0392 0.3044 +- 0.0661 0.3648 +- 0.0431   3062.0 +- 0.0
                 CD4_Tem 0.1599 +- 0.0162 0.089 +- 0.0322 0.1123 +- 0.0312   1396.0 +- 0.0
                 CD4_Tfh 0.3121 +- 0.0683 0.292 +- 0.1729 0.2921 +- 0.1236    953.0 +- 0.0
                  CD4_Th      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      3.0 +- 0.0
                CD4_Treg 0.5502 +- 0.015 0.4963 +- 0.0497 0.5212 +- 0.0337   2219.0 +- 0.0
                 CD8_Isg 0.2258 +- 0.0205 0.5083 +- 0.0341 0.3112 +- 0.014   1561.0 +- 0.0
                 CD8_Tem 0.3509 +- 0.0136 0.5355 +- 0.0264 0.4233 +- 0.0039   3705.0 +- 0.0
                 CD8_Tex 0.4673 +- 0.0495 0.2485 +- 0.0456 0.324 +- 0.0506   1683.0 +- 0.0
             Endo Arter. 0.8305 +- 0.0245 0.4986 +- 0.0253 0.6227 +- 0.0215    141.0 +- 0.0
             Endo Capil. 0.5139 +- 0.0188 0.4296 +- 0.0153 0.4678 +- 0.0136    169.0 +- 0.0
               Endo Imm. 0.7084 +- 0.0105 0.5946 +- 0.0107 0.6465 +- 0.0092    553.0 +- 0.0
             Endo Lymph.  0.91 +- 0.0698 0.1604 +- 0.0279 0.2716 +- 0.0414     48.0 +- 0.0
               Endo Ven. 0.6206 +- 0.0106 0.5882 +- 0.0208 0.6039 +- 0.015    441.0 +- 0.0
         Epithelial cell 0.9168 +- 0.005 0.8826 +- 0.0082 0.8993 +- 0.0048  13395.0 +- 0.0
                Mac/Mono  0.54 +- 0.0073 0.3307 +- 0.0102 0.4101 +- 0.0077    629.0 +- 0.0
               Mac_Anti. 0.9051 +- 0.0085 0.414 +- 0.0416 0.5671 +- 0.0391   1041.0 +- 0.0
                  Mac_ES 0.4643 +- 0.0742 0.0744 +- 0.0264 0.1269 +- 0.0421     43.0 +- 0.0
                 Mac_IFN 0.4503 +- 0.0084  0.57 +- 0.0176 0.503 +- 0.0108    743.0 +- 0.0
                  Mac_LA 0.4264 +- 0.0121 0.1792 +- 0.0088 0.2523 +- 0.0101    543.0 +- 0.0
             Mac_RTM_IFN 0.5447 +- 0.0086 0.4543 +- 0.0124 0.4953 +- 0.0096    884.0 +- 0.0
              Mac_RTM_LA 0.2589 +- 0.0073 0.4499 +- 0.0116 0.3286 +- 0.0085    351.0 +- 0.0
              Mac_RTM_MT 0.3671 +- 0.0124 0.3203 +- 0.0163 0.3419 +- 0.0122    192.0 +- 0.0
                    Mast 0.8167 +- 0.3375 0.0137 +- 0.0072 0.0269 +- 0.014    139.0 +- 0.0
           Myofibroblast 0.7426 +- 0.0474 0.097 +- 0.0069 0.1715 +- 0.0112    168.0 +- 0.0
                      NK 0.5207 +- 0.016 0.1996 +- 0.008 0.2884 +- 0.0075   1082.0 +- 0.0
                NK_Cyto. 0.5816 +- 0.0395 0.1549 +- 0.016 0.2442 +- 0.0207    253.0 +- 0.0
                  NK_rNK 0.2782 +- 0.0692 0.0196 +- 0.0082 0.0363 +- 0.0147    433.0 +- 0.0
               PCs (ECM) 0.6437 +- 0.0147 0.6716 +- 0.0117 0.6573 +- 0.0119    264.0 +- 0.0
              Plasma_IgG 0.9204 +- 0.0089 0.4616 +- 0.0233 0.6145 +- 0.0215    989.0 +- 0.0
          Prolif Stromal 0.6879 +- 0.0911 0.2316 +- 0.0566 0.3439 +- 0.068     19.0 +- 0.0
                Rejected      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0
               T_Prolif. 0.7231 +- 0.0156 0.582 +- 0.0967 0.6401 +- 0.0584    699.0 +- 0.0
                    VSMC 0.6341 +- 0.0141 0.4674 +- 0.0254 0.5379 +- 0.0204    322.0 +- 0.0
                    cDC1 0.7745 +- 0.0283 0.4683 +- 0.0231 0.5834 +- 0.0227    142.0 +- 0.0
                    cDC2 0.7343 +- 0.0037 0.6143 +- 0.0121 0.6689 +- 0.0079   2582.0 +- 0.0
                     mDC 0.6478 +- 0.0297 0.1675 +- 0.0267 0.2655 +- 0.0353    354.0 +- 0.0
                     pDC 0.9175 +- 0.0147 0.499 +- 0.0284 0.6461 +- 0.0258    201.0 +- 0.0

                accuracy                                 0.5429 +- 0.0048  47318.0 +- 0.0
               macro avg 0.5339 +- 0.0137 0.3466 +- 0.0053 0.3824 +- 0.0049  47318.0 +- 0.0
            weighted avg 0.6251 +- 0.0085 0.5429 +- 0.0048 0.559 +- 0.0023  47318.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.5323 +- 0.0042
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.542 +- 0.0046
Feature importance dropout (0.5% features dropped) Accuracy score: 0.5368 +- 0.0055
Feature importance dropout (1.0% features dropped) Accuracy score: 0.5404 +- 0.0045
Feature importance dropout (2.0% features dropped) Accuracy score: 0.5352 +- 0.0046


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.363 +- 0.0047
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.382 +- 0.0048
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.3712 +- 0.0041
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.373 +- 0.0037
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.3663 +- 0.0035



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



