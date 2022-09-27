#ENTRADA

#nombre = input("Ingrese un nombre:\t")
edad = input("Ingrese la edad:\t")
print(f"Usted se llama {nombre} y tiene {edad} años")
n1 = input("INGRESE UN NUMERO:\t")
print(f"La variable n1, contiene el valor: {n1} y es del tipo {type(n1)}")


n1 = 20 #EL NUMERO 20
print(f"La variable n1, contiene el valor: {n1} y es del tipo {type(n1)}")
n2 = '20' #LA PALABRA 20 #EN LAS PATENTES AG345
print(f"La variable n2, contiene el valor: {n2} y es del tipo {type(n2)}")


# CAMBIAR TIPO DE DATO
nuevo_n2 = int(n2) #-->> TRANSFORMAR AL '20' en el numero 20
print(f"La variable nuevo_n2, contiene el valor: {nuevo_n2} y es del tipo {type(nuevo_n2)}")

nuevo_n1 = str(n1) #-->> TRANSFORMAR AL '20' en el numero 20
print(f"La variable nuevo_n1, contiene el valor: {nuevo_n1} y es del tipo {type(nuevo_n1)}")

#OJO SOLO PUEDO PASAR A ENTEROS NUMEROS COMO STRING
casa = int('nico') #ESTO DA ERROR

