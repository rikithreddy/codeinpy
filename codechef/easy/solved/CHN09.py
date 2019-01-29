from collections import Counter

t = int(input())

for _ in range(t):
	s = input().strip()
	x = Counter(s)
	print(len(s)-max(x['a'],x['b']))