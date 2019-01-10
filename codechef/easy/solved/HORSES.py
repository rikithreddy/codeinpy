t = int(input())

for i in range (t):
	n = int(input())
	numbers = sorted(list(map( int,input().split() )))

	minimum = max(numbers)
	for j in range(n-1):

		temp = numbers[j+1] - numbers[j]
		if temp < minimum:
			minimum=temp
	print(int(minimum))