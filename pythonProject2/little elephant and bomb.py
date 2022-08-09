for _ in range(int(input())):
    n=int(input())
    s=input()
    cnt=0
    for i in range(n):
        if s[i]=='0':
         if i!=0 and i!=(n-1):
            if s[i-1]!='1' and s[i+1]!='1':
                cnt+=1
         else:
             if i==0:
                 if s[i+1]!='1':
                     cnt+=1
             else:
                 if s[i-1]!='1':
                     cnt+=1

    print(cnt)
