import sys
for _ in range(int(sys.stdin.readline())):
	n = int(sys.stdin.readline())
	x = set(map(int, sys.stdin.readline().strip().split()))
	print(len(x))