# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.3985 +- 0.0025

### Classification Report 

                               precision          recall        f1-score         support

           Activated NBC      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   3357.0 +- 0.0
                   CD4 T  0.47 +- 0.0027 0.6026 +- 0.0079 0.5281 +- 0.0026   9228.0 +- 0.0
                   CD8 T 0.8259 +- 0.0132 0.0633 +- 0.0057 0.1176 +- 0.0098   1563.0 +- 0.0
                      DC      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    267.0 +- 0.0
                      DN      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    281.0 +- 0.0
                     FDC 0.8909 +- 0.0072 0.2963 +- 0.0208 0.4443 +- 0.0224    486.0 +- 0.0
                    GCBC 0.4443 +- 0.0092 0.6544 +- 0.0272 0.5288 +- 0.0041  15654.0 +- 0.0
            Granulocytes      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    108.0 +- 0.0
                     ILC      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0     69.0 +- 0.0
                     MBC   0.1 +- 0.3162   0.0 +- 0.0001   0.0 +- 0.0001   9254.0 +- 0.0
                    Mast      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0     13.0 +- 0.0
              Mono/Macro 0.8046 +- 0.033 0.4649 +- 0.0396 0.5875 +- 0.0249    615.0 +- 0.0
                     NBC 0.3011 +- 0.0048 0.6748 +- 0.0268 0.4162 +- 0.0025  10138.0 +- 0.0
                      NK      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0     55.0 +- 0.0
             Naive CD4 T      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   3071.0 +- 0.0
             Naive CD8 T      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   1032.0 +- 0.0
                      PC 0.511 +- 0.1804 0.0017 +- 0.001 0.0034 +- 0.0021   2208.0 +- 0.0
                     PDC      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    145.0 +- 0.0
             cycling FDC      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0     81.0 +- 0.0
               cycling T      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0    579.0 +- 0.0
         cycling myeloid      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0     32.0 +- 0.0
              epithelial 0.9002 +- 0.0206 0.6203 +- 0.0227 0.7341 +- 0.0146    153.0 +- 0.0
                  preB/T      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0     12.0 +- 0.0

                accuracy                                 0.3985 +- 0.0025  58401.0 +- 0.0
               macro avg 0.2282 +- 0.0158 0.1469 +- 0.0025 0.1461 +- 0.0018  58401.0 +- 0.0
            weighted avg 0.3211 +- 0.0518 0.3985 +- 0.0025 0.3125 +- 0.0016  58401.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.3889 +- 0.0024
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.3957 +- 0.0025
Feature importance dropout (0.5% features dropped) Accuracy score: 0.3964 +- 0.0028
Feature importance dropout (1.0% features dropped) Accuracy score: 0.3895 +- 0.0044
Feature importance dropout (2.0% features dropped) Accuracy score: 0.3804 +- 0.0047


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.1347 +- 0.004
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.1456 +- 0.0018
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.1439 +- 0.0017
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.1407 +- 0.0022
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.1365 +- 0.002



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



