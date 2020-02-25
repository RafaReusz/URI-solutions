import math
while True:
	N = str(input())
	if N != "0":
		array = []
		for i in range(len(N)):
			array.append(int(N[i]))
		array.reverse()
		SOMA = 0
		for j in range(len(N)):
			SOMA += (array[j] * math.factorial(j + 1))
		print("%d" % (SOMA))
	else:
		break
