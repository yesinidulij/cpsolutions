for _ in range(int(input())):
    s=input()
    a=s[:(len(s)//2)]
    b=s[len(s)//2+1:]
    sum=0
    for i in range(len(b)):
        if b[i:] in a:
            sum=1
    if sum==0:
        print("NO")
    else:
        print("YES")

