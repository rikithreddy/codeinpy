t = int(input())


for _ in range(t):
	n,x = map(int,input().split())

	t = list(map(int,input().split()))
	t_ = sum(t)
	b = (t_//x) 

	if 	(t_ - min(t))//x == b: 
			print(-1)
	else:
		print(b)
