for _ in range(int(input())):
    x,y,k,n=map(int,input().split())
    sum=0
    for i in range(n):
        pi,ci=map(int,input().split())
        if (pi>=(x-y)) & (k>=ci):
            sum+=1

    if sum>0:
        print("luckychef")
    else:
        print("unluckychef")



