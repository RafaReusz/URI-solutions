import math
while True:
	T = int(input())
	if T != 0:
		NGB = T / 90
		NGA = (7 * T) / 90
		print("Brasil %d x Alemanha %d" % (math.floor(NGB),math.ceil(NGA)))
	else:
		break
