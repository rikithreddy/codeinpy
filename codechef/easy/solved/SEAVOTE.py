t = int(input())
for _ in range(t):
	n = int(input())
	x = list(map(int,input().split()))
	l =0
	for i in x:
		if i!=0:
			l+=1 
	sumt = sum(x)
	if sumt >=100 and sumt -100 < l:
		print('YES')
	else:
		print('NO')