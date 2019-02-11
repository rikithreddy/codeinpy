import sys 
for _ in range(int(sys.stdin.readline())):
	n,m = map(int, sys.stdin.readline().split())
	if n&1 ==0 or m&1==0:
		sys.stdout.write('YES\n')
	else:
		sys.stdout.write('NO\n')