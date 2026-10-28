# Work after the final presentation

## Submitted Jobs

### CLACELL scaled with higher Dropout

Submitted batch job 12247901
Submitted batch job 12248073
with_mean=False: Submitted batch job 12250932
Submitted batch job 12258795
Submitted batch job 12259209


### Combination of Conditional Autoencoder and Custom Ensemble

LinearSVC: Submitted batch job 12259451
Submitted batch job 12271675
Submitted batch job 12289115
Submitted batch job 12290233
Feature Importance auf den latenten Features: Submitted batch job 12299811
Run 9+: Submitted batch job 12355441
Feature Importance auf den Genen: Submitted batch job 12371296
Submitted batch job 12371388
Submitted batch job 12371389
Submitted batch job 12371390
2+: Submitted batch job 12376746
10+: Submitted batch job 12371398
12+: Submitted batch job 12376747
20+: Submitted batch job 12376883
30+: Submitted batch job 12376884
40+: Submitted batch job 12376885
50+: Submitted batch job 12376886

### Conditional Autoencoder without scaling

Submitted batch job 12390004
Submitted batch job 12390006
Submitted batch job 12390668

### Custom Ensemble

#### LinearSVC

Rejection Class: Submitted batch job 12399369

Stacking Classifier with Logistic Regression and no passthrough: Submitted batch job 12408410
Stacking Classifier with Logistic Regression and passthrough: Submitted batch job 12408460


### Reevaluation on new OOD Dataset

scGPT: Submitted batch job 1782007
CLACELL: Submitted batch job 12382944
CLACELL Conditional:
0+: Submitted batch job 12382998
10+: Submitted batch job 12382999
All have an Error with the batch_key in scrublet detection


### Reevaluation with combined training dataset

CLACELL Test: Submitted batch job 12416425

LinearSVC: Submitted batch job 12416428
Submitted batch job 12416429



NEW DATA
Submitted batch job 12416706
Submitted batch job 12417128

Cleaned v2
Submitted batch job 12420656


#### ML

LinearSVC: Submitted batch job 12420663
Submitted batch job 12420681
Submitted batch job 12420691 -> Done
Scaled: Submitted batch job 12420804
Submitted batch job 12421088
Submitted batch job 12421090 -> canceled after 5 Runs (sufficient data)
Run 10+: Submitted batch job 12421105 -> canceled after 4 Runs (sufficient data)
Run 20+: Submitted batch job 12421106 -> canceled after 4 Runs (sufficient data)
The chosen 10 runs are: 0,1,2,3,4,20 as 5,21 as 6,22 as 7,23 as 8,13 as 9
Access runs: 10,12,13

Random Forest: Submitted batch job 12420668
Submitted batch job 12420672
Submitted batch job 12420682
Scaled: Submitted batch job 12420806
Submitted batch job 12421092
Submitted batch job 12421099
Run 10+: Submitted batch job 12421108
Run 20+: Submitted batch job 12421109

Logistic Regression: Submitted batch job 12420673
Submitted batch job 12420683 -> one run after 9 hours
Run 0+: Submitted batch job 12421087
Submitted batch job 12421089
Scaled: Submitted batch job 12420803
Submitted batch job 12420805
Submitted batch job 12421091
Submitted batch job 12421097
Run 10+: Submitted batch job 12421111
Run 20+: Submitted batch job 12421112

ExtraTrees: Submitted batch job 12420675
Submitted batch job 12420684
Scaled: Submitted batch job 12420807
Submitted batch job 12421093
Submitted batch job 12421100
Run 10+: Submitted batch job 12421118
Run 20+: Submitted batch job 12421119

LightGBM: Submitted batch job 12420676
Submitted batch job 12420680
Run 10+: Submitted batch job 12421095
Run 20+: Submitted batch job 12421096
Scaled: Submitted batch job 12420808
Submitted batch job 12421094
Submitted batch job 12421098
Run 10+: Submitted batch job 12421116
Run 20+: Submitted batch job 12421117

TODO: Bei den scaled ML Algorithmen neue evaluieren, weil die id test daten nicht skaliert wurden! einfach X_train und X_test mit den skalierten Werten überschreiben (siehe custom ensemble linearsvc scaled)

#### Reference Models

CellTypist: Submitted batch job 12420700
Submitted batch job 12421113
Run 10+: Submitted batch job 12420719
Submitted batch job 12421114
Run 20+: Submitted batch job 12420720
Submitted batch job 12421115

SingleR: Submitted batch job 12420763

scGPT: Submitted batch job 1790377
Submitted batch job 1790390
Submitted batch job 1790443
Submitted batch job 1790467
Submitted batch job 1790474
Submitted batch job 1790497
Submitted batch job 1790542
Submitted batch job 1790740
torchtext copied from python 3.12 env: Submitted batch job 1790752
Submitted batch job 1790776
Submitted batch job 1790801
Submitted batch job 1790813
own python 3.12 env: Submitted batch job 1790859
Submitted batch job 1790886
Submitted batch job 1790930
Submitted batch job 1791019
Submitted batch job 1794197
Run 10+: Submitted batch job 1791156
Submitted batch job 1794198
Run 20+: Submitted batch job 1791157
Submitted batch job 1794199


