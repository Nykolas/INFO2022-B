
class Estudiante:

	#PARA CREAR UN ESTUDIANTE
	def __init__(self,nom,dni,sexo):
		self.nombre = nom
		self.dni = dni
		self.sexo = sexo

	def get_sexo(self):
		return self.sexo

	def set_sexo(self,nuevo):
		self.sexo = nuevo

	def get_nombre(self):
		return self.nombre

	def set_nombre(self, nuevo):
		self.nombre = nuevo



#CARGO LISTA DE ESTUDIANTES
lista_estudiantes = list()
for x in range(3):
	n = input("nombre:\t")
	s = input("sexo:\t")
	d = input("dni:\t")
	lista_estudiantes.append(Estudiante(n,d,s))



#MUESTRO LOS NOMBRES DE LOS ESTUDIANTES
for x in lista_estudiantes:
	print(x.set_nombre('carlos'))




