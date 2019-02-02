import sys
n,d = map(int, (sys.stdin.readline()).split()            )

a = list(map(int, (sys.stdin.readline()).split()))
for i in range(n):
	sys.stdout.write( str(a[(i+d)%n])+' ' ) 
