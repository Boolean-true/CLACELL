# Robustness Evaluation 

## In distribution testset 

### Accuracy 

Baseline accuracy score: 0.8447 +- 0.0391

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9998 +- 0.0002 0.9971 +- 0.0058 0.9985 +- 0.0029   3129.0 +- 0.0
             CD4+ T cell 0.8322 +- 0.0261 0.9429 +- 0.0337 0.8834 +- 0.0152   6465.0 +- 0.0
             CD8+ T cell 0.7191 +- 0.093 0.7903 +- 0.0519 0.7498 +- 0.0551   6401.0 +- 0.0
          Dendritic cell 0.7968 +- 0.1021    0.9 +- 0.034 0.8416 +- 0.0641    165.0 +- 0.0
                Monocyte 0.9986 +- 0.0009 0.9888 +- 0.0082 0.9937 +- 0.0039   3648.0 +- 0.0
                 NK cell 0.7979 +- 0.2763 0.3385 +- 0.2946 0.4345 +- 0.3269   2582.0 +- 0.0
             Plasma cell 0.8774 +- 0.149 0.9964 +- 0.0075 0.9258 +- 0.1011     56.0 +- 0.0

                accuracy                                 0.8447 +- 0.0391  22446.0 +- 0.0
               macro avg 0.8602 +- 0.0491 0.8506 +- 0.0488 0.8324 +- 0.063  22446.0 +- 0.0
            weighted avg 0.8463 +- 0.0538 0.8447 +- 0.0391 0.8274 +- 0.053  22446.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8461 +- 0.0396
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8449 +- 0.0392
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8423 +- 0.0378
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8428 +- 0.0379
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8271 +- 0.0417


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8352 +- 0.0607
Number of inconsistent predictions: 0.0 +- 0.0
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8322 +- 0.0618
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8302 +- 0.0588
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8318 +- 0.0607
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8286 +- 0.0609



## Out of data distribution 

### OOD Dataset: OOD_HIHA_Pediatric 

Baseline accuracy score: 0.8996 +- 0.0336

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9991 +- 0.0019 0.9979 +- 0.0029 0.9985 +- 0.0016    866.0 +- 0.0
             CD4+ T cell 0.9709 +- 0.0118 0.9371 +- 0.0344 0.9532 +- 0.0153   4474.0 +- 0.0
             CD8+ T cell 0.7638 +- 0.0834 0.9481 +- 0.0221 0.8434 +- 0.0473   2688.0 +- 0.0
          Dendritic cell 0.8061 +- 0.1064 0.9892 +- 0.0056 0.8846 +- 0.0703    120.0 +- 0.0
                Monocyte 0.9981 +- 0.0008 0.965 +- 0.0276 0.9811 +- 0.0145    889.0 +- 0.0
                 NK cell 0.9168 +- 0.1632 0.376 +- 0.3364 0.465 +- 0.3598    876.0 +- 0.0
             Plasma cell 0.9635 +- 0.0445 0.9971 +- 0.009 0.9795 +- 0.0235     70.0 +- 0.0

                accuracy                                 0.8996 +- 0.0336   9983.0 +- 0.0
               macro avg 0.9169 +- 0.0286 0.8872 +- 0.0495 0.8722 +- 0.0596   9983.0 +- 0.0
            weighted avg 0.9132 +- 0.0296 0.8996 +- 0.0336 0.8866 +- 0.0445   9983.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.8998 +- 0.0329
Number of inconsistent predictions: 289.7 +- 128.1475
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9003 +- 0.0337
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8984 +- 0.0335
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8987 +- 0.0318
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8971 +- 0.0325


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8748 +- 0.0578
Number of inconsistent predictions: 289.7 +- 128.1475
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8722 +- 0.0593
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.871 +- 0.0593
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8721 +- 0.0566
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8702 +- 0.0567


### OOD Dataset: OOD_HIHA_Young_Adult 

Baseline accuracy score: 0.921 +- 0.027

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9977 +- 0.002 0.9968 +- 0.0058 0.9973 +- 0.0026    968.0 +- 0.0
             CD4+ T cell 0.9714 +- 0.0177 0.9485 +- 0.0299 0.9593 +- 0.0113   4371.0 +- 0.0
             CD8+ T cell 0.7749 +- 0.0932 0.9382 +- 0.0398 0.8446 +- 0.0471   2141.0 +- 0.0
          Dendritic cell 0.8607 +- 0.1007 0.9808 +- 0.009 0.9135 +- 0.0604    146.0 +- 0.0
                Monocyte 0.9985 +- 0.0009 0.9851 +- 0.0144 0.9917 +- 0.0072   1703.0 +- 0.0
                 NK cell 0.8106 +- 0.3326 0.366 +- 0.3616 0.4437 +- 0.3805    629.0 +- 0.0
             Plasma cell 0.9244 +- 0.0934 0.9525 +- 0.0381 0.9345 +- 0.0486     40.0 +- 0.0

                accuracy                                  0.921 +- 0.027   9998.0 +- 0.0
               macro avg 0.9054 +- 0.0654 0.8811 +- 0.052 0.8692 +- 0.063   9998.0 +- 0.0
            weighted avg 0.9245 +- 0.0322  0.921 +- 0.027 0.9107 +- 0.0353   9998.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9201 +- 0.0263
Number of inconsistent predictions: 226.2 +- 93.4247
Feature importance dropout (0.1% features dropped) Accuracy score: 0.9215 +- 0.0271
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9199 +- 0.0255
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9193 +- 0.0246
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9189 +- 0.0256


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8727 +- 0.0609
Number of inconsistent predictions: 226.2 +- 93.4247
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8701 +- 0.0626
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8681 +- 0.0616
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8691 +- 0.0604
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.869 +- 0.0619


