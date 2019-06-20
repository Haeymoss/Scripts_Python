#!/usr/bin/python
# -*- coding: utf-8 -*-


from random import randint

print('')
print('Bienvenue à toi')

#le joueur saisi le nombre d'essai qu il estime avoir besoin 
choix_joueur_essai = int(input('saisie combien d\'essai maximum il te faudra pour me battre : '))
print('')

#variable nombre au hasard et nombe d'essai
nombre_a_deviner = randint (1,100)
nombre_essai = range(choix_joueur_essai)

#verification (permet de savoir le nombre qui doit être devine)
print(nombre_a_deviner)


# boucle conditionnel qui defini le comportement du programme
for i in nombre_essai:
	entrer_nombre = int(input('Veuillez saisir votre {0} essai : '.format(i+1)))


	if entrer_nombre < nombre_a_deviner:
		print ('le nombre à deviner est plus grand que {0}'.format(entrer_nombre))
	elif entrer_nombre > nombre_a_deviner:
		print ('le nombre à deviner est plus petit que {0}'.format(entrer_nombre))
	elif entrer_nombre == nombre_a_deviner:
		print ('Bravo :) :) :) ')
		print ('tu m\'a battu en {0} essai'.format(i+1))
		print ('')
		break


# si le nombre n'a ete trouve
if entrer_nombre != nombre_a_deviner:
	print('')
	print('le nombre à deviner etait {0} '.format(nombre_a_deviner))
	print('reessaie une prochaine fois avec plus d\'essai :)')
	print('')

print('Fin de l\'exercice')
print ('')
