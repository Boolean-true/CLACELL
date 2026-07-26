# Presentation 4

## Robustness Tests

Siehe Code

## Results
| Method | Baseline accuracy | Random dropout score | Train time | Robustness test time |
|---|---:|---:|---:|---:|
| RF | 0.7996 | 0.7890 | 35s | 17s |
| LogisticRegression | 0.9177 | 0.9148 | 57s | 32s |
| SVM | 0.5064 | 0.4571 | 1h35 | 6h11 |
| LightGBM | 0.2856 | 0.2559 | 11m | 14s |
| XGBoost | 0.9166 | 0.9011 | 37m | 31s |

nur SVM hatte angepasste Hyperparameter: kernel="poly", C=0.001, sonst 10h ohne Ergebnis

## Weitere Schritte

- Weiteren robustness test, der entweder default relevante gene löscht und dann prüft oder mit feature importance die relevantesten gene löscht und dann prüft. evtl mit dict für die verschiedenen wege für feature importance
- Robustness test auf den anderen Daten

## Mitschrieb

- die processed Daten sind nicht zum Testen gedacht, Rohdaten suchen
X- Bei CellTypist statt random train test split einfach nach Datensätzen splitten, damit die Modelle die Daten nicht gesehen haben -> LR ist jetzt 1,5% schlechter bbei random Dropout, vorher war sie nur 0,3% schlechter
- Wenn ich dann CellTypist evaluiere muss ich es noch selber trainieren
- Oder ich suche weitere Datensätze zum Testen
- CellTypist auf jeden Fall evaluieren
- decoupler anschauen
- evtl eher von einem Modell das ich nicht verwende z.B. RF die Feature Importance zum rauschmeißen nehmen, dann werden die anderen Modelle nicht unfair geschadet. Oder marker gene dafür verwenden -> TODO: zuerst einmal überschneidung von Feature Importance von RF mit marker genen anschauen, evtl sind die ja sehr ähnlich
- weitere Abstufungen bei Tests: within data distribution, out of distribution, outof distribution und random dropout
- Hyperparametertuning schonmal machen
- HPC anschauen, Anne schickt mir nen Link, bei Fragen melden
- cd $WORK um in Verzeichnis mit mehr Speicherplatz zu kommen