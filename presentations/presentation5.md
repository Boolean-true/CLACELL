# Presentation 5 am 8.6.26

## Code Improvements

- Split nach donor gemacht (siehe check_dataset.ipynb)
- Genfiltering
![Genfiltering](../training/gene_count_elbow_plot.png)
- Bayes search mit custom stopper


## Results

- Ergebnisse HPC

| Modell | Iterationen | Laufzeit | Zeit/Iteration | Bester Score | Beste Parameter |
|---|---|---|---|---|---|
| **Logistic Regression** | 10 | 11h26m | 1h9m | 0.8970 | `C=0.3520, class_weight=None, penalty=l1, tol=0.008815` |
| **Random Forest** | 19 | 1h1m | 3m | 0.8197 | `max_depth=30, max_features=sqrt, n_estimators=100` |
| **XGBoost** | 10 | 6h32m | 39m | 0.9240 | `colsample_bytree=0.3244, learning_rate=0.1728, max_depth=5` |

- Ergebnisse robustness tests

| Modell | Test Accuracy | Random Dropout | Multiple Executions | Feature Importance Dropout | Out of Distribution Accuracy |
|---|---|---|---|---|---|
| **Logistic Regression** | 0.9011 | 0.8803 | No Inconsistent Predictions | 5%: 0.4316<br>10%: 0.3699<br>15%: 0.4173<br>20%: 0.3631<br>25%: 0.3266<br>30%: 0.2988 | 0.1638 |
| **Random Forest** | 0.7474 | 0.7462 | No Inconsistent Predictions | 5%: 0.3461<br>10%: 0.0431<br>15%: 0.0145<br>20%: 0.0119<br>25%: 0.0118<br>30%: 0.0117 | 0.1136 |


## New Dataset

- HumanCellAtlas


## Weiteres Vorgehen

- Klassen mit wenigen Trainingsdaten herausfiltern
- Weiteren Datensatz analysieren
- Decoupler testen
- Robustness Tests mit out of distribution tests erweitern
- Ensemble Modelle / Ansätze für robustere Modelle trainieren


## Fragen

- Was soll mit Klassen mit sehr wenigen Trainingsdaten gemacht werden?







- Python package mit gridsearch, train und predict (wahrscheinlich in einem eigenen Repo)
- nach gridsearch und train wird reported auf hold out datensatz, gridsearch wechselt dann in train
- hold out split wird von mir gesetzt bei gridsearch(user gibt nur prozentteil an; wird dann an train weitergegeben), bei train kann user selber hold out datensatz angeben
- Comparison mit Celltypist -> schauen wie man es trainieren kann
- nur wenige Gene aus Feature Imporance löschen (0,1 0,5 1 2%)
- Ensemble Modell auch mit denselben Modellen auf jeweils unterschiedlichen Daten trainiert (also über Feature Importance Dropout werden Features gelöscht) (evtl hierbei testen ob ein Stacking/Voting Classifier oder ein regelbasiertes matching auf das Modell mit den meisten übereinstimmenden Features besser ist). Trotzdem auch ein normales Ensemble Modell testen und dann vergleichen
- Vor den Ensemble Modellen nochmal recherchieren ob es noch weitere relevante Modelle gibt und dann entscheiden welche Modelle in das Ensemble aufgenommen werden


## Entscheidung für min_genes

### Score bei optimaler LR mit jeweils train und test mit min_genes
Ohne: 0.9011296395911781, Macro F1: 0.504096164631464
20: 0.90224186247036, Macro F1: 0.5744418750743242
100: 0.9091800065338125, Macro F1: 0.7760799430608922
150: 0.9174180778535298, Macro F1: 0.8617811577208385
200: 0.9174180778535298, Macro F1: 0.8484774676167686

### Score bei optimaler LR mit jeweils train mit min_genes, test fest auf min_genes=200
Ohne: 0.915858687172629
20: 0.9167502507522568
100: 0.9175303688844311
150: 0.9176418143318845
200: 0.917753259779338
NEU
Ohne: 0.9164284143391247, Macro F1: 0.7122163277778566
20: 0.916318451726413, Macro F1: 0.7929844825760659
100: 0.916648339564548, Macro F1: 0.7950758496854666
150: 0.9176380030789532, Macro F1: 0.8508946077305661
200: 0.9174180778535298, Macro F1: 0.8484774676167686

