--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9178 +- 0.0109

                               precision          recall        f1-score         support

                  B cell 0.9925 +- 0.0047 0.9875 +- 0.0071  0.99 +- 0.0045    120.0 +- 0.0
          CD14+ monocyte 0.9969 +- 0.0016 0.9984 +- 0.0004 0.9976 +- 0.001   2575.0 +- 0.0
             CD4+ T cell 0.9273 +- 0.0227 0.9931 +- 0.0023 0.9589 +- 0.0112   3910.0 +- 0.0
        Cytotoxic T cell 0.8447 +- 0.0311 0.7412 +- 0.0665 0.7877 +- 0.0355   1824.0 +- 0.0
          Dendritic cell 0.9667 +- 0.1054  0.44 +- 0.1578 0.5901 +- 0.1457      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.7369 +- 0.0352 0.6796 +- 0.0819 0.7045 +- 0.0488    791.0 +- 0.0
             Plasma cell 0.9658 +- 0.0225 0.9653 +- 0.0237 0.9653 +- 0.0169     49.0 +- 0.0

                accuracy                                 0.9178 +- 0.0109   9281.0 +- 0.0
               macro avg 0.9288 +- 0.0127 0.8506 +- 0.0226 0.8743 +- 0.019   9281.0 +- 0.0
            weighted avg 0.9152 +- 0.0119 0.9178 +- 0.0109 0.9146 +- 0.0118   9281.0 +- 0.0

10% Random Dropout accuracy: 0.9098 +- 0.0112
50% Random Dropout accuracy: 0.8205 +- 0.0229
90% Random Dropout accuracy: 0.6672 +- 0.0566
92.5% Random Dropout accuracy: 0.644 +- 0.0718
95% Random Dropout accuracy: 0.601 +- 0.0985
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9155 +- 0.011
Feature importance dropout (0.5% features dropped) accuracy score 0.8984 +- 0.0131
Feature importance dropout (1.0% features dropped) accuracy score 0.8763 +- 0.0177
Feature importance dropout (2.0% features dropped) accuracy score 0.8372 +- 0.0212
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8737 +- 0.0072

                               precision          recall        f1-score         support

                  B cell 0.9991 +- 0.0003 0.9944 +- 0.0031 0.9967 +- 0.0016   3959.0 +- 0.0
          CD14+ monocyte 0.8961 +- 0.0348 0.9992 +- 0.0007 0.9445 +- 0.0195   3135.0 +- 0.0
             CD4+ T cell 0.9357 +- 0.0097 0.9854 +- 0.008 0.9599 +- 0.0053  13664.0 +- 0.0
        Cytotoxic T cell 0.632 +- 0.0168 0.7799 +- 0.0356  0.6976 +- 0.01   4839.0 +- 0.0
          Dendritic cell 0.9824 +- 0.0061 0.6183 +- 0.0919 0.7553 +- 0.0668    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0  0.65 +- 0.0229 0.7877 +- 0.0167     86.0 +- 0.0
     Natural killer cell 0.8106 +- 0.0498 0.2225 +- 0.0719 0.3432 +- 0.0979   2751.0 +- 0.0
             Plasma cell 0.817 +- 0.1109 0.987 +- 0.0293 0.8896 +- 0.0648     23.0 +- 0.0

                accuracy                                 0.8737 +- 0.0072  28986.0 +- 0.0
               macro avg 0.8841 +- 0.0164 0.7796 +- 0.0125 0.7968 +- 0.0122  28986.0 +- 0.0
            weighted avg 0.8784 +- 0.0094 0.8737 +- 0.0072 0.8566 +- 0.0096  28986.0 +- 0.0

10% Random Dropout accuracy: 0.8683 +- 0.0087
50% Random Dropout accuracy: 0.7686 +- 0.0387
90% Random Dropout accuracy: 0.5381 +- 0.0423
92.5% Random Dropout accuracy: 0.5166 +- 0.0632
95% Random Dropout accuracy: 0.4992 +- 0.0743
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8728 +- 0.0073
Feature importance dropout (0.5% features dropped) accuracy score 0.8614 +- 0.0081
Feature importance dropout (1.0% features dropped) accuracy score 0.8475 +- 0.01
Feature importance dropout (2.0% features dropped) accuracy score 0.7942 +- 0.0241
