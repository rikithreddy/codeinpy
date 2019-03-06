import sys
n = [0]*(int(sys.stdin.readline())+1)
a = list(map(int, sys.stdin.readline().split()))

for item in a:
	n[item]+=1

for i, j in enumerate(n):
	if j == 0:
		sys.stdout.write(str(i))
		sys.stdout.write(' ')

