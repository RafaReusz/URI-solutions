# -*- coding: utf-8 -*-
A, B = input().split()
A = int(A)
B = int(B)
C = input().split()
vetor = []
for x in range(0, B):
	vetor.append(int(C[x]))
temp1 = vetor[0] - 1
temp3 = A - vetor[len(vetor) - 1]
temp2 = 0
W = 0
Q = 1
while Q < len(vetor):
	CALC = int((vetor[Q] - vetor[W]) / 2)
	if CALC > temp2:
		temp2 = CALC
	W += 1
	Q += 1


if temp1 >= temp2 and temp1 >= temp3:
	print(temp1)
elif temp2 > temp1 and temp2 >= temp3:
	print(temp2)
elif temp3 > temp1 and temp3 > temp2:
	print(temp3)