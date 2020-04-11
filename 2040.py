while True:
	N = int(input())
	if N != 0:
		array_times = []
		array_pontos = []
		for i in range(N):
			time, pontuacao = input().split()
			time = str(time)
			pontuacao = int(pontuacao)
			array_times.append(time)
			array_pontos.append(pontuacao)

		for i in range(int(N / 2)):
			frase = str(input())
			time1 = ""
			time2 = ""
			gols1 = ""
			gols2 = ""


			parameter = 0

			while frase[parameter].isalpha() and frase[parameter] != " ":
				time1 += frase[parameter]
				parameter += 1
			
			parameter += 1

			
			while frase[parameter].isdigit():
				gols1 += frase[parameter]
				parameter += 1

			parameter += 1


			while frase[parameter].isdigit():
				gols2 += frase[parameter]
				parameter += 1
			
			parameter += 1

			while frase[parameter].isalpha() and parameter != len(frase) - 1:
				time2 += frase[parameter]
				parameter += 1
			time2 += frase[len(frase) - 1]

			
			index_time1 = array_times.index(time1)
			index_time2 = array_times.index(time2)
			
			gols1 = int(gols1)
			gols2 = int(gols2)

			array_pontos[index_time1] += 3 * gols1
			array_pontos[index_time2] += 3 * gols2

			if gols1 > gols2:
				array_pontos[index_time1] += 5
			
			elif gols1 < gols2:
				array_pontos[index_time2] += 5
			
			else:
				array_pontos[index_time1] += 1
				array_pontos[index_time2] += 1
	
		index_sport = array_times.index("Sport")
		index_max = array_pontos.index(max(array_pontos))
		if max(array_pontos) == array_pontos[index_sport]:
			print("O Sport foi o campeao com %d pontos :D" % (max(array_pontos)))
		else:
			print("O Sport nao foi o campeao. O time campeao foi o %s com %d pontos :(" % (array_times[index_max] ,max(array_pontos)))
		
		print()
	else:
		break