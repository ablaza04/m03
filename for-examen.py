#!/usr/bin/env python
# -*- coding: utf-8 -*-


# myrange
def myrange (inici, fi, augment):

    while inici <= fi:
		
        yield inici	
        
	inici = inici + augment

#fil = fila i col = columna
for fil in myrange (1,5,1):
	
	for col in myrange (1,4,1):
		
		if (fil == 1):
			if (col == 2):
				print "A",
			elif (col == 3):
				print "B",
			elif (col == 4):
				print "C",
			else:
				print "-",
		
		else:
			
				
			if (col == 1):
				print fil-1,
			
			elif (
					((fil == 3) and (col == 3))
					or ((fil == 4) and (col == 2))
				 ): 			 
				print "*",
					  
			else:
				print "-",

	print ""
