# Module templates - Interface utilisateur

## Rôle du module

Le répertoire `templates/` contient les modèles HTML utilisés par Flask pour générer les pages de l'application.

Il assure la présentation de la calculatrice et permet à l'utilisateur d'interagir avec les fonctionnalités mathématiques disponibles.

## Fichiers du module

| Fichier | Responsabilité |
|---|---|
| `index.html` | Définit l'interface de la calculatrice, le formulaire, les boutons et les fonctions JavaScript de gestion de l'affichage. |
| `README.md` | Documente le fonctionnement et les dépendances du module. |

## Fonctionnement

### Interface HTML

Le fichier `index.html` contient :

- Un champ d'affichage pour les expressions et les résultats.
- Des boutons numériques et des opérateurs arithmétiques.
- Un bouton permettant d'effacer l'expression.
- Un bouton permettant de soumettre le calcul.

### Interactions JavaScript

Deux fonctions assurent les interactions avec le champ d'affichage :

**`appendToDisplay(value)`**

Ajoute une valeur à l'expression affichée lorsque l'utilisateur sélectionne un chiffre ou un opérateur.

**`clearDisplay()`**

Vide le champ d'affichage lorsque l'utilisateur sélectionne le bouton d'effacement.

### Communication avec Flask

1. L'utilisateur construit une expression à l'aide des boutons.
2. Le formulaire transmet l'expression au serveur par une requête HTTP POST.
3. Le serveur traite l'expression à l'aide de la logique Python.
4. Flask génère la page HTML avec le résultat ou un message d'erreur.

## Dépendances et hypothèses

- Le module dépend de Flask pour le rendu des modèles HTML.
- Le fichier `style.css`, situé dans `static/`, fournit la présentation visuelle.
- JavaScript doit être activé dans le navigateur pour utiliser les boutons interactifs.
- Le traitement des opérations mathématiques est effectué côté serveur, et non dans JavaScript.

## Maintenance

Toute modification du formulaire HTML doit rester compatible avec les données attendues par le serveur Flask.

Les modifications des boutons et de leurs interactions doivent être vérifiées afin de garantir que les expressions envoyées au serveur correspondent aux opérations souhaitées.