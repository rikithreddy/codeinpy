import sys
t =int(sys.stdin.readline())

for _ in range(t):
	n =int(sys.stdin.readline())
	arr = list(map(int,sys.stdin.readline().split()))
	arr.sort()
	a = arr[0:n//2]
	b = arr[n//2:n]
	sum_=0
	for i in range(n//2):
		sum_+=b[-i-1] - a[i]
	sys.stdout.write(str(sum_)+'\n')