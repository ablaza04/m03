#!/usr/bin/env python
# -*- coding: utf-8 -*-

# myrange
def myrange (inici, fi, augment):

    while inici <= fi:

        yield inici

	inici = inici + augment

for fil in myrange (1,8,1):
	
	for col in myrange (1,8,1):
		
		if (fil %2 == 0) or (col %2 == 0):
			print "x",
		else:
			print " ",
	
	print ""
