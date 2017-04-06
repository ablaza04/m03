#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
aleatorio = randint(1,13)
aleatorio1 = randint(1,13)
aleatorio2=randint(1,4)
aleatorio3=randint(1,4)
jugador1 = randint
jugador2 = randint
Tipo=randint 
Tipo1=randint 

if aleatorio2 == 1:
	Tipo ="Pica"
if aleatorio2 == 2:
	Tipo ="Diamante"
if aleatorio2 == 3:
	Tipo ="Trebol"
if aleatorio2 == 4:
	Tipo ="Corazones"

if aleatorio3 == 1:
	Tipo1 ="Pica"
if aleatorio3 == 2:
	Tipo1 ="Diamante"
if aleatorio3 == 3:
	Tipo1 ="Trebol"
if aleatorio3 == 4:
	Tipo1 ="Corazones"

	
# Machine1 carta aleatoria
if aleatorio1 == 1:
	jugador1 ="1"
	
if aleatorio1 == 2:
	jugador1 ="2"


if aleatorio1 == 3:
	jugador1 ="3"
	
	
if aleatorio1 == 4:
	jugador1 ="	4"


if aleatorio1 == 5:
	jugador1 ="5"


if aleatorio1 == 6:
	jugador1 ="6"


if aleatorio1 == 7:
	jugador1 ="7"
	

if aleatorio1 == 8:
	jugador1 ="8"
	

if aleatorio1 == 9:
	jugador1 ="9"

if aleatorio1 == 10:
	jugador1 ="10"

if aleatorio1 == 11:
	jugador1 ="J"
	
if aleatorio1 == 12:
	jugador1 ="Q"

if aleatorio1 == 13:
	jugador1 ="K"
	
print "Machine 1 saca",jugador1,Tipo


# Machine2 carta aleatoria 
if aleatorio == 1:
	jugador2 ="1"

if aleatorio == 2:
	jugador2 ="2"


if aleatorio == 3:
	jugador2 ="3"
	
	
if aleatorio == 4:
	jugador2 ="4"


if aleatorio == 5:
	jugador2 ="5"


if aleatorio == 6:
	jugador2 ="6"


if aleatorio == 7:
	jugador2 ="7"
	

if aleatorio == 8:
	jugador2 ="8"
	

if aleatorio == 9:
	jugador2 ="9"

if aleatorio == 10:
	jugador2 ="10"

if aleatorio == 11:
	jugador2 ="J"
	
if aleatorio == 12:
	jugador2 ="Q"

if aleatorio == 13:
	jugador2 ="K"
	
print "Machine 2 saca",jugador2,Tipo1




if (jugador1==jugador2):
	print "Empate!",
		
else: # Ganador Machine1
	if (jugador1 > jugador2 ):
		print "Ganador: Machine1"
	else: # Ganador Machine2
		print "Ganador: Machine2"
