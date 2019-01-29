t = int(input())

for _ in range(t):
	n = int(input())
	x = set((input().strip()))

	if 'Y' not in x and 'I' not in x:
		print('NOT SURE')
	if 'Y' in x and 'I' in x:
		print('NOT SURE')
	if 'Y' in x:
		print('NOT INDIAN')
	if 'I' in x:
		print('INDIAN')