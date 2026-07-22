# Mitschrieb

- Box Plots erstellen! (für Tabelle (für jede Spalte einen Plot, x-achse sind die modelle (zeilen) und y-achse dann die jeweilige Metrik (z.B. Macro F1, RAM Peak usw)) und bei Zellenvergleich (aktuell ein Barplot))
- Im Report und in der Präsi eine Anleitung wie man das Package nutzt und damit einen fertigen Classifier erstellt
- Keine Livedemo, wenn dann Video aber nicht notwendig
- Graphical Abstract (zusätzlich)
- Unterpunkte zu allen subchapters und chapters und an Anne schicken!!
- Headings bei Output von Robustness Report nutzen (damit man es im browser anzeigen kann)
- Scores fett machen
- evtl Plots einbauen (muss ich aber nicht machen)
- Ich kann Anne noch auf die Titelseite des Papers dazuschreiben
- Ich habe keine Obergrenze als Seitenzahl einfach alles beschreiben, was ich will in dem Detailgrad den ich will (aber keine unnötigen Wörter)
- CLACELL ist mein Projekt acronym
- Ein Zitat auf scikit-learn passt
- Auf englisch präsentieren

- Funktionsweise der Vergleichsmodelle anschauen!

- Nächste Woche Montag bei Anne melden ob ich noch einen Termin brauche
- Anne fragt David wegen der German Conference on Bioinformatics (GCB2026)
- Anne fragt bei David nach, ob ich das Hauptseminar so machen kann
- Wenn es als Paper veröffentlicht wird, soll ich es vorher noch auf feineren Daten evaluieren (Anne würde sich dann um Daten kümmern)
- Bessere Abkürzung als CLACELL suchen (mit robust drinnen)


# Jobs auf dem HPC

CLACELL
Submitted batch job 12092020
Submitted batch job 12092037
Submitted batch job 12092039

CLACELL mit bayes_search: Submitted batch job 12098933
Submitted batch job 12100465
Submitted batch job 12100470

CLACELL mit bayes_search und complete pipeline: Submitted batch job 12100501
Submitted batch job 12100507
Submitted batch job 12100515
Submitted batch job 12102567
Submitted batch job 12102968
Submitted batch job 12103322
Submitted batch job 12109711
Submitted batch job 12110026

LinearSVC Bayes mit minimalen Anpassungen zum Zeit messen: Submitted batch job 12122394
LinearSVC Bayes mit minimalen Anpassungen zum Zeit messen auf $WORK: Submitted batch job 12122503
Submitted batch job 12122520

SingleR auf $WORK: Submitted batch job 12124716
Submitted batch job 12124719
SingleR auf $WORK mit env auf $WORK: Submitted batch job 12125986

CellTypist auf $WORK: Submitted batch job 12124717
Submitted batch job 12124720
CellTypist Bayes auf $WORK mit env auf $WORK: Submitted batch job 12124725
Submitted batch job 12124726
Submitted batch job 12124729
Submitted batch job 12124733
Submitted batch job 12124757

CellTypist auf $WORK und clacell env:
1: Submitted batch job 12128062
2: Submitted batch job 12128063
3: Submitted batch job 12128064


SingleR ohne bulking: Submitted batch job 12098385


Conditional Autoencoder mit 30% noise wie Autoencoder: 12109699
TODO: Andere Dropout rate bei CAE, Andere Architektur bei CAE -> noch einen run machen, bei dem das alles gleich ist! Vorher aber checken, ob ich die jeweilige Architektur wissenschaftlich begründen kann!!!


## Autoencoder

Anpassung auf Architektur aus Literatur

LR: Submitted batch job 12113310
Submitted batch job 12113344
9: Submitted batch job 12128169

LinearSVC: Submitted batch job 12113311
Submitted batch job 12113345

RF: Submitted batch job 12113312
Submitted batch job 12113346
10+: Submitted batch job 12121788

## Conditional Autoencoder

Anpassung auf Architektur vom Denoising Autoencoder

LR: Submitted batch job 12113339
9: Submitted batch job 12128630

LinearSVC: Submitted batch job 12113340

RF: Submitted batch job 12113329
10+: Submitted batch job 12121789


## V3 with Dropout Layer in Decoder

### Autoencoder

LR: Submitted batch job 12132616

LinerSVC: Submitted batch job 12132650

RF: Submitted batch job 12132558
10+: Submitted batch job 12132561

### Conditional Autoencoder

LR: Submitted batch job 12132680

LinearSVC: Submitted batch job 12132693

RF: Submitted batch job 12132458
10+: Submitted batch job 12132459