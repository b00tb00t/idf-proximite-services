# Analyse — Premier regard sur l'accessibilité aux services en Île-de-France

> **Note préliminaire importante** — Ce document présente des observations issues d'un projet d'entraînement. Les données utilisées sont incomplètes, les méthodes simplifiées, et les résultats doivent être interprétés comme un projet d'entraînement et non une analyse poussée et valide. Cette analyse ne constitue en aucun cas une étude socio-économique publiable. Une analyse territoriale sérieuse nécessiterait des données complémentaires, une méthodologie validée par des experts, et une connaissance approfondie du terrain.

---

## Ce que mesure l'IPS

L'IPS mesure le **temps de trajet moyen** des habitants d'une commune vers différents types d'équipements et services, normalisé en rang percentile parmi les 1 266 communes d'Île-de-France.

**Ce n'est pas :**
- Un indice de présence d'équipement dans la commune (un équipement accessible en 5 minutes dans la commune voisine score aussi bien qu'un équipement dans la commune elle-même)
- Un indice de qualité des services
- Un indice de vulnérabilité sociale ou économique
- Une mesure exhaustive de l'offre de services

**C'est :**
- Une mesure relative de proximité géographique, commune par commune, sur une séléction de services.
- Un outil d'identification de disparités basiques sur le territoire

---

## Limites et biais connus

### Limites des données de transport
La grille d'accessibilité INSEE utilisée calcule les temps de trajet en **voiture**, en conditions de circulation fluide (hors heures de pointe). Cela exclut :
- Les transports en commun (métro, RER, bus, tram, navettes), les déplacements à vélo / à pieds. 
- La congestion routière qui peut être significative en heures de pointes

Pour les communes denses bien desservies en transports en commun, les temps de trajet réels peuvent être inférieurs aux valeurs utilisées. Pour les communes les moins bien déservies, sans alternative à la voiture, les temps peuvent être sous-estimés si les ménages sans voiture sont nombreux.

### Limites de la sélection des équipements
Seuls 60 types d'équipements sur les ~200 disponibles dans la BPE ont été retenus. Des catégories importantes ont été exclues (services à la personne, artisanat, commerce de proximité non alimentaire). La sélection reflète des choix subjectifs, nécessaires à la création de l'indice par une seule personne dans un temps limité. 

### Limites des pondérations
Les poids attribués aux dimensions (santé essentielle = 5, sécurité = 1, etc.) et les méthodes d'agrégation (médiane pondérée pour l'enseignement supérieur, MIN pour les écoles primaires) sont des choix subjectifs et les calculs utilisés peuvent dans certains cas influer grandement sur les rangs attribués. L'objectif était d'obtenir de manière superficielle un ordre d'importance et de fréquence dans la vie d'une population générale et variée. Tous les choix sont bien sûr discutable étant donné que ce projet est pûrement à but d'entraînement et ne se prétend en rien être une analyse socio-économique. 

### Normalisation par rang percentile
Le rang percentile garantit une distribution uniforme des scores mais signifie que la moitié des communes aura toujours un score inférieur à 0,5, indépendamment de leur niveau d'accès aux services et équipements. Le score ne dit pas si une commune est "bien équipée" dans l'absolu — seulement si elle est mieux ou moins bien équipée que la médiane IDF.

### Données socio-économiques partielles
Le revenu médian Filosofi (disponible pour 1 251 des 1 266 communes) et le taux de pauvreté (disponible pour seulement 466 communes en raison du secret statistique) ne permettent pas une corrélation robuste. Les comparaisons entre IPS et revenus sont indicatives, pas conclusives.

### Données statiques
Les données BPE (2024), la grille d'accessibilité (2023) et le Filosofi (2021) ne sont pas synchrones. Des changements structurels survenus depuis (fermeture d'établissements, nouvelles lignes de transport, évolutions démographiques) ne sont pas reflétés.

---

## Observations préliminaires

Ces observations sont le résultats de calculs simples et non-appronfondis. On en tire non des conclusions mais de possibles hypothèses pour des analyses nécessitant plus d'approfondissement. 

### L'accessibilité et le revenu sont quasi-indépendants
Le revenu médian n'explique qu'1% de la variance des scores IPS. Cela suggère que l'équipement d'un territoire en IDF est largement déconnecté de la richesse de ses habitants. On peut supposer ici que la politique public d'aménagement aiderait n'avantagerait pas les communes les plus riches. 

Cette observation mérite cependant prudence : la mesure de revenu utilisée (revenu disponible par Unité de Consommation) est imparfaite, et la corrélation pourrait être différente avec d'autres indicateurs de niveau de vie.

### Les communes denses de petite couronne dominent le classement
Les 10 premières communes (Montrouge, Choisy-le-Roi, Cachan, Clichy, Ivry-sur-Seine...) sont toutes des communes de la petite couronne parisienne. On peut supposer que la densité urbaine génère  des temps de trajet courts, indépendamment de la qualité des services qui est peut-être moins bonne avec une population plus élevée. 

### Les communes rurales de Seine-et-Marne sont les moins bien desservies
Les 10 dernières communes sont toutes des petites communes rurales de Seine-et-Marne (Saint-Martin-du-Boschet, Les Marêts, Sancy-lès-Provins...), avec des scores entre 0,03 et 0,09. L'éloignement géographique des équipements est la variable dominante pour ces territoires.

### L'accessibilité aux transports est un multiplicateur structurel
Les communes dans le quartile inférieur de score transport ont un score IPS moyen de 0,27 contre 0,58 pour les autres. Ce résultat suggère que la désertification en transports pénalise l'accès à tous les autres services. Ceci est à interpréter avec prudence car à nouveau, le temps de transport ne considère que la voiture et non les autres services. 

### Le lycée professionnel est structurellement plus éloigné que le lycée général
En moyenne, les lycées professionnels sont à 16,2 minutes contre 9,8 minutes pour les lycées généraux. Cet écart atteint 9,6 minutes en Seine-et-Marne. Cette asymétrie pourrait représenter un frein à l'orientation vers les filières professionnelles pour les élèves des communes rurales.
---

## Ce qu'il faudrait pour aller plus loin

Une analyse territoriale sérieuse de l'accessibilité aux services en IDF nécessiterait :

- **Des données de multiples moyens de transport** pour calculer des temps de trajet réels en transports en commun.
- **Des données de fréquentation** pour pondérer les équipements par leur usage réel.
- **Une analyse qualitative** des services (capacité d'accueil, délais d'attente, horaires d'ouverture) pour ajouter une dimension d'accès réel à l'équipement. 
- **Une analyse dans le temps** pour mesurer l'évolution de l'accessibilité par commune. 
- **Une analyse sur le terrain** : pour mieux comprendre la réalité géographique des communes, notamment plus éloignées de Paris, ainsi que la réalité de certains équipements comparés à leur description basique. 
- **Une validation par des experts** en géographie, statistique, urbanisme, politique sociale.
