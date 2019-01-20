# cook your dish here
t = int(input())



for _ in range(t):
	x,y = map(float,input().split())

	print("%.6f"% (x*y)) if x <=1000 else print("%.6f" % (x*y - x*y*.1))