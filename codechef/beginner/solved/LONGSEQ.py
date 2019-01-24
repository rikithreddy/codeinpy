import numpy as np
t = int(input())


for _ in range(t):
	x  = np.array(list(input().strip()))

	if np.count_nonzero(x == '1') == len(x)-1   or np.count_nonzero(x == '0') == len(x)-1:
		print('Yes')
	else:
		print('No')
