from math import gcd
for _ in range(int(input())):
    A,B=map(int,input().split())
    li=[]
    for i in range(abs(A-B)):
        m=gcd(A+i,B+i)
        if m not in li:
            li.append(m)
    print(len(li))
