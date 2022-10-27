# [valor , valor, valor]
'''
CLAVE NO SE PUEDE REPETIR
VALOR puede ser "culaquier cosa" es decir:
-numero
-logico
-string
-lista
-diccionario

NO EXISTEN INDICES, SE ACCEDE POR LA CLAVE
en una lista se accede asi lista[indice]
en un diccionario se accede asi diccionario[clave]
{ clave: valor , clave: valor , clave: valor}

'''
dicc = {}
print(dicc)
print("------------------------------")
#cargar un valor
#dicc[clave] = valor

dicc['nombre'] = 'Nicolas'
print(dicc)
# SI LA CLAVE NO EXISTE, LA CREA
# PERO SI LA CLAVE YA EXISTE, MODIFICA SU VALOR
print("------------------------------")
dicc['nombre'] = 'MiCA'
print(dicc)
print("------------------------------")
dicc['telefono'] = 36245534332
print(dicc)
print("------------------------------")
#PARA VER UN VALOR NECESITO LA CLAVE
#print(dicc['nombre'])

#SOLO RECORRE LAS CLAVEs
for x in dicc:
	print(x)
print("------------------------------")

#PARA RECORRE CLAVE VALOR
# SE USAN 2 VARIABLES, DONDE LA PRIMERA VA A TENER LA CLAVE Y LA SEGuNDA EL VALOR

for nombre,telefono in dicc.items():
	print(f"{nombre}---->{telefono}")