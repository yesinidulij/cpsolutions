from math import ceil,gcd
for _ in range(int(input())):
    n,m=map(int,input().split())
    cntoddn=ceil(n/2)
    cntevenn=n//2
    mcntodd = ceil(m / 2)
    mcnteven = m // 2
    ans=(cntevenn*mcntodd)+(cntoddn*mcnteven)
    answ=ans//gcd(ans,n*m)
    nm=(n*m)//gcd(ans,n*m)
    print(str(answ)+"/"+str(nm))

