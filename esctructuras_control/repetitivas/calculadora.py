
print("-----------WELCOME-----------")
seguir = 'SI'
while seguir == 'SI':

	print("QUE QUIERE HACER:")
	print("1-SUMAR")
	print("2-RESTAR")
	print("3-DIVIDIR")
	print("4-MULTIPLICAR")
	print("5-SALIR")
	opcion = int(input())

	if opcion == 5:
		seguir = 'NO'
	else:
		n1 = int(input("INGRESE EL PRIMER NUMERO\t"))
		n2 = int(input("INGRESE EL SEGUNDO NUMERO\t"))
		if opcion == 1:
			resultado = n1 + n2
		elif opcion == 2:
			resultado = n1 - n2
		elif opcion == 3:
			resultado = n1 // n2
		elif opcion == 4:
			resultado = n1 * n2
		else:
			resultado = 0
			print("NO INGRESO UNA OPCION VALIDA")

		print(f"EL RESULTADO DE SU OPERACION ES: {resultado}")

print("GRACIAS POR USAR ESTA CALCULADORA")

