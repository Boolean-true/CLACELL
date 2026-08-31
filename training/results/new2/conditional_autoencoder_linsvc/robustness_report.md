# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.5173 +- 0.033

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.9992 +- 0.0008 0.8153 +- 0.0875 0.8956 +- 0.0535   3456.0 +- 0.0
          CD16+ Monocyte 0.5158 +- 0.2303 0.9539 +- 0.0493 0.6412 +- 0.1916    193.0 +- 0.0
    CD1C+ dendritic cell 0.2036 +- 0.1433 0.9731 +- 0.0319 0.3148 +- 0.1782    108.0 +- 0.0
       CD4 Memory T cell 0.4641 +- 0.0679 0.6321 +- 0.2583 0.4954 +- 0.1077   2888.0 +- 0.0
        CD4 Naive T cell      1.0 +- 0.0 0.0018 +- 0.002 0.0037 +- 0.004   3439.0 +- 0.0
       CD8 Memory T cell 0.0873 +- 0.014 0.6795 +- 0.2039 0.1533 +- 0.0238    818.0 +- 0.0
        CD8 Naive T cell 0.9851 +- 0.0051 0.504 +- 0.1136 0.6595 +- 0.1023   2047.0 +- 0.0
      Gamma-delta T cell 0.966 +- 0.0281 0.5865 +- 0.111 0.723 +- 0.0807   2544.0 +- 0.0
                    MAIT  0.5698 +- 0.13 0.8651 +- 0.0645 0.674 +- 0.0708    974.0 +- 0.0
           Memory B cell 0.5996 +- 0.0957 0.9615 +- 0.041 0.7335 +- 0.0688    897.0 +- 0.0
                 NK cell 0.9988 +- 0.0017 0.0953 +- 0.0747 0.1665 +- 0.122   2580.0 +- 0.0
            Naive B cell 0.9997 +- 0.0006 0.7249 +- 0.109 0.8361 +- 0.0757   2227.0 +- 0.0
             Plasma cell   0.4 +- 0.5164 0.0089 +- 0.0126 0.0174 +- 0.0245     56.0 +- 0.0
Plasmacytoid dendritic cell 0.6909 +- 0.4776 0.0596 +- 0.0609 0.1067 +- 0.1047     57.0 +- 0.0
       T regulatory cell 0.1158 +- 0.0914 0.075 +- 0.0807 0.0602 +- 0.0298    136.0 +- 0.0

                accuracy                                 0.5173 +- 0.033  22420.0 +- 0.0
               macro avg 0.6397 +- 0.0442 0.5291 +- 0.0125 0.4321 +- 0.0275  22420.0 +- 0.0
            weighted avg 0.8418 +- 0.009 0.5173 +- 0.033 0.5188 +- 0.0253  22420.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.4758 +- 0.0349
50% Random Dropout Accuracy: 0.2931 +- 0.0729
90% Random Dropout Accuracy: 0.1742 +- 0.0444
92.5% Random Dropout Accuracy: 0.1527 +- 0.0375
95% Random Dropout Accuracy: 0.1366 +- 0.046
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.5003 +- 0.0357
Feature importance dropout (0.5% features dropped) Accuracy score 0.4572 +- 0.0369
Feature importance dropout (1.0% features dropped) Accuracy score 0.4117 +- 0.0348
Feature importance dropout (2.0% features dropped) Accuracy score 0.2876 +- 0.0411


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.4026 +- 0.0258
50% Random Dropout Macro_F1: 0.2687 +- 0.0476
90% Random Dropout Macro_F1: 0.0701 +- 0.0252
92.5% Random Dropout Macro_F1: 0.0527 +- 0.0166
95% Random Dropout Macro_F1: 0.0387 +- 0.0151
Total samples: 22420.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.4213 +- 0.0284
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.3952 +- 0.0292
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.3533 +- 0.0248
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.2578 +- 0.0298



## Out of data distribution 

### Dataset Similarity + Accuracy 

Genes expected in training set: 10000
Genes actually matched in test set: 8693
Training data Max-Value: 8.634057
Test data Max-Value: 8.726716041564941
Baseline accuracy score 0.4304 +- 0.0585

