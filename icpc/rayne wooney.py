to=int(input())
for _ in range(to):
    n=int(input())
    ai=list(map(int,input().split()))
    maxd=0
    for i in range(1,n):
        if maxd<(ai[i]-ai[i-1]):
            maxd=ai[i]-ai[i-1]
    if maxd>0:
        print(maxd)
    else:
        print("UNFIT")


