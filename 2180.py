N = int(input())
array = []
i = N
while len(array) < 10:
	arrayFatoresPrimos = []
	for j in range(1, int(i ** 0.5) + 1):
		if i % j == 0:
			arrayFatoresPrimos.append(j)
	if len(arrayFatoresPrimos) == 1:
		array.append(i)
	i += 1

distanciaMarte = 60000000
tempoHoras = distanciaMarte / sum(array)
tempoDias = tempoHoras / 24
print("%d km/h" % (sum(array)))
print("%d h / %d d" % (tempoHoras, tempoDias))
