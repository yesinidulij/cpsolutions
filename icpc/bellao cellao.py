def solve(D, d, P, Q):
    li = [P] * d
    for i in range(d, D):
        li.append(li[i - d] + Q)
    return sum(li)


for _ in range(int(input())):
    D, d, P, Q = map(int, input().split())
    print(solve(D, d, P, Q))













from math import log,sqrt
for _ in range(int(input())):
    s=input()
    li=[]
    m=sqrt(len(s))
    a=int(m)
    for i in range(a-1,-1,-1):
        li.append(s[i::a])
    print(''.join(li))

    # cook your dish here
    try:
        while 1:
            s = input()
            cnt = 1
            string = ""
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    cnt += 1
                else:
                    string+= str(cnt) + s[i - 1]
                    cnt = 1
            string += str(cnt) + s[len(s) - 1]
            print(string)
    except:
        pass







    n = int(input())
    li = []
    for _ in range(n):
        mex = 0
        sume = 0
        squaresum = 0
        m = int(input())
        li.append(m)
    for i in range(n):
        squaresum += li[i] ** 2
        sume = sum(li[i + 1:])
        mex
        if mex < (squaresum * sume):
            mex = squaresum * sume
    print(mex)
