# cook your dish here
import sys

t = int(sys.stdin.readline().strip())
for _ in range(t):
	n = int(sys.stdin.readline().strip())
	r=[]
	l=[]
	for _ in range(n):
		x,y = map(int, sys.stdin.readline().strip().split())
		l.append(x)
		r.append(y)
	l.sort()
	r.sort()

	i=0
	j=0
	bomb = 0
	while i<n and j < n:
		if l[i]<r[j]:
			i+=1
		else:
			j+=1
			bomb+=1
	if j<n-1:
		bomb+=1
	sys.stdout.write(str(bomb)+'\n')