### OOD Dataset: OOD_HIHA_Older_Adult 

Baseline accuracy score: 0.9079 +- 0.042

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9995 +- 0.0013 0.9982 +- 0.0058 0.9988 +- 0.0031    764.0 +- 0.0
             CD4+ T cell 0.982 +- 0.0111 0.9673 +- 0.0174 0.9744 +- 0.0062   4116.0 +- 0.0
             CD8+ T cell 0.6665 +- 0.1518 0.9426 +- 0.0365 0.771 +- 0.0921   1457.0 +- 0.0
          Dendritic cell 0.794 +- 0.1433 0.9826 +- 0.0158 0.8704 +- 0.0984    167.0 +- 0.0
                Monocyte 0.9988 +- 0.0011 0.9785 +- 0.0238 0.9884 +- 0.0122   2413.0 +- 0.0
                 NK cell 0.9359 +- 0.1337 0.3787 +- 0.3748 0.4565 +- 0.3769   1040.0 +- 0.0
             Plasma cell 0.9605 +- 0.0847      1.0 +- 0.0 0.978 +- 0.0482     40.0 +- 0.0

                accuracy                                 0.9079 +- 0.042   9997.0 +- 0.0
               macro avg 0.9053 +- 0.0384 0.8926 +- 0.0544 0.8625 +- 0.0724   9997.0 +- 0.0
            weighted avg 0.9334 +- 0.0284 0.9079 +- 0.042 0.8944 +- 0.0538   9997.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.9113 +- 0.0411
Number of inconsistent predictions: 193.5 +- 72.9067
Feature importance dropout (0.1% features dropped) Accuracy score: 0.908 +- 0.0419
Feature importance dropout (0.5% features dropped) Accuracy score: 0.9074 +- 0.0414
Feature importance dropout (1.0% features dropped) Accuracy score: 0.9075 +- 0.0398
Feature importance dropout (2.0% features dropped) Accuracy score: 0.9065 +- 0.0401


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8695 +- 0.0709
Number of inconsistent predictions: 193.5 +- 72.9067
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8624 +- 0.0722
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8632 +- 0.072
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.864 +- 0.0702
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8626 +- 0.07


### OOD Dataset: OOD_AIDA 

Baseline accuracy score: 0.8703 +- 0.0485

### Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9989 +- 0.0005 0.9996 +- 0.0014 0.9992 +- 0.0005    895.0 +- 0.0
             CD4+ T cell 0.9797 +- 0.0174 0.9567 +- 0.0253  0.9677 +- 0.01   2315.0 +- 0.0
             CD8+ T cell 0.6635 +- 0.1116 0.9613 +- 0.0392 0.7806 +- 0.0753   2127.0 +- 0.0
          Dendritic cell 0.8972 +- 0.1261 0.9192 +- 0.0474 0.9006 +- 0.0687    156.0 +- 0.0
                Monocyte 0.993 +- 0.0031 0.9917 +- 0.0141 0.9923 +- 0.0062   2614.0 +- 0.0
                 NK cell 0.7726 +- 0.3521 0.2541 +- 0.3049 0.3292 +- 0.3355   1363.0 +- 0.0
             Plasma cell 0.9712 +- 0.0316 0.9978 +- 0.0069 0.9842 +- 0.0192     46.0 +- 0.0

                accuracy                                 0.8703 +- 0.0485   9516.0 +- 0.0
               macro avg 0.8966 +- 0.0553 0.8686 +- 0.0492 0.8505 +- 0.0626   9516.0 +- 0.0
            weighted avg 0.8834 +- 0.067 0.8703 +- 0.0485 0.8431 +- 0.0659   9516.0 +- 0.0

### Further Robustness Evaluation with metric: Accuracy 

Random% Random Dropout Accuracy: 0.872 +- 0.0467
Number of inconsistent predictions: 163.1 +- 56.2957
Feature importance dropout (0.1% features dropped) Accuracy score: 0.8704 +- 0.0489
Feature importance dropout (0.5% features dropped) Accuracy score: 0.8696 +- 0.049
Feature importance dropout (1.0% features dropped) Accuracy score: 0.8681 +- 0.0464
Feature importance dropout (2.0% features dropped) Accuracy score: 0.8682 +- 0.046


### Further Robustness Evaluation with metric: Macro_F1 

Random% Random Dropout Macro_F1: 0.8539 +- 0.0603
Number of inconsistent predictions: 163.1 +- 56.2957
Feature importance dropout (0.1% features dropped) Macro_F1 score: 0.8507 +- 0.0628
Feature importance dropout (0.5% features dropped) Macro_F1 score: 0.8507 +- 0.0632
Feature importance dropout (1.0% features dropped) Macro_F1 score: 0.8489 +- 0.0598
Feature importance dropout (2.0% features dropped) Macro_F1 score: 0.8497 +- 0.0601


### OOD Dataset: All 

Baseline accuracy score: N/A

### Classification Report 

                               precision          recall        f1-score         support

                  B cell             N/A             N/A             N/A             N/A
             CD4+ T cell             N/A             N/A             N/A             N/A
             CD8+ T cell             N/A             N/A             N/A             N/A
          Dendritic cell             N/A             N/A             N/A             N/A
                Monocyte             N/A             N/A             N/A             N/A
                 NK cell             N/A             N/A             N/A             N/A
             Plasma cell             N/A             N/A             N/A             N/A

                accuracy                                             N/A             N/A
               macro avg             N/A             N/A             N/A             N/A
            weighted avg             N/A             N/A             N/A             N/A

### Further Robustness Evaluation with metric: Accuracy 



### Further Robustness Evaluation with metric: Macro_F1 



