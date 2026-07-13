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
title: Presentation 7 am 13.7.26
mdc: true
---

# Presentation 7 am 13.7.26


---

## Code Improvements

- Alle Algorithmen über 10 Runs gemittelt und jeweils den Mittelwert + Standardabweichung angegeben
- Neue Vergleichsmodelle: scGPT und SingleR
- Geneformer und scANVI haben keine richtigen Ergebnisse in annehmbarer Zeit gebracht
- Custom Ensemble mit LR und RF
- Autoencoder + Denoising Autoencoder mit RF
- Beim Autoencoder geht das ML Modell auf den latenten raum und nicht auf die Gene!

---

## scGPT als Vergleichsmodell

- braucht eine A100 zum Training
- Ich habe es nur mit einem gegebenen Script finegetuned (Base ist das Modell für Blutzellen) #TODO: nachschauen welches genau
- Hatte initial eine sehr schlechte Leistung, ich habe angepasst:
  - StratifiedCrossValidation für eine gleiche Verteilung im train und valid split
  - Sampling sodass mindestens 1000 samples pro Klasse verfügbar waren
- Hat eine hohe Standardabweichung bei den Scores
  - Maximum: 0.4057 (CLACELL: 0.0426)
  - Durchschnitt: 0.1103 (CLACELL: 0.0054)
- Number of inconsistent predictions: 6770.5 +- 4031.5095

---

## Results I

<div class="text-[9.5px] leading-tight">

| Modell | Laufzeit | Peak RAM | GPU | Macro F1-Score | Random Dropout | OOD Macro F1-Score | OOD Dropout |
|---|---|---|---|---|---|---|---|
| RandomForest | 44.885 +- 2.4418 | 14.1657 +- 0.0 | Nein | 0.7964 | 0.8717 | 0.7892 | 0.886 |
| LogisticRegression | 233.507 +- 65.9274 | 12.8455 +- 1.0557 | Nein | 0.9004 | 0.907 | 0.7928 | 0.8725 |
| LinarSVC | 403.766 +- 106.7374 | 12.9602 +- 1.7293 | Nein | 0.9157 | 0.9117 | 0.7908 | 0.8733 |
| ExtraTrees | 49.168 +- 3.254 | 12.2392 +- 0.0 | Nein | 0.8085 | 0.8691 | 0.7548 | 0.8814 |
| LightGBM | 488.199 +- 58.4515 | 12.0876 +- 1.401 | Nein | 0.821 | 0.8509 | 0.8176 | 0.8624 |
| Autoencoder LinSVC| 148.246 +- 12.5516 | 17.3026 +- 0.1284 | Nein | 0.8634 | 0.8721 | 0.7678 | 0.8405 |
| Conditional Autoencoder RF | 110.721 +- 10.0074 | 19.2451 +- 0.2604 | 0.8698 | 0.9071 | 0.8307 | 0.8403 |
| Custom Ensemble LinSVC | 42.413 +- 28.9577 | 13.8709 +- 0.0 | Nein | 0.9225 | 0.9272 | 0.7766 | 0.8646 |
| CellTypist | 182.48 +- 3.4319 | 13.341 +- 1.2187 | Nein | 0.7342 | 0.7815 | 0.5834 | 0.6962 |
| scGPT | 122.271 +- 0.8571 | 14.9738 +- 0.5028 | Ja | 0.7301 | 0.8184 | 0.8153 | 0.8678 |
| SingleR | 11.902 +- 0.2698 | 11.9978 +- 0.1047 | Nein | 0.9056 | 0.9679 | 0.7543 | 0.7695 |

</div>

TODO: Bei LinearSVC noch die Zeit für das Einzeltraining draufrechnen

---

## Results II

<div class="flex justify-center">
  <img src="/in_distribution_ml_robustness_comparison.png" alt="In-distribution ML Robustness Comparison" class="w-[85%] max-w-full h-auto" />
</div>

---

## Results III

<div class="flex justify-center">
  <img src="/out_of_distribution_ml_robustness_comparison.png" alt="Out-of-distribution ML Robustness Comparison" class="w-[85%] max-w-full h-auto" />
</div>

---

## Results IV

<div class="flex justify-center">
  <img src="/in_distribution_ae_ensemble_robustness_comparison.png" alt="In-distribution AE Ensemble Robustness Comparison" class="w-[85%] max-w-full h-auto" />
</div>

---

## Results V

<div class="flex justify-center">
  <img src="/out_of_distribution_ae_ensemble_robustness_comparison.png" alt="Out-of-distribution AE Ensemble Robustness Comparison" class="w-[85%] max-w-full h-auto" />
</div>

---

## Results VI

<div class="flex justify-center">
  <img src="/in_distribution_comparison_robustness_comparison.png" alt="In-distribution Robustness Comparison" class="w-[85%] max-w-full h-auto" />
</div>

---

## Results VII

<div class="flex justify-center">
  <img src="/out_of_distribution_comparison_robustness_comparison.png" alt="Out-of-distribution Robustness Comparison" class="w-[85%] max-w-full h-auto" />
</div>


---

## Python package

- Custom Ensemble mit LinearSVC jetzt in CLACELL 1.0.0 verfügbar
- Kein internes Preprocessing mehr, eigene Methode: preprocess_data
- Kein interner Train Test Split mehr, es werden nur noch Dataframes akzeptiert

---

## Gliederungsentwurf

```
1. Introduction
2. Results
  2.1 Comparison of Machine Learning Architectures
  2.2 Comparison of Ensemble and Deep Learning Approaches
  2.3 Comparison with Reference Models
3. Discussion and Conclusion
  5.1 Interpretation of Findings
  5.2 Limitations
  5.3 Conclusion & Future Work
4. Materials and Methods
  4.1 Data Preprocessing
  4.2 Reference Models
  4.3 Marker-Based Annotation
  4.4 Machine Learning Algorithms
  4.5 Ensemble Learning Strategies
  4.6 Denoising & Hybrid Approaches
  4.7 Robustness Tests
5. CLACELL Package
```

> Changes: Results + Discussion weiter vorne, Data Preprocessing hinzugefügt, Software Implementation -> CLACELL Package

---

## Weiteres Vorgehen

- Weitere Anpassungen am Package
- Evtl weitere Verbesserungen am Modell
- Paper schreiben

---


## Fragen

### Report

- Titel des Reports?
- Soll ich dich nicht auf dem Report als Betreuerin erwähnen?
- Ist der Report richtig, es ist nicht zweispaltig?
- Gibt es eine Unter-/Obergrenze?
- Passt die neue Gliederung?
- Soll ich wirklich ein Kapitel Software Implementation machen zu dem package?
- Passt das Zitat beim HumanCellAtlas oder soll ich es weglassen?
- Was ist mein Projekt acronym? CLACELL?
- Dürfen andere bei meiner Präsi zuschauen, oder nur Prüfer?
- Präsentationssprache Englisch?
- Passt ein Zitat auf scikit-learn und scikit-optimize?
- Wie sehr muss ich darauf achten alles zu belegen? Und muss ich die Quellen alle gut kennen? Ich habe eine Quelle für BayesSearch

### Paper

- Wie soll es veröffentlicht werden?
- Hier schon einmal präsentieren? https://gcb2026.de/

### Allgemein

- Hast du Präferenzen für welche Metriken wichtiger sind?
- Kann ich auch einfach nur die besten Modelle in den Grafiken anzeigen? Sonst wird es sehr voll
- Test mit Anzahl an unterschiedlichen predictions bei Mehrfachem Ausführen löschen?

