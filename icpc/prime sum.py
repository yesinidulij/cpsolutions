for _ in range(int(input())):
    n = int(input())
    B = list(map(int, input().split()))[:n]
    li = [*range(1,n+1)]
    ans=0
    for i in range(n):
        m = B.count(li[i])
        sume = li[i]
        for j in range(i,n):
             if li[j]%B[j]==0 and B[j] in li[:j]:
                 li[j]=B[j]
    print(li)
    if li==B:
        print("YES")
    else:
        print("NO")
