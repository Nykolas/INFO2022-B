#Solicitar el ingreso de números al usuario y emitir un mensaje para 
#determinar si es par o impar. El ciclo debe finalizar cuando el usuario ingresa 0.


seguir = 0

while (seguir != 1):
	numero = int (input ("Ingrese número de usuario : \t"))

	if numero % 2 == 0:
		print (f"Numero ingresado {numero} es Par")
	else:
		print (f"Numero ingresado {numero} es Impar")

	seguir = int (input ("Quieres terminar?, 1 -> Si | 0 -> No \t"))

print ("-----------Terminamos--------------------") 