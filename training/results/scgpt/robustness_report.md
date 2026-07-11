--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.7971 +- 0.0904

                               precision          recall        f1-score         support

                  B cell 0.9767 +- 0.0585 0.9513 +- 0.0252 0.9624 +- 0.0271    117.0 +- 0.0
          CD14+ monocyte 0.9961 +- 0.0051 0.7846 +- 0.2141 0.862 +- 0.1431   2576.0 +- 0.0
             CD4+ T cell 0.9143 +- 0.084 0.9348 +- 0.0803 0.9192 +- 0.0474   3909.0 +- 0.0
        Cytotoxic T cell 0.7419 +- 0.2723 0.4545 +- 0.379 0.4943 +- 0.3363   1821.0 +- 0.0
          Dendritic cell 0.5243 +- 0.4057  0.56 +- 0.2271 0.405 +- 0.2491      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.5423 +- 0.2355 0.9118 +- 0.2238 0.6184 +- 0.1633    788.0 +- 0.0
             Plasma cell 0.4808 +- 0.3338 0.9857 +- 0.0194 0.5792 +- 0.3274     49.0 +- 0.0

                accuracy                                 0.7971 +- 0.0904   9272.0 +- 0.0
               macro avg 0.772 +- 0.1254 0.8228 +- 0.0438 0.7301 +- 0.0996   9272.0 +- 0.0
            weighted avg 0.8699 +- 0.0677 0.7971 +- 0.0904 0.7928 +- 0.0891   9272.0 +- 0.0

Random dropout accuracy score 0.8184 +- 0.0803
Total samples: 9272.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.7967 +- 0.0906
Feature importance dropout (0.5% features dropped) accuracy score 0.7895 +- 0.0944
Feature importance dropout (1.0% features dropped) accuracy score 0.7967 +- 0.091
Feature importance dropout (2.0% features dropped) accuracy score 0.7869 +- 0.095
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8663 +- 0.0462

                               precision          recall        f1-score         support

                  B cell 0.9894 +- 0.0282 0.9966 +- 0.0036 0.9928 +- 0.0145   3959.0 +- 0.0
          CD14+ monocyte 0.9632 +- 0.0215  0.9529 +- 0.07 0.9563 +- 0.0342   3135.0 +- 0.0
             CD4+ T cell 0.9631 +- 0.0448 0.9282 +- 0.0722 0.9425 +- 0.0315  13664.0 +- 0.0
        Cytotoxic T cell 0.722 +- 0.2185 0.5611 +- 0.2964 0.5772 +- 0.1999   4839.0 +- 0.0
          Dendritic cell 0.7991 +- 0.1958 0.8701 +- 0.1318 0.805 +- 0.1046    529.0 +- 0.0
           Megakaryocyte  0.995 +- 0.008 0.6372 +- 0.0572 0.7754 +- 0.0417     86.0 +- 0.0
     Natural killer cell 0.6611 +- 0.1846  0.815 +- 0.337 0.6382 +- 0.2406   2751.0 +- 0.0
             Plasma cell 0.746 +- 0.1768 0.9826 +- 0.055 0.835 +- 0.1266     23.0 +- 0.0

                accuracy                                 0.8663 +- 0.0462  28986.0 +- 0.0
               macro avg 0.8549 +- 0.0584 0.843 +- 0.0297 0.8153 +- 0.0429  28986.0 +- 0.0
            weighted avg 0.8947 +- 0.0355 0.8663 +- 0.0462 0.8579 +- 0.0476  28986.0 +- 0.0

Random dropout accuracy score 0.8678 +- 0.0415
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 6770.5 +- 4031.5095
Feature importance dropout (0.1% features dropped) accuracy score 0.8663 +- 0.0462
Feature importance dropout (0.5% features dropped) accuracy score 0.8658 +- 0.0463
Feature importance dropout (1.0% features dropped) accuracy score 0.8711 +- 0.0429
Feature importance dropout (2.0% features dropped) accuracy score 0.8667 +- 0.042
