import sys
import numpy as np 

for _ in range(int(sys.stdin.readline())):
	n = int(sys.stdin.readline())
	x = np.array(list(map(int,sys.stdin.readline().split())))
	y = np.array(list(map(int,sys.stdin.readline().split())))

	a = np.sum(x[0::2])+np.sum(y[1::2])
	b = np.sum(x[1::2])+np.sum(y[0::2])

	sys.stdout.write(str(a)+'\n') if a < b else sys.stdout.write(str(b)+'\n')