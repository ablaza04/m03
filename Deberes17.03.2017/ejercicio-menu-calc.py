#coding: utf8

#Menu de una Calculadora

print "Qué desea hacer el amo? "
print "0) Salir"
print "1) Sumar"
print "2) Restar"
print "3) Multiplicar"
print "4) Dividir"

opcion = raw_input ("Elija una opción ")

numero1 =int(raw_input ("Primer numero "))
numero2 =int(raw_input ("Segundo numero "))



if opcion == "1":
	suma = numero1 + numero2
	print "El resultado es ", suma

elif opcion == "2":
	resta = numero1 - numero2
	print "El resultado es", resta

elif opcion == "3":
	multiplicar = numero1 * numero2
	print "El resultado es", multiplicar

elif opcion == "4":
	dividir = numero1 / numero2
	print "El resultado es", dividir

elif opcion == "0":
	print "Hasta Luego!"
		
else: 
	print "ERROR : Esa Opción no existe !!! "
	
