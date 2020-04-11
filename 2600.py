N = int(input())
for i in range(N):
	classic = True
	array = []
	topo = int(input())
	meio = input().split()
	for j in range(4):
		meio[j] = int(meio[j])
	baixo = int(input())

	array.append(topo)
	for j in range(4):
		array.append(meio[j])
	array.append(baixo)

	if (array[0] + array[5] != 7) or (array[2] + array[4] != 7) or (array[1] + array[3] != 7):
		classic = False
	
	for j in range(6):
		parameter = array[j]
		if parameter <= 0:
			classic = False
		for p in range(6):
			if (parameter == array[p] and j != p):
				classic = False
	
	if classic == True:
		print("SIM")
	else:
		print("NAO")