# LOG3000 - TP3 : Calculatrice Web Flask

**Équipe :** 03  
**Cours :** LOG3000 - Processus du génie logiciel  
**Établissement :** Polytechnique Montréal  
**Dépôt GitHub :** https://github.com/Kojo-san/LOG3000-TP3-Equipe-3

## 1. Présentation du projet

Ce projet consiste à documenter, tester et améliorer une calculatrice web développée avec Python et Flask.

La calculatrice permet d'effectuer quatre opérations arithmétiques : addition, soustraction, multiplication et division.

Dans le cadre du TP3, l'équipe doit également appliquer des pratiques de développement collaboratif :

- Gestion de versions avec Git et GitHub.
- Documentation du code et des modules.
- Tests logiciels et détection des bogues.
- Suivi des anomalies avec GitHub Issues.
- Correction des bogues dans des branches distinctes.
- Révision et intégration avec les Pull Requests.

Le projet est limité à une calculatrice simple permettant d'évaluer une expression composée de deux opérandes et d'un opérateur.

## 2. Technologies utilisées

| Technologie | Utilisation |
|---|---|
| Python | Logique de calcul et serveur |
| Flask | Application web et gestion des requêtes HTTP |
| HTML  | Structure et rendu dynamique de l'interface |
| CSS | Présentation visuelle |
| JavaScript | Interactions avec les boutons |
| Git / GitHub | Gestion de versions et collaboration |
| pytest | Tests automatisés prévus pour le projet |

## 3. Structure du projet

```text
LOG3000-TP3-Equipe-3/
├── app.py
├── operators.py
├── README.md
├── static/
│   ├── README.md
│   └── style.css
└── templates/
    ├── README.md
    └── index.html
```

**Description des composants :**

- `app.py` : initialise Flask, définit les routes HTTP, analyse les expressions et appelle les opérations mathématiques.
- `operators.py` : contient les fonctions d'addition, de soustraction, de multiplication et de division.
- `templates/index.html` : fournit l'interface utilisateur et les interactions JavaScript.
- `static/style.css` : définit l'apparence de la calculatrice.

Les répertoires `static/` et `templates/` possèdent chacun leur propre README décrivant leurs responsabilités et leurs dépendances.

Un répertoire `tests/` sera ajouté pour les tests automatisés.

## 4. Prérequis

Pour installer et exécuter le projet :

- Python 3 et pip.
- Git.
- Un navigateur web moderne.
- Un éditeur de code, comme Visual Studio Code (recommandé).

## 5. Installation

### Étape 1 - Cloner le dépôt

```bash
git clone https://github.com/Kojo-san/LOG3000-TP3-Equipe-3.git
cd LOG3000-TP3-Equipe-3
```

### Étape 2 - Créer un environnement virtuel

```bash
python -m venv .venv
```

### Étape 3 - Activer l'environnement

Sur Windows (PowerShell) :

```powershell
.\.venv\Scripts\Activate.ps1
```

Sur Linux ou macOS :

```bash
source .venv/bin/activate
```

### Étape 4 - Installer les dépendances

```bash
python -m pip install -r requirements.txt
```

## 6. Exécution de l'application

Depuis la racine du projet, exécuter :

```bash
python app.py
```

Ouvrir ensuite l'adresse suivante dans un navigateur :

http://127.0.0.1:5000/

Le serveur Flask est configuré pour fonctionner en mode débogage dans l'environnement local. Ce mode n'est pas destiné à un déploiement en production.

## 7. Utilisation de la calculatrice

1. Ouvrir l'application dans le navigateur.
2. Sélectionner les chiffres pour construire une expression.
3. Choisir l'un des quatre opérateurs disponibles : `+`, `-`, `*` ou `/`.
4. Entrer le deuxième nombre.
5. Cliquer sur `=` pour envoyer l'expression au serveur.
6. Consulter le résultat affiché.
7. Utiliser `C` pour effacer le champ.

**Exemple :**

Expression : `10+5`  
Résultat attendu : `15`

L'application accepte une seule opération à la fois. Les expressions contenant plusieurs opérateurs ne sont pas prises en charge.

Le projet initial contient des anomalies connues qui seront identifiées par les tests et corrigées dans le cadre du TP3.

## 8. Tests

Les tests automatisés seront développés avec `pytest` et placés dans le répertoire `tests/`.

Ils permettront notamment de vérifier :

- Les quatre opérations arithmétiques.
- Le traitement des expressions valides.
- Le rejet des expressions invalides.
- Le traitement des erreurs, notamment la division par zéro.
- Le comportement des routes Flask.

Pour exécuter les tests depuis la racine du projet :

```bash
python -m pytest -v
```

Pour exécuter un fichier de tests particulier :

```bash
python -m pytest tests/test_operators.py -v
```

Le fichier `tests/README.md` précisera les cas couverts et les instructions d'exécution.

## 9. Processus de contribution

Le projet utilise un processus de collaboration fondé sur les GitHub Issues, les branches et les Pull Requests.

### 9.1 Création d'une Issue

Lorsqu'un bogue est détecté :

1. Créer une Issue dans GitHub.
2. Décrire le comportement observé et le comportement attendu.
3. Fournir les étapes de reproduction ou le test échoué.
4. Assigner l'Issue à un membre de l'équipe.

### 9.2 Création d'une branche

Chaque bogue doit être corrigé dans une branche distincte.

Convention de nommage :

```text
fix/issue-XX-description
```

Exemple :

```bash
git checkout main
git pull origin main
git checkout -b fix/issue-01-soustraction
```

### 9.3 Correction et validation

Effectuer la correction, puis exécuter les tests concernés.

Créer ensuite un commit explicite :

```bash
git add .
git commit -m "fix: corriger la soustraction (issue #1)"
```

Publier la branche :

```bash
git push -u origin fix/issue-01-soustraction
```

### 9.4 Pull Request

Après la correction :

1. Ouvrir une Pull Request vers `main`.
2. Expliquer le bogue et la solution.
3. Fournir les résultats des tests.
4. Associer la Pull Request à l'Issue.
5. Faire réviser les changements par un autre membre.
6. Fusionner la Pull Request après validation.

### 9.5 Validation finale

Après les fusions, exécuter l'ensemble des tests sur `main` pour vérifier qu'aucune régression n'a été introduite.

## 10. Documentation

La documentation du projet est répartie entre :

- Les docstrings Python dans `app.py` et `operators.py`.
- Les commentaires HTML, CSS et JavaScript.
- Les README des répertoires `static/` et `templates/`.
- Le README des tests, ajouté avec la suite de tests.
- Le présent README principal.

## 11. Équipe

- **Gamaliel Kalefe**
- **Marily Lemire**
- **Anita Bou Malham**

Les membres collaborent à la documentation, aux tests, à la correction des bogues et à la révision des Pull Requests.

## 12. État du projet

Projet universitaire en cours de documentation, de vérification et de correction.

Les résultats des tests, les Issues et les Pull Requests permettront de retracer les modifications et de démontrer la fiabilité de la version finale.