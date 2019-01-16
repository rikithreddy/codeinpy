t = int(input())


for i in range(t):
	n,m,k = map(int,input().split())
	x = abs(n-m)

	if(k > x):
		print(0)
	else:
		print(x-k)