--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.9224 +- 0.0065

                               precision          recall        f1-score         support

                  B cell   0.9917 +- 0.0   0.9917 +- 0.0   0.9917 +- 0.0    120.0 +- 0.0
          CD14+ monocyte 0.9984 +- 0.0006 0.9984 +- 0.0003 0.9984 +- 0.0004   2575.0 +- 0.0
             CD4+ T cell 0.903 +- 0.0137 0.9959 +- 0.001 0.9471 +- 0.0075   3910.0 +- 0.0
        Cytotoxic T cell 0.8931 +- 0.0089 0.7103 +- 0.0407 0.7906 +- 0.0244   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0      0.4 +- 0.0   0.5714 +- 0.0      5.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0      1.0 +- 0.0      1.0 +- 0.0      7.0 +- 0.0
     Natural killer cell 0.8172 +- 0.0135 0.7905 +- 0.0242 0.8033 +- 0.0098    791.0 +- 0.0
             Plasma cell 0.9915 +- 0.0109 0.9469 +- 0.0143 0.9687 +- 0.0098     49.0 +- 0.0

                accuracy                                 0.9224 +- 0.0065   9281.0 +- 0.0
               macro avg 0.9494 +- 0.002 0.8542 +- 0.0039 0.8839 +- 0.0036   9281.0 +- 0.0
            weighted avg 0.922 +- 0.0056 0.9224 +- 0.0065 0.9189 +- 0.0075   9281.0 +- 0.0

10% Random Dropout accuracy: 0.91 +- 0.0077
50% Random Dropout accuracy: 0.802 +- 0.0066
90% Random Dropout accuracy: 0.6833 +- 0.0122
92.5% Random Dropout accuracy: 0.6556 +- 0.0309
95% Random Dropout accuracy: 0.5883 +- 0.0783
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.9214 +- 0.0068
Feature importance dropout (0.5% features dropped) accuracy score 0.9011 +- 0.0075
Feature importance dropout (1.0% features dropped) accuracy score 0.8916 +- 0.0085
Feature importance dropout (2.0% features dropped) accuracy score 0.8611 +- 0.0103
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8677 +- 0.0039

                               precision          recall        f1-score         support

                  B cell 0.9993 +- 0.0002 0.9934 +- 0.0015 0.9963 +- 0.0008   3959.0 +- 0.0
          CD14+ monocyte 0.8988 +- 0.0164 0.9996 +- 0.0001 0.9464 +- 0.0091   3135.0 +- 0.0
             CD4+ T cell  0.92 +- 0.0076 0.9927 +- 0.0028 0.9549 +- 0.0032  13664.0 +- 0.0
        Cytotoxic T cell 0.6203 +- 0.0114 0.7456 +- 0.0239 0.677 +- 0.0115   4839.0 +- 0.0
          Dendritic cell 0.9882 +- 0.0016 0.5881 +- 0.0251  0.7371 +- 0.02    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.643 +- 0.0213 0.7825 +- 0.0158     86.0 +- 0.0
     Natural killer cell 0.8715 +- 0.0148 0.1903 +- 0.0462 0.3099 +- 0.0665   2751.0 +- 0.0
             Plasma cell 0.7768 +- 0.1239      1.0 +- 0.0 0.8694 +- 0.0785     23.0 +- 0.0

                accuracy                                 0.8677 +- 0.0039  28986.0 +- 0.0
               macro avg 0.8844 +- 0.0141 0.7691 +- 0.007 0.7842 +- 0.009  28986.0 +- 0.0
            weighted avg 0.8753 +- 0.0043 0.8677 +- 0.0039 0.8475 +- 0.0068  28986.0 +- 0.0

10% Random Dropout accuracy: 0.8589 +- 0.0049
50% Random Dropout accuracy: 0.7399 +- 0.0161
90% Random Dropout accuracy: 0.545 +- 0.0211
92.5% Random Dropout accuracy: 0.5254 +- 0.031
95% Random Dropout accuracy: 0.5021 +- 0.028
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8672 +- 0.0041
Feature importance dropout (0.5% features dropped) accuracy score 0.8547 +- 0.004
Feature importance dropout (1.0% features dropped) accuracy score 0.8452 +- 0.0047
Feature importance dropout (2.0% features dropped) accuracy score 0.8036 +- 0.0068