#### Ensembles and Autoencoder

AE LinSVC: Submitted batch job 12420723

AE LR: Submitted batch job 12420726

AE RF: Submitted batch job 12420733
Run 10+: Submitted batch job 12420735

CAE LinSVC: Submitted batch job 12420745
Run 10+: Submitted batch job 12421120
Run 20+: Submitted batch job 12421121

CAE LR: Submitted batch job 12420746

CAE RF: Submitted batch job 12420749
Run 10+: Submitted batch job 12420751
Run 20+: Submitted batch job 12420752


AB HIER WARTEN AUF HYPERPARAMETER AUS ML
CE LinSVC: Submitted batch job 12421169
Submitted batch job 12421170
Submitted batch job 12421175
Scaled: Submitted batch job 12421186

CE LR: TODO

CE RF: TODO


CE LinSVC with refined cell types: Submitted batch job 12425203
with ood test prints: Submitted batch job 12427077
fixed confusion matrix: Submitted batch job 12427131
Submitted batch job 12427345
ood tests and fixed t reg cells: Submitted batch job 12427095
fixed confusion matrix: Submitted batch job 12427132
Submitted batch job 12427346


Analyze ovarian dataset: Submitted batch job 12430763
Submitted batch job 12430765
Improved script: Submitted batch job 12436203
Submitted batch job 1501706 on cluster tinyfat
Submitted batch job 1501708 on cluster tinyfat
Submitted batch job 1501712 on cluster tinyfat
Submitted batch job 1501725 on cluster tinyfat
Submitted batch job 1501740 on cluster tinyfat
Submitted batch job 1501750 on cluster tinyfat

breast: Submitted batch job 1501707 on cluster tinyfat
Submitted batch job 1501709 on cluster tinyfat
Submitted batch job 1501711 on cluster tinyfat
Submitted batch job 1501726 on cluster tinyfat

Downsample adata to spatial: Submitted batch job 12430766
Submitted batch job 12430767
Submitted batch job 12430768
Submitted batch job 12430783 -> success but no genes
without preprocessing: Submitted batch job 12431151
Submitted batch job 12431154
Submitted batch job 12434162
Submitted batch job 12434555
Submitted batch job 1501700 on cluster tinyfat
Submitted batch job 1501701 on cluster tinyfat
With Sparse matrix: Submitted batch job 1501794 on cluster tinyfat
Convert dense matrix to sparse at the end: Submitted batch job 1501804 on cluster tinyfat

Downsample breast to spatial: Submitted batch job 1501702 on cluster tinyfat
With Sparse matrix: Submitted batch job 1501795 on cluster tinyfat
Convert dense matrix to sparse at the end: Submitted batch job 1501805 on cluster tinyfat

CE Spatial (mit estimated split): Submitted batch job 12430769
Submitted batch job 12430770
with loading of spatial data: Submitted batch job 12431134
Submitted batch job 12431148
Submitted batch job 12431150
Submitted batch job 12431153
Submitted batch job 12436198
Submitted batch job 12438030

CE Spatial with fixed dataset: Submitted batch job 12439870
Submitted batch job 12439955

CE Spatial Ovary with limited train and test data: Submitted batch job 12445475
Submitted batch job 12447198
Fixed robustness_result return in test_robustness: Submitted batch job 12447248


### Reevaluation with refined cell types

#### ML

LinearSVC: Submitted batch job 12435834
Submitted batch job 12436225
Submitted batch job 12436781
Submitted batch job 12438031
Scaled: Submitted batch job 12435835
Submitted batch job 12438039

RandomForest: Submitted batch job 12435836
Submitted batch job 12439082
Scaled: Submitted batch job 12435837
Submitted batch job 12439083

LogisticRegression: Submitted batch job 12435838
Submitted batch job 12438876
Run 2+: Submitted batch job 12440803
Run 3+: Submitted batch job 12441342
Run 10+: Submitted batch job 12439975
Run 20+: Submitted batch job 12440804
Run 30+: Submitted batch job 12440805
Scaled: Submitted batch job 12435839
Submitted batch job 12438877
Run 2+: Submitted batch job 12440806
Run 10+: Submitted batch job 12439240
Run 20+: Submitted batch job 12440808
Run 30+: Submitted batch job 12440810

ExtraTrees: Submitted batch job 12435840
Submitted batch job 12439084
Run 7+: Submitted batch job 12440795
Scaled: Submitted batch job 12435841
Submitted batch job 12439085
Run 7+: Submitted batch job 12440796

