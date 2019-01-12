t = int(input())


for i in range (t):
	x = input()
	y = input()
	c=0
	for j in range(len(y)):
		if y[j] in x:
			c+=1
	print(c)