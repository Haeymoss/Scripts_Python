"""1) Ouvrir le fichier prenoms.txt et lire son contenu.
   2) Récupérer chaque prénom séparément dans une liste.
   3) Nettoyer les prénoms pour enlever les virgules, points ou espace.
   4) Ecrire la liste ordonnée et nettoyée dans un nouveau fichier texte"""

from pprint import pprint#=> import de la fonction "pprint" qui permet un debug au fur et a mesure du script. Pas nécessaire

with open("arborescence_source_du_dossier_nom_fichier", "r") as f: #=> ouverture du ficheir 
    lines = f.read().splitlines() #=> lecture du fichier en séparant chaque line du fichier grace à la fonction 'splitlines'

prenoms = []
for line in lines: 
    prenoms.extend(line.split()) #=> genere une boucle qui passe a travers elemnts de chaque ligne. Les lignes vont être splités sur les espaces (car aucun autre caractere de dissociation n'aura été définit) et chaque élément ainsi dissocié va être inséré dans la dans la liste initié vierge 'prenoms'.

prenoms_final = [prenom.strip(",. ") for prenom in prenoms] #=> la fonction 'strip' permet de définir des caracteres à enlever au debut/fin d'une chaine de caractère

with open("arborescence_source_du_dossier_nouveau_nom_fichier", "w") as f:
    f.write("\n".join(sorted(prenoms_final))) #=> ouverture du fichier en ecriture. A chaque retour a la ligne "\n", on trie les éléments de la liste 'prenom_final' grâce a la fonction 'sorted'