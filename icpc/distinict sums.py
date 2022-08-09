for _ in range(int(input())):
    L,R=map(int,input().split())
    m=(R-L)+1
    ans=(m*(m+1))//2
    print(ans)