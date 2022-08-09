for _ in range(int(input())):
    n,k=map(int,input().split())
    li=list(map(int,input().split()))
    sume=0
    for i in range(n):
        for j in li[i:]:
            if sume>=k:
                break
            sume+=j
    if sume>0:
        print("YES")
    else:
        print("NO")