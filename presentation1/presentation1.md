# Erste Präsentation

## Aufbau der Pipeline

1. **Pre-processing**
  1.1 *Quality Control* (Filtert nur Daten von echten lebenden Zellen heraus (Probleme: Zelltod, Doubletten mit zwei Zellen als eine einzige, Leeres Tröpfchen wo keine Zelle drin ist sondern nur Hintergrundrauschen), filtert auch zero count genes heraus)
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


## Python Übersetzung der R Marker-based Annotation Strategy 

TODO: Was soll ich da zeigen?


## Ergebnis Literaturrecherche

- Current best practices in single-cell RNA-seq analysis: a tutorial, Luecken, M. D., & Theis, F. J. (2019), https://web.archive.org/web/20201103060108/https://mediatum.ub.tum.de/doc/1545615/document.pdf : Beschreibt die Pipeline mit einigen Hinweisen
- A comparison of automatic cell identification methods for single-cell RNA sequencing data, Tamim Abdelaal1,2†, Lieke Michielsen1,2†, Davy Cats3, Dylan Hoogduin3, Hailiang Mei3, Marcel J. T. Reinders1,2 and Ahmed Mahfouz (2019), https://link.springer.com/content/pdf/10.1186/s13059-019-1795-z.pdf : Vergleich unterschiedlicher Klassifikationsmethoden für scRNA

TODO: Was soll ich da zeigen?



## Fragen

- Wie kann ich auf die Daten zugreifen?
- Passt die Pipeline so?
