for _ in range(int(input())):
    n=int(input())
    ai=list(map(int,input().split()))
    max_dist=ai[0]-0
    for i in range(1,n):
        if (ai[i]-ai[i-1])>max_dist:
            max_dist=ai[i]-ai[i-1]
    print(max_dist)
