s=input()
cnt=0
sum=0
for i in range(len(s)):
        if s[i]=='O':
            if s[i-1]=='O':
                cnt+=1

            else:
                cnt=1
            sum += cnt
print(sum)

