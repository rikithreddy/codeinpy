

x,y = map(int,input().split())
if (x-y)%10==9:
	print(int(x-y-1))
else:
	print(int(x-y+1	))