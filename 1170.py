import math
N = int(input())
for i in range(N):
	C = float(input())
	days = 0
	while C > 1:
		C /= 2
		days += 1
	print("%d dias" % (days))