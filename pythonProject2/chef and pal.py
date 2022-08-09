for _ in range(int(input())):
    n=int(input())
    li=['0']*n
    if len(li)%2!=0:
        print(-1)
    else:
        for i in range(len(li)//2):
            li[i]='1'
        print(''.join(li))