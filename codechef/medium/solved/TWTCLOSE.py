
ln=input().split()
N=int(ln[0])
K=int(ln[1])
tp=0
queue=[]
while(K>0):
    ln=input()
    if " " in ln:
        lst=ln.split()
        cmd=lst[0]
        key=int(lst[1])
        if cmd=="CLICK":
            if key not in queue:
                queue.append(key)
            else:
                queue.remove(key)
    if ln=="CLOSEALL":
        queue=[]
    print(len(queue))
    K-=1

