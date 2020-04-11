N = int(input())
lowestPrice = None
for i in range(N):
	P, G = input().split()
	P = float(P)
	G = int(G)
	if i == 0:
		lowestPrice = P / G
	else:
		if P / G < lowestPrice:
			lowestPrice = P / G
print("%.2f" % (lowestPrice * 1000))