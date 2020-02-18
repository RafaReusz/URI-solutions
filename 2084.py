# -*- coding: utf-8 -*-
A = int(input())
B = input().split()
vetor = []
PARAMETER = False
for x in range(0, A):
    B[x] = int(B[x])
    vetor.append(B[x])
VOTOS = sum(vetor)
C1 = max(vetor)
if C1 / VOTOS >= 0.45:
    PARAMETER = True
vetor.remove(C1)
C2 = max(vetor)
if (C2 / VOTOS) + 0.1 <= C1 / VOTOS:
    PARAMETER = True

if PARAMETER == True:
    print("1")
else:
    print("2")