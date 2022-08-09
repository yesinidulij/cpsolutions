from math import  ceil
for _ in range(int(input())):
    n=int(input())
    li=[*range(1,n+1)]
    cnt=1
    m=[]
    for i in range(ceil(n/3)):
        m.append(li[-(i+1)])
        if li[cnt] not in m:
         m.append(li[cnt])
        m.append(li[cnt-1])
        cnt+=2
    print(*m)


