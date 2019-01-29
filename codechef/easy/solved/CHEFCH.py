import sys
t = int(input())


for _ in range(t):
	x = sys.stdin.readline().strip()

	m1 = 0
	m2 = 0
	n = len(x)  
	for i in range(n):
		if x[i]=='-' and i&1 ==0:
			m1+=1
		elif x[i]=='+' and i&1 == 1:
			m1+=1

		if x[i]=='+' and i&1 ==0:
			m2+=1
		elif x[i]=='-' and i&1 == 1:
			m2+=1

	print(m1) if m1<m2 else print(m2)