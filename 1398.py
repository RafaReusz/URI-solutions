# -*- coding: utf-8 -*-
while True:
    try:
        numero = []
        while "#" not in numero:
            A = str(input())
            for x in A:
                numero.append(x)
        numero.remove("#")
        C = int("".join(numero), 2)
        if C % 131071 == 0:
            print("YES")
        else:
            print("NO")
    except EOFError:
        break