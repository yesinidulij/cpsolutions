N,T=map(int,input().split())
cnt=T
li=[]
ans=''
for i in range(N):
    potions=int(input())
    li.append(potions)
for i in range(1,N):
   if li[i-1]>li[i]:
        ans="NO"
        break
else:
    ans="YES"
print(ans)
