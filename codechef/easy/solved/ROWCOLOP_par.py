import numpy as np
from sys import stdin, stdout

n,q = map(int, stdin.readline().split())
d = np.zeros((n,n))
for _ in range(q):
	state, id_ , value = stdin.readline().strip().split()
	if state == 'RowAdd':
		d[int(id_)-1] += int(value)
	else:
		d[:,int(id_)-1] += int(value)
stdout.write(str(int(np.max(d)))+ '\n')