# Indice de proximité aux services — Île-de-France

<span style="background-color:#009cad;"> >**Si vous lisez ceci** je postule à une formation dans votre établissement. Merci de l'intérêt que vous portez à ma candidature. Toutes les informations du projet sont disponibles ci-dessous. Les cartes sont disponibles dans la section qui suit. </span>

> **Projet d'entraînement** — Analyse de l'accessibilité aux équipements et services publics dans les 1 266 communes d'Île-de-France, à partir de données open source.

---

## 🗺️ Cartes interactives

| Carte | Description | Lien |
|---|---|---|
| **Indice IPS** | Score composite d'accessibilité par commune, 11 dimensions. | [Ouvrir](https://b00tb00t.github.io/idf-proximite-services/outputs/idf_ips_map.html) |
| **Équipements** | Localisation des 89 208 équipements, chargement à la demande. | [Ouvrir](https://b00tb00t.github.io/idf-proximite-services/outputs/idf_facilities_map.html) |

### Comment utiliser la carte IPS
- **Sélectionnez une catégorie** via le menu déroulant en haut à gauche pour afficher le score d'une dimension spécifique (santé, transport, éducation...)
- **Survolez** une commune pour voir son nom, score et rang
- **Cliquez** sur une commune pour afficher la fiche détaillée : scores par dimension, revenu médian, taux de pauvreté, structure démographique

### Comment utiliser la carte équipements
- **Cochez une catégorie** dans le panneau à droite pour charger les équipements correspondants
- Les points se **regroupent en clusters** selon le niveau de zoom
- Zoomez au **niveau 15** pour voir les équipements individuels

---

## 📚 Méthodologie et analyse

Pour mieux comprendre ce projet et répondre à vos possibles questions, deux pages supplémentaires sont disponibles : 

| Page | Description | Lien |
|---|---|---|
| **Méthodologie** | Stack technique, phases de développement. | [Ouvrir](https://b00tb00t.github.io/idf-proximite-services/METHODOLOGIE.html) |
| **Analyse** | Définition de l'IPS, limites et biais connus, observations simples. | [Ouvrir](https://b00tb00t.github.io/idf-proximite-services/ANALYSE.html) |

---

## 📊 L'Indice de proximité aux services (IPS)

L'IPS mesure, pour chaque commune d'Île-de-France, le temps de trajet moyen de ses habitants vers 60 types d'équipements et services, regroupés en 11 dimensions :

| Dimension | Poids | Équipements inclus |
|---|---|---|
| Soins essentiels | 5 | Médecin généraliste, pharmacie, urgences |
| Alimentaire | 5 | Supermarchés, épiceries, boulangeries |
| Éducation primaire | 4 | Maternelle, primaire, élémentaire |
| Éducation secondaire | 4 | Collège, lycée général, lycée pro |
| Transports | 4 | Gares nationales, régionales, locales |
| Services sociaux | 3 | Crèches, centres sociaux, EHPAD, accueil loisirs |
| Sports | 3 | Piscines, terrains, gymnases, salles |
| Culture | 3 | Cinémas, bibliothèques, conservatoires, spectacles |
| Éducation supérieure | 2 | Universités publiques et privées |
| Soins complémentaires | 2 | Dentiste, infirmier, laboratoire, maternité, PMI |
| Sécurité | 1 | Police, gendarmerie |

**Score IPS :** rang percentile normalisé parmi les 1 266 communes. Un score de 1,0 indique la commune la mieux desservie d'IDF, 0,0 la moins bien desservie.

---

## 📁 Sources de données

Toutes les données sont librement accessibles et publiées par des organismes publics.

| Dataset | Source | Lien |
|---|---|---|
| Limites administratives (ADMIN-EXPRESS COG) | IGN | [geoservices.ign.fr](https://geoservices.ign.fr/adminexpress) |
| Base Permanente des Équipements 2024 (BPE) | INSEE | [insee.fr](https://www.insee.fr/fr/statistiques/8217537) |
| Grille d'accessibilité aux équipements 2023 | INSEE | [data.gouv.fr](https://www.data.gouv.fr/fr/datasets/donnees-sur-la-localisation-et-lacces-de-la-population-aux-equipements/) |
| Filosofi 2021 — revenus par commune | INSEE | [insee.fr](https://www.insee.fr/fr/statistiques/7756859) |
| Recensement de la population 2022 (RP) | INSEE | [insee.fr](https://www.insee.fr/fr/statistiques/8647014) |

> Les données brutes ne sont pas ajoutées à ce repo en raison de leur taille.

---

## 🛠️ Stack technique

| Outil | Rôle |
|---|---|
| **Python** (GeoPandas, DuckDB, Folium, Matplotlib) | ETL, calcul des scores, cartographie |
| **PostGIS** (Docker) | Base de données spatiale |
| **DBeaver** | Administration et manipulation de la DB |
| **QGIS** | Exploration et validation visuelle |
| **Jupyter Notebooks** | Pipeline python |
| **GitHub Pages** | Hébergement des cartes |

Voir [METHODOLOGIE.md](METHODOLOGIE.md) pour le détail complet du processus technique.

---

## 📋 Structure du dépôt

```
├── notebooks/
│   ├── config.py                      # Configuration centralisée
│   ├── 01_data_inspection.ipynb       # Inspection des données brutes
│   ├── 02_data_loading.ipynb          # ETL et chargement PostGIS
│   ├── 03_accessibility_scores.ipynb  # Calcul des scores IPS
│   ├── 04_interactive_map.ipynb       # Création des cartes Folium
│   └── 05_analysis.ipynb              # Analyse et visualisations
├── outputs/
│   ├── idf_ips_map.html               # Carte IPS interactive
│   ├── idf_facilities_map.html        # Carte équipements interactive
│   ├── facilities/                    # GeoJSON par catégorie (chargement à la demande)
│   └── *.png                          # Graphiques d'analyse
├── README.md
├── METHODOLOGIE.md
└── ANALYSE.md
```

---

## ⚠️ Avertissements

Ce projet est un **exercice d'entraînement** en vue de présenter une production complète à différents instituts d'enseignements supérieurs. Les résultats ne constituent pas une analyse socio-économique publiable et utilisable. Voir [ANALYSE.md](ANALYSE.md) pour les limites et biais connus.

Des indices similaires existent déjà dans des analyses officielles (INSEE, services d'aménagement...). Ce projet en propose une version très simplifiée.

---

## 🤖 Création en collaboration avec une IA

N'étant pas un spécialiste en pipeline ETL et en formattage complexe de cartes pour des fichiers HTML, ce projet a été réalisé pour une partie de ces tâches avec une IA (Claude). Certaines validations ou optimisation côté PostGIS ont aussi été revues par l'IA. 

Les choix statistiques, de méthodologie, pondération , sélection et exploration des données et des équipements utilisés dans les cartes etc sont des choix seulement fait par l'auteur.  
