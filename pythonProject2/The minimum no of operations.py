for _ in range(int(input())):
    n=int(input())
    li=list(map(int,input().split()))
    cnt=0
    for i in range(n):
        sel=li.index(max(li))
        if li.count(max(li)) == len(li):
            break
        for j in range(n):
            if j == sel:
                continue
            li[j]+=1
        cnt+=1

    print(cnt)




