import sys

for _ in range(int(sys.stdin.readline())):
	r_ = int(sys.stdin.readline())
	r_ = r_**2 
	x1,y1 = map(int, sys.stdin.readline().split())
	x2,y2 = map(int, sys.stdin.readline().split())
	x3,y3 = map(int, sys.stdin.readline().split())
	c = 0

	if (x1-x2)**2 + (y1-y2)**2  <= r_:
		c+=1
	if (x1-x3)**2 + (y1-y3)**2  <= r_:
		c+=1
	if (x2-x3)**2 + (y3-y2)**2  <= r_:
		c+=1
	if c >= 2:
		sys.stdout.write("yes\n")
	else:
		sys.stdout.write("no\n")

