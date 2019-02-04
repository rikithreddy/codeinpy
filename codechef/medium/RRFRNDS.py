import sys

n = int(sys.stdin.readline())
adj_mat = []
ints = []
for ln_i in range(n):
	adj_mat.append(sys.stdin.readline())
	ints.append(int(adj_mat[ln_i], 2))
requests = 0
for i in range(n):
	for j in range(i):
		if adj_mat[i][j] == '0':
			if (ints[i] & ints[j]): 
				requests += 2
sys.stdout.write(str(requests)+'\n')