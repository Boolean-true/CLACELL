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
title: Presentation 8 am 28.10.2026
mdc: true
---

# Presentation 8 am 28.10.2026

---

## Mapping Coarse auf Fine Grained

<div class="flex justify-center">
  <img src="/spatial_breast_celltype_mapping_slide.png" alt="Spatial Breast Celltype Mapping" class="w-[95%] max-w-full h-auto" />
</div>

---


## Rejection Class Implementierungen

- PyOD im Ensemble-Output Space: IsolationForest auf den Wahrscheinlichkeiten der Modelle des Custom Ensembles (Base Rfs + Meta LR) -> Problem: Batch Effekt wirkt stärker als initial angenommen
- PyOD Entropy: Statt den direkten Wahrscheinlichkeiten wird die maximale Wahrscheinlichkeit, Entropy und der Margin zwischen bester und zweitbester Klasse als Input für den KNN verwendet (Fokus auf Model Uncertainty)
- Ensemble Disagreement: Standardabweichung der Wahrscheinlichkeiten der Basis RFs wird berechnet; zur Rejection wird anhand eines Schwellenwertes rejected (95. bzw. 90. Percentile des Trainingsdatensatzes)
- Vorhersage-Entropie: Entropie auf Wahrscheinlichkeiten berechnet und anhand eines Schwellenwertes rejected (95. Percentile des Trainingsdatensatzes)

---

## Ergebnisse auf Spatial

| Classifier | Coarse Rejected | Fine Rejected | Coarse Macro F1 | Fine Macro F1 |
| --- | --- | --- | --- | --- |
| No Rejection | 0% | 0% | 83% | 44.7% |
| PyOD Ensemble-Output | 99% | 99% | 2.3% | 0.7% |
| PyOD Entropy | 15.7% | 37% | 67.7% | 27.7% |
| Ensemble Disagreement 0.95 | 4.4% | 11.7% | 69.7% | 38.2% |
| Ensemble Disagreement 0.9 | 9% | 15.8% | 66.5% | 34.4% |
| Vorhersage-Entropie | 17% | 51.8% | 69.3% | 27.9% |

Wenn man bei Ensemble Disagreement 0.95 die Rejection Class weglässt, kommt man auf 78.4% Macro F1 bei Coarse und 39.1% Macro F1 bei Fine Grained -> immer noch niedriger als ohne Rejection Class

---

## Ensemble Disagreement Coarse Classification Report 

                               precision          recall        f1-score         support

                  B cell 0.9029 +- 0.0078 0.6329 +- 0.0145 0.7441 +- 0.0102   3032.0 +- 0.0
        Endothelial cell 0.9778 +- 0.0018 0.8938 +- 0.0079 0.9339 +- 0.0043   1352.0 +- 0.0
         Epithelial cell 0.9168 +- 0.005 0.8826 +- 0.0082 0.8993 +- 0.0048  13395.0 +- 0.0
            Myeloid cell 0.9826 +- 0.001 0.8737 +- 0.0086 0.9249 +- 0.0049   7844.0 +- 0.0
     Natural killer cell   0.7 +- 0.0083 0.2215 +- 0.0127 0.3363 +- 0.0146   1768.0 +- 0.0
             Plasma cell 0.9204 +- 0.0089 0.4616 +- 0.0233 0.6145 +- 0.0215    989.0 +- 0.0
                Rejected      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0      0.0 +- 0.0
            Stromal cell 0.9843 +- 0.0009 0.9148 +- 0.0075 0.9483 +- 0.0041   3657.0 +- 0.0
                  T cell 0.8148 +- 0.0017 0.9377 +- 0.0038 0.8719 +- 0.001  15281.0 +- 0.0

                accuracy                                 0.8522 +- 0.0021  47318.0 +- 0.0
               macro avg   0.8 +- 0.0015 0.6465 +- 0.002 0.697 +- 0.0018  47318.0 +- 0.0
            weighted avg 0.8928 +- 0.0012 0.8522 +- 0.0021 0.8625 +- 0.0012  47318.0 +- 0.0


---

<div class="flex justify-center">
  <img src="/sparse_fine_grained_macro_f1_per_coarse_cell_type.png" alt="Spatial Breast Celltype Mapping" class="w-[95%] max-w-full h-auto" />
</div>

---

## Weiteres Vorgehen

- Rejection Class verbessern
- Evtl LightGBM statt RF verwenden für eine bessere Leistung bei sparse Daten
- Evtl Trainings und Testdaten anpassen (Anzahl Donors)
- CATBoost evaluieren