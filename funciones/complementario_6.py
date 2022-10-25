'''
Escriba una función que tome una cadena de caracteres como primer parámetro y 
el ancho de la terminal en caracteres como segundo parámetro.
Su función debe devolver una nueva cadena que consta de la cadena original y
el número correcto de espacios iniciales para que la cadena original aparezca
centrada dentro del ancho proporcionado cuando se imprima. 

No agregue ningún carácter al final de la cadena. Incluya un programa principal que use su función.
'''

def caracteres(cadena,ancho):
	a_rellenar_izq = (ancho-len(cadena)) // 2

	# OPCION SIN CICLO
	salida_sin_ciclo = (" " * a_rellenar_izq) + cadena

	# OPCION CON CILCO
	'''salida_con_ciclo = ""
	for k in range(a_rellenar_izq):
		salida_con_ciclo = " " + salida_con_ciclo
	salida_con_ciclo = salida_con_ciclo + cadena'''

	return salida_sin_ciclo


cadena=input("Ingrese la cadena de caracteres:\t")
ancho = 124 #SUPUESTO

ca = caracteres(cadena,ancho)

print(ca)
