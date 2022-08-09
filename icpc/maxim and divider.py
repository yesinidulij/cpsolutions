from math import  sqrt
t=int(input())
for _ in range(t):
    count=0
    n=int(input())
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            if '7' in str(i) or "4" in str(i):
                count+=1
            if ('7' in str(n//i) or "4" in str(n//i)) and i!=n//i:
                count+=1
    print(count)