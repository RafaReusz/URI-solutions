# -*- coding: utf-8 -*-
while True:
	A = int(input())
	if A != 0:
		cx,cy,r1,r2	= input().split()
		cx = int(cx)
		cy = int(cy)
		r1 = int(r1)
		r2 = int(r2)
		dentrochiquinha = 0
		bordachiquinha = 0
		dentropopis = 0
		bordapopis = 0
		for x in range(0, A):
			chiquinhax, chiquinhay = input().split()
			chiquinhax = int(chiquinhax)
			chiquinhay = int(chiquinhay)
			popisx, popisy = input().split()
			popisx = int(popisx)
			popisy = int(popisy)
			DISCHIQUINHA = ((((cx - chiquinhax) ** 2)) + ((cy - chiquinhay) ** 2)) ** 0.5
			DISPOPIS = ((((cx - popisx) ** 2)) + ((cy - popisy) ** 2)) ** 0.5
			if DISCHIQUINHA < r1:
				dentrochiquinha += 1
			if DISCHIQUINHA <= r2:
				bordachiquinha += 1
			if DISPOPIS < r1:
				dentropopis += 1
			if DISPOPIS <= r2:
				bordapopis += 1
		if dentrochiquinha > dentropopis:
			print("C > P")
		elif dentropopis > dentrochiquinha:
			print("P > C")
		elif dentropopis == dentrochiquinha:
			if bordachiquinha > bordapopis:
				print("C > P")
			elif bordapopis > bordachiquinha:
				print("P > C")
			else:
				print("C = P")

	else:
		break