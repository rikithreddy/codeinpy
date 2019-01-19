t = int(input())

for _ in range(t):
	n = int(input())
	d={}
	s2 = None
	s1 = input().strip()
	total=1
	for i in range(n-1):
		temp = input().strip()
		if temp == s1:
			total+=1
		else:
			s2 = temp
			total-=1 

	if total> 0:
		print(s1)
	elif total < 0:
		print(s2)
	else:
		print('Draw')