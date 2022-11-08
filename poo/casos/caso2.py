from os import system


class Vehiculo:
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas
    
    def mostrar(self):
        # self.__class__.__name__ es el nombre de la clase del objeto.
        return f'Clase "{self.__class__.__name__}"\n'\
                f'Color {self.color}\n'\
                f'Ruedas {self.ruedas}\n'
    
class Coche(Vehiculo):
    def __init__(self, velocidad,cilindrada,color, ruedas):
        super().__init__(color, ruedas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    
    def mostrar(self):
        return  super().mostrar()+\
                f'Velocidad maxima {self.velocidad} km/h\n'\
                f'Cilindrada {self.cilindrada} cc\n'\
    
class Camioneta(Coche):
    def __init__(self, carga, velocidad, cilindrada, color, ruedas):
        super().__init__(velocidad, cilindrada, color, ruedas)
        self.carga=carga
    
    def mostrar(self):
        return  super().mostrar()+\
                f'Carga maxima {self.carga} kg\n'

class Bicicleta(Vehiculo):
    def __init__(self, tipo,color, ruedas):
        super().__init__(color, ruedas)
        self.tipo=tipo
    
    def mostrar(self):
        return  super().mostrar()+\
                f'Tipo {self.tipo} \n'

class Motocicleta(Bicicleta):
    def __init__(self, velocidad, cilindrada, tipo, color, ruedas):
        super().__init__(tipo, color, ruedas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    
    def mostrar(self):
        return  super().mostrar()+\
                f'Velocidad maxima {self.velocidad} km/h\n'\
                f'Cilindrada {self.cilindrada} cc\n'\



def catalogar(lista):
    print("Lista de vehiculos\n")
    for i in lista:
        #NO TENGO NI IDEA DE QUE i
        print(i.mostrar())


coche1=Coche(250,500,'rojo',4)
camioneta1=Camioneta(5000,200,700,'azul',4)
bicicleta1=Bicicleta('deportiva','verde',2)
moto1=Motocicleta(250,500,'urbana','negra',2)


vehiculo=[coche1,camioneta1,bicicleta1,moto1]


catalogar(vehiculo)
