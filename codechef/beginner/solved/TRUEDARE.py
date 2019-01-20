import numpy as np
t = int(input())


for _ in range(t):

	tr = int(input())
	Tr = list(map(int,input().split()))
	Tr = list(np.unique(np.array(Tr)))

	dr = int(input())
	Dr = list(map(int,input().split()))
	Dr = list(np.unique(np.array(Dr)))

	
	ts = int(input())
	Ts = list(map(int,input().split()))
	Ts = list(np.unique(np.array(Ts)))
	


	ds = int(input())
	Ds = list(map(int,input().split()))
	Ds = list(np.unique(np.array(Ds)))
		
	do = True

	for i in Ts:
		if i not in Tr:
			do =False
			break

	if do:
		for i in Ds:
			if i not in Dr:
				do =False


	print('yes') if do else print('no')