### Score bei optimaler LR mit jeweils train mit min_genes, test fest auf min_genes=20
Ohne: 0.90224186247036, Macro F1: 0.5811079720161112
20: 0.9029963354171158, Macro F1: 0.5840748885803906
100: 0.9004095710282388, Macro F1: 0.5182459015849566
150: 0.9001940073291658, Macro F1: 0.4826242326190024
200: 0.8872601853847812, Macro F1: 0.3724735797384595

=> min_samples=150

## Entscheidung ob zusätzlich Standardscaler
### LR ohne Standardscaler
0.9173081152408181
Macro F1: 0.8603947961498007

### LR mit Standardscaler
0.9066417418077853
Macro F1: 0.7843370852693642

=> Ohne Standardscaler


## Annotate Data

### CellTypist Dataset

Annotation: Submitted batch job 11906765
Submitted batch job 11906767
Submitted batch job 11906783
Submitted batch job 11906786
Submitted batch job 11906805
Im neuen venv: Submitted batch job 11910671
Submitted batch job 11910890
Im 3.12 venv: Submitted batch job 11911153
Submitted batch job 11911338
Submitted batch job 11911503 -> zu wenig RAM
Maximaler RAM auf Woody: Submitted batch job 11914679 -> zu wenig RAM
Auf TinyFat: Submitted batch job 1407154 on cluster tinyfat
Submitted batch job 1407228 on cluster tinyfat
Submitted batch job 1407371 on cluster tinyfat
Submitted batch job 1407375 on cluster tinyfat
Submitted batch job 1407505 on cluster tinyfat
Submitted batch job 1408307 on cluster tinyfat
Submitted batch job 1408530 on cluster tinyfat
Submitted batch job 1409026 on cluster tinyfat

- Many Problems with RAM and with Segmentation Faults
- Final try took 1:16 hours and 245GB RAM

### humancellatlas

Submitted batch job 1410282 on cluster tinyfat
Submitted batch job 1410306 on cluster tinyfat -> Zu wenig RAM
Limit Anndata to 15.000 Cells: Submitted batch job 1413673 on cluster tinyfat


## Train Models

LightGBM: Submitted batch job 11849786 -> Cancelled wegen time limit nach 9 Iterationen, best score: score=0.863; Hyperparameters: feature_fraction=0.691167806437252, learning_rate=0.011884061970449536, n_estimators=114, num_leaves=96; Grund: ein Split startet erst wenn der vorherige beendet ist
2. Versuch mit Parallelisierung auf CV: Submitted batch job 11893005 -> Wieder cancelled wegen time limit, ein zwischenergebnis: [CV 4/5; 1/1] END feature_fraction=0.6606968391259233, learning_rate=0.018412588192430017, n_estimators=128, num_leaves=28;, score=0.903 total time=47.7min

LinearSVC: Submitted batch job 11870566 -> Cancelled wegen time limit, keine prints im .out log
9.6. & 10.6. sind Server down, daher erst am Donnerstag Ergebnisse
2. Versuch mit angepasstem Hyperparameterraum: Submitted batch job 11893131
Parallel ein Versuch auf meinem PC: Ergebnis nach 19 Iterationen in 34m: Test-Split Accuracy:  0.8959, Hyperparameters: {'C': 0.05907694609979313, 'class_weight': None, 'penalty': 'l1', 'tol': 0.0004717746164106244}

ExtraTrees: Submitted batch job 11895804




Set 1 | Voting: hard | Modelle: ['rf', 'et', 'lr'] -> Accuracy: 0.7689
Set 2 | Voting: soft | Modelle: ['rf', 'et', 'lr'] -> Accuracy: 0.8939
Set 3 | Voting: hard | Modelle: ['rf', 'linsvc', 'lr'] -> Accuracy: 0.8965
Set 4 | Voting: hard | Modelle: ['et', 'linsvc', 'lr'] -> Accuracy: 0.8956
Set 5 | Voting: hard | Modelle: ['rf', 'linsvc', 'et', 'lr'] -> Accuracy: 0.7914
Set 6 | Voting: hard | Modelle: ['rf', 'linsvc', 'et', 'lr', 'lgbm'] -> Accuracy: 0.7806


