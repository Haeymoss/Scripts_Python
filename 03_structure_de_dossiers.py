import os
import json

#permet d'indiquer, si la structure de dossier existe deja, l'arborescence de celle-ci
def print_structure(adresse_json):
	with open(adresse_json, 'r') as f:
		structure_json = json.load(f)
		print('Les dossiers ont deja ete cree')
		print('Voici l\'arborescence des dossiers :')
		for key, values in structure_json.items():
			print ('. {0}'.format(key))
			for value in values:
				print('--- {0}'.format(value))

			print('')
			print('_'*30)



#creation des dossiers selon l'arborescence du dictionnaire
def structure_dossier (dictionnaire):
	for key, values in dictionnaire.items():
		for value in values:
			dossier = '{0}/{1}/{2}'.format(adresse_base, key, value)
			os.makedirs(dossier)
			print('Creation du dossier : {0}'.format(dossier))


#creation et ecriture du fichier json∏
def ecriture_json (fichier_json, dictionnaire):
	with open (fichier_json, 'w') as f:
		json.dump(dictionnaire, f, indent=4)




"""saisie des differentes adresses et creation de variables les contenant"""
adresse_base = r'\Users\ruidasilva\Desktop\Structure'
adresse_base = adresse_base.replace('\\', '/')

adresse_json = r'\Users\ruidasilva\Desktop\Structure\structure.json'
adresse_json = adresse_json.replace('\\', '/')



#structure souhaite des dossiers
structure = { 
			'cle1' : ['valeur1', 'valeur2', 'valeur3'],
			'cle2' : ['valeur4', 'valeur5', 'valeur6'],
			'cle3' : ['valeur7', 'valeur8', 'valeur9']
			}



#si le fichier json est déja existant et généré avec l'arborescence souhaité
if os.path.isfile(adresse_json):
	print_structure(adresse_json)


#sinon appel des fonction et execution de celles ci
else:
	structure_dossier (structure)
	ecriture_json (adresse_json, structure)
