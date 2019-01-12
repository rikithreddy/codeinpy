t = int(input())

numbers = []
for i in range(t):
	numbers.append(int(input()))

numbers = sorted(numbers)

for i in range(t):
	print(numbers[i])