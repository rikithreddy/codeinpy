import sys

n,d = map(int,sys.stdin.readline().strip().split())
num = []
for i in range(n):
	num.append(int(sys.stdin.readline().strip()))
num.sort()


i,j,pairs = 0,1,0

while(j<n):
	if num[j] - num[i] <= d:
		pairs+=1
		i+=2
		j+=2
	else:
		i+=1
		j+=1

sys.stdout.write(str(pairs)+'\n')



