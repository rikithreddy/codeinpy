import sys
import string
for _ in range(int(sys.stdin.readline())):
	n = int(sys.stdin.readline())
	d = list(string.ascii_lowercase)
	for _ in range(n):
		s = sys.stdin.readline().strip()
		temp =[]
		for i in d:
			if i in s:
				temp.append(i)

		d = temp 
	sys.stdout.write(str(len(d))+'\n')