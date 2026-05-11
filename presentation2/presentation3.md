
# 3. Präsentation am 11.05.26

---

## Ergebnisse

- scumi-dev läuft nicht
- python reimplementierung: 20 min zu 16,5 min
- Trainingsdaten aus CellTypist habe ich gefunden -> sehen so weit gut aus
- Bei Random Forest wird Preprocessing benötigt

---

## Weiteres Vorgehen

- Preprocessing des CellTypist Datensatzes für ML Algorithmen
- Tests für robusten Klassifikator
- Training verschiedener ML Algorithmen und Tests zur Robustheit

---

## Fragen

- Passen die Annotationen in dem Datensatz?
- Nehmen wir deine Daten als Testdatensätze und die CellTypist zum Training?
- Wie annotieren wir die Testdatensätze?
- Tipps/Hinweise zum Preprocessing?

---

## Mitschrieb

- CodeProfiler, wo ist Bottleneck bei python reimplementierung
- pca und knn graph aus loop raus (alles was nur einmal berechnet werden muss)
- sc-type als Alternative -> Vergleichen bzgl Laufzeit und Ergebnissen
- Testdaten mit marker based annotieren
- scanpy anschauen für Preprocessing oder sc-best-practices (Buch) als Bckground
- Zellzyklusgene, Mitochondrial genes und Ribosomialgenes alles raus
- Pipeline aufbauen und dann alle drei versionen testen
- scumi-dev bzw sc-type soll ziemlich schnell sein (evtl parallelisieren)
- bei robustheitstests zwei stück: biased (gene die z.B. RF interessant fand) und random x10 oder 20 und dann mitteln; evtl dritter test noch: biased und immer die aus den top 100 oder 25 genen pro zelltyp schmeißt mman was raus



---

### Output von python reimplementierung

