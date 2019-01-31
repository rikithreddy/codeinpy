from sys import stdin,stdout

for _ in range(int(stdin.readline())):
	n = int(stdin.readline())

	arr = list(map(int, stdin.readline().split()))
	gcd = arr[0]
	for i in range(1,n):
		while arr[i] != 0:
			gcd , arr[i] = arr[i], gcd%arr[i] 

	stdout.write(str(gcd)+'\n')


