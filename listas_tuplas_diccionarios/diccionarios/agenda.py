'''
	OP1
	agenda = [
				{'nombre':___, 'telefono':___, 'mail':____},
				{'nombre':___, 'telefono':___, 'mail':____},
				{'nombre':___, 'telefono':___, 'mail':____}
			]
	agenda[0]['nombre']
	agenda[1]['nombre']
	agenda[2]['nombre']		
	OP2
	agenda = {
				'nombre':{'telefono':_____, 'mail':____}
				'nombre':{'telefono':_____, 'mail':____}
				'nombre':{'telefono':_____, 'mail':____}
			}
	agenda['nombre'] --> {'telefono':_____, 'mail':____}
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
	nom = input("Ingrese nuevo nombre:\t")
	tel = int(input(f"Ingrese telefo\t"))
	mail = input(f"Ingrese mail\t")

	#OP1
	dic = {'telefono':tel, 'mail':mail}
	#OP2
	#dic ={}
	#dic['telefono'] = tel
	#dic['mail'] = mail
	if nom in agenda.keys():
		print(f"El contacto {nom} ya existe y no se lo puede agregar!")
		print(f"Si quiere modificarlo ejecute la opcion modificar")
	else:
		agenda[nom] = dic

	return agenda

def mostrar(agenda):
	'''
	agenda {'Nico':{'telefono':3355878, 'mail':n@g.com}, 'Dany':{'telefono':3624587896, 'mail':dany@g.com} }

	.items() me lo transforma en una lista:
	[ ('Nico' , {'telefono':3355878, 'mail':n@g.com}) , ('Dany', {'telefono':3624587896, 'mail':dany@g.com} ) ]

	en la primera iteracion el for se para en el primer valor de la lista
	('Nico' , {'telefono':3355878, 'mail':n@g.com})---> esto siempre tiene 2 valores
	k ---> el primer valor ---> 'Nico'
	v ---> el segundo valor --->>{'telefono':3355878, 'mail':n@g.com}
	
	EN EL FOR INTERNO
	v -->{'telefono':3355878, 'mail':n@g.com}
	v.items() --->  [ ('telefono',3355878) , ('mail',n@g.com) ]
	la primera vez
	c ---> 'telefono'
	d ---> 3355878
	la segunda vez
	c ---> 'mail'
	d ---> 3n@g.com
	'''
	print("------AGENDA--------")
	for k,v in agenda.items():
		print(f"Contacto {k}: ")
		for c,d in v.items():
			print(f"\t {c}---->{d}")
	print("------FIN AGENDA--------")

def buscar(agenda):
	#funcion que muestra el telefono de un nombre buscado
	buscado = input("A quien quiere buscar?:\t")

	#agenda {'Nico':{'telefono':3355878, 'mail':n@g.com}, 'Dany':{'telefono':3624587896, 'mail':dany@g.com} }
	# CUANDO ACCEDO A 
	# agenda[buscado] ---> agenda['Nico'] ---> {'telefono':3355878, 'mail':n@g.com}
	# agenda[buscado]['telefono']-->agenda['Nico']['telefono'] ---> {'telefono':3355878, 'mail':n@g.com}['telefono'] ---->3355878
	if buscado in agenda.keys():
		print(f"el telefono de {buscado} es: {agenda[buscado]['telefono']}")
	else:
		print("El contacto buscado no existe.")
			

#-----PROGRAMA--------
agenda = dict()

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

