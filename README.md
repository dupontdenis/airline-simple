# Airline - application de gestion de vols

Petite application web construite avec Django. Elle affiche les vols enregistrés en base de données et permet de les gérer depuis l'interface d'administration Django.

## Fonctionnalités

- Affichage de la liste des vols, triée par identifiant.
- Enregistrement d'un vol avec une origine, une destination et une durée en minutes.
- Gestion des vols depuis l'interface d'administration.
- Stockage local avec SQLite.
- Affichage d'un message lorsque la liste des vols est vide.

## Technologies

- Python 3.13 (Python 3.12 ou plus récent recommandé)
- Django 6.1.2
- SQLite, fourni avec Python

## Prérequis

Installez Python et Git. Vérifiez que les commandes sont disponibles :

```bash
python --version
git --version
```

Sous Windows, `py --version` peut remplacer `python --version`.

## Cloner le dépôt

Remplacez `<URL_DU_DEPOT>` par l'URL HTTPS ou SSH du dépôt Git :

```bash
git clone <URL_DU_DEPOT>
cd <DOSSIER_DU_PROJET>
```

Par exemple, si le dépôt est hébergé sur GitHub :

```bash
git clone https://github.com/<UTILISATEUR>/<DEPOT>.git
cd <DEPOT>
```

## Créer et activer un environnement virtuel

À exécuter depuis le dossier contenant `manage.py`.

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloque l'activation du script, vous pouvez utiliser l'invite de commandes ou Git Bash à la place.

### Windows - invite de commandes (CMD)

```bat
py -m venv .venv
.venv\Scripts\activate.bat
```

### Windows - Git Bash

```bash
py -m venv .venv
source .venv/Scripts/activate
```

### macOS ou Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Une fois l'environnement activé, le nom `.venv` apparaît généralement au début de l'invite du terminal.

## Installer les dépendances

Avec l'environnement virtuel activé, installez les paquets déclarés dans `requirements.txt` :

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Le fichier `requirements.txt` fixe Django à la version 6.1.2 afin de reproduire l'environnement utilisé par le projet.

## Préparer la base de données

Les migrations créent les tables Django et la table des vols dans la base SQLite locale :

```bash
python manage.py migrate
```

La base est créée dans `db.sqlite3` à la racine du projet.

## Démarrer l'application

```bash
python manage.py runserver
```

Ouvrez ensuite ces adresses dans votre navigateur :

- Liste des vols : <http://127.0.0.1:8000/flights/>
- Administration : <http://127.0.0.1:8000/admin/>

Arrêtez le serveur avec `Ctrl+C` dans le terminal.

## Créer un compte administrateur et ajouter des vols

Créez un compte pour accéder à l'administration :

```bash
python manage.py createsuperuser
```

Suivez les questions dans le terminal, puis connectez-vous sur <http://127.0.0.1:8000/admin/>. Le modèle `Flight` y est enregistré. Vous pourrez y créer des vols avec les champs suivants :

- `origin` : ville ou aéroport de départ (64 caractères maximum) ;
- `destination` : ville ou aéroport d'arrivée (64 caractères maximum) ;
- `duration` : durée du vol en minutes.

Les vols ajoutés apparaissent ensuite sur la page `/flights/`.

## Commandes utiles

Vérifier la configuration Django :

```bash
python manage.py check
```

Lancer les tests du projet :

```bash
python manage.py test
```

Créer les fichiers de migration après une modification des modèles :

```bash
python manage.py makemigrations
python manage.py migrate
```

Désactiver l'environnement virtuel à la fin de la session :

```bash
deactivate
```

## Structure du projet

```text
airline_simple/       Configuration Django et routes principales
flights/              Application de gestion des vols
  migrations/         Historique des migrations de base de données
  templates/flights/  Modèles HTML de la page des vols
manage.py             Commandes d'administration Django
requirements.txt      Dépendances Python du projet
db.sqlite3            Base SQLite locale, créée après les migrations
```

## Remarque pour le déploiement

Les réglages actuels sont prévus pour le développement local : `DEBUG` est activé, la clé secrète est définie dans le code et `ALLOWED_HOSTS` est vide. Avant tout déploiement, configurez une clé secrète et les hôtes autorisés via des variables d'environnement, désactivez `DEBUG` et appliquez la checklist de déploiement Django.
