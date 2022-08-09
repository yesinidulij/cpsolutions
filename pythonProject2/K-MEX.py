for _ in range(int(input())):
    n,m,k=map(int,input().split())
    li=list(map(int,input().split()))
    matrix=[]
    mi=sorted(li)
    flag=0
    a=0
    if k in li:
     mi.remove(k)
    print(mi)
    if m>=k:
        if mi[0] > 0 and len(mi) >= m:
            if k==0:
                flag=1
        else:
         for i in range(1,len(mi)):

            if mi[i]-mi[i-1]>1:
               ab=mi[i-1] + 1
               if (k==ab and a==0) and len(mi)>=m:
                   flag=1
                   a+=1
               else:
                   flag=0
            if (mi[i] - mi[i - 1])==1 or (mi[i] - mi[i - 1])==0:
                if (k==max(mi)+1) and len(mi)>=m:
                    flag=1
                elif (k>(max(mi)+1)):
                    flag=0
    if flag==1:
        print("YES")
    else:
        print("NO")


