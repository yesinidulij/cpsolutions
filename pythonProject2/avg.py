
l=[]
A=[]
sum=0
n=int(input())
def fun(l):
    avg=0
    for i in range(n):
        cc = 0
        for j in range(n):

            if i!=j:
             avg+=((1/5)*(l[j]))*((4/5)**j)
             cc+=1
        if cc==(n-1):
         A.append(avg/(n-1))
for i in range(n):
    s=int(input())
    l.append(s)
for i in range(n):
    sum+=(1/5)*(l[i]*(4/5)**i)
    v=fun(l)
print(sum)
c = 0
for i in range(n):
    c=c+A[i]
print(c/n)
