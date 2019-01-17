t = int(input())

global d
d ={}

def factorial(n):
	if n==0:
		return 1
	else:
		if n in d:
			return d[n]
		else:
			d[n] = n * factorial(n-1)
			return d[n]


for i in range(t):
	n = int(input())
	print(factorial(n))