t = int(input())


for _ in range(t):
	x = list(map(int,input().split()))
	flag = False
	sum_ = 0
	for i in range(30):
		if x[i]==1:
			sum_+=1
			if sum_ > 5:
				flag = True
				break

		else:
			sum_=0

	print('#coderlifematters') if flag else print("#allcodersarefun")