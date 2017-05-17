#!/usr/bin/env python
# -*- coding: utf-8 -*-


import calendar

mes= input ("Introduzca el mes que desea el amo: ")
anyo= 2017

cont=1

num_dia_mes= calendar.monthrange(anyo,mes)[1]
dia_semana=(calendar.weekday(anyo,mes,1))+1

# myrange
def myrange (inici, fi, augment):

    while inici <= fi:

	yield inici

	inici = inici + augment

for fil in myrange (1,6,1):
	
	for col in myrange (1,7,1):
		
		if (fil == 1):
			if (col == 1):
				print "Lun",
			elif (col == 2):
				print "Mar",
			elif (col == 3):
				print "Mie",
			elif (col == 4):
				print "Jue",
			elif (col == 5):
				print "Vie",
			elif (col == 6):
				print "Sab",
			elif (col == 7):
				print "Dom",
			
		elif (fil==2):
			if (dia_semana <= col):
				print cont,
				cont = cont+1
			else:
				print " ",
			
		elif (cont <= num_dia_mes):
			print cont,
			cont =cont+1
		else:
			print "",
	print " "
					
					
				
