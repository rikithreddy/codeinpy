import sys

t = int(sys.stdin.readline())

for _ in range(t):
	p1,p2,k = map(int,sys.stdin.readline().split())
	if ((p1+p2)//k )%2 == 1:
		sys.stdout.write('COOK\n')
	else:
        sys.stdout.write('CHEF\n')