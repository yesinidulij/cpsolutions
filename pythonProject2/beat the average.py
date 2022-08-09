for _ in range(int(input())):
    n,m,x=map(int,input().split())
    sume=0
    cnt=0
    while sume<x:
        sume=(sume+(x+1))//n
        cnt+=1
    print(sume)