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
2.6 Robustness Tests
3. Results
3.1 Comparison of Machine Learning Architectures
3.2 Comparison of Ensemble and Deep Learning Approaches
3.3 Comparison with CellTypist
4. Software Implementation
5. Discussion and Conclusion
5.1 Interpretation of Findings
5.2 Limitations
5.3 Conclusion & Future Work


## Weiteres Vorgehen

- Autoencoder mit LinearSVC und evtl RandomForest statt LogisticRegression testen
- StackingClassifier
- Paper anfangen


## Fragen

- Anne nicht auf dem Paper als Betreuerin erwähnen?
- Ist das Paper richtig, es ist nicht zweispaltig?
- Ist die Obergrenze der Seitenzahlen 4?
- Passt die Gliederung?
- Wird das Paper gepublished?
- Beim Package sollte das Preprocessing in eine eigene Klasse kommen, die dann vor der Annotation und dem Modelltraining ausgeführt wird?
- Passen die Ergebnisse soweit? Oder muss ich etwas ändern?



- bei result im paper technisch (Laufzeit, RAM), in und out of distribution als Unterkapitel. auch auf die einzelnen Klassen eingehen, wie wahrscheinlich es ist, dass diese Klasse richtig klassifiziert wird (siehe Classification Report). Evtl noch Precision auf support (anzahl samples pro klasse) plotten
- Deep Learning & Hybrid Approaches -> Denoising & Hybrid Approaches (Denoising Autoencoder ist kein Deep Learning weil ich eine LogisticRegression zum Klassifizieren verwende)
- evaluate im package in eine datei schreiben
- Modelle über mehrere Runs vergleichen (mitteln)
- Weitere Vergleichsmodelle, gerne LLM
- CellClassifier soll der Klassifikator heißen
- ich kann Preprocessing als Klasse anbieten, aber auf jeden Fall eine Anleitung machen und Hinweise aufs Preprocessing (Split und Genfilterung)
- bei adata objekten (kann ich sagen) muss mit angegeben werden auf welchem Feature gesplittet wird (kann ich mir selber überlegen und definieren)
- Grafiken anpassen, alle Schriften müssen lesbar sein
- MarkerAnnotator soll keine default marker gene haben
- evtl testen das Denoising vor eine andere Methode zu schreiben (also vor einen anderen Algorithmus, z.B. CellTypist) (OPTIONAL)
- evtl einen vollständigen Deep Learning Ansatz nehmen mit einem Deep Learning Klassifikator nach dem Denoising
- Bei den Grafiken auch Precision, Recall und F1 vergleichen
- Aufbereiten, dass es als Paper gepublished werden kann

- Geht der Klassifikator beim Denoising Autoencoder auf den latenten Raum oder auf 10.000 (rekonstruierte) Gene?