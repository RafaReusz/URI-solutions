# -*- coding: utf-8 -*-
import math
A = int(input())
MAIOR = 0
POSICAO = 0
for x in range(0, A):
	B, C = input().split()
	B = int(B)
	C = int(C)
	TOTAL = C * math.log10(B)
	if TOTAL > MAIOR:
		MAIOR = TOTAL
		POSICAO = x
print(POSICAO)