# Méthodologie technique — Indice de proximité aux services IDF

## Vue d'ensemble

Ce document décrit le processus technique complet du projet, de l'acquisition des données brutes à la publication des cartes interactives.

---

## Stack technique et choix d'outils

### PostGIS (Docker)
**Rôle :** Base de données spatiale centrale — stockage, indexation et requêtage de toutes les données géographiques.

**Déploiement :** Instance locale via Docker (`postgis/postgis:16-3.4`).

### Python — GeoPandas, DuckDB, Folium, Matplotlib
**Rôle :** ETL, calcul des scores, cartographie interactive, visualisations d'analyse.

- **GeoPandas** : lecture des fichiers géographiques (GeoPackage, Shapefile), manipulation de géométries, chargement vers PostGIS.
- **DuckDB** : prétraitement des fichiers Parquet volumineux (grille d'accessibilité INSEE, d'environ 20 millions de lignes) + requêtes SQL directement sur les fichiers Parquet.
- **Folium** : génération des cartes interactives HTML/Leaflet
- **Matplotlib** : graphiques d'analyse (scatter plots, heatmaps, histogrammes)
- **SQLAlchemy + psycopg2** : connexion Python ↔ PostGIS

### QGIS
**Rôle :** Validation visuelle des données via la connexion à la DB PostGis  — vérification des projections, de la cohérence des géometries et d'échantillon de données.

### Jupyter Notebooks
**Rôle :** Environnement de développement. Chaque notebook correspond à une phase du projet et documente les choix effectués.

---

## Phase 1 — Inspection des données

Identification des colonnes utiles et du format de chaque fichier pour s'assurer d'un ETL sain : 

- Format long vs. format large (Filosofi publié en format SDMX long, nécessitant un pivot)
- Quadrillage IRIS vs. commune
- Codes TYPEQU de la BPE

---

## Phase 2 — Schéma de base de données

Cinq tables principales dans le schéma `idf` créé : 


- idf.communes          -- polygones des 1 266 communes IDF (EPSG:2154)
- idf.facilities        -- 89 208 points d'équipements (EPSG:2154)
- idf.socioeco          -- indicateurs socio-économiques par commune
- idf.accessibility_grid -- temps de trajet pondérés par commune × type d'équipement
- idf.commune_index     -- scores IPS finaux par commune

Index GiST sur toutes les colonnes géométrie, index B-tree sur les codes commune (`insee_com`) et types d'équipement (`typequ`) pour permettre des les appliquer en clause pour limiter la carte à l'IDF et les équipements choisis. 

---

## Phase 3 — ETL

### Communes (IGN ADMIN-EXPRESS)
Chargement via **GeoPandas** avec `set_crs(EPSG:2154)`  puis reprojection en WGS84 pour Folium. La projection Lambert-93 est conservée en base pour tous les calculs métriques.

### Équipements BPE
Filtrage aux 8 départements IDF et aux 60 types d'équipements retenus. Construction de géométries Point à partir des coordonnées Lambert-93 `LAMBERT_X`/`LAMBERT_Y`. Ajout d'une colonne `indicator` mappant chaque code TYPEQU vers un nom lisible via `FACILITY_TYPES` dans `config.py`.

### Filosofi
Pivot du format long vers le format large (une ligne par commune, une colonne par indicateur). Agrégation pondérée par population pour Paris (niveau commune `75056`, pas par arrondissement).

### Recensement RP 2022
Agrégation des données IRIS (quadrillage en zone de 200m2) vers le niveau commune.

### Grille d'accessibilité INSEE
Traitement via **DuckDB** directement sur le fichier Parquet (~20 millions de lignes) sans chargement en mémoire. Agrégation par commune et type d'équipement avec **moyenne pondérée par population** :

```sql
SUM(duree * pop) / NULLIF(SUM(pop), 0) AS avg_travel_min
```

Cette moyenne reflète le temps de trajet vécu par les habitants réels, et non par les cellules géographiques vides (zones industrielles, forêts...) 

---

## Phase 4 — Calcul des scores IPS

### Étape 1 — Agrégation des codes TYPEQU en indicateurs

Plusieurs codes TYPEQU peuvent correspondre au même indicateur. Trois méthodes d'agrégation selon la nature du groupe :

| Méthode | Application | Justification |
|---|---|---|
| **MIN** | École primaire (C108+C109), lycée pro (C302+C303), sécurité, alimentaire... | Les codes sont fonctionnellement équivalents — le plus proche suffit |
| **Médiane simple** | Sports autres, culture | Types hétérogènes mais de valeur comparable |
| **Médiane pondérée** | Enseignement supérieur public, enseignement supérieur privé | Institutions avec des volumes d'élèves très différents — les universités (C501/C502, poids 4) doivent peser davantage que les établissements acceuillant moins d'élèves (C403, poids 1) |

### Étape 2 — Normalisation par rang percentile

Pour chaque indicateur, le temps de trajet de chaque commune est converti en score 0-1 par rang percentile :

```python
score = 1 - (rang - 1) / (N - 1)
```

**Avantage et désavantage du rang percentile** Le rang percentile évite qu'une valeurs extrême (temps de trajet jusqu'à X équipement > 70 min) compresse les communes dans les meilleurs valeurs si on utilisait une classification min-max. Le désavantage est que les commune ayant des temps de trajets exceptionnellement courts sur X équipement seront moins mis en valeur dans le classement (ex : rang 1 = trajet de 1 min, rang 2 = trajet de 10 min. Rang 1 sera moins mis en valeur )

### Étape 3 — Scores par dimension

Moyenne pondérée des scores indicateurs au sein de chaque dimension. La dimension *Alimentaire* applique des poids internes : supermarché ×4, épicerie locale ×2, boulangerie ×1.

### Étape 4 — Score IPS (Indice de Proximité aux Services) composite

Moyenne pondérée des scores de dimension :

```
IPS = (Somme des score par dimension × poids de chaque dimension) / Somme des poids de toutes les dimensions
```

Poids totaux : 36. Distribution résultante : moyenne 0.50, écart-type 0.216, min 0.030, max 0.951.

---

## Phase 5 — Cartographie

### Carte IPS (idf_eai_map.html — 43 Mo)
- Layer unique GeoJSON avec scores pré-calculés pour les 12 catégories.
- Changement de catégorie via JavaScript (`setStyle()`) sans rechargement de données
- Popups riches encodées en base64 pour éviter les conflits d'échappement HTML/JSON
- Légende "simplifiée" 

### Carte équipements (idf_facilities_map.html — 27 Mo)
- Architecture **lazy loading** : les 9 fichiers GeoJSON (~18 Mo au total) sont chargés à la demande au clic
- Le fichier HTML ne contient aucun point à l'ouverture — chargement uniquement pour les catégories activées
- Clustering Leaflet.markercluster (rayon 50px, clustering désactivé au zoom 15)
- MarkerCluster chargé dynamiquement via `loadScript()` après initialisation complète de Leaflet



---

## Rôle de l'IA dans le développement

Ce projet a été développé avec l'assistance de Claude. L'IA a été particulièrement utile pour :

- **L'ETL** : relecture et debug des scripts de chargement, gestion des encodages, résolution des incompatibilités de versions (SQLAlchemy 2.x, GeoPandas, Folium)
- **La cartographie Folium** : injection JavaScript, gestion du cycle de vie des scripts, lazy loading
- **Debug** :  Identification de problèmes (Projection, encoding, script ordering)

Les choix statistiques, de méthodologie, pondération , sélection et exploration des données et des équipements utilisés dans les cartes etc sont des choix seulement fait par l'auteur. 
