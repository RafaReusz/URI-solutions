# -*- coding: utf-8 -*-
while True:
    try:
        A, B = input().split()
        A = int(A)
        B = int(B)
        v = []
        for x in range(1, A + 1):
            v.append(x)
        C = input().split()
        for i in range(0, len(C)):
            C[i] = int(C[i])
        for i in range(0, len(C)):
            v.remove(C[i])
        if len(v) != 0:
            for w in range(0, len(v)):
                print(v[w], end=" ")
            print()
        else:
            print("*")
    except EOFError:
        break