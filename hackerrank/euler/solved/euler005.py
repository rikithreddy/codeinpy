import sys
lcm = [1]
for i in range(2,41):
	y = lcm[i-2]
	x = i
	while y!=0:
		x,y  = y , x%y
	lcm.append(i*lcm[i-2] // x)

for _ in range(int(sys.stdin.readline())):
	sys.stdout.write(str(lcm[int(sys.stdin.readline())-1 ]) + '\n' )