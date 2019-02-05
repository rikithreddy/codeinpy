import sys
l =[]
for _ in range(int(sys.stdin.readline())):
	l.append(int(sys.stdin.readline()))

for i in range(32,-1,-1):
	num = 2<<i
	temp =[]
	for x in l:
		if num&x!=0:
			temp.append(x)
	if len(temp) > 1:
		l = temp

sys.stdout.write(str(l[0]&l[1]))