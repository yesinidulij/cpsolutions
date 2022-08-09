t=int(input())
for _ in range(t):
    L,R=map(int,input().split())

    if R%L!=0:
        print(R)
    else:
        print(-1)