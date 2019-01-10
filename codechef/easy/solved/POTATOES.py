
from math import sqrt



def prime(num):

	for i in range(2,int(sqrt(float(num)))+1):
		if num%i ==0:
			return False
		
	return True

t = int(input())


for i in range(t):
	x,y  = map(int, input().split())

	j=1
	while True:
		if prime(x+y+j):
			print(j)
			break
		j+=1
