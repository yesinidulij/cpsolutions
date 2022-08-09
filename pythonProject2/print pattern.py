for _ in range(int(input())):
    li=[[1,2,4,7],
        [3,5,8,11],
        [6,9,12,14],
        [10,13,15,16]]
    n=int(input())

    matrix=[]
    for i in range(n):
        sm = []
        for j in range(n):
            sm.append(li[i][j])
        matrix.append(sm)
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=" ")
        print("\n")
