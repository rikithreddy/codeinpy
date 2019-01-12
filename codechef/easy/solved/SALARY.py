t = int(input())


for i in range(t):
	n = int(input())

	W = sorted(list(map(int, input().split())))


	add = sum(W)
	mini = min(W)	
	print(add - n*mini)