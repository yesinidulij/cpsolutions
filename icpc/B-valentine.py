for _ in range(int(input())):
    n=int(input())
    b1=list(map(int,input().split()))
    g1=list(map(int,input().split()))
    if max(max(g1),max(b1)) in b1 and max(max(g1),max(b1)) in g1:
       print( max(max(g1),max(b1)) + min(min(b1),min(g1)))
    if max(max(g1),max(b1)) not in b1:
        print(max(g1)+min(b1))
    if max(max(g1),max(b1)) not in g1:
        print(max(b1)+min(g1))