LightGBM: Submitted batch job 12435842
Run 10+: Submitted batch job 12435845
Submitted batch job 12439065
Run 1+: Submitted batch job 12440812
Run 10+: Submitted batch job 12439241
Run 12+: Submitted batch job 12441176
Run 20+: Submitted batch job 12440813
Run 30+: Submitted batch job 12440824
Run 40+: Submitted batch job 12440825
Scaled: Submitted batch job 12435843
Run 10+: Submitted batch job 12435846
Submitted batch job 12439066
Run 1+: Submitted batch job 12440814
Run 10+: Submitted batch job 12439242
Run 12+: Submitted batch job 12441177
Run 20+: Submitted batch job 12440815
Run 30+: Submitted batch job 12440826
Run 40+: Submitted batch job 12440827

#### Reference Models

scGPT: Submitted batch job 1797244
Submitted batch job 1797531
Run 10+: Submitted batch job 1797245
Submitted batch job 1797540
Run 20+: Submitted batch job 1797246
Submitted batch job 1797541
Batch size 32: Submitted batch job 1798245
Batch size 48: Submitted batch job 1798255
Submitted batch job 1798525
With -u flag: Submitted batch job 1800036
With -u flag and 48 batch size: Submitted batch job 1800034

CellTypist: Submitted batch job 12439962
Run 1+: Submitted batch job 12441339
Run 10+: Submitted batch job 12439963
Run 11+: Submitted batch job 12441340
Run 20+: Submitted batch job 12439964
Run 22+: Submitted batch job 12441341

SingleR: Submitted batch job 12439971

#### Autoencoders + Ensembles

AE LinSVC: Submitted batch job 12439980
Run 10+: Submitted batch job 12440820

AE LR: Submitted batch job 12439981
Run 1+: Submitted batch job 12441354

AE RF: Submitted batch job 12439982
Run 4+: Submitted batch job 12441350
Run 10+: Submitted batch job 12439983

CAE LinSVC: Submitted batch job 12439991
Run 10+: Submitted batch job 12440821
Run 20+: Submitted batch job 12440822

CAE LR: Submitted batch job 12439992

CAE RF: Submitted batch job 12439993

CE LinSVC: Submitted batch job 12441263
Submitted batch job 12441336
Scaled: Submitted batch job 12441271

CE LinSVC Stacking: Submitted batch job 12441901

CE LinSVC Stacking Passthrough: Submitted batch job 12441902


### Reevaluation with more OOD Datasets

#### ML

LinearSVC: Submitted batch job 12461532
Submitted batch job 12462093
Submitted batch job 12465947
Submitted batch job 12469861
Submitted batch job 12471863
With adjusted doublet detection: Submitted batch job 12472382
Submitted batch job 12473235
With raw counts for all ood datasets: Submitted batch job 12473684
With gene symbols in AIDA Dataset: Submitted batch job 12480774
Scaled: Submitted batch job 12462097
Submitted batch job 12469908
Submitted batch job 12474131
Submitted batch job 12481038
Fixed scaling for ID: Submitted batch job 12496671

RandomForest: Submitted batch job 12461877
Submitted batch job 12469905
Submitted batch job 12474135
Submitted batch job 12480926
Run 10+: Submitted batch job 12474193
Scaled: Submitted batch job 12462098
Submitted batch job 12469914
Submitted batch job 12474136
Submitted batch job 12480927
Fixed scaling for ID: Submitted batch job 12496673
Run 10+: Submitted batch job 12462133
Submitted batch job 12474194

ExtraTrees: Submitted batch job 12461908
Submitted batch job 12469915
Submitted batch job 12474142 -> abgebrochen, da ich ausreichend Ergebnisse habe
Submitted batch job 12480924
Run 10+: Submitted batch job 12474265 -> abgebrochen, da ich ausreichend Ergebnisse habe
Scaled: Submitted batch job 12462104
Submitted batch job 12469916
Submitted batch job 12474143 -> abgebrochen, da ich ausreichend Ergebnisse habe
Submitted batch job 12480925
Fixed scaling for ID: Submitted batch job 12496674
Run 10+: Submitted batch job 12462140
Submitted batch job 12474266 -> abgebrochen, da ich ausreichend Ergebnisse habe

