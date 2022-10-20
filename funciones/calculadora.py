def suma(a,b):
	r = a+b
	return r

def resta(a,b):
	r = a-b
	return r

def multiplicacion(a,b):
	r = a*b
	return r

def division(a,b):
	r = a/b
	return r

def menu():
	print("QUE QUIERE HACER:")
	print("1-SUMAR")
	print("2-RESTAR")
	print("3-DIVIDIR")
	print("4-MULTIPLICAR")
	print("5-SALIR")
	opcion = int(input())
	return opcion

#----------PROGRAMA--------------

print("WELCOME TO CALCULADORA")

while True:
	op = menu()
	if op == 5:
		break
	else:
		n1 = int(input("INGRESE EL PRIMER NUMERO\t"))
		n2 = int(input("INGRESE EL SEGUNDO NUMERO\t"))
		if op == 1:
			resultado = suma(n1,n2)
		elif op == 2:
			resultado = resta(n1,n2)
		elif op == 3:
			resultado = division(n1,n2)
		elif op == 4:
			resultado = multiplicacion(n1,n2)

		print(f"EL RESULTADO DE SU OPERACION ES: {resultado}")

print("GRACIAS POR USAR ESTA CALCULADORA")
