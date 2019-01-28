import string
import sys
x,y = sys.stdin.readline().strip().split()
y = list(y)
alpha = string.ascii_lowercase


for _ in range(int(x)):
	t =sys.stdin.readline().strip()
	tl = t.lower()
	for i in range(len(t)):
		if tl[i] == '_':
			sys.stdout.write(' ')
		elif tl[i] in [',','.','!','?']:
			sys.stdout.write(t[i])
		else:
			temp = alpha.index(tl[i])
			temp = y[temp]
			if t[i].isupper():
				temp = temp.upper()
			sys.stdout.write(temp)
	sys.stdout.write('\n')