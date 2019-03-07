import sys
for _ in range(int(sys.stdin.readline())):
	n = int(sys.stdin.readline())
	arr = map(int,sys.stdin.readline().split())
	sys.stdout.write(str(sum(arr)-n+1)+'\n')