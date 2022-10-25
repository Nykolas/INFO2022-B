
def CrearABC():
	#CREA UNA LISTA DEL ABCDARIO
	abc = list()
	for x in map(chr, range(97, 123)):
		abc.append(x)
	return abc
	#RETORNA ['a','b','c'....]

def Capi(cadena):
	# el primero de todos
	abc = CrearABC()
	cadena = list(cadena)

	#PONE MAYUSCULA PRIMERA LETRA (SI ES DEL ABC)
	if cadena[0] in abc:
		cadena[0] = cadena[0].upper()


	for indice in range(len(cadena)):
		# EL DE LA i solita
		if cadena[indice] == 'i':
			if len(cadena)-1 > indice and cadena[indice - 1] == " " and cadena[indice + 1] == " ":
				cadena[indice] = cadena[indice].upper()

		# el primero despues de un signo
		if cadena[indice] in ['.','!','¿','?']:
			# esto sirve para asegurarme que no estoy en el ultimo caracter de la frase!!!!
			if len(cadena) - 1 > indice and cadena[indice+1] in abc:
				cadena[indice + 1] = cadena[indice + 1].upper()

			if len(cadena) - 2 > indice and cadena[indice+2] in abc and cadena[indice + 1] == " ":
				cadena[indice + 2] = cadena[indice + 2].upper()

					
	return "".join(cadena)


s = input("INGRESE UNA FRASE:\n")
resultado = Capi(s)

print("EL TEXTO RESULTANTE ES:\n"+resultado)




