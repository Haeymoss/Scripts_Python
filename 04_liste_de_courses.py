import os
import json

dossier_courant = os.path.dirname(__file__) #=> recupere le chemin du dossier courant
chemin_liste = os.path.join(dossier_courant, "liste.json") #=> imbrique le chemin du dossier courant avec le fichier liste.json

if os.path.exists(chemin_liste): #=> si le fichier existe deja, l'ouvre
    with open(chemin_liste, "r") as f:
        liste_de_courses = json.load(f)
else: #=> si le fichier n'existe pas, crée une liste
    liste_de_courses = []

affichage = """
Choisissez une option:
\t1: Ajouter un élément
\t2: Enlever un élément
\t3: Afficher la liste
\t4: Vider la liste
\t5: Terminer
""" #=> les 3""" permettent de générer une chaine de caractère sur plusieurs lignes. Menu du script.

option = "0" #=> définit une option par défaut

while option != "5":
    option = input(affichage) #=> boucle tant que le choix est différent de 5, la boucle s'exécute sans fin
    
    if option == "1":
        item_a_ajouter = input("Entrez le nom de l'élément à ajouter: ")
        liste_de_courses.append(item_a_ajouter) #=> ajoute un élément à la liste de course
    elif option == "2":
        item_a_retirer = input("Entrez le nom de l'élément à enlever: ")
        if item_a_retirer in liste_de_courses:
            liste_de_courses.remove(item_a_retirer) #=> supprime un élément de la liste de course
    elif option == "3":
        if liste_de_courses: #=> evalue la liste. Si la liste est constituée d'éléments elle est considéré comme 'True', sinon 'False'
            print("\n".join(liste_de_courses)) #=> si la liste contien des éléments, elle est considéré comme 'True'. Affiche les éléments avec un retour à la ligne (\n)
        else: 
            print("La liste ne contient aucun élément.") #=> si la liste ne contient pas d'éléments, elle est considéré comme 'False'.
    elif option == "4":
        liste_de_courses.clear() #=> vide la liste

with open(chemin_liste, "w") as f:
    json.dump(liste_de_courses, f, indent=4) #=> sauvegarder la liste ainsi constitué.


