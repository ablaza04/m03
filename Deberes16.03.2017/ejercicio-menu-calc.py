#coding: utf8

#Menu de una Calculadora


numero =int(raw_input ("Primer numero "))
numero2 =int(raw_input ("Segundo numero "))

print "Qué desea hacer el amo? "
print "1) Sumar"
print "2) Restar"
print "3) Multiplicar"
print "4) Dividir"
print "5) Salir"

numero3 = raw_input ("Elija una opción ")

if numero3 == "1":
	suma = numero + numero2
	print "El resultado es ", suma

elif numero3 == "2":
	resta = numero - numero2
	print "El resultado es", resta

elif numero3 == "3":
	multiplicar = numero * numero2
	print "El resultado es", multiplicar

elif numero3 == "4":
	dividir = numero / numero2
	print "El resultado es", dividir

elif numero3 == "5":
	print "Hasta Luego!"
		
else: 
	print "ERROR : Esa Opción no existe !!!"
	
