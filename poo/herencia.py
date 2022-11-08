

class Vehiculo:

	def __init__(self, color, ruedas):
		self.color = color
		self.ruedas = ruedas

	def get_color(self):
		return self.color

	def get_ruedas(self):
		return self.ruedas

	def set_color(self, nuevo_color):
		self.color = nuevo_color

	def set_ruedas(self, nuevo_ruedas):
		self.ruedas = nuevo_ruedas


class Coche(Vehiculo):

	def __init__(self,color,ruedas,velo,cc):
		#SUPER ES EL PADRA
		super().__init__(color,ruedas)
		self.velocidad = velo
		self.cilindrada = cc

	def get_velocidad(self):
		return self.velocidad

	def get_cilindrada(self):
		return self.cilindrada

	def set_velocidad(self, nuevo_velocidad):
		self.velocidad = nuevo_velocidad

	def set_cilindrada(self, nuevo_cilindrada):
		self.cilindrada = nuevo_cilindrada

	def __str__(self):
		return f"COCHE: con cilindrada = {self.cilindrada}"

c1 = Coche('rojo',4,200,180)

print(c1)

