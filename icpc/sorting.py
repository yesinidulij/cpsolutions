# cook your dish here
b = input()
li = list(map(str, b.split()))
n = int(input())
mi=[]
for i in range(n):
    string=input()
    mi.append(tuple(string.split()))
m = int(input())
for i in range(m):

    first = input()
    print(b)
    mi.sort(key=lambda x: x[li.index(first)])
    for j in mi:
        for i in j:
            print(i,end=" ")
        print()
    print("\n")


