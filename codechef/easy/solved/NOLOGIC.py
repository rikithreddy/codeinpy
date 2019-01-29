import string 


t = int (input())


for _ in range(t):
	letters = list(string.ascii_lowercase)
	x = input().strip()
	x = x.lower()
	for i in range(len(x)):
		if x[i] in letters:
			letters.remove(x[i])

	if len(letters)!=0:
		print(''.join(letters))
	else:
		print('~')