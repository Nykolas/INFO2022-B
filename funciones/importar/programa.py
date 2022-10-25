
import funciones #OP 1, importa todo el archivo

from funciones import saludar, mostrarme #OP2 importo solo la/s funciones que necesito

#PROGRAMA

n = input("Ingresa tu nombre: \t")

funciones.saludar() #OP 1 debo seleccionar de todo el archivo, que funcion quiero.

mostrarme(n)#OP 2, ejecuto directamente la funcion.


