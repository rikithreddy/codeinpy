


def subsetsum(x,sum_,n):
	if sum_==0: return True

	if n==0: return False

	if x[n-1] > sum_:
		return subsetsum(x,sum_,n-1)
	return subsetsum(x,sum_,n-1) or subsetsum(x,sum_-x[n-1],n-1)

t = int(input())

for _ in range(t):
	n,sum_  =map (int,input().split())

	x = []
	for i in range(n):
		x.append(int(input()))

	print('Yes') if subsetsum(x, sum_,n) else print('No')