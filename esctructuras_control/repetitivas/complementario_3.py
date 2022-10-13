#Diseñar un programa que permita obtener el producto entre A y B mediante sumas sucesivas.
# A x B = A + A + A + A (B cantaidad)
# 3 x 4 = 12 == 3 + 3 + 3 + 3 = 12



A = int (input ("Ingrese el valor A :\t"))
B = int (input ("Ingrese el valor B: \t"))

suma = 0

for x in range (0,B,1):
	suma = suma + A  #(es lo mismo que --> suma += A)

print (f"Suma final = valor A*B : \t {suma} ")