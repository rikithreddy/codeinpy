import sys
def x(n):
	return str(abs((n*(n+1)*(2*n+1) // 6) - n*n*(n+1)*(n+1) // 4       ) )
for _ in range(int(sys.stdin.readline())):
	sys.stdout.write(x(int(sys.stdin.readline()))   +'\n'           )

