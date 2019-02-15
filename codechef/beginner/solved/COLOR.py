import sys
from collections import Counter
for _ in range( int(sys.stdin.readline())):
	n = int(sys.stdin.readline())
	x = Counter(sys.stdin.readline())
	sys.stdout.write(str(n-max(x.values())) +'\n')