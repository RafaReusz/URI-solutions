while True:
	try:
		PARAMETER = True
		STR = str(input())
		if len(STR) > 32 or len(STR) < 6:
			PARAMETER = False
		if PARAMETER == True:
			for i in range(0, len(STR)):
				if ord(STR[i]) < 48 or (ord(STR[i]) > 57 and ord(STR[i]) < 65) or (ord(STR[i]) > 90 and ord(STR[i]) < 97) or ord(STR[i]) > 122:
					PARAMETER = False
		if PARAMETER == True:
			PARAMETERNUMBERS = []
			PARAMETERTINY = []
			PARAMETERCAPITAL = []
			for i in range(0, len(STR)):
				if (ord(STR[i]) > 47 and ord(STR[i]) < 58):
					PARAMETERNUMBERS.append(STR[i])
				if (ord(STR[i]) > 64 and ord(STR[i]) < 91):
					PARAMETERTINY.append(STR[i])
				if (ord(STR[i]) > 96 and ord(STR[i]) < 123):
					PARAMETERCAPITAL.append(STR[i])
			if len(PARAMETERNUMBERS) == 0 or len(PARAMETERTINY) == 0 or len(PARAMETERCAPITAL) == 0:
				PARAMETER = False
		if PARAMETER == True:
			print("Senha valida.")
		else:
			print("Senha invalida.")
	except EOFError:
		break
