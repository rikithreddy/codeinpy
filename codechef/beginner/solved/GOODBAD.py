def counts(w):
	l,u = 0,0
	for i in range(len(w)):
		if w[i].islower():
			l+=1
		else:
			u+=1
	return (l,u)

t = int(input())
for _ in range(t):
	n,k = map(int,input().split())
	w = input().strip()
	l,u = counts(w)

	lf=False
	uf= False
	if l+k>=n:
		lf = True
	if u+k >= n :
		uf = True


	if lf and uf:
		print('both')
	elif lf:
		print('chef')
	elif uf:
		print('brother')
	else:
		print('none')



