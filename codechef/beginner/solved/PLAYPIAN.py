import sys
for _ in range( int(sys.stdin.readline())):
	x = sys.stdin.readline().strip()
	i = 0
	flag = True
	n = len(x)
	while (i<n):
		if x[i] == x[i+1]:
			flag = False
			break
		i+=2
	sys.stdout.write('yes\n') if flag else sys.stdout.write('no\n')
