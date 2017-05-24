#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system ("clear")

jugadores={ 1 :"Michael Jordan", 2 :"Kobe Bryant", 3 :"Westbrook", 4 :"Lebron James"}

print jugadores

del jugadores[1]
print jugadores
jugadores[1] = "Kyrie Irving"
print jugadores

del jugadores[2]
print jugadores
jugadores[2] = "Stephen Curry"
print jugadores

print "----------------------------------------------------------------------------"

jugadores_altura={ 1 :"1,91", 2 :"1,91", 3 :"1,91", 4 :"2,03"}

for altura in jugadores:
	print jugadores[1], "--->", jugadores_altura[1],	
	print jugadores[2], "--->", jugadores_altura[2],
	print jugadores[3], "--->", jugadores_altura[3],
	print jugadores[4], "--->", jugadores_altura[4]

