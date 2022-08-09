n=int(input())
s=input()
sume=int(s,2)
ans=0
for i in range(sume):
    if sume%(2**i)==0:
        ans=i
print(ans)