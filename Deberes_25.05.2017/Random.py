#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

# Random con Diccionario
diccionario = { "Goat" : "Michael Jordan" , "Black Mamba" : "Kobe Bryant" , "King" : "Lebron James"}
print "Jugadores: ", random.choice(diccionario.keys())

# Random con Lista
lista = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
print "Abecedario: ", random.choice(lista)

# Random con Tupla
tupla = (1,2,3,4,5,6,7,8,9,10)
print "Numeros: ", random.choice(tupla)
