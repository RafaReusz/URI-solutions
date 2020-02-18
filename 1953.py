# -*- coding: utf-8 -*-
while True:
	try:		
		A = int(input())
		vp = []
		vc = []
		for x in range(0, A):
			B, C = input().split()
			B = int(B)
			C = str(C)
			vp.append(C)
			vc.append(B)
		TOTAL = 0
		EHD = 0
		EPR = 0
		for i in range(0, A):
			if vp[i] == "EPR":
				EPR += 1
			elif vp[i] == "EHD":
				EHD += 1
			else:
				TOTAL += 1
		print("EPR: %d" % (EPR))
		print("EHD: %d" % (EHD))
		print("INTRUSOS: %d" % (TOTAL))
	except EOFError:
		break
