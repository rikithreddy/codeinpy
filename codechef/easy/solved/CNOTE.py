t = int(input())


for _ in range(t):
	x,y,k,n = map(int,input().split())

	leftp = x-y
	luck =0
	for i in range(n):
		p,c = map(int,input().split())
		if p>=leftp and c <= k:
			luck=1
	
	print('LuckyChef') if luck==1 else print('UnluckyChef')



