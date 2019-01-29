t = int(input())


for _ in range(t):
	n = int(input())
	x = [int(p) for p in input().strip()]
	des = [1]*n

	if n == 1:
		print(1-x[0])
	else:
		if x[0]==1:
			des[0] = 0
			des[1] = 0

		if x[-1] == 1:
			des[-1] = 0
			des[-2] = 0


		if n >2:
			for i in range(1,n-1):
				if x[i] == 1:
					des[i-1] ,des[i] , des[i+1] = 0,0,0
		print(sum(des))



