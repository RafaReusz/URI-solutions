# -*- coding: utf-8 -*-
import math
while True:
    try:
        A, B, C = input().split()
        A = int(A)
        B = int(B)
        C = int(C)
        P = (A + B + C) / 2
        AREATRI = (P * (P - A) * (P - B) * (P - C)) ** 0.5
        RAD1 = AREATRI / P
        AREA1 = math.pi * (RAD1 ** 2)
        AREA2 = AREATRI - AREA1
        RAD2 = (A * B * C) / (4 * AREATRI)
        TOPAREA = (math.pi * (RAD2 ** 2)) - AREATRI
        print("%.4f %.4f %.4f" % (TOPAREA, AREA2, AREA1))
    except EOFError:
        break