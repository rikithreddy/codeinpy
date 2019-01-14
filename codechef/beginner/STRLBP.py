t = int(input())

for _ in range(t):
	seq = input().strip()
	cnt =0
	for  i in range(-1,len(seq)-1):
		if seq[i]!=seq[i+1]:
			cnt+=1
	print('uniform') if cnt <=2 else print('non-uniform')