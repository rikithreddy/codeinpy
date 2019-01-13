t = int(input())


for i in range(t):
	x, y = map(int , input().split())

	if (y!=0):
		s = x//y
		teac= x%y

		print('{} {}'.format(s,teac))
	else: 
		print('0 {0}'.format(x))
