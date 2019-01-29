# cook your dish here
import sys
import numpy as np
n,k = map(int,sys.stdin.readline().split())
a = np.array(list(map(int,sys.stdin.readline().split())))


l = np.sort(a)
if k!=0:
    ak = l[k-1]
    if k%2==0:
    	a = ak-a
    else:
    	a = ak+a
    if k!=0:
        a[a<0] = 0
for i in range(n):
	sys.stdout.write(str(a[i])+' ')
sys.stdout.write('\n')