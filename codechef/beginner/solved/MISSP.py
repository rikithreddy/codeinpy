import sys
for _ in range(int(sys.stdin.readline())):
	sum_ = 0
	for _ in range (int(sys.stdin.readline())):
		sum_^=int(sys.stdin.readline())

	sys.stdout.write(str(sum_)+'\n')