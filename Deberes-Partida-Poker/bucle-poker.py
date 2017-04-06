# coding:utf-8

salir = False
from random import randint
while (salir == False):
	
# Variables
	j1num=randint(2,14)
	j1palo=randint(1,4)
	j2num=randint(2,14)
	j2palo=randint(1,4)
	
# J1 carta aleatoria
	numero=j1num
	if (j1num==11):
		numero="J"
	if (j1num==12):
		numero="Q"
	if (j1num==13):
		numero="K"
	if (j1num==14):
		numero="A"

	if (j1palo==1):
		palo="Picas"
	if (j1palo==2):
		palo="Treboles"
	if (j1palo==3):
		palo="Diamantes"
	if (j1palo==4):
		palo="Corazones"

	print "Jugador 1 saca: " , numero, "de " , palo



# j2 carta aleatoria
	numero=j2num
	if (j2num==11):
		numero="J"
	if (j2num==12):
		numero="Q"
	if (j2num==13):
		numero="K"
	if (j2num==14):
		numero="A"

	if (j2palo==1):
		palo="Picas"
	if (j2palo==2):
		palo="Treboles"
	if (j2palo==3):
		palo="Diamantes"
	if (j2palo==4):
		palo="Corazones"

	print "Jugador 2 saca: " , numero, "de " , palo




	# Comprovem si hi ha empat
	if (j1num==j2num):
		print "Empate"
	else:
		if (j1num>j2num):
			print "Guanya jugador1"
			salir = True
		else:
			print "Guanya jugador2"
			salir = True
