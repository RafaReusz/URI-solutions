# -*- coding: utf-8 -*-
def fib_to(n):
	fib3 = []
	fibs = [0, 1]
	if len(fib3) < n:
		while True:
			if len(fib3) < n:
				FIBP = fibs[len(fibs) - 1] + fibs[len(fibs) - 2]
				fibs.append(FIBP)
				if FIBP % 3 == 0:
					fib3.append(FIBP)
				else:
					FRASE = str(FIBP)
					for i in range(0, len(FRASE)):
						if FRASE[i] == "3":
							fib3.append(FIBP)
							break
			else:
				break
	return fib3[n - 1]
while True:
	try:
		A = int(input())
		print(fib_to(A))
	except EOFError:
		break
