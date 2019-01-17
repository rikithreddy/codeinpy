t = int(input())


for _ in range(t):
	n = int(input())
	x = list(map(int,input().split()))
	print('YES') if sum(x)%2==1 else print('NO')

