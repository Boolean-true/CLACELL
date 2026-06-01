
# Zweite Präsentation am 27.04.26

---

## Pipeline & Daten

- Passen die Daten die ich verwende?
- Soll ich auf die Daten noch SCDownstream anwenden?
- Werden die Daten immer das Ergebnis aus nfcore sein, oder muss ich das bei anderen Daten auch anwenden?
- Passen die Marker Gene aus scumi-dev? Oder bekomme ich noch andere?

---

## Vergleich scumi-dev R annotation strategy mit python Implementierung

- Ich habe ein Script dafür angefangen
- Für die python Implementierung habe ich es mir auch in einem Notebook angeschaut
- Problem: alter R Code, benötigt alte Version von Seurat -> macht Probleme
- 1. Versuch: Arch Linux mit Rscript in der Command Line sowie Aufruf über rpy2 in python -> fail
- 2. Versuch: Windows mit Rscript in der Command Line sowie Aufruf über rpy2 in python -> fail
- 3. Versuch: Docker mit den R files -> fail
- 4. Versuch: Arch Linux mit Nix (packetmanager) -> erster Test hat funktioniert



## Mitschrieb

- Die daten sind alle prozessiert, evtl sind nicht alle Gene drinnen
- Die h5ad files in den ersten 4 Ordnern in blood enthalten Genüberschneidungen, aber überschneiden sich nicht komplett (z.B. 800/1000 überschneiden sich)
- SRR enthält das was aus der Pipeline kommt
- noch nicht so relevant welche Daten
- scdownstream bringt nicht viel, nur bei Rohdaten -> erstmal weglassen
- Eingabe ist h5ad file, Preprocessing mit scdownstreaming ist dem Nutzer überlassen muss ich nicht machen
- marker gene aus scumi dev passen
- pixi.sh als environment als Alternative für Nix für scumi-dev (da gibt es ein environment file mit allen dependencies und Versionen (von KI holen))
- CellTypist ist ein Tool mit DeepLearning (braucht GPU)
- Tools muss man trotzdem evtl neu trainieren weil wir unsere eigenen Label in den Trainingsdaten haben wollen
- CellTypist Paper anschauen und Korpus der anotierten trainingsdaten finden (evtl cellxgenes website)
- sctype als Referenz für marker based annotation strategy
- Evtl gibt mir Anne noch Daten und Marker (als echte Daten)

### Nächste Schritte 
- scumi-dev zum laufen bringen (Nix und pixi.sh probieren)
- Zeit messen bei scumi-dev und bei python Implementierung (10 min ist zu lang, R ist langsamer als Python)
- trainingsdaten suchen 
- Random Forest anschauen
- scumi-dev evaluieren und welche Markergene relevant sind




[workspace]
authors = ["Julian Kraus <j.kraus.2301@gmail.com>"]
channels = ["conda-forge", "bioconda"]
name = "Project_CLACELL"
platforms = ["linux-64"]
version = "0.1.0"

[dependencies]
# R-Basisversion (4.0/4.1 ist ideal für Seurat v3)
r-base = ">=4.0,<4.1"
# Seurat v3-Ära
r-seurat = "3.2.3"
# Notwendige Abhängigkeiten für scumi-dev / sc-Bioinformatik
r-devtools = "*"
r-biocmanager = "*"
r-rcpp = "*"

# --- Python-Stack ---
# Python massiv modernisieren
python = "3.10.*" # 3.10 ist oft stabiler für rpy2 als 3.9
anndata = ">=0.10.7" 
scanpy = ">=1.9"
pandas = ">=2.0"
numpy = ">=1.23,<2.0"
rpy2 = "*"
h5py = ">=3.10"

[tasks]
# Task zum Installieren von scumi-dev direkt aus GitHub innerhalb der R-Umgebung
install-scumi = "Rscript -e 'devtools::install_github(\"igrabski/scumi-dev\")'"
# Startet eine interaktive R-Session in der Umgebung
r-shell = "R"
