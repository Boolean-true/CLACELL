## Mitschrieb vom 28.10.2026

- Die Plasma Zellen gehören anscheinend zu B Zellen, nochmal prüfen und gegebenefalls als sub-zelltyp der b zellen aufnehmen
- breast cancer auf scrna seq level und nicht sparse evaluieren zum vergleich
- donor filtern, evtl kleinere datensätze
- vergleichsmodelle auf breast cancer datensatz loslassen
- 0.975 und höher als percentile testen, da es so aussieht, dass kleinere rejection zu einem besseren Ergebnis führt
- knn ist gefährlich weil er outlier mit neuen zellen nicht erkennt. es gäbe local outlier. pyod bietet ensemble, der verschiedene scores zusammenfasst. dann muss man scores kalibieren (d.h. bei fine grained auf known outliern, z.b. t zellen bei b zellen). bei fine grained dann infos von allen zelltypen nehmen um z.b. bei b zellen outlier zu detecten. also werden z.b. t zellen bei b zellen als outlier verwendet und es wird dann ein schwellenwert gewählt um outlier zu erkennen
- **erste prio**: mean squared error bzw construction loss autoencoder
- wenn keine verbesserung, dann schauen ob es bereits tools gibt
- evaluation auf allen 4 spatial datensätzen (aber auf dense scrna seq daten evaluieren). best of us vs vergleichsmodelle
- evtl testen einen auf dense trainierten classifier auf sparse loszulassen
- daten prüfen ob normalisiert

- template: bioinformatics journal template 9 seiten. graphical abstract usw rausschmeißen, kostet nur platz
- schonmal schreiben des drafts anfangen, dann kann anne stück für stück es durchlesen

**Weitere Ansätze zur Rejection Class**
- bei autoencoder anhand von reconstruction loss rejecten
- mixture model trainieren (ähnlich wie singler würde das dann vorgehen)


### Zusammenfassung Vorgehen

- Nochmal checken, ob ich die Datensätze normalisiert habe
- Beim breast cancer Datensatz die Donors nochmal anschauen, evtl mehr dazu nehmen und Donors aus kleineren Datensätzen entfernen (somit den Datensatz "bereinigen")
- Zuerst auf dense level (scrna seq) evaluieren, das beste modell + referenzmodelle dann auf sparse (spatial) evaluieren. Dabei zuerst schauen was passiert wenn man ein auf dense trainiertes modell auf sparse loslässt und dann gegebenenfalls noch das modell auf sparse trainieren und dann auf sparse evaluieren
- Das für alle 4 der ursprünglichen spatial datensätze machen (breast, tonsil, ovary, pancreas). Evtl eins nach dem anderen, dann habe ich früher bereits Ergebnisse für einzelne Datensätze
- Bei jedem Datensatz evaluieren welcher meiner Ansätze ma Besten ist. Evtl die ML Evaluation weglassen u Zeit zu sparen. Dann habe ich für jeden der 4 Datensätze ein bestes Modell. Dafür (evtl auch für ein zweitbestes Modell) dann eine Rejection Class implementieren (gegebenenfalls auf verschiedene Arten). Das wird dann mit den Referenzmodellen verglichen

- Parallel dazu schonmal den Paper Draft anfangen