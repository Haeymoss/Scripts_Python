#Trier des fichiers en fonction de leur extension

import os
from glob import glob #=> obtenir la liste de l'arborescence de tous les fichier
import shutil #=> module permettant de déplacer les fichiers

chemin = "arborescence_source_du_dossier"

extensions = {".mp3": "Musique",
              ".wav": "Musique",
              ".mp4": "Videos",
              ".mov": "Videos",
              ".jpeg": "Images",
              ".jpg": "Images",
              ".png": "Images",
              ".pdf": "Documents"} #=> dictionnaires avec les differentes extensions

fichiers = glob(os.path.join(chemin, "*")) #=> joindre l'arborescence précédemment indiqué avec l'asterix. L'asterix (joker) va permettre de recupérer tous les fichier présent sans avoir à préciser une extension. 

for fichier in fichiers: #=> génère une boucle qui va passer dans chaque éléments de la liste précédemment généré 'fichiers'
    extension = os.path.splitext(fichier)[-1] #=> on split les fichier afin de récupérer l'extension après le point (.) grâce au -1 (dernier élément de la liste)
    dossier = extensions.get(extension) #=> recupérer la valeur associé au dictionnaire 'extensions' et à la clé extension. Il s'agit des nom des dossiers.
    
    if dossier: #=> renvoie 'True' si la valeur existe dans le dictionnaire pour permettre la continuité du script
        chemin_dossier = os.path.join(chemin, dossier) #=> joindre a l'arborescence existante, le nom des dossiers à créer si nécessaire
        os.makedirs(chemin_dossier, exist_ok=True) #=> crée les dossiers sans générer d'erreur s'ils sont déja existants (grace à 'existe_ok = True')
        shutil.move(fichier, chemin_dossier) #=> déplacer le fichier dans l'arborescence définie 'chemin_dossier'
