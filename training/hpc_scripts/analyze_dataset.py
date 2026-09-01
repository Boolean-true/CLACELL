import anndata as ad
import pandas as pd
import itertools
import numpy as np
import pandas as pd
from concurrent.futures import ProcessPoolExecutor
import itertools
import os


H5AD_PATH = "/home/woody/iwbn/iwbn133h/data/10x-gex/ovarian/f8f7f2b0-b8a5-4087-8048-8d3f5b6a49dd.h5ad"
TARGET_MIN = 0.20
TARGET_MAX = 0.35
TARGET_CENTER = 0.275
DONOR_COL = "donor_id"
LABEL_COL = "author_cell_type"

# ==========================================
# 1. NUR METADATEN LADEN (SCHONER FÜR DEN RAM)
# ==========================================
# Wir lesen nur die .obs Tabelle aus, ohne die schwere X-Matrix in den RAM zu laden
obs_df = ad.read_h5ad(H5AD_PATH, backed="r").obs[[DONOR_COL, LABEL_COL]].copy()

donor_counts = obs_df[DONOR_COL].value_counts().sort_index()
total_cells = donor_counts.sum()
donors = donor_counts.index.tolist()

print("Cells pro Donor:\n", donor_counts)
print("\nGesamtzahl Zelle:", total_cells)

# Pre-computing als leichte globale Primitiven (Ints, Sets, Dicts)
cell_dict = donor_counts.to_dict()
class_dict = obs_df.groupby(DONOR_COL)[LABEL_COL].apply(set).to_dict()
all_classes = set(obs_df[LABEL_COL].unique())

# obs_df wird nicht mehr benötigt -> Speicher freigeben
del obs_df

print(f"Anzahl eindeutiger Klassen ({LABEL_COL}): {len(all_classes)}")


# ==========================================
# 2. SCHNELLE EVALUIERUNG OHNE PRINT & DICTS
# ==========================================
def evaluate_combination(test_donors):
    """Gibt nur (score, test_donors) zurück, um den Puffer klein zu halten."""
    test_cells = sum(cell_dict[d] for d in test_donors)
    test_ratio = test_cells / total_cells

    # Early Exit: Ratio muss im Bereich liegen
    if not (TARGET_MIN <= test_ratio <= TARGET_MAX):
        return None

    # Klassen im Test-Set prüfen
    test_classes = set().union(*(class_dict[d] for d in test_donors))
    if test_classes != all_classes:
        return None

    # Klassen im Train-Set prüfen
    train_donors = [d for d in donors if d not in test_donors]
    train_classes = set().union(*(class_dict[d] for d in train_donors))
    if train_classes != all_classes:
        return None

    score = abs(test_ratio - TARGET_CENTER)
    # Keinesfalls print() hier verwenden!
    #print(f"test_ratio: {test_ratio}, train_donors: {train_donors}, test_donors: {list(test_donors)}", flush=True)
    return (score, test_donors, test_ratio, test_cells)


def gen_all_combinations():
    for r in range(1, len(donors)):
        for comb in itertools.combinations(donors, r):
            yield comb


# ==========================================
# 3. PARALLELE AUSFÜHRUNG
# ==========================================
if __name__ == "__main__":
    num_cores = min(os.cpu_count() or 1, 16)
    print(f"\nStarte parallele Prüfung auf {num_cores} CPU-Kernen...")

    best_split = None
    best_score = np.inf

    with ProcessPoolExecutor(max_workers=num_cores) as executor:
        for res in executor.map(
            evaluate_combination, gen_all_combinations(), chunksize=2000
        ):
            if res is not None:
                score, test_donors, test_ratio, test_cells = res
                if score < best_score:
                    best_score = score
                    best_split = {
                        "train_donors": [
                            d for d in donors if d not in test_donors
                        ],
                        "test_donors": list(test_donors),
                        "test_ratio": test_ratio,
                        "test_cells": int(test_cells),
                    }

    # ==========================================
    # 4. DATEN ERST JETZT IN DEN SPEICHER LADEN
    # ==========================================
    if best_split is None:
        print("\n[!] Kein gültiger Split gefunden.")
    else:
        print("\nBEST SPLIT GEFUNDEN")
        print("-" * 40)
        print("Train Donors:", best_split["train_donors"])
        print("Test Donors :", best_split["test_donors"])
        print(f"Test Anteil : {best_split['test_ratio']:.3f}")

        print("\nLade AnnData-Objekt zum Slicen...")
        adata = ad.read_h5ad(H5AD_PATH)
        #adata = adata.raw.to_adata()

        train_adata = adata[
            adata.obs[DONOR_COL].isin(best_split["train_donors"])
        ].copy()
        test_adata = adata[
            adata.obs[DONOR_COL].isin(best_split["test_donors"])
        ].copy()

        print("Train shape:", train_adata.shape)
        print("Test shape :", test_adata.shape)



