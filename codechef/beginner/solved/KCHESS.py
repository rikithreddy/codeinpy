t = int(input())
all_set = set()
for _ in range(t):
	n = int(input())
	for i in range(n):
		x,y = map(int, input().split())
		all_=[ (x+2,y+1),(x+2,y-1),
					(x+1,y+2), (x+1,y-2),
					(x-1,y+2),(x-1,y-2),
					(x-2,y+1),(x-2,y-1) ]
		for p in all_:
			all_set.add(p)
	all_set = set(all_set)
	x,y = map(int, input().split())
	tem = [(x,y),(x,y+1),(x,y-1),
		(x-1,y-1),(x-1,y),(x-1,y+1),
		(x+1,y-1),(x+1,y),(x+1,y+1)]
	flag = False	
	for l in tem:
		if (l not in all_set):
			flag=True

	print('NO') if flag else print('YES')