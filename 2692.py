N, M = input().split()
N = int(N)
M = int(M)
array_Wrong = []
array_Correct = []

for _ in range(N):
	wrong, correct = input().split()
	wrong = str(wrong)
	correct = str(correct)
	array_Wrong.append(wrong)
	array_Correct.append(correct)


for x in range(M):
	phrase_wrong = str(input())
	phrase_correct = ""
	for y in range(len(phrase_wrong)):
		if phrase_wrong[y] in array_Wrong:
			parameter = array_Wrong.index(phrase_wrong[y])
			phrase_correct += array_Correct[parameter]
		elif phrase_wrong[y] in array_Correct:
			parameter = array_Correct.index(phrase_wrong[y])
			phrase_correct += array_Wrong[parameter]
		else:
			phrase_correct += phrase_wrong[y]
	print(phrase_correct)