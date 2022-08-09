from math import gcd,lcm
for _ in range(int(input())):
    n=int(input())
    newlist=[]
    for i in range(n):
        for j in range(n):
            if (i+j)==n:
                m=int(gcd(i,j))+int(lcm(i,j))
                newlist.append(m)
    print(newlist.count(min(newlist)))