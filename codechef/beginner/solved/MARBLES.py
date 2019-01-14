t = int(input())




def get_comb(n,k):
	num = 1
	den = 1
	for i in range(n+1-k,n+1):
		num*=i

	for i in range(1,k+1):
		den*=i

	return num//den


for _ in range(t):

	n,k = map(int,input().split())
	total = 1
	
	n = n-1
	k = k-1
	if (n-k < k):
		k = n-k

	print(get_comb(n,k))

