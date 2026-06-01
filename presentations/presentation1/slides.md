---
# try also 'default' to start simple
theme: seriph
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
# some information about your slides (markdown enabled)
title: Welcome to Slidev
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
# apply UnoCSS classes to the current slide
class: text-left
# https://sli.dev/features/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# enable Comark Syntax: https://comark.dev/syntax/markdown
comark: true
# duration of the presentation
duration: 35min
---

# Erste Präsentation am 16.04.26

---

## Aufbau der Pipeline


1. **Pre-processing**
  1.1 *Quality Control* (Filtert nur Daten von echten lebenden Zellen heraus
  1.2 *Normalization* (e.g. count depth scaling)
  1.3 *evtl noch data correction*
2. **Dimensionalitätsreduktion**
  2.1 *Feature Selection*: nur Features mit hoher Varianz behalten
  2.2 *Dimensionalitätsreduktion*
3. **Klassifizierungsstrategien**
  3.1 **Marker-based Annotation**: Clustering und dann Klassifizierung der Cluster
  3.2 **Machine Learning**
  3.3 **Deep Learning**
4. **Evaluation**

=> Passt die Pipeline so? -> Fertigpiepelien nehmen, NFCORE, nextflow als Sprache, SCDownstream macht alles bis Schritt 2

---


## Python Übersetzung der R Marker-based Annotation Strategy 

- Die Annotation Strategy aus dem R Ordner in scumi-dev wurde in python übersetzt
- Es konnte kein aussagekräftiger Test gemacht werden, da die Daten fehlen
- Ich benötige Count-Matrix (Gene x Zellen) und Markerdefinitionen

=> Wie kann ich auf die Daten zugreifen?
-> Ich kann preprocessed Daten bekommen (keine FastQ file sondern eine Matrix, mehr nicht), muss keine Exakte Übereinstimmung mit R package sein, 95% reichen auch

pixie statt conda zur requirements Verwaltung

---

## Ergebnis Literaturrecherche

- Current best practices in single-cell RNA-seq analysis: a tutorial, Luecken, M. D., & Theis, F. J. (2019), https://web.archive.org/web/20201103060108/https://mediatum.ub.tum.de/doc/1545615/document.pdf : Beschreibt die Pipeline mit einigen Hinweisen
- A comparison of automatic cell identification methods for single-cell RNA sequencing data, Tamim Abdelaal1,2†, Lieke Michielsen1,2†, Davy Cats3, Dylan Hoogduin3, Hailiang Mei3, Marcel J. T. Reinders1,2 and Ahmed Mahfouz (2019), https://link.springer.com/content/pdf/10.1186/s13059-019-1795-z.pdf : Vergleich unterschiedlicher Klassifikationsmethoden für scRNA



Nächstes Treffen: Mo, 27.04. 16 Uhr - alle zwei Wochen, 21. Mai 14:30 ist Ausweichtermin wegen Pfingsten (über Zoom)
