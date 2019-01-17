t = int(input())


p1 = 0
p2 = 0 
maxi = 0
leader = 1

for i in range(t):
	x,y = map(int,input().split())
	p1+=x
	p2+=y
	if abs(p1-p2) > maxi:
		leader = 1 if p1 > p2 else 2 
		maxi = abs(p1-p2)

print('{} {}'.format(leader,maxi))