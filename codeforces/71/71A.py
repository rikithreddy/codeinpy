from sys import stdin

n = int(stdin.readline())

for i in range(n):
	x = stdin.readline().strip()
	l = len(x)
	if l > 10:
		print( x[0] + str(l-2) + x[-1])
	else:
		print(x)
