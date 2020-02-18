while True:
	try:
		C = float(input())
		i = float(input())
		n = int(input())
		FINALCOMPOSTO = C * (1 + i) ** n
		FINALSIMPLES = C + (C * i * n)
		print("DIFERENCA DE VALOR = %.2f" % (FINALCOMPOSTO - FINALSIMPLES))
		print("JUROS SIMPLES = %.2f" % (FINALSIMPLES -  C))
		print("JUROS COMPOSTO = %.2f" % (FINALCOMPOSTO - C))
	except EOFError:
		break