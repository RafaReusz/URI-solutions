somador = 0
while True:
	N = int(input())
	if N > 0:
		if somador > 0:
			print()
		array = []
		for _ in range(N):
			string = str(input())
			array.append(string)
		parameter = ""
		for i in range(N):
			if len(array[i]) > len(parameter):
				parameter = array[i]
		for p in range(N):
			for x in range(len(parameter) - len(array[p])):
				print(" ",end="")
			print(array[p])
		somador += 1

	else:
		break