CellTypist: Submitted batch job 11905024
Submitted batch job 11905067
Robustness: Submitted batch job 11905075
Submitted batch job 11905078: Score auf Test data: 0.8727
Submitted batch job 11905081: Score auf Test data: 0.8727
Submitted batch job 11905082
Submitted batch job 11905603


Autoencoder: Submitted batch job 11906564
Submitted batch job 11906614 -> 0.8298 in 17min
Submitted batch job 11906733
Submitted batch job 11906736
V1 ohne Standardscaler: Submitted batch job 11906746 -> geht nicht
V1 mit Robustnesstest: Submitted batch job 11906766
Submitted batch job 11906784
Submitted batch job 11906804
Submitted batch job 11908792
Eigene Klasse für Model: Submitted batch job 11914920
Submitted batch job 11915328 -> Ergebnis, aber das Löschen mit Feature Importance gibt immer dasselbe Ergebnis
Submitted batch job 11915851

Vergleich LR: Submitted batch job 11915836


## Robustness Comparison

### LogisticRegression
#### Trained on CellTypist Labels
Baseline accuracy score 0.9011
Random dropout accuracy score 0.8900
Total samples: 9295
Number of inconsistent predictions: 0
Feature importance dropout (0% features dropped) accuracy score 0.8916
Feature importance dropout (0% features dropped) accuracy score 0.6949
Feature importance dropout (1% features dropped) accuracy score 0.6024
Feature importance dropout (2% features dropped) accuracy score 0.5374
Out of data distribution
Genes expected in training set: 10000
Genes actually matched in test set: 8408
Training data Max-Value: 2.6092522
Test data Max-Value: 3.0608508586883545
Baseline accuracy score 0.1638

#### Trained on scumi annotated Labels
Baseline accuracy score 0.9495
Random dropout accuracy score 0.9396
Total samples: 9094
Number of inconsistent predictions: 0
Feature importance dropout (0% features dropped) accuracy score 0.8189
Feature importance dropout (0% features dropped) accuracy score 0.7161
Feature importance dropout (1% features dropped) accuracy score 0.7160
Feature importance dropout (2% features dropped) accuracy score 0.7108
Out of data distribution
Genes expected in training set: 10000
Genes actually matched in test set: 8408
Training data Max-Value: 2.6020768
Test data Max-Value: 3.0608508586883545
Baseline accuracy score 0.0000

Macro F1: 0.9578187526238896

### RandomForest
Baseline accuracy score 0.7474
Random dropout accuracy score 0.7403
Total samples: 9295
Number of inconsistent predictions: 0
Feature importance dropout (0% features dropped) accuracy score 0.7215
Feature importance dropout (0% features dropped) accuracy score 0.6272
Feature importance dropout (1% features dropped) accuracy score 0.5912
Feature importance dropout (2% features dropped) accuracy score 0.5720
Out of data distribution
Genes expected in training set: 10000
Genes actually matched in test set: 8408
Training data Max-Value: 2.6092522
Test data Max-Value: 3.0608508586883545
Baseline accuracy score 0.1136

### ExtraTrees
Baseline accuracy score 0.7526
Random dropout accuracy score 0.7405
Total samples: 9295
Number of inconsistent predictions: 0
Feature importance dropout (0% features dropped) accuracy score 0.7232
Feature importance dropout (0% features dropped) accuracy score 0.6088
Feature importance dropout (1% features dropped) accuracy score 0.5674
Feature importance dropout (2% features dropped) accuracy score 0.5622
Out of data distribution
Genes expected in training set: 10000
Genes actually matched in test set: 8408
Training data Max-Value: 2.6092522144317627
Test data Max-Value: 3.0608508586883545
Baseline accuracy score 0.1190

### LinearSVC
Baseline accuracy score 0.8979
Random dropout accuracy score 0.8833
Total samples: 9295
Number of inconsistent predictions: 0
Feature importance dropout (0% features dropped) accuracy score 0.8738
Feature importance dropout (0% features dropped) accuracy score 0.7098
Feature importance dropout (1% features dropped) accuracy score 0.5743
Feature importance dropout (2% features dropped) accuracy score 0.4372

