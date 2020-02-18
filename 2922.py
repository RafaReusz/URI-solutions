while True:
	try:
		A, B = input().split()
		A = int(A)
		B = int(B)
		TOTALSALAS = abs(A - B) - 1
		if TOTALSALAS > 0:
			print("%d" %(TOTALSALAS))
		else:
			print(0)
	except EOFError:
		break
