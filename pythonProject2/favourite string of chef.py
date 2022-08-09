for _ in range(int(input())):
    n=int(input())
    s=input()
    cnt=0
    for i in range(n):
        if s[i:i+4]=="code":
            if ("chef" in s[i+4:]) and ("chef" not in s[:i]):
                cnt+=1
    if cnt!=0:
        print("AC")
    else:
        print("WA")