# End the test execution
quit()

adata = ad.read_h5ad('/home/woody/iwbn/iwbn133h/data/10x-gex/ovarian/f8f7f2b0-b8a5-4087-8048-8d3f5b6a49dd.h5ad')

# Use raw counts
adata = adata.raw.to_adata()

# == 1. Overview of the Dataset ==

print(adata)

print(adata.obs['author_cell_type'].value_counts())


# == 2. Best Donor Split ==


# ==========================================
# 1. KONFIGURATION & DATEN-VORBEREITUNG
# ==========================================
TARGET_MIN = 0.20
TARGET_MAX = 0.35
TARGET_CENTER = 0.275
DONOR_COL = "donor_id"
LABEL_COL = "author_cell_type"

# Zellzahlen & Donoren
donor_counts = adata.obs[DONOR_COL].value_counts().sort_index()
total_cells = donor_counts.sum()
donors = donor_counts.index.tolist()

print("Cells pro Donor:")
print(donor_counts)
print("\nGesamtzahl:", total_cells)

# PRE-COMPUTING (Wichtigster Geschwindigkeits-Boost)
# Daten aus Pandas in native Python Dictionaries & Sets umwandeln
cell_dict = donor_counts.to_dict()
class_dict = adata.obs.groupby(DONOR_COL)[LABEL_COL].apply(set).to_dict()
all_classes = set(adata.obs[LABEL_COL].unique())

print(f"Anzahl eindeutiger Klassen ({LABEL_COL}): {len(all_classes)}")


# ==========================================
# 2. PRÜFFUNKTION FÜR EINZELNE KOMBINATION
# ==========================================
def evaluate_combination(test_donors):
    """Prüft eine Donorkombination extrem schnell ohne Pandas-Overhead."""
    # 1. Schnelle Verhältnis-Prüfung (Early Exit)
    test_cells = sum(cell_dict[d] for d in test_donors)
    test_ratio = test_cells / total_cells

    if not (TARGET_MIN <= test_ratio <= TARGET_MAX):
        return None

    # 2. Klassen-Prüfung für Test-Split (nur wenn Ratio im Zielbereich liegt)
    test_classes = set().union(*(class_dict[d] for d in test_donors))
    if test_classes != all_classes:
        return None

    # 3. Klassen-Prüfung für Train-Split
    train_donors = [d for d in donors if d not in test_donors]
    train_classes = set().union(*(class_dict[d] for d in train_donors))
    if train_classes != all_classes:
        return None

    # Target-Score berechnen
    score = abs(test_ratio - TARGET_CENTER)

    print(f"test_ratio: {test_ratio}, train_donors: {train_donors}, test_donors: {list(test_donors)}")
    return {
        "score": score,
        "train_donors": train_donors,
        "test_donors": list(test_donors),
        "test_ratio": test_ratio,
        "test_cells": int(test_cells),
    }


# ==========================================
# 3. PARALLELE AUSFÜHRUNG
# ==========================================
def gen_all_combinations():
    """Generator für alle Donor-Kombinationen von Größe 1 bis N-1."""
    for r in range(1, len(donors)):
        for comb in itertools.combinations(donors, r):
            yield comb


