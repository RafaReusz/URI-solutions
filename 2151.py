# -*- coding: utf-8 -*-
A = int(input())
for x in range(0, A):
    L, C, I, J = input().split()
    L = int(L)
    C = int(C)
    I = int(I)
    J = int(J)
    X = I - 1
    Y = J - 1
    mat = [None] * L
    for i in range(0, L):
        mat[i] = input().split()
        for j in range(0, C):
            mat[i][j] = int(mat[i][j])
    for i in range(0, L):
        for j in range(0, C):
            DISX = abs(X - i)
            DISC = abs(Y - j)
            if DISX >= 9 or DISC >= 9:
                mat[i][j] += 1
            elif DISX < 9 and DISC < 9:
                if DISX > DISC:
                    mat[i][j] += 10 - DISX
                elif DISC > DISX:
                    mat[i][j] += 10 - DISC
                else:
                    mat[i][j] += 10 - DISX
    print("Parede %d:" % (x + 1))
    for i in range(0, L):
        for j in range(0, C - 1):
            print(mat[i][j], end=" ")
        print(mat[i][C - 1])