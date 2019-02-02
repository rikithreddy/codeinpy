import sys
l=[list(map(int,(sys.stdin.readline()).split()))]
l.append(list(map(int,(sys.stdin.readline()).split())))
l.append(list(map(int,(sys.stdin.readline()).split())))
l.append(list(map(int,(sys.stdin.readline()).split())))
l.append(list(map(int,(sys.stdin.readline()).split())))
l.append(list(map(int,(sys.stdin.readline()).split())))

sum_ = -999
for i in range(0,4):
	for j in range(0,4):
		x = l[i][j] + l[i][j+1] + l[i][j+2] + l[i+1][j+1] + l[i+2][j] + l[i+2][j+1] + l[i+2][j+2]
		if x > sum_:
			sum_= x

sys.stdout.write(str(sum_))
