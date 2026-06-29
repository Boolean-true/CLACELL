---
# try also 'default' to start simple
theme: seriph
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev

# apply any unocss classes to the current slide
class: 'text-center'
# some information about the slides, markdown enabled
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
transition: slide-left
title: Presentation 5 am 8.6.26
mdc: true
---

# Presentation 6 am 29.6.26


---

## Code Improvements I

- Trainingsdatensatz + Out of Distribution Datensatz mit scumi Reimplementierung annotiert (>400GB RAM) und diese Labels zum Training verwendet (Decoupler hat keine guten Ergebnisse gebracht)
- Bei beiden Datensätzen werden die Rohcounts verwendet und preprocessed

<div class="text-xs leading-tight">

<table>
  <thead>
    <tr>
      <th>Cell</th>
      <th>Number of Samples</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>CD4+ T cell</td><td>13529</td></tr>
    <tr><td>CD14+ monocyte</td><td>6480</td></tr>
    <tr><td>Natural killer cell</td><td>3958</td></tr>
    <tr><td>Cytotoxic T cell</td><td>2822</td></tr>
    <tr><td>B cell</td><td>393</td></tr>
    <tr><td>Megakaryocyte</td><td>151</td></tr>
    <tr><td>Dendritic cell</td><td>134</td></tr>
    <tr><td>Plasma cell</td><td>106</td></tr>
  </tbody>
</table>

</div>
TODO: Püfen ob das stimmt

<br><br>

### CellTypist Baseline

- CellTypist ist kein DL Tool sondern eine LogisticRegression
- CellTypist wurde neu trainiert, geht aber nur auf einer älteren scikit-learn Version

---

## Code Improvements II

### Robustheitstest

- TODO: Aufbau zeigen
- Feature Importance Dropout wird jetzt über die Markergene gemacht. Da es nicht genügend Markergene gibt, werden die restlichen aufgefüllt. TODO: wie werden sie aufgefüllt?
Dabei wird interleaved, also jeweils ein Markergen pro Klasse, dann das nächste pro Klasse

---

## Neue Ansätze

- Denoising Autoencoder
  - Encoder bringt Features in latenten Raum TODO: wieviel
  - Decoder rekonstruiert Features
  - TODO: Wo ist mein Early Stopping?
- Conditional Autoencoder
  - Um Batch Effekte zu vermeiden (Split nach Donor), wird dem Modell in einem One-Hot Vektor mitgeteilt, von welchem Donor das Sample stammt -> Autoencoder lernt im latenten Raum nicht mit von wem das Sample stammt
  - Bei Inferenz wird ein Nullvektor mitgegeben
  - TODO: Wo ist mein Early Stopping?
- Custom Ensemble (0%; 0,75%;15%;25% Feature Importance Drop)
  - Werte so gewählt, dass es keine Überschneidung mit Robustheitstests gibt
  - Bisher wurden nur lineare Modelle getestet und es wurde die Feature Importance des besten Random Forest genommen

---

## Results I

TODO

---

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

---

## Gliederungsentwurf

```
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
```

> Die Unterebenen sind noch nicht final

---

## Weiteres Vorgehen

- Denoising Autoencoder mit LinearSVC und evtl RandomForest statt LogisticRegression testen
- StackingClassifier
- Evtl Ensemble, bei dem das erste Modell Features 1-x, zweites Features x-y, ... bekommt
- Autoencoder und Custom Ensemble weiter verbessern
- Paper anfangen

---


## Fragen

- Anne nicht auf dem Paper als Betreuerin erwähnen?
- Ist das Paper richtig, es ist nicht zweispaltig?
- Ist die Obergrenze der Seitenzahlen 4?
- Passt die Gliederung?
- Wird das Paper gepublished?
- Beim Package sollte das Preprocessing in eine eigene Klasse kommen, die dann vor der Annotation und dem Modelltraining ausgeführt wird?
- Passen die Ergebnisse soweit? Oder muss ich etwas ändern?
