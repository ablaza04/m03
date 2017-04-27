#!/usr/bin/env python
# -*- coding: utf-8 -*-

numero = 1
total = 0
for numero in range (1,6):
	print numero
	
	if (numero == 5):
		print "----"

	total = total + numero
	numero = numero+1
	
print total
