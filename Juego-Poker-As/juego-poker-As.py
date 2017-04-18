# coding:utf-8
# Les cartes tenen un nº: A,2-10,J,Q,K (total 13)
# Les cartes tenen un pal: cors, piques, trebols, diamants (total de 4)

from random import randint

# Generem la tirada de jugador1 (agafa una carta aleatoria)
j1num=randint(2,14)
j1palo=randint(1,4)

numero=j1num
if (j1num==11):
    numero="J"
if (j1num==12):
    numero="Q"
if (j1num==13):
    numero="K"
if (j1num==14):
    numero="A"

if (j1palo==1):
    palo="Picas"
if (j1palo==2):
    palo="Treboles"
if (j1palo==3):
    palo="Diamantes"
if (j1palo==4):
    palo="Corazones"

print "Jugador 1 te: " , numero, "de " , palo



# Generem la tirada de jugador2 (agafa una carta aleatoria)
j2num=randint(2,14)
j2palo=randint(1,4)

numero=j2num
if (j2num==11):
    numero="J"
if (j2num==12):
    numero="Q"
if (j2num==13):
    numero="K"
if (j2num==14):
    numero="A"

if (j2palo==1):
    palo="Picas"
if (j2palo==2):
    palo="Treboles"
if (j2palo==3):
    palo="Diamantes"
if (j2palo==4):
    palo="Corazones"

print "Jugador 2 te: " , numero, "de " , palo




# Comprovem si hi ha empat
if (j1num==j2num):
    print "Empat"
else:
    if (j1num>j2num):
        print "Guanya jugador1"
    else:
        print "Guanya jugador2"

