C = int(input())	
for i in range(C):
	entrada = input().split()
	pessoas = int(entrada[0])
	notas = []
	entrada.pop(0)
	for j in range(pessoas):
		notas.append(int(entrada[j]))
	SOMATOTAL = sum(notas)
	MEDIA = SOMATOTAL / pessoas
	pessoasAcimaMedia = 0
	for x in range(pessoas):
		if notas[x] > MEDIA:
			pessoasAcimaMedia += 1
	porcentagemPessoasAcimaMedia = 100 * (pessoasAcimaMedia / pessoas)
	print("%.3f" % (porcentagemPessoasAcimaMedia), end="")
	print("%")