n=input()
l=[]
l=n
flag=0

for i in range(len(n)):
    if i>0:
        if (l[i]=='s') and (l[i-1]=='s'):
            flag+=1
if flag==0:
    print("no hiss")

else:
    print("hiss")
