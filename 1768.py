while True:
	try:
		N = int(input())
		parameter = 1
		espacos = int(N / 2)
		espacos_vazios = espacos
		while parameter <= N:
			for i in range(espacos_vazios):
				print(" ",end="")
			for j in range(parameter):
				print("*",end="")
			parameter += 2
			espacos_vazios -= 1
			print()

		parameter = 1
		espacos = int(N / 2)
		espacos_vazios = espacos
		while parameter <= 3:
			for i in range(espacos_vazios):
				print(" ",end="")
			for j in range(parameter):
				print("*", end="")
			parameter += 2
			espacos_vazios -= 1
			print()
		print()
	except EOFError:
		break