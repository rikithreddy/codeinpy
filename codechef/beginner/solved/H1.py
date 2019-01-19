t = int(input())

testcases = []

for _ in range(t):
	x = input().strip()
	r1 = list(map(int,input().split()))
	r2 = list(map(int,input().split()))
	r3 = list(map(int,input().split()))
	x = r1+r2+r3
	testcases.append(x)


prime = [3,5,7,11,13,17]
swaps = [ (0,1),(0,3),(1,2),(1,4),(2,5),(3,6),(3,4),(4,5) ,(4,7)
		,(5,8),(6,7),(7,8)]

current=[[1,2,3,4,5,6,7,8,9]]
visited={(1,2,3,4,5,6,7,8,9):0}



while len(current)!=0:
	state = current.pop(0)
	for move in swaps:

		if state[move[0]] + state[move[1]] in prime:
			s2=state[:]
			s2[move[0]] ,s2[move[1]] = state[move[1]],state[move[0]]
			if tuple(s2) not in visited:
				visited[tuple(s2)] =  visited[tuple(state)] +1
				current.append(s2)



for i in testcases:
	if tuple(i) in visited:
		print(visited[tuple(i)])
	else:
		print(-1)