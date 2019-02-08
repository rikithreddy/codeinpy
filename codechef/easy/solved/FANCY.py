import sys 
for _ in range(int(sys.stdin.readline())):
	x = sys.stdin.readline().strip()
	if len(x) > 3:
		if ' not ' in x or (x[0:3] =='not' and x[3]==' ') or (x[-3:len(x)]=='not' in x and x[-4]==' '):
			sys.stdout.write('Real Fancy\n')
		else:
			sys.stdout.write('regularly fancy\n')
	else:
		if 'not'==x:
			sys.stdout.write('Real Fancy\n')
		else:
			sys.stdout.write('regularly fancy\n')
			