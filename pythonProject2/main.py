for _ in range(int(input())):
    s=input()
    li=[]
    cnt=0
    for i in range(1,len(s)):

        if s.count(s[i])%2==0:
            if s.count(s[i-1])%2!=0:
             while len(li)!=9:
                li.append(s[i:])
                cnt+=1

    if cnt==0:
     while len(li)!=9:
        li.append(s)
    m=''.join(li)
    print(m[:8])



