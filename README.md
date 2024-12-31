# RPLIFE - Conway's Game of Life

### Description

Il s'agit d'une implémentation sous console du Jeu de la vie ou Game of
Life en anglais.
C'est donc une application console développée en python.

## Guide d'installation.

Pour installer il faut se place dans le repertoire de projet
(`rplife`) et activer l'environnement virtuel python :

```bash
# sous windows
venv\Scripts\activate
# sous linux
venv/Scripts/activate
```

Puis, installer l'application (en vrai c'est créer le packet de l'application)

```bash
# pour pouvoir aisément effectuer des modifications effectuer des
# modifications, utiliser l'option -e :
python -m pip install -e .

# pour juste installer et tester :
python -m pip install .
```

`.` pour l'installer à partir du repertoir actuel c'est à dire le
dossier du projet.

## Guide d'utilisation

Etant une application en console, il y a une aide. Pour cela, taper
la commande :

```bash
rplife --help
```

dont le contenu est le suivant :

```
usage: rplife [-h] [--version] [-p {Blinker,Toad,Beacon,Pulsar,Penta Decathlon,Glider,Glider Gun,Bunnies}] [-a] [-v {UnifiedView}]
              [-g GEN] [-f FPS]

Conway's Game of Life in your terminal

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -p {Blinker,Toad,Beacon,Pulsar,Penta Decathlon,Glider,Glider Gun,Bunnies}, --pattern {Blinker,Toad,Beacon,Pulsar,Penta Decathlon,Glider,Glider Gun,Bunnies}
                        take a pattern for the Game of Life (default : Blinker)
  -a, --all             show all available patterns in a sequence
  -v {UnifiedView}, --view {UnifiedView}
                        display the life grid in a specific view (default: UnifiedView)
  -g GEN, --gen GEN     number of generations to display (default: 10)
  -f FPS, --fps FPS     number of frames per second (default: 7)
```

Tout y est décrit. Mais à titre d'illustration, pour lancer le pattern
par défaut, taper juste :

```bash
rplife
```

Un pattern interressant est "Pulsar", vous pouvez bien l'admirer en tapant :

```bash
rplife -p "Pulsar" -g 100 -f 3
```

Et pour voir tous les patterns disponibles, taper :

```bash
rplife -a
```

## Tester sans installer

Si vous n'installez pas l'application mais vous voulez juste lancer le code que vous avez téléchargé,
placez vous dans le repertoire du projet, activer l'environnement virtuel :

```bash
# sous windows
venv\Scripts\activate
# sous linux
venv/Scripts/activate
```

puis tapez par exemple :

```bash
python -m rplife
```

Vous l'aurez compris, il n'y a juste qu'à prefixer les commandes d'exécution par `python` après avoir
activer l'environnement virtuel qui contient les dépendances du projet.