if __name__ == "__main__":
    num_cores = os.cpu_count()
    num_cores = min(num_cores, 32)
    print(f"\nStarte parallele Prüfung auf {num_cores} CPU-Kernen...")

    best_split = None
    best_score = np.inf

    # ProcessPoolExecutor verteilt die Arbeit effizient in Chunks
    with ProcessPoolExecutor(max_workers=num_cores) as executor:
        # chunksize verhindert Prozess-Overhead bei Millionen von Kombinationen
        results = executor.map(
            evaluate_combination, gen_all_combinations(), chunksize=5000
        )

        for res in results:
            if res is not None and res["score"] < best_score:
                best_score = res["score"]
                best_split = res

    # ==========================================
    # 4. ERGEBNIS-AUSGABE & SPLIT ANWENDEN
    # ==========================================
    if best_split is None:
        print(
            "\n[!] Kein gültiger Split gefunden, der alle Ziel- und"
            " Klassen-Kriterien erfüllt."
        )
    else:
        print("\nBEST SPLIT")
        print("-" * 40)
        print("Train Donors:", best_split["train_donors"])
        print("Test Donors :", best_split["test_donors"])
        print(f"Test Anteil : {best_split['test_ratio']:.3f}")
        print(f"Test Zellen : {best_split['test_cells']}")

        # AnnData aufteilen
        train_adata = adata[
            adata.obs[DONOR_COL].isin(best_split["train_donors"])
        ].copy()
        test_adata = adata[
            adata.obs[DONOR_COL].isin(best_split["test_donors"])
        ].copy()

        print("\nTrain shape:", train_adata.shape)
        print("Test shape :", test_adata.shape)



# End the test execution
quit()
# OLD

TARGET_MIN = 0.20
TARGET_MAX = 0.35
TARGET_CENTER = 0.275
DONOR_COL = "donor_id"
LABEL_COL = "author_cell_type"

# 1. Zellen pro Donor ermitteln und ausgeben
donor_counts = adata.obs[DONOR_COL].value_counts().sort_index()
total_cells = donor_counts.sum()

print("Cells pro Donor:")
print(donor_counts)
print("\nGesamtzahl:", total_cells)

# 2. Alle existierenden Klassen ermitteln
all_classes = set(adata.obs[LABEL_COL].unique())
print(f"Anzahl eindeutiger Klassen ({LABEL_COL}): {len(all_classes)}")

# Besten Split initialisieren
best_split = None
best_score = np.inf
donors = donor_counts.index.tolist()

# 3. Alle Kombinationen von 1 bis len(donors) - 1 durchlaufen
for r in range(1, len(donors)):
    for test_donors in itertools.combinations(donors, r):
        test_donors_list = list(test_donors)
        test_cells = donor_counts[test_donors_list].sum()
        test_ratio = test_cells / total_cells

        # Kriterium: Test-Verhältnis im Zielbereich
        if test_ratio > TARGET_MAX or test_ratio < TARGET_MIN:
            continue

        train_donors_list = [d for d in donors if d not in test_donors_list]

        # Kriterium: Prüfen, ob alle Klassen im Train-Split vorhanden sind
        train_classes = set(adata.obs.loc[adata.obs[DONOR_COL].isin(train_donors_list), LABEL_COL].unique())
        if train_classes != all_classes:
            continue

        # Kriterium: Prüfen, ob alle Klassen im Test-Split vorhanden sind
        test_classes = set(adata.obs.loc[adata.obs[DONOR_COL].isin(test_donors_list), LABEL_COL].unique())
        if test_classes != all_classes:
            continue

        # Score berechnen (Abweichung von TARGET_CENTER)
        score = abs(test_ratio - TARGET_CENTER)

        if score < best_score:
            best_score = score
            best_split = {
                "train_donors": train_donors_list,
                "test_donors": test_donors_list,
                "test_ratio": test_ratio,
                "test_cells": int(test_cells)
            }

# Ergebnisausgabe
if best_split is None:
    print("\n[!] Kein gültiger Split gefunden, der alle Ziel- und Klassen-Kriterien erfüllt.")
else:
    print("\nBEST SPLIT")
    print("-" * 40)

    print("Train Donors:")
    print(best_split["train_donors"])

    print("\nTest Donors:")
    print(best_split["test_donors"])

    print(f"\nTest Anteil: {best_split['test_ratio']:.3f}")
    print(f"Test Zellen: {best_split['test_cells']}")

    # Split anwenden
    train_adata = adata[
        adata.obs[DONOR_COL].isin(best_split["train_donors"])
    ].copy()

    test_adata = adata[
        adata.obs[DONOR_COL].isin(best_split["test_donors"])
    ].copy()

    print("\nTrain shape:", train_adata.shape)
    print("Test shape :", test_adata.shape)
