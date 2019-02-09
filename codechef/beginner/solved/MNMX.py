import sys 
for _ in range(int(sys.stdin.readline())):
	n = int(int(sys.stdin.readline()))
	a =list(map(int, sys.stdin.readline().split()))
	sys.stdout.write(str( (n-1)*min(a) ) +'\n')