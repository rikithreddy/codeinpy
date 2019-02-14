import sys
for _ in range( int(sys.stdin.readline())):
	c = 0 
	for _ in range(int(sys.stdin.readline())):
		x,y = map(int ,(sys.stdin.readline()).split())
		if y-x > 5: c+=1

	sys.stdout.write(str(c)+'\n')