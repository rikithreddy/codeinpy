def x(n):
	d = {}
	for i in range(n):
		z = sum(list(map(int, list(str(i)))))
	if z not in d:
		d[z] = 1
	else:
		d[z]+=1
	from collections import Counter
	x = Counter(d.values())[ max(d.values()) ]
	return x

print(x(10))