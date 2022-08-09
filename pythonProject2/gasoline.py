for _  in range(int(input())):
    N=int(input())
    fi=list(map(int,input().split()))
    gas=fi[0]
    distance=0
    for i in range(1,N):
        if gas==0:
            break
        gas+=fi[i]-1
        distance+=1
    print(distance+gas)




