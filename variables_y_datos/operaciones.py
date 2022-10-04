# OPERADORES MATEMATICOS  + / - *
print("OPERADORES MATEMATICOS")
n1 = 5
n2 = 7
print(n1 * n2)


# OPERADORES LOGICOS  and or not  (actuan con valores logicos y retornan un valor logico)
print("OPERADORES LOGICOS")
v1 = True
v2 = False
v3 = True

print(v1 and v2) #False 
print(v1 or v2) #True
print(v1 and v3) #True
print(not v1) #False
print(v1 and v3 or v2) #True

# OPERADORES RELACIONALES > ; < ; = ; >= ; <= ; !=  (actuan sobre cualquier tipo de datos ordinal, retornan un valor logico)
print("OPERADORES RELACIONALES")
n1 = 10
n2 = 15

print(n1 > n2) #False
print(n1 != n2) #True

s1 = "nico"
s2 = "carlos"
print(s1 > s2) #True

print("--------------------------------")

print( (n1 < n2) and (s1 > s2) ) #True