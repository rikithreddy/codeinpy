t = int(input())

def gcd(x,y):
	while(y!=0):
		x,y = y,x%y
	return x



for i in range(t):
	x = list(map(int,input().split()))
	gcd_= gcd(x[1],x[2])
	for i in range(3,len(x)):
		gcd_ = gcd(gcd_,x[i])
	for i in range(1,len(x)):
		print(x[i]//gcd_,end=" ")
	print()
