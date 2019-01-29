t = int(input())

for _ in range(t):
	x = input().strip()
	y = input().strip()

	flag = True
	for i in range(len(x)):
		if x[i]!=y[i] and x[i]!='?' and y[i]!='?':
			flag=False
			break

	print('Yes') if flag else print('No')