SelectionResult(auc_final=B cell                         0.986297
CD14+ monocyte                 0.986196
CD16+ monocyte                 0.976820
CD4+ T cell                    0.995351
Cytotoxic T cell               0.983757
Dendritic cell                 0.992736
Megakaryocyte                  0.992833
Natural killer cell            0.991277
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.996424
dtype: float64, label_final=CAATTTCAGACCCGCT            CD4+ T cell
TAATTCCGTCCATACA         CD14+ monocyte
ACAGGGATCTCTTAAC            CD4+ T cell
CATTCCGAGTGAGTGC         CD14+ monocyte
GTTGAACCACTGCGAC         CD14+ monocyte
                           ...         
AAGCGTTAGACTTCCA         CD14+ monocyte
GTGGCGTGTAGAATGT         CD14+ monocyte
CGATCGGGTAGAATGT    Natural killer cell
GAGGGTAGTAGATCCT       Cytotoxic T cell
TTACGTTAGGTAAGAG    Natural killer cell
Name: cluster, Length: 7610, dtype: object, params_final={'number_neighbor': 15, 'variable_gene': False, 'resolution': 0.8, 'num_pc': 50}, model_final=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA    12
GTGGCGTGTAGAATGT    12
CGATCGGGTAGAATGT    10
GAGGGTAGTAGATCCT    13
TTACGTTAGGTAAGAG    10
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 0.8, 'num_pc': 50, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), candidates=[ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     3
GTGGCGTGTAGAATGT    10
CGATCGGGTAGAATGT    17
GAGGGTAGTAGATCCT     6
TTACGTTAGGTAAGAG     6
Name: cluster, Length: 7610, dtype: object, auc=Series([], dtype: float64), silhouette=-1.0, num_clusters=22, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.0, 'num_pc': 100}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     3
GTGGCGTGTAGAATGT    10
CGATCGGGTAGAATGT    17
GAGGGTAGTAGATCCT     6
TTACGTTAGGTAAGAG     6
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.0, 'num_pc': 100, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     3
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT     5
CGATCGGGTAGAATGT    10
GAGGGTAGTAGATCCT    10
TTACGTTAGGTAAGAG    10
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.985082
CD14+ monocyte                 0.920535
CD16+ monocyte                 0.943589
CD4+ T cell                    0.993107
Cytotoxic T cell               0.972776
Dendritic cell                 0.838367
Megakaryocyte                  0.836710
Natural killer cell            0.982273
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.995746
dtype: float64, silhouette=0.15368024103751757, num_clusters=12, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 0.8, 'num_pc': 20}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     3
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT     5
CGATCGGGTAGAATGT    10
GAGGGTAGTAGATCCT    10
TTACGTTAGGTAAGAG    10
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 0.8, 'num_pc': 20, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     6
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     3
GTGGCGTGTAGAATGT     5
CGATCGGGTAGAATGT    10
GAGGGTAGTAGATCCT    10
TTACGTTAGGTAAGAG    10
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.981788
CD14+ monocyte                 0.934438
CD16+ monocyte                 0.950243
CD4+ T cell                    0.993614
Cytotoxic T cell               0.980144
Dendritic cell                 0.872144
Megakaryocyte                  0.854793
Natural killer cell            0.987328
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.995746
dtype: float64, silhouette=0.13899575634027453, num_clusters=14, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 0.8, 'num_pc': 30}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     6
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     3
GTGGCGTGTAGAATGT     5
CGATCGGGTAGAATGT    10
GAGGGTAGTAGATCCT    10
TTACGTTAGGTAAGAG    10
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 0.8, 'num_pc': 30, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     7
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT     4
CGATCGGGTAGAATGT    12
GAGGGTAGTAGATCCT    12
TTACGTTAGGTAAGAG    12
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.985082
CD14+ monocyte                 0.944297
CD16+ monocyte                 0.948908
CD4+ T cell                    0.993169
Cytotoxic T cell               0.972225
Dendritic cell                 0.994584
Megakaryocyte                  0.840314
Natural killer cell            0.981701
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.995746
dtype: float64, silhouette=0.13823903315768898, num_clusters=14, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.0, 'num_pc': 20}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     7
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT     4
CGATCGGGTAGAATGT    12
GAGGGTAGTAGATCCT    12
TTACGTTAGGTAAGAG    12
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.0, 'num_pc': 20, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     4
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     2
GTGGCGTGTAGAATGT    10
CGATCGGGTAGAATGT    13
GAGGGTAGTAGATCCT    13
TTACGTTAGGTAAGAG    13
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.981788
CD14+ monocyte                 0.934558
CD16+ monocyte                 0.949587
CD4+ T cell                    0.993914
Cytotoxic T cell               0.980371
Dendritic cell                 0.871956
Megakaryocyte                  0.853680
Natural killer cell            0.987328
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.995746
dtype: float64, silhouette=0.14046751976021563, num_clusters=16, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.0, 'num_pc': 30}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     4
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     2
GTGGCGTGTAGAATGT    10
CGATCGGGTAGAATGT    13
GAGGGTAGTAGATCCT    13
TTACGTTAGGTAAGAG    13
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.0, 'num_pc': 30, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     3
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     4
GTGGCGTGTAGAATGT     8
CGATCGGGTAGAATGT    12
GAGGGTAGTAGATCCT    15
TTACGTTAGGTAAGAG    12
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.981619
CD14+ monocyte                 0.946395
CD16+ monocyte                 0.949306
CD4+ T cell                    0.995406
Cytotoxic T cell               0.978714
Dendritic cell                 0.891813
Megakaryocyte                  0.905146
Natural killer cell            0.987214
Plasmacytoid dendritic cell    0.995746
dtype: float64, silhouette=0.14229613133415026, num_clusters=16, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 0.8, 'num_pc': 50}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     3
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     4
GTGGCGTGTAGAATGT     8
CGATCGGGTAGAATGT    12
GAGGGTAGTAGATCCT    15
TTACGTTAGGTAAGAG    12
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 0.8, 'num_pc': 50, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     3
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT     2
CGATCGGGTAGAATGT    14
GAGGGTAGTAGATCCT     2
TTACGTTAGGTAAGAG     2
Name: cluster, Length: 7610, dtype: object, auc=CD14+ monocyte                 0.933902
CD16+ monocyte                 0.960785
CD4+ T cell                    0.936636
Dendritic cell                 0.866099
Megakaryocyte                  0.930542
Natural killer cell            0.983804
Plasmacytoid dendritic cell    0.995890
dtype: float64, silhouette=0.10888492061206563, num_clusters=17, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 0.8, 'num_pc': 100}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     3
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT     2
CGATCGGGTAGAATGT    14
GAGGGTAGTAGATCCT     2
TTACGTTAGGTAAGAG     2
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 0.8, 'num_pc': 100, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     3
GTGGCGTGTAGAATGT    13
CGATCGGGTAGAATGT    14
GAGGGTAGTAGATCCT    15
TTACGTTAGGTAAGAG    14
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.973844
CD14+ monocyte                 0.943574
CD16+ monocyte                 0.954805
CD4+ T cell                    0.995414
Cytotoxic T cell               0.978858
Dendritic cell                 0.890645
Megakaryocyte                  0.898373
Natural killer cell            0.987452
Plasmacytoid dendritic cell    0.995746
dtype: float64, silhouette=0.13264152970041485, num_clusters=19, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.0, 'num_pc': 50}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     3
GTGGCGTGTAGAATGT    13
CGATCGGGTAGAATGT    14
GAGGGTAGTAGATCCT    15
TTACGTTAGGTAAGAG    14
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.0, 'num_pc': 50, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     6
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     7
GTGGCGTGTAGAATGT    19
CGATCGGGTAGAATGT    16
GAGGGTAGTAGATCCT    22
TTACGTTAGGTAAGAG    16
Name: cluster, Length: 7610, dtype: object, auc=Series([], dtype: float64), silhouette=-1.0, num_clusters=23, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.2, 'num_pc': 50}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     6
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     7
GTGGCGTGTAGAATGT    19
CGATCGGGTAGAATGT    16
GAGGGTAGTAGATCCT    22
TTACGTTAGGTAAGAG    16
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.2, 'num_pc': 50, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     3
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT     4
CGATCGGGTAGAATGT    12
GAGGGTAGTAGATCCT    12
TTACGTTAGGTAAGAG    12
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.985082
CD14+ monocyte                 0.942035
CD16+ monocyte                 0.941518
CD4+ T cell                    0.993481
Cytotoxic T cell               0.978567
Dendritic cell                 0.990114
Megakaryocyte                  0.835710
Natural killer cell            0.984987
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.995746
dtype: float64, silhouette=0.13976794449289365, num_clusters=14, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.2, 'num_pc': 20}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     3
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT     4
CGATCGGGTAGAATGT    12
GAGGGTAGTAGATCCT    12
TTACGTTAGGTAAGAG    12
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.2, 'num_pc': 20, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT    12
CGATCGGGTAGAATGT    21
GAGGGTAGTAGATCCT     7
TTACGTTAGGTAAGAG     6
Name: cluster, Length: 7610, dtype: object, auc=Series([], dtype: float64), silhouette=-1.0, num_clusters=24, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.2, 'num_pc': 100}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT    12
CGATCGGGTAGAATGT    21
GAGGGTAGTAGATCCT     7
TTACGTTAGGTAAGAG     6
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.2, 'num_pc': 100, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     3
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     4
GTGGCGTGTAGAATGT     9
CGATCGGGTAGAATGT    18
GAGGGTAGTAGATCCT    12
TTACGTTAGGTAAGAG    18
Name: cluster, Length: 7610, dtype: object, auc=Series([], dtype: float64), silhouette=-1.0, num_clusters=27, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.5, 'num_pc': 50}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     3
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     4
GTGGCGTGTAGAATGT     9
CGATCGGGTAGAATGT    18
GAGGGTAGTAGATCCT    12
TTACGTTAGGTAAGAG    18
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.5, 'num_pc': 50, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     9
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     7
GTGGCGTGTAGAATGT     8
CGATCGGGTAGAATGT    13
GAGGGTAGTAGATCCT    13
TTACGTTAGGTAAGAG    13
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.981788
CD14+ monocyte                 0.927806
CD16+ monocyte                 0.942640
CD4+ T cell                    0.993892
Cytotoxic T cell               0.980371
Dendritic cell                 0.864908
Megakaryocyte                  0.848546
Natural killer cell            0.986706
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.995746
dtype: float64, silhouette=0.1191392114984926, num_clusters=17, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.2, 'num_pc': 30}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     9
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     7
GTGGCGTGTAGAATGT     8
CGATCGGGTAGAATGT    13
GAGGGTAGTAGATCCT    13
TTACGTTAGGTAAGAG    13
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.2, 'num_pc': 30, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     6
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     7
GTGGCGTGTAGAATGT    13
CGATCGGGTAGAATGT    23
GAGGGTAGTAGATCCT    29
TTACGTTAGGTAAGAG     8
Name: cluster, Length: 7610, dtype: object, auc=Series([], dtype: float64), silhouette=-1.0, num_clusters=30, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.5, 'num_pc': 100}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     6
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     7
GTGGCGTGTAGAATGT    13
CGATCGGGTAGAATGT    23
GAGGGTAGTAGATCCT    29
TTACGTTAGGTAAGAG     8
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.5, 'num_pc': 100, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     3
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     6
GTGGCGTGTAGAATGT     7
CGATCGGGTAGAATGT    15
GAGGGTAGTAGATCCT    15
TTACGTTAGGTAAGAG    15
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.985082
CD14+ monocyte                 0.978702
CD16+ monocyte                 0.947350
CD4+ T cell                    0.994240
Cytotoxic T cell               0.979171
Dendritic cell                 0.988491
Megakaryocyte                  0.995443
Natural killer cell            0.984987
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.995746
dtype: float64, silhouette=0.13860848887624494, num_clusters=17, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.5, 'num_pc': 20}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     3
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     6
GTGGCGTGTAGAATGT     7
CGATCGGGTAGAATGT    15
GAGGGTAGTAGATCCT    15
TTACGTTAGGTAAGAG    15
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.5, 'num_pc': 20, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     5
                    ..
AAGCGTTAGACTTCCA     6
GTGGCGTGTAGAATGT    16
CGATCGGGTAGAATGT    14
GAGGGTAGTAGATCCT    14
TTACGTTAGGTAAGAG    14
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.981788
CD14+ monocyte                 0.948376
CD16+ monocyte                 0.951414
CD4+ T cell                    0.994351
Cytotoxic T cell               0.980147
Dendritic cell                 0.992749
Megakaryocyte                  0.842102
Natural killer cell            0.986706
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.995746
dtype: float64, silhouette=0.1331531426424982, num_clusters=20, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.5, 'num_pc': 30}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     5
                    ..
