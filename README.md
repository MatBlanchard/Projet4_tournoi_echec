# OpenClassrooms: Projet 4 - Gestion de tournoi d'échec
Ce programe a été réalisé dans le cadre du projet 4 de la formation python d'OpenClassrooms. Il s'agit d'un gestionnaire de tournois d'échecs.
## Instalation:
- Commencez tout d'abord par installer Python.
```
https://www.python.org/downloads/
```
- Lancez ensuite la console, placez vous dans le dossier de votre choix puis clonez ce repository:
```
git clone https://github.com/MatBlanchard/Projet4_tournoi_echec.git
```
- Déplacez vous dans le repository:
```
cd Projet4_tournoi_echec
```
- Créez un nouvel environnement virtuel:
```
python -m venv env
```
- Activez le.
```
env\scripts\activate.bat
```
- Installez les packages.
```
pip install -r requirements.txt
```
- Vous pouvez enfin lancer le script:
```
python main.py
```
## Utilisation
Le menu principal est divisé en 5 options.
### 1) Créer un tournoi
- Le programme vous permet de gérer des tournois d'échecs, sélectionnez "Créer un tournoi", puis laissez vous guider.
- Si aucun joueurs n'est présent dans la base de donnée, le programme vous renverra au menu principal.
- Vous serez invité à rentrer les résultats après chaque match. A la fin d'un tournoi, un classement sera généré.
- A tout moment, vous pouvez quitter le tournoi et la progression de celui-ci sera sauvegardé.
- A la fin du tournoi, le programme vous invitera à modifier le classement des joueurs.
### 2) Charger un tournoi
- Cette section vous permet de charger un tournoi depuis la base de donnée.
- Une fois le tournoi chargé, vous serez invité à le continuer ou voir les résultats de celui-ci si il est terminé. 
- Si aucun tournoi n'a été créer, le programme vous renverra au menu principal.
### 3) Créer un joueur
- Cette section permet de créer un joueur.
- Vous devrez rentrer le nom, le prénom, la date de naissance, le sexe et le classement de celui-ci.
- Vous pourrez modifier le classement du joueur dans la section 4.
### 4) Modifier le classement d'un joueur
- Cette section permet de modifier le classement d'un joueur.
### 5) Les rapports
- Cette section vous permet de générer différents rapport.
- Vous pouvez consulter: le classement global des joueurs par classement et ordre alphabétique.
- Les détails des tournois passés: classement des joueurs du tournoi, rondes et matchs de chaque tournois.
## Générer le rapport flake8
- Tapez la commande:
```
flake8 --format=html --htmldir=flake-report
```
- Vous devez, au prélable, avoir installé les packages
- Le rapport sera généré dans le dossier flake-report