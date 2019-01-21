t = int(input())

for i in range(t):
	n = int(input())
	a = list(map(int,input().split()))


	if n == 1:
		print(2*a[0])

	else:
		xor =(2*a[0])^(2*a[1])

		for j in range(2,len(a)):
			xor^=(2*a[j])

		print(xor)


