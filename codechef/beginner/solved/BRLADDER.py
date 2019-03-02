import sys
for _ in range(int(sys.stdin.readline())):
	a, b = map(int, sys.stdin.readline().strip().split())
	if abs(a-b) == 2:
		sys.stdout.write("YES\n")
	elif (a&1 == 0 and b&1 == 1 and a-b == 1):
		sys.stdout.write("YES\n")
	elif (b&1 == 0 and a&1 == 1 and b-a == 1):
		sys.stdout.write("YES\n")

	else:
		sys.stdout.write("NO\n")

