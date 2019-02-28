from sys import stdin, stdout
wrds = stdin.readline().strip()
for _ in range(int(stdin.readline().strip())):
	word = stdin.readline().strip()
	if all(x in wrds for x in word):
		stdout.write("Yes\n")
	else:
		stdout.write("No\n")
