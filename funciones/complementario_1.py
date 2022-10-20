def tarifa(x):
	TARIFA = 15
	TARIFA_BASE = 40
	recorrido = ((x * 1000)//140)* TARIFA + TARIFA_BASE
	return recorrido

print("\n-----Bienvenido al TAXI-----\n")
km = float(input("Ingrese los KM recorridos: "))
print("Su total es de: $", tarifa(km))
print("\n-----Fin del recorrido-----\n")

r = 3
r.sqrt(2)