AAGCGTTAGACTTCCA     6
GTGGCGTGTAGAATGT    16
CGATCGGGTAGAATGT    14
GAGGGTAGTAGATCCT    14
TTACGTTAGGTAAGAG    14
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': True, 'resolution': 1.5, 'num_pc': 30, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT    0
TAATTCCGTCCATACA    2
ACAGGGATCTCTTAAC    0
CATTCCGAGTGAGTGC    3
GTTGAACCACTGCGAC    2
                   ..
AAGCGTTAGACTTCCA    7
GTGGCGTGTAGAATGT    7
CGATCGGGTAGAATGT    9
GAGGGTAGTAGATCCT    9
TTACGTTAGGTAAGAG    9
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.985704
CD14+ monocyte                 0.917411
CD16+ monocyte                 0.945808
CD4+ T cell                    0.994239
Cytotoxic T cell               0.973313
Dendritic cell                 0.812156
Megakaryocyte                  0.873424
Natural killer cell            0.983554
Plasmacytoid dendritic cell    0.995746
dtype: float64, silhouette=0.16037805083621792, num_clusters=11, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 0.8, 'num_pc': 20}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT    0
TAATTCCGTCCATACA    2
ACAGGGATCTCTTAAC    0
CATTCCGAGTGAGTGC    3
GTTGAACCACTGCGAC    2
                   ..
AAGCGTTAGACTTCCA    7
GTGGCGTGTAGAATGT    7
CGATCGGGTAGAATGT    9
GAGGGTAGTAGATCCT    9
TTACGTTAGGTAAGAG    9
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 0.8, 'num_pc': 20, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT    0
TAATTCCGTCCATACA    1
ACAGGGATCTCTTAAC    0
CATTCCGAGTGAGTGC    2
GTTGAACCACTGCGAC    1
                   ..
AAGCGTTAGACTTCCA    5
GTGGCGTGTAGAATGT    4
CGATCGGGTAGAATGT    8
GAGGGTAGTAGATCCT    8
TTACGTTAGGTAAGAG    8
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.981788
CD14+ monocyte                 0.943418
CD16+ monocyte                 0.944801
CD4+ T cell                    0.994376
Cytotoxic T cell               0.973971
Dendritic cell                 0.888344
Megakaryocyte                  0.882780
Natural killer cell            0.983199
Plasmacytoid dendritic cell    0.995746
dtype: float64, silhouette=0.15895666455341478, num_clusters=13, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 0.8, 'num_pc': 30}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT    0
TAATTCCGTCCATACA    1
ACAGGGATCTCTTAAC    0
CATTCCGAGTGAGTGC    2
GTTGAACCACTGCGAC    1
                   ..
AAGCGTTAGACTTCCA    5
GTGGCGTGTAGAATGT    4
CGATCGGGTAGAATGT    8
GAGGGTAGTAGATCCT    8
TTACGTTAGGTAAGAG    8
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 0.8, 'num_pc': 30, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     3
GTGGCGTGTAGAATGT     4
CGATCGGGTAGAATGT    11
GAGGGTAGTAGATCCT    13
TTACGTTAGGTAAGAG    11
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.966283
CD14+ monocyte                 0.947497
CD16+ monocyte                 0.951701
CD4+ T cell                    0.995322
Cytotoxic T cell               0.977338
Dendritic cell                 0.900756
Megakaryocyte                  0.902138
Natural killer cell            0.986726
Plasmacytoid dendritic cell    0.995746
dtype: float64, silhouette=0.14636571335400025, num_clusters=14, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 0.8, 'num_pc': 50}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     3
GTGGCGTGTAGAATGT     4
CGATCGGGTAGAATGT    11
GAGGGTAGTAGATCCT    13
TTACGTTAGGTAAGAG    11
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 0.8, 'num_pc': 50, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT    0
TAATTCCGTCCATACA    1
ACAGGGATCTCTTAAC    0
CATTCCGAGTGAGTGC    5
GTTGAACCACTGCGAC    1
                   ..
AAGCGTTAGACTTCCA    8
GTGGCGTGTAGAATGT    2
CGATCGGGTAGAATGT    9
GAGGGTAGTAGATCCT    9
TTACGTTAGGTAAGAG    9
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.981788
CD14+ monocyte                 0.936844
CD16+ monocyte                 0.945630
CD4+ T cell                    0.994322
Cytotoxic T cell               0.980739
Dendritic cell                 0.879572
Megakaryocyte                  0.866042
Natural killer cell            0.987319
Plasmacytoid dendritic cell    0.995746
dtype: float64, silhouette=0.15907753530599647, num_clusters=13, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.0, 'num_pc': 30}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT    0
TAATTCCGTCCATACA    1
ACAGGGATCTCTTAAC    0
CATTCCGAGTGAGTGC    5
GTTGAACCACTGCGAC    1
                   ..
AAGCGTTAGACTTCCA    8
GTGGCGTGTAGAATGT    2
CGATCGGGTAGAATGT    9
GAGGGTAGTAGATCCT    9
TTACGTTAGGTAAGAG    9
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.0, 'num_pc': 30, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     8
GTGGCGTGTAGAATGT     8
CGATCGGGTAGAATGT    10
GAGGGTAGTAGATCCT    10
TTACGTTAGGTAAGAG    10
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.985704
CD14+ monocyte                 0.946099
CD16+ monocyte                 0.949567
CD4+ T cell                    0.993689
Cytotoxic T cell               0.979609
Dendritic cell                 0.973302
Megakaryocyte                  0.853712
Natural killer cell            0.988309
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.995746
dtype: float64, silhouette=0.16314180008265727, num_clusters=13, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.0, 'num_pc': 20}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     8
GTGGCGTGTAGAATGT     8
CGATCGGGTAGAATGT    10
GAGGGTAGTAGATCCT    10
TTACGTTAGGTAAGAG    10
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.0, 'num_pc': 20, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT    0
TAATTCCGTCCATACA    2
ACAGGGATCTCTTAAC    0
CATTCCGAGTGAGTGC    3
GTTGAACCACTGCGAC    2
                   ..
AAGCGTTAGACTTCCA    4
GTGGCGTGTAGAATGT    8
CGATCGGGTAGAATGT    1
GAGGGTAGTAGATCCT    8
TTACGTTAGGTAAGAG    8
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.982793
CD14+ monocyte                 0.947817
CD16+ monocyte                 0.958867
CD4+ T cell                    0.942347
Dendritic cell                 0.963398
Megakaryocyte                  0.835571
Natural killer cell            0.984135
Plasmacytoid dendritic cell    0.995890
dtype: float64, silhouette=0.1340354128240525, num_clusters=15, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 0.8, 'num_pc': 100}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT    0
TAATTCCGTCCATACA    2
ACAGGGATCTCTTAAC    0
CATTCCGAGTGAGTGC    3
GTTGAACCACTGCGAC    2
                   ..
