# WebDeck

Le WebDeck est une application Flask qui permet à l'utilisateur de contrôler son ordinateur à distance depuis n'importe quel appareil doté d'un navigateur et d'un écran tactile. Contrairement au StreamDeck d'Elgato, qui nécessite un équipement physique, le WebDeck utilise une application Flask que l'utilisateur héberge sur son propre ordinateur.

## Installation
1. Clonez le dépôt git en utilisant la `git clone https://github.com/LeLenoch/WebDeck-PRE-RELEASE.git` ou en téléchargant le [fichier ZIP](https://github.com/LeLenoch/WebDeck-PRE-RELEASE/archive/refs/heads/main.zip)

2. Accédez au dossier du projet : `cd webdeck`

3. Installez les dépendances nécessaires avec `pip install -r requirements.txt`

4. Exécutez le programme en utilisant `python main.py`

5. Ouvrez votre navigateur web préféré sur votre appareil et accédez à l'URL suivante : http://IP:PORT/, remplacer IP par l'ip locale de votre ordinateur (s'affiche lors du lancement du programme) et le PORT par le port inscrit tout en bas de config.json (par défaut 5000)


## Configuration

La configuration des boutons se fait dans un fichier JSON. Voici un exemple de fichier `config_example.json`:


Les paramètres de configuration suivants sont disponibles:

- `ear-soundboard`: active ou désactive le retour son de la soundboard. Valeurs valides: `"true"` ou `"false"`.
- `mp3_method`: spécifie la méthode à utiliser pour lire les fichiers MP3. Valeurs valides: `"vlc"` ou `"pygame"`.
- `show-console`: active ou désactive l'affichage de la console sur la page. Valeurs valides: `"true"` ou `"false"`.
- `dev-mode`: active ou désactive le mode de développement. Valeurs valides: `"true"` ou `"false"`.
- `spotify-api`: spécifie les informations d'identification de l'API Spotify. Les champs `USERNAME`, `CLIENT_ID` et `CLIENT_SECRET` doivent être renseignés.

Les paramètres de configuration de l'interface utilisateur suivants sont disponibles:

- `theme`: spécifie le thème à utiliser pour l'interface utilisateur. Le nom du fichier CSS doit être spécifié.
- `background`: spécifie l'image à utiliser comme arrière-plan de l'interface utilisateur.
- `show-names`: active ou désactive l'affichage des noms des boutons. Valeurs valides: `"true"` ou `"false"`.
- `names-color`: spécifie la couleur du texte pour les noms de boutons.
- `computer-usage-reload-time`: spécifie le temps en millisecondes entre chaque rafraîchissement des informations d'utilisation de l'ordinateur.
- `height`: spécifie la hauteur de la grille de boutons.
- `width`: spécifie la largeur de la grille de boutons.

Chaque bouton est défini par un objet dans le tableau `buttons`. Les champs suivants sont disponibles pour chaque bouton:

- `name`: le nom à afficher sur le bouton.
- `position`: la position du bouton sur la grille (par exemple, "a1", "b2", etc.).
- `image`: l'image à afficher sur le bouton.
- `image_size`: la taille de l'image. Peut être spécifié en pourcentage ou en pixels.
- `background-color`: la couleur de fond du bouton.
- `color`: la couleur du texte sur le bouton.
- `message`: la commande à exécuter lorsque le bouton est pressé.

Pour configurer les boutons, modifiez simplement le fichier `config_example.json` en fonction de vos besoins.

## Commandes disponibles

Les commandes suivantes sont disponibles pour les boutons:

- `/folder <nom_du_dossier>` : ouvre le dossier spécifié du webdeck
- `/openfile <chemin_vers_le_fichier>` : ouvre le fichier ou logiciel spécifié
- `/start <chemin_vers_le_fichier>` : ouvre le fichier ou logiciel spécifié
- `/batch <code>` : exécute du batch
- `/exec <code>` : exécute du python
- `/volume +` : augmente de 1 le volume de windows
- `/volume -` : baisse de 1 le volume de windows
- `/volume set <nombre>` : change le volume de windows
- `/spotify likesong` : mettre le son actuellement joué sur spotify en favoris
- `/spotify likealbum` : mettre l'album actuellement joué sur spotify en favoris
- `/spotify add_or_remove` : ajoute ou retire le son actuellement joué dans la playlist spécifiée
- `/spotify add_to_playlist <nom de la playlist>` : ajoute le son actuellement joué dans la playlist spécifiée
- `/spotify remove_from_playlist` : retire le son actuellement joué dans la playlist spécifiée
- `/spotify follow_or_unfollow_artist` : s'abonne ou se désabonne de l'artiste actuellement joué
- `/spotify follow_artist` : s'abonner à l'artiste actuellement écouté
- `/spotify unfollow_artist` : se désabonner de l'artiste actuellement en écoute
- `/spotify volume +` : augmente de 1 le volume de SPOTIFY (pas de windows) (requiert spotify prenium)
- `/spotify volume -` : baisse de 1 le volume de SPOTIFY (pas de windows) (requiert spotify prenium)
- `/spotify volume set <nombre>` : change le volume de SPOTIFY (pas de windows) (requiert spotify prenium)
- `/fullscreen` : active/désactive le mode plein écran
- `/reload` : recharge la page
- `/screensaver` : éteint les écrans
- `/screensaver full` : éteint les écrans complètement
- `/screensaver off` : rallume les écrans
- `/superAltF4` : ferme de force la fenêtre au premier plan
- `/taskill <programme.exe>` : ferme de force le programme spécifié
- `/forceclose <programme.exe>` : ferme de force le programme spécifié
- `/restart <programme.exe>` : redémarre le programme spécifié
- `/restartexplorer` : redémarre l'explorateur Windows
- `/key <touche>` : presse une touche
- `/write <texte>` : écrit le texte
- `/writeandsend <texte>` : écrit le texte et appuie sur Entrée
- `/copy` : copie (Ctrl+C)
- `/copy <texte>` : copie le texte spécifié
- `/paste` : colle (Ctrl+V)
- `/paste <texte>` : colle le texte spécifié
- `/clipboard` : ouvre le presse-papiers de Windows
- `/clearclipboard` : efface le presse-papiers de Windows
- `/locksession` : verrouille la session Windows
- `/speechrecognition` : active la reconnaissance vocale de Windows pour écrire en parlant



Exemple du fichier json:
```json
{
    "settings": {
        "ear-soundboard": "true",
        "mp3_method": "vlc",
        "show-console": "false",
        "dev-mode": "false",
        "spotify-api": {
            "USERNAME": "",
            "CLIENT_ID": "",
            "CLIENT_SECRET": ""
        }
    },
    "front": {
        "theme": "theme1.css",
        "background": "",
        "show-names": "true",
        "names-color": "#b3b3b3",
        "computer-usage-reload-time": "3000",
        "height": "4",
        "width": "8",
        "buttons": {
            "index": [
                {
                    "name": "Folder 1",
                    "position": "a1",
                    "image": "folder.png",
                    "image_size": "70%",
                    "message": "/folder folder1"
                },
                {
                    "name": "Spotify",
                    "position": "a2",
                    "image": "spotify.png",
                    "image_size": "70%",
                    "message": "/folder spotify"
                },
                {
                    "name": "Fullscreen",
                    "position": "a3",
                    "image": "fullscreen2.png",
                    "image_size": "50%",
                    "message": "/fullscreen"
                },
                {
                    "name": "Refresh",
                    "position": "a4",
                    "image": "reload.png",
                    "image_size": "50%",
                    "message": "/reload"
                },
                {
                    "name": "ETEINDRE ECRANS",
                    "position": "a5",
                    "image": "screensaver.png",
                    "image_size": "100%",
                    "message": "/screensaver"
                },
                {
                    "name": "ETEINDRE ECRANS FULL",
                    "position": "a6",
                    "image": "screensaver-full.png",
                    "image_size": "50%",
                    "message": "/screensaver full"
                },
                {
                    "name": "RE ALLUMER ECRANS",
                    "position": "a7",
                    "image": "computer-screen.svg",
                    "image_size": "50%",
                    "message": "/screensaver off"
                },
                {
                    "name": "restart explorer",
                    "position": "b3",
                    "image": "https://www.sordum.org/wp-content/uploads/2020/01/restart_explorer.png",
                    "image_size": "80%",
                    "message": "/restartexplorer"
                },
                {
                    "VOID": "VOID"
                },
                {
                    "name": "button pious",
                    "position": "c7",
                    "image": "D:\\Images\\jop3.png",
                    "image_size": "100%",
                    "message": "/openfile D:\\Images\\jop3.png"
                },
                {
                    "name": "Config",
                    "position": "d1",
                    "image": "",
                    "image_size": "90%",
                    "background-color": "91a2ff",
                    "message": "/open-config"
                },
                {
                    "name": "Color picker",
                    "position": "d4",
                    "image": "eyedropper.svg",
                    "image_size": "50%",
                    "color": "#fff",
                    "background-color": "#2e2e2e",
                    "message": "/colorpicker lang:fr"
                },
                {
                    "name": "GPU usage",
                    "position": "d5",
                    "image": "",
                    "image_size": "100%",
                    "color": "#fff",
                    "background-color": "#2e2e2e",
                    "message": "/usage 'GPU USAGE' usage_dict['gpus']['GPU1']['utilization_percent']"
                },
                {
                    "name": "RAM USAGE",
                    "position": "d6",
                    "image": "",
                    "image_size": "100%",
                    "message": "/usage 'RAM%' usage_dict['memory']['usage_percent']"
                },
                {
                    "name": "disk E usage",
                    "position": "d7",
                    "image": "",
                    "image_size": "100%",
                    "message": "/usage 'disque E' usage_dict['disks']['E']['total_gb']"
                },
                {
                    "name": "Cpu usage",
                    "position": "d8",
                    "image": "",
                    "image_size": "100%",
                    "color": "#fff",
                    "background-color": "#2e2e2e",
                    "message": "/usage 'CPU USAGE' usage_dict['cpu']['usage_percent']"
                }
            ],
            "folder1": [
                {
                    "name": "back to index",
                    "image": "folder.png",
                    "image_size": "70%",
                    "message": "/folder index"
                }
            ],
            "spotify": [
                {
                    "name": "Retour",
                    "position": "a1",
                    "image": "back10.svg",
                    "image_size": "110%",
                    "message": "/folder index"
                },
                {
                    "name": "Previous",
                    "position": "a6",
                    "image": "skip-start-fill.svg",
                    "image_size": "100%",
                    "background-color": "#1ed664",
                    "message": "/soundcontrol previous"
                },
                {
                    "name": "Play/Pause",
                    "position": "a7",
                    "image": "playpause.png",
                    "image_size": "100%",
                    "background-color": "#1ed664",
                    "message": "/soundcontrol playpause"
                },
                {
                    "name": "Next",
                    "position": "a8",
                    "image": "skip-end-fill.svg",
                    "image_size": "100%",
                    "background-color": "#1ed664",
                    "message": "/soundcontrol next"
                },
                {
                    "name": "Mute",
                    "position": "d8",
                    "image": "volume-mute.png",
                    "image_size": "100%",
                    "background-color": "#1ed664",
                    "message": "/soundcontrol mute"
                }
            ]
        }
    },
    "url": {
        "ip": "0.0.0.0",
        "port": 5000
    }
}
```
