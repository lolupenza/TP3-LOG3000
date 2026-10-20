# static/

## Raison d'être
Contient les fichiers statiques de l'application, c'est-à-dire les fichiers envoyés
tels quels au navigateur, sans traitement par Python. Flask sert automatiquement
ce dossier à l'adresse `/static/...`.

## Fichiers
`style.css` : Mise en forme de la calculatrice : centrer de la page, apparence de l'écran (`#display`), grille de 4 colonnes pour les boutons et couleurs des chiffres et des opérateurs.

## Dépendances et hypothèses
- Chargé par `templates/index.html` via `url_for('static', filename='style.css')`.
- Le CSS suppose que `index.html` utilise les sélecteurs suivants : `.calculator`, `h1`, `#display`, `.buttons`, `.btn` et `.operator`. Renommer l'un d'eux dans le HTML sans le modifier ici casse la mise en forme.
- La grille de `.buttons` suppose 4 boutons par ligne (3 chiffres + 1 opérateur).
- Aucune dépendance externe (pas de framework CSS ni de police à télécharger).
