import math

def isprime(n):
	if n == 1:
		return False
	if n == 2:
		return True
	if n%2 ==0:
		return False
	for i in range(3, int(math.sqrt(n))+1):
		if n%i == 0:
			return False
		
	return True

t = int(input())
for i in range(t):
	n = int(input())
	print('yes') if (isprime(n)) else print('no')