LogisticRegression: Submitted batch job 12461924
Submitted batch job 12469921
Submitted batch job 12474146
Submitted batch job 12480903 -> abgebrochen, da ich ausreichend Ergebnisse habe
Run 10+: Submitted batch job 12461955
Submitted batch job 12469922
Submitted batch job 12474147
Submitted batch job 12480904 -> abgebrochen, da ich ausreichend Ergebnisse habe
Run 20+: Submitted batch job 12461956
Submitted batch job 12469929
Submitted batch job 12474148
Submitted batch job 12480905 -> abgebrochen, da ich ausreichend Ergebnisse habe
Run 30+: Submitted batch job 12469930
Submitted batch job 12474149
Submitted batch job 12480906 -> abgebrochen, da ich ausreichend Ergebnisse habe
Run 40+: Submitted batch job 12474308
Submitted batch job 12480907 -> abgebrochen, da ich ausreichend Ergebnisse habe
Scaled: Submitted batch job 12462105
Submitted batch job 12470023
Submitted batch job 12474152
Submitted batch job 12480909 -> abgebrochen, da ich ausreichend Ergebnisse habe
Fixed scaling for ID: Submitted batch job 12496677
Run 10+: Submitted batch job 12462106
Submitted batch job 12470024
Submitted batch job 12474156
Submitted batch job 12480910 -> abgebrochen, da ich ausreichend Ergebnisse habe
Fixed scaling for ID: Submitted batch job 12496678
Run 20+: Submitted batch job 12462107
Submitted batch job 12470025
Submitted batch job 12474157
Submitted batch job 12480911 -> abgebrochen, da ich ausreichend Ergebnisse habe
Fixed scaling for ID: Submitted batch job 12496679
Run 30+: Submitted batch job 12474313
Submitted batch job 12480912 -> abgebrochen, da ich ausreichend Ergebnisse habe
Fixed scaling for ID: Submitted batch job 12496936
Run 40+: Submitted batch job 12474314
Submitted batch job 12480913 -> abgebrochen, da ich ausreichend Ergebnisse habe
Fixed scaling for ID: Submitted batch job 12496937

LightGBM: Submitted batch job 12461937
Submitted batch job 12470063
Submitted batch job 12474321 -> abgebrochen, da ich ausreichend Ergebnisse habe
Submitted batch job 12480914 -> abgebrochen, da ich ausreichend Ergebnisse habe
Run 10+: Submitted batch job 12461982
Submitted batch job 12470064
Submitted batch job 12474322 -> abgebrochen, da ich ausreichend Ergebnisse habe
Submitted batch job 12480915 -> abgebrochen, da ich ausreichend Ergebnisse habe
Run 20+: Submitted batch job 12461983
Submitted batch job 12470065
Submitted batch job 12474323 -> abgebrochen, da ich ausreichend Ergebnisse habe
Submitted batch job 12480916 -> abgebrochen, da ich ausreichend Ergebnisse habe
Run 30+: Submitted batch job 12461986
Submitted batch job 12470066
Submitted batch job 12474324 -> abgebrochen, da ich ausreichend Ergebnisse habe
Submitted batch job 12480917 -> abgebrochen, da ich ausreichend Ergebnisse habe
Run 40+: Submitted batch job 12474338 -> abgebrochen, da ich ausreichend Ergebnisse habe
Submitted batch job 12480918 -> abgebrochen, da ich ausreichend Ergebnisse habe
Scaled: Submitted batch job 12462113
Submitted batch job 12470072
Submitted batch job 12474327 -> abgebrochen, da ich ausreichend Ergebnisse habe
Submitted batch job 12480919 -> abgebrochen, da ich ausreichend Ergebnisse habe
Fixed scaling for ID: Submitted batch job 12496680
Run 10+: Submitted batch job 12462114
Submitted batch job 12470073
Submitted batch job 12474328 -> abgebrochen, da ich ausreichend Ergebnisse habe
Submitted batch job 12480920 -> abgebrochen, da ich ausreichend Ergebnisse habe
Fixed scaling for ID: Submitted batch job 12496681
Run 20+: Submitted batch job 12462115
Submitted batch job 12470074
Submitted batch job 12474329 -> abgebrochen, da ich ausreichend Ergebnisse habe
Submitted batch job 12480921 -> abgebrochen, da ich ausreichend Ergebnisse habe
Fixed scaling for ID: Submitted batch job 12496682
Run 30+: Submitted batch job 12462116
Submitted batch job 12470075
Submitted batch job 12474330 -> abgebrochen, da ich ausreichend Ergebnisse habe
Submitted batch job 12480922 -> abgebrochen, da ich ausreichend Ergebnisse habe
Run 40+: Submitted batch job 12474339 -> abgebrochen, da ich ausreichend Ergebnisse habe
Submitted batch job 12480923 -> abgebrochen, da ich ausreichend Ergebnisse habe


#### Autoencoders and Ensembles

AE LinSVC: Submitted batch job 12481212
Run 10+: Submitted batch job 12481217

AE RF: Submitted batch job 12481213
Run 4+: Submitted batch job 12488466 -> abgebrochen, da ich ausreichend Ergebnisse habe
Run 10+: Submitted batch job 12481216

CAE LinSVC: Submitted batch job 12481214
Run 10+: Submitted batch job 12481218 -> abgebrochen, da ich ausreichend Ergebnisse habe
Run 20+: Submitted batch job 12481219 -> abgebrochen, da ich ausreichend Ergebnisse habe

CAE RF: Submitted batch job 12481215
Run 10+: Submitted batch job 12481220 -> abgebrochen, da ich ausreichend Ergebnisse habe
Run 20+: Submitted batch job 12481221 -> abgebrochen, da ich ausreichend Ergebnisse habe

CE LinSVC: Submitted batch job 12484438
Scaled: Submitted batch job 12484439

CE RF: Submitted batch job 12487651
Submitted batch job 12488467
Scaled: Submitted batch job 12487652
Submitted batch job 12488468
Fixed ID scaling: Submitted batch job 12508958

