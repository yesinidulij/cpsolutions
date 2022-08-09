for _ in range(int(input())):
    li=[]
    while 1:
        n=int(input())
        if n==0:
            break
        li.append(n)
    vi=sorted(li)
    sume=0
    for i in range(len(vi)):
        sume+=(2*(vi[n-(i+1)]**(i+1)))
    if sume<=5000000:
     print(sume)
    else:
        print("Too expensive")
