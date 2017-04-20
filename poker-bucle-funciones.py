# coding: utf-8
# Cartas nº: A,2-10,J,Q,K (total 13)
# palos: corazones, picas, treboles, diamantes (total de 4)

from random import randint

saldo=100
apuesta=0
salir=False
salir_apuesta=False	
	
if (saldo < 10):
	salir_apuesta = True
	salir = True 
else:
	salir_apuesta=False
	print "Estado de su Saldo actual:" , saldo
	print "Apuesta mínima 10€"
	print "Salir: -1"
	apuesta=input("Introduzca su apuesta: ")
		
while (salir_apuesta == False):
	salir = True	
	if (apuesta==-1):
			salir_apuesta=True
			salir=True
	else:
		if (apuesta>=10 and apuesta<=saldo):
			saldo=saldo-apuesta
			salir_apuesta=True
			
		else:
				print "Apuesta Incorrecta"
				if (apuesta<10):
					print "La apuesta Mínima es de 10€ chaval!"
				if (apuesta>saldo):
					print "No puede apostar más de su saldo"
				print "Salir: -1"
				apuesta=input("Introduca su apuesta: ")	

saldo=100
apuesta=0
salir=False
j1num=randint(2,14)
j1palo=randint(1,4)
j2num=randint(2,14)
j2palo=randint(1,4)
							
while (salir==False):
				
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
	

	

		# Empate
	if (j1num == j2num):
		print "Gana Banca Siempre!"	
		
	else:
		#Gana jugador
		if (j2num>j1num):
			print "Has Ganado eres un Crack!"
			saldo=saldo+(apuesta*2)
		else:
			print "Perdedor, Manco!!!"
	
	print "Estado de su Saldo actual:" , saldo
	salir = True		

	# Ni gana ni pierde
	if (saldo==100):
		print "\nGracias por venir"
	else:
		
		if (saldo<100):
			print "\nPringao, Gracias a Ti me forro"
		else:
			print "\nMe he quedado con tu cara, no vuelvas"	
	
