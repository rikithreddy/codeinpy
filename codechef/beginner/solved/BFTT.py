from sys import stdin, stdout

def num(n):
    k=0
    while(True):
        next=str(n+1)
        if(next.count("3")>=3):
            break
        n+=1
    return next


for _ in range(int(stdin.readline())):
    n=int(stdin.readline())
    stdout.write(num(n) +'\n')