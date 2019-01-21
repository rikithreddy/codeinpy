import math
import sys
global prime
global facs
prime =[2]
def isprime(n):
	x = True
	t =int(math.sqrt(n))
	for i in prime:
		if n%i==0:
			x=False 
			break
		if i > t+1:
			break
	return x


facs ={}

def getfactors(n,i):
	if (n,i) in facs:
		return facs[(n,i)]

	if n%i!=0:
		return 0

	else:
		cal_ = 1+ getfactors(n//i,i)
		facs[(n,i)]=cal_
		return cal_



for i in range(3,1000000):
	if isprime(i):
		prime.append(i)


t = int(sys.stdin.readline())

for i in range(t):
	n = int(sys.stdin.readline())
	ai = list(map(int,sys.stdin.readline().strip().split()))
	
	d = {}
	for a in ai:
		for j in prime:
			if j > a:
				break

			t = getfactors(a,j)

			if j in d:
				d[j] += t
			else:
				d[j] = t

			a/=pow(j,t)


	sum_ = 1

	for j in d.values():
		sum_ *= (j+1)

	print(sum_)

