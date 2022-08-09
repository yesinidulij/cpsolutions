for _ in range(int(input())):
    n=int(input())
    li=[1,2]
    mi=[]
    for i in range(2,n+1):
        li.append((li[(i-1)]^li[(i-2)]))
    for i in li:
        print(i,end=" ")
    print("\n")
