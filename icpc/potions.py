N,T=map(int,input().split())
cnt=T
li=[]
for i in range(N):
    potions=int(input())
    li.append(potions)
for i in range(1,N):
    if li[i]==li[i-1]+T:
        print("YES")
        break
else:
    print("NO")
