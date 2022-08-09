from math import ceil
n = int(input())

for i in range(n):
    m = input()
    s, d = [int(i) for i in m.split()]
    if s >= d:

        a = (s + d) // 2
        b =( s - a)
        m=a-b
        if m!=d:
            print("impossible")
        else:
         print(a,b)
    else:
        print("impossible")
