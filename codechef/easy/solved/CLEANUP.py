t = int(input())


for i in range(t):
	n,m = map( int, input().split()  )

	completed  =   list(map(int, input().split()) )

	all_elements = list(range(1,n+1))

	for j in range(len(completed)):
		idx = all_elements.index(completed[j])
		del all_elements[idx]


	l1 = []
	l2 = []
	for j in range(n-m):
		if j%2==0:
			l1.append(str(all_elements[j]))
		else:
			l2.append(str(all_elements[j]))

	print(' '.join(l1))
	print(' '.join(l2))


