while True:
	N, D = input().split()
	N = int(N)
	D = int(D)
	if N == 0 and D == 0:
		break
	else:
		PARAMETER = False
		mat = [None] * D
		for i in range(D):
			mat[i] = input().split()
			for j in range(N):
				mat[i][j] = int(mat[i][j])
		arrayParticipacoes = []
		for j in range(N):
			arrayParticipacoes.append(0)
		for i in range(D):
			for j in range(N):
				if mat[i][j] == 1:
					arrayParticipacoes[j] += 1
		if D in arrayParticipacoes:
			print("yes")
		else:
			print("no")
