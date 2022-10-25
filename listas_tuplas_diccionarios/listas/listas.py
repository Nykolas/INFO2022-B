

# [20,34,43] 
# EN PYTHON AS LISTAS PUEDEN SER HETEROGENEAS.
# [ 43,'nico', [3,4,8] ] 

'''
 FUNCIONES MAS COMUNES
 CREAR UNA LISTA
 1)  x = []
 2)  x = list()
 AGREGAR ELEMENTOS (siempre agrega al final)
 x.append(elto) -->> [1,5,4] --> x.append(8) ---> [1,5,4,8]
 VER TAMAÑO DE LISTA
 len(x)
 
 VER UN VALOR ESPECIFICO
 x[indice]--> [4,6,7] --> x[1] ---> 6
 x[indice] = valor--> [4,6,7] --> x[1] = 10 ---> [4,10,7]

 '''

 # CARGAR UNA LISTA CON EL NOMBRE DE LA COM 1 y MOSTRARLA

nombre = list()

seguir = "SI"
while seguir.upper() == 'SI':
	n = input("INGRESE NOMBRE DEL ESTUDIANTE:\t")
	nombre.append(n)

	seguir = input("QUIERE SEGUIR? SI O NO\t")

print("TERMINO LA CARGA")
print("-------------------------------------")

#RECORRER UNA LISTA

for valor in nombre:

	print(f"NOMBRE-----> {valor}")


#RECORRE UNA LISTA POR EL INDICE
print("MOSTRAR POR INDICE-------------")

for indice in range(len(nombre)): # [0,1,2]
	
	print(f"NOMBRE----->{nombre[indice]}")
