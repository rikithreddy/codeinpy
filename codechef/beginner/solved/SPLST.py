t = int(input())

for _ in range(t):
	a,b,c ,x,y  = map(int,input().split())
	if a+b+c == x+y:
		if min(x,y) >= min(a,b,c):
			print('YES')
		else:
			print('NO')
	else :
		print('NO')