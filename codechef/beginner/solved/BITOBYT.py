t = int(input())



def calculate(n):
	if n/26.0 > 1:

		# print(n/26,n/26 >0.0)
		if n%26!=0:
			a = int(pow(2,n//26))
			b = calculate(n%26)
			return b[0]*a , b[1]*a, b[2]*a
		else: 
			a =int(pow(2,(n//26) -1))
			return 0,0,a
	elif n in range(0,3):
		return (1,0,0)
	elif n in range(3,11):
		return (0,1,0)
	else: 
		return (0,0,1)


for _ in range (t):
	n = float(input())
	ans = calculate(n)
	print('{} {} {}'.format(ans[0],ans[1],ans[2]))