t = int(input())

for _ in range(t):
	n = int(input())
	playlist = list(map(int, input().split()))
	k = int(input())
	value = playlist[k-1]
	sortedlist = sorted(playlist)
	print(int(sortedlist.index(value))+1)