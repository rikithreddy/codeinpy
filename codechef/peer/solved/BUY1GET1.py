import math
t = int(input())


for i in range(t):
	jewels = input()
	unique = {}

	for x in jewels:
		if x in unique.keys():
			unique[x]+=1
		else:
			unique[x]=1



	total =0
	for j in unique:
		delta = unique[j]
		total+= math.ceil (delta /2)

	print(total)