# TODOs bei der evaluation_pipeline

- custom ensemble soll schon alle versionen drin haben (stacking, stacking passthrough, voting usw)
- scCAT oder spatialCAT statt clacell?
- noqa aus run_task.py entfernen?
- bootstrap.py auf hpc ordnerstruktur anpassen
- die namen für technical metrics sollten identisch mit den bisherigen sein
!!- feature importance für robustness tests für die 4 datensätze berechnen und verwenden (nicht die von linsvc oder rf!)
- autoencoder linsvc hyperparameter space prüfen auch im vergleich zu conditional autoencoder. aktuell ist er anders als im eigentlichen skript
- linearsvc bei custom ensemble in calibratedclassifier
- prüfen ob die zeitmessung jetzt wirklich alles beinhaltet
- bei beiden autoencodern prüfen, ob es immer noch dopplungen bei methoden gibt
- alle cvs auf die werte aus den python files setzen und nicht dynamisch machen. macht aber keinen unterschied wenn ich immer mindestens 5 zellen pro zelltyp im train split habe
- breast datensatz für probelauf nehmen

## Anmerken

- sollte die feature importance von linsvc + rf auch einmal pro seed berechnet werden?
- den ganzen ablauf nochmal erklären lassen. das was ich starte submitted dann eigene jobs? was wird parallelisiert? verlangsamt das nicht das ganze?
- das ist an einigen stellen aufgebjäht, reduzieren
- was ist der vorteil bei z.b. dem autoencoder alles in einzelne funktionen zu packen gegenüber einem script von anfang bis ende wie bisher?
