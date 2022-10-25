'''
Construya un algoritmo que sume todos los elementos en posición par de una lista.
'''

import random

#CARGA UNA LISTA DE 5 ELEMENTOS ALEATORIOS (VALORES ENTRE 1 y 100)
lista = list()
for r in range(10):
	lista.append(random.randrange(1,10))
print(lista)

#TERMINA LA CARGA ALEATORIA
suma = 0
for pos in range(len(lista)):
	if pos%2==0:
		suma = suma + lista[pos]

print(f"LA SUMA ES: {suma}")