for _ in range(int(input())):
    n=int(input())
    li=[]
    for i in range(n):
        s=input()
        li.append(s)
    print("Begin on "+li[n-1][8:])
    for i in range(n-2,-1,-1):
        if (li[i][0]=="R" and li[i+1][0]=="L" ) or (li[i][0]=="B" and li[i+1][0]=="L" ) or (li[i][0]=="L" and li[i+1][0]=="L" ):
            print("Right on"+li[i][8:])
        elif (li[i][0]=="L" and li[i+1][0]=="R" ) or (li[i][0]=="B" and li[i+1][0]=="R" ) or (li[i][0]=="R" and li[i+1][0]=="R" ):
            print("Left on"+li[i][8:])
    print()

