'''
Cargue dos listas, y actualice la primer lista con los elementos que están en la segunda y no en la primera.
'''
#random.randrange(1,20) NOS DAUN NUMERO ALEATORIO ENTRE 1 y 20
import random

#CARGA LAS LISTAS ALEATORIAS
lista1 = list()
for r in range(10):
	lista1.append(random.randrange(1,20))

lista2 = list()
for r in range(10):
	lista2.append(random.randrange(1,20))


print(lista1)
print(lista2)


for elto in lista2:
	if elto not in lista1:
		lista1.append(elto)

print(lista1)

