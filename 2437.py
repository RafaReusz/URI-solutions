A, B, C, D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)
DISX = abs(A - C)
DISY = abs(B - D)
print("%d" % (DISX + DISY))