CE LinSVC Stacking: Submitted batch job 12487501
Scaled: Submitted batch job 12496666

CE LinSVC Stacking Passthrough: Submitted batch job 12487503
Scaled: Submitted batch job 12496667

CE RF Stacking: Submitted batch job 12496634
Scaled: Submitted batch job 12496668

CE RF Stacking Passthrough: Submitted batch job 12496635
Scaled: Submitted batch job 12496669

CAE CE LinSVC Gene Drop: Submitted batch job 12487558
10+: Submitted batch job 12487559
20+: Submitted batch job 12487560
30+: Submitted batch job 12487562
Submitted batch job 12492923
40+: Submitted batch job 12488469
50+: Submitted batch job 12488470
60+: Submitted batch job 12492924
70+: Submitted batch job 12492925
80+: Submitted batch job 12492926
90+: Submitted batch job 12492927


#### Reference Models

CellTypist: Submitted batch job 12474465
Submitted batch job 12480928 -> abgebrochen, da ich ausreichend Ergebnisse habe
Run 10+: Submitted batch job 12474466
Submitted batch job 12480929 -> abgebrochen, da ich ausreichend Ergebnisse habe
Run 20+: Submitted batch job 12474467
Submitted batch job 12480930 -> abgebrochen, da ich ausreichend Ergebnisse habe

scGPT: Submitted batch job 1805719 -> abgebrochen, da ich ausreichend Ergebnisse habe
Run 10+: Submitted batch job 1805720 -> abgebrochen, da ich ausreichend Ergebnisse habe
Run 20+: Submitted batch job 1805721 -> abgebrochen, da ich ausreichend Ergebnisse habe

SingleR: Submitted batch job 12481222



CLACELL complete Pipeline: Submitted batch job 12487666


### Coarse Labels

#### ML

LinearSVC: Submitted batch job 12498398
Scaled: Submitted batch job 12498404

Random Forest: Submitted batch job 12498405
Scaled: Submitted batch job 12498406

ExtraTrees: Submitted batch job 12498407
Scaled: Submitted batch job 12498408

LogisticRegression: Submitted batch job 12498409
Run 10+: Submitted batch job 12498410
Run 20+: Submitted batch job 12498411
Scaled: Submitted batch job 12498412
Run 10+: Submitted batch job 12498413
Run 20+: Submitted batch job 12498414

LightGBM: Submitted batch job 12498415
Run 10+: Submitted batch job 12498416
Run 20+: Submitted batch job 12498417
Scaled: Submitted batch job 12498418
Run 10+: Submitted batch job 12498419
Run 20+: Submitted batch job 12498420


#### AE, CAE and Ensembles

AE LinSVC: Submitted batch job 12499862
Run 10+: Submitted batch job 12500887

AE RF: Submitted batch job 12499863
Run 10+: Submitted batch job 12500888

CAE LinSVC: Submitted batch job 12499864
Run 10+: Submitted batch job 12500890

CAE RF: Submitted batch job 12499865
Run 10+: Submitted batch job 12500891

CE LinSVC: Submitted batch job 12508545
Scaled: Submitted batch job 12508796

CE LinSVC Stacking: Submitted batch job 12508797
Scaled: Submitted batch job 12508855

CE LinSVC Stacking Passthrough: Submitted batch job 12508798
Scaled: Submitted batch job 12508856

CE RF: Submitted batch job 12513495
Scaled: Submitted batch job 12513498

CE RF Stacking: Submitted batch job 12513496
Scaled: Submitted batch job 12513499

CE RF Stacking Passthrough: Submitted batch job 12513497
Scaled: Submitted batch job 12513500


CAE CE LinSVC Gene Drop: Submitted batch job 12499871
Run 10+: Submitted batch job 12499872
Run 20+: Submitted batch job 12499873
Run 30+: Submitted batch job 12500893
Run 40+: Submitted batch job 12500894
Run 50+: Submitted batch job 12500895
Run 60+: Submitted batch job 12500896
Run 70+: Submitted batch job 12500897
Run 80+: Submitted batch job 12500898
Run 90+: Submitted batch job 12500899


#### Reference Models

CellTypist: Submitted batch job 12499868
Run 10+: Submitted batch job 12499869

SingleR: Submitted batch job 12499870

scGPT: Submitted batch job 1814932
Run 10+: Submitted batch job 1814933
Run 20+: Submitted batch job 1814934


#### Spatial

##### Ovary

CE RF Stacking: Submitted batch job 12541443
Submitted batch job 12541545
Submitted batch job 12541739
Submitted batch job 12542542
Submitted batch job 12542637

##### Breast

CE RF Stacking: Submitted batch job 12542461
Submitted batch job 12542541
Submitted batch job 12542636
Full set of Donors: Submitted batch job 12542819

Hierarchical CE RF Stacking: Submitted batch job 12681033
Submitted batch job 12686777
Submitted batch job 12691025