### VotingClassifier
Baseline accuracy score 0.8993
Random dropout accuracy score 0.8869
Total samples: 9295
Number of inconsistent predictions: 0
Feature importance dropout (0% features dropped) accuracy score 0.8817
Feature importance dropout (0% features dropped) accuracy score 0.7044
Feature importance dropout (1% features dropped) accuracy score 0.6072
Feature importance dropout (2% features dropped) accuracy score 0.4892
Out of data distribution
Genes expected in training set: 10000
Genes actually matched in test set: 8408
Training data Max-Value: 2.6092522144317627
Test data Max-Value: 3.0608508586883545
Baseline accuracy score 0.1624

### StackingClassifier
Baseline accuracy score 0.9013
Random dropout accuracy score 0.8897
Total samples: 9295
Number of inconsistent predictions: 0
Feature importance dropout (0% features dropped) accuracy score 0.8912
Feature importance dropout (0% features dropped) accuracy score 0.6880
Feature importance dropout (1% features dropped) accuracy score 0.5918
Feature importance dropout (2% features dropped) accuracy score 0.5346
Out of data distribution
Genes expected in training set: 10000
Genes actually matched in test set: 8408
Training data Max-Value: 2.6092522144317627
Test data Max-Value: 3.0608508586883545
Baseline accuracy score 0.1664

### DAE
Mit test_data.X
Baseline accuracy score 0.8415
Random dropout accuracy score 0.8279
Total samples: 9295
Number of inconsistent predictions: 0
Feature importance dropout (0% features dropped) accuracy score 0.8415
Feature importance dropout (0% features dropped) accuracy score 0.8415
Feature importance dropout (1% features dropped) accuracy score 0.8415
Feature importance dropout (2% features dropped) accuracy score 0.8415
Out of Distribution wurde auf dem HPC nicht getestet

Mit test_data.to_df()
Baseline accuracy score 0.8409
Random dropout accuracy score 0.8267
Total samples: 9295
Number of inconsistent predictions: 0
Feature importance dropout (0% features dropped) accuracy score 0.8298
Feature importance dropout (0% features dropped) accuracy score 0.7621
Feature importance dropout (1% features dropped) accuracy score 0.7416
Feature importance dropout (2% features dropped) accuracy score 0.7265
Out of data distribution

### Ensemble mit LogisticRegression mit unterschiedlichen Features
#### Im Training Feature Importance der LogisticRegression
Mit Feature Importance der LogisticRegression (Problem: Bereits im Training vorhanden)
Baseline accuracy score 0.9082
Random dropout accuracy score 0.8932
Total samples: 9094
Number of inconsistent predictions: 0
Feature importance dropout (0% features dropped) accuracy score 0.8945
Feature importance dropout (0% features dropped) accuracy score 0.8843
Feature importance dropout (1% features dropped) accuracy score 0.8651
Feature importance dropout (2% features dropped) accuracy score 0.7857
Out of data distribution nicht gemacht
-> Problem: Feature Importance Drop ist derselbe wie im Training

Mit Feature Importance des RandomForests
Baseline accuracy score 0.9082
Random dropout accuracy score 0.9002
Total samples: 9094
Number of inconsistent predictions: 0
Feature importance dropout (0% features dropped) accuracy score 0.8965
Feature importance dropout (0% features dropped) accuracy score 0.8123
Feature importance dropout (1% features dropped) accuracy score 0.7515
Feature importance dropout (2% features dropped) accuracy score 0.6019
Out of data distribution

#### Im Training Feature Importance des RandomForest
Mit Feature Importance der LogisticRegression
Baseline accuracy score 0.9161
Random dropout accuracy score 0.9087
Total samples: 9094
Number of inconsistent predictions: 0
Feature importance dropout (0% features dropped) accuracy score 0.8204
Feature importance dropout (0% features dropped) accuracy score 0.7724
Feature importance dropout (1% features dropped) accuracy score 0.7686
Feature importance dropout (2% features dropped) accuracy score 0.7866
Out of data distribution

Mit Feature Importance des RandomForests (Problem: Bereits im Training vorhanden)
Baseline accuracy score 0.9161
Random dropout accuracy score 0.9071
Total samples: 9094
Number of inconsistent predictions: 0
Feature importance dropout (0% features dropped) accuracy score 0.9164
Feature importance dropout (0% features dropped) accuracy score 0.9036
Feature importance dropout (1% features dropped) accuracy score 0.8726
Feature importance dropout (2% features dropped) accuracy score 0.6310
Out of data distribution