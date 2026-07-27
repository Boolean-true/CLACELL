--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9089 +- 0.01

                               precision          recall        f1-score         support

                  B cell 0.9974 +- 0.0041 0.9617 +- 0.0125 0.9792 +- 0.0063    120.0 +- 0.0
          CD14+ monocyte 0.9911 +- 0.0035 0.9972 +- 0.0008 0.9942 +- 0.0015   2575.0 +- 0.0
             CD4+ T cell 0.9212 +- 0.0123 0.9931 +- 0.002 0.9557 +- 0.0066   3910.0 +- 0.0
        Cytotoxic T cell 0.8774 +- 0.0212 0.6601 +- 0.0718 0.7506 +- 0.0422   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0  0.48 +- 0.1932  0.629 +- 0.169      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.6685 +- 0.0686 0.7709 +- 0.0611 0.711 +- 0.0213    791.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.9429 +- 0.0285 0.9704 +- 0.0152     49.0 +- 0.0

                accuracy                                  0.9089 +- 0.01   9281.0 +- 0.0
               macro avg 0.932 +- 0.0065 0.8507 +- 0.0231 0.8738 +- 0.0228   9281.0 +- 0.0
            weighted avg 0.9119 +- 0.0055  0.9089 +- 0.01 0.9055 +- 0.0109   9281.0 +- 0.0

Random dropout accuracy score 0.9019 +- 0.01
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9064 +- 0.0105
Feature importance dropout (0.5% features dropped) accuracy score 0.8881 +- 0.0109
Feature importance dropout (1.0% features dropped) accuracy score 0.8635 +- 0.0117
Feature importance dropout (2.0% features dropped) accuracy score 0.8295 +- 0.0119
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.849 +- 0.0155

                               precision          recall        f1-score         support

                  B cell 0.9991 +- 0.0003 0.9683 +- 0.0139 0.9834 +- 0.0072   3959.0 +- 0.0
          CD14+ monocyte 0.6973 +- 0.0745 0.9985 +- 0.0009 0.8191 +- 0.0505   3135.0 +- 0.0
             CD4+ T cell 0.9436 +- 0.0091 0.943 +- 0.0234 0.9431 +- 0.0096  13664.0 +- 0.0
        Cytotoxic T cell 0.6614 +- 0.0229 0.7113 +- 0.0373 0.6847 +- 0.0188   4839.0 +- 0.0
          Dendritic cell 0.9847 +- 0.0033 0.4552 +- 0.0647 0.6202 +- 0.0615    529.0 +- 0.0
           Megakaryocyte 0.982 +- 0.0116 0.7547 +- 0.0297 0.8531 +- 0.0191     86.0 +- 0.0
     Natural killer cell 0.7077 +- 0.0515  0.3598 +- 0.09 0.4697 +- 0.0724   2751.0 +- 0.0
             Plasma cell 0.9719 +- 0.0415 0.9826 +- 0.0225 0.9766 +- 0.0206     23.0 +- 0.0

                accuracy                                 0.849 +- 0.0155  28986.0 +- 0.0
               macro avg 0.8685 +- 0.0133 0.7717 +- 0.0178 0.7937 +- 0.0198  28986.0 +- 0.0
            weighted avg 0.8559 +- 0.012 0.849 +- 0.0155 0.841 +- 0.0155  28986.0 +- 0.0

Random dropout accuracy score 0.8222 +- 0.0233
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8432 +- 0.0171
Feature importance dropout (0.5% features dropped) accuracy score 0.8123 +- 0.0234
Feature importance dropout (1.0% features dropped) accuracy score 0.7692 +- 0.0326
Feature importance dropout (2.0% features dropped) accuracy score 0.7001 +- 0.0437
