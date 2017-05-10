#!/usr/bin/env python
# -*- coding: utf-8 -*-


# myrange
def myrange (inici, fi, augment):

    while inici <= fi:

        yield inici

	inici = inici + augment

for fil in myrange (1,4,1):
	
	for col in myrange (1,8,1):
		# (*) tota la fila 1 i 4
		if (fil == 1) or (fil == 4):
			print "*",
			
		else: # (*) per fila 2 columna 1, fila 2 columna8 i fila 3 columna 1, fila 3 columna 8		
			if ( (fil == 2 and col == 1) or (fil == 2 and col == 8) or
			(fil == 3 and col == 1) or (fil == 3 and col == 8) ):
				print "*",
			# part del mig una "cara"	
			elif (fil==2 and col==4) or (fil==2 and col==5):
				print ".",
				
			elif (fil==3 and col==4):
				print "\\",
				
			elif (fil==3 and col==5):
				print "/",
				 
			
	print " "
















































































