# Module de tests - LOG3000 TP3

## Objectif

Ce répertoire contient les tests automatisés de la calculatrice Flask. Ils permettent de vérifier le comportement des opérations mathématiques, du serveur Flask et de l'interface HTML.

Les tests sont développés avec `pytest` et servent à détecter les anomalies, vérifier les corrections et prévenir les régressions.

## Organisation

| Fichier | Responsabilité |
|---|---|
| `test_operators.py` | Tests unitaires des quatre opérations arithmétiques |
| `test_app.py` | Tests de la logique de calcul et des routes Flask |
| `test_interface.py` | Tests des libellés, boutons et éléments HTML |
| `README.md` | Documentation du module de tests |

## Prérequis

- Python 3
- Flask
- pytest

Installer les dépendances depuis la racine du projet :

```bash
python -m pip install -r requirements.txt
```

## Exécution des tests

Exécuter tous les tests :

```bash
python -m pytest tests/ -v
```

Exécuter un module particulier :

```bash
python -m pytest tests/test_operators.py -v
python -m pytest tests/test_app.py -v
python -m pytest tests/test_interface.py -v
```

Exécuter un test spécifique :

```bash
python -m pytest tests/test_operators.py::test_divide_by_zero -v
```

## Méthodologie

1. Définir le comportement attendu.
2. Créer des tests pour les cas normaux, limites et invalides.
3. Exécuter les tests sur la version initiale.
4. Documenter les anomalies dans GitHub Issues.
5. Corriger chaque anomalie dans une branche distincte.
6. Relancer les tests concernés.
7. Exécuter l'ensemble des tests après intégration.

## Résultats initiaux

Les tests ont été exécutés avant les corrections.

| Module | Tests | Réussis | Échoués |
|---|---:|---:|---:|
| Opérations | 17 | 6 | 11 |
| Application Flask | 19 | 14 | 5 |
| Interface HTML | 17 | 13 | 4 |
| **Total** | **53** | **33** | **20** |

Les résultats mettent en évidence des erreurs de soustraction, multiplication, division et d'affichage des boutons.

## Limites

Les tests de l'interface inspectent le HTML produit par Flask. Ils ne simulent pas les clics dans un navigateur réel.

Les tests ne garantissent pas l'absence de tous les bogues possibles. Ils couvrent les comportements définis par les cas de test.

## Suivi des anomalies

Chaque bogue confirmé doit faire l'objet d'une GitHub Issue contenant :

- Une description du problème.
- Le comportement attendu.
- Le comportement observé.
- Les étapes de reproduction.
- Le ou les tests échoués.
- Le membre responsable.

Les corrections seront effectuées dans des branches séparées et intégrées par Pull Request après validation.