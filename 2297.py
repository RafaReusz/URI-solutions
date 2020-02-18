# -*- coding: utf-8 -*-
TT = 0
while True:
	
	CA = 0
	CB = 0
	R = int(input())
	TT += 1
	for x in range(0, R):
		A, B = input().split()
		A = int(A)
		B = int(B)
		CA += A
		CB += B
		
	if CA > CB:
		print('Teste %d' % (TT))
		print('Aldo\n')
	elif CB > CA:
		print('Teste %d' % (TT))
		print('Beto\n')
	elif R == 0:
		break