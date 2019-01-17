t = int(input())

for _ in range(t):
	house = [1]*100
	m,x,y = map(int,input().split())
	police = list(map(int,input().split()))
	dist = x*y

	for d in range(m):
		i = police[d-1]
		end = i+dist+1 if i+dist<100 else 100
		start = i-dist if i-dist>=0 else 0
		house[start:end] = [0]*(end-start)

	print(sum(house))
