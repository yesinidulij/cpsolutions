n,k=map(int,input().split())
li=["0"]*n
cnt=0
for i in range(k):
    s=input()
    if "CLICK" in s:
       if li[int(s[len(s)-1])-1]=="0":
           cnt+=1
           li[int(s[len(s) - 1])-1]="1"
       else:
           cnt -= 1
           li[int(s[len(s) - 1])-1] = "0"
    else:
        li=["0"]*n
        cnt=0
    print(cnt)


