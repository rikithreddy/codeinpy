t = int(input())


for _ in range(t):
	n,k = map(int,input().split())

	frgt = input().strip().split()
	alllang = []
	for _ in range(k):
		alllang+=input().strip().split()[1:]

	for i in frgt:
		print('YES',end=' ') if i in alllang else print('NO',end =' ')
	print()

