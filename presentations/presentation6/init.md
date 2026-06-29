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

<br><br>

### CellTypist
---

## Code Improvements II

### Robustheitstest

- Aufbau zeigen
- Feature Importance Dropout wird jetzt über die Markergene gemacht. Da es nicht genügend Markergene gibt, werden die restlichen aufgefüllt mit Genen aus einer differentiellen Genexpression.
Dabei wird interleaved, also jeweils ein Markergen pro Klasse, dann das nächste pro Klasse

---

## CellTypist Baseline

- CellTypist ist kein DL Tool sondern eine LogisticRegression
- CellTypist wurde neu trainiert, geht aber nur auf einer älteren scikit-learn Version

---

## Neue Ansätze

- Denoising Autoencoder
  - Encoder bringt Features in latenten Raum 128
  - Decoder rekonstruiert Features
  - Early Stopping mit patience=5
- Conditional Autoencoder
  - Um Batch Effekte zu vermeiden (Split nach Donor), wird dem Modell in einem One-Hot Vektor mitgeteilt, von welchem Donor das Sample stammt -> Autoencoder lernt im latenten Raum nicht mit von wem das Sample stammt
  - Bei Inferenz wird ein Nullvektor mitgegeben
  - Early Stopping mit patience=5
- Custom Ensemble (0%; 0,75%;15%;25% Feature Importance Drop)
  - Werte so gewählt, dass es keine Überschneidung mit Robustheitstests gibt
  - Bisher wurden nur lineare Modelle getestet und es wurde die Feature Importance des besten Random Forest genommen

---

## Results I

<div class="text-[9.5px] leading-tight">

| Modell | Iterationen | Laufzeit | Zeit/Iteration | Train Score | Test Score | Macro F1-Score | Random Dropout | OOD Test Score | OOD Macro F1 | OOD Random Dropout |
|---|---|---|---|---|---|---|---|---|---|---|
| RandomForest | 19 | 40m | 2m | 0.9759 | 0.8868 | 0.81 | 0.8582 | 0.9068 | 0.80 | 0.8954 |
| LogisticRegression | 19 | 3h25m | 11m | 0.9656 | 0.9213 | 0.92 | 0.9123 | 0.8765 | 0.80 | 0.8707 |
| LinearSVC | 15 | 8h17m | 33m | 0.9634 | 0.9244 | 0.92 | 0.9244 | 0.8752 | 0.79 | 0.8727 |·
| ExtraTrees | 19 | 44m | 2m | 0.9736 | 0.8877 | 0.82 | 0.8728 | 0.8898 | 0.75 | 0.8811 |
| LightGBM | 19 | 8h37m | 27m | 0.9590 | 0.8501 | 0.81 | 0.8427 | 0.8886 | 0.82 | 0.8812 |
| Voting | 18 | 9h | 30m | 0.9750 | 0.8920 | 0.82 | 0.8743 | 0.8915 | 0.78 | 0.8820 |
| Autoencoder | 150 + 50 | 2h56m | unknown | 0.9609 | 0.9004 | 0.83 | 0.8848 | 0.8496 | 0.75 | 0.8413 |
| Conditional Autoencoder | 40 + 50 | 1h3m | unknown | 0.9588 | 00.9052 | 0.87 | 0.8951 | 0.8533 | 0.81 | 0.8188 |
| Custom Ensemble LR | 1 | 9m | 9m | unknown | 0.9126 | 0.91 | 0.9044 | 0.8698 | 0.79 | 0.8696 |
| Custom Ensemble LinSVC | 1 | 30s | 30s | unknown | 0.9359 | 0.92 | 0.9330 | 0.8688 | 0.77 | 0.8642 |
| CellTypist | 50 | 1h35m | 2m | 0.918 | 0.8033 | 0.72 | 0.7782 | 0.7067 | 0.51 | 0.6388 |

</div>

---

## Results II

<div class="flex justify-center">
  <img src="/in_distribution_robustness_comparison.png" alt="In-distribution Robustness Comparison" class="w-[85%] max-w-full h-auto" />
</div>

---

## Results III

<div class="flex justify-center">
  <img src="/out_of_distribution_robustness_comparison.png" alt="Out-of-distribution Robustness Comparison" class="w-[85%] max-w-full h-auto" />
</div>


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

- Soll ich dich nicht auf dem Paper als Betreuerin erwähnen?
- Ist das Paper richtig, es ist nicht zweispaltig?
- Ist die Obergrenze der Seitenzahlen 4?
- Passt die Gliederung?
- Wird das Paper gepublished?
- Beim Package sollte das Preprocessing in eine eigene Klasse kommen, die dann vor der Annotation und dem Modelltraining ausgeführt wird?
- Hast du Präferenzen für welche Metriken wichtiger sind?
