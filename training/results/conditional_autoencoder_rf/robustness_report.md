--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9146 +- 0.0089

                               precision          recall        f1-score         support

                  B cell 0.9892 +- 0.0068 0.9892 +- 0.0056 0.9892 +- 0.0045    120.0 +- 0.0
          CD14+ monocyte 0.9851 +- 0.0051 0.9965 +- 0.0014 0.9908 +- 0.0023   2575.0 +- 0.0
             CD4+ T cell 0.9501 +- 0.0145 0.9792 +- 0.0038 0.9644 +- 0.0064   3910.0 +- 0.0
        Cytotoxic T cell 0.8969 +- 0.0265 0.6958 +- 0.0542 0.7823 +- 0.0328   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0      0.4 +- 0.0   0.5714 +- 0.0      5.0 +- 0.0
           Megakaryocyte 0.9653 +- 0.0767      1.0 +- 0.0 0.9808 +- 0.0427      7.0 +- 0.0
     Natural killer cell 0.6195 +- 0.0384 0.8216 +- 0.0643 0.7047 +- 0.0347    791.0 +- 0.0
             Plasma cell      1.0 +- 0.0 0.951 +- 0.0172 0.9748 +- 0.0091     49.0 +- 0.0

                accuracy                                 0.9146 +- 0.0089   9281.0 +- 0.0
               macro avg 0.9258 +- 0.0109 0.8542 +- 0.0083 0.8698 +- 0.0086   9281.0 +- 0.0
            weighted avg 0.922 +- 0.0088 0.9146 +- 0.0089 0.914 +- 0.0096   9281.0 +- 0.0

Random dropout accuracy score 0.9071 +- 0.0101
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9108 +- 0.0084
Feature importance dropout (0.5% features dropped) accuracy score 0.8944 +- 0.0111
Feature importance dropout (1.0% features dropped) accuracy score 0.8742 +- 0.0139
Feature importance dropout (2.0% features dropped) accuracy score 0.835 +- 0.0174
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8663 +- 0.0127

                               precision          recall        f1-score         support

                  B cell 0.9993 +- 0.0004  0.962 +- 0.016 0.9803 +- 0.0084   3959.0 +- 0.0
          CD14+ monocyte 0.8275 +- 0.073 0.9917 +- 0.0063 0.9006 +- 0.0466   3135.0 +- 0.0
             CD4+ T cell 0.9241 +- 0.0251 0.9637 +- 0.0242 0.943 +- 0.0114  13664.0 +- 0.0
        Cytotoxic T cell 0.7054 +- 0.0454 0.6337 +- 0.0777 0.665 +- 0.0507   4839.0 +- 0.0
          Dendritic cell 0.9963 +- 0.0018 0.6709 +- 0.0573 0.8006 +- 0.0416    529.0 +- 0.0
           Megakaryocyte 0.9982 +- 0.0055 0.6547 +- 0.0146 0.7907 +- 0.0108     86.0 +- 0.0
     Natural killer cell 0.6645 +- 0.0748 0.5545 +- 0.1178 0.5956 +- 0.0753   2751.0 +- 0.0
             Plasma cell  0.976 +- 0.054 0.9652 +- 0.0494 0.9696 +- 0.0416     23.0 +- 0.0

                accuracy                                 0.8663 +- 0.0127  28986.0 +- 0.0
               macro avg 0.8864 +- 0.0109 0.7995 +- 0.0183 0.8307 +- 0.0144  28986.0 +- 0.0
            weighted avg 0.8644 +- 0.0147 0.8663 +- 0.0127 0.8611 +- 0.0147  28986.0 +- 0.0

Random dropout accuracy score 0.8403 +- 0.0259
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8592 +- 0.0147
Feature importance dropout (0.5% features dropped) accuracy score 0.825 +- 0.0222
Feature importance dropout (1.0% features dropped) accuracy score 0.7598 +- 0.0517
Feature importance dropout (2.0% features dropped) accuracy score 0.6929 +- 0.0569
