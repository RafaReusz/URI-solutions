# -*- coding: utf-8 -*-
A = int(input())
for x in range(0, A):
	B, C = input().split()
	B = int(B)
	C = int(C)
	for y in range(0, C):
		TOTAL = 0
		MAIOR = 0
		PS = input().split()
		for i in range(0, B):
			PS[i] = float(PS[i])
		for i in range(0, B):
			TOTAL += PS[i]
		for i in range(0, B):
			if PS[i] > MAIOR:
				MAIOR = PS[i]
		MEDIA = TOTAL / B
		if MEDIA >= 7:
			print("%.2f" % (MAIOR))
		if MEDIA < 4:
			print("%.2f" % (MEDIA))
		if 4 <= MEDIA < 7:
			NOTA = 0
			for i in range(0,B):
				if PS[i] > MEDIA and PS[i] < 7 and PS[i] > NOTA:
					NOTA = PS[i]
			if NOTA > MEDIA:
				print("%.2f" % (NOTA))
			else:
				print("%.2f" % (MEDIA))