lista = [1,2,3,3,3,3,3,3,4]

n = 3

for i in range(len(lista)):
	if n in lista:
		lista.remove(n)

	print(lista)

print(lista)