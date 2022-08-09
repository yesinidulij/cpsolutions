

def seive():
    array=[True]*10**5
    global count
    count=[]

    for i in range(2,10**5):
        if i*i>10**5:
            break
        if array[i]==True:
         for j in range(i*i,10**5,i):
             array[j]=False
    for j in range(5,10**5):
         if array[j]==array[j-2]==True:
             count.append((j-2,j))





for _ in range(int(input())):
    n=int(input())
    seive()
    print(count[n])
