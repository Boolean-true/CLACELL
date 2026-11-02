# TODOs bei der evaluation_pipeline

- Punkte aus Opencode Session nochmal durchgehen

## Lesen
- prüfen ob die zeitmessung jetzt wirklich alles beinhaltet
- bei beiden autoencodern prüfen, ob es immer noch dopplungen bei methoden gibt

## Nach dem Probelauf

- custom ensemble soll schon alle versionen drin haben (stacking, stacking passthrough, voting usw)
?- scCAT oder spatialCAT statt clacell?
?- noqa aus run_task.py entfernen?
- alle cvs auf die werte aus den python files setzen und nicht dynamisch machen. macht aber keinen unterschied wenn ich immer mindestens 5 zellen pro zelltyp im train split habe
!!- feature importance für robustness tests für die 4 datensätze berechnen und verwenden (nicht die von linsvc oder rf!)
- output path (aktuell: <output_root>/<experiment>/<dataset>/results/<model>/coarse/result_<i>.csv) evtl anpassen
- prüfen ob das DataFrame als Input für das CustomEnsemble passt

## Anmerken

- den ganzen ablauf nochmal erklären lassen. das was ich starte submitted dann eigene jobs? was wird parallelisiert? verlangsamt das nicht das ganze?
- folderstruktur auf dem hpc geben und fragen, ob dort alle dateien gefunden werden


## Submitted Jobs

1. Pilot: Submitted batch job 12836744