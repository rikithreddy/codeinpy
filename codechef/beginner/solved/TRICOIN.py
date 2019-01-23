t = int(input())

for _ in range(t):
	n = int(input())

	a = 0
	while(True):
		if(a*(a+1)//2 > n):
			a-=1
			break

		a+=1

	print(a)