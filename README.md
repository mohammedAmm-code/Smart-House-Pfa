# Documentation Projet : Système de Monitoring Énergétique

## Présentation générale

Le **Système de Monitoring Énergétique** est une application web permettant de surveiller, analyser et visualiser la production et la consommation d'énergie en temps réel. Cette solution complète intègre la collecte de données (simulées ou provenant de capteurs IoT), l'analyse avec détection d'anomalies, et un tableau de bord visuel interactif pour une prise de décision efficace.

## Architecture du Projet

Le projet est structuré selon une approche modulaire pour faciliter la maintenance et l'évolutivité :

```
projet/
│
├── app.py                 # Application Flask principale
├── simulator.py           # Générateur de données simulées
├── analyzer.py            # Analyse des données et détection des anomalies
├── alerter.py             # Système de notifications et alertes
├── data_simulation/       # Stockage des données simulées
│   └── data.csv           # Fichier de données
├── templates/             # Templates HTML
│   └── index.html         # Interface utilisateur du tableau de bord
├── iot_integration/       # Modules d'intégration IoT (extensible)
└── requirements.txt       # Dépendances Python
```

## Fonctionnalités principales

### 1. Génération de données
- Simulation de données de production et consommation énergétique
- Intervalle de temps configurable entre les générations de données
- Possibilité d'intégration avec des capteurs IoT réels

### 2. Analyse et détection d'anomalies
- Analyse automatique des données de consommation
- Détection des pics de consommation dépassant un seuil configurable
- Base extensible pour des algorithmes d'analyse plus complexes

### 3. Système d'alertes
- Notifications en cas de surconsommation
- Actuellement configuré pour des alertes console (extensible pour email, SMS, etc.)

### 4. Interface utilisateur moderne et intuitive
- Tableau de bord interactif avec animations fluides
- Graphiques dynamiques de suivi de production/consommation
- Filtres temporels (jour, semaine, mois)
- Indicateurs de performance clés (KPIs) visuels
- Interface responsive adaptée aux appareils mobiles

## Spécifications techniques

### Backend
- **Langage** : Python 3.x
- **Framework web** : Flask
- **Traitement de données** : Pandas
- **Stockage** : Fichiers CSV (extensible vers bases de données)

### Frontend
- **Structure** : HTML5 avec templates Jinja2
- **Style** : Bootstrap 5 avec CSS personnalisé
- **Visualisation** : Chart.js pour les graphiques interactifs
- **Animations** : Bibliothèque AOS (Animate On Scroll)
- **Icônes** : Font Awesome

## Guide de démarrage

### Prérequis
- Python 3.7 ou supérieur
- Pip (gestionnaire de paquets Python)

### Installation

1. Cloner le dépôt ou extraire l'archive du projet
2. Installer les dépendances :
   ```
   pip install -r requirements.txt
   ```

### Exécution

1. Lancer le simulateur de données dans un terminal :
   ```
   python simulator.py
   ```

2. Lancer l'application web dans un autre terminal :
   ```
   python app.py
   ```

3. Accéder à l'interface via un navigateur :
   ```
   http://localhost:5000
   ```

4. Pour tester l'analyse d'anomalies (optionnel) :
   ```
   python analyzer.py
   ```

## Personnalisation et extension

### Ajustements des seuils d'alerte
Dans `analyzer.py`, modifiez le paramètre `threshold` pour ajuster le seuil de détection des anomalies.

### Intégration IoT
Le dossier `iot_integration/` est prévu pour ajouter des modules de connexion à des capteurs réels. Les données doivent suivre le même format que les données simulées.

### Enrichissement des alertes
Le module `alerter.py` peut être étendu pour envoyer des notifications par email, SMS ou services tiers en implémentant les fonctions correspondantes.

## Avantages pour le client

- **Visibilité en temps réel** : Surveillance continue des flux énergétiques
- **Détection proactive** : Identification rapide des anomalies
- **Prise de décision éclairée** : Visualisation claire des tendances
- **Économies potentielles** : Optimisation de la consommation énergétique
- **Extensibilité** : Architecture adaptable à différents environnements
- **Interface attrayante** : Expérience utilisateur moderne et intuitive

## Perspectives d'évolution

- Implémentation d'un système d'authentification
- Ajout de prévisions de consommation par machine learning
- Développement d'une API RESTful pour intégration avec d'autres systèmes
- Support pour différents types de capteurs et sources d'énergie
- Dashboard mobile dédié
- Stockage dans une base de données pour l'historique long terme

---

© 2025 Energy Monitoring System. Tous droits réservés.