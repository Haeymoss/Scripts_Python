"""1) Parcourir chaque fichier et récupérer le numéro du compte bancaire 'Crédit Mutuel' ainsi que le numéro de sécurité sociale.
   2) Afficher les deux numéros à la fin du script."""

import json
import glob #=> module glob

dossier = "arborescence_source_du_dossier**"
files = glob.glob(dossier, recursive=True) #=> fonction récursive permettant de récupérer la liste de l'arborescence de chaque fichier. L'asterix (**joker) va permettre de recupérer tous les fichier présent sans avoir à préciser une extension

numero_de_compte = None #=> Initialise les 2 variables identifié comme point de départ départ "None".
numero_securite_sociale = None

for f in files: #=> parcourir chaque fichier avec une boucle
    if f.endswith(".json"): #=> methode permettant d'identifier les fichier finissant par ".json"
        with open(f, "r") as f:
            contenu = json.load(f) #=> in récupère le contenu du fichier ainsi ouvert
            if "Credit Mutuel" in contenu: #=> on s'assure que la chaine de caractere recherché est présente dans le contenu
                numero_de_compte = contenu["Credit Mutuel"]["Numero de compte"] #=> on récupere la valeur souhaitée contenu dans le dictionnaire "Credit Mutuel", puis dans le dictionnaire "Numero de compte"
    elif f.endswith(".txt"): #=> de la même façon si le fichier rencontré est un .'txt, methode permettant d'identifier les fichier finissant par ".txt"
        with open(f, "r") as f:
            contenu = f.read()
            if "Numéro de sécurité sociale" in contenu:
                numero_securite_sociale = contenu.split(":")[-1] #=> le valeurs recherchés sont présenté dans le fichier source de la sorte : Numéro de sécurité sociale : 123456789. 

print(numero_de_compte)          
print(numero_securite_sociale) #=> renvoi les valeur recherchés
