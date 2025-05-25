# ⚡ Projet de Monitoring Énergétique

## 📝 Présentation

Le **Système de Monitoring Énergétique** est une plateforme web intelligente conçue pour :
- Suivre la **production** et la **consommation énergétique**,
- **Détecter les anomalies**,
- Comparer des **méthodes d’optimisation**,
- Et fournir un **dashboard visuel interactif**.

💡 Idéal pour les installations photovoltaïques, les environnements industriels ou les projets IoT liés à l'énergie.

---

## 🧱 Architecture du projet



```
energy_monitoring_project/
│
├── alerts/ # Notifications (alerter.py)
│ └── alerts_history/ # Historique des alertes en JSON
│
├── dashboard/ # Application web Flask
│ ├── app.py # Serveur principal
│ └── templates/ # Interface HTML (index.html)
│
├── data_analysis/ # Détection d’anomalies
│ └── analyzer.py
│
├── data_simulation/ # Génération et stockage de données
│ ├── simulator.py
│ └── data.csv
│
├── iot_integration/ # Intégration future de capteurs IoT
│
├── optimizers/ # Méthodes d'optimisation
│ ├── linear_optimizer.py
│ └── metaheuristic_optimizer.py
│
├── utils/ # Calcul des métriques
│ └── metrics.py
│
├── comparison.py # Comparaison des méthodes
├── requirements.txt # Dépendances Python
├── README.md # Documentation
└── tree.txt # Vue arborescente
```


---

## 🚀 Fonctionnalités

### 📊 1. Monitoring temps réel
- Dashboard responsive et moderne
- Graphiques dynamiques (Chart.js)
- Filtres temporels, export CSV et PDF

### 🔍 2. Analyse et détection d’anomalies
- Détection de surconsommation
- Seuil configurable
- Possibilité d’intégration de modèles IA

### ⚙️ 3. Optimisation (double méthode)
- **Linéaire** : ajustement par méthode déterministe
- **Métaheuristique** : approche adaptative et intelligente
- Résultat optimal affiché avec justification

---

## 🛠️ Technologies utilisées

### 🔧 Backend
- Python 3.x
- Flask
- Pandas
- FPDF

### 🎨 Frontend
- HTML5, Jinja2
- Bootstrap 5
- Chart.js
- Animate.css

---

## ▶️ Mise en route
1. Cloner le dépôt ou extraire l'archive du projet
```
   git clone https://github.com/mohammedAmm-code/Smart-House-Pfa.git
   ```
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

### 📦 Installation des dépendances

```bash
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