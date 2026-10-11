# 🏗️ Python Object-Oriented Programming (OOP) for Data Engineering

## 📝 Description du Projet
Ce module est la suite logique de mon cursus en Data Engineering. L'objectif de ce projet est de refactoriser un pipeline **ETL** procédural en une architecture logicielle **Orientée Objet (POO)** hautement maintenable, modulaire et robuste.

Le pipeline extrait des données hétérogènes de deux sources (base relationnelle **MySQL** et documents **MongoDB**), encapsule la logique de traitement dans des classes spécialisées, standardise le transport des flux via des *Data Batches* natifs, et sécurise l'exécution à l'aide d'exceptions métiers personnalisées.

---

## 📐 Architecture Logicielle & Design Patterns

### 1. Héritage & Polymorphisme (Connecteurs Multi-Sources)
* **`BaseFileConnector`** : Classe parente abstraite centralisant la logique commune de validation d'existence et de chargement des fichiers de données.
* **`MongoProjectConnector`** & **`MySqlProductConnector`** : Classes enfants spécialisées surchargeant (*overriding*) les méthodes d'extraction pour nettoyer les spécificités propres à chaque technologie (BSON/JSON vs Données relationnelles mises à plat).

### 2. Encapsulation & Sécurité (Data Quality)
* Utilisation d'attributs protégés (`_filepath`) pour restreindre les modifications accidentelles de configuration depuis l'extérieur de la classe.
* Séparation stricte de la responsabilité : Les connecteurs extraient, la classe `DataBatch` transporte, et `ETLPipelineEngine` orchestre le flux global.

### 3. Dunder Methods (Intégration Pythonic)
* Implémentation des méthodes spéciales `__str__` et `__len__` sur la classe `DataBatch` afin de permettre une interaction native avec les fonctions standards de Python (ex: `len(batch_projets)` ou `print(batch)`).

### 4. Robustesse (Exceptions Personnalisées)
* Création de la classe d'exception `MissingFileException` pour isoler les pannes d'infrastructure.
* Utilisation complète des structures `try / except / else / finally` garantissant la libération systématique des ressources mémoire en fin de cycle.

---

## 📂 Structure du Répertoire
```text
├── projecttracker.projects.json   # Export NoSQL brut (Projets MongoDB)
├── produits_mysql_propres.json    # Données SQL nettoyées (Produits MySQL)
├── app_pipeline.py                # 🚀 Moteur du pipeline d'orchestration global en POO
├── synthese_poo_complete.json     # 📊 JSON Consolidé final (Généré automatiquement)
└── README.md                      # Documentation d'architecture
```

---

## ⚙️ Installation et Exécution

### 1. Activer l'environnement virtuel (.venv)
Sur Windows (PowerShell) :
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

### 2. Lancer le Pipeline ETL en POO
```bash
python app_pipeline.py
```

---

## 📊 Format du Livrable Consolidé (`synthese_poo_complete.json`)
Le fichier final unifie les indicateurs de volume et injecte les enregistrements nettoyés dans une structure claire [2] :
```json
{
    "total_projets": 15,
    "total_produits": 14,
    "projets": [ ... ],
    "produits": [ ... ]
}
```