AAGCGTTAGACTTCCA    4
GTGGCGTGTAGAATGT    8
CGATCGGGTAGAATGT    1
GAGGGTAGTAGATCCT    8
TTACGTTAGGTAAGAG    8
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 0.8, 'num_pc': 100, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     4
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT    13
CGATCGGGTAGAATGT    10
GAGGGTAGTAGATCCT    16
TTACGTTAGGTAAGAG    10
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.973844
CD14+ monocyte                 0.941828
CD16+ monocyte                 0.951997
CD4+ T cell                    0.995370
Cytotoxic T cell               0.978124
Dendritic cell                 0.882195
Megakaryocyte                  0.895049
Natural killer cell            0.987214
Plasmacytoid dendritic cell    0.995746
dtype: float64, silhouette=0.1377542520882114, num_clusters=17, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.0, 'num_pc': 50}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     4
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT    13
CGATCGGGTAGAATGT    10
GAGGGTAGTAGATCCT    16
TTACGTTAGGTAAGAG    10
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.0, 'num_pc': 50, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     3
GTGGCGTGTAGAATGT     6
CGATCGGGTAGAATGT    16
GAGGGTAGTAGATCCT     6
TTACGTTAGGTAAGAG     6
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.716765
CD14+ monocyte                 0.925419
CD16+ monocyte                 0.957890
CD4+ T cell                    0.988459
Cytotoxic T cell               0.977414
Dendritic cell                 0.932911
Megakaryocyte                  0.825654
Natural killer cell            0.984283
Plasmacytoid dendritic cell    0.992072
dtype: float64, silhouette=0.11891615129428076, num_clusters=18, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.0, 'num_pc': 100}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     3
GTGGCGTGTAGAATGT     6
CGATCGGGTAGAATGT    16
GAGGGTAGTAGATCCT     6
TTACGTTAGGTAAGAG     6
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.0, 'num_pc': 100, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     6
GTGGCGTGTAGAATGT     5
CGATCGGGTAGAATGT    11
GAGGGTAGTAGATCCT    11
TTACGTTAGGTAAGAG    11
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.981788
CD14+ monocyte                 0.943549
CD16+ monocyte                 0.951573
CD4+ T cell                    0.993693
Cytotoxic T cell               0.973509
Dendritic cell                 0.973302
Megakaryocyte                  0.843202
Natural killer cell            0.982722
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.995746
dtype: float64, silhouette=0.1384746021897004, num_clusters=14, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.2, 'num_pc': 20}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     6
GTGGCGTGTAGAATGT     5
CGATCGGGTAGAATGT    11
GAGGGTAGTAGATCCT    11
TTACGTTAGGTAAGAG    11
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.2, 'num_pc': 20, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     5
GTTGAACCACTGCGAC     2
                    ..
AAGCGTTAGACTTCCA     7
GTGGCGTGTAGAATGT     4
CGATCGGGTAGAATGT    13
GAGGGTAGTAGATCCT    13
TTACGTTAGGTAAGAG    13
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.981788
CD14+ monocyte                 0.928848
CD16+ monocyte                 0.946962
CD4+ T cell                    0.995010
Cytotoxic T cell               0.980710
Dendritic cell                 0.853109
Megakaryocyte                  0.852059
Natural killer cell            0.987319
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.995746
dtype: float64, silhouette=0.14087390606693417, num_clusters=16, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.2, 'num_pc': 30}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     5
GTTGAACCACTGCGAC     2
                    ..
AAGCGTTAGACTTCCA     7
GTGGCGTGTAGAATGT     4
CGATCGGGTAGAATGT    13
GAGGGTAGTAGATCCT    13
TTACGTTAGGTAAGAG    13
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.2, 'num_pc': 30, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     3
GTGGCGTGTAGAATGT     9
CGATCGGGTAGAATGT    19
GAGGGTAGTAGATCCT     5
TTACGTTAGGTAAGAG     5
Name: cluster, Length: 7610, dtype: object, auc=Series([], dtype: float64), silhouette=-1.0, num_clusters=22, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.2, 'num_pc': 100}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     3
GTGGCGTGTAGAATGT     9
CGATCGGGTAGAATGT    19
GAGGGTAGTAGATCCT     5
TTACGTTAGGTAAGAG     5
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.2, 'num_pc': 100, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     4
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT    21
CGATCGGGTAGAATGT    20
GAGGGTAGTAGATCCT    24
TTACGTTAGGTAAGAG    20
Name: cluster, Length: 7610, dtype: object, auc=Series([], dtype: float64), silhouette=-1.0, num_clusters=25, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.5, 'num_pc': 50}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     4
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT    21
CGATCGGGTAGAATGT    20
GAGGGTAGTAGATCCT    24
TTACGTTAGGTAAGAG    20
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.5, 'num_pc': 50, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     4
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT     8
CGATCGGGTAGAATGT    15
GAGGGTAGTAGATCCT    18
TTACGTTAGGTAAGAG    15
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.962663
CD14+ monocyte                 0.939439
CD16+ monocyte                 0.952654
CD4+ T cell                    0.995370
Cytotoxic T cell               0.978124
Dendritic cell                 0.875198
Megakaryocyte                  0.892819
Natural killer cell            0.987214
Plasmacytoid dendritic cell    0.995746
dtype: float64, silhouette=0.13834455929732073, num_clusters=19, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.2, 'num_pc': 50}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     4
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT     8
CGATCGGGTAGAATGT    15
GAGGGTAGTAGATCCT    18
TTACGTTAGGTAAGAG    15
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.2, 'num_pc': 50, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     4
GTGGCGTGTAGAATGT     3
CGATCGGGTAGAATGT    13
GAGGGTAGTAGATCCT    13
TTACGTTAGGTAAGAG    13
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.985704
CD14+ monocyte                 0.942049
CD16+ monocyte                 0.950111
CD4+ T cell                    0.993693
Cytotoxic T cell               0.979609
Dendritic cell                 0.970151
Megakaryocyte                  0.841157
Natural killer cell            0.986306
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.995806
dtype: float64, silhouette=0.13159885035992547, num_clusters=16, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.5, 'num_pc': 20}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     4
GTGGCGTGTAGAATGT     3
CGATCGGGTAGAATGT    13
GAGGGTAGTAGATCCT    13
TTACGTTAGGTAAGAG    13
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.5, 'num_pc': 20, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     3
GTTGAACCACTGCGAC     5
                    ..
AAGCGTTAGACTTCCA    13
GTGGCGTGTAGAATGT    12
CGATCGGGTAGAATGT    16
GAGGGTAGTAGATCCT    16
TTACGTTAGGTAAGAG    16
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.981788
CD14+ monocyte                 0.947688
CD16+ monocyte                 0.951141
CD4+ T cell                    0.995250
Cytotoxic T cell               0.980622
Dendritic cell                 0.991985
Megakaryocyte                  0.845740
Natural killer cell            0.987348
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.995746
dtype: float64, silhouette=0.1370507189908719, num_clusters=18, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.5, 'num_pc': 30}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     3
GTTGAACCACTGCGAC     5
                    ..
AAGCGTTAGACTTCCA    13
GTGGCGTGTAGAATGT    12
CGATCGGGTAGAATGT    16
GAGGGTAGTAGATCCT    16
TTACGTTAGGTAAGAG    16
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.5, 'num_pc': 30, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     4
GTGGCGTGTAGAATGT    15
CGATCGGGTAGAATGT    19
GAGGGTAGTAGATCCT    25
TTACGTTAGGTAAGAG     6
Name: cluster, Length: 7610, dtype: object, auc=Series([], dtype: float64), silhouette=-1.0, num_clusters=28, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.5, 'num_pc': 100}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts', 'highly_variable', 'means', 'dispersions', 'dispersions_norm'
    uns: 'log1p', 'hvg'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     4
