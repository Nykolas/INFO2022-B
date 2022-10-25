'''
 Ingresar una palabra, carácter por carácter, en una lista y determinar si es palíndromo.
'''

palabra = list()

op = 'S'
while op == 'S':
	letra = input("INGRESE SIG CARACTER\t")
	palabra.append(letra)

	op = input("OTRA? S-N\t").upper()

#PALABRA TIENE LO QUE EL USUARIO INGRESO

original = list(palabra)
palabra.reverse()

print(original)
print(palabra)

if original == palabra:
	print("ES PALINDROMO")
else:
	print("NO ES PALINDROMO")