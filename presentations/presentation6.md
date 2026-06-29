# Presentation 6 am 29.6.26

## Code Improvements

- Trainingsdatensatz + Out of Distribution Datensatz mit scumi Reimplementierung annotiert und diese Labels zum Training verwendet (Decoupler hat keine guten Ergebnisse gebracht)
- Bei beiden Datensätzen werden die Rohcounts verwendet und preprocessed

## CellTypist Baseline

- CellTypist ist kein DL Tool sondern eine LogisticRegression
- CellTypist wurde neu trainiert, geht aber nur auf einer älteren scikit-learn Version

## Neue Ansätze

- Autoencoder
- Conditional Autoencoder
- Custom Ensemble (0%; 0,75%;15%;25% Feature Importance Drop)

## Ergebnisse

- TODO: Tabellen und Grafiken einfügen

## Python package

- Package jetzt verfügbar mit ```pip install clacell```
- MarkerAnnotator zum annotieren mit der scumi Reimplementierung
- BloodCellClassifier als Klassifikator (aktuell eine simple LogisticRegression)
    - grid_search für Hyperparametersuche
    - train fürs Training
    - evaluate für die Robustheitstests
    - predict zur Vorhersage
- Als Input sind Dataframes und Anndata Objekte möglich
- Ergebnisse sind nur so gut, weil im Package intern Train und Test Split nicht nach Donor sondern Random gesplittet werden

## Gliederungsentwurf

1. Introduction
1.1 Background
1.2 State of the Art & Limitations
1.3 My Contributions
2. Materials and Methods
2.1 Datasets & Baseline
2.2 Marker-Based Annotation
2.3 Machine Learning Architectures
2.4 Ensemble Learning Strategies
2.5 Deep Learning & Hybrid Approaches
3. Results
4. Software Implementation
5. Discussion and Conclusion
5.1 Interpretation of Findings
5.2 Limitations
5.3 Conclusion & Future Work

TODO: Nochmal drüberschauen und anpassen

## Weiteres Vorgehen

- Autoencoder mit LinearSVC und evtl RandomForest statt LogisticRegression testen
- StackingClassifier
- Paper anfangen


## Fragen

- Anne nicht auf dem Paper als Betreuerin erwähnen?
- Ist das Paper richtig, es ist nicht zweispaltig?
- Ist die Obergrenze der Seitenzahlen 4?
- Passt die Gliederung?
- Beim Package sollte das Preprocessing in eine eigene Klasse kommen, die dann vor der Annotation und dem Modelltraining ausgeführt wird?