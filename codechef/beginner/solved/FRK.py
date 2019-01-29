n = int(input())
subs = ['ch','he','ef', 'che' , 'hef', 'chef']

count = 0
for _ in range(n):
	name  = input().strip()
	for x in subs:
		if x in name:
			count+=1
			break
print(count) 
