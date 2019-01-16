t = int(input())


for _ in range(t):
	n = input().strip()
	while(n[-1]=='0'):
		n = n[:-1]
	print(n[::-1])
