import sys

days = {'monday' : 0, 'tuesday':1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}

t = int(sys.stdin.readline())

for _ in range(t):
	lo = sys.stdin.readline().strip().split()
	s,e,l,r = days[lo[0]], days[lo[1]], int(lo[2]) , int(lo[3])

   
	x = e - s + 1 if e >= s else e - s + 8
	if x < l:
		x += (l - x) // 7 * 7 if (l - x) % 7 == 0 else ((l - x) // 7 + 1) * 7

	print('impossible') if x > r else print('many') if x + 7 <= r else print(x)
