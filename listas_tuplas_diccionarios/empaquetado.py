
def resta(a,b):

	r = a - b
	if r < 0:
		return True,r  # (True,r)
	else:
		return False,r


negativo,valor = resta(10,5)

print(f"El resultado fue {valor}, y es negativo {negativo}")