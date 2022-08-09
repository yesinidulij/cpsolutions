# cook your dish here
t=int(input())
while(t>0):
    t-=1
    n=int(input())
    cnt=0
    for i in range(1,n+1,2):
        k=n+1-i
        cnt+=k**2
    print(cnt)