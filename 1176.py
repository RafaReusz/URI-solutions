def Fibonacci(x):
	array = [0,1]
	if x == 0:
		return 0
	elif x == 1:
		return 1
	else:
		while len(array) - 1 != x:
			array.append(array[-1] + array[-2])
		return array[-1]

T = int(input())
for i in range(T):
	N = int(input())
	print("Fib(%d) = %d" % (N, Fibonacci(N)))