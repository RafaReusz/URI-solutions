instancia = 1
while True:
	assinatura = str(input())
	if assinatura != "0":
		if instancia > 1:
			print()
		obra = str(input())
		print("Instancia %d" % (instancia))
		if assinatura in obra:
			print("verdadeira")
		else:
			print("falsa")

		instancia += 1

	else:
		break