t = int(input())

for i in range(t):

	n = int(input())

	for j in range(n):

		I,N,Q = map(int , input().split())
		x = int(N/2)
		if N%2==0 or I==Q:
			print(x)
		else:
			print(1+x)
