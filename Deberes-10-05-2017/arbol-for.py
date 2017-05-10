#!/usr/bin/env python
# -*- coding: utf-8 -*-

# myrange
def myrange (inici, fi, augment):

    while inici <= fi:

        yield inici

	inici = inici + augment

for fil in myrange (1,6,1):
	
	for col in myrange (1,5,1):
		
		if (fil == 1 and col == 3):
			print "*",
			
		elif (fil ==2 and col == 3):
			print "^",
		elif (fil == 3 ):
			if (col == 2):
				print "^",
			if (col == 3):
				print "^",
			if (col == 4):
				print "^",
			else:
				print "",
				
		elif (fil == 4):
			print "^",
		elif (fil == 5 and col == 3) or (fil == 6 and col == 3):
			print "I",
			
		else:
			print " ",
			
	print ""
			
				
				
				
