import sys

for _ in range(int(sys.stdin.readline())):
	n,k,v = map(float, sys.stdin.readline().strip().split())
	x = float(sum(list(map(int, sys.stdin.readline().strip().split()))))

	number = (v*(n+k)-x)/k
	x = int(number) if number.is_integer() else -1
	sys.stdout.write(str(x)+'\n' if x > 0 else "-1\n")	
