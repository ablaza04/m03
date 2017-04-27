#!/usr/bin/env python
# -*- coding: utf-8 -*-

numero = 2
total = 0
salir = False 
while (salir == False):
	print numero
	
	if (numero %2==0):
		
		if (numero == 6):
			salir = True
			
	total = total+numero 
	numero = numero+1

print "----"
print total
