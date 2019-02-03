import sys
from collections import Counter
for _ in range(int(sys.stdin.readline())):
	 n,a,b = map(int, sys.stdin.readline().split())
	 arr = map(int, sys.stdin.readline().split())
	 x = Counter(arr)

	 if a not in x:
	 	x[a] = 0
	 if b not in x:
	 	x[b] = 0
	 sys.stdout.write(str(  (x[a]/n) * (x[b]/n)    )+ '\n')