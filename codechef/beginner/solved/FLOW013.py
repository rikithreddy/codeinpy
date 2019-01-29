t = int(input())

for _ in range(t):
	x = list(map(int,input().split()))
	if sum(x) == 180:
		print('YES')
	else:
		print('NO')