for _ in range(int(input())):
    s=input()
    cnt=0
    for i in range(len(s)):
        if s[i]=="C":
            if "E"in (s[:i]) or "S" in (s[:i]):
                cnt+=1
        elif s[i]=="E":
            if "S" in s[:i]:
             cnt+=1
    if cnt==0:
        print("YES")
    else:
        print("NO")

