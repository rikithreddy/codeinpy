t = int(input())

for i in range(t):
	n = int(input())
	cars = list(map(int,input().split()))
	total = 1
	temp = cars[0]
	for j in range(1,n):
		if cars[j] < temp:
			total+=1
			temp = cars[j]
	print(total)