Hierarchical CE RF Stacking Entropy Rejection: Submitted batch job 12695458

Hierarchical CE RF Stacking PyOD: Submitted batch job 12695975
Hierarchical CE RF Stacking PyOD Entropy: Submitted batch job 12699725

Hierarchical CE RF Stacking Ensemble Disagreement Rejection: Submitted batch job 12696824
0.9 Quantile: Submitted batch job 12700423

Hierarchical Catboost: Submitted batch job 12726472
Submitted batch job 12728551
Submitted batch job 12731469

##### Tonsil

Downsample to spatial: Submitted batch job 1540082 on cluster tinyfat
Submitted batch job 1540084 on cluster tinyfat
Submitted batch job 1540092 on cluster tinyfat -> Erfolg mit nucleus_gene_stats_2
Submitted batch job 1540107 on cluster tinyfat

CE RF Stacking (auf annotation_figure_1): Submitted batch job 12546674
Submitted batch job 12546745
min: 30.0
median: 232.0
mean: 270.01144366197184
max: 2492.0

CE RF Stacking (mit gene_stats_2 und auf annotation_figure_1): Submitted batch job 12547237


EVALUIERUNGSTEST ob robustness tests nach anpassung von spatial daten noch mit den anderen methoden gehen: Submitted batch job 12546690 -> geht noch

### Hierarchical (both coarse and fine grained)

CE RF Stacking: Submitted batch job 12613800
Submitted batch job 12614506


### Annotation

#### Human Immune Health Atlas

60.000 Samples: Submitted batch job 1494795 on cluster tinyfat
Submitted batch job 1494796 on cluster tinyfat
Submitted batch job 1494797 on cluster tinyfat
Submitted batch job 1494798 on cluster tinyfat
Submitted batch job 1494800 on cluster tinyfat
Submitted batch job 1494801 on cluster tinyfat
Submitted batch job 1494803 on cluster tinyfat
doublet detection without batch: Submitted batch job 1494804 on cluster tinyfat
[:60000] statt [6000]: 0Submitted batch job 1494805 on cluster tinyfat
Submitted batch job 1494806 on cluster tinyfat
50.000 Samples: Submitted batch job 1494811 on cluster tinyfat
40.000 Samples: Submitted batch job 1494815 on cluster tinyfat
30.000 Samples: Submitted batch job 1494825 on cluster tinyfat
30.000 Samples + DC und Plasma: Submitted batch job 1496045 on cluster tinyfat
Submitted batch job 1496868 on cluster tinyfat

Test with improved memory and runtime: Submitted batch job 1498144 on cluster tinyfat
100.000 Samples: Submitted batch job 1498161 on cluster tinyfat
90.000 Samples: Submitted batch job 1498164 on cluster tinyfat
80.000 Samples: Submitted batch job 1498182 on cluster tinyfat


With more NK Cells:
80.000 Samples: Submitted batch job 1498369 on cluster tinyfat
Submitted batch job 1498371 on cluster tinyfat
75.000 Samples: Submitted batch job 1498372 on cluster tinyfat

Coarse Labels (nutzt als Basis human_immune_health_atlas_full_annotated_fine_grained_cleaned.h5ad)
Submitted batch job 1505134 on cluster tinyfat
Submitted batch job 1505572 on cluster tinyfat
Submitted batch job 1505635 on cluster tinyfat
Submitted batch job 1505674 on cluster tinyfat


#### Human Cell Atlas

80.000 Samples: Submitted batch job 1498209 on cluster tinyfat
Submitted batch job 1498210 on cluster tinyfat
Submitted batch job 1498214 on cluster tinyfat
Submitted batch job 1498215 on cluster tinyfat
70.000 Samples: Submitted batch job 1498241 on cluster tinyfat
60.000 Samples: Submitted batch job 1498257 on cluster tinyfat
50.000 Samples: Submitted batch job 1498266 on cluster tinyfat

Fixed:
80.000 Samples: Submitted batch job 1498295 on cluster tinyfat
70.000 Samples: Submitted batch job 1498311 on cluster tinyfat
60.000 Samples: Submitted batch job 1498312 on cluster tinyfat
50.000 Samples: Submitted batch job 1498314 on cluster tinyfat
40.000 Samples: Submitted batch job 1498324 on cluster tinyfat -> Success

More Donors:
40.000 Samples: Submitted batch job 1498361 on cluster tinyfat

#### CellTypist Dataset

Submitted batch job 1498283 on cluster tinyfat
Submitted batch job 1498293 on cluster tinyfat
Submitted batch job 1498294 on cluster tinyfat

#### AIDA

Fine Grained: Submitted batch job 1505731 on cluster tinyfat
Submitted batch job 1505732 on cluster tinyfat
Submitted batch job 1505734 on cluster tinyfat



## Todo
- AIDA Datensatz
- Annes Datensatz
- Marker gene aus Github verwenden

