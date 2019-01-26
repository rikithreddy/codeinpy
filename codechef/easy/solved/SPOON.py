import numpy as np
t = int(input())

for _ in range(t):
	r,c = map(int,input().split())
	lists = []
	flag = False 
	for _ in range(r):
		str_ = input().strip()
		if 'spoon' in str_.lower():
			flag = True
		lists.append(list(str_))

	if not flag:
		lists = list(np.array(lists).T)
		for x in lists:
			if 'spoon' in "".join(x).lower():
				flag = True
				print('There is a spoon!')

				break


	else: 
		print('There is a spoon!')

	if not flag:
		print('There is indeed no spoon!')