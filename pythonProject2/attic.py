for _ in range(int(input())):
    p=input()
    cnt=0
    sume=0
    for i in p:
        if i=='.':
            cnt+=1
        else:
            cnt=0