### Classification Report 

                               precision          recall        f1-score         support

          CD14+ Monocyte 0.7564 +- 0.2353 0.9677 +- 0.0141 0.8281 +- 0.1741  12317.0 +- 0.0
          CD16+ Monocyte 0.9265 +- 0.0442 0.9842 +- 0.0104 0.9538 +- 0.0205   1903.0 +- 0.0
    CD1C+ dendritic cell 0.7076 +- 0.2118 0.9361 +- 0.0544 0.7826 +- 0.1412   1079.0 +- 0.0
       CD4 Memory T cell 0.3096 +- 0.0601 0.4265 +- 0.328 0.3123 +- 0.1709  14241.0 +- 0.0
        CD4 Naive T cell 0.2987 +- 0.481 0.0019 +- 0.0057 0.0037 +- 0.0113  17151.0 +- 0.0
       CD8 Memory T cell 0.0411 +- 0.0123 0.0992 +- 0.0546 0.0528 +- 0.0149   6650.0 +- 0.0
        CD8 Naive T cell 0.9902 +- 0.0052 0.3516 +- 0.1754 0.4975 +- 0.1789   6516.0 +- 0.0
      Gamma-delta T cell  0.0935 +- 0.02 0.2498 +- 0.0828 0.1356 +- 0.0333   2271.0 +- 0.0
                    MAIT 0.5116 +- 0.1034 0.9522 +- 0.0647 0.6563 +- 0.0744   2889.0 +- 0.0
           Memory B cell 0.6179 +- 0.0791 0.8684 +- 0.0664 0.7178 +- 0.0538   1395.0 +- 0.0
                 NK cell 0.9991 +- 0.002 0.3016 +- 0.2597 0.4076 +- 0.3107   5959.0 +- 0.0
            Naive B cell 0.9504 +- 0.0231 0.9666 +- 0.0174 0.9581 +- 0.0076   3385.0 +- 0.0
             Plasma cell   0.9 +- 0.3162 0.131 +- 0.1456 0.2067 +- 0.2152    930.0 +- 0.0
Plasmacytoid dendritic cell 0.8981 +- 0.3156 0.7283 +- 0.3353 0.7846 +- 0.3309    584.0 +- 0.0
       T regulatory cell      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0   1731.0 +- 0.0

                accuracy                                 0.4304 +- 0.0585  79001.0 +- 0.0
               macro avg 0.6001 +- 0.0445 0.531 +- 0.0403 0.4865 +- 0.0527  79001.0 +- 0.0
            weighted avg 0.5213 +- 0.0928 0.4304 +- 0.0585 0.386 +- 0.0536  79001.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

10% Random Dropout Accuracy: 0.4109 +- 0.0594
50% Random Dropout Accuracy: 0.3194 +- 0.0629
90% Random Dropout Accuracy: 0.203 +- 0.0453
92.5% Random Dropout Accuracy: 0.1957 +- 0.0402
95% Random Dropout Accuracy: 0.1758 +- 0.0393
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score 0.4278 +- 0.0589
Feature importance dropout (0.5% features dropped) Accuracy score 0.4251 +- 0.0589
Feature importance dropout (1.0% features dropped) Accuracy score 0.3994 +- 0.0553
Feature importance dropout (2.0% features dropped) Accuracy score 0.3759 +- 0.0522


### Further Robustness Evaluation with metric: Macro_F1 

10% Random Dropout Macro_F1: 0.4658 +- 0.0512
50% Random Dropout Macro_F1: 0.3051 +- 0.0594
90% Random Dropout Macro_F1: 0.0553 +- 0.0235
92.5% Random Dropout Macro_F1: 0.0492 +- 0.0232
95% Random Dropout Macro_F1: 0.0392 +- 0.0173
Total samples: 79001.0 +- 0.0
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score 0.4838 +- 0.0527
Feature importance dropout (0.5% features dropped) Macro_F1 score 0.4882 +- 0.0532
Feature importance dropout (1.0% features dropped) Macro_F1 score 0.4431 +- 0.0441
Feature importance dropout (2.0% features dropped) Macro_F1 score 0.4001 +- 0.0424