GTGGCGTGTAGAATGT    15
CGATCGGGTAGAATGT    19
GAGGGTAGTAGATCCT    25
TTACGTTAGGTAAGAG     6
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': True, 'resolution': 1.5, 'num_pc': 100, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     3
                    ..
AAGCGTTAGACTTCCA     8
GTGGCGTGTAGAATGT     8
CGATCGGGTAGAATGT    12
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    12
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.977886
CD16+ monocyte                 0.978238
CD4+ T cell                    0.992929
Cytotoxic T cell               0.984827
Dendritic cell                 0.941581
Megakaryocyte                  0.966149
Natural killer cell            0.991358
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.996414
dtype: float64, silhouette=0.1675740866928674, num_clusters=15, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 0.8, 'num_pc': 20}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     3
                    ..
AAGCGTTAGACTTCCA     8
GTGGCGTGTAGAATGT     8
CGATCGGGTAGAATGT    12
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    12
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 0.8, 'num_pc': 20, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     3
                    ..
AAGCGTTAGACTTCCA     7
GTGGCGTGTAGAATGT     7
CGATCGGGTAGAATGT    11
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    11
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.983224
CD16+ monocyte                 0.972366
CD4+ T cell                    0.994670
Cytotoxic T cell               0.984682
Dendritic cell                 0.950084
Megakaryocyte                  0.992717
Natural killer cell            0.991737
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.996414
dtype: float64, silhouette=0.21601355685149293, num_clusters=13, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 0.8, 'num_pc': 30}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     3
                    ..
AAGCGTTAGACTTCCA     7
GTGGCGTGTAGAATGT     7
CGATCGGGTAGAATGT    11
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    11
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 0.8, 'num_pc': 30, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA    12
GTGGCGTGTAGAATGT    12
CGATCGGGTAGAATGT    10
GAGGGTAGTAGATCCT    13
TTACGTTAGGTAAGAG    10
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.986196
CD16+ monocyte                 0.976820
CD4+ T cell                    0.995351
Cytotoxic T cell               0.983757
Dendritic cell                 0.992736
Megakaryocyte                  0.992833
Natural killer cell            0.991277
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.996424
dtype: float64, silhouette=0.2194817652884632, num_clusters=14, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 0.8, 'num_pc': 50}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA    12
GTGGCGTGTAGAATGT    12
CGATCGGGTAGAATGT    10
GAGGGTAGTAGATCCT    13
TTACGTTAGGTAAGAG    10
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 0.8, 'num_pc': 50, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT    0
TAATTCCGTCCATACA    1
ACAGGGATCTCTTAAC    0
CATTCCGAGTGAGTGC    1
GTTGAACCACTGCGAC    2
                   ..
AAGCGTTAGACTTCCA    4
GTGGCGTGTAGAATGT    4
CGATCGGGTAGAATGT    8
GAGGGTAGTAGATCCT    0
TTACGTTAGGTAAGAG    8
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.987520
CD16+ monocyte                 0.939249
CD4+ T cell                    0.994524
Cytotoxic T cell               0.985546
Dendritic cell                 0.947140
Megakaryocyte                  0.994248
Natural killer cell            0.989624
Plasmacytoid dendritic cell    0.996845
dtype: float64, silhouette=0.27510533105987467, num_clusters=11, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 0.8, 'num_pc': 100}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT    0
TAATTCCGTCCATACA    1
ACAGGGATCTCTTAAC    0
CATTCCGAGTGAGTGC    1
GTTGAACCACTGCGAC    2
                   ..
AAGCGTTAGACTTCCA    4
GTGGCGTGTAGAATGT    4
CGATCGGGTAGAATGT    8
GAGGGTAGTAGATCCT    0
TTACGTTAGGTAAGAG    8
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 0.8, 'num_pc': 100, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     6
                    ..
AAGCGTTAGACTTCCA    14
GTGGCGTGTAGAATGT    14
CGATCGGGTAGAATGT    13
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    13
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.976031
CD16+ monocyte                 0.978328
CD4+ T cell                    0.992936
Cytotoxic T cell               0.984827
Dendritic cell                 0.968464
Megakaryocyte                  0.964535
Natural killer cell            0.991203
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.996414
dtype: float64, silhouette=0.16418858484455634, num_clusters=17, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.0, 'num_pc': 20}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     6
                    ..
AAGCGTTAGACTTCCA    14
GTGGCGTGTAGAATGT    14
CGATCGGGTAGAATGT    13
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    13
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.0, 'num_pc': 20, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     3
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     3
GTTGAACCACTGCGAC     5
                    ..
AAGCGTTAGACTTCCA     8
GTGGCGTGTAGAATGT     8
CGATCGGGTAGAATGT    13
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    13
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.981941
CD16+ monocyte                 0.972421
CD4+ T cell                    0.994111
Cytotoxic T cell               0.984766
Dendritic cell                 0.970887
Megakaryocyte                  0.991500
Natural killer cell            0.991789
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.996414
dtype: float64, silhouette=0.1914797444801499, num_clusters=15, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.0, 'num_pc': 30}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     3
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     3
GTTGAACCACTGCGAC     5
                    ..
AAGCGTTAGACTTCCA     8
GTGGCGTGTAGAATGT     8
CGATCGGGTAGAATGT    13
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    13
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.0, 'num_pc': 30, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA    13
GTGGCGTGTAGAATGT    13
CGATCGGGTAGAATGT    11
GAGGGTAGTAGATCCT    14
TTACGTTAGGTAAGAG    11
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.983191
CD16+ monocyte                 0.976820
CD4+ T cell                    0.994728
Cytotoxic T cell               0.983757
Dendritic cell                 0.982467
Megakaryocyte                  0.992797
Natural killer cell            0.991277
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.996424
dtype: float64, silhouette=0.2082184339503292, num_clusters=15, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.0, 'num_pc': 50}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA    13
GTGGCGTGTAGAATGT    13
CGATCGGGTAGAATGT    11
GAGGGTAGTAGATCCT    14
TTACGTTAGGTAAGAG    11
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.0, 'num_pc': 50, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA    10
GTGGCGTGTAGAATGT    10
CGATCGGGTAGAATGT     8
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG     8
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.984227
CD16+ monocyte                 0.973201
CD4+ T cell                    0.994150
Cytotoxic T cell               0.980453
Dendritic cell                 0.947181
Megakaryocyte                  0.994084
Natural killer cell            0.987157
Plasmacytoid dendritic cell    0.996602
dtype: float64, silhouette=0.2118594556697035, num_clusters=12, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.0, 'num_pc': 100}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA    10
GTGGCGTGTAGAATGT    10
CGATCGGGTAGAATGT     8
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG     8
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.0, 'num_pc': 100, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     5
                    ..
AAGCGTTAGACTTCCA    17
GTGGCGTGTAGAATGT    17
CGATCGGGTAGAATGT    15
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    15
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.977094
CD16+ monocyte                 0.980273
CD4+ T cell                    0.993481
Cytotoxic T cell               0.983247
Dendritic cell                 0.939792
Megakaryocyte                  0.968416
Natural killer cell            0.991358
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.996414
dtype: float64, silhouette=0.1351420685281, num_clusters=18, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.2, 'num_pc': 20}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     5
                    ..
AAGCGTTAGACTTCCA    17
GTGGCGTGTAGAATGT    17
CGATCGGGTAGAATGT    15
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    15
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.2, 'num_pc': 20, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     4
                    ..
