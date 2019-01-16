n = int(input())

x = list(map(int,input().split()))

t = 0
for i in range(n):
	t= (t+1) if x[i]%2==0 else (t-1)
print('READY FOR BATTLE') if t > 0 else print('NOT READY')
