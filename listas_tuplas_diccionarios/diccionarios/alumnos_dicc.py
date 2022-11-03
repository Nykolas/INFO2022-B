'''
Un programa que me permita cargar los datos de los alumnos del info nombre, localidad y dni
Me permita agregar  la nota de los exámenes, teniendo en cuenta que hay dos módulos y 3 notas para cada uno.
Debe tener un menú interactivo que permita:
	Mostrar el alumno con mayor promedio
	Mostrar todos los que aprobaron ambos módulos
	Dado el DNI de un alumno, me muestre sus notas.

'''

'''

ALUMNOS ={

209998882:{'nombre':'nicolas','localidad':'Resistencia','notasPW':[7,6,3], 'notasBD':[6,8,2]},
801223132:{'nombre':'Maria','localidad':'Barranqueras','notasPW':[2,10,2], 'notasBD':[5,9,1]}

}

'''

import os

def menu():
	print("1: Cargar un ALumno")
	print("2: Cargar una nota")
	print("3: listar alumnos")
	print("4: listar notas de un alumno")
	print("5: Mostrar alumno con mayor promedio")
	print("6: Mostrar los que aprobaron ambos modulo")
	print("0: SALIR")
	return input()

def CargarAlumno(alumnos):
	dni = input("Ingrese el dni\t")
	if dni in alumnos.keys():
		print("YA EXISTE ESE ALUMNO")
	else:
		nombre = input("Ingrese el nombre\t")
		localidad = input("Ingrese localidad\t")
		alu = dict()
		alu['nombre'] = nombre
		alu['localidad'] = localidad
		alu['notasPW'] = list()
		alu['notasBD'] = list()
		alumnos[dni] = alu
	return alumnos

def CargarNota(alumnos):
	dni = input("Ingrese el dni\t")
	if dni in alumnos.keys():
		alu = alumnos[dni]
		print("VAMOS A CARGAR LAS NOTAS DE PW")
		n1 = int(input("Ingrese la nota 1\t"))
		n2 = int(input("Ingrese la nota 2\t"))
		n3 = int(input("Ingrese la nota 3\t"))
		alu['notasPW'] = [n1,n2,n3]
		print("VAMOS A CARGAR LAS NOTAS DE BD")
		n1 = int(input("Ingrese la nota 1\t"))
		n2 = int(input("Ingrese la nota 2\t"))
		n3 = int(input("Ingrese la nota 3\t"))
		alu['notasBD'] = [n1,n2,n3]
	else:
		print("EL DNI INGRESADO NO ES VALIDO")

	return alumnos

def Listar(alumnos):
	for k,v in alumnos.items():
		print(f"nombre: {v['nombre'].upper()} --- dni: {k} --- notas BD {v['notasBD']} ---- notasPW {v['notasPW']}")
	
def MostrarNotasAlumno(alumnos):
	dni = input("Ingrese el dni\t")
	if dni in alumnos.keys():
		alu = alumnos[dni]
		notasPW = alu['notasPW']
		notasBD = alu['notasBD']
		print(f"EL ALUMNO {alu['nombre'].upper()} cuenta con las siguientes notas")
		print("EN PROGRAMACION WEB")
		for n in notasPW:
			print(n, end = " -- ")
		print()
		print("EN BASE DE DATOS")
		for n in notasBD:
			print(n, end = " -- ")
		print()
	else:
		print("EL DNI INGRESADO NO ES VALIDO")
def MayorPromedio(alumnos):
	mayor = 0
	for dni,datos in alumnos.items():
		promedioBD = sum(datos['notasBD'])/len(datos['notasBD'])
		promedioPW = sum(datos['notasPW'])/len(datos['notasPW'])
		total = (promedioPW + promedioBD) / 2
		if total > mayor:
			mayor = total
			alumnoMayor = datos
	print(f"EL ALUMNO CON MAYOR PROMEDIO ES: {alumnoMayor['nombre']}, y su promedio fue de : {mayor}")

def MostrarAprobados():
	pass

def Main():
	alumnos = dict()
	while True:
		op = menu()
		if op == '1':
			alumnos = CargarAlumno(alumnos)
		elif op == '2':
			alumnos = CargarNota(alumnos)
		elif op == '3':
			Listar(alumnos)
		elif op == '4':
			MostrarNotasAlumno(alumnos)
		elif op == '5':
			MayorPromedio(alumnos)
		elif op == '6':
			MostrarAprobados(alumnos)
		else:
			break
		input('----CONTINUAR----')

		os.system('cls') #LIMPIA LA PANTALLA
Main()