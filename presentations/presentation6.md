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


## Mitschrieb

- bei result im paper technisch (Laufzeit, RAM), in und out of distribution als Unterkapitel. auch auf die einzelnen Klassen eingehen, wie wahrscheinlich es ist, dass diese Klasse richtig klassifiziert wird (siehe Classification Report). Evtl noch Precision auf support (anzahl samples pro klasse) plotten
- Deep Learning & Hybrid Approaches -> Denoising & Hybrid Approaches (Denoising Autoencoder ist kein Deep Learning weil ich eine LogisticRegression zum Klassifizieren verwende)
X- evaluate im package in eine datei schreiben
- Modelle über mehrere Runs vergleichen (mitteln)
- Weitere Vergleichsmodelle, gerne LLM
X- CellClassifier soll der Klassifikator heißen
- ich kann Preprocessing als Klasse anbieten, aber auf jeden Fall eine Anleitung machen und Hinweise aufs Preprocessing (Split und Genfilterung)
- bei adata objekten (kann ich sagen) muss mit angegeben werden auf welchem Feature gesplittet wird (kann ich mir selber überlegen und definieren)
- Grafiken anpassen, alle Schriften müssen lesbar sein
X- MarkerAnnotator soll keine default marker gene haben
- evtl testen das Denoising vor eine andere Methode zu schreiben (also vor einen anderen Algorithmus, z.B. CellTypist) (OPTIONAL)
- evtl einen vollständigen Deep Learning Ansatz nehmen mit einem Deep Learning Klassifikator nach dem Denoising
- Bei den Grafiken auch Precision, Recall und F1 vergleichen
- Aufbereiten, dass es als Paper gepublished werden kann

- Geht der Klassifikator beim Denoising Autoencoder auf den latenten Raum oder auf 10.000 (rekonstruierte) Gene?


### Vorgehensplan

- Fixes am package vornehmen
- Anleitung für package schreiben
- Script zum Mitteln der Ergebnisse erstellen
    X- Robustness Test gibt die Ergebnisse zusätzlich als Dataframe oder Dictionary zurück
    - Trainingsskript erweitern, dass mehrere Runs gemacht werden und dann gemittelt wird. Evtl so modular machen, dass es ein erweitertes Script gibt was für einen Run ein anderes Script aufruft
    - Im Script evtl auch gleich Runtime und RAM Verbrauch mit erfassen und mitteln
- Alle Modelle mit dem Script Mitteln (auch CellTypist)
- Nebenher Literaturrecherche zu weiteren Vergleichsmodellen
- Irgendwann mit dem Paper anfangen

Weitere TODOs
- Evtl CellTypist mit BayesSearch testen?

#### Ziele Sonntag

- Fixes am package vornehmen
    X- Bei predict fehlende gene mit 0 auffüllen und andere Gene entfernen -> selbe Methode bei ood Datensatz verwenden
    X- robustness test statt path für ood datensatz direkt ein dataframe oder anndata objekt nehmen (und Preprocessing aus Test rausschmeißen)
    - evtl nur Dataframes als Input?
X- package publishen
X- scGPT Trainingsscript fixen
X- scGPT Trainingsscript mit Hyperparameteroptimierung? -> nur mit Random Seed trainieren
X- scGPT, CellTypist und Autoencoder Script zum Mitteln starten
X- Paper
    X- Gliederung nochmal anhand der Beispielgliederung überarbeiten
    X- Citations fixen
    X- Mindestens 3 Subsections schreiben (oder eine Section)
- evtl scBERT testen


## HPC Scripte

### scGPT Training
scGPT: Submitted batch job 1725881
Submitted batch job 1725973
Submitted batch job 1725976
Submitted batch job 1725977
Submitted batch job 1725978
Submitted batch job 1725980
Submitted batch job 1725997
Submitted batch job 1726003
Submitted batch job 1726017
Submitted batch job 1726915
Submitted batch job 1726920
Submitted batch job 1726979
Submitted batch job 1726993
Submitted batch job 1727109
Batching and fixed prediction labels: Submitted batch job 1729065
Submitted batch job 1729203
Submitted batch job 1729397
Submitted batch job 1730514
Submitted batch job 1731028
stratify train valid split: Submitted batch job 1731095
Sampling and filter feature_importance dropout: Submitted batch job 1731247
Submitted batch job 1731361

### Evaluation over multiple runs

RandomForest: Submitted batch job 12018521
Submitted batch job 12018737
Submitted batch job 12018794
Submitted batch job 12018877
Submitted batch job 12018945
Submitted batch job 12018956

LogisticRegression: Submitted batch job 12018983
Run 7+: Submitted batch job 12024294

LinearSVC: Submitted batch job 12018984
Submitted batch job 12019024
Run 4+: Submitted batch job 12024295

ExtraTrees: Submitted batch job 12018985
Submitted batch job 12019022

LightGBM: Submitted batch job 12018986
Submitted batch job 12019023
Run 3+: Submitted batch job 12024296

Autoencoder: To test if autoencoder_lr.py or autoencoder_lr_v1.py should be used, submitted job for not _v1: Submitted batch job 12018988
Submitted batch job 12023436
Submitted batch job 12023806
Submitted batch job 12023859
Autoencoder mit RandomSearch: Submitted batch job 12023814
Submitted batch job 12024277

Conditional Autoencoder mit RandomSearch: Submitted batch job 12023816
Submitted batch job 12024278

scGPT: Submitted batch job 1731504
Submitted batch job 1731535
Submitted batch job 1731840

CellTypist: Submitted batch job 12020499
Submitted batch job 12023804
Submitted batch job 12024276



## Fragen

- Passt neue Gliederung?
- Soll ich wirklich ein Kapitel Software Implementation machen zu dem package?
- Passt das Zitat beim HumanCellAtlas oder soll ich es weglassen?