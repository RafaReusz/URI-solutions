T = int(input())
for _ in range(T):
	N = int(input())
	arrayNames = input().split()
	arrayPresenca = input().split()
	arrayReprovados = []
	for i in range(len(arrayPresenca)):
		presencas = 0
		total = 0
		for j in range(len(arrayPresenca[i])):
			if arrayPresenca[i][j] == "P":
				presencas += 1
				total += 1
			elif arrayPresenca[i][j] == "A":
				total += 1
		if presencas / total < 0.75:
			arrayReprovados.append(arrayNames[i])
	if len(arrayReprovados) > 0:
		for w in range(len(arrayReprovados)):
			if w != len(arrayReprovados) - 1:
				print(arrayReprovados[w], end=" ")
			else:
				print(arrayReprovados[w], end="")
	print()
						