import sys
for _ in range(int(sys.stdin.readline())):
	n = int(sys.stdin.readline())
	l = list(map(int,(sys.stdin.readline()).split()))
	r = list(map(int,(sys.stdin.readline()).split()))
	mas = -1	
	rating = -1
	index = 0
	for i in range(n):
		t = l[i]*r[i]
		if mas  < t:
			mas = t
			rating = r[i]
			index = i
		elif mas == t:
			if r[i] > rating:
				rating = r[i]
				index = i

	sys.stdout.write(str(index+1)+'\n')

