'''
agenda = [
			['nico',3624246431],
			['mica',3624112233],
			['dany',3624112321]
		]

		[[nombre,telefono],[nombre,telefono]]
		[nomnbre,telfono,nombre,telefono]

'''
def menu():
	print("QUE QUIERE HACER:")
	print("1-agregar")
	print("2-mostrar")
	print("3-buscar")
	print("5-SALIR")
	opcion = int(input())
	return opcion

def agregar(agenda):
	n = input("Ingrese nuevo nombre:\t")
	t = int(input(f"Ingrese telefo:{n}\t"))
	l = [n,t]
	agenda.append(l)
	return agenda

def mostrar(agenda):
	for contacto in agenda:
		#concataco es una lista con esta forma [nombre,telefono]
		print(f"{contacto[0]}---->Tel: {contacto[1]}")

def buscar(agenda):
	#funcion que muestra el telefono de un nombre buscado
	buscado = input("A quien quiere buscar?:\t")
	encontro = False
	for contacto in agenda:
		if buscado == contacto[0]:
			print(f"el telefono de {buscado} es: {contacto[1]}")
			encontro = True	
	if not encontro:
		print("El contacto buscado no existe.")
			

#-----PROGRAMA--------
agenda = list()

while True:
	op = menu()
	if op == 5:
		break
	else:
		if op == 1:
			agenda = agregar(agenda)
		elif op == 2:
			mostrar(agenda)
		elif op == 3:
			buscar(agenda)

