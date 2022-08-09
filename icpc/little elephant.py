t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    pi=list(map(int,input().split()))[:m]
    sume=0
    for i in range(n):
        s=input()
        vi=list(map(str,s[2:].split()))
        vi.sort()
        ci=int(s[0])
        ans=min(pi.count(int(vi[0])),len(vi))
        sume+=sum(vi[:ans])
        vi[:ans].clear()
    print(sume)