array_pessoas = []
n = int(input())
input_pessoas = input().split()
for i in range(n):
	array_pessoas.append(input_pessoas[i])

m = int(input())
input_pessoas_sairam = input().split()
for i in range(m):
	array_pessoas.remove(input_pessoas_sairam[i])

for i in range(n - m):
	if i != n - m - 1:
		print(array_pessoas[i], end=" ")
	else:
		print(array_pessoas[i])
