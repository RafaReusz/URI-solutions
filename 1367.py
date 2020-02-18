while True:
	N = int(input())
	if N != 0:
		S = 0
		P = 0
		arrayLetra = []
		arrayTempo = []
		arrayEstado = []
		for i in range(N):
			Letra, Tempo, Estado = input().split()
			Letra = str(Letra)
			Tempo = int(Tempo)
			Estado = str(Estado)
			arrayLetra.append(Letra)
			arrayTempo.append(Tempo)
			arrayEstado.append(Estado)
		arrayCorretas = []
		arrayTempoCorretas = []
		for i in range(N):
			if arrayEstado[i] == "correct":
				arrayCorretas.append(arrayLetra[i])
				arrayTempoCorretas.append(arrayTempo[i])
		for i in range(N):
			if arrayEstado[i] == "incorrect" and arrayLetra[i] in arrayCorretas:
				P += 20
		S += len(arrayCorretas)
		P += sum(arrayTempoCorretas)
		print("%d %d" % (S, P))
	else:
		break