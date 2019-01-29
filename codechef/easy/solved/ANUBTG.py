import sys

t = int(sys.stdin.readline())

for _ in range(t):
	n = int(sys.stdin.readline())
	arr = sorted(list(map(int, sys.stdin.readline().split())),	reverse = True)
	sum_ = 0 
	i =0 
	while i < n:

		sum_+=arr[i]
		if i+1< n:
			sum_+=arr[i+1]
		i+=4
	sys.stdout.write(str(sum_)+'\n')

