t = int(input())
for i in range(t):
	total, n = input().split()
	total = int(total)
	n = int(n)
	array_produtos = []
	string_produtos = input().split()
	for j in range(n):
		array_produtos.append(float(string_produtos[j]))
	
	maior_preco = 0
	for j in range(n):
		qtde = int(total / array_produtos[j])
		if (total - (qtde * array_produtos[j]) > maior_preco) and qtde != 0:
			maior_preco = total - (qtde * array_produtos[j])

	print("%.2f" % (maior_preco))