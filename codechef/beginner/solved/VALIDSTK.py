import sys

t = int(sys.stdin.readline())

for _ in range(t):
	n= int(sys.stdin.readline())
	x = list(map(int,sys.stdin.readline().split()))
	count =0 
	flag = True
	for i in range(n):
		if x[i] == 1:
			count+=1
		else:
			count-=1
			if count == -1:
				flag = False
				break
	sys.stdout.write('Valid\n') if flag else sys.stdout.write('Invalid\n')