AAGCGTTAGACTTCCA    20
GTGGCGTGTAGAATGT    20
CGATCGGGTAGAATGT    16
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    15
Name: cluster, Length: 7610, dtype: object, auc=Series([], dtype: float64), silhouette=-1.0, num_clusters=21, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.5, 'num_pc': 20}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     4
                    ..
AAGCGTTAGACTTCCA    20
GTGGCGTGTAGAATGT    20
CGATCGGGTAGAATGT    16
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    15
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.5, 'num_pc': 20, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     3
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     3
GTTGAACCACTGCGAC     4
                    ..
AAGCGTTAGACTTCCA     8
GTGGCGTGTAGAATGT     8
CGATCGGGTAGAATGT    15
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    15
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.986208
CD16+ monocyte                 0.978844
CD4+ T cell                    0.994111
Cytotoxic T cell               0.984766
Dendritic cell                 0.966428
Megakaryocyte                  0.991517
Natural killer cell            0.991789
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.996414
dtype: float64, silhouette=0.17295723094414073, num_clusters=17, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.2, 'num_pc': 30}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     3
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     3
GTTGAACCACTGCGAC     4
                    ..
AAGCGTTAGACTTCCA     8
GTGGCGTGTAGAATGT     8
CGATCGGGTAGAATGT    15
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    15
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.2, 'num_pc': 30, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     4
GTGGCGTGTAGAATGT     4
CGATCGGGTAGAATGT    13
GAGGGTAGTAGATCCT    15
TTACGTTAGGTAAGAG    13
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.984722
CD16+ monocyte                 0.976820
CD4+ T cell                    0.994642
Cytotoxic T cell               0.983816
Dendritic cell                 0.992574
Megakaryocyte                  0.992797
Natural killer cell            0.991277
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.996424
dtype: float64, silhouette=0.17937181473369262, num_clusters=16, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.2, 'num_pc': 50}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     4
GTGGCGTGTAGAATGT     4
CGATCGGGTAGAATGT    13
GAGGGTAGTAGATCCT    15
TTACGTTAGGTAAGAG    13
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.2, 'num_pc': 50, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT    0
TAATTCCGTCCATACA    1
ACAGGGATCTCTTAAC    0
CATTCCGAGTGAGTGC    1
GTTGAACCACTGCGAC    2
                   ..
AAGCGTTAGACTTCCA    6
GTGGCGTGTAGAATGT    6
CGATCGGGTAGAATGT    9
GAGGGTAGTAGATCCT    0
TTACGTTAGGTAAGAG    9
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.987442
CD16+ monocyte                 0.973201
CD4+ T cell                    0.994714
Cytotoxic T cell               0.985116
Dendritic cell                 0.977716
Megakaryocyte                  0.994353
Natural killer cell            0.989843
Plasmacytoid dendritic cell    0.996845
dtype: float64, silhouette=0.22348181144693985, num_clusters=12, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.2, 'num_pc': 100}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT    0
TAATTCCGTCCATACA    1
ACAGGGATCTCTTAAC    0
CATTCCGAGTGAGTGC    1
GTTGAACCACTGCGAC    2
                   ..
AAGCGTTAGACTTCCA    6
GTGGCGTGTAGAATGT    6
CGATCGGGTAGAATGT    9
GAGGGTAGTAGATCCT    0
TTACGTTAGGTAAGAG    9
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.2, 'num_pc': 100, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA    12
GTGGCGTGTAGAATGT    12
CGATCGGGTAGAATGT    17
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    17
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.984729
CD16+ monocyte                 0.978864
CD4+ T cell                    0.993557
Cytotoxic T cell               0.984355
Dendritic cell                 0.968701
Megakaryocyte                  0.992040
Natural killer cell            0.991789
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.996424
dtype: float64, silhouette=0.09211804358661639, num_clusters=20, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.5, 'num_pc': 30}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA    12
GTGGCGTGTAGAATGT    12
CGATCGGGTAGAATGT    17
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    17
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.5, 'num_pc': 30, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     2
                    ..
AAGCGTTAGACTTCCA    16
GTGGCGTGTAGAATGT    16
CGATCGGGTAGAATGT    14
GAGGGTAGTAGATCCT     1
TTACGTTAGGTAAGAG    14
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.981361
CD16+ monocyte                 0.975134
CD4+ T cell                    0.995130
Cytotoxic T cell               0.983285
Dendritic cell                 0.969100
Megakaryocyte                  0.992951
Natural killer cell            0.991492
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.996424
dtype: float64, silhouette=0.16936607961996406, num_clusters=17, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.5, 'num_pc': 50}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     2
                    ..
AAGCGTTAGACTTCCA    16
GTGGCGTGTAGAATGT    16
CGATCGGGTAGAATGT    14
GAGGGTAGTAGATCCT     1
TTACGTTAGGTAAGAG    14
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.5, 'num_pc': 50, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     2
                    ..
AAGCGTTAGACTTCCA     3
GTGGCGTGTAGAATGT     3
CGATCGGGTAGAATGT    11
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    11
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.988480
CD16+ monocyte                 0.977058
CD4+ T cell                    0.994714
Cytotoxic T cell               0.985116
Dendritic cell                 0.979397
Megakaryocyte                  0.994325
Natural killer cell            0.989843
Plasmacytoid dendritic cell    0.996845
dtype: float64, silhouette=0.1927674988763925, num_clusters=14, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.5, 'num_pc': 100}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     2
                    ..
AAGCGTTAGACTTCCA     3
GTGGCGTGTAGAATGT     3
CGATCGGGTAGAATGT    11
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    11
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 15, 'variable_gene': False, 'resolution': 1.5, 'num_pc': 100, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     4
                    ..
AAGCGTTAGACTTCCA     3
GTGGCGTGTAGAATGT     3
CGATCGGGTAGAATGT    10
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    10
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.985548
CD16+ monocyte                 0.978116
CD4+ T cell                    0.993781
Cytotoxic T cell               0.985856
Dendritic cell                 0.950864
Megakaryocyte                  0.996443
Natural killer cell            0.991358
Plasmacytoid dendritic cell    0.996579
dtype: float64, silhouette=0.20282401293836802, num_clusters=14, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 0.8, 'num_pc': 20}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     4
                    ..
AAGCGTTAGACTTCCA     3
GTGGCGTGTAGAATGT     3
CGATCGGGTAGAATGT    10
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    10
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 0.8, 'num_pc': 20, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT    0
TAATTCCGTCCATACA    1
ACAGGGATCTCTTAAC    0
CATTCCGAGTGAGTGC    1
GTTGAACCACTGCGAC    2
                   ..
AAGCGTTAGACTTCCA    4
GTGGCGTGTAGAATGT    4
CGATCGGGTAGAATGT    9
GAGGGTAGTAGATCCT    0
TTACGTTAGGTAAGAG    9
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.981552
CD16+ monocyte                 0.971923
CD4+ T cell                    0.994199
Cytotoxic T cell               0.986701
Dendritic cell                 0.937148
Megakaryocyte                  0.992945
Natural killer cell            0.991562
Plasmacytoid dendritic cell    0.996579
dtype: float64, silhouette=0.22358997710885248, num_clusters=12, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 0.8, 'num_pc': 30}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT    0
TAATTCCGTCCATACA    1
ACAGGGATCTCTTAAC    0
CATTCCGAGTGAGTGC    1
GTTGAACCACTGCGAC    2
                   ..
