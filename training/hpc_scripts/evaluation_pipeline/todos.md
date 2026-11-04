# TODOs bei der evaluation_pipeline

- Punkte aus Opencode Session nochmal durchgehen (2.3, 2.6)
- Autoencoder + Conditional Autoencoder bekommen aktuell die Laufzeit für die Feature Importance (für Custom Ensemble) mit angerechnet -> entfernen!
- SCRIPT_DIR in allen sh scripts evtl hardcoden

## Lesen
- prüfen ob die zeitmessung jetzt wirklich alles beinhaltet
- bei beiden autoencodern prüfen, ob es immer noch dopplungen bei methoden gibt

## Nach dem Probelauf

- custom ensemble soll schon alle versionen drin haben (stacking, stacking passthrough, voting usw)
?- scCAT oder spatialCAT statt clacell?
?- noqa aus run_task.py entfernen?
- alle cvs auf die werte aus den python files setzen und nicht dynamisch machen. macht aber keinen unterschied wenn ich immer mindestens 5 zellen pro zelltyp im train split habe
!!- feature importance für robustness tests für die 4 datensätze berechnen und verwenden (nicht die von linsvc oder rf!) -> FI rein aus Differenzielle Genexpression erstellen für alle 4 Datensätze
- output path (aktuell: <output_root>/<experiment>/<dataset>/results/<model>/coarse/result_<i>.csv) evtl anpassen
- prüfen ob das DataFrame als Input für das CustomEnsemble passt

## Evtl

- orchestrate.py beinhaltet auch eine implementierung um mit einem job alles zu machen, das ist dann aber halt ein 24h job, der wird zeitlich nicht ausreichen und parallelisert dementsprechend weniger als einzelne jobs für z.b. tuning

## Anmerken

- den ganzen ablauf nochmal erklären lassen. das was ich starte submitted dann eigene jobs? was wird parallelisiert? verlangsamt das nicht das ganze?
- folderstruktur auf dem hpc geben und fragen, ob dort alle dateien gefunden werden


## Submitted Jobs

1. Pilot: Submitted batch job 12836744
SCRIPT_DIR gehardcoded: Submitted batch job 12841141
Submitted batch job 12841352 -> Klappt. Es gibt aber nur einen job für je fi, tune, run, aggregate. prüfen wie das wiederaufnehmen geht, 24h werden wahrscheinlich nicht für alle ansätze reichen
submit_features geht mit dem script dir nicht, manuell gestartet: Submitted batch job 12841949
einzeln submit_features.sh starten hat nicht geklappt, daher nur alle sachen nach prepare und orchestrate ausgeführt: Submitted batch job 12842012