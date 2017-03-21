# coding: utf8

#Menu de una Calculadora
 
salir = False

while(salir == False):

	print "\n1) Sumar"
	print "2) Restar"
	print "3) Multiplicar"
	print "4) Dividir"
	print "5) Salir\n"


	tecla = raw_input ("Introduzca un numero:\n")


	if (tecla == "S" or tecla == "s"): 
		print "Adios"
		salir = True

	if tecla == "1":
		print "Has escogido la opcion 1!"

	elif tecla == "2":
		print "Has escogido la opcion 2!"

	elif tecla == "3":
		print "Has escogido la opcion 3!"

	elif tecla == "4":
		print "Has escogido la opcion 4!"

	elif tecla == "5":
		print "Has escogido la opcion 5!"
