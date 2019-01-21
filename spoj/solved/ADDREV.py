t = int(input())

for _ in range(t):
        x,y = input().split()
        x =x.strip()
        y = y.strip()
        x = x[::-1] 
        y = y[::-1]

        x = int(x)
        y = int(y)
        answer = (x+y)
        strans = str(answer)[::-1]
        while len(strans)!=1:
                if strans[0]=='0':
                        strans = strans[1:]
                else:
                        break 
        print (strans)






