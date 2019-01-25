import math
from sys import stdin
def isprime(n):
	if n == 1:
		return False
	if n == 2:
		return True
	if n>2 and n%2==0:
		return False
	for i in range(3,int(math.sqrt(n))+1):	
		if n%i ==0:
			return False
	return True




				

t = int(stdin.readline())


for _ in range(t):
	m,n = map(int,stdin.readline().split())

	for i in range(m,n+1):
		if(isprime(i)):
			print(i)
	print()