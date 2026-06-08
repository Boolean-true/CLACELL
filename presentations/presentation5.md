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