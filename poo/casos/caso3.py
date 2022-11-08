"""Desarrollar un programa que cargue los datos de un triángulo.

Implementar una clase con los métodos para inicializar los atributos
, imprimir el valor del lado con un tamaño mayor y el tipo de triángulo
que es (equilátero, isósceles o escaleno)."""

class Triangulo():
    def __init__(self, lado_1, lado_2,lado_3):
        self.lado_1 = lado_1
        self.lado_2 = lado_2
        self.lado_3 = lado_3
    
    def mayor(self):
        lista_lados = [self.lado_1, self.lado_2, self.lado_3]
        lista_lados.sort()
        return lista_lados[2]
        
    
    def tipo(self):
        if self.lado_1==self.lado_2==self.lado_3:
            return "equilátero"
        elif self.lado_1!=self.lado_2!=self.lado_3:
            return "escaleno"
        else:
            return "isósceles"


l1 = float(input(f"Ingrese el valor del del lado 1 del triangulo: "))
l2 = float(input(f"Ingrese el valor del del lado 2 del triangulo: "))
l3 = float(input(f"Ingrese el valor del del lado 3 del triangulo: "))  

triangulo = Triangulo(l1,l2,l3)
print(triangulo.mayor())
print(triangulo.tipo())