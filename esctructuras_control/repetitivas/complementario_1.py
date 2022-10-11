# Determinar el número mayor de 10 números ingresados.

TOPE = 11
# WHILE
'''
i = 1
maximo = 0

while (i < TOPE):
	numero = int(input(f"Ingrese el numero {i}\t"))

	if numero > maximo:
		maximo = numero

	i+= 1

print(f"EL VALOR MAS GRANDE INGRESADO ES: {maximo}")
'''
#FOR

# range(1,TOPE) --> [1,2,3,4,5,6,7,8,9,10]
maximo = 0

for i in range(1,TOPE):

	numero = int(input(f"Ingrese el numero {i}\t"))

	if numero > maximo:
		maximo = numero

	print(maximo)

print(f"EL VALOR MAS GRANDE INGRESADO ES: {maximo}")