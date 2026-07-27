--- Robustness Evaluation ---
--- In distribution testset ---
Baseline accuracy score 0.851 +- 0.0185

                               precision          recall        f1-score         support

                  B cell 0.9666 +- 0.0098 0.9592 +- 0.0293 0.9626 +- 0.0136    120.0 +- 0.0
          CD14+ monocyte 0.9966 +- 0.002 0.9981 +- 0.0011 0.9973 +- 0.0012   2575.0 +- 0.0
             CD4+ T cell 0.8401 +- 0.0516 0.9928 +- 0.0021 0.9093 +- 0.0293   3910.0 +- 0.0
        Cytotoxic T cell 0.9325 +- 0.0264 0.3045 +- 0.1053 0.4501 +- 0.1159   1824.0 +- 0.0
          Dendritic cell      1.0 +- 0.0  0.26 +- 0.0966 0.4048 +- 0.115      5.0 +- 0.0
           Megakaryocyte 0.9875 +- 0.0395      1.0 +- 0.0 0.9933 +- 0.0211      7.0 +- 0.0
     Natural killer cell 0.5846 +- 0.1191 0.9186 +- 0.0316 0.7065 +- 0.086    791.0 +- 0.0
             Plasma cell 0.9721 +- 0.0181 0.8367 +- 0.0419 0.8987 +- 0.0229     49.0 +- 0.0

                accuracy                                 0.851 +- 0.0185   9281.0 +- 0.0
               macro avg  0.91 +- 0.0122 0.7837 +- 0.0162 0.7903 +- 0.0207   9281.0 +- 0.0
            weighted avg 0.8824 +- 0.0131 0.851 +- 0.0185 0.8266 +- 0.0275   9281.0 +- 0.0

Random dropout accuracy score 0.8362 +- 0.0153
Total samples: 9281.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.846 +- 0.0171
Feature importance dropout (0.5% features dropped) accuracy score 0.8269 +- 0.0131
Feature importance dropout (1.0% features dropped) accuracy score 0.8144 +- 0.0116
Feature importance dropout (2.0% features dropped) accuracy score 0.792 +- 0.0086
--- Out of data distribution ---
Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.8457 +- 0.0111

                               precision          recall        f1-score         support

                  B cell 0.9986 +- 0.0004 0.9298 +- 0.042 0.9625 +- 0.023   3959.0 +- 0.0
          CD14+ monocyte 0.8769 +- 0.0271 0.9936 +- 0.0105 0.9315 +- 0.0191   3135.0 +- 0.0
             CD4+ T cell 0.8524 +- 0.0189 0.9936 +- 0.0039 0.9175 +- 0.012  13664.0 +- 0.0
        Cytotoxic T cell 0.6672 +- 0.0563 0.4875 +- 0.0625 0.5588 +- 0.0318   4839.0 +- 0.0
          Dendritic cell 0.9955 +- 0.0018 0.6015 +- 0.0661 0.748 +- 0.0521    529.0 +- 0.0
           Megakaryocyte      1.0 +- 0.0 0.5919 +- 0.0242 0.7433 +- 0.019     86.0 +- 0.0
     Natural killer cell 0.7865 +- 0.0781 0.5064 +- 0.1742 0.5906 +- 0.1175   2751.0 +- 0.0
             Plasma cell 0.7915 +- 0.1545 0.787 +- 0.0949 0.7808 +- 0.0914     23.0 +- 0.0

                accuracy                                 0.8457 +- 0.0111  28986.0 +- 0.0
               macro avg 0.8711 +- 0.0233 0.7364 +- 0.0105 0.7791 +- 0.0153  28986.0 +- 0.0
            weighted avg 0.8408 +- 0.0103 0.8457 +- 0.0111 0.8305 +- 0.0136  28986.0 +- 0.0

Random dropout accuracy score 0.824 +- 0.0136
Total samples: 28986.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) accuracy score 0.8415 +- 0.0103
Feature importance dropout (0.5% features dropped) accuracy score 0.8003 +- 0.0157
Feature importance dropout (1.0% features dropped) accuracy score 0.7648 +- 0.0204
Feature importance dropout (2.0% features dropped) accuracy score 0.6844 +- 0.0212
