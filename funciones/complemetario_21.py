'''
Escriba una función llamada numeros_pares que, dada una lista de enteros,
 devuelve una nueva lista que contiene solo los enteros pares. 
Use la función en un programa principal y pruebe su código en varios valores diferentes. 
'''
import random

def numeros_pares(entrada):
	salida = list()
	for elto in entrada:
		if elto%2 == 0:
			salida.append(elto)
	return salida

def cargar_lista():
	lista = list()
	for r in range(5):
		lista.append(random.randrange(1,100))
	return lista

datos = cargar_lista()

print(numeros_pares(datos))