a,n,k = map(int,input().split())


n+=1

for i in range(k):
	print(int(a%n) ,end=' ')
	a/=n