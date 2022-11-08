"""Realizar una clase que administre una agenda. Se debe almacenar 
para cada contacto el nombre, el teléfono y el email. Además deberá
mostrar un menú con las siguientes opciones.
Añadir contacto
Lista de contactos
Buscar contacto
Editar contacto
Cerrar agenda
"""
from os import system

class Contacto():
    
    def __init__(self, nombre, telefono, email):

        self.nombre = nombre
        self.telefono = telefono
        self.email = email
    
    def __str__(self):

        return f"Nombre: {self.nombre} \n" \
            f"Telefono: {self.telefono} \n" \
            f"Email: {self.email} \n"

    def mov_nombre(self, nombre):

        self.nombre = nombre
    
    def mov_telefono(self, telefono):

        self.telefono = telefono
    
    def mov_email(self, email):

        self.email = email
    
class Agenda():
    contactos = []

    #busca por el nombre y devuelve verdadero
    def existe(self, nom):
        
        for i in (self.contactos):

            if nom == i.nombre:

                return True

        return False

    #aniadir un contacto
    def aniadir(self):

        print("Añadir un contacto\n" \
            "----------------------------")
        bandera = True
        while bandera:
            
            #Comprobamos que el nombre de no exista ya que no puede haber 2 iguales
            nombre = input("Ingrese el nombre: ")
            bandera = self.existe(nombre)

            if bandera:
                
                print("El contacto ya existe")
                x = int(input("Desea intentar denuevo ingrese '1', de lo contrario precione enter '2': "))
                if x == 2:
                    break            
                continue

            telefono = input("Ingrese el telefono: ")
            email = input("Ingrese el email: ")
            aux = Contacto(nombre, telefono, email)
            self.contactos.append(aux)
            input("--------------------------------\n" \
                "Contacto Guardado con exito precione [enter] ")
        
    #recorre la lista y llama al metodo __str__ de contacto
    def listar(self):

        print("Lista de contacto")
        for i in (self.contactos):

            print("---------------------")
            print(i.__str__())
        
        input("--------------------------------\n" \
            "Para volver al Menu principal precione [enter] ")

    #busca y devuelve un objeto del tipo contacto
    def buscar(self, nom):
        
        for i in (self.contactos):

            if nom == i.nombre:

                return i.__str__() 

        print("No existe el contacto")

    #busca y devuelve el lugar y si es existe con un valor verdadero
    def buscar_lugar(self, nom):
        
        for i in range(len(self.contactos)):

            if nom == self.contactos[i].nombre:

                return i, True       

        return None, False

    #Busca si existe el contacto y lugo te deja editar 
    def editar(self, nom):
        #buscamos el contacto a edita
        index, existe = self.buscar_lugar(nom)
        if existe:

            #comenzamos la edicion 
            print(self.contactos[index].__str__())
            bandera = (input("Desea cambiar el nombre ingrese 'si':")).lower()
            if bandera == "si":
                #como sabemos no puede haber 2 contactos con el mismo nombre
                bandera2 = True
                while bandera2:

                    nombre = input("Ingrese el nombre: ")
                    bandera2 = self.existe(nombre)

                    if bandera2:
                
                        print("El contacto ya existe")
                        x = int(input("Desea intentar denuevo ingrese '1', de lo contrario precione enter '2': "))
                        if x == 2:
                            break            
                        continue

                self.contactos[index].mov_nombre(nombre)
                bandera = ""

            bandera = (input("Desea cambiar el telefono ingrese 'si':")).lower()
            if bandera == "si":

                telefono = input("Ingrese el telefono: ")
                self.contactos[index].mov_telefono(telefono)
                bandera = ""

            bandera = (input("Desea cambiar el email ingrese 'si':")).lower()
            if bandera == "si":

                email = input("Ingrese el email: ")
                self.contactos[index].mov_email(email)
                bandera = ""
            print("Cambios gusdados con exito")
        else:

            print("no existe el contacto")
        

#program
agenga = Agenda()
while True:

    system("clear")
    print("Menu de la agenda\n")
    x = int(input("1-Añadir contacto \n" \
        "2-Lista de contactos \n" \
        "3-Buscar contacto \n" \
        "4-Editar contacto \n" \
        "5-Cerrar agenda \n--> "))

    system("clear")   
    if x == 1:

        agenga.aniadir()

    elif x == 2:

        agenga.listar()

    elif x == 3:

        print("Busqueda\n"\
            "-------------------")
            
        aux = input("Ingrese nombre desea busqueda: ")
        print(agenga.buscar(aux))
        input("--------------------------------\n" \
            "Para volver al Menu principal precione [enter] ")

    elif x == 4:

        print("Editar Contacto\n"\
            "-------------------")

        aux = input("Ingrese nombre desea editar: ")
        agenga.editar(aux)
        input("--------------------------------\n" \
            "Para volver al Menu principal precione [enter] ")

    elif x == 5:

        break

    else:
        
        print("Error. El valor ingresado no tiene una funcion definida")