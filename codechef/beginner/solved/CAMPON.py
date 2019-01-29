import sys
import numpy as np

t = int(sys.stdin.readline())

for _ in range(t):
	D= int(sys.stdin.readline())
	sum_ = np.zeros(31)
	for _ in range (D):
		d,p = map(int, sys.stdin.readline().split())
		sum_[d-1]+=p
	cumsum =[0]
	for i in range(31):
		cumsum.append(cumsum[i]+sum_[i])

	Q = int(sys.stdin.readline())
	for _ in range(Q):
		d,p = map(int, sys.stdin.readline().split())
		if p <= cumsum[d]:
			sys.stdout.write('Go Camp\n')
		else:
			sys.stdout.write('Go Sleep\n')