Optimierungen beim Annotieren
X- PCA nur einmal für je hvg und nicht hvg
X- knn nur viermal (ergebnisse abspeichern) (einmal pro pca und parameter)
Meine Ideen
X- tsne evtl entfernen, ist ja nur zur Visualisierung da, die ich nicht mache
=> 1h36min->17min, 322GB->235GB

Spatial
- Wir betrachten erstmal nur 2um spatial daten (subzellular) und klassifizieren das

Weitere Tests
- Kein Scaling vor CAE
- Rejection Class
- Reevaluierung aller Algorithmen auf $WORK
- Metriken in Robustnesstests von Accuracy auf F1 Score ändern
- Custom Ensemble mit mehreren Modellen
- Custom Ensemble mit Stacking (passthrough mit False und True testen!)

Donnerstag
X- ergebnisse von cae ohne scaling anschauen
- annotation
X- rejection class ergebnisse anschauen


## Gespräch am 21.08.

- Paper in Overlea reinkopieren
- 10x-visium enthält die datensätze
- modelle werden auf scrna seq datensätze trainiert und wir zeigen, wenn man auf spatial daten runterskaliert sind wir noch besser als die Vergleichsmodelle
- Datensätze in 10x-visium sind zum abschätzen wie sparse die spatial daten sind
- training auf 10x-gex datensätzen
- ABER noch für alle anderen 5 datensätze in 10x-visium ein pendant in scrna seq finden und verwenden. Alle 6 Datensätze dann zusammen als Trainingsdatensatz erstellen

schritt 1: wie gut können wir einzelne tissues klassifizieren? (6 Datensätze)
schritt 2: auf spatial daten runtersamplen und dann classifier trainieren


was ich mir überlegen kann in bezug auf modelltraining: trainingsmodus mit uniform dropout für spatial daten. Eigenen Downsampler anbieten (bereits testen, nur 10%, 5%, 2% der Datenpunkte nehmen (random runtergesampled), evaluieren wie gut das modell dann ist)

preprocessing auf spatial daten anpassen mit weniger genen (evtl nur 1.000 gene)

NEUEN OOD DATENSATZ VERWENDEN wegen scGPT


PAPER
in methods viele technische details (scheint aber nicht so schlimm zu sein, Anne hat sie nicht wieder gefunden)


vor training annotationen checken
- umap plotten
- gene mit clustern vergleichen
- datensätze evtl kombinieren (früherer OOD und ID)


compute normalization target sum noch auf dem merged datensatz zum checken ob dort nur rohdaten drin sind


### Neu Evaluieren

#### ML

- LinearSVC
- LogisticRegression
- ExtraTrees?
- Random Forest
- LightGBM?



## Aufgaben

### TODOs vor Reevaluierung

X- Robustness Tests zusätzlich noch mit F1-Score

### Reevaluierung auf fine-grained

- ML
    X- LinSVC
    - LR
    X- RF
    X- ExtraTrees
    - LightGBM
- Custom Ensemble (auch Stacking)
- Autoencoder
- Referenzmodelle (scGPT und SingleR hier auch ohne Anpassung)

### Spatial

- Downsampling durchlesen und gegebenenfalls anpassen

#### Ovary


#### Breast
#### Tonsil
#### Pancreas




## Mitschrieb vom 1.9.

weiteren OOD Testdatensatz, evtl AIDA. Anne schaut sich AIDA an

Bestehenden OOD Datensatz aufteilen in drei Altersstufen Pediatric, Young Adult und Adult !!!
Bestehenden OOD evtl runtersamplen wenn AIDA dazukommt
Test Script anpassen auf mehrere OOD Datensätze

Evtl Weitere Option biem Package mit alle subclassifier trainieren

Coarse grained auch noch evaluieren auf neuen Datensätzen

kleineren run für spaptial (subsamplen) bis es läuft

tonsil müsste bei spatial auch gehen. layer counts für Rohdaten

Bei Marker genen bei ? bei spatial die letzte Spalte nehmen, wenn kein Wert da drin ist, dann das Gen verwerfen

evtl plots für die ood datensätze nach modell und nicht nach ood datensatz, also ein plot für linsvc mit unterschiedlichen ood datensätzen


Poster:
- Eher Plots, kaum Text
- Man kann auch Informationen aufbringen, die eine Erklärung benötigen, da ich ja neben dem Poster stehe. Also muss nicht alles auf dem Poster erklärt werden
- Ergebnisse zuerst (als interessantestes; ganz oben), Architektur weiter unten für Interessierte



IDENTIFIZIERTE PROBLEME, die vor einem Retraining behoben werden müssen:
X- scGPT hat im id datensatz 3552 gene, custom ensemble hat dort 4141 gene. matchende gene im ood datensatz: 945 (scGPT) vs 1091 (custom ensemble) -> wahrscheinlich kommt das daher, dass vor HVG Selection bei scGPT nur die Gene herausgefiltert werden, die in seinem Vokabular sind
X- beim Random Dropout mit höherem Dropout werden im OOD Datensatz viel zu viele Gene entfernt, sodass keine mehr übrig sind (also alle auf 0 sind) -> man muss darauf schauen, dass noch gene mit werten übrig sind (sowohl bei sccGPT als auch bei anderen Modelen, die müssten dasselbe Problem haben!!)
    X-> Random Dropout nur noch mit 10%
    X-> beim Random Dropout nur noch Gene >0 droppen
    X-> beim Feature Importance Dropout nur Gene aus der Feature Importance wählen, die >0 sind
