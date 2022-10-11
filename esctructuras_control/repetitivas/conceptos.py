
# while [condicion/es]:
#	 CODIGO

# CODIGO SE EJECUTA REPETITIVAMENTE, HASTA QUE LA CONDICIONE SEA FALSA
'''
seguir = 'SI'

while (seguir.upper() == 'SI'):

	tope = int(input("INGRESE EL TOPE A MOSTRAR\t"))

	numero = 1
	while (numero <= tope):
		print(numero, end = ' ')
		numero += 1   # i = i + 1

	print("\n------------------------------------------")
	seguir = input("QUIERE PROBAR NUEVAMENTE?, ingrese SI o NO \t")


print("--------------TERMINAMOS---------------")

'''

#FOR EN PYTHON, RECORRE CUALQUIER ESTRUCTURA QUE SE ITERABLE

#ESTRUCTURAS ITERABLES
# RANGOS (SIMULA EL FOR COMUN) 
# LISTAS [1,5,8,19]
# TUPLAS (1,10,22)
# DICCIONARIOS {k:v, k:v}
# ETC

# range(valor_inicial, valor_final, incremento)
# valor_inicial , si no lo aclaro por defecto es 0
# incremento si no lo aclaro por defecto es 1

# range(10) == range(0,10,1) ---> [0,1,2,3,4,5,6,7,8,9]
# range(1,5) ---> [1,2,3,4]
# range(1,10,2) --> [1,3,5,7,9]

#for valor in range(0,100,2):
#	print(valor, end= " ")

#for x in [0,1,2,3]:

tope = int(input("INGRESE EL TOPE A MOSTRAR\t"))

for numero in range(1,tope+1):
	print(numero, end = '/')