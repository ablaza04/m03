# coding:utf-8
# Les cartes tenen un nº: A,2-10,J,Q,K (total 13)
# Les cartes tenen un pal: cors, piques, trebols, diamants (total de 4)

import random 
from random import randint

salir= False

numero= ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
palos= ["Diamante","Corazon","Trebol","Pica"]

while (salir == False):
		

	# Generamos la tirada de jugador1 (coge una carta aleatoria)
	j1num=random.choice(numero)
	j1palo=random.choice(palos)

		
	# Generamos la tirada de jugador2 (coge una carta aleatoria)
	j2num=random.choice(numero)
	j2palo=random.choice(palos)



	# Comprobamos si hay empate
	if (j1num==j2num):
		print "Jugador 1 saca: " , j1num, "de " , j1palo
		print "Jugador 2 saca: " , j2num, "de " , j2palo
	
		print "Empate"
	else: #Si gana j1 o j2
		
		if (j1num>j2num):
			print "Jugador 1 saca: " , j1num, "de " , j1palo
			print "Jugador 2 saca: " , j2num, "de " , j2palo
			print "Gana jugador1"
		else:
			print "Jugador 1 saca: " , j1num, "de " , j1palo
			print "Jugador 2 saca: " , j2num, "de " , j2palo
			print "Gana jugador2"
			
	salir = True
