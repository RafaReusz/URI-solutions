# -*- coding: utf-8 -*-
import math
def primo(x):
	isprime = True
	for i in range(2, int(x ** 0.5) + 1):
		if x % i == 0:
			isprime = False
			break
	if isprime == True:
		return "Prime"
	else:
		return "Not Prime"
A = int(input())
for x in range(0, A):
	NB = int(input())
	print(primo(NB))
