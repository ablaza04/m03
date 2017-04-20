# coding: utf-8
# Cartas nº: A,2-10,J,Q,K (total 13)
# palos: corazones, picas, treboles, diamantes (total de 4)

from random import randint


salir = False 
apuesta = raw_input("Introduzca su apuesta: ")
saldo = 100
apuesta_minima = 10
	
while (salir == False):
	salir = True
	
	j1num=randint(2,14)
	j1palo=randint(1,4)
	j2num=randint(2,14)
	j2palo=randint(1,4)
	
	
	if (apuesta_minima < 10):
		print "Apuesta Mínima 10€ !!!"	
		salir = True 
		salir_apuesta = True
	
	
			
	# Banca carta aleatoria
	numero=j1num
	if (j1num==11):
		numero="J"
	if (j1num==12):
		numero="Q"
	if (j1num==13):
		numero="K"
	if (j2num==14):
		numero="A"	

	if (j1palo==1):
		palo="Picas"
	if (j1palo==2):
		palo="Treboles"
	if (j1palo==3):
		palo="Diamantes"
	if (j1palo==4):
		palo="Corazones"

	print "Banca saca: " , numero, "de " , palo



	# Yo carta aleatoria
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

	print "Yo saco: " , numero, "de " , palo

	
	
	# Gana Banca o Ganas Tu
	if (j1num > j2num):
		print "Gana Banca !"
		print ("Estado de su saldo Actual: "), saldo
		saldo=saldo-apuesta
		salir = True 
	
		
	else: 
		print "Ganas Tu, eres un Crack!"
		print ("Estado de su saldo Actual: "), saldo
		saldo=saldo+(apuesta*2)
		salir = True
	
	# Empate
	if (j1num == j2num):
		print "Gana Banca Siempre!"	
		print ("Estado de su saldo Actual: "), saldo
		
		
		
