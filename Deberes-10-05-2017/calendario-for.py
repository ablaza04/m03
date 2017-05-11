#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
			
				
			else:
				if (fil == 1 and col == 7):
					print "1",
					print "",
				
				
	print ""
					
					
					
				
