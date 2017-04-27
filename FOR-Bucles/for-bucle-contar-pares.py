#!/usr/bin/env python
# -*- coding: utf-8 -*-


limite = input ("Hasta que numero desea el amo? ") 
for contador in range (0,limite+1):
	
	if contador %2 == 0:
		print contador
		
	if (contador == limite) :
		salir = True
	contador = contador+1
