#!/usr/bin/env python
# -*- coding: utf-8 -*-

numero = 1
total = 0
salir = False
while (salir == False) :
	print numero
	
	
	if (numero == 5):
		salir = True
		print "----"
	total = total+numero
	numero = numero+1
print total
