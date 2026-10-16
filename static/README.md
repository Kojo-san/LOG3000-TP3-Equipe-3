# Module static - Ressources statiques

## Rôle du module

Le répertoire `static/` contient les ressources statiques utilisées par l'application Flask. Ces fichiers sont transmis au navigateur sans être générés dynamiquement par le serveur.

Dans ce projet, ce module est responsable de la présentation visuelle de la calculatrice.

## Fichiers du module

| Fichier | Responsabilité |
|---|---|
| `style.css` | Définit l'apparence générale, les couleurs, les dimensions, la disposition des boutons et les effets visuels de la calculatrice. |
| `README.md` | Documente le rôle et les dépendances du module. |

## Fonctionnement

Le fichier `style.css` définit notamment :

- Le centrage de la calculatrice dans la fenêtre.
- L'apparence du conteneur principal.
- Le style du champ d'affichage.
- L'organisation des boutons dans une grille.
- La distinction visuelle des opérateurs.
- Les effets au survol et au clic.

## Dépendances et hypothèses

- Le module est servi automatiquement par Flask à partir du répertoire `static/`.
- Le fichier CSS est chargé dans `templates/index.html` avec `url_for('static', filename='style.css')`.
- Les sélecteurs CSS doivent correspondre aux classes et identifiants utilisés dans le HTML.
- Aucune bibliothèque CSS externe n'est nécessaire.

## Maintenance

Toute modification des classes ou identifiants HTML doit être vérifiée dans `style.css` pour éviter de compromettre la présentation de l'interface.