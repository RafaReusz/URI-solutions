T = int(input())
for i in range(T):
	N = str(input())
	factorialParameter = 0
	numberParameter = ""
	for j in range(len(N)):
		if N[j] == "!":
			factorialParameter += 1
		elif N[j].isnumeric() == True:
			numberParameter += N[j]
	finalProduct = 1
	numberParameter = int(numberParameter)
	while numberParameter > 1:
		finalProduct *= numberParameter
		numberParameter -= factorialParameter
	print(finalProduct)