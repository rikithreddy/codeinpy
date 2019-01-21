n1,n2,n3 = map(int,input().split())

d = {}

for _ in range(n1+n2+n3):
	t =int(input()) 
	if t in d:
		d[t]+=1
	else:
		d[t]=1

l=[]
for x,y in d.items():
	if y>1:
		l.append(x)

l = sorted(l)
print(len(l))
for i in range(len(l)):
	print(l[i])

