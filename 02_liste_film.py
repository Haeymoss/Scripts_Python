#!/usr/bin/python
# -*- coding: utf-8 -*-




# demande a l'utilisateur de rentrer des nom de film
#ajoute ces films dans une liste
#gérer les doublons
#classer ces films par ordre alphabetique
#afficher la liste

import random as r 
from random import randint

#
continuer ='o'
liste_film = []

while continuer == 'o':


	print('')
	film_ajoute = input('Insérer le nom d\'un film : ')

#condition du film a ajouter avec la mise en minuscule des données saisie afin de s assurer que le film n est pas deja existant 
	if film_ajoute.lower() in [film.lower() for film in liste_film] :
		print('{0} est déja dans la liste '.format(film_ajoute))

#ajoute le film a la liste
	else :
		
		liste_film.append(film_ajoute)	



	continuer = input('voulez vous continuer ? o/n ')


#trie alphabetiquement la liste
liste_film.sort()
print('')
print(liste_film)
