#Escriba un algoritmo que permita cargar una lista. 
#Y que luego, una vez cargada, controle y sustituya cualquier elemento negativo por 0.

numeros = list()

seguir = "SI"
while seguir.upper() == 'SI':
	n = int(input("INGRESE NUMERO:\t"))
	numeros.append(n)
	seguir = input("QUIERE SEGUIR? SI O NO\t")


for indice in range(len(numeros)):
	if numeros[indice] < 0:
		numeros[indice] = 0

print(numeros)
