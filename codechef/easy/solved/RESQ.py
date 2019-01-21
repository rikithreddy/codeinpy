import math

t = int(input())

def facs(n):
	s =[]
	for i in range(1,int(math.sqrt(n))+1):
		if n% i ==0:
			s.append([i,n//i])
	return s


for _ in range(t):
	n = int(input())

	f = facs(n)
	min_ = 10**8 +1
	for i in f:
		tem = abs(i[0]-i[1])
		if tem < min_:
			min_ = tem
	print(tem)

