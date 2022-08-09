li=[]
mi=[]
while 1:
    n=input()
    if n=="-1":
        break
    li.append(tuple(map(str,n.split())))
li.sort(key=lambda x:x[1])
for i in li:
    mi.append(list(i))
penality=0
if li[0][2]=="wrong":
 penality+=20
sume=0
cnt=0
if li[0][2]=="right":
    sume+=int(li[0][0])
    cnt+=1
for i in range(1,len(mi)):
    if li[i][2]=="wrong":
        if li[i][1]!=li[i-1][1]:
            penality=0
        penality+=20
    else:
            sume += int(li[i][0])
            cnt+=1
            if li[i][1]!=li[i-1][1]:
                continue
            sume+=penality
print(cnt,sume)
