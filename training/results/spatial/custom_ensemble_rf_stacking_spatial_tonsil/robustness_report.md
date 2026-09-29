# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.616 +- 0.0019

### Classification Report 

                               precision          recall        f1-score         support

           Activated NBC      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   3357.0 +- 0.0
                   CD4 T 0.7269 +- 0.0027 0.8958 +- 0.0041 0.8026 +- 0.0021   9228.0 +- 0.0
                   CD8 T 0.8634 +- 0.0047 0.7328 +- 0.0109 0.7927 +- 0.0049   1563.0 +- 0.0
                      DC 0.8644 +- 0.006 0.764 +- 0.0079 0.8111 +- 0.0054    267.0 +- 0.0
                      DN      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    281.0 +- 0.0
                     FDC 0.8889 +- 0.0037 0.9088 +- 0.0061 0.8988 +- 0.0041    486.0 +- 0.0
                    GCBC 0.649 +- 0.0039 0.8169 +- 0.0063 0.7233 +- 0.0019  15654.0 +- 0.0
            Granulocytes 0.9919 +- 0.0177 0.2444 +- 0.0393 0.3908 +- 0.0525    108.0 +- 0.0
                     ILC      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0     69.0 +- 0.0
                     MBC 0.6079 +- 0.008 0.2036 +- 0.0058 0.305 +- 0.0064   9254.0 +- 0.0
                    Mast      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0     13.0 +- 0.0
              Mono/Macro 0.8685 +- 0.005 0.8763 +- 0.0039 0.8724 +- 0.0037    615.0 +- 0.0
                     NBC 0.4352 +- 0.0036 0.7618 +- 0.0039 0.5539 +- 0.0028  10138.0 +- 0.0
                      NK 0.571 +- 0.0349 0.2036 +- 0.0391 0.298 +- 0.0429     55.0 +- 0.0
             Naive CD4 T 0.7041 +- 0.0149 0.4211 +- 0.0108 0.5268 +- 0.0083   3071.0 +- 0.0
             Naive CD8 T 0.8732 +- 0.0207 0.502 +- 0.0599 0.6352 +- 0.0441   1032.0 +- 0.0
                      PC 0.8364 +- 0.0234 0.4088 +- 0.0184 0.5486 +- 0.0135   2208.0 +- 0.0
                     PDC 0.9905 +- 0.0033 0.8579 +- 0.0081 0.9194 +- 0.0045    145.0 +- 0.0
             cycling FDC      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0     81.0 +- 0.0
               cycling T      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    579.0 +- 0.0
         cycling myeloid      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0     32.0 +- 0.0
              epithelial 0.9705 +- 0.0068 0.7078 +- 0.0154 0.8185 +- 0.0091    153.0 +- 0.0
                  preB/T      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0     12.0 +- 0.0

                accuracy                                 0.616 +- 0.0019  58401.0 +- 0.0
               macro avg 0.5149 +- 0.002 0.4046 +- 0.0043 0.4303 +- 0.0038  58401.0 +- 0.0
            weighted avg 0.5957 +- 0.0017 0.616 +- 0.0019 0.5719 +- 0.0018  58401.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.5983 +- 0.0034
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.615 +- 0.002
Feature importance dropout (0.5% features dropped) Accuracy score: 0.6137 +- 0.0022
Feature importance dropout (1.0% features dropped) Accuracy score: 0.6064 +- 0.0016
Feature importance dropout (2.0% features dropped) Accuracy score: 0.5953 +- 0.0019


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.4081 +- 0.0052
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.4299 +- 0.0038
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.4282 +- 0.0034
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.4022 +- 0.0027
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.3745 +- 0.0029



## Out of data distribution 

### OOD Dataset: All 

Baseline accuracy score: N/A

### Classification Report 

                               precision          recall        f1-score         support

           Activated NBC             N/A             N/A             N/A             N/A
                   CD4 T             N/A             N/A             N/A             N/A
                   CD8 T             N/A             N/A             N/A             N/A
                      DC             N/A             N/A             N/A             N/A
                      DN             N/A             N/A             N/A             N/A
                     FDC             N/A             N/A             N/A             N/A
                    GCBC             N/A             N/A             N/A             N/A
            Granulocytes             N/A             N/A             N/A             N/A
                     ILC             N/A             N/A             N/A             N/A
                     MBC             N/A             N/A             N/A             N/A
                    Mast             N/A             N/A             N/A             N/A
              Mono/Macro             N/A             N/A             N/A             N/A
                     NBC             N/A             N/A             N/A             N/A
                      NK             N/A             N/A             N/A             N/A
             Naive CD4 T             N/A             N/A             N/A             N/A
             Naive CD8 T             N/A             N/A             N/A             N/A
                      PC             N/A             N/A             N/A             N/A
                     PDC             N/A             N/A             N/A             N/A
             cycling FDC             N/A             N/A             N/A             N/A
               cycling T             N/A             N/A             N/A             N/A
         cycling myeloid             N/A             N/A             N/A             N/A
              epithelial             N/A             N/A             N/A             N/A
                  preB/T             N/A             N/A             N/A             N/A

                accuracy                                             N/A             N/A
               macro avg             N/A             N/A             N/A             N/A
            weighted avg             N/A             N/A             N/A             N/A

### Further Robustness Evaluation with metric: Accuracy 



### Further Robustness Evaluation with metric: Macro_F1 



