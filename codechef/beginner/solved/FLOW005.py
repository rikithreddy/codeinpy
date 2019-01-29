t = int(input())


notes = [100,50,10,5,2,1]

for i in range(t):
	n = int(input())
	c =0
	for j in notes:
		c += n//j
		n = n%j
		if n ==1:
			break

	print(c)