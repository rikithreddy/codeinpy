import math




t = int(input())

for i in range(t):
	b,ls = map(float,input().split())
	mini = math.sin(  math.acos(b/ls) )*ls
	maxi = ls/math.sin(  math.atan(ls/b) )
	print(str(mini)+' '+str(maxi))