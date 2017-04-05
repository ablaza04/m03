#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
aleatorio = randint(1,13)
aleatorio1 = randint(1,13)
aleatorio2 = randint(1,4)
jugador1 = aleatorio
jugador2 = aleatorio1
cartas = randint 


# Machine1 aleatorio cartas	
if aleatorio == 1:
	jugador1 ="1" 

if aleatorio == 2:
	jugador1 ="2" 

if aleatorio == 3:
	jugador1 ="3"
	
if aleatorio == 4:
	jugador1 ="4"

if aleatorio == 5:
	jugador1 ="5"

if aleatorio == 6:
	jugador1 ="6"

if aleatorio == 7:
	jugador1 ="7"

if aleatorio == 8:
	jugador1 ="8"

if aleatorio == 9:
	jugador1 ="9"

if aleatorio == 10:
	jugador1 ="10"

if aleatorio == 11:
	jugador1 ="J"
	
if aleatorio == 12:
	jugador1 ="Q"

if aleatorio == 13:
	jugador1 ="K"

print "Machine 1 saca",jugador1


# Machine2 aleatorio cartas
if aleatorio1 == 1:
	jugador2 ="1"
	
if aleatorio1 == 2:
	jugador2 ="2"

if aleatorio1 == 3:
	jugador2 ="3"
	
if aleatorio1 == 4:
	jugador2 ="4"

if aleatorio1 == 5:
	jugador2 ="5"

if aleatorio1 == 6:
	jugador2 ="6"

if aleatorio1 == 7:
	jugador2 ="7"
	
if aleatorio1 == 8:
	jugador2 ="8"
	
if aleatorio1 == 9:
	jugador2 ="9"

if aleatorio1 == 10:
	jugador2 ="10"

if aleatorio1 == 11:
	jugador2 ="J"
	
if aleatorio1 == 12:
	jugador2 ="Q"

if aleatorio1 == 13:
	jugador2 ="K"
	
print "Machine 2 saca:",jugador2 


if aleatorio2 == 1:
	cartas = "de Picas"
if aleatorio2 == 2:
	cartas = "de Diamantes"
if aleatorio2 == 3:
	cartas = "de Treboles"
if aleatorio2 == 4:
	cartas = "de Corazones"


# Empate
if jugador1==jugador2 :
	print "Empate"
	
#Gana jugador1
if (jugador1 > jugador2 ):
	print "Gana Machine 1"
else: # Gana jugador2
	print "Gana Machine 2"

