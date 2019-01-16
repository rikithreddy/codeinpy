import numpy as np
n,q=map(int,sys.stdin.readline())
arr=np.zeros(n,dtype=bool)
for _ in range(q):
    a,b,c=map(int,sys.stdin.readline())
    if a==0:
        arr[b:c+1]=~arr[b:c+1]
    else:
        print(arr[b:c+1].sum())
        
