

cantidad_filas = int(input("ingrese fil:\t"))
cantidad_columnas = int(input("ingrese col:\t"))

print("\n\n")

if cantidad_columnas%2 == 0:
	impar = False
else:
	impar = True

for fila in range(1,cantidad_filas+1):

	for columna in range(cantidad_columnas//2):

		if fila%2 == 0:
			print("[V]", end ="")
			print("[A]", end ="")
		else:
			print("[A]", end ="")
			print("[V]", end ="")


	#ESTA ADENTRO DEL FOR DE FILAS
	#PERO AFUERA DEL FOR DE COLUMNAS		
	if impar:
		if fila%2 == 0:
			print("[V]", end ="")
		else:
			print("[A]", end ="")

	print("")

