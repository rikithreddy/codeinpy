t = int(input())

for _ in range(t):
	n = int(input())

	data = [[0]*n for _ in range(n)]
	n2 = n*n
	i,j = 0,0
	jmax = 0
	imin = 0
	jmin=0
	done =0
	for k in range(n2):
		data[i][j] =k

		i+=1
		j-=1



		if j <jmin:

			j = jmax+1

			if jmax!=n-1:
				jmax+=1
				i=jmin
				j=jmax
			else:

				jmin+=1
				i=jmin
				j=n-1


	for i in range(n):
		for j in range(n):
			print((data[i][j])+1,end=' ')

		print()