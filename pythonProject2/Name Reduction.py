# cook your dish here
for _ in range(int(input())):
    A,B=map(str,input().split())
    D=A+B
    mydict=dict(D)
    print(mydict)
    n=int(input())
    flag=0
    c=""
    for  _ in range(n):
        ci=input()
        c+=ci
    if c in stri:
        print("YES")
    else:
        print("NO")