import sys
for _ in range(int(sys.stdin.readline())):
	n,a,b,k = map(int, sys.stdin.readline().split())
	mul = a*b
	while b!=0:
		a,b = b, a%b
	sys.stdout.write('Win') if n - n// (mul//a)  >= k else sys.stdout.write('Lose')
