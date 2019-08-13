# -*- coding: utf-8 -*-
import math
while True:
    try:
        A, B = input().split()
        A = int(A)
        B = int(B)
        C = math.factorial(A) + math.factorial(B)
        print(C)
    except EOFError:
        break
