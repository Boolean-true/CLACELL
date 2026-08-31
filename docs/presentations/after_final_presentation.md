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