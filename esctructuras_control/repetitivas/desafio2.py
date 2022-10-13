'''
Se inicia una campaña de recolección de colillas de cigarrillos en los barrios.

Realizá un programa que permita registrar cantidad de colillas recolectadas por un número
determinado de personas. Luego obtener estadísticas al respecto informando porcentaje de personas 
que han encontrado menos de 100 colillas, más de 100 y menos de 200, más de 200 colillas.

'''

#SOLUCION CON UN FOR (NECESITO SABER LA CANTIDAD DE PERSONAS)

personas = int(input("Cuantas personas desea analizar\t"))

menos_100 = 0
mas_100_menos_200 = 0
mas_200 = 0


for var in range(1,personas+1):

	cuantas = int(input(f"ingrese la cantidad de colillas recolectadas por la persona {var}\t"))
	if (cuantas < 100):
		menos_100 += 1
	elif (cuantas < 200):
		mas_100_menos_200 += 1
	else:
		mas_200 += 1


porcentaje_menos_100 = menos_100 * 100 / personas
porcentaje_mas_100_menos_200 = mas_100_menos_200 * 100 / personas
porcentaje_mas_200 = mas_200 * 100 / personas

print(f"el porcentaje total de personas que encontraron menos de 100 colillas son %{porcentaje_menos_100}")
print(f"el porcentaje total de personas que encontraron mas de 100 y menos de 200 colillas son %{porcentaje_mas_100_menos_200}")
print(f"el porcentaje total de personas que encontraron mas de 200 colillas son %{porcentaje_mas_200}")


# SOLUCION CON UN WHILE (NO SE CUANTAS PERSONAS SON)

menos_100 = 0
mas_100_menos_200 = 0
mas_200 = 0

continuar = 'SI'
personas = 1
while continuar.upper() == 'SI':

	cuantas = int(input(f"ingrese la cantidad de colillas recolectadas por la persona {personas}\t"))
	if (cuantas < 100):
		menos_100 += 1
	elif (cuantas < 200):
		mas_100_menos_200 += 1
	else:
		mas_200 += 1

	continuar = input("DESEA CONTINUAR CARGANDO PERSONAS SI o NO\t")
	personas +=1 


porcentaje_menos_100 = menos_100 * 100 / personas
porcentaje_mas_100_menos_200 = mas_100_menos_200 * 100 / personas
porcentaje_mas_200 = mas_200 * 100 / personas

print(f"el porcentaje total de personas que encontraron menos de 100 colillas son %{porcentaje_menos_100}")
print(f"el porcentaje total de personas que encontraron mas de 100 y menos de 200 colillas son %{porcentaje_mas_100_menos_200}")
print(f"el porcentaje total de personas que encontraron mas de 200 colillas son %{porcentaje_mas_200}")


