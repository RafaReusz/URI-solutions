# -*- coding: utf-8 -*-
A = str(input())
NUMEROA = int(A, 2)
B = int(input())
vetor = []
for x in range(0, B):
    C = int(input())
    if NUMEROA % C == 0:
        vetor.append(C)
vetor.sort()
if len(vetor) == 0:
    print("Nenhum")

else:
    for x in range(0, len(vetor) - 1):
        print("%d" % (vetor[x]), end=' ')
    for x in range(len(vetor) - 1, len(vetor)):
        print("%d" % (vetor[x]))
