n = int(input())



c = list(map(int, input().split()))


total = sum(c)

expected = (n*(n+1))/2

if total == expected:
	print('YES')
else:
	print('NO')