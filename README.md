# TP3 - LOG3000 : Calculatrice Flask

**Équipe 19**

## Description du projet

Ce projet est une calculatrice web simple écrite en Python avec le framework **Flask**.
L'utilisateur compose une expression à l'aide de boutons dans son navigateur (par exemple `8+2`),
puis le serveur calcule le résultat et l'affiche à l'écran.

# TP3 - LOG3000 : Calculatrice Flask

**Équipe 19**

## Description du projet

Ce projet est une calculatrice web basique écrite en Python avec le framework Flask.
L'utilisateur compose une expression à l'aide de boutons dans son navigateur (par exemple `8+2`),
puis le serveur calcule le résultat et l'affiche à l'écran.

### Portée
- Opérations prises en charge : addition (`+`), soustraction (`-`), multiplication (`*`) et division (`/`).
- Une expression contient un seul opérateur entre deux nombres (ex. : `12*3`).
- Les nombres sont traités comme des nombres décimaux.
- **Hors portée** : expressions à plusieurs opérateurs (`1+2+3`), parenthèses, nombres négatifs en début d'expression (`-5+2`).

Ce projet a été fourni avec des erreurs. Le mandat de l'équipe 19 est de les corriger,
de documenter le code et d'ajouter des tests.

### Structure du projet

TP3-LOG3000/
├── app.py          # Serveur Flask : route « / » et analyse de l'expression (calculate)
├── operators.py    # Fonctions arithmétiques : add, subtract, multiply, divide
├── templates/      # Gabarits HTML (voir templates/README.md)
│   └── index.html
└── static/         # Fichiers CSS (voir static/README.md)
    └── style.css

# TP3 - LOG3000 : Calculatrice Flask

**Équipe 19**

## Description du projet

Ce projet est une calculatrice web simple écrite en Python avec le framework **Flask**.
L'utilisateur compose une expression à l'aide de boutons dans son navigateur (par exemple `8+2`),
puis le serveur calcule le résultat et l'affiche à l'écran.

### Portée
- Opérations prises en charge : addition (`+`), soustraction (`-`), multiplication (`*`) et division (`/`).
- Une expression contient **un seul opérateur** entre deux nombres (ex. : `12*3`).
- Les nombres sont traités comme des nombres décimaux.
- Hors portée : expressions à plusieurs opérateurs (`1+2+3`), parenthèses, nombres négatifs en début d'expression (`-5+2`).

Ce projet a été fourni avec des erreurs. Le mandat de l'équipe 19 est de les **corriger**,
de **documenter** le code et d'ajouter des **tests**.

### Structure du projet

```
TP3-LOG3000/
├── app.py          # Serveur Flask : route « / » et analyse de l'expression (calculate)
├── operators.py    # Fonctions arithmétiques : add, subtract, multiply, divide
├── templates/      # Gabarits HTML (voir templates/README.md)
│   └── index.html
└── static/         # Fichiers CSS (voir static/README.md)
    └── style.css
```

## Installation

### Prérequis
- Git
- Python 3.8 ou plus récent

### Étapes d'installation

1. **Cloner le dépôt.** Sur la page GitHub du dépôt, cliquer sur le bouton Code, choisir l'onglet HTTPS et copier l'URL. Dans un terminal, à l'emplacement voulu :
   ```bash
   git clone https://github.com/lolupenza/TP3-LOG3000.git
   cd TP3-LOG3000
   ```

2. **Installer la dépendance :**
   ```bash
   pip install flask
   ```

## Utilisation

### Lancer l'application
Avec l'environnement virtuel activé :
```bash
python app.py
```
Puis ouvrir **http://127.0.0.1:5000** dans un navigateur.
Pour arrêter le serveur, appuyer sur `Ctrl + C` dans le terminal.

### Utiliser la calculatrice
1. Cliquer sur les chiffres pour saisir le premier nombre.
2. Cliquer sur un opérateur (`+`, `-`, `*`, `/`).
3. Saisir le second nombre.
4. Cliquer sur **=** pour obtenir le résultat.
5. Cliquer sur **C** pour effacer l'écran.

### Exécuter les tests
Les tests utilisent pytestet se trouvent dans le dossier `tests/`.

1. Installer pytest (dans l'environnement virtuel) :
   ```bash
   pip install pytest
   ```
2. Lancer tous les tests depuis la racine du projet :
   ```bash
   pytest
   ```
3. Lancer un seul fichier de tests :
   ```bash
   pytest tests/test_operators.py
   ```
Chaque correction de bogue doit être accompagnée d'un test qui reproduit le problème.

## Flux de contribution

### Issues
- Chaque bogue ou tâche fait l'objet d'une **issue** GitHub, avec une description claire (comportement attendu / comportement observé).
- Assigner l'issue à la personne qui s'en occupe avant de commencer.

### Branches
- `main` contient la version stable. Les changments au code ne sont jamais poussés directement sur main.
- Créer une branche par issue, à partir de `main` à jour :
  ```bash
  git checkout main
  git pull
  git checkout -b fix/nom-court-du-bogue
  ```
- Convention de nommage :
  - `fix/...` : correction de bogue (ex. : `fix/soustraction-inversee`)
  - `feature/...` : nouvelle fonctionnalité
  - `test/...` : ajout de tests

### Commits
- Messages courts et descriptifs, au présent : `Corrige l'ordre des opérandes dans subtract`.
- Mentionner l'issue concernée : `Corrige la division entière (#4)`.

### Pull requests
1. Pousser la branche : `git push -u origin nom-de-la-branche`.
2. Ouvrir une **pull request** vers `main` sur GitHub.
3. Dans la description, expliquer le.s changement.s et lier l'issue avec `Closes #numéro` (l'issue se fermera automatiquement à la fusion).
4. Vérifier que tous les tests passent (`pytest`).
5. Obtenir l'approbation d'au moins **un** autre membre de l'équipe avant de fusionner.