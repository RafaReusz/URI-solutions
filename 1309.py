while True:
	try:
		dolares = str(input())
		centavos = str(input())
		print("$",end="")
		arraydolares = []
		for i in range(len(dolares)):
			arraydolares.append(dolares[i])
		arraydolares.reverse()
		parameterVirgulas = len(arraydolares) - 1
		while parameterVirgulas >= 0:
			print(arraydolares[parameterVirgulas],end="")
			if (parameterVirgulas) % 3 == 0 and parameterVirgulas != 0:
				print(",",end="")
			parameterVirgulas -= 1

		if int(centavos) >= 10:
			print(".%s" % (centavos))
		else:
			print(".0%s" % (centavos))
	except EOFError:
		break