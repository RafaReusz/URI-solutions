# -*- coding: utf-8 -*-
while True:
	h,p,f = input().split()
	h = int(h)
	p = int(p)
	f = int(f)
	if h != 0 and p != 0 and f != 0:
		mat = [None] * h
		for i in range(0, h):
			mat[i] = input().split()
			for j in range(0, p):
				mat[i][j] = int(mat[i][j])
		linha = input().split()
		vetor = []
		for l in range(0, len(linha)):
			linha[l] = int(linha[l])
			vetor.append(linha[l])
		SUM = 0
		for i in range(0, h):
			for j in range(0, p):
				if mat[i][j] == 0:
					SUM += 1
		while SUM < len(vetor):
			vetor.pop()
		vetor2 = []
		for l in range(len(vetor) -1 ,-1,-1):
			vetor2.append(vetor[l])
		for j in range(p - 1,-1,-1):
			for i in range(h - 1,-1,-1):
				if mat[i][j] == 0:
					if len(vetor2) != 0:
						mat[i][j] = vetor2[len(vetor2) - 1]
						vetor2.pop()
		for i in range(0, h):
			for j in range(0, p - 1):
				print(mat[i][j],end=" ")
			for j in range(p - 1, p):
				print(mat[i][j])
	else:
		break
