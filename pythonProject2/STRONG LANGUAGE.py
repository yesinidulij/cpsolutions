for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    flag=0
    for i in s:
        if "*"*k in s:
          flag+=1
    if flag!=0:
        print("YES")
    else:
        print("NO")