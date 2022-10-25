'''
Un número primo es un número entero mayor que 1 que solo es divisible por uno y por sí mismo. 
Escriba una función que determine si su parámetro es primo o no, devolviendo 
True si lo es y False en caso contrario. Escriba un programa principal que lea un
número entero del usuario y muestre un mensaje que indique si es primo o no.

Asegúrese de que el programa principal no se ejecutará si el archivo que contiene su 
solución se importa a otro programa.
'''

def primo(numero):
	
    divisores = []
    for i in range(1, numero+1):
        if(numero % i == 0):
            divisores.append(i)

    if(len(divisores) > 2):
        return 'No es primo'
    else:
        return 'Es primo'

numero = int(input("Ingrese un numero:\n"))
print(primo(numero))
