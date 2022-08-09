for _ in range(int(input())):
    n=int(input())
    Ai=list(map(int,input().split()))
    ans=Ai[0]
    cnt=1
    for i in Ai:
        if i>ans:
            cnt+=1
            ans=i
    print(cnt)