AAGCGTTAGACTTCCA    4
GTGGCGTGTAGAATGT    4
CGATCGGGTAGAATGT    9
GAGGGTAGTAGATCCT    0
TTACGTTAGGTAAGAG    9
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 0.8, 'num_pc': 30, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA    11
GTGGCGTGTAGAATGT    11
CGATCGGGTAGAATGT     8
GAGGGTAGTAGATCCT    10
TTACGTTAGGTAAGAG     8
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.984547
CD16+ monocyte                 0.972827
CD4+ T cell                    0.995409
Cytotoxic T cell               0.984246
Dendritic cell                 0.945254
Megakaryocyte                  0.992941
Natural killer cell            0.991274
Plasmacytoid dendritic cell    0.996579
dtype: float64, silhouette=0.21418537952322836, num_clusters=12, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 0.8, 'num_pc': 50}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA    11
GTGGCGTGTAGAATGT    11
CGATCGGGTAGAATGT     8
GAGGGTAGTAGATCCT    10
TTACGTTAGGTAAGAG     8
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 0.8, 'num_pc': 50, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     3
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT     5
CGATCGGGTAGAATGT    10
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    10
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.990885
CD16+ monocyte                 0.948286
CD4+ T cell                    0.994190
Cytotoxic T cell               0.985559
Dendritic cell                 0.980005
Megakaryocyte                  0.997872
Natural killer cell            0.989187
Plasmacytoid dendritic cell    0.996992
dtype: float64, silhouette=0.24867477748371025, num_clusters=12, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 0.8, 'num_pc': 100}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     3
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT     5
CGATCGGGTAGAATGT    10
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    10
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 0.8, 'num_pc': 100, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     3
                    ..
AAGCGTTAGACTTCCA    14
GTGGCGTGTAGAATGT    14
CGATCGGGTAGAATGT    11
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    11
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.986773
CD16+ monocyte                 0.978116
CD4+ T cell                    0.993754
Cytotoxic T cell               0.985271
Dendritic cell                 0.962344
Megakaryocyte                  0.995979
Natural killer cell            0.991358
Plasmacytoid dendritic cell    0.996579
dtype: float64, silhouette=0.17580249170439136, num_clusters=15, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.0, 'num_pc': 20}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     3
                    ..
AAGCGTTAGACTTCCA    14
GTGGCGTGTAGAATGT    14
CGATCGGGTAGAATGT    11
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    11
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.0, 'num_pc': 20, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     2
                    ..
AAGCGTTAGACTTCCA    10
GTGGCGTGTAGAATGT    10
CGATCGGGTAGAATGT    12
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    12
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.985184
CD16+ monocyte                 0.971923
CD4+ T cell                    0.994670
Cytotoxic T cell               0.984797
Dendritic cell                 0.973390
Megakaryocyte                  0.993002
Natural killer cell            0.991562
Plasmacytoid dendritic cell    0.996579
dtype: float64, silhouette=0.20274315357472816, num_clusters=14, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.0, 'num_pc': 30}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     2
                    ..
AAGCGTTAGACTTCCA    10
GTGGCGTGTAGAATGT    10
CGATCGGGTAGAATGT    12
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    12
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.0, 'num_pc': 30, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA    13
GTGGCGTGTAGAATGT    13
CGATCGGGTAGAATGT    10
GAGGGTAGTAGATCCT    12
TTACGTTAGGTAAGAG    10
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.986024
CD16+ monocyte                 0.973171
CD4+ T cell                    0.995686
Cytotoxic T cell               0.983347
Dendritic cell                 0.975964
Megakaryocyte                  0.992451
Natural killer cell            0.991274
Plasmacytoid dendritic cell    0.996579
dtype: float64, silhouette=0.19969176033034045, num_clusters=14, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.0, 'num_pc': 50}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA    13
GTGGCGTGTAGAATGT    13
CGATCGGGTAGAATGT    10
GAGGGTAGTAGATCCT    12
TTACGTTAGGTAAGAG    10
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.0, 'num_pc': 50, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT    0
TAATTCCGTCCATACA    1
ACAGGGATCTCTTAAC    0
CATTCCGAGTGAGTGC    1
GTTGAACCACTGCGAC    2
                   ..
AAGCGTTAGACTTCCA    5
GTGGCGTGTAGAATGT    5
CGATCGGGTAGAATGT    9
GAGGGTAGTAGATCCT    0
TTACGTTAGGTAAGAG    9
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.989596
CD16+ monocyte                 0.974174
CD4+ T cell                    0.994990
Cytotoxic T cell               0.985712
Dendritic cell                 0.980341
Megakaryocyte                  0.993936
Natural killer cell            0.989187
Plasmacytoid dendritic cell    0.996992
dtype: float64, silhouette=0.24757436317778586, num_clusters=12, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.0, 'num_pc': 100}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT    0
TAATTCCGTCCATACA    1
ACAGGGATCTCTTAAC    0
CATTCCGAGTGAGTGC    1
GTTGAACCACTGCGAC    2
                   ..
AAGCGTTAGACTTCCA    5
GTGGCGTGTAGAATGT    5
CGATCGGGTAGAATGT    9
GAGGGTAGTAGATCCT    0
TTACGTTAGGTAAGAG    9
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.0, 'num_pc': 100, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     3
                    ..
AAGCGTTAGACTTCCA    10
GTGGCGTGTAGAATGT    10
CGATCGGGTAGAATGT    12
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    12
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.981267
CD16+ monocyte                 0.978277
CD4+ T cell                    0.993760
Cytotoxic T cell               0.984338
Dendritic cell                 0.948579
Megakaryocyte                  0.972320
Natural killer cell            0.991358
Plasmacytoid dendritic cell    0.996579
dtype: float64, silhouette=0.15667557292247822, num_clusters=16, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.2, 'num_pc': 20}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     3
                    ..
AAGCGTTAGACTTCCA    10
GTGGCGTGTAGAATGT    10
CGATCGGGTAGAATGT    12
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    12
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.2, 'num_pc': 20, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     4
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT     5
CGATCGGGTAGAATGT    12
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    12
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.984546
CD16+ monocyte                 0.972282
CD4+ T cell                    0.994553
Cytotoxic T cell               0.984397
Dendritic cell                 0.973957
Megakaryocyte                  0.991410
Natural killer cell            0.991562
Plasmacytoid dendritic cell    0.996579
dtype: float64, silhouette=0.20012647055745145, num_clusters=14, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.2, 'num_pc': 30}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     4
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT     5
CGATCGGGTAGAATGT    12
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    12
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.2, 'num_pc': 30, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     4
GTGGCGTGTAGAATGT     4
CGATCGGGTAGAATGT    11
GAGGGTAGTAGATCCT    13
TTACGTTAGGTAAGAG    11
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.984030
CD16+ monocyte                 0.972682
CD4+ T cell                    0.995686
Cytotoxic T cell               0.983347
Dendritic cell                 0.964561
Megakaryocyte                  0.992451
Natural killer cell            0.991274
Plasmacytoid dendritic cell    0.996579
dtype: float64, silhouette=0.19736775124317799, num_clusters=14, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.2, 'num_pc': 50}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     4
GTGGCGTGTAGAATGT     4
CGATCGGGTAGAATGT    11
GAGGGTAGTAGATCCT    13
TTACGTTAGGTAAGAG    11
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.2, 'num_pc': 50, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT    0
TAATTCCGTCCATACA    1
ACAGGGATCTCTTAAC    0
CATTCCGAGTGAGTGC    1
GTTGAACCACTGCGAC    2
                   ..
