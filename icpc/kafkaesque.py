cnt=1
li=[]
for i in range(int(input())):
    n=int(input())
    li.append(n)

for i in range(1,len(li)):
    if li[i]<li[i-1]:
        cnt+=1
print(cnt)