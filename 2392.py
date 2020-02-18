# -*- coding: utf-8 -*-
A, B = input().split()
A = int(A)
B = int(B)
vd = []
vpo = []
vpfinais = []
for y in range(0, A):
    vpfinais.append(0)
for x in range(0, B):
    Po, D = input().split()
    Po = int(Po)
    D = int(D)
    vd.append(D)
    vpo.append(Po - 1)
for s in range(0, B):
    for i in range(0, A):
        DIVISIVEL = abs(i - vpo[s])
        if DIVISIVEL % vd[s] == 0:
            vpfinais[i] = 1
for l in range(0, A):
    print(vpfinais[l])
