t = int(input())


for i in range(t):

	x = list(input().strip())
	d ={}
	for t in x:
		if t in d:
			d[t]+=1
		else:
			d[t]=1

	if 2* max(list(d.values())) == sum(d.values()):
		print('YES')
	else:
		print("NO")
