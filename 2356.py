while True:
	try:
		D = str(input())
		S = str(input())
		Resistente = False
		for i in range(len(D)):
			if D[i] == S[0] and len(D) - i >= len(S):
				PARAMETER = True
				for j in range(len(S)):
					if D[i + j] != S[j]:
						PARAMETER = False
				if PARAMETER == True:
					Resistente = True
		if Resistente == True:
			print("Resistente")
		else:
			print("Nao resistente")
	except EOFError:
		break