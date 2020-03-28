"""Itérez sur le dictionnaire 'd' afin de créer les dossiers 'Films', 'Employes' et 'Exercices' 
ainsi que leur sous-dossier"""

import os

chemin = "/Users/.../..." #=> Chemin du dossier de destination

d = {"Films": ["Le seigneur des anneaux", #=> exemples de dictionnaires à itérer
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

for key, value in d.items():
    for dossier in value:
        chemin_dossier = os.path.join(chemin, key, dossier)
        os.makedirs(chemin_dossier, exist_ok=True)