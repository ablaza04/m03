#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import listdir

# Te muestra todo los directorios y subcarpetas de la ruta donde estas.
for root, dirs, files in os.walk(".", topdown=True):
	for name in files:
		print (os.path.join(root,name))
		
########################################################################

# Saber tamaño de los directorios y archivos. 
def get_size(the_path):
    """Get size of a directory tree or a file in bytes."""
    path_size = 0
    for path, directories, files in os.walk(the_path):
        for filename in files:
            path_size += os.lstat(os.path.join(path, filename)).st_size
        for directory in directories:
            path_size += os.lstat(os.path.join(path, directory)).st_size
    path_size += os.path.getsize(the_path)
    return path_size
