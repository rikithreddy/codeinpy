t = int(input())


for i in range(t):
	n = int(input())
	d ={}
	for _ in range(n):
		x = input().strip()

		user, vote = x.split()
		bit =1
		if vote =='-':
			bit = -1

		d[user]  = bit 
	
	temp =0
	for x in d.values():
		temp+=x

	print(temp)

