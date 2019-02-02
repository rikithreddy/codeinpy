import sys
int(sys.stdin.readline())
x = sys.stdin.readline()
t,total = 0,0 
for i in x:
	if i =='D':
		if t ==0:
			total+=1
		t-=1
	else:
		t+=1

sys.stdout.write(str(total))