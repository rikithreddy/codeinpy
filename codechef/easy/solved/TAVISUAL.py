import sys

for _ in range(int(sys.stdin.readline())):
	 n, c, q = map(int, sys.stdin.readline().split())

	 for _ in range(q):
	 	l, r = map(int, sys.stdin.readline().split())
	 	if l <= c <= r:
	 		c = r - c + l 

	 sys.stdout.write(str(c)+'\n')