X- OOD Datensatz anpassen
    X- ausschließlich die author annotation verwenden, diese aber auf meine Zelltypen mappen und filtern
    X- human immune health atlas splitten nach Altersgruppe
    X- jede der vier OOD Datensätze soll 10.000 Zellen haben mit 3-5 Donors, ideal 4 Donors. die Zellen werden gleichmäßig auf die Donors aufgeteilt, sodass jeder Donor noch jeden Zelltyp hat (stratified split)
X- Robustness Tests anpassen
    X- Robustness Tests anpassen auf vier einzelne OOD Datensätze
    ABGELEHNT- Robustness Tests confusion matrix in results mit abspeichern
    X- Robustness Tests anpassen, damit die Mean + Varianz bei F1 über verschiedene Donor hinweg mit gespeichert wird
- CellTypist Robustness Tests habe ich bei run 2 nicht angepasst, das sind noch die alten!!
- Trainings-Scripte anpassen
    - Test robustness mit neuer Signatur (mehr OOD Datensätze, neue Feature Importance, Donor col ID, neue label obs)
    - Neuen Trainingsdatensatz nehmen
    - Labels updaten
    - rohcounts benutzen!:
# Use raw data instead of already preprocessed data
adata.X = adata.layers['counts'].copy()
X- Feature Importance Dropout evtl die verwendete Feature Importance updaten, die ist mittlerweile veraltet

- Bei Spatial evtl eine neue Feature Importance machen?!
X- Coarse Labels bei ID Datensatz auch mit mergen der fine grained labels holen



## TODOs

X- scaled für alle ML nochmal prüfen, ob ID jetzt passt
X- scaled für CEs evaluieren
X- CE scaled stacking passthrough und kein passthrough bei sowohl rf als auch linsvc hatten falsche hyperparameter bei fine grained -> neu evaluieren
X- CE RF Scaled (nicht Stacking, nur normal scaled) hatte bei ID Dataset kein scaling -> gefixter run gestartet, danach die Evaluation auf coarse labels machen
- weiteres Modell für CE?
X- Hierarchischer Classifier
- Rejection class

X- Coarse Labels evaluieren
X- CE bei Coarse

- scGPT und SingleR ohne meine Optimierungen laufen lassen

- beste Modelle sowie Referenzmodelle auf Spatial laufen lassen



## Weiteres Vorgehen (Gespräch am 13.10.)

- mein vorgehen mit der klasse um alles zu trainieren (dreiteilig) sieht gut aus
- anne hat sich daten angeschaut
    - der breast datensatz besteht aus unterschiedlichen einzeldatensätzen, wenn ich dann mit dem donor split welche entferne, kann ich nicht mehr gut vorhersagen. Daher malignant cells rauslassen. evtl schauen ob ich die donor liste für train und test anpasse (weniger datensatzvarianz?)
    - auf coarse ergebnisse anschauen ob malignant cells gehen und dann entscheiden ob man es entfernt
    - schauen wie viele zellen pro zelltypen vorhanden sind und anhand dessen weitere batches inkludieren
    - ovary ist alles aus einer studie, daher kein sampling bias
- outlier management implementieren (rejection class)
    - pyod
    - selber informieren!
    - wenn paul off the shelf eine empfehlung hat, schickt Anne sie mir, ansonsten ein Meeting mit Paul
- spatial datensätze annotieren
    - marker annotator validieren
    - oder fine grained labels (author annotation) zu coarse labeln mergen. Obergruppierung ist möglicherweise im paper, ansonsten evtl in meta daten. oder in die figure vom paper schauen
- welche outlier classes (recected classes) gibt es bei dem breast datensatz?
    - evtl fibroblast
- Dokument mit Todos als Überblick
- hierarchical auf spatial evaluieren
- anne lädt mich in ein neues overleaf projekt ein. erstmal nicht den ganzen report reinpasten, wieder von scratch anfangen (bis auf z.B. Einleitung)
- ich kann am 28.10. gerne mit zum talk kommen (10 Uhr)


### TODOs

- Weiter machen mit Package Option alle Classifier zu trainieren (dreiteilig)
    - ML Algorithmen
    - CE, AE, CAE auf bestem ML Algorithmus
    - Hierarchical auf bestem vorherigen Algorithmus
- outlier management
    X- PyOD
    X- Statistische Methodem (Unsicherheit des Modells)
- bei spatial datensätzen zwei annotationsebenen erschaffen
    X- Breast
X- Hierarchischen Classifier auf Sparse evaluieren
- Todos genau festlegen