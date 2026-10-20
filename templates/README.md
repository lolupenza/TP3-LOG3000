# templates/

## Raison d'être
Contient les gabarits HTML de l'application. Flask cherche automatiquement
les templates dans ce dossier lorsque `render_template()` est appelé.

## Fichiers
`index.html` : Interface de la calculatrice : écran, boutons (chiffres, opérateurs, C, =) et petites fonctions JavaScript pour composer l'expression.

## Dépendances et hypothèses
- Rendu par la route `/` de `app.py`, qui fournit la variable `result`.
- Utilise la syntaxe Jinja2 (`{{ ... }}`, `{# ... #}`), fournie avec Flask.
- Charge `static/style.css` via `url_for('static', ...)`.
- Le formulaire envoie le champ `display` en POST. `app.py` suppose que ce nom ne change pas.
- L'expression ne doit contenir qu'un seul opérateur (règle vérifiée par `calculate()` dans `app.py`).