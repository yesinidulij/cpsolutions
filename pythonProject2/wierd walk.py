for _ in range(int(input())):
    n=int(input())
    Ai=list(map(int,input().split()))
    Bi=list(map(int,input().split()))
    xA=0
    xB=0
    wd=0
    for i in range(n):
        if xA==xB and Ai[i]==Bi[i]:
            wd+=Ai[i]
        xA+=Ai[i]
        xB+=Bi[i]
    print(wd)
