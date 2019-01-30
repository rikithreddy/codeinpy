import sys
t = int(sys.stdin.readline())

for _ in range(t):
	n,w = map(int,sys.stdin.readline().split())

	c = list(map(int,sys.stdin.readline().split()))
	p = list(map(int,sys.stdin.readline().split()))
	tx = list(map(int,sys.stdin.readline().split()))
	all_=[]
	prod = []
	for i in range(n):
		temp = c[i]*p[i]
		prod.append(temp)
		all_.append((temp/tx[i], i))
	all_.sort(key=lambda x: x[0],reverse=True)
	total = 0

	for i in range(n):
		tm = all_[i][1]
		temp = tx[tm]

		w -= temp
		if w <=0:
			break
		else:
			total+=prod[tm]
	sys.stdout.write(str(total)+'\n')
