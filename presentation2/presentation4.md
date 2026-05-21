# Presentation 4

## Robustness Tests

TODO

## Results

- Method: Baseline accuracy, random dropout score (both on test split), train time, robustness test time

- RF: 0.7996, 0.7890, 35s, 17s
- LogisticRegression: 0.9177, 0.9148, 57s, 32s
- SVM: 0.5064, 0.4571, 1h35, 6h11
- LightGBM: 0.2856, 0.2559, 11m, 14s
- XGBoost: 0.9166, 0.9011, 37m, 31s

nur SVM hatte angepasste Hyperparameter: kernel="poly", C=0.001, sonst 10h ohne Ergebnis

TODO: weiteren robustness test, der entweder default relevante gene löscht und dann prüft oder mit feature importance die relevantesten gene löscht und dann prüft. evtl mit dict für die verschiedenen wege für feature importance
TODO: erweiterten robustness test testen
TODO: siehe gemini die dataframes vergleichen
TODO: robustness test auf den anderen Daten