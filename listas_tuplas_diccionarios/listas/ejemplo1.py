
l1 = [10,24,35,67]

#Generar que la lista l de entrada, contenga sus valores multiplicados por 2.
# [20,48,70,134]

print(l1)

for indice in range(len(l1)):
	l1[indice] = l1[indice] * 2

print(l1)

print("--------------------")

l2 = [10,24,35,67]
print(l2)
l3 = list()
# ESTOY OBLIGADO A CREAR OTRALISTA
for valor in l2:
	l3.append(valor * 2)

print(l3)