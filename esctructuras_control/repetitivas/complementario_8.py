# Diseñar un programa que permita calcular el total de una compra, ingresando cantidad y precio de los productos. 
# El programa debe estar preparado para que el ingreso de los datos se produzca hasta que el usuario lo desee.

print("VAMOS A CALCULAR EL MONTO TOTAL DE UNA COMPRA\n")

seguir = 'SI'

#CADA ITERACION VA A SER UN PRODUCTO, Y EL TOTAL ESTARA DETERMiNADO POR LA SUMA DE (PRECIO X CANTIDAD) DE PRODUCTO
total = 0
while (seguir.upper() == 'SI'):

	cantidad = int(input("INGRESE LA CANTIDAD: \t"))
	precio = float(input("INGRESE EL PRECIO: \t"))

	total = total + (cantidad * precio)

	seguir = input("Quiere ingresar otro producto? Si o NO\t")


print(f"EL TOTAL DE LA COMPRA ES DE  ${total}.")


'''
total = 0

coca, 200, 3 --> 3*200 = 600 ---- total = 600
hileo, 100, 1 ---> 1*100 = 100 ----- total = 700
masitas, 150 , 2 --> 2 * 150 = 300 ----total = 1000

mostrar total
'''