AAGCGTTAGACTTCCA    6
GTGGCGTGTAGAATGT    6
CGATCGGGTAGAATGT    9
GAGGGTAGTAGATCCT    0
TTACGTTAGGTAAGAG    9
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.989119
CD16+ monocyte                 0.945902
CD4+ T cell                    0.994942
Cytotoxic T cell               0.985278
Dendritic cell                 0.980289
Megakaryocyte                  0.993019
Natural killer cell            0.989187
Plasmacytoid dendritic cell    0.996067
dtype: float64, silhouette=0.2417890270393762, num_clusters=12, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.2, 'num_pc': 100}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT    0
TAATTCCGTCCATACA    1
ACAGGGATCTCTTAAC    0
CATTCCGAGTGAGTGC    1
GTTGAACCACTGCGAC    2
                   ..
AAGCGTTAGACTTCCA    6
GTGGCGTGTAGAATGT    6
CGATCGGGTAGAATGT    9
GAGGGTAGTAGATCCT    0
TTACGTTAGGTAAGAG    9
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.2, 'num_pc': 100, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     9
GTGGCGTGTAGAATGT     9
CGATCGGGTAGAATGT    15
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    15
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.981130
CD16+ monocyte                 0.978266
CD4+ T cell                    0.993754
Cytotoxic T cell               0.985271
Dendritic cell                 0.955643
Megakaryocyte                  0.973549
Natural killer cell            0.991358
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.996579
dtype: float64, silhouette=0.09014966655011493, num_clusters=19, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.5, 'num_pc': 20}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     9
GTGGCGTGTAGAATGT     9
CGATCGGGTAGAATGT    15
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    15
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.5, 'num_pc': 20, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     2
                    ..
AAGCGTTAGACTTCCA    15
GTGGCGTGTAGAATGT    15
CGATCGGGTAGAATGT    13
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    13
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.983465
CD16+ monocyte                 0.972477
CD4+ T cell                    0.994242
Cytotoxic T cell               0.984401
Dendritic cell                 0.969556
Megakaryocyte                  0.992532
Natural killer cell            0.991737
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.996579
dtype: float64, silhouette=0.1768735285697415, num_clusters=16, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.5, 'num_pc': 30}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     2
                    ..
AAGCGTTAGACTTCCA    15
GTGGCGTGTAGAATGT    15
CGATCGGGTAGAATGT    13
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    13
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.5, 'num_pc': 30, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT     5
CGATCGGGTAGAATGT    12
GAGGGTAGTAGATCCT    14
TTACGTTAGGTAAGAG    12
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.979104
CD16+ monocyte                 0.972682
CD4+ T cell                    0.996167
Cytotoxic T cell               0.983369
Dendritic cell                 0.943705
Megakaryocyte                  0.990328
Natural killer cell            0.991274
Plasma cell                    0.750362
Plasmacytoid dendritic cell    0.996579
dtype: float64, silhouette=0.18216238986360156, num_clusters=15, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.5, 'num_pc': 50}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     1
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     1
GTTGAACCACTGCGAC     1
                    ..
AAGCGTTAGACTTCCA     5
GTGGCGTGTAGAATGT     5
CGATCGGGTAGAATGT    12
GAGGGTAGTAGATCCT    14
TTACGTTAGGTAAGAG    12
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.5, 'num_pc': 50, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None), ModelCandidate(clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     3
                    ..
AAGCGTTAGACTTCCA    13
GTGGCGTGTAGAATGT    13
CGATCGGGTAGAATGT    10
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    10
Name: cluster, Length: 7610, dtype: object, auc=B cell                         0.986297
CD14+ monocyte                 0.989432
CD16+ monocyte                 0.975287
CD4+ T cell                    0.994870
Cytotoxic T cell               0.985138
Dendritic cell                 0.980341
Megakaryocyte                  0.993665
Natural killer cell            0.989624
Plasmacytoid dendritic cell    0.996992
dtype: float64, silhouette=0.20005022844687448, num_clusters=14, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.5, 'num_pc': 100}, model=ClusterResult(adata=AnnData object with n_obs × n_vars = 7610 × 989
    obs: 'n_genes', 'n_genes_by_counts', 'total_counts', 'total_counts_mito', 'pct_counts_mito', 'cluster'
    var: 'n_cells', 'mito', 'n_cells_by_counts', 'mean_counts', 'pct_dropout_by_counts', 'total_counts'
    uns: 'log1p'
    obsm: 'X_pca', 'X_tsne', clusters=CAATTTCAGACCCGCT     0
TAATTCCGTCCATACA     2
ACAGGGATCTCTTAAC     0
CATTCCGAGTGAGTGC     2
GTTGAACCACTGCGAC     3
                    ..
AAGCGTTAGACTTCCA    13
GTGGCGTGTAGAATGT    13
CGATCGGGTAGAATGT    10
GAGGGTAGTAGATCCT     0
TTACGTTAGGTAAGAG    10
Name: cluster, Length: 7610, dtype: object, params={'number_neighbor': 30, 'variable_gene': False, 'resolution': 1.5, 'num_pc': 100, 'normalize': True, 'min_cells': 3, 'min_genes': 1, 'species': 'human'}), adata=None)], auc_table=    number_neighbor  variable_gene  resolution  num_pc   avg_auc  auc_signal
0                15           True         1.0     100  0.000000    0.000000
1                15           True         0.8      20  2.218547    4.218547
2                15           True         0.8      30  2.300599    4.300599
3                15           True         1.0      20  2.406388    4.406388
4                15           True         1.0      30  2.299287    4.299287
..              ...            ...         ...     ...       ...         ...
59               30          False         1.2     100  2.560101    4.360101
60               30          False         1.5      20  2.592207    4.592207
61               30          False         1.5      30  2.621648    4.621648
62               30          False         1.5      50  2.589867    4.589867
63               30          False         1.5     100  2.591645    4.391645

[64 rows x 6 columns], silhouette_table=    number_neighbor  variable_gene  resolution  num_pc  silhouette
0                15           True         1.0     100   -1.000000
1                15           True         0.8      20    0.153680
2                15           True         0.8      30    0.138996
3                15           True         1.0      20    0.138239
4                15           True         1.0      30    0.140468
..              ...            ...         ...     ...         ...
59               30          False         1.2     100    0.241789
60               30          False         1.5      20    0.090150
61               30          False         1.5      30    0.176874
62               30          False         1.5      50    0.182162
63               30          False         1.5     100    0.200050

[64 rows x 5 columns], cluster_table=    number_neighbor  variable_gene  resolution  num_pc  num_clusters
0                15           True         1.0     100            22
1                15           True         0.8      20            12
2                15           True         0.8      30            14
3                15           True         1.0      20            14
4                15           True         1.0      30            16
..              ...            ...         ...     ...           ...
59               30          False         1.2     100            12
60               30          False         1.5      20            19
61               30          False         1.5      30            16
62               30          False         1.5      50            15
63               30          False         1.5     100            14

[64 rows x 5 columns])