N = int(input())
array = []
for i in range(N):
	nx = int(input())
	array.append(nx)
HIGHESTPOSITION = 0
HIGHESTVOTES = 0
for i in range(N):
	if array[i] > HIGHESTVOTES:
		HIGHESTPOSITION = i
		HIGHESTVOTES = array[i]
if HIGHESTPOSITION == 0:
	print("S")
else:
	print("N")
