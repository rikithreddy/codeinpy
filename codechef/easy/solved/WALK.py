import sys
t = int(sys.stdin.readline())

for _ in range(t):
	n = int(sys.stdin.readline())
	w = list(map(int,sys.stdin.readline().split()))
	mini = w[0]
	for i in range(n):
		
		if w[i]+=i > mini:
			mini = w[i]+i

	sys.stdout.write(str(mini)+'\n')